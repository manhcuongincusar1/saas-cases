-- Số đếm thêm cho g5-retention. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g5-retention.extra.sql
-- (1) step theo kênh và loại video, step không gắn case
select v.channel, v.kind, count(*) as steps, sum(case when s.case_id is null then 1 else 0 end) as steps_khong_gan_case, count(distinct s.video_id) as videos
from steps s join videos v using(video_id) where s.tactic = 'g5-retention' group by 1, 2 order by 1, 2;
-- (2) case full dùng g5 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g5-retention' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) nhóm việc (từ khoá trên what + tactic_note + tool; các nhóm chồng lấn nhau). Mỗi dòng: số case full có step khớp
with k as (select s.*, coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,'') || ' ' || coalesce(s.tool,'') as t from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full' where s.tactic = 'g5-retention')
select 'nói chuyện, hỗ trợ, xin phản hồi hoặc review' as nhom, count(distinct video_id || '/' || case_id) as case_full from k where regexp_matches(t, 'nói chuyện|gọi|nhắn|hỗ trợ|support|review|phản hồi|feedback|liên lạc|DM|chat|ghi màn hình|ghi âm|Intercom', 'i')
union all select 'thông báo, nhắc, SMS, widget, trigger hằng ngày', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'thông báo|nhắc|SMS|widget|trigger', 'i')
union all select 'huỷ, churn, bán chéo, cộng đồng người mua', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'huỷ|churn|bán chéo|Telegram|quay lại', 'i')
union all select 'đo power user, analytics, retention', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'power user|analytics|Mixpanel|PostHog|retention|cohort', 'i');
-- (4) số retention hoặc churn founder tự nêu (trường cost, threshold, hoặc trong mô tả step); tự khai, không phải chuẩn của kho
select c.product, s.ts, s.what, s.threshold from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 'g5-retention' and (regexp_matches(s.what || ' ' || coalesce(s.threshold, ''), 'retention|churn|giữ được|giữ [0-9]') and regexp_matches(s.what || ' ' || coalesce(s.threshold, ''), '[0-9]%')) order by 1, 2;
-- (5) step theo chặng
select stage, count(*) as steps from steps where tactic = 'g5-retention' group by 1 order by 2 desc;
