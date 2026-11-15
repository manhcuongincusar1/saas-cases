-- engine/scripts/recipe_stats.py g11-positioning-messaging; chạy lại: duckdb kb/data/kb.duckdb < engine/recipes/g11-positioning-messaging.sql

-- đếm
select count(*) as steps,
       count(distinct video_id) as videos,
       count(distinct case when case_id is not null then video_id || '/' || case_id end) as cases_all,
       sum(case when case_id is null then 1 else 0 end) as steps_host_only
from steps where tactic = 'g11-positioning-messaging';

-- case full + giống user
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = 'g11-positioning-messaging'
)
select count(*) as cases_full,
       sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id
                                 and a.value in ('existing_audience','capital','network','prior_success')) then 1 else 0 end) as khong_neu_4_loi_the,
       sum(case when not exists (select 1 from advantages a where a.video_id = k.video_id and a.case_id = k.case_id
                                 and a.value = 'existing_audience') then 1 else 0 end) as khong_neu_audience,
       sum(case when exists (select 1 from cases c where c.video_id = k.video_id and c.case_id = k.case_id and c.demand_kind is null) then 1 else 0 end) as khong_ke_bang_chung_nhu_cau
from k;

-- months_to_current
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = 'g11-positioning-messaging'
)
select count(c.months_to_current) as n,
       round(median(c.months_to_current), 1) as trung_vi,
       round(quantile_cont(c.months_to_current, 0.25), 1) as p25,
       round(quantile_cont(c.months_to_current, 0.75), 1) as p75
from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id;

-- kênh trả tiền hay organic (scale_channels)
with k as (
  select distinct s.video_id, s.case_id from steps s
  join cases c on c.video_id = s.video_id and c.case_id = s.case_id and c.depth = 'full'
  where s.tactic = 'g11-positioning-messaging'
)
select sum(case when c.scale_channels like '%paid_%' or c.scale_channels like '%influencer_paid%' then 1 else 0 end) as co_kenh_tra_tien,
       sum(case when c.scale_channels is not null and c.scale_channels <> ''
                 and c.scale_channels not like '%paid_%' and c.scale_channels not like '%influencer_paid%' then 1 else 0 end) as thuan_organic,
       sum(case when c.scale_channels is null or c.scale_channels = '' then 1 else 0 end) as khong_neu
from k join cases c on c.video_id = k.video_id and c.case_id = k.case_id;
