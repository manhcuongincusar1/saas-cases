-- Phân loại nhánh s4 là PHÂN LOẠI TAY của người viết theo mô tả step. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s4-tiktok-comment-mining.extra.sql
-- X = soi trend/format viral để chọn ý tưởng, Y = đọc comment để tìm hoặc xác nhận nhu cầu
create temp table nhanh as select * from (values
 ('-VlJIg','flame','X'),('1nfPvJ','naturalwrite','X'),('zpTXi8','payout','X'),('QXxESN','vugola','X'),('hKqLce','puffcount','X'),('D7eaHc','copia','X'),
 ('EQfZCe','go-tall','Y'),('FIgn-1','dbli','Y'),('LYdJ3d','glowup','Y'),('Eg93po','stella','Y'),('CwHD6F','payout','Y'),('orYTlk','stoppr','Y'),('W48emw','bulkmockup','Y')
) t(v, case_id, nh);
-- kiểm: case có step s4 mà chưa phân loại (phải là 0)
select count(*) as chua_phan_loai from (select distinct video_id, case_id from steps where tactic='s4-tiktok-comment-mining' and case_id is not null) k where not exists (select 1 from nhanh b where k.video_id like b.v || '%' and k.case_id = b.case_id);
-- theo nhánh: case, founder khác nhau (đếm theo tên trong DB, Connor Burd và Connor là một người ở hai video)
select b.nh, count(*) as cases, count(distinct c.founder_who) as ten_khac_nhau
from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 1;
-- case full theo community_insider (true / false / null)
select c.community_insider, count(*) as cases from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 1;
-- loại bằng chứng nhu cầu trước launch (demand_kind) của 13 case
select c.demand_kind, count(*) as cases from nhanh b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 2 desc;
-- step chỉ host: bao nhiêu step theo giai đoạn (stage)
select stage, count(*) as steps from steps where tactic='s4-tiktok-comment-mining' and case_id is null group by 1 order by 1;
-- step của founder (có case): theo giai đoạn
select stage, count(*) as steps from steps where tactic='s4-tiktok-comment-mining' and case_id is not null group by 1 order by 1;
-- step nhắc đúng khung VSC hoặc comment hỏi tên app (từ khoá trên what + tactic_note)
select count(*) as steps_nhac_vsc_hoac_hoi_app from steps where tactic='s4-tiktok-comment-mining' and regexp_matches(what || ' ' || coalesce(tactic_note,''), 'VSC|hỏi tên app|hỏi app|hỏi cách', 'i');
-- số founder (case) có step là đọc comment (từ khoá comment trên what), không tính host
select count(distinct video_id || '/' || case_id) as cases_doc_comment from steps where tactic='s4-tiktok-comment-mining' and case_id is not null and regexp_matches(what, 'comment', 'i');
