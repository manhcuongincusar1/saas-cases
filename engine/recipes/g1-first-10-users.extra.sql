-- Số đếm thêm cho g1-first-10-users. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g1-first-10-users.extra.sql
-- (1) step theo chặng, và theo năm video
select stage, count(*) as steps from steps where tactic = 'g1-first-10-users' group by 1 order by 2 desc;
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g1-first-10-users' group by 1 order by 1;
-- (2) case full dùng g1 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g1-first-10-users' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) nhóm cách có người dùng đầu (từ khoá trên what + tactic_note của step g1; các nhóm chồng lấn nhau). Mỗi dòng: số case full có step khớp
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g1-first-10-users' and c.depth = 'full'),
x as (select s.video_id, s.case_id, s.what || ' ' || coalesce(s.tactic_note, '') as t from steps s join g using(video_id, case_id) where s.tactic = 'g1-first-10-users')
select 'Reddit (nhắc Reddit trong step)' as nhom, count(distinct video_id || case_id) as case_full from x where regexp_matches(t, 'reddit', 'i')
union all select 'audience, waitlist, email, khách cũ, đối tác có sẵn', count(distinct video_id || case_id) from x where regexp_matches(t, 'audience sẵn|waitlist|email|follower|khách cũ|khách sẵn|đối tác', 'i')
union all select 'DM, cold, gõ cửa, nhắn trực tiếp, gặp trực tiếp', count(distinct video_id || case_id) from x where regexp_matches(t, 'DM|cold|nhắn|gõ cửa|outreach|gặp trực tiếp|gửi trực tiếp|liên hệ', 'i')
union all select 'bạn bè, người quen, beta nhỏ', count(distinct video_id || case_id) from x where regexp_matches(t, 'bạn bè|người quen|bạn là|người thân|beta', 'i')
union all select 'step nhắc bị chặn, bị khoá, bị lọc, bị giận', count(distinct video_id || case_id) from x where regexp_matches(t, 'chặn|khoá|bị lọc|giận', 'i');
-- (4) case full có first_users reddit trong g1, và trong số đó bao nhiêu không nêu existing_audience
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g1-first-10-users' and c.depth = 'full'),
r as (select * from g where exists (select 1 from first_users f where f.video_id = g.video_id and f.case_id = g.case_id and f.channel = 'reddit'))
select count(*) as reddit_first_users,
       sum(case when not exists (select 1 from advantages a where a.video_id = r.video_id and a.case_id = r.case_id and a.value = 'existing_audience') then 1 else 0 end) as khong_nêu_audience
from r;
-- (5) tổng case full có first_users reddit trên cả kho, để so với (4)
select count(distinct f.video_id || '/' || f.case_id) as reddit_first_users_ca_kho from first_users f join cases c using(video_id, case_id) where c.depth = 'full' and f.channel = 'reddit';
