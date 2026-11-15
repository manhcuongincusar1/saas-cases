---
schema: 2
video_id: 2dfMUtHlQik
channel: starter-story
title: 'How I Built It: $400K/Month Mobile App (Gravl)'
date: 2025-11-13
url: https://www.youtube.com/watch?v=2dfMUtHlQik
transcript: starter-story-kb/videos/2025-11-13_how-i-built-it-400k-month-mobile-app-gravl/transcript.md
kind: founder_case
speakers:
- name: Pat Walls
  role: host
- name: Julian
  role: founder
bias: Video ca ngợi app của Julian; Starter Story có quảng cáo HubSpot trong video và kênh bán dịch vụ
  build app (Starter Story Build). Doanh thu là lời kể, không có dashboard.
analyzed: 2026-11-15
cases:
- id: gravl
  depth: full
  product: Gravl (app tập gym bằng AI)
  what: 'App tập gym AI: tạo bài tập cá nhân hoá theo thiết bị, mục tiêu và lịch tập; đồng bộ buổi tập
    từ Apple Health và Strava'
  type:
  - mobile-app
  customer: Người tập gym muốn bài tập cá nhân hoá; trả subscription
  founder:
    who: Julian
    base: Gốc Argentina, từng làm ở Úc (video không nói nơi ở hiện tại)
    technical: true
    team: Đồng sáng lập; năm đầu 3 người (Julian làm dev, Matias và Aaron làm growth/ads); nay khoảng
      13–14 người
    background: Kỹ sư phần mềm, từng làm startup, Atlassian, công ty truyền hình, quỹ đầu tư; lớn lên
      ở phòng gym của bố
  revenue:
    amount: 440000
    unit: usd
    basis: monthly
    note: Julian nói 'over 440K' tháng trước (đầu video); tiêu đề nói $400K/tháng; không có dashboard
    q: Last month, we made over $440K.
    ts: 00:00
    evidence: claimed
  pricing: Subscription; hard paywall trước khi đăng nhập lần đầu
  idea_origin:
  - own_pain
  - domain_expertise
  scale_channels:
  - paid_meta
  - paid_tiktok
  community_at_discovery:
    value: Người tập gym, đã dùng một app tập luyện khác và thấy nó đáng để làm lại tốt hơn
    insider: true
    q: Julian was a dude at the gym who discovered a
    ts: 00:00
  demand_signal: null
  prior_failures:
    count: 2
    what: Công ty trước (nền tảng influencer rồi thành agency) làm không tốt; app tracker đầu tiên bị
      bỏ vì giống bản copy
    q: The business wasn't doing great.
    ts: 02:52
  unfair_advantage:
  - value: domain_expertise
    what: Lớn lên ở phòng gym của bố, tập từ nhỏ
    q: My dad used to own a fitness center.
    ts: 01:33
  - value: technical_skill
    what: Kỹ sư phần mềm, tự làm được phần dev chính
    q: got into software engineering and uh moved to Australia.
    ts: 01:49
  - value: cofounder
    what: Đồng sáng lập lo growth và ads trong khi Julian làm dev
    q: Matias and Aaron did the growth and ads.
    ts: '13:14'
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 24
      value: khoảng 2 năm từ lúc ra mắt tới mức khoảng 440K/tháng
      q: We launched around 2 years ago
      ts: 01:16
  first_users:
  - channel: reddit
    what: Đăng thread Reddit kể cách làm app, kèm spec kỹ thuật; có vài trăm like và ~300k impressions
      trong vài giờ; có vài nghìn người dùng đầu (Julian không nhớ chính xác)
    q: I'm a massive supporter of of Reddit as a distribution channel.
    ts: 04:45
  - channel: paid_unspecified
    what: Chạy ads ngay sau khi thêm subscription; người đăng ký đầu tiên trong 10 phút (video không nêu
      nền tảng lúc đó)
    q: We got a subscription within the first 10 minutes of like activating the ads.
    ts: 07:11
  build:
    time: khoảng 2–3 tháng cho MVP (Julian nói 'maybe')
    cut: []
    q: Initial MVP took around two to three months maybe.
    ts: 03:58
steps:
- stage: find-idea
  ts: 03:07
  case: gravl
  what: Làm tracker giống app khác thì thấy 'giống bản copy'; dùng thử Fitbot thấy bài tập kỳ lạ, có chỗ
    nguy hiểm, nên quyết làm bản có engine bài tập đúng.
  tactic: s11-copy-or-localize-proven
  tactic_note: Làm bản tốt hơn của app đã chạy, bắt đầu từ lỗi nhận ra khi dùng
- stage: build
  ts: 04:14
  case: gravl
  what: Bản đầu là tracker, sau đó chuyển sang logic tạo bài tập; phần khó nhất là xử lý nhiều thiết lập
    (thiết bị, mục tiêu, tần suất, thể trạng).
- stage: launch
  ts: 04:45
  case: gravl
  what: Đăng thread Reddit về cách làm app cho cộng đồng developer; thu được vài nghìn người dùng đầu.
  tactic: g1-first-10-users
  tactic_note: 'Reddit: thread kể quá trình build, nhắm developer/người thích tập gym'
- stage: launch
  ts: 05:17
  case: gravl
  what: 'App còn miễn phí: người dùng báo bug và xin tính năng; Julian coi đó là dấu hiệu đúng hướng và
    là lúc cần làm kinh doanh nghiêm túc.'
  tactic: s10-customer-interviews
  tactic_note: 'sau launch: Dùng app miễn phí để thu bug và feature request từ người dùng đầu, trước khi
    thu phí'
- stage: monetize
  ts: '10:36'
  case: gravl
  what: Đặt paywall cứng trước khi đăng nhập lần đầu, sau phần câu hỏi cá nhân hoá và trước khi người
    dùng thấy sản phẩm; Julian nói nhiều người vẫn trả.
  tactic: g4-pricing-paywall
- stage: grow
  ts: 06:55
  case: gravl
  what: Chạy paid ads ngay sau khi có subscription; dịch app sang tiếng Tây Ban Nha và chạy ads ở Nam
    Mỹ, chi dưới 50 USD/ngày.
  tactic: g6-paid-ads
  tactic_note: Ads là kênh chính sau Reddit; chọn Nam Mỹ vì ads rẻ hơn Mỹ (Julian nói Mỹ đắt và cạnh tranh)
  threshold: dưới 50 USD/ngày
- stage: retain
  ts: '11:38'
  case: gravl
  what: Có chat hỗ trợ 24/7 trong app, người thật trả lời (không phải AI); Julian nói người dùng đánh
    giá cao điều này.
  tactic: g5-retention
  tactic_note: Hỗ trợ người thật trong app, không chỉ tài liệu
quotes:
- ts: 07:42
  who: Julian
  stage: validate
  theme:
  - sell-before-build
  text: The tip number one for sure will be to validate before spending money on ads.
  vi: 'Lời khuyên số một: validate trước khi chi tiền cho ads.'
- ts: 07:58
  who: Julian
  stage: validate
  theme:
  - sell-before-build
  text: And when I say validate, it's not just that the product work, but also that people are willing
    to pay for it.
  vi: Validate không chỉ là sản phẩm chạy được, mà còn là người ta sẵn sàng trả tiền.
- ts: '13:48'
  who: Julian
  stage: mindset
  theme:
  - passion-fuel
  text: Be proud of what you build.
  vi: Hãy tự hào về thứ bạn làm.
- ts: '14:03'
  who: Julian
  stage: mindset
  theme:
  - persistence
  text: Another thing will be to keep pushing then don't give up too soon.
  vi: Điều nữa là cứ tiếp tục, đừng bỏ cuộc quá sớm.
- ts: '14:34'
  who: Julian
  stage: mindset
  theme:
  - stuck-on-one-thing
  text: In our case was our previous startup. We probably dragged that for an extra year.
  vi: Với chúng tôi là startup trước đó; chúng tôi kéo dài nó thêm khoảng một năm.
rules: []
numbers:
- ts: 01:16
  metric: subscriber (Julian nói)
  value: 70000
  unit: count
  evidence: claimed
- ts: '12:43'
  metric: chi phí chạy ads (Meta, TikTok, một ít Google/Apple search) so với doanh thu
  value: khoảng 1/3 doanh thu
  unit: ratio
  evidence: claimed
- ts: '13:14'
  metric: hoa hồng Apple
  value: 15%
  unit: ratio
  evidence: claimed
- ts: '13:14'
  metric: số người trong team hiện tại
  value: 13–14
  unit: count
  evidence: claimed
- ts: '13:31'
  metric: chi phí hạ tầng, AI, tool mỗi tháng
  value: 1000
  unit: usd_per_month
  evidence: claimed
- ts: 07:27
  metric: chi tiêu ads ban đầu
  value: dưới 50
  unit: usd_per_day
  evidence: claimed
frameworks:
- organic-find-format-then-paid-scale
idea_patterns: []
---

## Một câu

Julian (dev gốc Argentina, từng làm agency) thấy một app tập gym có bài tập kém nên làm bản tốt hơn: Reddit cho vài nghìn người dùng đầu, rồi ads ngay sau khi có subscription đưa app lên khoảng $440K/tháng theo lời kể.

## Bài học cho tôi

- Làm bản tốt hơn của app đã chạy, bắt đầu từ lỗi chính mình thấy khi dùng (`03:07`).
- Ads chỉ bật sau khi đã có subscription và người dùng đầu; chi phí ads lúc đó khoảng 1/3 doanh thu (`12:43`).

## Đừng tin vội

- Doanh thu là lời kể của chính founder (`claimed`), không có dashboard; tiêu đề nói $400K, phần đầu nói 440K.
- Điều kiện riêng khó chép: nền tảng gym và kỹ năng dev có sẵn, đồng sáng lập lo growth/ads, và một agency trước đó đã cho họ kinh nghiệm user acquisition. Chi phí ads thấp ở Nam Mỹ là chiến lược riêng; Julian nói chính ở Mỹ thì đắt và cạnh tranh hơn.
- Video không nói tín hiệu nhu cầu nào trước khi làm app (không có demand_signal); thread Reddit là lần ra mắt đầu tiên.
- Video là quảng cáo kép: HubSpot tài trợ và Starter Story Build là sản phẩm của kênh.
