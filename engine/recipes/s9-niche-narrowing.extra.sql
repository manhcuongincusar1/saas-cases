-- Phân loại cụm s9 là PHÂN LOẠI TAY của người viết theo mô tả step. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s9-niche-narrowing.extra.sql
-- T = thu hẹp/chọn khe hẹp (gồm đổi khách mục tiêu hoặc tình huống cụ thể), M = mở sang nhóm khách/sản phẩm kề của thứ đang chạy
create temp table cum as select * from (values
 ('7yLgHe','wrestle-ai','T'),('DiRxTf','3ak-track-app','T'),('E_4gRy','coconote','T'),('LRX8TW','packager','T'),('TUN8Y8','visualizee','T'),('mOpYez','pep-ai','T'),('pb4JIH','flame','T'),('spiC5m','local-rank','T'),('tMkpiF','boot-dev','T'),('AoE1yX','attention-design','T'),('NPpky9','hero-analytics','T'),('MLAH5O','alia','T'),('jZ1W85','bro','T'),
 ('32vqaJ','sprout','M'),('Adl5_l','sitegpt','M'),('X2T92M','magicslides','M'),('iVy5J7','task-magic','M'),('xWnqY2','scanemon','M'),('iVy5J7','mail-lead','M'),('iVy5J7','leadquest','M')
) t(v, case_id, cum);
-- kiểm: case có step s9 mà chưa phân loại (phải là 0)
select count(*) as chua_phan_loai from (select distinct video_id, case_id from steps where tactic='s9-niche-narrowing' and case_id is not null) k where not exists (select 1 from cum b where k.video_id like b.v || '%' and k.case_id = b.case_id);
-- theo cụm: case, case full, founder khác nhau
select b.cum, count(*) as cases, sum(case when c.depth='full' then 1 else 0 end) as full_cases, count(distinct c.founder_who) as founders
from cum b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 1;
-- case full theo community_insider (true / false / null)
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s9-niche-narrowing')
select c.community_insider, count(*) as cases from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id group by 1 order by 1;
-- step chỉ host: bao nhiêu video, người nói
select count(*) as steps_host, count(distinct video_id) as videos from steps where tactic='s9-niche-narrowing' and case_id is null;
-- case full có idea_origin nhắc niche_down hoặc adjacent_expansion
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s9-niche-narrowing')
select sum(case when c.idea_origin like '%niche_down%' then 1 else 0 end) as niche_down, sum(case when c.idea_origin like '%adjacent_expansion%' then 1 else 0 end) as adjacent_expansion, count(*) as tong from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id;
-- case full có doanh thu hiện tại quy về USD/tháng đã nêu (chỉ đếm basis monthly hoặc mrr), phân bố
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s9-niche-narrowing')
select c.revenue_basis, count(*) as cases from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id group by 1 order by 2 desc;
-- case full có người đã nêu thất bại trước (prior_failures_count > 0)
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s9-niche-narrowing')
select sum(case when c.prior_failures_count > 0 then 1 else 0 end) as co_that_bai_truoc, count(*) as tong from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id;
