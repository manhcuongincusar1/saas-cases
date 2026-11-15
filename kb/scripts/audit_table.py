#!/usr/bin/env python3
"""Bảng audit cho mọi case depth=full: các trường phán đoán kèm `q` để người đọc kiểm 100%.

Dùng: python3 -I kb/scripts/audit_table.py [file.md ...]     (không tham số = tất cả kb/videos)
Mỗi case in: id · demand_signal (kind→level, q) · idea_origin · unfair_advantage (value, q) · first_users (channel, q)
· time_to_revenue (months, q). Người đọc sửa dòng sai trực tiếp trong file, ghi số dòng đã sửa.
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
files = [pathlib.Path(a) for a in sys.argv[1:]] or sorted((ROOT / "kb/videos").rglob("*.md"))


def cut(s, n=110):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[:n] + "…"


rows = 0
for p in files:
    fm = yaml.safe_load(p.read_text(encoding="utf-8").split("\n---", 1)[0][4:])
    for c in fm.get("cases") or []:
        if c.get("depth") != "full":
            continue
        rows += 1
        print(f"\n## {p.name} · {c.get('id')}")
        ds = c.get("demand_signal")
        print(f"  demand: {ds.get('kind')}→{ds.get('level')} | {cut(ds.get('q'))}" if ds else "  demand: null")
        print(f"  idea_origin: {c.get('idea_origin')}")
        cd = c.get("community_at_discovery")
        if cd:
            print(f"  community: insider={cd.get('insider')} | {cut(cd.get('value'), 80)} | {cut(cd.get('q'), 90)}")
        for a in c.get("unfair_advantage") or []:
            print(f"  advantage: {a.get('value')} | {cut(a.get('q'), 100)}")
        for u in c.get("first_users") or []:
            print(f"  first_user: {u.get('channel')} | {cut(u.get('q'), 100)}")
        for k, m in (c.get("time_to_revenue") or {}).items():
            if m:
                print(f"  time {k}: {m.get('months')} tháng | {cut(m.get('q'), 100)}")
        rev = c.get("revenue")
        if rev:
            print(f"  revenue: {rev.get('amount')} {rev.get('unit')}/{rev.get('basis')} [{rev.get('evidence')}] | {cut(rev.get('q'), 100)}")
print(f"\n{rows} case full")
