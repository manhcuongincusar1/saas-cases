#!/usr/bin/env python3
"""
Cắt transcript thành ĐOẠN gắn vào KHUNG (framework.md).

    python3 segment.py submit            # gửi batch cho mọi video chưa cắt
    python3 segment.py submit --limit 5  # thử 5 video trước
    python3 segment.py status            # xem batch chạy tới đâu
    python3 segment.py fetch             # lấy kết quả về data/segments/
    python3 segment.py report            # thống kê: nút nào được củng cố, đoạn nào chưa khớp

Nguyên tắc:
  1. Bộ mã nút lấy TRỰC TIẾP từ framework.md — sửa file đó là đổi được từ vựng,
     không phải sửa script.
  2. Đoạn không khớp nút nào thì gắn "?" kèm đề xuất tên nút mới. Đây là nguyên
     liệu để soạn chặng BUILD và SỐNG & LỚN, không phải lỗi.
  3. Bỏ đoạn quảng cáo (sponsor read) — mỗi video có 1-2 phút loại này.
  4. Chạy lại được: video đã có file kết quả thì bỏ qua.
"""
import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
VIDEOS = os.path.join(ROOT, "videos")
OUT = os.path.join(ROOT, "data", "segments")
STATE = os.path.join(ROOT, ".segment_state.json")
FRAMEWORK = os.path.join(ROOT, "framework.md")
MODEL = "claude-opus-5"

# ------------------------------------------------------------------ khung

def load_nodes():
    """Rút bộ mã nút từ framework.md — dòng bảng dạng | `2.7` | Tên | ..."""
    with open(FRAMEWORK, encoding="utf-8") as fh:
        text = fh.read()
    nodes = {}
    for code, name in re.findall(r"^\|\s*`([0-9]+\.[0-9A-Za-z]+)`\s*\|\s*([^|]+?)\s*\|", text, re.M):
        nodes[code] = re.sub(r"\*\*|\*", "", name).strip()
    if not nodes:
        sys.exit("Không đọc được nút nào từ framework.md — kiểm tra định dạng bảng.")
    return nodes, text


SYSTEM = """Bạn cắt transcript video Starter Story thành các ĐOẠN phục vụ một khung khởi nghiệp.

KHUNG (đây là toàn bộ từ vựng — chỉ được dùng mã trong đây, hoặc "?"):

{framework}

NHIỆM VỤ

Đọc transcript, tìm mọi đoạn NÓI ĐƯỢC MỘT ĐIỀU CỤ THỂ phục vụ khung. Với mỗi đoạn:

- `s`, `e`: mốc bắt đầu/kết thúc dạng MM:SS, lấy từ chính các mốc [MM:SS] trong transcript.
  Đoạn thường dài 30 giây tới 3 phút.
- `nut`: mảng mã nút khớp (vd ["2.7","3.7"]). Nếu đoạn hay nhưng KHÔNG nút nào khớp,
  dùng ["?"] và thêm trường `moi` = tên nút mới bạn đề xuất (một cụm danh từ ngắn tiếng Việt).
- `tom`: MỘT câu tiếng Việt nói đoạn đó chứa gì. Phải có CHI TIẾT CỤ THỂ — con số, tên
  công cụ, các bước thật. "Nói về marketing" là vô dụng; "10 TikTok/ngày trong 1 tháng rồi
  mới đổ ads" là dùng được. Người đọc câu này phải quyết định được có đáng nhảy vào xem không.
- `kq`: kết quả kèm theo nếu đoạn có nêu (vd "$30K/tháng", "biên ~90%", "thất bại, bỏ ý tưởng").
  Bỏ trống nếu không có.

QUY TẮC

1. BỎ QUA đoạn quảng cáo (sponsor read) và đoạn tự quảng bá Starter Story Build. Ghi chúng
   vào `bo_qua` kèm lý do. Mỗi video thường có 1-2 phút loại này, hay nằm ở giữa và cuối.
2. BỎ QUA phần chào hỏi, tiểu sử thuần tuý, lời cảm ơn — trừ khi chúng chứa một điều cụ thể
   dùng được (vd mốc thời gian thật, số tiền khởi đầu thật).
3. Đoạn THẤT BẠI cũng quý ngang đoạn thành công. Ghi rõ trong `kq`.
4. Đừng cố nhét đoạn vào nút cho đủ. "?" là câu trả lời đúng khi thật sự không khớp — và
   là thứ chúng tôi cần để mở rộng khung.
5. Một video thường ra 5-15 đoạn. Video không phục vụ khung (thương mại điện tử thuần,
   creator có sẵn triệu follower) có thể ra rất ít — đó là kết quả hợp lệ, đừng bịa thêm.
6. Viết `tom` và `moi` bằng tiếng Việt tự nhiên, không dịch máy.
"""

SCHEMA = {
    "type": "json_schema",
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "required": ["segments", "bo_qua"],
        "properties": {
            "segments": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["s", "e", "nut", "tom"],
                    "properties": {
                        "s": {"type": "string"},
                        "e": {"type": "string"},
                        "nut": {"type": "array", "items": {"type": "string"}},
                        "moi": {"type": "string"},
                        "tom": {"type": "string"},
                        "kq": {"type": "string"},
                    },
                },
            },
            "bo_qua": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["s", "e", "ly_do"],
                    "properties": {
                        "s": {"type": "string"},
                        "e": {"type": "string"},
                        "ly_do": {"type": "string"},
                    },
                },
            },
        },
    },
}

# ------------------------------------------------------------------ tiện ích

def jobs(limit=None):
    """(tên thư mục, đường dẫn transcript) cho video chưa có file kết quả."""
    out = []
    for name in sorted(os.listdir(VIDEOS)):
        src = os.path.join(VIDEOS, name, "transcript.md")
        if not os.path.isfile(src):
            continue
        if os.path.exists(os.path.join(OUT, name + ".json")):
            continue
        out.append((name, src))
    return out[:limit] if limit else out


def body(path):
    """Chỉ lấy phần transcript, bỏ frontmatter/mô tả/chương ở đầu."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    i = text.find("## Transcript")
    return text[i:] if i != -1 else text


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh)
    return {"batches": []}


def save_state(s):
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump(s, fh, ensure_ascii=False, indent=2)


def client():
    try:
        import anthropic
    except ImportError:
        sys.exit("Thiếu SDK. Chạy: pip install anthropic")
    return anthropic.Anthropic()


def vid_of(name):
    meta = os.path.join(VIDEOS, name, "meta.json")
    if os.path.exists(meta):
        with open(meta, encoding="utf-8") as fh:
            m = json.load(fh)
        return m.get("id") or m.get("video_id") or ""
    return ""

# ------------------------------------------------------------------ lệnh

def cmd_submit(limit, effort):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    _, framework = load_nodes()
    todo = jobs(limit)
    if not todo:
        return print("Không còn video nào để cắt.")

    requests = []
    for name, src in todo:
        requests.append(Request(
            custom_id=name[:64],
            params=MessageCreateParamsNonStreaming(
                model=MODEL,
                max_tokens=16000,
                system=[{
                    "type": "text",
                    "text": SYSTEM.format(framework=framework),
                    "cache_control": {"type": "ephemeral"},
                }],
                output_config={"effort": effort, "format": SCHEMA},
                messages=[{"role": "user", "content": body(src)}],
            ),
        ))

    cl = client()
    batch = cl.messages.batches.create(requests=requests)
    state = load_state()
    state["batches"].append({"id": batch.id, "n": len(requests)})
    save_state(state)
    print(f"Đã gửi {len(requests)} video → {batch.id}")
    print(f"Theo dõi: python3 {os.path.basename(__file__)} status")


def cmd_status():
    cl = client()
    state = load_state()
    if not state["batches"]:
        return print("Chưa gửi batch nào.")
    for b in state["batches"]:
        r = cl.messages.batches.retrieve(b["id"])
        c = r.request_counts
        print(f"{b['id']}  {r.processing_status:12} xong {c.succeeded}/{b['n']}  "
              f"lỗi {c.errored}  huỷ {c.canceled}")


def cmd_fetch():
    cl = client()
    state = load_state()
    os.makedirs(OUT, exist_ok=True)
    written = errors = 0

    for b in state["batches"]:
        r = cl.messages.batches.retrieve(b["id"])
        if r.processing_status != "ended":
            print(f"{b['id']}: {r.processing_status}, chưa lấy được")
            continue

        for res in cl.messages.batches.results(b["id"]):
            name = res.custom_id
            if res.result.type != "succeeded":
                print(f"  LỖI {name}: {res.result.type}", file=sys.stderr)
                errors += 1
                continue
            text = "".join(bl.text for bl in res.result.message.content if bl.type == "text")
            try:
                data = json.loads(text)
            except json.JSONDecodeError:
                m = re.search(r"\{.*\}", text, re.S)   # phòng khi model bọc trong ```json
                if not m:
                    print(f"  KHÔNG PARSE ĐƯỢC {name}", file=sys.stderr)
                    errors += 1
                    continue
                data = json.loads(m.group(0))

            data["f"] = name
            data["vid"] = vid_of(name)
            with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as fh:
                json.dump(data, fh, ensure_ascii=False, indent=1)
            written += 1

    print(f"Đã ghi {written} file vào {os.path.relpath(OUT, ROOT)}/  ({errors} lỗi)")


def cmd_report():
    nodes, _ = load_nodes()
    if not os.path.isdir(OUT):
        return print("Chưa có kết quả. Chạy submit → fetch trước.")

    hits = collections.Counter()
    moi = collections.Counter()
    total = files = skipped = 0

    for fn in sorted(os.listdir(OUT)):
        if not fn.endswith(".json"):
            continue
        with open(os.path.join(OUT, fn), encoding="utf-8") as fh:
            d = json.load(fh)
        files += 1
        skipped += len(d.get("bo_qua", []))
        for seg in d.get("segments", []):
            total += 1
            for n in seg.get("nut", []):
                if n == "?":
                    moi[seg.get("moi", "(không nêu tên)")] += 1
                else:
                    hits[n] += 1

    print(f"{files} video · {total} đoạn · {skipped} đoạn quảng cáo bị bỏ\n")
    print("SỨC NẶNG TỪNG NÚT (số đoạn chống lưng):")
    for code in sorted(nodes, key=lambda c: (-hits[c], c)):
        bar = "█" * min(hits[code], 40)
        print(f"  {code:6} {hits[code]:4}  {bar}  {nodes[code][:46]}")

    trong = [c for c in nodes if hits[c] == 0]
    if trong:
        print(f"\n⚠ {len(trong)} nút KHÔNG có đoạn nào chống lưng: {', '.join(sorted(trong))}")
        print("  → hoặc khung sai, hoặc kho thật sự không nói về nó. Cả hai đều đáng biết.")

    if moi:
        print(f"\nĐỀ XUẤT NÚT MỚI (nguyên liệu cho chặng BUILD và SỐNG & LỚN):")
        for name, n in moi.most_common(40):
            print(f"  {n:4}  {name}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["submit", "status", "fetch", "report"])
    ap.add_argument("--limit", type=int, help="chỉ xử lý N video đầu")
    ap.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    a = ap.parse_args()

    if a.cmd == "submit":
        cmd_submit(a.limit, a.effort)
    elif a.cmd == "status":
        cmd_status()
    elif a.cmd == "fetch":
        cmd_fetch()
    else:
        cmd_report()
