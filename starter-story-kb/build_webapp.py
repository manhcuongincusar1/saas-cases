#!/usr/bin/env python3
"""Gom toàn bộ case + playbook thành một file JSON để nhúng vào webapp tĩnh.

Chạy: python3 build_webapp.py
Kết quả: web/data.json  (nguồn cho web/index.html)
"""
import base64
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(ROOT, "web")

# ---------------------------------------------------------------- frontmatter

SCALAR = re.compile(r"^([a-z_]+):\s*(.*)$")
NESTED = re.compile(r"^\s+([a-z_]+):\s*(.*)$")


def parse_front_matter(text):
    """YAML phẳng + một cấp lồng (key_metrics). Đủ cho định dạng của kho này."""
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, text
    data, current = {}, None
    for line in m.group(1).split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        nest = NESTED.match(line)
        if nest and current:
            data[current][nest.group(1)] = nest.group(2).strip()
            continue
        top = SCALAR.match(line)
        if not top:
            continue
        key, raw = top.group(1), top.group(2).strip()
        if raw == "":
            data[key] = {}
            current = key
        else:
            current = None
            if raw.startswith("[") and raw.endswith("]"):
                data[key] = [x.strip() for x in raw[1:-1].split(",") if x.strip()]
            else:
                data[key] = raw.strip('"').strip("'")
    return data, text[m.end():]


# ------------------------------------------------------------------- rewrites

SHOT = re.compile(r"^[ \t]*!\[[^\]]*\]\(screenshots/(\d+)_(\d+)m(\d+)s_([^)]*?)\.(?:jpg|png)\)[ \t]*$", re.M)
ANY_IMG = re.compile(r"^[ \t]*!\[[^\]]*\]\([^)]*\)[ \t]*$", re.M)
INLINE_SHOT = re.compile(r"\[([^\]]*)\]\(screenshots/\d+_(\d+)m(\d+)s_[^)]*\)")
ROOT_README = re.compile(r"\]\(\.\./\.\./README\.md\)")
CASE_LINK = re.compile(r"\]\(\.\./(?:videos/)?([^/)]+)/case\.md\)")
TRANSCRIPT_LINK = re.compile(r"\[([^\]]*)\]\(transcript\.md\)")
PLAYBOOK_LINK = re.compile(r"\]\((0[1-4]-[a-z-]+)\.md\)")
VIDEOS_README = re.compile(r"\]\((?:\.\./)?videos/README\.md\)")
PB_FROM_CASE = re.compile(r"\]\(\.\./\.\./playbooks/(0[1-4]-[a-z-]+)\.md\)")
SHOT_FOLDER_FRAG = re.compile(r"\s*·?\s*(?:Ảnh(?: chụp(?: màn hình)?)?:?\s*)?\[[^\]]*\]\(screenshots/\)")
TRANSCRIPT_FOOTER = re.compile(r"^- Transcript: .*$", re.M)


def html_attr(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def clean_shot_label(raw):
    label = raw.replace("-", " ").strip()
    label = re.sub(r"^ch ", "", label)
    label = re.sub(r"\busd\b", "$", label)
    label = re.sub(r"\s+", " ", label)
    # "$ 25 000" -> "$25.000" cho dễ đọc
    label = re.sub(r"\$\s*((?:\d+\s+)*\d+)",
                   lambda m: "$" + ".".join(m.group(1).split()), label)
    return label.strip()


def chapter_at(chapters, secs):
    """Tên chương chứa mốc thời gian này — để mốc đọc như một dòng mục lục."""
    found = ""
    for start, title in chapters or []:
        if start <= secs:
            found = title
        else:
            break
    return found


def rewrite_body(md, video_id=None, folder=None, chapters=None):
    """Ảnh -> link tua thẳng tới giây đó trong video. Link nội bộ -> route trong app."""

    def shot(m):
        idx, mm, ss, label = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        secs = mm * 60 + ss
        stamp = f"{mm:02d}:{ss:02d}"
        raw_label = clean_shot_label(label)
        # Ưu tiên tên chương: nói rõ mốc này dẫn tới phần nào của video
        text = chapter_at(chapters, secs) or raw_label
        if not video_id:
            return ""
        href = f"https://www.youtube.com/watch?v={video_id}&t={secs}s"
        hint = html_attr(raw_label) if raw_label and raw_label != text else ""
        title_attr = f' title="Trên màn hình: {hint}"' if hint else ""
        return (
            f'<p class="shot"><a href="{href}" target="_blank" rel="noopener"{title_attr}>'
            f'<span class="shot-play">▶</span><span class="shot-time">{stamp}</span>'
            f'<span class="shot-label">{text}</span></a></p>'
        )

    md = SHOT.sub(shot, md)
    md = TRANSCRIPT_FOOTER.sub("", md)
    if video_id:
        md = INLINE_SHOT.sub(
            lambda m: f"[{m.group(1)}](https://www.youtube.com/watch?v={video_id}"
                      f"&t={int(m.group(2))*60+int(m.group(3))}s)", md)
    md = ROOT_README.sub("](#/about)", md)
    md = SHOT_FOLDER_FRAG.sub("", md)
    md = PB_FROM_CASE.sub(lambda m: f"](#/playbook/{m.group(1)})", md)
    md = ANY_IMG.sub("", md)  # ảnh không theo quy ước -> bỏ
    md = CASE_LINK.sub(lambda m: f"](#/case/{m.group(1)})", md)
    md = PLAYBOOK_LINK.sub(lambda m: f"](#/playbook/{m.group(1)})", md)
    md = VIDEOS_README.sub("](#/library)", md)
    if video_id:
        md = TRANSCRIPT_LINK.sub(
            lambda m: f"[{m.group(1)}](https://www.youtube.com/watch?v={video_id})", md
        )
    else:
        md = TRANSCRIPT_LINK.sub(lambda m: m.group(1), md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


# ---------------------------------------------------------------- phân nhóm

GROUP_RULES = [
    ("Mobile app", ("mobile-app", "ios-app", "app-store", "mobile-subscription")),
    ("Khoá học · cộng đồng", ("course", "info-product", "coaching", "cohort", "community",
                              "membership", "education", "bootcamp", "workshop")),
    ("Creator · nội dung", ("creator", "newsletter", "youtube", "podcast", "media", "adsense",
                            "affiliate", "writing", "author", "book", "content", "blog",
                            "ghostwriting", "audience")),
    ("Dịch vụ · agency", ("service", "agency", "consult", "advisory", "freelance", "done-for-you",
                          "brokerage", "recruit", "studio")),
    ("Thương mại điện tử", ("ecommerce", "dtc", "physical", "apparel", "merch", "print-on-demand",
                            "retail", "supplement", "beverage", "hardware", "amazon")),
    ("Marketplace · nền tảng", ("marketplace", "directory", "job-board", "listing", "aggregator",
                                "network")),
    ("SaaS", ("saas", "software", "extension", "plugin", "api", "tool", "app-subscription",
              "wrapper", "micro", "open-core", "b2c-usage-based", "usage-based")),
    ("Sản phẩm số", ("digital-product", "template", "notion", "preset", "ebook", "asset-pack")),
    ("Đầu tư · thâu tóm", ("acquisition", "holding", "investment", "portfolio-acquisition",
                           "vc", "fund", "real-estate", "flipping")),
]


def group_of(model, category):
    hay = f"{model} {category}".lower()
    for name, needles in GROUP_RULES:
        if any(n in hay for n in needles):
            return name
    return "Khác"


def rev_tier(v):
    if v is None:
        return None
    if v < 10_000:
        return 0
    if v < 50_000:
        return 1
    if v < 200_000:
        return 2
    if v < 1_000_000:
        return 3
    return 4


def to_int(x):
    if x is None:
        return None
    s = re.sub(r"[^\d]", "", str(x))
    return int(s) if s else None


# --------------------------------------------------------------------- build

def load_meta(folder):
    """Chapters + thời lượng + tiêu đề gốc từ meta.json của yt-dlp."""
    path = os.path.join(ROOT, "videos", folder, "meta.json")
    if not os.path.exists(path):
        return [], 0, ""
    try:
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
    except (ValueError, OSError):
        return [], 0, ""
    chaps = []
    for ch in (d.get("chapters") or []):
        title = (ch.get("title") or "").strip()
        if title:
            chaps.append([int(ch.get("start") or 0), title])
    return chaps, int(d.get("duration") or 0), (d.get("title") or "").strip()


def load_thumb(video_id):
    """Thumbnail YouTube đã nén sẵn (160x90 webp) -> data URI, để nhúng thẳng vào trang.
    Artifact chặn ảnh từ host ngoài, và nhúng vào thì đọc offline vẫn thấy ảnh."""
    if not video_id:
        return ""
    path = os.path.join(ROOT, "_raw", "thumbs", video_id + ".webp")
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as fh:
        return "data:image/webp;base64," + base64.b64encode(fh.read()).decode("ascii")


def src_path(base_dir, stem, lang):
    """Bản dịch nếu có, không thì rơi về bản gốc tiếng Việt."""
    if lang != "vi":
        p = os.path.join(base_dir, f"{stem}.{lang}.md")
        if os.path.exists(p):
            return p, True
    p = os.path.join(base_dir, f"{stem}.md")
    return (p, False) if os.path.exists(p) else (None, False)


def build(lang="vi"):
    cases = []
    missing = 0
    video_dirs = sorted(
        d for d in os.listdir(os.path.join(ROOT, "videos"))
        if os.path.isdir(os.path.join(ROOT, "videos", d))
    )

    for folder in video_dirs:
        path, translated = src_path(os.path.join(ROOT, "videos", folder), "case", lang)
        if not path:
            continue
        if lang != "vi" and not translated:
            missing += 1
        with open(path, encoding="utf-8") as fh:
            raw = fh.read()
        fm, body = parse_front_matter(raw)
        if not fm:
            print(f"  bỏ qua (không có frontmatter): {folder}", file=sys.stderr)
            continue
        if lang != "vi" and translated:
            with open(os.path.join(ROOT, "videos", folder, "case.md"), encoding="utf-8") as fh:
                vi_fm, _ = parse_front_matter(fh.read())
            for k in ("id", "slug", "model", "category", "tags", "video_url", "published",
                      "views", "revenue_usd_month", "replicability_vn", "difficulty",
                      "opex_usd_month", "tech_stack"):
                if k in vi_fm:
                    fm[k] = vi_fm[k]

        vid = fm.get("id", "")
        chapters, duration, vtitle = load_meta(folder)
        # Bỏ H1 đầu tiên — tiêu đề đã hiển thị ở header của app
        body = re.sub(r"^\s*#\s+.*\n", "", body, count=1)
        body = rewrite_body(body, video_id=vid, folder=folder, chapters=chapters)

        rev = to_int(fm.get("revenue_usd_month"))
        model = fm.get("model", "")
        category = fm.get("category", "")
        km = fm.get("key_metrics") if isinstance(fm.get("key_metrics"), dict) else {}
        stack = fm.get("tech_stack") if isinstance(fm.get("tech_stack"), list) else []
        tags = fm.get("tags") if isinstance(fm.get("tags"), list) else []

        thumb = load_thumb(vid)
        n_shots = len(re.findall(r'class="shot"', body))
        words = len(re.findall(r"\S+", body))

        cases.append({
            "f": folder,
            "id": vid,
            "t": fm.get("product", folder),
            "tl": fm.get("tagline", ""),
            "fo": fm.get("founder", ""),
            "r": rev,
            "rb": fm.get("revenue_basis", ""),
            "m": model,
            "c": category,
            "g": group_of(model, category),
            "au": fm.get("audience", ""),
            "ch": fm.get("main_channel", ""),
            "st": fm.get("started", ""),
            "t1": fm.get("time_to_first_sale", ""),
            "t2": fm.get("time_to_scale", ""),
            "tm": fm.get("team_size", ""),
            "fu": fm.get("funding", ""),
            "vn": to_int(fm.get("replicability_vn")) or 0,
            "d": to_int(fm.get("difficulty")) or 0,
            "p": fm.get("published", ""),
            "v": to_int(fm.get("views")) or 0,
            "tags": tags,
            "stack": stack,
            "km": km,
            "th": thumb,
            "ch2": chapters,
            "dur": duration,
            "vt": vtitle,
            "shots": n_shots,
            "w": words,
            "body": body,
        })

    playbooks = []
    pb_dir = os.path.join(ROOT, "playbooks")
    slugs = sorted({fn[:-3].split(".")[0] for fn in os.listdir(pb_dir) if fn.endswith(".md")})
    for slug in slugs:
        path, _ = src_path(pb_dir, slug, lang)
        if not path:
            continue
        with open(path, encoding="utf-8") as fh:
            md = fh.read()
        md = re.sub(r"^\s*#\s+.*\n", "", md, count=1)
        playbooks.append({
            "slug": slug,
            "w": len(re.findall(r"\S+", md)),
            "body": rewrite_body(md),
        })

    data = {
        "built": "2026-09-04",
        "lang": lang,
        "cases": cases,
        "playbooks": playbooks,
    }

    out_dir = os.path.join(OUT_DIR, lang)
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "data.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, separators=(",", ":"))

    size = os.path.getsize(out)
    print(f"[{lang}] {len(cases)} case · {len(playbooks)} playbook → "
          f"{os.path.relpath(out, ROOT)} ({size/1e6:.2f} MB)"
          + (f"  ⚠ {missing} case chưa dịch, dùng bản tiếng Việt" if missing else ""))


def all_langs():
    with open(os.path.join(OUT_DIR, "i18n.json"), encoding="utf-8") as fh:
        return list(json.load(fh).keys())


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--all" in args:
        for lg in all_langs():
            build(lg)
    elif "--lang" in args:
        build(args[args.index("--lang") + 1])
    else:
        build("vi")
