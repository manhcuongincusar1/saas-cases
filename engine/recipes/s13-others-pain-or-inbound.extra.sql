-- Phân loại nhánh s13 là PHÂN LOẠI TAY của người viết theo mô tả step. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s13-others-pain-or-inbound.extra.sql
-- A = nỗi đau của người khác mà founder quan sát hoặc được kể, B = lời nhờ/lời mời/tin nhắn/tweet đến tay
create temp table nhanh as select * from (values
 ('CoqAxV','question-ai','A'),('FIgn-1','dbli','A'),('HBCwzf','stagetimer','A'),('bq3-qH','parakeet-chat','A'),('dWeoSK','locked','A'),('qYYeu0','locked','A'),
 ('4BsxnG','scrape-creators','B'),('9655E1','fitted','B'),('I10xtU','payout','B'),('yue9in','sheets-resume','B'),('zdbimh','jungle','B'),('D4fkiQ','trust-the-mual','B')
) t(v, case_id, nh);
-- kiểm: case có step s13 mà chưa phân loại (phải là 0)
select count(*) as chua_phan_loai from (select distinct video_id, case_id from steps where tactic='s13-others-pain-or-inbound' and case_id is not null) k where not exists (select 1 from nhanh b where k.video_id like b.v || '%' and k.case_id = b.case_id);
-- theo nhánh: case, case full, founder khác nhau
select b.nh, count(*) as cases, sum(case when c.depth='full' then 1 else 0 end) as full_cases, count(distinct c.founder_who) as founders
from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 1;
-- case full theo community_insider (true / false / null), theo nhánh
select b.nh, c.community_insider, count(*) as cases from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id where c.depth='full' group by 1, 2 order by 1, 2;
-- nhánh B (case full): có nêu existing_audience, cofounder/network liên quan audience hoặc một lợi thế nào về audience không
select b.nh, count(*) as cases_full,
  sum(case when exists (select 1 from advantages a where a.video_id=c.video_id and a.case_id=c.case_id and a.value='existing_audience') then 1 else 0 end) as nêu_existing_audience
from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id where c.depth='full' group by 1 order by 1;
-- nhánh nào có bằng chứng nhu cầu trước launch (demand_kind khác null), case full
select b.nh, sum(case when c.demand_kind is not null then 1 else 0 end) as co_bang_chung_nhu_cau, count(*) as cases_full
from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id where c.depth='full' group by 1 order by 1;
-- tháng tới mức hiện tại theo nhánh (n nhỏ)
select b.nh, count(c.months_to_current) as n, round(median(c.months_to_current),1) as trung_vi, min(c.months_to_current) as nho_nhat, max(c.months_to_current) as lon_nhat
from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id where c.depth='full' group by 1 order by 1;
-- step chỉ host của s13
select count(*) as steps_host, count(distinct video_id) as videos from steps where tactic='s13-others-pain-or-inbound' and case_id is null;
-- số founder khác nhau (full)
select count(distinct c.founder_who) as founders_full from (select distinct video_id, case_id from steps where tactic='s13-others-pain-or-inbound' and case_id is not null) k join cases c on c.video_id=k.video_id and c.case_id=k.case_id and c.depth='full';
