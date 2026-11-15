-- Số đếm thêm cho s10-customer-interviews. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s10-customer-interviews.extra.sql
-- (1) tách nhánh: sau launch = tactic_note bắt đầu bằng 'sau launch', trước launch (chặng validate, không đánh dấu), chưa rõ = còn lại (find-idea hoặc launch, không đánh dấu), host = step không gắn case
select case when case_id is null then '4 host/expert'
            when tactic_note like 'sau launch%' then '3 sau launch'
            when stage = 'validate' then '1 trước launch (chặng validate, không đánh dấu sau launch)'
            else '2 chưa rõ trước/sau (find-idea hoặc launch, không đánh dấu)' end as nhanh,
       count(*) as steps,
       count(distinct case when case_id is not null then video_id || '/' || case_id end) as case_all
from steps where tactic = 's10-customer-interviews' group by 1 order by 1;
-- (2) số case full theo từng nhánh (một case có thể nằm ở hai nhánh)
select case when s.tactic_note like 'sau launch%' then 'sau launch'
            when s.stage = 'validate' then 'trước launch (validate)'
            else 'chưa rõ' end as nhanh,
       count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's10-customer-interviews' group by 1 order by 2 desc;
-- (3) loại bằng chứng nhu cầu của case full có step s10
select coalesce(c.demand_kind, 'không nêu') as demand_kind, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's10-customer-interviews' group by 1 order by 2 desc;
-- (4) case full có step s10 theo community_insider (true / false / không nêu)
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's10-customer-interviews' group by 1 order by 2 desc;
-- (5) tháng tới mức doanh thu hiện tại của case full có step s10 trước launch (chặng validate, không đánh dấu sau launch) và có số tháng
select count(c.months_to_current) as n, round(median(c.months_to_current), 1) as trung_vi
from cases c where c.depth = 'full' and c.months_to_current is not null and exists
  (select 1 from steps s where s.video_id = c.video_id and s.case_id = c.case_id and s.tactic = 's10-customer-interviews'
   and s.stage = 'validate' and (s.tactic_note is null or s.tactic_note not like 'sau launch%'));
