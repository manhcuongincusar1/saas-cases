-- Số đếm thêm cho g2-aso-seo-organic. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g2-aso-seo-organic.extra.sql
-- (1) tách ASO (store, app có sẵn) và SEO (web, kể cả YouTube/Google). ASO = case_id trong danh sách dưới đây (đã đọc từng step); phần còn lại là SEO/web
with a as (select s.*, c.depth, c.months_to_current, c.community_insider,
  case when s.case_id in ('cardstock','coconote','momego','rootd','habit-tracker','habitkit','28-apps-portfolio','wishlists','client-keyword-named-app') or (s.case_id is null and s.video_id like 'Y6Rstw%') then 'ASO' else 'SEO/web' end as nhom
  from steps s left join cases c using(video_id, case_id) where s.tactic = 'g2-aso-seo-organic')
select nhom, count(*) as steps, count(distinct video_id || case_id) filter (where depth = 'full') as case_full, count(distinct video_id || case_id) as tong_case, sum(case when case_id is null then 1 else 0 end) as step_chi_host from a group by 1 order by 1;
-- (2) months_to_current theo nhóm (case full)
with k as (select distinct s.video_id, s.case_id,
  case when s.case_id in ('cardstock','coconote','momego','rootd','habit-tracker','habitkit','28-apps-portfolio','wishlists') then 'ASO' else 'SEO/web' end as nhom
  from steps s join cases c using(video_id, case_id) where s.tactic = 'g2-aso-seo-organic' and c.depth = 'full')
select nhom, count(c.months_to_current) as n, round(median(c.months_to_current), 1) as trung_vi, round(quantile_cont(c.months_to_current, 0.25), 1) as p25, round(quantile_cont(c.months_to_current, 0.75), 1) as p75
from k join cases c using(video_id, case_id) group by 1 order by 1;
-- (3) kiểu SEO (từ khoá trên what + tactic_note; chồng lấn nhau), đếm case full
with x as (select s.video_id, s.case_id, s.what || ' ' || coalesce(s.tactic_note, '') as t from steps s join cases c using(video_id, case_id) where s.tactic = 'g2-aso-seo-organic' and c.depth = 'full')
select 'free tool làm SEO' as kieu, count(distinct video_id || case_id) as case_full from x where regexp_matches(t, 'free tool|công cụ miễn phí|công cụ ký miễn phí', 'i')
union all select 'SEO theo lập trình / landing theo từng cụm từ', count(distinct video_id || case_id) from x where regexp_matches(t, 'programmatic|theo lập trình|từng cụm từ tìm kiếm', 'i')
union all select 'trang so sánh / alternative / từ khoá ý định mua', count(distinct video_id || case_id) from x where regexp_matches(t, 'alternative|so sánh|ý định mua', 'i')
union all select 'blog, hướng dẫn, nội dung dài', count(distinct video_id || case_id) from x where regexp_matches(t, 'blog|hướng dẫn|bài viết|guide|bài hỗ trợ|listicle', 'i')
union all select 'YouTube hoặc video theo từ khoá', count(distinct video_id || case_id) from x where regexp_matches(t, 'YouTube|video', 'i')
union all select 'xin backlink', count(distinct video_id || case_id) from x where regexp_matches(t, 'backlink', 'i');
-- (4) kênh người dùng đầu ghi seo hoặc app_store_search (cả kho, case full), và trong g2
select f.channel, count(distinct f.video_id || '/' || f.case_id) as case_full_ca_kho,
       count(distinct f.video_id || '/' || f.case_id) filter (where exists (select 1 from steps s where s.video_id = f.video_id and s.case_id = f.case_id and s.tactic = 'g2-aso-seo-organic')) as trong_do_co_g2
from first_users f join cases c using(video_id, case_id) where c.depth = 'full' and f.channel in ('seo', 'app_store_search') group by 1 order by 1;
-- (5) case full dùng g2 theo community_insider (true / false = outsider / null = không nêu)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g2-aso-seo-organic' and c.depth = 'full')
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;
-- (6) step theo chặng, theo năm video
select stage, count(*) as steps from steps where tactic = 'g2-aso-seo-organic' group by 1 order by 2 desc;
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g2-aso-seo-organic' group by 1 order by 1;
-- (7) months_to_current từng case full dùng g2 (để thấy độ trải 3 tới 120 tháng)
select distinct c.case_id, c.months_to_current from steps s join cases c using(video_id, case_id) where s.tactic = 'g2-aso-seo-organic' and c.depth = 'full' and c.months_to_current is not null order by 2;
