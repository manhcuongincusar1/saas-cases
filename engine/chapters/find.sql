-- Số đếm của mục "Thực tế" chương FIND. Chạy: duckdb kb/data/kb.duckdb < engine/chapters/find.sql
-- (1) tổng case full và số case không nêu idea_origin
select count(*) as case_full, sum(case when idea_origin is null or idea_origin = '' then 1 else 0 end) as khong_nêu_origin from cases where depth = 'full';

-- (2) idea_origin trên case full (một case có thể có nhiều origin)
with o as (select unnest(string_split(idea_origin, ',')) as origin from cases where depth = 'full' and idea_origin <> '')
select origin, count(*) as n from o group by 1 order by 2 desc;

-- (3) founder có thuộc nhóm khách lúc thấy vấn đề không (community_at_discovery.insider)
select coalesce(cast(community_insider as varchar), 'không nêu') as insider, count(*) as n from cases where depth = 'full' group by 1 order by 2 desc;

-- (4) idea_origin của case KHÔNG phải người trong cuộc hoặc không nêu
with o as (select unnest(string_split(idea_origin, ',')) as origin from cases where depth = 'full' and community_insider is not true and idea_origin <> '')
select origin, count(*) as n from o group by 1 order by 2 desc;

-- (5) case full có ít nhất một step dùng tactic tìm bằng công cụ
select count(distinct c.video_id || '/' || c.case_id) as case_full_dung_cong_cu
from cases c join steps s on s.video_id = c.video_id and s.case_id = c.case_id
where c.depth = 'full' and s.tactic in ('s1-revenue-spy','s2-aso-keyword-gap','s2-google-trends-volume','s3-competitor-reviews','s6-upwork-demand');
select count(distinct c.video_id || '/' || c.case_id) as case_full_dung_cong_cu_ca_reddit_tiktok
from cases c join steps s on s.video_id = c.video_id and s.case_id = c.case_id
where c.depth = 'full' and s.tactic in ('s1-revenue-spy','s2-aso-keyword-gap','s2-google-trends-volume','s3-competitor-reviews','s6-upwork-demand','s3-reddit-pain-mining','s4-tiktok-comment-mining');

-- (6) số case full theo tactic tìm ý tưởng (mỗi case tính một lần cho mỗi tactic)
select s.tactic, count(distinct c.video_id || '/' || c.case_id) as case_full
from cases c join steps s on s.video_id = c.video_id and s.case_id = c.case_id
where c.depth = 'full' and s.stage = 'find-idea' and s.tactic is not null group by 1 order by 2 desc;

-- (7) thời gian tới mức doanh thu hiện tại, toàn bộ case full có số
select count(months_to_current) as n, round(median(months_to_current), 1) as trung_vi,
       round(quantile_cont(months_to_current, 0.25), 1) as p25, round(quantile_cont(months_to_current, 0.75), 1) as p75,
       sum(case when months_to_current <= 3 then 1 else 0 end) as tu_3_thang_tro_xuong,
       sum(case when months_to_current <= 1 then 1 else 0 end) as tu_1_thang_tro_xuong
from cases where depth = 'full';

-- (8) tactic find-idea theo nhóm insider; insider = true | null (không nêu) | false (đứng ngoài). Đổi điều kiện ở dòng where để lấy từng nhóm.
select case when c.community_insider is true then 'trong cuộc' when c.community_insider is false then 'đứng ngoài' else 'không nêu' end as nhom,
       s.tactic, count(distinct c.video_id || '/' || c.case_id) as case_full
from cases c join steps s on s.video_id = c.video_id and s.case_id = c.case_id
where c.depth = 'full' and s.stage = 'find-idea' and s.tactic is not null group by 1, 2 order by 1, 3 desc;

-- (9) idea_origin của riêng 21 case đứng ngoài
with o as (select unnest(string_split(idea_origin, ',')) as origin from cases where depth = 'full' and community_insider is false and idea_origin <> '')
select origin, count(*) as n from o group by 1 order by 2 desc;
