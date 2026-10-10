#!/usr/bin/env python3
"""Sinh index.md + videos/README.md + data/cases.csv từ thư mục videos/.
Chạy lại sau khi thêm/sửa bất kỳ case.md nào:  python3 build_index.py
"""
import os, csv, glob, json, yaml, datetime, re

KB = os.path.dirname(os.path.abspath(__file__))
VID = f'{KB}/videos'

FIELDS = ['slug', 'product', 'founder', 'revenue_usd_month', 'model', 'category',
          'audience', 'main_channel', 'team_size', 'funding', 'started',
          'time_to_first_sale', 'time_to_scale', 'replicability_vn', 'difficulty',
          'opex_usd_month', 'startup_cost_usd', 'tags', 'id', 'published', 'views',
          'video_url', 'tagline', 'folder']

MODEL_VN = {
    'mobile-app-subscription': 'App di động (subscription)',
    'b2b-saas-subscription': 'SaaS B2B',
    'b2c-saas-subscription': 'SaaS B2C',
    'database-directory-saas': 'Database / Directory',
    'ecommerce': 'Thương mại điện tử',
    'agency-service': 'Agency / Dịch vụ',
    'content-media': 'Nội dung / Media',
    'info-product': 'Sản phẩm thông tin',
    'marketplace': 'Marketplace',
    'newsletter': 'Newsletter',
    'physical-product': 'Sản phẩm vật lý',
    'local-service': 'Dịch vụ địa phương',
}


def num(v):
    """Chấp nhận 4, '4', '4/5' -> 4; không parse được -> None."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return v
    m = re.match(r'\s*([\d.]+)', str(v))
    return float(m.group(1)) if m else None


def money(v):
    v = num(v)
    if v is None:
        return '—'
    if v >= 1_000_000:
        return f'${v/1_000_000:.1f}M'
    if v >= 1_000:
        return f'${v/1_000:.0f}K'
    return f'${v:.0f}'


def stars(n):
    n = num(n)
    if n is None:
        return '—'
    return '●' * int(n) + '○' * (5 - int(n))


def load_all():
    """Đọc mọi thư mục video. Trả về (cases đã phân tích, tất cả video)."""
    cases, all_videos = [], []
    for d in sorted(glob.glob(f'{VID}/*/')):
        folder = os.path.basename(d.rstrip('/'))
        mp = f'{d}meta.json'
        if not os.path.exists(mp):
            continue
        m = json.load(open(mp, encoding='utf-8'))
        desc = re.sub(r'\s+', ' ', (m.get('description') or '').split('\n')[0]).strip()
        row = {
            'folder': folder,
            'desc': desc,
            'summary': '',
            'title': m.get('title', ''),
            'published': m.get('upload_date', ''),
            'views': m.get('view_count') or 0,
            'duration': m.get('duration') or 0,
            'id': m.get('id', ''),
            'has_case': os.path.exists(f'{d}case.md'),
            'n_shots': len(glob.glob(f'{d}screenshots/*.jpg')),
            'has_transcript': os.path.exists(f'{d}transcript.md'),
        }
        all_videos.append(row)

        if row['has_case']:
            txt = open(f'{d}case.md', encoding='utf-8').read()
            sm = re.search(r'\*\*Tóm tắt 30 giây:\*\*(.+?)(?:\n\n|\Z)', txt, re.S)
            if sm:
                row['summary'] = re.sub(r'\*\*|\s+', lambda mo: '' if mo.group(0).startswith('*') else ' ',
                                        sm.group(1)).strip()
            fm_match = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
            if not fm_match:
                print(f'  ⚠ thiếu frontmatter: {folder}/case.md')
                continue
            try:
                fm = yaml.safe_load(fm_match.group(1)) or {}
            except yaml.YAMLError as e:
                print(f'  ⚠ YAML lỗi ở {folder}: {e}')
                continue
            fm['folder'] = folder
            fm.setdefault('slug', folder)
            cases.append(fm)
    return cases, all_videos


def write_csv(cases):
    os.makedirs(f'{KB}/data', exist_ok=True)
    with open(f'{KB}/data/cases.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, extrasaction='ignore')
        w.writeheader()
        for c in cases:
            row = dict(c)
            if isinstance(row.get('tags'), list):
                row['tags'] = ';'.join(str(t) for t in row['tags'])
            w.writerow(row)


def section(title, rows, cols):
    if not rows:
        return ''
    s = f'\n### {title}\n\n| ' + ' | '.join(cols) + ' |\n|' + '---|' * len(cols) + '\n'
    return s + '\n'.join(rows) + '\n'


def link(c):
    return f"videos/{c['folder']}/case.md"


def build_index(cases, all_videos):
    total_rev = sum(num(c.get('revenue_usd_month')) or 0 for c in cases)
    by_rev = sorted(cases, key=lambda c: -(num(c.get('revenue_usd_month')) or 0))
    L = []
    L.append('# Starter Story — Knowledge Base Case Study\n')
    L.append(f'> **{len(cases)}/{len(all_videos)} video đã phân tích sâu** · tổng doanh thu ghi nhận '
             f'**{money(total_rev)}/tháng** · cập nhật {datetime.date.today().strftime("%d/%m/%Y")}\n')
    L.append('Mỗi case trả lời 4 câu: **ý tưởng đến từ đâu · validate thế nào · '
             'go-to-market ra sao · áp dụng ở VN được không.**\n')
    L.append(f'📁 [**Bảng tra toàn bộ {len(all_videos)} video**](videos/README.md) — mỗi video một thư mục: '
             'transcript thật + ảnh + tóm tắt · 📘 [`playbooks/`](playbooks/) — đúc kết xuyên suốt nhiều case '
             '· 📊 [`data/cases.csv`](data/cases.csv) — query bằng DuckDB\n')
    L.append('---\n')

    L.append('## Case đã phân tích sâu (xếp theo doanh thu/tháng)\n')
    L.append('| Doanh thu/th | Sản phẩm | Mô hình | Kênh chính | Sao chép ở VN | Case |')
    L.append('|---:|---|---|---|:---:|---|')
    for c in by_rev:
        L.append('| **{rev}** | {prod} | {model} | {chan} | {rep} | [mở]({f}) |'.format(
            rev=money(c.get('revenue_usd_month')),
            prod=str(c.get('product', c.get('slug', '—')))[:38],
            model=MODEL_VN.get(c.get('model'), c.get('model', '—')),
            chan=str(c.get('main_channel', '—'))[:34],
            rep=stars(c.get('replicability_vn')),
            f=link(c)))
    L.append('')

    L.append('---\n\n## Lối vào nhanh\n')

    hi = [c for c in cases if (num(c.get('replicability_vn')) or 0) >= 4
          and (num(c.get('difficulty')) or 5) <= 3]
    L.append(section('🎯 Dễ sao chép nhất ở VN (replicability ≥4, difficulty ≤3)',
             [f"| [{c.get('product','—')}]({link(c)}) | {money(c.get('revenue_usd_month'))} | {c.get('tagline','')} |"
              for c in sorted(hi, key=lambda c: -(num(c.get('revenue_usd_month')) or 0))],
             ['Case', 'DT/tháng', 'Làm gì']))

    solo = [c for c in cases if str(c.get('team_size', '')).startswith('1')]
    L.append(section('👤 Một mình làm được',
             [f"| [{c.get('product','—')}]({link(c)}) | {money(c.get('revenue_usd_month'))} | {c.get('main_channel','—')} |"
              for c in sorted(solo, key=lambda c: -(num(c.get('revenue_usd_month')) or 0))],
             ['Case', 'DT/tháng', 'Kênh']))

    cheap = [c for c in cases if (num(c.get('opex_usd_month')) or 99999) <= 500]
    L.append(section('💰 Chi phí vận hành cực thấp',
             [f"| [{c.get('product','—')}]({link(c)}) | {money(c.get('revenue_usd_month'))} | ${c.get('opex_usd_month')}/tháng |"
              for c in sorted(cheap, key=lambda c: -(num(c.get('revenue_usd_month')) or 0))],
             ['Case', 'DT/tháng', 'Chi phí']))

    for key, heading in (('model', '## Theo mô hình kinh doanh'), ('main_channel', '## Theo kênh tăng trưởng')):
        groups = {}
        for c in cases:
            groups.setdefault(str(c.get(key, '—')), []).append(c)
        L.append(f'\n---\n\n{heading}\n')
        for k, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            label = MODEL_VN.get(k, k) if key == 'model' else k
            links = ', '.join(f"[{c.get('product', c['slug'])}]({link(c)})"
                              for c in sorted(g, key=lambda c: -(num(c.get('revenue_usd_month')) or 0)))
            L.append(f'- **{label}** ({len(g)}) — {links}')
        L.append('')

    tagmap = {}
    for c in cases:
        for t in (c.get('tags') or []):
            tagmap.setdefault(str(t), []).append(c)
    L.append('\n---\n\n## Theo chủ đề\n')
    for t, g in sorted(tagmap.items(), key=lambda kv: -len(kv[1])):
        L.append(f'- `{t}` ({len(g)}) — ' + ', '.join(f"[{c.get('product', c['slug'])}]({link(c)})" for c in g))

    L.append('\n---\n\n*Nguồn: kênh YouTube [Starter Story](https://www.youtube.com/@starterstory). '
             'Tài liệu nghiên cứu cá nhân — phân tích và đúc kết, không phải bản sao nội dung gốc.*')
    return '\n'.join(L)


def build_videos_readme(all_videos, cases):
    by_folder = {c['folder']: c for c in cases}
    vids = sorted(all_videos, key=lambda v: v['published'], reverse=True)
    done = sum(1 for v in vids if v['has_case'])
    tot_views = sum(v['views'] for v in vids)
    tot_hours = sum(v['duration'] for v in vids) / 3600
    tot_shots = sum(v['n_shots'] for v in vids)

    L = [f'# Toàn bộ {len(vids)} video\n',
         f'> **{done} video đã phân tích sâu** (có `case.md`) · {len(vids) - done} video còn lại có '
         f'transcript + ảnh + số liệu để tra cứu\n',
         f'> Tổng **{tot_views/1e6:.1f}M lượt xem** · **{tot_hours:.1f} giờ** · **{tot_shots:,} ảnh**\n',
         'Mỗi thư mục chứa: `README.md` (tóm tắt + số liệu bắt được + chapters) · `transcript.md` · '
         '`meta.json` · `screenshots/` — và `case.md` nếu đã phân tích sâu.\n',
         '---\n',
         '| Đăng | Video | Nói về gì | Views | Phân tích |',
         '|---|---|---|---:|---|']
    for v in vids:
        d = v['published']
        d_fmt = f'{d[6:8]}/{d[4:6]}/{d[0:4]}' if len(d) == 8 else '—'
        c = by_folder.get(v['folder'])
        mark = f"✅ [case]({v['folder']}/case.md) · {money(c.get('revenue_usd_month'))}" if c else '⏳'
        blurb = (v['summary'] or v['desc'] or '')[:150]
        if len(v['summary'] or v['desc'] or '') > 150: blurb += '…'
        blurb = blurb.replace('|', '·')
        # tóm tắt lấy từ case.md (nằm trong videos/<folder>/) nên link chéo của nó
        # bắt đầu bằng ../ ; file này ở videos/ nên phải bỏ ../ đi
        blurb = re.sub(r'\]\(\.\./', '](', blurb)
        L.append(f"| {d_fmt} | [{v['title'][:56]}]({v['folder']}/README.md) | {blurb} | {v['views']:,} | {mark} |")
    L.append('\n---\n\n← [Quay lại index chính](../index.md)')
    return '\n'.join(L)


if __name__ == '__main__':
    cases, all_videos = load_all()
    write_csv(cases)
    open(f'{KB}/index.md', 'w', encoding='utf-8').write(build_index(cases, all_videos))
    open(f'{VID}/README.md', 'w', encoding='utf-8').write(build_videos_readme(all_videos, cases))
    print(f'✅ {len(all_videos)} video ({len(cases)} có case) → index.md + videos/README.md + data/cases.csv')
