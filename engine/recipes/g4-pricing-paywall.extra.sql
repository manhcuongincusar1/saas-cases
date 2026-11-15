-- Số đếm thêm cho g4-pricing-paywall. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g4-pricing-paywall.extra.sql
-- (1) step theo kênh và loại video, step chỉ host, và case full theo kênh. Kênh Superwall bán paywall (có lợi ích thương mại)
select v.channel, v.kind, count(*) as steps, sum(case when s.case_id is null then 1 else 0 end) as steps_host_only, count(distinct s.video_id) as videos
from steps s join videos v using(video_id) where s.tactic = 'g4-pricing-paywall' group by 1, 2 order by 1, 2;
select v.channel, count(*) as steps, sum(case when s.case_id is null then 1 else 0 end) as steps_host_only
from steps s join videos v using(video_id) where s.tactic = 'g4-pricing-paywall' group by 1 order by 1;
select v.channel, v.kind, c.depth, count(distinct s.video_id || '/' || s.case_id) as cases
from steps s join videos v using(video_id) join cases c on c.video_id = s.video_id and c.case_id = s.case_id
where s.tactic = 'g4-pricing-paywall' group by 1, 2, 3 order by 1, 2, 3;
-- (2) case full dùng g4 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g4-pricing-paywall' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (3) chia mục con: mỗi step vào ĐÚNG MỘT nhóm theo từ khoá trên what + tactic_note, ưu tiên theo thứ tự D, E, F, C, B, A (xấp xỉ; đọc step để chắc)
-- D onboarding dẫn tới paywall; E khuyến mãi, ưu đãi khi thoát, winback; F thí nghiệm giá/paywall và đo; C paywall và trial; B mô hình và thời điểm thu tiền; A chọn giá và gói
create or replace temp view g4 as
select s.*, v.channel,
 case
  when regexp_matches(coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,''), 'onboarding|quiz|quét khuôn mặt', 'i') then 'D onboarding dẫn tới paywall'
  when regexp_matches(coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,''), 'giảm giá|giảm [0-9]|giảm khoảng|giảm nửa|ưu đãi|khuyến mãi|thoát paywall|đóng paywall|abandon|vòng quay|limited time|limited spots|suất|mã giảm|drawer|offer', 'i') then 'E khuyến mãi, ưu đãi khi thoát'
  when regexp_matches(coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,''), 'A/B|AB test|Superwall|RevenueCat|mixed panel|LTV|ROAS|thử các mức|thử mức|tăng giá|hạ giá|đổi giá|thử nghiệm|test', 'i') then 'F thí nghiệm giá và đo'
  when regexp_matches(coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,''), 'paywall|trial|dùng thử|placement|nút X|hard|soft', 'i') then 'C paywall và trial'
  when regexp_matches(coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,''), 'freemium|miễn phí|lifetime|trọn đời|một lần|credit|usage|Stripe|bản beta|bật thu|chưa thu|bắt đầu thu|bắt đầu bán|pay-as-you-go|open-core|PLG|không có gói|bỏ hẳn gói|bắt trả|bật in-app|mới bật|hết tiền|banner|web và app|ra gói subscription|Bật giá|trả phí', 'i') then 'B mô hình và thời điểm thu tiền'
  else 'A chọn giá và gói' end as grp
from steps s join videos v using(video_id) where s.tactic = 'g4-pricing-paywall';
select grp, count(*) as steps,
       sum(case when case_id is null then 1 else 0 end) as steps_host_only,
       sum(case when channel = 'superwall' then 1 else 0 end) as steps_superwall,
       sum(case when channel = 'starter-story' then 1 else 0 end) as steps_starter_story,
       count(distinct case when case_id is not null then video_id || '/' || case_id end) as cases_all
from g4 group by 1 order by 1;
select g4.grp, count(distinct g4.video_id || '/' || g4.case_id) as cases_full
from g4 join cases c on c.video_id = g4.video_id and c.case_id = g4.case_id and c.depth = 'full' group by 1 order by 1;
-- (4) từ khoá trong step (các nhóm chồng lấn; mỗi dòng: số case full có step khớp)
with k as (select s.*, coalesce(s.what,'') || ' ' || coalesce(s.tactic_note,'') as t from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full' where s.tactic = 'g4-pricing-paywall')
select 'hard paywall, paywall cứng, không có gói miễn phí' as nhom, count(distinct video_id || '/' || case_id) as case_full from k where regexp_matches(t, 'hard|paywall cứng|không có gói miễn phí|không freemium', 'i')
union all select 'freemium hoặc gói miễn phí', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'freemium|gói free|gói miễn phí|bản miễn phí|premium có', 'i')
union all select 'trial, dùng thử', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'trial|dùng thử', 'i')
union all select 'gói tuần', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'gói tuần|/tuần|tuần \$|tuần khoảng', 'i')
union all select 'gói năm', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'gói năm|/năm|năm \$', 'i')
union all select 'lifetime, trọn đời, LTD, mua một lần', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'lifetime|trọn đời|LTD|một lần', 'i')
union all select 'credit, usage, pay-as-you-go', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'credit|usage|pay-as-you-go', 'i')
union all select 'retainer, theo đầu người, enterprise, B2B', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'retainer|đầu người|enterprise|B2B', 'i')
union all select 'Stripe, web (thanh toán ngoài App Store)', count(distinct video_id || '/' || case_id) from k where regexp_matches(t, 'Stripe|web app|trên web|web và app', 'i');
-- (5) danh sách giá founder nêu: step case full có số tiền và gói tuần/năm. Một case một dòng; con số tự khai, không phải chuẩn của kho
select c.product, s.ts, s.what from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 'g4-pricing-paywall' and regexp_matches(s.what, '\$[0-9]|[0-9] ?USD') and regexp_matches(s.what, 'tuần|năm') order by c.product, s.ts;
-- (6) ước lượng tháng tới mức doanh thu hiện tại, theo mục con (case full có step trong nhóm)
select g4.grp, count(c.months_to_current) as n, round(median(c.months_to_current), 1) as trung_vi
from g4 join cases c on c.video_id = g4.video_id and c.case_id = g4.case_id and c.depth = 'full' group by 1 order by 1;
-- (7) loại sản phẩm của case full dùng g4, theo kênh: mobile/iOS hay loại khác (web, API, agency...)
with k as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g4-pricing-paywall' and c.depth = 'full')
select v.channel, sum(case when regexp_matches(c.type, 'mobile|ios') then 1 else 0 end) as mobile_ios, sum(case when not regexp_matches(c.type, 'mobile|ios') then 1 else 0 end) as loai_khac, count(*) as cases_full
from k join cases c using(video_id, case_id) join videos v using(video_id) group by 1 order by 1;
-- (8) step nhắc tên công cụ Superwall (A/B test paywall), theo kênh
select v.channel, count(*) as steps_nhac_superwall, count(distinct s.video_id) as videos
from steps s join videos v using(video_id) where s.tactic = 'g4-pricing-paywall' and regexp_matches(s.what || ' ' || coalesce(s.tactic_note, ''), 'Superwall') group by 1 order by 1;
-- (9) case full dùng g4 có months_to_10k_mrr (mốc 10k, tự khai)
select c.product, c.months_to_10k_mrr from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full' where s.tactic = 'g4-pricing-paywall' and c.months_to_10k_mrr is not null group by 1, 2 order by 2;
