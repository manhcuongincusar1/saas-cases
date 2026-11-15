-- Số đếm của mục "Thực tế" và "Tín hiệu nhu cầu" chương VALIDATE. Chạy: duckdb kb/data/kb.duckdb < engine/chapters/validate.sql
-- (1) tổng case full, số sản phẩm khác nhau (case_id), và phân bố demand_kind (không nêu = null)
select count(*) as case_full, count(distinct case_id) as san_pham_khac_nhau from cases where depth = 'full';
select coalesce(demand_kind, 'không nêu') as demand_kind, demand_level, count(*) as n from cases where depth = 'full' group by 1, 2 order by 3 desc;
-- (2) case full có tín hiệu từ mức 5 trở lên, trên số case có nêu tín hiệu
select sum(case when demand_level >= 5 then 1 else 0 end) as muc_5_tro_len, sum(case when demand_level is not null then 1 else 0 end) as co_nêu_tin_hieu from cases where depth = 'full';
-- (3) trong 105 case không nêu demand_kind, bao nhiêu case có step ở chặng validate (video có kể việc, trường nhu cầu để trống)
select count(*) as khong_neu, sum(case when exists (select 1 from steps s where s.video_id = c.video_id and s.case_id = c.case_id and s.stage = 'validate') then 1 else 0 end) as co_step_validate
from cases c where c.depth = 'full' and c.demand_kind is null;
-- (4) không nêu theo kênh
select v.channel, count(*) as case_full, sum(case when c.demand_kind is null then 1 else 0 end) as khong_neu
from cases c join videos v using (video_id) where c.depth = 'full' group by 1 order by 2 desc;
-- (5) built_first: số case, số case có prior_failures_count > 0, tổng số lần, số case có mô tả prior_failures_what, số case có months_to_current
select count(*) as built_first, sum(case when prior_failures_count > 0 then 1 else 0 end) as co_prior_failures_count,
       sum(prior_failures_count) as tong_so_lan, sum(case when prior_failures_what is not null then 1 else 0 end) as co_mo_ta_prior_failures,
       count(months_to_current) as co_thang
from cases where depth = 'full' and demand_kind = 'built_first';
-- (6) so sánh: tất cả case full, tỉ lệ có prior_failures_count > 0 và có mô tả
select count(*) as case_full, sum(case when prior_failures_count > 0 then 1 else 0 end) as co_prior_failures_count,
       sum(case when prior_failures_what is not null then 1 else 0 end) as co_mo_ta_prior_failures
from cases where depth = 'full';
-- (7) prior_failures theo từng nhóm demand_kind
select coalesce(demand_kind, 'không nêu') as demand_kind, count(*) as n, sum(case when prior_failures_count > 0 then 1 else 0 end) as co_prior_failures_count
from cases where depth = 'full' group by 1 order by 2 desc;
-- (8) liệt kê 23 case built_first với prior_failures_what và prior_failures_q
select video_id[:6] as video, case_id, prior_failures_count, prior_failures_what, prior_failures_q from cases where depth = 'full' and demand_kind = 'built_first' order by video_id;
-- (9) built_first mà cùng sản phẩm xuất hiện ở video khác có bằng chứng nhu cầu khác
select b.video_id[:6] as video_built_first, b.case_id, o.video_id[:6] as video_khac, o.depth, o.demand_kind
from cases b join cases o on o.case_id = b.case_id and o.video_id <> b.video_id
where b.depth = 'full' and b.demand_kind = 'built_first' order by 2;
-- (10) months_to_current theo nhóm bằng chứng nhu cầu (case full)
select case when demand_kind = 'built_first' then '1 built_first'
            when demand_level >= 3 then '2 demand_level>=3'
            when demand_kind is null then '3 không nêu'
            else '4 mức 1-2 (friends_praise, content_views)' end as nhom,
       count(*) as case_full, count(months_to_current) as n_co_thang,
       round(median(months_to_current), 1) as trung_vi, round(quantile_cont(months_to_current, 0.25), 1) as p25, round(quantile_cont(months_to_current, 0.75), 1) as p75
from cases where depth = 'full' group by 1 order by 1;
-- (11) months_to_current theo từng demand_kind
select coalesce(demand_kind, 'không nêu') as demand_kind, count(months_to_current) as n, round(median(months_to_current), 1) as trung_vi
from cases where depth = 'full' group by 1 order by 2 desc;
-- (12) số case có months_to_current ở từng nhóm và số case từ 3 tháng trở xuống
select case when demand_kind = 'built_first' then 'built_first' when demand_level >= 3 then 'demand_level>=3' when demand_kind is null then 'không nêu' else 'mức 1-2' end as nhom,
       count(months_to_current) as n, sum(case when months_to_current <= 3 then 1 else 0 end) as tu_3_thang_tro_xuong, sum(case when months_to_current <= 1 then 1 else 0 end) as tu_1_thang_tro_xuong
from cases where depth = 'full' group by 1 order by 1;
-- (13) 9 case paid: sản phẩm, số tiền, chặng và ghi chú (mô tả demand_what, q và mốc)
select video_id[:6] as video, case_id, demand_what, demand_ts, months_to_current from cases where depth = 'full' and demand_kind = 'paid' order by video_id;
-- (14) community_insider của 23 case built_first và 9 case paid (true / false / không nêu)
select demand_kind, sum(case when community_insider is true then 1 else 0 end) as insider, sum(case when community_insider is false then 1 else 0 end) as outsider,
       sum(case when community_insider is null then 1 else 0 end) as khong_neu
from cases where depth = 'full' and demand_kind in ('built_first', 'paid') group by 1;
