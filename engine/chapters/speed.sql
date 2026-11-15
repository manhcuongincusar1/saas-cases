-- Mục "Tốc độ": các case có số tháng tới mốc $10k MRR, kèm đường tới audience của từng case. Chạy: duckdb kb/data/kb.duckdb < engine/chapters/speed.sql
-- (1) 10 case có months_to_10k_mrr (founder tự khai; mốc tính từ lúc ra mắt hoặc từ lúc bắt đầu, video không thống nhất)
select c.case_id, c.months_to_10k_mrr, c.months_to_current, c.revenue_amount, c.revenue_basis
from cases c where c.depth = 'full' and c.months_to_10k_mrr is not null order by c.months_to_10k_mrr, c.case_id;

-- (2) lợi thế liên quan audience của từng case trong (1): existing_audience, prior_success, network, capital
select c.case_id, c.months_to_10k_mrr,
       string_agg(distinct a.value, ', ') filter (where a.value in ('existing_audience','prior_success','network','capital')) as loi_the_neu
from cases c left join advantages a on a.video_id = c.video_id and a.case_id = c.case_id
where c.depth = 'full' and c.months_to_10k_mrr is not null group by 1, 2 order by 2, 1;

-- (3) kênh người dùng đầu tiên của từng case trong (1)
select c.case_id, c.months_to_10k_mrr, string_agg(distinct u.channel, ', ') as kenh_dau
from cases c left join first_users u on u.video_id = c.video_id and u.case_id = c.case_id
where c.depth = 'full' and c.months_to_10k_mrr is not null group by 1, 2 order by 2, 1;
