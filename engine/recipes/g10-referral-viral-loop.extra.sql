-- Số đếm thêm cho g10-referral-viral-loop. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g10-referral-viral-loop.extra.sql
-- (1) cơ chế theo từng case (đã đọc từng step; một case có thể thuộc nhiều cơ chế). Cột: số case, tổng gồm case full và mention
select 'mời bạn để mở khoá (mời 3 bạn)' as co_che, count(distinct video_id || case_id) as so_case from steps where tactic = 'g10-referral-viral-loop' and case_id in ('glam-up', 'glowup')
union all select 'referral trả bằng credit', count(distinct video_id || case_id) from steps where tactic = 'g10-referral-viral-loop' and case_id in ('parakeet-chat')
union all select 'link hoặc asset chia sẻ có tên app', count(distinct video_id || case_id) from steps where tactic = 'g10-referral-viral-loop' and case_id in ('stagetimer', 'magic-music', 'glam-up')
union all select 'vòng xã hội, mật độ, bạn bè kéo bạn bè', count(distinct video_id || case_id) from steps where tactic = 'g10-referral-viral-loop' and case_id in ('lobby', 'shepherd', 'ngl');
-- (2) từng case: depth, doanh thu tự khai, scale_channels, community_insider
select c.case_id, c.depth, c.revenue_amount, c.revenue_unit, c.revenue_basis, c.scale_channels, c.community_insider
from cases c where (c.video_id, c.case_id) in (select video_id, case_id from steps where tactic = 'g10-referral-viral-loop') order by 1;
-- (3) case full dùng g10 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g10-referral-viral-loop' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (4) step theo năm video
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g10-referral-viral-loop' group by 1 order by 1;
