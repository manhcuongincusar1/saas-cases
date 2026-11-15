-- Số đếm thêm cho s14-test-with-target-group. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s14-test-with-target-group.extra.sql
-- (1) loại bằng chứng nhu cầu của case full có step s14
select coalesce(c.demand_kind, 'không nêu') as demand_kind, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's14-test-with-target-group' group by 1 order by 2 desc;
-- (2) case full có step s14 theo community_insider (true / false / không nêu)
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's14-test-with-target-group' group by 1 order by 2 desc;
-- (3) step s14 theo chặng
select stage, count(*) as steps from steps where tactic = 's14-test-with-target-group' group by 1 order by 2 desc;
