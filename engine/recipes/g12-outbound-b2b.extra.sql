-- Số đếm thêm cho g12-outbound-b2b. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g12-outbound-b2b.extra.sql
-- (1) các step g12: case, loại khách, chặng, kênh video
select s.video_id[:6] as video, coalesce(s.case_id, 'HOST') as case_id, s.stage, v.channel, s.ts from steps s join videos v using(video_id) where s.tactic = 'g12-outbound-b2b' order by s.video_id;
-- (2) case dùng g12 theo community_insider (true / false = outsider / không nêu = null)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g12-outbound-b2b' and c.depth = 'full')
select case when c.community_insider is true then 'insider' when c.community_insider is false then 'outsider' else 'không nêu' end as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) số doanh thu founder nêu của case dùng g12 (mức hiện tại hoặc tích luỹ, ghi rõ cơ sở)
select c.case_id, c.revenue_amount, c.revenue_unit, c.revenue_basis, c.months_to_current from cases c join steps s using(video_id, case_id) where s.tactic = 'g12-outbound-b2b' and c.depth = 'full' group by all order by 1;
-- (4) các step cold email/cold outreach thuộc tactic khác (g1, g7), để đối chiếu: kho không có tactic cold email riêng ngoài g12
select s.video_id[:6] as video, s.case_id, s.tactic, s.ts, s.what from steps s where regexp_matches(lower(s.what || ' ' || coalesce(s.tactic_note, '')), 'cold email|email lạnh|cold outreach') and s.tactic <> 'g12-outbound-b2b' and s.tactic in ('g1-first-10-users', 'g7-creator-ops', 'g14-press-pr') order by s.video_id;
-- (5) video có bias nêu quảng cáo hoặc tài trợ trong các video có step g12
select v.video_id[:6] as video, v.channel, left(v.bias, 160) as bias from steps s join videos v using(video_id) where s.tactic = 'g12-outbound-b2b' order by 1;
