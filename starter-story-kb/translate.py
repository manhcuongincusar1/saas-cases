#!/usr/bin/env python3
"""Dịch toàn bộ case + playbook sang các ngôn ngữ khác qua Batch API của Claude.

MIỄN PHÍ (LiteLLM router — Gemini/Mistral free tier, xem BẢNG PROVIDER bên dưới):

    python3 translate.py run en --limit 3           # chạy thử 3 case
    python3 translate.py run zh-Hans hi             # Gemini lo CJK + Ấn ngữ
    python3 translate.py run en es id --via mistral # Mistral lo tiếng châu Âu

TRẢ PHÍ (Anthropic Batch API — chất lượng cao nhất, ~$20/ngôn ngữ):

    python3 translate.py submit en zh-Hans          # gửi batch, in ra batch id
    python3 translate.py status                     # xem các batch đang chạy
    python3 translate.py fetch                      # tải kết quả về đĩa

Kết quả ghi ra: videos/<folder>/case.<lang>.md  và  playbooks/<file>.<lang>.md

Ba nguyên tắc của script này:
  1. KHÔNG tin model với dữ liệu máy. Mọi trường frontmatter điều khiển bộ lọc
     (id, slug, model, category, tags, số liệu, ngày) đều được ÁP LẠI từ bản gốc
     sau khi dịch xong — model có bịa cũng không ảnh hưởng.
  2. KHÔNG dịch đường dẫn. Link `../folder/case.md` và ảnh `screenshots/...` giữ
     nguyên byte, vì build_webapp.py còn phải rewrite chúng.
  3. Chạy lại được. File đã dịch thì bỏ qua, batch lưu vào .translate_state.json.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(ROOT, ".translate_state.json")
MODEL = "claude-opus-5"

# Đường miễn phí: LiteLLM gọi các provider còn free tier thật (kiểm tra 09/2026).
# Mỗi mục là chuỗi model của LiteLLM + fallback khi dính rate limit.
# Nút thắt là TOKEN/NGÀY chứ không phải số request — việc này cần ~18 triệu token.
PROVIDERS = {
    # Gemini AI Studio: context 1M, đa ngữ tốt nhất trong nhóm free.
    # Hạn mức thật xem ở aistudio.google.com/rate-limit (250–1500 req/ngày tuỳ model).
    "gemini": {
        "model": "gemini/gemini-3-flash",
        "fallbacks": ["gemini/gemini-2.5-flash", "mistral/mistral-large-latest"],
        "env": "GEMINI_API_KEY",
        "rpm": 10,
    },
    # Mistral Experiment: 1 req/s, 500K token/phút, 1 TỈ token/tháng.
    "mistral": {
        "model": "mistral/mistral-large-latest",
        "fallbacks": ["mistral/mistral-small-latest"],
        "env": "MISTRAL_API_KEY",
        "rpm": 55,
    },
    # OpenRouter: 20 req/phút, 50/ngày khi chưa nạp (1000/ngày sau khi nạp $10 một lần).
    "openrouter": {
        "model": "openrouter/deepseek/deepseek-chat-v3.1:free",
        "fallbacks": ["openrouter/qwen/qwen3-235b-a22b:free"],
        "env": "OPENROUTER_API_KEY",
        "rpm": 18,
    },
}
DEFAULT_PROVIDER = "gemini"

LANGS = {
    "en":      "English",
    "zh-Hans": "Simplified Chinese (简体中文, mainland conventions)",
    "zh-Hant": "Traditional Chinese (繁體中文, Taiwan conventions — 軟體/網路/影片, not mainland terms)",
    "hi":      "Hindi (हिन्दी)",
    "id":      "Bahasa Indonesia",
    "es":      "Spanish (español, neutral Latin American)",
}

# Trường frontmatter do máy dùng — luôn lấy lại từ bản gốc, không nhận từ model
MACHINE_FIELDS = {
    "id", "slug", "model", "category", "tags", "video_url", "published", "views",
    "revenue_usd_month", "replicability_vn", "difficulty", "opex_usd_month",
    "startup_cost_usd", "revenue_total_usd", "tech_stack",
}

SYSTEM = """You translate a Vietnamese knowledge base of indie-hacker case studies into {lang}.

The source is analysis written for Vietnamese readers. Your output is one edition of a
reference book that indie hackers worldwide read to extract MECHANISM — how founders found
an idea, validated it, and reached customers.

## Rules

1. **Translate meaning, not words.** The register is direct, concrete, unsentimental.
   Keep it that way. Do not add hedging, encouragement, or filler the source does not have.

2. **Preserve the markdown structure exactly.** Same headings, same heading levels, same
   table columns, same blockquotes, same bold/italic emphasis, same list nesting, same
   horizontal rules, same emoji, same ⭐ markers.

3. **Never touch these — copy them byte for byte:**
   - Link targets: `](../any-folder-name/case.md)`, `](transcript.md)`, URLs
   - Image paths: `![](screenshots/02_01m08s_usd-25-000.jpg)`
   - Raw HTML blocks such as `<p class="shot">...</p>`
   - YAML frontmatter KEYS (left of the colon)
   - Numbers, currency amounts, dates, product names, company names, person names,
     tech stack names, and YouTube video titles

4. **Frontmatter:** translate only human-readable descriptions — `tagline`, `founder`,
   `audience`, `main_channel`, `started`, `time_to_first_sale`, `time_to_scale`,
   `team_size`, `funding`, `revenue_basis`, and the values under `key_metrics`.
   Leave `product` as-is unless it is a Vietnamese description rather than a brand name.
   Leave every other field exactly as written.

5. **The localization section — this is the one place you EDIT, not translate.**
   The source has a section titled "Áp dụng cho tôi (indie hacker VN)" (the number varies).
   It mixes universal judgment with Vietnam-specific commentary. For this edition:
   - **Remove** anything specific to Vietnam: low Vietnamese ARPU, receiving international
     payments from Vietnam, Vietnamese legal or tax constraints, Vietnamese-language
     markets, "lợi thế riêng của VN", comparisons to Vietnamese salaries or costs.
   - **Keep** what applies to any indie hacker anywhere: what is genuinely copyable, the
     real barriers to execution, skills and assets the founder already had, and above all
     the "Khi nào KHÔNG nên dùng mô hình này" part — when NOT to copy this model. That
     part is the most valuable in the section; never drop it.
   - **Retitle** the section neutrally, keeping its number, e.g. "## 9. Applying this yourself".
   - If removing the Vietnam material leaves a subsection empty, drop that subsection.

6. **Keep the source-bias section** ("Cảnh báo thiên kiến nguồn") in full — it warns the
   reader that this channel only interviews winners. That applies to every reader.

Output the translated markdown file and nothing else. No preamble, no code fences around
the whole document, no notes about what you changed."""


# ------------------------------------------------------------------ frontmatter

def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def parse_flat(fm_text):
    """Đọc frontmatter thành list (indent, key, raw) để áp lại đúng thứ tự."""
    out = []
    for line in fm_text.split("\n"):
        m = re.match(r"^(\s*)([a-z_]+):(.*)$", line)
        out.append((m.group(1), m.group(2), m.group(3)) if m else (None, None, line))
    return out


def reimpose_machine_fields(translated, original):
    """Ghi đè mọi trường máy bằng giá trị gốc. Model bịa cũng không lọt được."""
    src_fm, _ = split_front_matter(original)
    out_fm, out_body = split_front_matter(translated)
    if not src_fm or not out_fm:
        return translated

    src = {}
    for indent, key, raw in parse_flat(src_fm):
        if key and not indent:
            src[key] = raw

    lines = []
    for indent, key, raw in parse_flat(out_fm):
        if key and not indent and key in MACHINE_FIELDS and key in src:
            lines.append(f"{key}:{src[key]}")
        elif key is not None:
            lines.append(f"{indent}{key}:{raw}")
        else:
            lines.append(raw)

    # Trường máy bị model làm rơi hẳn -> thêm lại
    present = {k for i, k, r in parse_flat("\n".join(lines)) if k and not i}
    for key in MACHINE_FIELDS:
        if key in src and key not in present:
            lines.append(f"{key}:{src[key]}")

    return "---\n" + "\n".join(lines) + "\n---\n" + out_body


# ------------------------------------------------------------------ công việc

def jobs(limit=None):
    """Danh sách file nguồn cần dịch."""
    items = []
    for folder in sorted(os.listdir(os.path.join(ROOT, "videos"))):
        p = os.path.join(ROOT, "videos", folder, "case.md")
        if os.path.exists(p):
            items.append(("case", folder, p))
    for fn in sorted(os.listdir(os.path.join(ROOT, "playbooks"))):
        if fn.endswith(".md") and "." not in fn[:-3]:
            items.append(("playbook", fn[:-3], os.path.join(ROOT, "playbooks", fn)))
    return items[:limit] if limit else items


def out_path(kind, name, lang):
    if kind == "case":
        return os.path.join(ROOT, "videos", name, f"case.{lang}.md")
    return os.path.join(ROOT, "playbooks", f"{name}.{lang}.md")


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


# ------------------------------------------------------------------ lệnh

def cmd_submit(langs, limit=None):
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    cl = client()
    state = load_state()
    todo = jobs(limit)

    for lang in langs:
        if lang not in LANGS:
            sys.exit(f"Ngôn ngữ chưa khai báo: {lang}. Có: {', '.join(LANGS)}")

        requests = []
        for kind, name, path in todo:
            if os.path.exists(out_path(kind, name, lang)):
                continue  # đã dịch rồi
            with open(path, encoding="utf-8") as fh:
                src = fh.read()
            requests.append(Request(
                custom_id=f"{lang}|{kind}|{name}"[:64],
                params=MessageCreateParamsNonStreaming(
                    model=MODEL,
                    max_tokens=32000,
                    system=[{
                        "type": "text",
                        "text": SYSTEM.format(lang=LANGS[lang]),
                        "cache_control": {"type": "ephemeral"},
                    }],
                    output_config={"effort": "low"},
                    messages=[{"role": "user", "content": src}],
                ),
            ))

        if not requests:
            print(f"{lang}: không còn gì để dịch")
            continue

        batch = cl.messages.batches.create(requests=requests)
        state["batches"].append({"id": batch.id, "lang": lang, "n": len(requests)})
        save_state(state)
        print(f"{lang}: đã gửi {len(requests)} request → {batch.id}")

    print(f"\nTheo dõi: python3 {os.path.basename(__file__)} status")


def cmd_status():
    cl = client()
    state = load_state()
    if not state["batches"]:
        return print("Chưa gửi batch nào.")
    for b in state["batches"]:
        r = cl.messages.batches.retrieve(b["id"])
        c = r.request_counts
        print(f"{b['lang']:8} {b['id']}  {r.processing_status:12} "
              f"xong {c.succeeded}/{b['n']}  lỗi {c.errored}  huỷ {c.canceled}")


def cmd_fetch():
    cl = client()
    state = load_state()
    written = errors = 0

    for b in state["batches"]:
        r = cl.messages.batches.retrieve(b["id"])
        if r.processing_status != "ended":
            print(f"{b['lang']}: {r.processing_status}, chưa lấy được")
            continue

        srcs = {f"{k}|{n}": p for k, n, p in jobs()}
        for res in cl.messages.batches.results(b["id"]):
            lang, kind, name = res.custom_id.split("|", 2)
            if res.result.type != "succeeded":
                print(f"  LỖI {res.custom_id}: {res.result.type}", file=sys.stderr)
                errors += 1
                continue
            text = "".join(bl.text for bl in res.result.message.content if bl.type == "text")
            with open(srcs[f"{kind}|{name}"], encoding="utf-8") as fh:
                original = fh.read()
            text = reimpose_machine_fields(text.strip() + "\n", original)
            dest = out_path(kind, name, lang)
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(text)
            written += 1

    print(f"Đã ghi {written} file, {errors} lỗi.")
    print("Tiếp theo: python3 build_webapp.py --all && python3 bundle_webapp.py --all")


def cmd_run(langs, provider, limit=None, workers=4):
    """Dịch tuần tự/song song qua LiteLLM. Ghi từng file ngay khi xong -> dừng giữa chừng
    rồi chạy lại cũng không mất gì."""
    try:
        import litellm
    except ImportError:
        sys.exit("Thiếu router. Chạy: pip install litellm")
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    cfg = PROVIDERS[provider]
    if not os.environ.get(cfg["env"]):
        sys.exit(f"Chưa có {cfg['env']}. export {cfg['env']}=...")
    litellm.suppress_debug_info = True

    gate = threading.Semaphore(workers)
    last = [0.0]
    tick = threading.Lock()
    gap = 60.0 / cfg["rpm"]

    def pace():
        with tick:
            wait = last[0] + gap - time.time()
            if wait > 0:
                time.sleep(wait)
            last[0] = time.time()

    def one(kind, name, path, lang):
        dest = out_path(kind, name, lang)
        if os.path.exists(dest):
            return None
        with open(path, encoding="utf-8") as fh:
            original = fh.read()
        for attempt in range(5):
            pace()
            try:
                with gate:
                    r = litellm.completion(
                        model=cfg["model"],
                        fallbacks=cfg["fallbacks"],
                        max_tokens=32000,
                        messages=[
                            {"role": "system", "content": SYSTEM.format(lang=LANGS[lang])},
                            {"role": "user", "content": original},
                        ],
                    )
                text = r.choices[0].message.content or ""
                if len(text) < len(original) * 0.3:
                    raise ValueError(f"bản dịch quá ngắn ({len(text)} / {len(original)} ký tự)")
                with open(dest, "w", encoding="utf-8") as fh:
                    fh.write(reimpose_machine_fields(text.strip() + "\n", original))
                return dest
            except Exception as e:
                if attempt == 4:
                    print(f"  LỖI {lang}/{name}: {e}", file=sys.stderr)
                    return False
                time.sleep(min(60, 4 * 2 ** attempt))

    todo = jobs(limit)
    for lang in langs:
        if lang not in LANGS:
            sys.exit(f"Ngôn ngữ chưa khai báo: {lang}. Có: {', '.join(LANGS)}")
        pending = [(k, n, p) for k, n, p in todo if not os.path.exists(out_path(k, n, lang))]
        if not pending:
            print(f"{lang}: không còn gì để dịch")
            continue
        print(f"{lang}: {len(pending)} file qua {cfg['model']} ({cfg['rpm']} req/phút)…")
        done = fail = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futs = {pool.submit(one, k, n, p, lang): n for k, n, p in pending}
            for f in as_completed(futs):
                r = f.result()
                if r is False:
                    fail += 1
                elif r:
                    done += 1
                    if done % 10 == 0 or done == len(pending):
                        print(f"    {done}/{len(pending)}")
        print(f"{lang}: xong {done}, lỗi {fail}")

    print(f"\nTiếp theo: python3 build_webapp.py --all && python3 bundle_webapp.py --all")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    limit = None
    provider = DEFAULT_PROVIDER
    if "--limit" in rest:
        i = rest.index("--limit")
        limit = int(rest[i + 1])
        rest = rest[:i] + rest[i + 2:]
    if "--via" in rest:
        i = rest.index("--via")
        provider = rest[i + 1]
        rest = rest[:i] + rest[i + 2:]
        if provider not in PROVIDERS:
            sys.exit(f"Provider lạ: {provider}. Có: {', '.join(PROVIDERS)}")

    if cmd == "run":
        cmd_run(rest or list(LANGS), provider, limit)
    elif cmd == "submit":
        cmd_submit(rest or list(LANGS), limit)
    elif cmd == "status":
        cmd_status()
    elif cmd == "fetch":
        cmd_fetch()
    else:
        sys.exit(__doc__)
