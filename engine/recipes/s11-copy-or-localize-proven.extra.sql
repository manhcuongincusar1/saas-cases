-- Phân loại biến thể s11 là PHÂN LOẠI TAY của người viết theo mô tả step (what, tactic_note), không phải trường trong DB. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s11-copy-or-localize-proven.extra.sql
-- A = chép nguyên mẫu, B1 = bản địa hoá thị trường/ngôn ngữ, B2 = chuyển nền tảng/kênh, C1 = remix đổi ngách/đối tượng/chủ đề, C2 = làm tốt hơn/đẹp hơn/đơn giản hơn cùng ngách
create temp table bien_the as select * from (values
 ('7Jtttj','boost-app-social','A'),('F8i0kk','papermark','A'),('I10xtU','payout','A'),('zrsGDD','glowly','A'),('qIlX7c','duckmath','A'),('zFfBuy','sunflower','A'),
 ('GQ27QV','calbuddy','B1'),
 ('DTree0','ngl','B2'),('NvtsM8','data-fetcher','B2'),('si3Hzk','stronger','B2'),
 ('32vqaJ','glam-up','C1'),('Bf12MN','glam-up','C1'),('CAi50V','scanamon','C1'),('NmIHgC','preycreen','C1'),('yw5iIg','runafy','C1'),('orYTlk','stoppr','C1'),('D7eaHc','copia','C1'),('s9aLA4','geosports','C1'),('PSx0vc','veed-io','C1'),
 ('2dfMUt','gravl','C2'),('BNr1JO','supergrow','C2'),('w8oUlf','signaturely','C2'),('wvYej-','letterly','C2'),('gU9FtZ','oceans','C2'),('g9J_-5','habit-tracker','C2'),('Nnpz1w','shipper','C2'),('yBjcmM','prayer-lock','C2'),('PmyXmp','bible-buddy','C2'),('PIXXEA','cut-coach','C2')
) t(v, case_id, bt);
-- kiểm: số case có step s11 mà không có trong bảng phân loại (phải là 0)
select count(*) as chua_phan_loai from (select distinct video_id, case_id from steps where tactic='s11-copy-or-localize-proven' and case_id is not null) k where not exists (select 1 from bien_the b where k.video_id like b.v || '%' and k.case_id = b.case_id);
-- theo biến thể: case, founder khác nhau, case full, số case có kênh trả tiền, tháng tới hiện tại
select b.bt, count(*) as cases, count(distinct c.founder_who) as founders, sum(case when c.depth='full' then 1 else 0 end) as full_cases,
  sum(case when c.scale_channels like '%paid_%' or c.scale_channels like '%influencer_paid%' then 1 else 0 end) as co_kenh_tra_tien,
  count(c.months_to_current) as n_thang, round(median(c.months_to_current),1) as trung_vi_thang
from bien_the b join cases c on c.video_id like b.v || '%' and c.case_id = b.case_id group by 1 order by 1;
-- case full theo community_insider (true / false / null)
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s11-copy-or-localize-proven')
select c.community_insider, count(*) as cases from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id group by 1 order by 1;
-- số founder khác nhau (full) dùng s11
select count(distinct c.founder_who) as founders_full from (select distinct s.video_id, s.case_id from steps s where s.tactic='s11-copy-or-localize-proven' and s.case_id is not null) k join cases c on c.video_id=k.video_id and c.case_id=k.case_id and c.depth='full';
-- case full có step s11 mà idea_origin nhắc trend_copy hoặc revenue_scouting
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s11-copy-or-localize-proven')
select sum(case when c.idea_origin like '%trend_copy%' then 1 else 0 end) as trend_copy, sum(case when c.idea_origin like '%revenue_scouting%' then 1 else 0 end) as revenue_scouting, count(*) as tong from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id;
-- case full có demand_kind nêu bằng chứng nhu cầu là doanh thu sản phẩm tương tự (similar_product_revenue)
with k as (select distinct s.video_id, s.case_id from steps s join cases c on c.video_id=s.video_id and c.case_id=s.case_id and c.depth='full' where s.tactic='s11-copy-or-localize-proven')
select c.demand_kind, count(*) as cases from k join cases c on c.video_id=k.video_id and c.case_id=k.case_id group by 1 order by 2 desc;
