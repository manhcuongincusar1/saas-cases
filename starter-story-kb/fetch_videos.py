#!/usr/bin/env python3
"""Lấy video MỚI từ kênh Starter Story: metadata + transcript (auto-caption) + thumbnail nhỏ.
Ghi đúng vào chỗ reorganize.py cần: _raw/meta/, _raw/transcripts/, _raw/thumbs/.

    python3 fetch_videos.py new              # tự dò video mới trên kênh, tải hết
    python3 fetch_videos.py new --dry-run    # chỉ liệt kê video mới, không tải
    python3 fetch_videos.py <id> [<id> ...]  # tải đúng những video_id này (bỏ qua nếu đã có; --force để ghi đè)

Sau khi chạy xong:
    python3 reorganize.py          # gom vào videos/<ngày>_<slug>/
    (viết case.md cho video mới nếu muốn phân tích sâu — xem case.md bất kỳ để lấy khuôn)
    python3 build_index.py         # cập nhật index.md, videos/README.md, data/cases.csv
    python3 build_webapp.py --all && python3 bundle_webapp.py --all   # nếu có publish web/artifact.html

Cần có sẵn: yt-dlp, ffmpeg, cwebp (brew install webp), curl.

LƯU Ý: bước "chọn mốc chụp ảnh theo heatmap + chapter + câu nhắc $" rồi cắt ảnh bằng ffmpeg
KHÔNG nằm trong script này — heatmap most-replayed thường không có ở video mới đăng, và bước
tải file video 720p + cắt ảnh tốn thời gian/dung lượng hơn hẳn. Làm tay khi thực sự cần ảnh.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
META_DIR = os.path.join(ROOT, "_raw", "meta")
TRANSCRIPT_DIR = os.path.join(ROOT, "_raw", "transcripts")
THUMB_DIR = os.path.join(ROOT, "_raw", "thumbs")
CHANNEL_URL = "https://www.youtube.com/@starterstory/videos"

META_FIELDS = ['id', 'title', 'upload_date', 'duration', 'view_count', 'like_count',
               'comment_count', 'description', 'chapters', 'heatmap', 'thumbnail',
               'webpage_url', 'tags']

# ------------------------------------------------------------------ tiện ích


def run(cmd, retries=0, backoff=40):
    """Chạy lệnh; tự thử lại khi bị YouTube rate-limit (429)."""
    for attempt in range(retries + 1):
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout
        if "429" in r.stderr and attempt < retries:
            print(f"    bị rate-limit, chờ {backoff}s rồi thử lại ({attempt + 1}/{retries})...",
                  file=sys.stderr)
            time.sleep(backoff)
            continue
        print(r.stderr, file=sys.stderr)
        sys.exit(f"lệnh thất bại: {' '.join(cmd)}")


def fmt_date(d):
    return f'{d[6:8]}/{d[4:6]}/{d[0:4]}' if d and len(d) == 8 else '—'


def check_deps():
    missing = [b for b in ("yt-dlp", "ffmpeg", "cwebp", "curl") if not shutil_which(b)]
    if missing:
        sys.exit(f"Thiếu công cụ: {', '.join(missing)}. Cài rồi chạy lại "
                  f"(vd: brew install yt-dlp ffmpeg webp).")


def shutil_which(bin_name):
    import shutil
    return shutil.which(bin_name)


# ------------------------------------------------------------------ dò video mới


def existing_ids():
    if not os.path.isdir(META_DIR):
        return set()
    return {fn[:-5] for fn in os.listdir(META_DIR) if fn.endswith(".json")}


def channel_ids_newest_first():
    out = run(["yt-dlp", "--flat-playlist", "--print", "%(id)s", CHANNEL_URL], retries=2)
    return [line.strip() for line in out.splitlines() if line.strip()]


def find_new_ids():
    """Kênh liệt kê mới nhất trước — dừng ngay khi gặp video đã có trong _raw/meta/."""
    have = existing_ids()
    new = []
    for vid in channel_ids_newest_first():
        if vid in have:
            break
        new.append(vid)
    return list(reversed(new))  # trả về theo thứ tự đăng tăng dần


# ------------------------------------------------------------------ metadata


def fetch_meta(vid):
    out = run(["yt-dlp", "--dump-json", "--skip-download", f"https://www.youtube.com/watch?v={vid}"],
              retries=2)
    full = json.loads(out.strip().splitlines()[-1])
    m = {k: full.get(k) for k in META_FIELDS}
    m['chapters'] = [{'start': c['start_time'], 'end': c.get('end_time'), 'title': c['title']}
                      for c in (full.get('chapters') or [])]
    m['heatmap'] = full.get('heatmap') or []
    os.makedirs(META_DIR, exist_ok=True)
    with open(os.path.join(META_DIR, f"{vid}.json"), "w", encoding="utf-8") as fh:
        json.dump(m, fh, ensure_ascii=False, indent=2)
    return m


# ------------------------------------------------------------------ transcript


def fetch_subs_json3(vid, workdir):
    out_tpl = os.path.join(workdir, vid)
    run(["yt-dlp", "--write-auto-subs", "--sub-lang", "en", "--sub-format", "json3",
         "--skip-download", "-o", out_tpl, f"https://www.youtube.com/watch?v={vid}"],
        retries=6, backoff=40)
    p = out_tpl + ".en.json3"
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def events_to_lines(data, chunk_ms=15500):
    """Auto-caption json3 (đã tách dòng sẵn, không rolling-overlap) -> [(giây, text), ...]
    gộp mỗi dòng ~15 giây, giống định dạng transcript.md hiện có trong kho."""
    events = data.get("events", [])
    lines, buf, line_start = [], [], None

    def flush():
        if buf:
            text = re.sub(r"[ \t]+", " ", re.sub(r"\n+", " ", "".join(buf))).strip()
            if text:
                lines.append((line_start // 1000, text))

    for e in events:
        segs = e.get("segs")
        if not segs:
            continue
        text = "".join(s.get("utf8", "") for s in segs)
        if not text.strip():
            continue
        start = e.get("tStartMs", 0)
        if line_start is None:
            line_start = start
        if buf and start - line_start >= chunk_ms:
            flush()
            buf, line_start = [], start
        if buf and not buf[-1].endswith((" ", "\n")) and not text.startswith((" ", "\n")):
            buf.append(" ")
        buf.append(text)
    flush()
    return lines


def build_transcript_md(vid, m, lines):
    d = m.get('upload_date') or ''
    dur = m.get('duration') or 0
    desc = re.sub(r'\n{2,}', '\n', (m.get('description') or '').strip())
    ch = m.get('chapters') or []
    ch_md = '\n'.join(f"- `{c['start'] // 60:02d}:{c['start'] % 60:02d}` {c['title']}"
                       for c in ch) or '_(không có chapter)_'
    body = "\n".join(f"[{t // 60:02d}:{t % 60:02d}] {text}" for t, text in lines)

    return f"""# {m.get('title', '')}

| | |
|---|---|
| **Video** | <{m.get('webpage_url', f'https://www.youtube.com/watch?v={vid}')}> |
| **Kênh** | Starter Story |
| **Đăng** | {fmt_date(d)} |
| **Thời lượng** | {dur // 60}:{dur % 60:02d} |
| **Lượt xem** | {(m.get('view_count') or 0):,} |
| **Video ID** | `{vid}` |

## Mô tả gốc

{desc}

## Chương

{ch_md}

---

## Transcript (auto-caption YouTube, gộp ~15 giây/dòng)

{body}
"""


# ------------------------------------------------------------------ thumbnail nhỏ (cho webapp)


def fetch_thumb(vid, workdir):
    """Ảnh nhỏ 160x90 webp để nhúng vào web/data.json — KHÔNG phải screenshot trong video."""
    os.makedirs(THUMB_DIR, exist_ok=True)
    src = os.path.join(workdir, f"{vid}_thumb_src.webp")
    png = os.path.join(workdir, f"{vid}_thumb.png")
    dst = os.path.join(THUMB_DIR, f"{vid}.webp")
    try:
        subprocess.run(["curl", "-sL", f"https://i.ytimg.com/vi_webp/{vid}/mqdefault.webp",
                         "-o", src], check=True, capture_output=True)
        subprocess.run(["ffmpeg", "-y", "-i", src, "-vf", "scale=160:90", "-loglevel", "error", png],
                        check=True, capture_output=True)
        subprocess.run(["cwebp", "-quiet", png, "-o", dst], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"    ⚠ không lấy được thumbnail cho {vid}: {e}", file=sys.stderr)
        return False


# ------------------------------------------------------------------ orchestrate


def fetch_one(vid, workdir, force):
    print(f"== {vid} ==")
    meta_path = os.path.join(META_DIR, f"{vid}.json")
    if os.path.exists(meta_path) and not force:
        print("  đã có sẵn, bỏ qua (--force để tải lại)")
        return

    m = fetch_meta(vid)
    print(f"  meta: {m.get('title', '')[:70]}  ({fmt_date(m.get('upload_date'))})")

    data = fetch_subs_json3(vid, workdir)
    if data is None:
        print(f"  ⚠ không có auto-caption tiếng Anh cho {vid} — video sẽ không có transcript.md")
    else:
        lines = events_to_lines(data)
        md = build_transcript_md(vid, m, lines)
        os.makedirs(TRANSCRIPT_DIR, exist_ok=True)
        with open(os.path.join(TRANSCRIPT_DIR, f"{vid}.md"), "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"  transcript: {len(lines)} dòng -> _raw/transcripts/{vid}.md")

    if fetch_thumb(vid, workdir):
        print(f"  thumbnail: _raw/thumbs/{vid}.webp")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ids", nargs="+", help="'new' để tự dò video mới trên kênh, hoặc 1+ video ID cụ thể")
    ap.add_argument("--dry-run", action="store_true", help="chỉ liệt kê, không tải gì")
    ap.add_argument("--force", action="store_true", help="tải lại kể cả video đã có sẵn")
    a = ap.parse_args()
    check_deps()

    if a.ids == ["new"]:
        print("Đang dò video mới trên kênh Starter Story...")
        todo = find_new_ids()
        if not todo:
            return print("Không có video mới.")
        print(f"Tìm thấy {len(todo)} video mới: {', '.join(todo)}")
    else:
        todo = a.ids

    if a.dry_run:
        return

    with tempfile.TemporaryDirectory(prefix="starter-story-fetch-") as workdir:
        for vid in todo:
            fetch_one(vid, workdir, a.force)

    print(f"\n✅ Xong {len(todo)} video. Bước tiếp theo:")
    print("  python3 reorganize.py")
    print("  # viết case.md cho video mới nếu muốn phân tích sâu (xem case.md bất kỳ để lấy khuôn)")
    print("  python3 build_index.py")
    print("  python3 build_webapp.py --all && python3 bundle_webapp.py --all   # nếu có publish webapp")


if __name__ == "__main__":
    main()
