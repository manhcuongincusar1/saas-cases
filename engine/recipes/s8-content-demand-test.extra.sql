-- Số đếm thêm cho s8-content-demand-test. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s8-content-demand-test.extra.sql
-- (1) loại bằng chứng nhu cầu của case full có step s8 (demand_kind, không nêu = null)
select coalesce(c.demand_kind, 'không nêu') as demand_kind, c.demand_level, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's8-content-demand-test' group by 1, 2 order by 3 desc;
-- (2) case full có step s8 đạt mức 5 trở lên (comment hỏi mua, phỏng vấn lặp, trả tiền)
select count(distinct s.video_id || '/' || s.case_id) as case_full_muc_5_tro_len
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's8-content-demand-test' and c.demand_level >= 5;
-- (3) case full có step s8 theo community_insider (true / false / không nêu)
select coalesce(cast(c.community_insider as varchar), 'không nêu') as insider, count(distinct s.video_id || '/' || s.case_id) as case_full
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's8-content-demand-test' group by 1 order by 2 desc;
-- (4) step gắn case có nhắc landing/page, waitlist, hoặc nội dung đăng (đếm từ khoá trên what + tactic_note, ba nhóm chồng lấn)
select count(*) as step_gan_case,
       sum(case when regexp_matches(what || ' ' || coalesce(tactic_note, ''), 'landing|page|trang', 'i') then 1 else 0 end) as nhac_landing_page,
       sum(case when regexp_matches(what || ' ' || coalesce(tactic_note, ''), 'waitlist', 'i') then 1 else 0 end) as nhac_waitlist,
       sum(case when regexp_matches(what || ' ' || coalesce(tactic_note, ''), 'TikTok|video|Reels|reels|tweet|LinkedIn|Reddit|meme|bài|Instagram|blog', 'i') then 1 else 0 end) as nhac_noi_dung_dang
from steps where tactic = 's8-content-demand-test' and case_id is not null;
-- (5) case full có step s8 mà doanh thu đầu tiên hoặc thanh toán đến trước launch (demand_kind = paid)
select count(distinct s.video_id || '/' || s.case_id) as case_full_paid
from steps s join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
where s.tactic = 's8-content-demand-test' and c.demand_kind = 'paid';
