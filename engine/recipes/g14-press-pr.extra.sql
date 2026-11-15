-- Số đếm thêm cho g14-press-pr. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g14-press-pr.extra.sql
-- (1) các step g14: case, chặng, kênh video
select s.video_id[:6] as video, coalesce(s.case_id, 'HOST') as case_id, s.stage, v.channel, s.ts from steps s join videos v using(video_id) where s.tactic = 'g14-press-pr' order by s.video_id, s.ts;
-- (2) case dùng g14 theo community_insider (true / false = outsider / không nêu = null)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g14-press-pr' and c.depth = 'full')
select case when c.community_insider is true then 'insider' when c.community_insider is false then 'outsider' else 'không nêu' end as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) số doanh thu và tháng tới mức hiện tại founder nêu của case dùng g14
select c.case_id, c.revenue_amount, c.revenue_unit, c.revenue_basis, c.months_to_current from cases c join steps s using(video_id, case_id) where s.tactic = 'g14-press-pr' and c.depth = 'full' group by all order by 1;
-- (4) lý do báo chí đến, theo tactic_note của từng step (không phải đếm, để đọc)
select s.case_id, s.tactic_note from steps s where s.tactic = 'g14-press-pr' and s.case_id is not null order by s.video_id;
-- (5) trong 4 case g14, bao nhiêu case cũng có step g3 hoặc g1 hoặc g9 (kênh khác cùng giai đoạn)
select c.case_id, string_agg(distinct s2.tactic, ', ') as tactic_khac
from (select distinct video_id, case_id from steps where tactic = 'g14-press-pr' and case_id is not null) c
left join steps s2 on s2.video_id = c.video_id and s2.case_id = c.case_id and s2.tactic like 'g%' and s2.tactic <> 'g14-press-pr' group by 1 order by 1;
-- (6) video có bias nêu quảng cáo hoặc tài trợ trong các video có step g14
select v.video_id[:6] as video, v.channel, left(v.bias, 160) as bias from steps s join videos v using(video_id) where s.tactic = 'g14-press-pr' group by all order by 1;
