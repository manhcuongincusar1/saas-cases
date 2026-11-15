#!/usr/bin/env python3
"""Dựng kb/data/kb.duckdb từ kb/videos/**/*.md (schema 2) + transcript gốc. DB là bản SINH RA: sửa file .md rồi chạy lại, không sửa DB.

Dùng: python3 -I kb/scripts/build.py
Bảng: videos, cases, advantages, first_users, steps, quotes, rules, numbers, segments (transcript theo đoạn), meta.
Khoá nối: video_id (+ case_id). Trường cột là phẳng để SQL; trường lồng (q, ts) giữ nguyên.
"""
import datetime
import pathlib
import re

import sys

import duckdb
import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import check  # noqa: E402  (load_segments dùng chung)

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = ROOT / "kb/data/kb.duckdb"
OUT.parent.mkdir(parents=True, exist_ok=True)
if OUT.exists():
    OUT.unlink()


def load(p):
    text = p.read_text(encoding="utf-8")
    head, body = text.split("\n---", 1)
    return yaml.safe_load(head[4:]), body


def s(x):
    return None if x is None else str(x)


def g(d, *keys):
    for k in keys:
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d


V, C, ADV, FU, ST, Q, R, N, SEG = [], [], [], [], [], [], [], [], []
for p in sorted((ROOT / "kb/videos").glob("*/*.md")):
    fm, body = load(p)
    vid = fm["video_id"]
    V.append((vid, fm.get("channel"), s(fm.get("title")), s(fm.get("date")), fm.get("url"), fm.get("kind"), s(fm.get("bias")),
              fm.get("transcript"), str(p.relative_to(ROOT)), body.strip(),
              ", ".join(f"{x.get('name')} ({x.get('role')})" for x in fm.get("speakers") or [])))
    for c in fm.get("cases") or []:
        cid = c.get("id")
        rev = c.get("revenue") or {}
        ds = c.get("demand_signal") or {}
        t = c.get("time_to_revenue") or {}
        com = c.get("community_at_discovery") or {}
        pf = c.get("prior_failures") or {}
        b = c.get("build") or {}
        C.append((vid, cid, c.get("depth"), s(c.get("product")), s(c.get("what")), ",".join(c.get("type") or []), s(c.get("customer")),
                  s(c.get("pricing")), rev.get("amount"), rev.get("unit"), rev.get("basis"), rev.get("evidence"), s(rev.get("q")), s(rev.get("ts")),
                  ",".join(c.get("idea_origin") or []), ",".join(c.get("scale_channels") or []),
                  s(com.get("value")), com.get("insider"), s(com.get("q")), s(com.get("ts")),
                  ds.get("kind"), ds.get("level"), s(ds.get("what")), s(ds.get("q")), s(ds.get("ts")),
                  pf.get("count"), s(pf.get("what")), s(pf.get("q")),
                  g(t, "first_dollar", "months"), g(t, "to_1k_mrr", "months"), g(t, "to_10k_mrr", "months"), g(t, "to_current", "months"),
                  s(g(t, "to_current", "q")), s(g(t, "to_current", "ts")),
                  s(b.get("time")), s("; ".join(map(str, b.get("cut") or [])) or None), s(b.get("q")), s(b.get("ts")),
                  s(g(c, "founder", "who")), s(g(c, "founder", "background")), g(c, "founder", "technical")))
        for a in c.get("unfair_advantage") or []:
            ADV.append((vid, cid, a.get("value"), s(a.get("what")), s(a.get("q")), s(a.get("ts"))))
        for u in c.get("first_users") or []:
            FU.append((vid, cid, u.get("channel"), s(u.get("what")), s(u.get("q")), s(u.get("ts"))))
    for st in fm.get("steps") or []:
        ST.append((vid, s(st.get("case")), st.get("stage"), s(st.get("ts")), s(st.get("what")), st.get("tactic"), s(st.get("tactic_note")),
                   s(st.get("tool")), s(st.get("threshold")), s(st.get("cost"))))
    for q in fm.get("quotes") or []:
        Q.append((vid, s(q.get("ts")), q.get("who"), q.get("stage"), ",".join(q.get("theme") or []), s(q.get("text")), s(q.get("vi"))))
    for r in fm.get("rules") or []:
        R.append((vid, s(r.get("ts")), r.get("who"), r.get("stage"), ",".join(r.get("theme") or []), s(r.get("text")), s(r.get("vi")), r.get("evidence")))
    for n in fm.get("numbers") or []:
        N.append((vid, s(n.get("ts")), s(n.get("metric")), s(n.get("value")), n.get("unit"), n.get("evidence")))
    # transcript theo đoạn: dùng chung load_segments của check.py (cả định dạng Starter Story "[mm:ss] text" lẫn Superwall "… [hh:mm:ss → hh:mm:ss]")
    tp = ROOT / fm["transcript"]
    if tp.exists():
        for idx, (sec, text) in enumerate(check.load_segments(tp)):
            ts = f"{sec // 3600:02d}:{sec % 3600 // 60:02d}:{sec % 60:02d}" if sec >= 3600 else f"{sec // 60:02d}:{sec % 60:02d}"
            SEG.append((vid, idx, ts, None, text))

db = duckdb.connect(str(OUT))
db.execute("create table videos(video_id varchar primary key, channel varchar, title varchar, date varchar, url varchar, kind varchar, bias varchar, transcript varchar, file varchar, body varchar, speakers varchar)")
db.execute("""create table cases(video_id varchar, case_id varchar, depth varchar, product varchar, what varchar, type varchar, customer varchar, pricing varchar,
 revenue_amount double, revenue_unit varchar, revenue_basis varchar, revenue_evidence varchar, revenue_q varchar, revenue_ts varchar,
 idea_origin varchar, scale_channels varchar,
 community varchar, community_insider boolean, community_q varchar, community_ts varchar,
 demand_kind varchar, demand_level integer, demand_what varchar, demand_q varchar, demand_ts varchar,
 prior_failures_count integer, prior_failures_what varchar, prior_failures_q varchar,
 months_first_dollar double, months_to_1k_mrr double, months_to_10k_mrr double, months_to_current double, months_to_current_q varchar, months_to_current_ts varchar,
 build_time varchar, build_cut varchar, build_q varchar, build_ts varchar,
 founder_who varchar, founder_background varchar, founder_technical boolean)""")
db.execute("create table advantages(video_id varchar, case_id varchar, value varchar, what varchar, q varchar, ts varchar)")
db.execute("create table first_users(video_id varchar, case_id varchar, channel varchar, what varchar, q varchar, ts varchar)")
db.execute("create table steps(video_id varchar, case_id varchar, stage varchar, ts varchar, what varchar, tactic varchar, tactic_note varchar, tool varchar, threshold varchar, cost varchar)")
db.execute("create table quotes(video_id varchar, ts varchar, who varchar, stage varchar, theme varchar, text varchar, vi varchar)")
db.execute("create table rules(video_id varchar, ts varchar, who varchar, stage varchar, theme varchar, text varchar, vi varchar, evidence varchar)")
db.execute("create table numbers(video_id varchar, ts varchar, metric varchar, value varchar, unit varchar, evidence varchar)")
db.execute("create table segments(video_id varchar, idx integer, ts varchar, chapter varchar, text varchar)")
for name, rows in (("videos", V), ("cases", C), ("advantages", ADV), ("first_users", FU), ("steps", ST), ("quotes", Q), ("rules", R), ("numbers", N), ("segments", SEG)):
    if rows:
        db.executemany(f"insert into {name} values ({','.join('?' * len(rows[0]))})", rows)
db.execute("create table meta as select ? as built_at, 'schema 2; sinh từ kb/videos bằng kb/scripts/build.py — không sửa tay' as note", [datetime.datetime.now().isoformat(timespec="seconds")])
for name in ("videos", "cases", "advantages", "first_users", "steps", "quotes", "rules", "numbers", "segments"):
    print(f"{name:12s}", db.execute(f"select count(*) from {name}").fetchone()[0])
db.close()
