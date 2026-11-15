#!/usr/bin/env python3
"""Điền hai khối TỰ SINH của một công thức từ kb/data/kb.duckdb:
  <!-- stats:start --> … <!-- stats:end -->        bảng số đếm (SQL chạy lại được, lưu ở engine/recipes/<id>.sql)
  <!-- evidence:start --> … <!-- evidence:end -->  bảng câu trích NGUYÊN VĂN, lấy từ danh sách chọn engine/evidence/<id>.picks.yaml
Đồng thời ghi engine/evidence/<id>.yaml (để check_recipes.py kiểm).

picks.yaml: danh sách {v: <6 ký tự đầu video_id>, ts: "07:04", use: "câu này dùng để làm gì"}; tìm trong bảng quotes rồi rules.
Dùng: python3 -I engine/scripts/build_recipe.py <id> [<tactic để đếm> ...]   (mặc định tactic = id)
Công thức nhiều tactic (hoặc không có tactic, ví dụ mục Thực tế): truyền các tactic cách nhau bằng dấu cách.
"""
import pathlib
import re
import sys

import duckdb
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/scripts"))
import recipe_stats  # noqa: E402

DB = duckdb.connect(str(ROOT / "kb/data/kb.duckdb"), read_only=True)


def fmt(v):
    return "—" if v is None else str(v)


def stats_block(tactics):
    tl = ", ".join(f"'{t}'" for t in tactics)
    q = {}
    q["step"] = DB.execute(f"""select count(*), count(distinct video_id), sum(case when case_id is null then 1 else 0 end),
        count(distinct case when case_id is not null then video_id || '/' || case_id end) from steps where tactic in ({tl})""").fetchone()
    base = f"""with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
        where s.tactic in ({tl}))"""
    q["full"] = DB.execute(base + f""" select count(*),
        sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id and a.value in ('existing_audience','capital','network','prior_success')) then 1 else 0 end),
        sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id and a.value = 'existing_audience') then 1 else 0 end),
        sum(case when exists (select 1 from cases c where c.video_id = k.video_id and c.case_id = k.case_id and c.demand_kind is null) then 1 else 0 end)
        from k""").fetchone()
    q["m"] = DB.execute(base + """ select count(c.months_to_current), round(median(c.months_to_current),1), round(quantile_cont(c.months_to_current,0.25),1),
        round(quantile_cont(c.months_to_current,0.75),1) from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id""").fetchone()
    q["ch"] = DB.execute(base + """ select sum(case when c.scale_channels like '%paid_%' or c.scale_channels like '%influencer_paid%' then 1 else 0 end),
        sum(case when c.scale_channels is not null and c.scale_channels <> '' and c.scale_channels not like '%paid_%' and c.scale_channels not like '%influencer_paid%' then 1 else 0 end),
        sum(case when c.scale_channels is null or c.scale_channels = '' then 1 else 0 end)
        from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id""").fetchone()
    steps, vids, host_only, cases_all = q["step"]
    nfull, nsim, nnoaud, nnodemand = q["full"]
    mn, med, p25, p75 = q["m"]
    paid, org, nospec = q["ch"]
    rows = [
        ("Step mang tactic này", f"{steps} step trong {vids} video"),
        ("Case (video, case) có step này", f"{cases_all}, trong đó {nfull} case full (founder kể kỹ)"),
        ("Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung)", f"{host_only}/{steps}"),
        ('Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước', f"{nsim}/{nfull}"),
        ("Case full không nêu existing_audience", f"{nnoaud}/{nfull}"),
        ("Case full video không kể bằng chứng nhu cầu trước launch", f"{nnodemand}/{nfull}"),
        ("Tháng tới mức doanh thu hiện tại (trung vị, p25–p75)", f"{fmt(med)} tháng ({fmt(p25)}–{fmt(p75)}), n={mn}"),
        ("Kênh scale trả tiền / thuần organic / không nêu", f"{fmt(paid)} / {fmt(org)} / {fmt(nospec)}"),
    ]
    out = ["| Số đếm | Giá trị |", "|---|---|"] + [f"| {a} | {b} |" for a, b in rows]
    out.append("")
    out.append("*\"Không nêu\" ≠ \"không có\". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/" + tactics[0] + ".sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*")
    return "\n".join(out)


def evidence(rid):
    pf = ROOT / "engine/evidence" / f"{rid}.picks.yaml"
    picks = yaml.safe_load(pf.read_text(encoding="utf-8"))
    items, md = [], ["| Ai · video · mốc | Nguyên văn | Dùng cho |", "|---|---|---|"]
    for p in picks:
        hit = None
        for tbl, kind in (("quotes", "quote"), ("rules", "rule")):
            rows = DB.execute(f"select t.video_id, t.ts, t.who, t.text, v.title, v.transcript, v.file from {tbl} t join videos v using(video_id) "
                              f"where t.video_id like ? and t.ts = ?", [p["v"] + "%", str(p["ts"])]).fetchall()
            if rows:
                hit = (rows[0], kind)
                break
        if not hit:  # dự phòng: trường q của case (lợi thế, người dùng đầu); founder = cases.founder_who
            for tbl, kind in (("advantages", "case"), ("first_users", "case")):
                rows = DB.execute(f"select t.video_id, t.ts, coalesce(c.founder_who, 'founder'), t.q, v.title, v.transcript, v.file from {tbl} t "
                                  f"join cases c on c.video_id = t.video_id and c.case_id = t.case_id join videos v on v.video_id = t.video_id "
                                  f"where t.video_id like ? and t.ts = ?", [p["v"] + "%", str(p["ts"])]).fetchall()
                if rows:
                    hit = (rows[0], kind)
                    break
        if not hit:
            raise SystemExit(f"KHÔNG TÌM THẤY {p}")
        (vid, ts, who, text, title, transcript, file), kind = hit
        text = " ".join(text.split())
        items.append({"transcript": transcript, "ts": ts, "speaker": who, "kind": kind, "case": p.get("case", ""), "what": p["use"], "text": text})
        slug = pathlib.Path(file).stem
        role = {"rule": "host/expert", "quote": "founder", "case": "founder"}[kind]
        if p.get("who"):  # tên gọn; dùng khi cases.founder_who quá dài (trường case) hoặc nhiều đồng sáng lập
            who = p["who"]
        elif len(who) > 40:
            raise SystemExit(f"tên quá dài, thêm who: vào pick {p}")
        md.append(f"| {who} ({role}) · `{slug}` · {ts} | \"{text}\" | {p['use']} |")
    (ROOT / "engine/evidence" / f"{rid}.yaml").write_text(yaml.safe_dump(items, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    return "\n".join(md)


def fill(text, tag, block):
    pat = re.compile(rf"(<!-- {tag}:start -->).*?(<!-- {tag}:end -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"thiếu khối {tag} trong công thức")
    return pat.sub(lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", text)


def main():
    rid = sys.argv[1]
    tactics = sys.argv[2:] or [rid]
    path = ROOT / "engine/recipes" / f"{rid}.md"
    text = path.read_text(encoding="utf-8")
    if "<!-- stats:start -->" in text:
        text = fill(text, "stats", stats_block(tactics))
    if "<!-- evidence:start -->" in text:
        text = fill(text, "evidence", evidence(rid))
    path.write_text(text, encoding="utf-8")
    recipe_stats.main(tactics) if len(tactics) == 1 else None
    print("đã điền", path.name)


if __name__ == "__main__":
    main()
