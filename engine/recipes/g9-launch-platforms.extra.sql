-- Số đếm thêm cho g9-launch-platforms. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g9-launch-platforms.extra.sql
-- (1) theo nhóm nền tảng (từ khoá trên what + tactic_note của step g9; nhóm chồng lấn một phần). Cột: case full, tổng case, số step
with s as (select s.*, c.depth, s.what || ' ' || coalesce(s.tactic_note, '') as x from steps s left join cases c using(video_id, case_id) where s.tactic = 'g9-launch-platforms')
select 'Product Hunt' as nhom, count(distinct video_id || case_id) filter (where depth = 'full') as case_full, count(distinct video_id || case_id) as tong_case, count(*) as steps from s where regexp_matches(x, 'Product Hunt', 'i')
union all select 'Hacker News / Show HN', count(distinct video_id || case_id) filter (where depth = 'full'), count(distinct video_id || case_id), count(*) from s where regexp_matches(x, 'Hacker News|Show HN', 'i')
union all select 'lifetime deal, AppSumo, RocketHub', count(distinct video_id || case_id) filter (where depth = 'full'), count(distinct video_id || case_id), count(*) from s where regexp_matches(x, 'lifetime|LTD|AppSumo|RocketHub', 'i')
union all select 'marketplace / chợ ứng dụng (không tính Product Hunt, HN)', count(distinct video_id || case_id) filter (where depth = 'full'), count(distinct video_id || case_id), count(*) from s where regexp_matches(x, 'marketplace|chợ ứng dụng|Chrome Web Store|SetApp|App Store|Webflow app|Airtable|Shopify|Google Workspace', 'i') and not regexp_matches(x, 'Product Hunt|Hacker News', 'i')
union all select 'directory, thư mục', count(distinct video_id || case_id) filter (where depth = 'full'), count(distinct video_id || case_id), count(*) from s where regexp_matches(x, 'directory|thư mục', 'i')
union all select 'pre-order, crowdfunding, hackathon', count(distinct video_id || case_id) filter (where depth = 'full'), count(distinct video_id || case_id), count(*) from s where regexp_matches(x, 'pre-order|crowdfunding|Indiegogo|hackathon', 'i');
-- (2) Product Hunt và Hacker News được nhắc ở BẤT KỲ tactic nào (steps có case + first_users), tính theo case
with src as (
  select video_id, case_id, what || ' ' || coalesce(tactic_note, '') as x from steps where case_id is not null
  union all select video_id, case_id, what || ' ' || coalesce(q, '') from first_users)
select 'Product Hunt' as nhom, count(distinct s.video_id || s.case_id) filter (where c.depth = 'full') as case_full, count(distinct s.video_id || s.case_id) as tong_case from src s join cases c using(video_id, case_id) where regexp_matches(x, 'Product Hunt|producthunt', 'i')
union all select 'Hacker News / Show HN', count(distinct s.video_id || s.case_id) filter (where c.depth = 'full'), count(distinct s.video_id || s.case_id) from src s join cases c using(video_id, case_id) where regexp_matches(x, 'Hacker News|Show HN', 'i')
union all select 'Product Hunt hoặc Hacker News', count(distinct s.video_id || s.case_id) filter (where c.depth = 'full'), count(distinct s.video_id || s.case_id) from src s join cases c using(video_id, case_id) where regexp_matches(x, 'Product Hunt|producthunt|Hacker News|Show HN', 'i');
-- (3) case full dùng g9 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g9-launch-platforms' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (4) step theo chặng, theo năm video
select stage, count(*) as steps from steps where tactic = 'g9-launch-platforms' group by 1 order by 2 desc;
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g9-launch-platforms' group by 1 order by 1;
