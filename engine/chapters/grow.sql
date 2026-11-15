-- Số đếm của mục "Thực tế" chương GROW (phần 1). Chạy: duckdb kb/data/kb.duckdb < engine/chapters/grow.sql
-- (1) tổng case full
select count(*) as case_full from cases where depth = 'full';

-- (2) kênh người dùng đầu tiên (first_users.channel), case full; một case có thể có nhiều kênh
select f.channel, count(distinct f.video_id || '/' || f.case_id) as so_case
from first_users f join cases c on c.video_id = f.video_id and c.case_id = f.case_id
where c.depth = 'full' group by 1 order by 2 desc;

-- (3) case full có ít nhất một dòng first_users, và case full không có dòng nào
select count(distinct c.video_id || '/' || c.case_id) filter (where exists (select 1 from first_users f where f.video_id = c.video_id and f.case_id = c.case_id)) as co_first_users,
       count(distinct c.video_id || '/' || c.case_id) filter (where not exists (select 1 from first_users f where f.video_id = c.video_id and f.case_id = c.case_id)) as khong_nêu_first_users
from cases c where c.depth = 'full';

-- (4) kênh scale trả tiền (paid_*, influencer_paid) / thuần organic / không nêu, case full
select sum(case when scale_channels like '%paid_%' or scale_channels like '%influencer_paid%' then 1 else 0 end) as co_kenh_tra_tien,
       sum(case when scale_channels is not null and scale_channels <> ''
                 and scale_channels not like '%paid_%' and scale_channels not like '%influencer_paid%' then 1 else 0 end) as thuan_organic,
       sum(case when scale_channels is null or scale_channels = '' then 1 else 0 end) as khong_neu
from cases where depth = 'full';

-- (5) thời gian tới mức doanh thu hiện tại, toàn bộ case full có số
select count(months_to_current) as n, round(median(months_to_current), 1) as trung_vi,
       round(quantile_cont(months_to_current, 0.25), 1) as p25, round(quantile_cont(months_to_current, 0.75), 1) as p75,
       sum(case when months_to_current <= 3 then 1 else 0 end) as tu_3_thang_tro_xuong,
       sum(case when months_to_current <= 1 then 1 else 0 end) as tu_1_thang_tro_xuong
from cases where depth = 'full';

-- (6) số case (full / tổng) theo tactic grow; mỗi case tính một lần cho mỗi tactic
select s.tactic,
       count(distinct s.video_id || '/' || s.case_id) filter (where c.depth = 'full') as case_full,
       count(distinct s.video_id || '/' || s.case_id) as case_tong,
       sum(case when s.case_id is null then 1 else 0 end) as step_chi_host
from steps s left join cases c on c.video_id = s.video_id and c.case_id = s.case_id
where s.tactic like 'g%' and s.tactic not in ('other') group by 1 order by 2 desc;
