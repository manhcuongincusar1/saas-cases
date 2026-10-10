#!/usr/bin/env python3
"""Gom mọi thứ của MỘT video vào MỘT thư mục: videos/<ngày>_<slug>/
   - README.md      : tóm tắt, link video, chapters, số liệu bắt được, danh sách ảnh
   - transcript.md  : transcript gốc
   - case.md        : phân tích sâu (nếu đã viết)
   - meta.json      : metadata gốc
   - screenshots/   : ảnh
Chạy lại được nhiều lần (idempotent).
"""
import os, re, json, glob, shutil

KB = os.path.dirname(os.path.abspath(__file__))
VID = f'{KB}/videos'

MONEY = re.compile(r'\$\s?\d[\d,]*(?:\.\d+)?\s?(?:k|m|million|thousand)?(?:\s?(?:/|per\s)\s?(?:mo|month|year|yr|week|day))?', re.I)
METRIC = re.compile(r'\b\d[\d,]*\s?(?:k|m)?\s+(?:users?|downloads?|customers?|subscribers?|installs?|followers?|views?)\b', re.I)

def slug(s, n=52):
    s = re.sub(r"['’]", '', s.lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:n].rstrip('-') or 'video'

def fmt_date(d):
    return f'{d[6:8]}/{d[4:6]}/{d[0:4]}' if d and len(d) == 8 else '—'

def parse_transcript(path):
    """-> (danh sách (giây, text), phần thân gốc)"""
    if not os.path.exists(path):
        return [], None
    txt = open(path, encoding='utf-8').read()
    body = txt.split('## Transcript', 1)[-1]
    body = body.split('\n', 2)[-1] if body.startswith('(') or '\n' in body else body
    rows = []
    for line in txt.splitlines():
        m = re.match(r'\[(\d+):(\d+)\]\s*(.*)', line)
        if m:
            rows.append((int(m[1]) * 60 + int(m[2]), m[3]))
    return rows, txt

def key_numbers(rows, limit=8):
    """Trích các dòng transcript có nêu con số — để lướt nhanh mà không cần đọc hết."""
    hits = []
    for t, txt in rows:
        money = MONEY.findall(txt)
        metric = METRIC.findall(txt)
        if not money and not metric:
            continue
        score = len(money) * 2 + len(metric)
        if re.search(r'\b(revenue|mrr|arr|month|profit|made|makes|paying)\b', txt, re.I):
            score += 2
        # câu chứa con số, cắt gọn quanh chỗ nhắc tiền
        snippet = re.sub(r'\s+', ' ', txt).strip()
        if len(snippet) > 260:
            pos = snippet.find((money or metric)[0])
            snippet = ('…' if pos > 60 else '') + snippet[max(0, pos - 60):pos + 200] + '…'
        hits.append((score, t, snippet))
    hits.sort(key=lambda x: -x[0])
    picked, seen = [], set()
    for score, t, s in hits:
        if any(abs(t - p[0]) < 25 for p in picked):
            continue
        if s[:70] in seen:
            continue
        seen.add(s[:70]); picked.append((t, s))
        if len(picked) >= limit:
            break
    return sorted(picked)

def legacy_case(vid):
    """Chỉ dùng cho lần migrate đầu: tìm case trong cases/ cũ (thư mục này đã bỏ)."""
    for p in glob.glob(f'{KB}/cases/*.md'):
        head = open(p, encoding='utf-8').read(400)
        if re.search(rf'^id:\s*{re.escape(vid)}\s*$', head, re.M):
            return p
    return None

def folder_name(m, vid, used):
    d = m.get('upload_date') or ''
    base = f"{d[0:4]}-{d[4:6]}-{d[6:8]}_{slug(m.get('title',''))}" if len(d) == 8 else slug(m.get('title', vid))
    return base if base not in used else f'{base}_{vid[:6]}'

def main():
    os.makedirs(VID, exist_ok=True)
    metas = sorted(glob.glob(f'{KB}/_raw/meta/*.json'))

    # lượt 1: chốt tên thư mục cho từng video + map slug-case -> thư mục
    used, folders, slug2folder = set(), {}, {}
    for mp in metas:
        vid = os.path.basename(mp)[:-5]
        m = json.load(open(mp, encoding='utf-8'))
        f = folder_name(m, vid, used); used.add(f); folders[vid] = f
        cp = legacy_case(vid)
        if cp:
            slug2folder[os.path.basename(cp)[:-3]] = f

    made, with_case = 0, 0

    for mp in metas:
        vid = os.path.basename(mp)[:-5]
        m = json.load(open(mp, encoding='utf-8'))
        d = m.get('upload_date') or ''
        folder = folders[vid]
        out = f'{VID}/{folder}'
        os.makedirs(f'{out}/screenshots', exist_ok=True)

        # 1) meta
        shutil.copyfile(mp, f'{out}/meta.json')

        # 2) transcript
        src_tr = f'{KB}/_raw/transcripts/{vid}.md'
        rows, full = parse_transcript(src_tr)
        if full:
            shutil.copyfile(src_tr, f'{out}/transcript.md')

        # 3) screenshots
        shots = sorted(glob.glob(f'{KB}/screenshots/{vid}/*.jpg'))
        for s in shots:
            dst = f'{out}/screenshots/{os.path.basename(s)}'
            if not os.path.exists(dst):
                shutil.copyfile(s, dst)

        # 4) case: nếu đã nằm sẵn trong thư mục thì giữ nguyên; nếu còn ở cases/ cũ thì migrate sang
        has_case = os.path.exists(f'{out}/case.md')
        cp = None if has_case else legacy_case(vid)
        if cp:
            body = open(cp, encoding='utf-8').read()
            body = re.sub(r'\.\./screenshots/[A-Za-z0-9_-]+/', 'screenshots/', body)
            body = re.sub(r'\.\./_raw/transcripts/[A-Za-z0-9_-]+\.md', 'transcript.md', body)
            def _xref(mo):
                tgt = mo.group(1)
                if tgt == 'transcript':
                    return '](transcript.md)'
                return f'](../{slug2folder[tgt]}/case.md)' if tgt in slug2folder else mo.group(0)
            body = re.sub(r'\]\(([a-z0-9-]+)\.md\)', _xref, body)   # link case↔case
            open(f'{out}/case.md', 'w', encoding='utf-8').write(body)
            has_case = True
        if has_case:
            with_case += 1

        # 5) README của video
        dur = m.get('duration') or 0
        ch = '\n'.join(f"- `{c['start']//60:02d}:{c['start']%60:02d}` {c['title']}" for c in m.get('chapters', []))
        desc = re.sub(r'\n{2,}', '\n', (m.get('description') or '').strip())
        desc = '\n'.join(l for l in desc.split('\n')
                         if not re.search(r'(http|Chapters:|🔔|🏁|Follow|Check out)', l))[:600]
        nums = key_numbers(rows)
        nums_md = '\n'.join(f'- `{t//60:02d}:{t%60:02d}` {s}' for t, s in nums) or '_(không bắt được con số nào)_'
        # đếm ảnh ở thư mục đích, không phải ở nguồn legacy — ảnh có thể được thêm tay
        out_shots = sorted(glob.glob(f'{out}/screenshots/*.jpg'))
        shots_md = '\n'.join(
            f'{i}. `{os.path.basename(s)}` — ![]({("screenshots/" + os.path.basename(s))})'
            for i, s in enumerate(out_shots, 1)) or '_(chưa có ảnh)_'

        status = ('✅ **Đã phân tích sâu** → [`case.md`](case.md)' if has_case
                  else ('⏳ **Chưa phân tích sâu** — có transcript và ảnh đầy đủ để tra cứu' if full
                        else '⚠️ **Video này không có phụ đề tự động** — chỉ có ảnh và metadata'))
        rows_md = (('| [`case.md`](case.md) | **Phân tích đầy đủ** — ý tưởng, validate, GTM, áp dụng ở VN |\n' if has_case else '')
                   + ('| [`transcript.md`](transcript.md) | Transcript gốc, có timestamp |\n' if full else '')
                   + '| [`meta.json`](meta.json) | Metadata gốc (chapters, heatmap, mô tả) |\n'
                   + f'| [`screenshots/`](screenshots/) | {len(out_shots)} ảnh 720p |')

        readme = f"""# {m.get('title','')}

{status}

| | |
|---|---|
| **Video** | <{m.get('webpage_url', f'https://www.youtube.com/watch?v={vid}')}> |
| **Đăng** | {fmt_date(d)} |
| **Thời lượng** | {dur//60}:{dur%60:02d} |
| **Lượt xem** | {(m.get('view_count') or 0):,} |
| **Lượt thích** | {(m.get('like_count') or 0):,} |
| **Video ID** | `{vid}` |

## Trong thư mục này

| File | Nội dung |
|---|---|
{rows_md}

## Mô tả gốc

{desc or '_(không có)_'}

## Số liệu bắt được từ transcript

> Các đoạn founder nhắc tới con số, kèm timestamp để tua thẳng tới đó trong video.

{nums_md}

## Chương

{ch or '_(không có chapter)_'}

## Ảnh

{shots_md}

---

← [Quay lại index](../../index.md) · [Toàn bộ video](../README.md)
"""
        open(f'{out}/README.md', 'w', encoding='utf-8').write(readme)
        made += 1

    print(f'✅ {made} thư mục video ({with_case} có case.md phân tích sâu)')

if __name__ == '__main__':
    main()
