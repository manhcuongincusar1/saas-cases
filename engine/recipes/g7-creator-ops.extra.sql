-- Số đếm thêm cho g7-creator-ops. Chạy: duckdb kb/data/kb.duckdb < engine/recipes/g7-creator-ops.extra.sql
-- Các mục con là nhóm theo từ khoá trên (what + tactic_note + cost + threshold) của step g7. Các nhóm CHỒNG LẤN nhau: một step có thể thuộc nhiều nhóm.
-- "Case full" = case depth full có step khớp. "Chỉ host" = step không gắn case. Tiền trong kho là số founder (hoặc host) nêu, một case một con số.

-- (1) step theo chặng, theo năm video, theo kênh video
select stage, count(*) as steps from steps where tactic = 'g7-creator-ops' group by 1 order by 2 desc;
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 'g7-creator-ops' group by 1 order by 1;
select v.channel, count(*) as steps, count(distinct s.video_id) as videos, sum(case when s.case_id is null then 1 else 0 end) as chi_host from steps s join videos v using(video_id) where s.tactic = 'g7-creator-ops' group by 1 order by 2 desc;

-- (2) case full dùng g7 theo community_insider (true / false = outsider / không nêu = null)
with g as (select distinct s.video_id, s.case_id from steps s join cases c using(video_id, case_id) where s.tactic = 'g7-creator-ops' and c.depth = 'full')
select case when c.community_insider is true then 'insider' when c.community_insider is false then 'outsider' else 'không nêu' end as insider, count(*) as n from g join cases c using(video_id, case_id) group by 1 order by 2 desc;

-- (3) các mục con: số step, số case (mọi độ sâu), số case full, số step chỉ host. Nhóm theo từ khoá, chồng lấn
with x as (
  select s.video_id, s.case_id, c.depth, lower(s.what || ' ' || coalesce(s.tactic_note, '') || ' ' || coalesce(s.cost, '') || ' ' || coalesce(s.threshold, '')) as t
  from steps s left join cases c using(video_id, case_id) where s.tactic = 'g7-creator-ops'
), m as (
  select *, 'A tìm, lọc, tiếp cận, tuyển' as nhom from x where regexp_matches(t, 'tìm creator|tìm influencer|tìm người|tuyển|dm |dm$|outreach|email|lọc|phỏng vấn|ứng viên|chọn creator|chọn influencer|handshake|sideshift|upwork|hashtag|liên hệ|nhắn|inbound|outbound|paid promo')
  union all select *, 'B trả tiền và cấu trúc deal' from x where regexp_matches(t, 'trả|retainer|cpm|rev share|chia |affiliate|hoa hồng|equity|thưởng|flat|usd|\$|giá|ngân sách|sàn view|minimum view|% ad spend')
  union all select *, 'C brief, duyệt, đào tạo, quản, giữ' from x where regexp_matches(t, 'brief|duyệt|đào tạo|huấn luyện|khoá học|warm|coach|manager|quản|discord|giữ|cắt|onboard|hợp đồng|kịch bản|hook|hướng dẫn|nhóm chat|whatsapp|crm')
  union all select *, 'D nhân bản format đã thắng, quy mô' from x where regexp_matches(t, 'format|nhân|scale|repost|reposter|viral|90%|slideshow|nhiều tài khoản|tài khoản')
  union all select *, 'E thuê hay không: thất bại, agency, tự làm, đối tác' from x where regexp_matches(t, 'thất bại|flop|không hiệu quả|ít view|không ra|agency|in-house|nội bộ|đừng|tránh|lỗ|sai lầm|ít chuyển đổi|bỏ đi|tự làm|co-founder|đồng sáng lập|không thành|chưa có kết quả')
)
select nhom, count(*) as steps, count(distinct case when case_id is not null then video_id || '/' || case_id end) as case_all,
       count(distinct case when depth = 'full' then video_id || '/' || case_id end) as case_full,
       sum(case when case_id is null then 1 else 0 end) as chi_host
from m group by 1 order by 1;

-- (4) tiền theo từng nhóm trả: một case một con số. Đếm case full có step nhắc từng kiểu trả
with x as (
  select s.video_id, s.case_id, lower(s.what || ' ' || coalesce(s.tactic_note, '') || ' ' || coalesce(s.cost, '') || ' ' || coalesce(s.threshold, '')) as t
  from steps s join cases c using(video_id, case_id) where s.tactic = 'g7-creator-ops' and c.depth = 'full'
)
select 'retainer cố định' as kieu, count(distinct video_id || '/' || case_id) as case_full from x where regexp_matches(t, 'retainer')
union all select 'CPM (trả theo 1.000 view)', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'cpm|trên 1.000 view|mỗi 100.000 view|theo view')
union all select 'phí cố định theo video hoặc theo bài', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'mỗi video|/video|mỗi bài|flat|cho 3 video|cho 4 video|4 video')
union all select 'chia doanh thu hoặc lợi nhuận (rev share)', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'rev share|chia doanh thu|chia phần trăm|chia % |revenue split|doanh thu của')
union all select 'equity hoặc chia sở hữu', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'equity|quyền sở hữu|50%')
union all select 'affiliate, hoa hồng, referral', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'affiliate|hoa hồng|referral|giới thiệu được')
union all select 'minimum view clause hoặc sàn view', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'minimum view|sàn view|mvc|bảo đảm')
union all select 'thử trước (trial, video test, gói thử)', count(distinct video_id || '/' || case_id) from x where regexp_matches(t, 'trial|gói thử|video test|hợp đồng thử|trả trước|thử 1 tháng');

-- (5) bảng số tiền do founder nêu (cột cost hoặc threshold có số). Mỗi dòng một step của case full
select s.video_id[:6] as video, s.case_id, s.ts, s.cost, s.threshold
from steps s join cases c using(video_id, case_id)
where s.tactic = 'g7-creator-ops' and c.depth = 'full' and (coalesce(s.cost, '') <> '' or coalesce(s.threshold, '') <> '') and regexp_matches(coalesce(s.cost, '') || coalesce(s.threshold, ''), '[0-9]')
order by s.video_id, s.ts;

-- (6) tiền do HOST nêu (case_id null), tách riêng khỏi số của founder
select s.video_id[:6] as video, s.ts, v.channel, s.cost, s.threshold
from steps s join videos v using(video_id)
where s.tactic = 'g7-creator-ops' and s.case_id is null and regexp_matches(coalesce(s.cost, '') || coalesce(s.threshold, ''), '[0-9]')
order by s.video_id, s.ts;

-- (7) điều kiện trước: case full có step g7 mà step nói chính founder tự làm hoặc tìm ra format thắng TRƯỚC khi thuê (đọc tay từng step, danh sách tường minh theo video prefix + case)
with picks(vp, cid) as (values
  ('Bf12MN','glam-up'), ('9WWvLj','social-wizard'), ('RVnnqT','nomad-table'), ('N2oWiw','gleam'), ('si3Hzk','stronger'), ('s9qQPM','pingo')
)
select p.vp, p.cid, c.depth, count(s.ts) as steps_g7 from picks p left join cases c on c.video_id like p.vp || '%' and c.case_id = p.cid left join steps s on s.video_id like p.vp || '%' and s.case_id = p.cid and s.tactic = 'g7-creator-ops' group by 1, 2, 3 order by 1;

-- (8) case full có step g7 ghi thất bại, flop, ít chuyển đổi, không hiệu quả hoặc sai lầm (đọc tay từng step, danh sách tường minh)
with picks(vp, cid) as (values
  ('1nfPvJ','naturalwrite'), ('3X4Vne','savewise'), ('RypUD_','abmax'), ('yBjcmM','prayer-lock'), ('r_JUxa','massive'), ('PdudtX','push-scroll'), ('OV09yP','symmetry')
)
select p.vp, p.cid, c.depth, count(s.ts) as steps_g7 from picks p left join cases c on c.video_id like p.vp || '%' and c.case_id = p.cid left join steps s on s.video_id like p.vp || '%' and s.case_id = p.cid and s.tactic = 'g7-creator-ops' group by 1, 2, 3 order by 1;

-- (9) step g7 có chữ agency hoặc nền tảng bán creator (Sideshift, Noise, Pebble, Handshake) và kênh video: để đếm phần có động cơ bán hàng
select s.video_id[:6] as video, v.channel, coalesce(s.case_id, 'HOST') as case_id, s.ts, s.what
from steps s join videos v using(video_id)
where s.tactic = 'g7-creator-ops' and regexp_matches(lower(s.what || ' ' || coalesce(s.tactic_note, '')), 'sideshift|noise|pebble|handshake|agency|marketplace')
order by 1, s.ts;

-- (10) video có bias nêu công cụ hoặc nền tảng BÁN creator/UGC, và số step g7 của chúng
select v.video_id[:6] as video, v.channel, count(*) as steps_g7, sum(case when s.case_id is null then 1 else 0 end) as chi_host
from steps s join videos v using(video_id)
where s.tactic = 'g7-creator-ops' and regexp_matches(lower(v.bias), 'sideshift|noise|arcads|evo marketing|pebble|clover')
group by 1, 2 order by 3 desc;

-- (11) tổng của (10): step g7 nằm ở video có bias nêu nền tảng hoặc công ty bán creator, UGC, phân phối
select count(*) as steps_g7, count(distinct s.video_id) as videos, sum(case when s.case_id is null then 1 else 0 end) as chi_host
from steps s join videos v using(video_id)
where s.tactic = 'g7-creator-ops' and regexp_matches(lower(v.bias), 'sideshift|noise|arcads|evo marketing|pebble|clover');

-- (12) video Arcads (kênh jason-lee) có step g7 nào không
select count(*) as steps_g7_trong_video_arcads from steps s join videos v using(video_id) where s.tactic = 'g7-creator-ops' and regexp_matches(lower(v.bias), 'arcads');

-- (13) trả creator theo từng giai đoạn: số case full có step g7 chặng launch (trả creator khi vừa ra mắt)
select count(distinct s.video_id || s.case_id) as case_full_g7_o_chang_launch from steps s join cases c using(video_id, case_id) where s.tactic = 'g7-creator-ops' and s.stage = 'launch' and c.depth = 'full';
