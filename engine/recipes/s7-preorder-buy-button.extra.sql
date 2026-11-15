-- Số đếm thêm cho s7-preorder-buy-button. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s7-preorder-buy-button.extra.sql
-- (1) loại bằng chứng nhu cầu của case full có step s7
select coalesce(c.demand_kind, 'không nêu') as demand_kind, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's7-preorder-buy-button' group by 1 order by 2 desc;
-- (2) step có tactic_note nhắc dịch vụ làm tay (không phân biệt hoa thường), gồm cả step chỉ host
select count(*) as steps, count(distinct case when case_id is not null then video_id || '/' || case_id end) as case_all,
       sum(case when case_id is null then 1 else 0 end) as steps_host
from steps where tactic = 's7-preorder-buy-button' and tactic_note ilike '%dịch vụ làm tay%';
-- (3) case full có step s7 theo community_insider (true / false / không nêu)
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's7-preorder-buy-button' group by 1 order by 2 desc;
-- (4) case full demand_kind = paid mà có step s7, trên tổng 9 case paid
select count(distinct c.video_id || '/' || c.case_id) as paid_co_step_s7, (select count(*) from cases where depth = 'full' and demand_kind = 'paid') as tong_paid
from cases c where c.depth = 'full' and c.demand_kind = 'paid'
  and exists (select 1 from steps s where s.video_id = c.video_id and s.case_id = c.case_id and s.tactic = 's7-preorder-buy-button');
-- (5) case full có step s7 nhưng demand_kind để trống (video có kể pre-sale ở step, trường nhu cầu không điền)
select c.video_id[:6] as video, c.case_id, c.product
from cases c where c.depth = 'full' and c.demand_kind is null
  and exists (select 1 from steps s where s.video_id = c.video_id and s.case_id = c.case_id and s.tactic = 's7-preorder-buy-button');
