-- Số đếm thêm cho g8-funnel-measurement. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g8-funnel-measurement.extra.sql
-- (1) step theo kênh và loại video, step không gắn case. Kênh Superwall bán paywall, Starter Story bán chương trình riêng
select v.channel, v.kind, count(*) as steps, sum(case when s.case_id is null then 1 else 0 end) as steps_khong_gan_case, count(distinct s.video_id) as videos
from steps s join videos v using(video_id) where s.tactic = 'g8-funnel-measurement' group by 1, 2 order by 1, 2;
-- (2) case full dùng g8 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g8-funnel-measurement' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) nhóm việc (từ khoá trên what + tactic_note + tool; các nhóm chồng lấn nhau). Mỗi dòng: số case full có step khớp
with k as (select s.*, coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,'') || ' ' || coalesce(s.tool,'') as t from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full' where s.tactic = 'g8-funnel-measurement')
select 'phễu, drop-off, bước rơi' as nhom, count(distinct video_id || '/' || case_id) as case_full from k where regexp_matches(t, 'phễu|drop-off|bước rơi|funnel|view, click|view → cài', 'i')
union all select 'attribution: UTM, coupon, creator code, spike, tên miền, MMP', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'UTM|coupon|creator code|attribution|ManyChat|custom product page|spike|tên miền|AppsFlyer|MMP|link riêng|Post Hook', 'i')
union all select 'chi phí và lợi nhuận: ROAS, CPA, CPI, CPM, LTV, P&L', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'ROAS|CPA|CPI|CPM|RPM|LTV|P&L|chi phí mỗi|hoà vốn|mỗi đô', 'i')
union all select 'công cụ đo: PostHog, Mixpanel, RevenueCat, Superwall, Amplitude, AppsFlyer', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'PostHog|Mixpanel|RevenueCat|Superwall|Amplitude|AppsFlyer', 'i')
union all select 'thí nghiệm, A/B test, OKR', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'A/B|AB test|thí nghiệm|OKR', 'i')
union all select 'đo nội dung: view, 3 giây, playbook', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'view|3 giây|watch time|playbook', 'i');
-- (4) step theo năm video
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g8-funnel-measurement' group by 1 order by 1;
-- (5) step theo chặng
select stage, count(*) as steps from steps where tactic = 'g8-funnel-measurement' group by 1 order by 2 desc;
-- (6) step có số cụ thể ở trường threshold hoặc cost (founder hoặc expert nêu)
select count(*) as steps_co_so, (select count(*) from steps where tactic = 'g8-funnel-measurement') as tong_steps from steps where tactic = 'g8-funnel-measurement' and (threshold is not null or cost is not null);
