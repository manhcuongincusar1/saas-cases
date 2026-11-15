---
schema: 2
video_id: aLidq3_FwW0
channel: starter-story
title: I Make $13K/Month From This Simple App
date: 2026-10-07
url: https://www.youtube.com/watch?v=aLidq3_FwW0
transcript: starter-story-kb/videos/2026-10-07_i-make-13k-month-from-this-simple-app/transcript.md
kind: founder_case
speakers:
- name: Max
  role: founder
- name: Gus
  role: host
- name: Pat
  role: host
bias: Video có HubSpot CRM tài trợ (đoạn giữa); Starter Story bán database ý tưởng miễn phí và đang tuyển
  người; Max quảng bá app Maxed AI trên chính kênh. Số liệu là lời founder đọc từ RevenueCat.
analyzed: 2026-11-15
cases:
- id: maxed-ai
  depth: full
  product: 'Maxed AI: app coach tập lifting trên iOS (AI chỉnh chương trình tập, nhận lệnh bằng chat)'
  what: 'All-in-one app sức khoẻ/fitness: coach AI chỉnh lịch tập, theo dõi lift, dinh dưỡng, supplement/peptide,
    bảng xếp hạng và feed cộng đồng'
  type:
  - ios-app
  customer: Người tập gym/lifting muốn chương trình tập cá nhân hoá; trả gói năm $24.99
  founder:
    who: Max
    base: null
    technical: false
    team: Không có team lớn (host nói); Max làm chính
    background: Học Michigan, hai kỳ thực tập finance (VC, sales & trading); chưa từng làm app trước khi
      bắt đầu
  revenue:
    amount: 14000
    unit: usd
    basis: last_28_days
    note: 'Đọc từ RevenueCat: gần 14.000 trong 28 ngày; founder nói khoảng 14–15k/tháng. MRR thấp vì gói
      năm'
    q: over the last 28 days, we're, you know, nearly 14,000 dollars in revenue
    ts: 01:41
    evidence: measured
  pricing: Chỉ gói năm $24.99 trả trước (~$2/tháng); hard paywall
  idea_origin:
  - passion_skin
  scale_channels:
  - founder_led_content
  - paid_unspecified
  community_at_discovery:
    value: Tập lifting cùng bạn bè suốt đại học; chính Max là người tập
    insider: true
    q: My friends and I lifted all of college
    ts: 05:00
  demand_signal:
    kind: built_first
    level: 0
    what: Build app trước rồi mới quảng bá; lúc đầu ngại marketing. Không có tín hiệu nhu cầu nào trước
      khi build
    q: I built an app, but I was too afraid to market it
    ts: '10:27'
  prior_failures:
    count: 1
    what: 'App đánh giá món ăn Dish Rate: bỏ vì nghĩ làm dev tốn hàng chục nghìn đô'
    q: I'd have to pay tens of thousands dollars in development to get this thing live
    ts: 04:10
  unfair_advantage:
  - value: network
    what: Gặp qua Instagram một người có kinh nghiệm làm app, người này dẫn dắt Max (hard paywall, hướng
      đi)
    q: Fortunately, I met someone through Instagram that had some experience building apps
    ts: 06:21
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 6
      value: 6 tháng từ lúc bắt đầu học làm app tới ~14k/tháng
      q: Six months ago, I'd never built a mobile app
      ts: 00:49
  first_users:
  - channel: founder_led_content
    what: 'Founder-led content (quay video hằng ngày, đăng X): lời founder nói đem nhiều subscriber về
      app'
    q: being able to do founder-led content has brought on so many subscribers to the app
    ts: 02:47
  build:
    time: ~6 tháng dùng Claude Code tự build và cập nhật app (chưa từng viết app trước đó)
    cut: []
    q: I got set up with a Claude code $15 membership and just started typing
    ts: 04:26
steps:
- stage: find-idea
  ts: 05:00
  case: maxed-ai
  what: Chọn lifting vì chính Max mê nó; thấy Strava và Nike Run Club thống trị chạy bộ nhưng lifting
    chưa có nền tảng thống nhất, nên làm luôn.
  tactic: s5-insider
  tactic_note: Chọn ngách từ đam mê của chính mình rồi nhìn khoảng trống so với app chạy bộ lớn; không
    dùng số doanh thu đối thủ
- stage: monetize
  ts: 01:57
  case: maxed-ai
  what: Chỉ bán gói năm $24.99 trả trước (~$2/tháng), vì không muốn sống nhờ việc người dùng quên huỷ
    gói.
  tactic: g4-pricing-paywall
  cost: $24.99/năm
- stage: monetize
  ts: 06:37
  case: maxed-ai
  what: Làm hard paywall theo lời người có kinh nghiệm gặp qua Instagram; đây là bước đầu tiên.
  tactic: g4-pricing-paywall
- stage: launch
  ts: 06:37
  case: maxed-ai
  what: Không đủ ngân sách thuê 50 UGC creator nên tự quay video mỗi ngày (5–10 video), vượt ngại bị bạn
    bè chế giễu; xem hold rate và skip rate để tìm format.
  tactic: g3-organic-content-formats
- stage: grow
  ts: 07:11
  case: maxed-ai
  what: Chạy video tự quay có hiệu quả nhất làm paid ads; bắt đầu ngân sách thấp, tăng dần khi thấy product-market
    fit.
  tactic: g6-paid-ads
  cost: ~$250/ngày
  tactic_note: Creative lấy từ video organic đã thử trước
- stage: grow
  ts: 08:34
  case: maxed-ai
  what: Đăng hành trình lên X từ khoảng 3 tháng trước; founder ước khoảng 1/3 doanh thu đến từ người theo
    dõi trên X.
  tactic: g3-organic-content-formats
quotes:
- ts: 05:00
  who: Max
  stage: find-idea
  theme:
  - passion-fuel
  text: but I wanted to build something I was actually passionate about and lifting is my favorite thing
    to do in the world
  vi: Tôi muốn làm thứ mình thật sự đam mê, và lifting là thứ tôi thích nhất trên đời.
- ts: 04:26
  who: Max
  stage: build
  theme:
  - action-over-research
  text: Six months later, I don't think I've gone a day without being in my terminal
  vi: Sáu tháng sau, tôi không ngày nào rời khỏi terminal.
- ts: 06:54
  who: Max
  stage: grow
  theme:
  - emotional-bottleneck
  text: Because the reality is most people don't even care.
  vi: Thực tế là hầu hết mọi người chẳng quan tâm đâu.
- ts: 08:51
  who: Max
  stage: grow
  theme: []
  text: Be as public about it as possible.
  vi: Hãy công khai càng nhiều càng tốt.
- ts: '10:27'
  who: Max
  stage: mindset
  theme:
  - persistence
  text: go all in, film yourself, annoy the crap out of everyone around you because you're so obsessed
    with it
  vi: Hãy all in, quay chính mình, làm phiền mọi người xung quanh vì bạn quá mê nó.
rules:
- ts: '11:17'
  who: Gus
  stage: find-idea
  theme: []
  text: I think my big takeaway is just that you don't really need like a crazy unique idea to be successful.
  vi: 'Điều tôi rút ra: bạn không cần một ý tưởng quá độc đáo mới thành công.'
  evidence: opinion
- ts: '11:34'
  who: Gus
  stage: grow
  theme: []
  text: the one thing that you can't replicate is personal brand
  vi: Thứ không ai sao chép được là thương hiệu cá nhân.
  evidence: opinion
numbers:
- ts: 01:57
  metric: người đăng ký trả phí đang hoạt động
  value: 1000
  unit: count
  evidence: measured
- ts: 02:14
  metric: khách mới trong 28 ngày
  value: 20000
  unit: count
  evidence: measured
frameworks:
- organic-find-format-then-paid-scale
- annual-plan-push
idea_patterns:
- passion-skin
---
## Một câu

Max chưa từng viết app, học dùng Claude Code rồi tự build app coach tập lifting trên iOS: chỉ bán gói năm $24.99, tự quay video mỗi ngày và đẩy video tốt nhất vào paid ads; sau khoảng 6 tháng đạt ~14k/tháng (lời founder đọc từ RevenueCat).

## Bài học cho tôi

- Quay video hằng ngày, xem hold rate và skip rate, rồi chỉ đẩy video tốt nhất vào paid ads; ngân sách tăng dần khi có tín hiệu (`06:37`, `07:11`).
- Ý tưởng đến từ đam mê và một khoảng trống nhìn thấy được, không từ kiểm chứng nhu cầu; Max tự nhận build trước rồi mới quảng bá (`05:00`, `10:27`).

## Đừng tin vội

- Doanh thu là số founder đọc từ dashboard trong video do chính kênh quay; video có HubSpot tài trợ và kênh bán database ý tưởng. Max quảng bá app của mình trên cùng kênh.
- Max tự nhận có khoảng 100 đối thủ trong ngách lifting. Video không có số retention; gói năm trả trước nên doanh thu 28 ngày chưa phản ánh việc giữ khách sau 12 tháng.
- Video không nói ai là khách trả đầu tiên và họ tìm thấy app bằng cách nào. Khách đầu tiên đến "khoảng 4 tháng trước" (không quy đổi thành tháng từ lúc bắt đầu, nên mốc `first_dollar` để null).
- Điều kiện riêng: thời điểm AI coding đủ rẻ và dễ dùng; Max không có kinh nghiệm làm app trước đó nên không chép được nguyên xi con đường này.
