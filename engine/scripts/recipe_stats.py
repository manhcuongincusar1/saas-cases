#!/usr/bin/env python3
"""Số đếm của một công thức, lấy từ kb/data/kb.duckdb bằng SQL chạy lại được.

Dùng:  python3 -I engine/scripts/recipe_stats.py <tactic> [<tactic> ...]      (ví dụ: s5-insider)
Hiệu ứng phụ: ghi câu truy vấn đã thay tactic vào engine/recipes/<tactic>.sql (nếu ghi được), để người đọc chạy lại.

Định nghĩa (để công thức không phải lặp lại):
- "case" = một cặp (video_id, case_id) có ÍT NHẤT MỘT step mang tactic đó. Một founder kể hai sản phẩm là 2 case (ghi chú trong công thức).
- "founder" = case có depth=full (founder kể kỹ); mention = chỉ được nhắc.
- "chỉ host" = step không gắn case nào (do host/expert mô tả, không phải việc founder đã làm).
- "giống user" = case full KHÔNG nêu cả 4 lợi thế: existing_audience, capital, network, prior_success. Đó là "không nêu", không phải "không có".
- months_to_current = số tháng founder nêu từ lúc bắt đầu tới mức doanh thu hiện tại (n có thể nhỏ).
"""
import pathlib
import sys

import duckdb

ROOT = pathlib.Path(__file__).resolve().parents[2]
DB = ROOT / "kb/data/kb.duckdb"

SQL = {
    "đếm": """
select count(*) as steps,
       count(distinct video_id) as videos,
       count(distinct case when case_id is not null then video_id || '/' || case_id end) as cases_all,
       sum(case when case_id is null then 1 else 0 end) as steps_host_only
from steps where tactic = '{t}';
""",
    "case full + giống user": """
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = '{t}'
)
select count(*) as cases_full,
       sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id
                                 and a.value in ('existing_audience','capital','network','prior_success')) then 1 else 0 end) as khong_neu_4_loi_the,
       sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id
                                 and a.value = 'existing_audience') then 1 else 0 end) as khong_neu_audience,
       sum(case when exists (select 1 from cases c where c.video_id = k.video_id and c.case_id = k.case_id and c.demand_kind is null) then 1 else 0 end) as khong_ke_bang_chung_nhu_cau
from k;
""",
    "months_to_current": """
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = '{t}'
)
select count(c.months_to_current) as n,
       round(median(c.months_to_current), 1) as trung_vi,
       round(quantile_cont(c.months_to_current, 0.25), 1) as p25,
       round(quantile_cont(c.months_to_current, 0.75), 1) as p75
from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id;
""",
    "kênh trả tiền hay organic (scale_channels)": """
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = '{t}'
)
select sum(case when c.scale_channels like '%paid_%' or c.scale_channels like '%influencer_paid%' then 1 else 0 end) as co_kenh_tra_tien,
       sum(case when c.scale_channels is not null and c.scale_channels <> ''
                 and c.scale_channels not like '%paid_%' and c.scale_channels not like '%influencer_paid%' then 1 else 0 end) as thuan_organic,
       sum(case when c.scale_channels is null or c.scale_channels = '' then 1 else 0 end) as khong_neu
from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id;
""",
}


def main(tactics):
    db = duckdb.connect(str(DB), read_only=True)
    for t in tactics:
        out = [f"-- engine/scripts/recipe_stats.py {t}; chạy lại: duckdb kb/data/kb.duckdb < engine/recipes/{t}.sql\n"]
        print(f"## {t}")
        for name, q in SQL.items():
            q = q.format(t=t)
            cols = [d[0] for d in db.execute(q).description]
            row = db.execute(q).fetchone()
            print(f"  {name}: " + ", ".join(f"{c}={v}" for c, v in zip(cols, row)))
            out.append(f"-- {name}\n{q.strip()}\n")
        try:
            (ROOT / "engine/recipes" / f"{t}.sql").write_text("\n".join(out), encoding="utf-8")
        except OSError as e:
            print("  (không ghi được .sql:", e, ")")


if __name__ == "__main__":
    main(sys.argv[1:] or ["s5-insider"])
