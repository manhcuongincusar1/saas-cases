-- Số đếm thêm cho g11-positioning-messaging. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g11-positioning-messaging.extra.sql
-- (1) step theo chặng
select stage, count(*) as steps from steps where tactic = 'g11-positioning-messaging' group by 1 order by 2 desc;
-- (2) step theo case (6 ký tự đầu video_id, HOST là step do host mô tả)
select substr(video_id, 1, 6) as v, coalesce(case_id, 'HOST') as ca, count(*) as steps from steps where tactic = 'g11-positioning-messaging' group by 1, 2 order by 3 desc, 2;
-- (3) case full dùng g11 theo community_insider (true là người trong cuộc, false là outsider, null là video không nêu: đừng gộp false với null)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g11-positioning-messaging' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (4) doanh thu tự khai và tháng tới mức doanh thu hiện tại của từng case (revenue_evidence cho biết có số kiểm chứng hay không)
select distinct substr(c.video_id, 1, 6) as v, c.case_id, c.revenue_amount, c.revenue_basis, c.revenue_evidence, c.months_to_current from steps s join cases c using(video_id, case_id) where s.tactic = 'g11-positioning-messaging' order by 2;
-- (5) kênh người dùng đầu của case full dùng g11 (first_users), một case có thể có nhiều kênh hoặc không có dòng nào
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g11-positioning-messaging' and c.depth = 'full')
select coalesce(f.channel, 'không có dòng first_users') as channel, count(distinct g.video_id || '/' || g.case_id) as case_full from g left join first_users f using(video_id, case_id) group by 1 order by 2 desc;
