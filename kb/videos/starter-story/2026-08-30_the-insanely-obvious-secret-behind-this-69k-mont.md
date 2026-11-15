---
schema: 2
video_id: BA_fC95p43c
channel: starter-story
title: The Insanely Obvious Secret Behind This $69K/Month SaaS
date: 2026-08-30
url: https://www.youtube.com/watch?v=BA_fC95p43c
transcript: starter-story-kb/videos/2026-08-30_the-insanely-obvious-secret-behind-this-69k-month-sa/transcript.md
kind: founder_case
speakers:
- name: Gaurav
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story bán database 90+ ý tưởng miễn phí (link trong mô tả) và đang tuyển người; Fastlane
  là case của họ. Con số 69k/tháng do founder tự nói.
analyzed: 2026-11-15
cases:
- id: fastlane
  depth: full
  product: 'Fastlane (usefastlane.ai): tạo video/slideshow short-form từ website sản phẩm rồi lên lịch
    đăng TikTok, Instagram, YouTube'
  what: 'Công cụ marketing AI cho solo builder: đọc xu hướng trong ngách, tạo hàng nghìn nội dung ngắn
    đúng sản phẩm, đăng hàng loạt'
  type:
  - web-app
  customer: Solopreneur làm app di động hoặc SaaS
  founder:
    who: Gaurav
    base: null
    technical: true
    team: 2 co-founder (Gaurav và Joe)
    background: Tự học làm app sau khi xem video Starter Story; co-founder Joe không kỹ thuật nhưng dựng
      dashboard khách hàng bằng Claude Code
  revenue:
    amount: 69000
    unit: usd
    basis: mrr
    note: Founder nói ~69k/tháng doanh thu định kỳ; màn hình Stripe được đưa lên nhưng founder không đọc
      số từ đó nên để claimed
    q: We do around 69k a month in recurring revenue just for our software product.
    ts: 01:02
    evidence: claimed
  pricing: null
  idea_origin:
  - own_pain
  scale_channels: []
  community_at_discovery:
    value: Người xem Starter Story đang tự làm app; gặp co-founder Joe cũng làm SaaS và gặp cùng nỗi đau
      marketing
    insider: true
    q: He was in a very similar situation with his own SaaS project and we all faced the same problem
    ts: 02:52
  demand_signal:
    kind: paid
    level: 8
    what: Bản beta trả phí (trước launch công khai) đạt ~16k ARR từ một số người dùng trả tiền; tiền đến
      sau khi đã build beta
    q: we scaled from around 16k ARR just from some paid beta
    ts: 01:02
  prior_failures:
    count: 1
    what: 'Sản phẩm ngang ''Cast AI'' (SEO, LLM SEO, Reddit, short-form trong một app): làm vài V1 rồi
      bỏ để chỉ giữ short-form'
    q: We spun up a few V1s, which we started in July.
    ts: 03:53
  unfair_advantage:
  - value: technical_skill
    what: Tự học code qua video rồi tự build app
    q: And I just started building my own apps the moment I watched that video.
    ts: 02:36
  - value: cofounder
    what: Co-founder Joe gặp cùng nỗi đau marketing và cùng làm SaaS; Joe dựng dashboard bằng AI
    q: I met my co-founder Joe.
    ts: 02:52
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 2
      value: 2 tháng tính từ lúc launch công khai (không phải từ lúc bắt đầu làm)
      q: We officially launched just over 2 months ago
      ts: 01:02
  first_users:
  - channel: reddit
    what: 'Giai đoạn lấy khách 1-1: đăng Reddit và lead magnet khắp mạng xã hội; ai đăng ký waitlist được
      gửi email mời gọi rồi xem họ dùng sản phẩm (video không nói bao nhiêu người)'
    q: we'd be crawling Reddit threads, posting lead magnets all across social media
    ts: '11:16'
  build:
    time: Bản V1 từ tháng 7; bản vertical bắt đầu tháng 10 và có beta tháng 12; launch công khai 23/3
      (video không nói số tháng build)
    cut:
    - Sản phẩm ngang Cast AI (SEO, LLM SEO, Reddit, short-form trong một app)
    q: That development started around in October, and by the time we got to December, we had shipped
      a beta
    ts: 04:09
steps:
- stage: find-idea
  ts: 02:52
  case: fastlane
  what: Sau vài app tự làm, nhận ra khó nhất là đưa app tới người xem; co-founder Joe gặp cùng vấn đề.
    Ý tưởng marketing tool bắt nguồn từ nỗi đau đó.
  tactic: s5-insider
- stage: build
  ts: 03:53
  case: fastlane
  what: Làm vài V1 sản phẩm ngang 'Cast AI' từ tháng 7, ship từ tháng 8, tiếp tục ship đến tháng 9.
- stage: validate
  ts: 06:56
  case: fastlane
  what: 'Thêm nút ''Book a call'' (viền cầu vồng) trong UI: ai đặt lịch được thêm 7 ngày truy cập; gọi
    khoảng 20 cuộc mỗi tuần từ tháng 8.'
  tactic: s10-customer-interviews
  tool: Calendly
  threshold: ~20 cuộc/tuần
- stage: validate
  ts: '10:31'
  case: fastlane
  what: 'Phỏng vấn theo sách The Mom Test: không hỏi ''bạn có dùng không'', mà hỏi lần gần nhất đã giải
    quyết vấn đề thế nào và tốn bao nhiêu tiền hay thời gian.'
  tactic: s10-customer-interviews
- stage: build
  ts: '11:01'
  case: fastlane
  what: 'Giai đoạn usability: mời người đăng ký waitlist gọi, chia sẻ màn hình, im lặng xem họ dùng MVP
    rồi sửa UI.'
- stage: launch
  ts: '11:16'
  case: fastlane
  what: 'Lấy người dùng đầu: đăng Reddit và lead magnet khắp mạng xã hội; ai đăng ký waitlist thì gửi
    email mời gọi 1-1.'
  tactic: g1-first-10-users
- stage: monetize
  ts: 01:02
  case: fastlane
  what: 'Bán bản beta trả phí trước khi launch công khai: ~16k ARR từ một số người dùng beta.'
  tactic: g4-pricing-paywall
  tactic_note: Thu tiền từ bản beta trước launch; video không nêu giá
- stage: retain
  ts: '12:17'
  case: fastlane
  what: 'Sau launch: theo dõi power user dùng nhiều nhất rồi gọi hỏi nền tảng giúp họ thế nào.'
  tactic: g5-retention
quotes:
- ts: 06:40
  who: Gaurav
  stage: validate
  theme:
  - action-over-research
  text: but biggest driver of how we ended up building Fast Zen was literally just talking to as many
    customers as we possibly could.
  vi: Yếu tố lớn nhất khiến chúng tôi build ra sản phẩm là nói chuyện với càng nhiều khách càng tốt.
- ts: '10:31'
  who: Gaurav
  stage: validate
  theme:
  - action-over-research
  text: Try DMing people on Twitter, and get on a call with them, even if you have to pay them
  vi: Nhắn DM người trên Twitter, xin gọi cho họ, kể cả phải trả tiền.
- ts: '14:22'
  who: Gaurav
  stage: mindset
  theme:
  - learn-from-others
  text: We never would have built Fastlane if it wasn't for Starter Story.
  vi: Chúng tôi sẽ không bao giờ build Fastlane nếu không có Starter Story.
- ts: '14:38'
  who: Gaurav
  stage: mindset
  theme:
  - risk-and-leap
  text: I'd say just don't be afraid of going against the norm.
  vi: 'Tôi sẽ nói: đừng sợ đi ngược số đông.'
rules:
- ts: '10:01'
  who: Pat Walls
  stage: launch
  theme:
  - right-audience
  text: talking to customers isn't the solution, but it is the mechanism to figuring out where to market.
  vi: Nói chuyện với khách không phải lời giải, nhưng là cơ chế để tìm ra nên tiếp thị ở đâu.
  evidence: opinion
numbers:
- ts: 01:02
  metric: MRR tự nêu (lúc quay)
  value: 69000
  unit: usd_per_month
  evidence: claimed
- ts: 01:19
  metric: người dùng trả tiền
  value: 1000
  unit: count
  evidence: claimed
- ts: 04:09
  metric: người đăng ký waitlist trước khi ship beta vertical
  value: 2000
  unit: count
  evidence: claimed
- ts: 07:26
  metric: số cuộc gọi khách hàng đã thực hiện
  value: 2000
  unit: count
  evidence: claimed
frameworks:
- customer-calls-first
idea_patterns: []
---

## Một câu

Fastlane (công cụ tạo video short-form cho solo builder) đạt ~69k/tháng theo lời founder: bỏ bản sản phẩm ngang để chỉ giữ một việc, rồi gọi khoảng 2.000 khách để chọn đúng tính năng.

## Bài học cho tôi

- Gọi khách có hệ thống: nút "Book a call" đổi 7 ngày truy cập thêm lấy khoảng 20 cuộc mỗi tuần (`06:56`); phỏng vấn theo Mom Test, hỏi lần cuối đã giải quyết thế nào, không hỏi "có dùng không" (`10:31`).
- Bỏ sản phẩm ngang, chỉ giữ một việc: vài V1 'Cast AI' (SEO + Reddit + short-form) bị bỏ sau khi nói chuyện với khách, còn short-form (`03:53`, `04:09`).

## Đừng tin vội

- Ai được lợi: Starter Story bán database 90+ ý tưởng và đang tuyển người. Con số 69k và 1.000 người trả tiền là lời founder. Màn hình Stripe được đưa lên (`02:05`) nhưng founder không đọc số từ đó, nên để claimed.
- Tiền đến sau khi đã build bản beta (paid beta ~16k ARR, `01:02`), không phải trước khi build. Đây là bằng chứng nhu cầu sau khi có sản phẩm thô, không phải pre-build.
- Điều kiện riêng: founder tự học code và co-founder Joe dựng dashboard bằng Claude Code (`09:15`). Chạy 2.000 cuộc gọi cần đội và thời gian lớn; khó sao chép nguyên xi.
- Video không nói: giá gói, chi phí quảng cáo, kênh nào đưa 10 người dùng đầu ngoài Reddit. Video có chỗ không khớp: 'launch công khai 23/3' nhưng lại nói 'launched just over 2 months ago', nên mốc 2 tháng chỉ nên dùng như lời kể.
