---
schema: 2
video_id: qYYeu0E-1SI
channel: superwall
title: The 14-Year-Old Who Built a $14k/Month AI App
date: 2026-06-07
url: https://www.youtube.com/watch?v=qYYeu0E-1SI
transcript: superwall/youtube-transcript/superwall/the-14-year-old-who-built-a-14kmonth-ai-app/transcript.md
kind: founder_case
speakers:
- name: Evan Yadegari
  role: founder
- name: Joseph Choi
  role: host
bias: Video có nhiều đoạn tài trợ hoặc quảng cáo (Superwall, Rork giảm giá, SpyTalk có link trong mô tả);
  host bán Consumer Club (hội viên trả phí, dinner). Số tiền là lời kể, không có dashboard.
analyzed: 2026-11-15
cases:
- id: locked
  depth: full
  product: 'Locked: app năng suất kiểu gamified, biến việc tự cải thiện thành trò chơi (check việc, nhận
    XP, cạnh tranh)'
  what: Người dùng check việc hằng ngày trong app; creator kiểu 'day in the life' quay cảnh dùng app và
    được trả tiền
  type:
  - mobile-app
  customer: Gen Z muốn tập trung và tự cải thiện
  founder:
    who: Evan Yadegari
    base: null
    technical: false
    team: có co-founder cũ (Alex, Monge) làm cùng từ đầu; video không nêu quy mô đội
    background: Làm content gaming và website (Totally Science, EvanClub), đã thử app Problem Pal; không
      biết code trước khi làm Locked
  revenue:
    amount: 14000
    unit: usd
    basis: monthly
    note: '''over $14,000 a month'', lời founder, không có dashboard'
    q: My app is Locked and I was able to scale up to over $14,000 a month
    ts: 00:00:00
    evidence: claimed
  pricing: Gói chính $30/năm hoặc $7/tuần
  idea_origin:
  - passion_skin
  scale_channels:
  - influencer_paid
  community_at_discovery:
    value: Gen Z (cùng tuổi founder) đang khó tập trung vì mạng xã hội
    insider: true
    q: specifically Gen Z with all of the brain rot being advertised towards them
    ts: 00:03:55
  demand_signal:
    kind: self_reported_pain_or_free_waitlist
    level: 4
    what: Bạn cùng tuổi tự kể mình hay mất tập trung và nghiện app; chưa có tiền
    q: He told me that he was always struggling to stay focused
    ts: 00:05:00
  prior_failures:
    count: 2
    what: Vài app trước (trong đó có Problem Pal) 'làm tạm được' nhưng không scale được
    q: you had a couple of apps that did okay, but you weren't able to scale those
    ts: 00:03:55
  unfair_advantage:
  - value: cofounder
    what: Co-founder cũ (Alex, Monge) cùng làm từ Figma đến prototype
    q: my old co-founder and I
    ts: 00:05:15
  - value: network
    what: Anh trai là founder Cal AI (đã exit); video không nói anh trực tiếp giúp gì ngoài bài học
    q: He's the younger brother of Zach Yatagari
    ts: 00:00:00
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: influencer_paid
    what: Video creator 'day in the life' (trả tiền) giúp đạt ngày $1.000 đầu tiên và ~1 triệu view
    q: this video helped us hit our first $1,000 day
    ts: 00:08:51
  build: null
- id: tenx
  depth: mention
  product: '10X: nền tảng ''Shopify cho app'', nhập prompt ra app đầy đủ kèm công cụ marketing'
  what: Founder mới ra mắt, đo bằng ARR sau một tháng
  revenue:
    amount: 30000
    unit: usd
    basis: arr
    note: '''over 30,000 in ARR'' sau khoảng một tháng từ ra mắt'
    q: So far, we're at over 30,000 in ARR
    ts: 00:22:03
    evidence: claimed
- id: problem-pal
  depth: mention
  product: 'Problem Pal: app AI giúp làm bài tập về nhà nhanh'
  what: Video TikTok 'làm bài tập trong 10 giây' pitch thẳng app; founder nói video này kéo phần lớn traction
  revenue:
    amount: 2000
    unit: usd
    basis: monthly
    note: '''scaled to $2,000 a month'''
    q: scaled to $2,000 a month
    ts: 00:03:35
    evidence: claimed
  first_users:
  - channel: tiktok_organic
    what: Video TikTok organic (khoảng 200k view) pitch thẳng app trong video
    q: that video drove a ton of traction
    ts: 00:21:00
steps:
- stage: build
  ts: 00:05:15
  case: locked
  what: 'Vẽ Figma (onboarding và màn hình chính), đưa vào Claude làm prototype, rồi lặp: thêm key, sửa
    bug, cải thiện UX/UI; founder không biết code trước đó.'
- stage: find-idea
  ts: 00:03:55
  case: locked
  what: Thấy Gen Z khó tập trung vì mạng xã hội; bạn cùng tuổi gợi ý app gamify; áp cơ chế game (đã từng
    chơi) vào tự cải thiện.
  tactic: s13-others-pain-or-inbound
  tactic_note: Nỗi đau của bạn bè cùng tuổi (Gen Z), không phải nghề của founder; cơ chế game lấy từ thói
    quen chơi game
- stage: launch
  ts: 00:06:07
  case: locked
  what: Thử lần lượt Reddit, X, influencer và paid ads; chọn influencer vì thấy hiệu quả nhất.
  tactic: other
  tactic_note: So sánh nhiều kênh rồi chọn kênh; phần intro lại nói Reddit hiệu quả nhất (mâu thuẫn trong
    video)
- stage: launch
  ts: 00:06:26
  case: locked
  what: Gửi DM hàng loạt cho creator (gym, self-improvement, day-in-the-life) qua Instagram và TikTok;
    cao điểm gửi 500 DM/ngày.
  tactic: g7-creator-ops
  threshold: khoảng 100 DM/ngày/tài khoản (ngưỡng bị giới hạn)
- stage: launch
  ts: 00:10:03
  case: locked
  what: Chọn creator theo engagement và số view (từ vài nghìn view/video), không theo số follower.
  tactic: g7-creator-ops
- stage: launch
  ts: 00:12:56
  case: locked
  what: Mở DM bằng chữ 'paid promo?' rồi mời creator gọi điện để thương lượng, không đàm phán qua DM.
  tactic: g7-creator-ops
- stage: grow
  ts: 00:13:37
  case: locked
  what: 'Dùng bốn kiểu deal: cố định, CPM có trần, minimum view clause (kiểu ưa thích nhất), và thưởng
    thêm theo view.'
  tactic: g7-creator-ops
- stage: grow
  ts: 00:15:51
  case: locked
  what: 'Đặt minimum view theo CPM $1–2: ví dụ trả $800 thì minimum 400.000–800.000 view; không đạt thì
    trả theo tỉ lệ đã đạt.'
  tactic: g7-creator-ops
  threshold: CPM $1–2 mỗi nghìn view; ví dụ $800 ứng với 400k–800k view
- stage: launch
  ts: 00:16:58
  case: locked
  what: Yêu cầu creator gắn app trong 15 giây đầu và comment 'What's this app? I need this' rồi ghim;
    gửi hợp đồng và duyệt bài trước khi đăng.
  tactic: g7-creator-ops
- stage: grow
  ts: 00:17:44
  case: locked
  what: Quy kết lượt tải theo spike khi video nổ (Instagram không cho gắn link riêng).
  tactic: g8-funnel-measurement
  tactic_note: Attribution bằng spike lượt tải app trên App Store, không dùng link
- stage: grow
  ts: 00:18:03
  case: locked
  what: Creator nào có lời thì renew cùng deal, rồi thương lượng deal lớn hơn.
  tactic: g7-creator-ops
- stage: monetize
  ts: 00:09:13
  case: locked
  what: Gói chính $30/năm hoặc $7/tuần; khoảng 10 lượt tải cho một đăng ký trả tiền.
  tactic: g4-pricing-paywall
- stage: grow
  ts: 00:09:38
  case: locked
  what: Giữ CPM của video influencer dưới RPM (khoảng $3–4) để biết video có lời không.
  tactic: g8-funnel-measurement
- stage: grow
  ts: 00:20:38
  case: problem-pal
  what: Làm video TikTok organic làm bài tập nhanh rồi pitch thẳng app trong video; phần lớn traction
    đến từ video này.
  tactic: g3-organic-content-formats
quotes:
- ts: 00:18:23
  who: Evan Yadegari
  stage: mindset
  theme:
  - risk-and-leap
  text: Either you win or you learn.
  vi: Hoặc bạn thắng, hoặc bạn học.
- ts: 00:19:03
  who: Evan Yadegari
  stage: grow
  theme: []
  text: I would just care about followers and views, but in reality, that's a huge mistake.
  vi: Tôi từng chỉ quan tâm follower và view, nhưng thực ra đó là sai lầm lớn.
- ts: 00:25:57
  who: Evan Yadegari
  stage: find-idea
  theme: []
  text: For ideation, the first thing I do is think about problems I have or others face that are similar
    to myself
  vi: Khi lên ý tưởng, việc đầu tiên tôi làm là nghĩ về vấn đề mình hoặc người khác gặp, giống mình.
- ts: 00:25:57
  who: Evan Yadegari
  stage: find-idea
  theme:
  - revenue-first
  text: I would say it's best to stick to problems or pain points, but if if you can hop on a trend, that's
    also great.
  vi: Tốt nhất là bám vào vấn đề hoặc nỗi đau; nhưng nếu bắt được trend thì cũng tốt.
- ts: 00:27:00
  who: Evan Yadegari
  stage: find-idea
  theme: []
  text: If you want to speed run to $10,000 a month, think of a problem that you or others face.
  vi: Muốn đạt 10.000 đô/tháng nhanh nhất, hãy nghĩ tới một vấn đề bạn hoặc người khác gặp.
rules:
- ts: 00:26:35
  who: Joseph Choi
  stage: find-idea
  theme:
  - revenue-first
  text: Cuz people are willing to pay to solve problems, whereas something like this where it's like a
    game, it's not really solving a problem necessarily.
  vi: Người ta sẵn sàng trả tiền để giải quyết vấn đề; còn kiểu game này thì không thật sự giải quyết
    vấn đề.
  evidence: opinion
numbers:
- ts: 00:00:00
  metric: Locked doanh thu mỗi tháng (lời founder)
  value: 14000
  unit: usd_per_month
  evidence: claimed
- ts: 00:08:37
  metric: Một video creator (khoảng 1 triệu view) mang về ít nhất
  value: 3000
  unit: usd
  evidence: claimed
- ts: 00:09:13
  metric: Số lượt tải cho một đăng ký trả tiền (Locked)
  value: 10
  unit: downloads_per_subscription
  evidence: claimed
- ts: 00:11:22
  metric: Tỉ lệ trả lời DM influencer trên Instagram
  value: 3–4%
  unit: ratio
  evidence: claimed
- ts: 00:11:59
  metric: DM gửi mỗi ngày lúc cao điểm
  value: 500
  unit: count_per_day
  evidence: claimed
frameworks:
- gamified-habit-blocker
- right-audience-over-views
idea_patterns:
- passion-skin
---

## Một câu

Evan (14 tuổi) làm Locked, app gamify việc tự cải thiện, lên khoảng 14k$/tháng chủ yếu nhờ gửi DM hàng loạt cho creator và trả theo deal có minimum view, không dựa vào quảng cáo trả tiền.

## Bài học cho tôi

- Chọn creator theo engagement và số view, không theo follower; đọc comment xem có người thật hay không (`00:10:03`, `00:19:03`).
- Mở DM ngắn bằng "paid promo?", kéo sang cuộc gọi, rồi đặt minimum view theo CPM; đo bằng spike lượt tải vì Instagram không cho gắn link (`00:12:56`, `00:15:50`, `00:17:44`).

## Đừng tin vội

- Video nhiều đoạn quảng cáo (Superwall, Rork giảm giá, SpyTalk có link, Consumer Club trả phí). Số 14k và 30k ARR của 10X là lời kể, không có dashboard; 10X mới một tháng.
- Mâu thuẫn trong video: phần intro nói Reddit hiệu quả nhất, phần sau nói influencer hiệu quả nhất; không có số liệu so sánh kênh.
- Cách này cần quy mô: 5–10 nghìn influencer được tiếp cận, nhiều tài khoản DM, tài khoản được mua follower để verify; video không nói chi phí tổng, chi phí mỗi khách hay thời gian đạt mốc.
- Founder có lợi thế anh trai là founder Cal AI và tài khoản TikTok có sẵn từ các dự án trước (video không nói tài khoản đó đóng góp bao nhiêu).
