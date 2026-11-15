-- Số đếm thêm cho g6-paid-ads. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g6-paid-ads.extra.sql
-- Tiền trong kho là số founder (hoặc host) nêu, một case một con số. Các nhóm theo từ khoá CHỒNG LẤN nhau. "Case full" = case depth full.

-- (1) step theo chặng, theo năm video, theo kênh video
select stage, count(*) as steps from steps where tactic = 'g6-paid-ads' group by 1 order by 2 desc;
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g6-paid-ads' group by 1 order by 1;
select v.channel, count(*) as steps, count(distinct s.video_id) as videos, sum(case when s.case_id is null then 1 else 0 end) as chi_host from steps s join videos v using(video_id) where s.tactic = 'g6-paid-ads' group by 1 order by 2 desc;

-- (2) case full dùng g6 theo community_insider (true / false = outsider / không nêu = null)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g6-paid-ads' and c.depth = 'full')
select case when c.community_insider is true then 'insider' when c.community_insider is false then 'outsider' else 'không nêu' end as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;

-- (3) nền tảng: đếm trên trường có cấu trúc cases.scale_channels của case full dùng g6 (một case có thể có nhiều nền tảng)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g6-paid-ads' and c.depth = 'full')
select 'paid_meta' as nen_tang, count(*) as case_full from g join cases c using(video_id, case_id) where c.scale_channels like '%paid_meta%'
union all select 'paid_tiktok', count(*) from g join cases c using(video_id, case_id) where c.scale_channels like '%paid_tiktok%'
union all select 'paid_google', count(*) from g join cases c using(video_id, case_id) where c.scale_channels like '%paid_google%'
union all select 'paid_apple_search', count(*) from g join cases c using(video_id, case_id) where c.scale_channels like '%paid_apple_search%'
union all select 'paid_unspecified', count(*) from g join cases c using(video_id, case_id) where c.scale_channels like '%paid_unspecified%'
union all select 'influencer_paid (không phải g6, để đối chiếu)', count(*) from g join cases c using(video_id, case_id) where c.scale_channels like '%influencer_paid%'
union all select 'không có kênh paid nào trong scale_channels', count(*) from g join cases c using(video_id, case_id) where coalesce(c.scale_channels, '') not like '%paid_%' and coalesce(c.scale_channels, '') not like '%influencer_paid%';

-- (4) nhóm theo nền tảng nhắc trong step (từ khoá trên what + tactic_note), chồng lấn. Mỗi dòng: step, case full, step chỉ host
with x as (
  select s.video_id, s.case_id, c.depth, lower(s.what || ' ' || coalesce(s.tactic_note, '')) as t from steps s left join cases c using(video_id, case_id) where s.tactic = 'g6-paid-ads'
), m as (
  select *, 'Meta (Facebook, Instagram)' as nhom from x where regexp_matches(t, 'meta|facebook|instagram')
  union all select *, 'TikTok Ads, Spark Ads' from x where regexp_matches(t, 'tiktok ads|spark|smart plus|chạy tiktok|ads trên tiktok|quảng cáo tiktok')
  union all select *, 'Google (Search, App Campaigns, YouTube)' from x where regexp_matches(t, 'google|youtube|infeed')
  union all select *, 'Apple Search Ads' from x where regexp_matches(t, 'apple')
  union all select *, 'khác (Twitter, LinkedIn, influencer boost)' from x where regexp_matches(t, 'twitter|linkedin')
  union all select *, 'không nêu nền tảng' from x where regexp_matches(t, 'không nêu nền tảng|nền tảng không nêu|paid_unspecified|không nói nền tảng|video không nêu nền tảng|chưa nói rõ')
)
select nhom, count(*) as steps, count(distinct case when depth = 'full' then video_id || '/' || case_id end) as case_full, sum(case when case_id is null then 1 else 0 end) as chi_host from m group by 1 order by 1;

-- (5) thời điểm so với organic: chỉ tính khi what hoặc tactic_note NÓI RÕ (đọc tay từng step, danh sách tường minh theo video prefix + case)
with truoc(vp, cid) as (values ('EF3uyv','bank-statement-converter'), ('8BtHk-','story-short'), ('KgS3hb','canary'), ('g9J_-5','habit-tracker'), ('DPb-M0','chartdetector')),
sau(vp, cid) as (values ('7yLgHe','wrestle-ai'), ('9655E1','fitted'), ('AtYlYz','bloom'), ('EQfZCe','go-tall'), ('I10xtU','payout'), ('PIXXEA','cut-coach'), ('ST2ROU','pushscroll'),
  ('_a4ch3','vert-ventures'), ('aLidq3','maxed-ai'), ('gpn1jE','habitkit'), ('lXGmWd','sizzle-ai'), ('mOpYez','pep-ai'), ('qGIWJB','gym-app-lipa'), ('rGLXc1','money-ai'), ('ukGtpn','sway-ai'),
  ('vw2Yc4','28-apps-portfolio'), ('xeUhKu','outrank'), ('zPijWd','make-logo-ai'), ('KgS3hb','canary'), ('P4Qode','snag'), ('hKqLce','puffcount'), ('g9J_-5','habit-tracker'), ('NmIHgC','preycreen'), ('VZ1Xsp','arvow'))
select 'nói rõ chạy từ đầu hoặc trước organic' as nhom, count(distinct c.video_id || c.case_id) as case_full_co_step_g6, string_agg(distinct t.cid, ', ') as cac_case
from truoc t join cases c on c.video_id like t.vp || '%' and c.case_id = t.cid and c.depth = 'full' join steps s on s.video_id = c.video_id and s.case_id = c.case_id and s.tactic = 'g6-paid-ads'
union all
select 'nói rõ chạy sau khi có organic hoặc video thắng', count(distinct c.video_id || c.case_id), string_agg(distinct t.cid, ', ')
from sau t join cases c on c.video_id like t.vp || '%' and c.case_id = t.cid and c.depth = 'full' join steps s on s.video_id = c.video_id and s.case_id = c.case_id and s.tactic = 'g6-paid-ads'
union all
select 'nằm ở cả hai nhóm', count(*), string_agg(t.cid, ', ') from truoc t join sau u on u.vp = t.vp and u.cid = t.cid;

-- (6) tiền do founder nêu ở step g6 của case full (cột cost hoặc threshold có số). Mỗi dòng một step
select s.video_id[:6] as video, s.case_id, s.ts, s.cost, s.threshold
from steps s join cases c using(video_id, case_id)
where s.tactic = 'g6-paid-ads' and c.depth = 'full' and regexp_matches(coalesce(s.cost, '') || ' ' || coalesce(s.threshold, ''), '[0-9]')
order by s.video_id, s.ts;

-- (7) tiền, ngưỡng do HOST nêu (case_id null) ở step g6
select s.video_id[:6] as video, v.channel, s.ts, s.cost, s.threshold
from steps s join videos v using(video_id)
where s.tactic = 'g6-paid-ads' and s.case_id is null and regexp_matches(coalesce(s.cost, '') || ' ' || coalesce(s.threshold, ''), '[0-9]')
order by s.video_id, s.ts;

-- (8) case full có step g6 mà step ghi lỗ, hoà vốn, bỏ hoặc không đáng (nhóm theo từ khoá trên what + tactic_note)
select s.video_id[:6] as video, s.case_id, s.ts, s.what
from steps s join cases c using(video_id, case_id)
where s.tactic = 'g6-paid-ads' and c.depth = 'full' and regexp_matches(lower(s.what || ' ' || coalesce(s.tactic_note, '')), 'không có lời|không hoà vốn|cắt quảng cáo|bỏ |không thích biên|biên lợi nhuận giảm|không đủ kinh tế|kém hiệu quả|không còn hiệu quả|giảm khi chi|khoá vĩnh viễn|tiết kiệm')
order by s.video_id, s.ts;

-- (9) case full có cả g6 và g7 (trả creator rồi chạy paid, hoặc ngược lại)
select count(*) as case_full_ca_g6_va_g7 from (
  select distinct a.video_id, a.case_id from steps a join steps b on a.video_id = b.video_id and a.case_id = b.case_id and b.tactic = 'g7-creator-ops'
  join cases c on c.video_id = a.video_id and c.case_id = a.case_id and c.depth = 'full' where a.tactic = 'g6-paid-ads'
);

-- (10) video có bias nêu nền tảng hoặc công ty BÁN creator/UGC/phân phối (Sideshift, Arcads, Clover, Noise, Pebble) và số step g6 của chúng
select v.video_id[:6] as video, v.channel, count(*) as steps_g6, sum(case when s.case_id is null then 1 else 0 end) as chi_host
from steps s join videos v using(video_id)
where s.tactic = 'g6-paid-ads' and regexp_matches(lower(v.bias), 'arcads|sideshift|noise|clover|pebble')
group by 1, 2 order by 3 desc;
-- (11) tổng của (10)
select count(*) as steps_g6, count(distinct s.video_id) as videos, sum(case when s.case_id is null then 1 else 0 end) as chi_host
from steps s join videos v using(video_id)
where s.tactic = 'g6-paid-ads' and regexp_matches(lower(v.bias), 'arcads|sideshift|noise|clover|pebble');
-- (12) step chỉ host theo kênh video (để biết host nào)
select v.channel, count(*) as steps_host from steps s join videos v using(video_id) where s.tactic = 'g6-paid-ads' and s.case_id is null group by 1;
