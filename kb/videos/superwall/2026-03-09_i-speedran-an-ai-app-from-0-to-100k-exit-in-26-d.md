---
schema: 2
video_id: yw5iIgO4PbY
channel: superwall
title: I speedran an ai app from 0 to $100k exit in 26 days
date: 2026-03-09
url: https://www.youtube.com/watch?v=yw5iIgO4PbY
transcript: superwall/youtube-transcript/superwall/i-speedran-an-ai-app-from-0-to-100k-exit-in-26-days/transcript.md
kind: founder_case
speakers:
- name: Caleb Dean
  role: founder
- name: Joseph Choi
  role: host
bias: Superwall (công cụ paywall) tài trợ kênh; host bán Consumer Club và dinner cho founder. Founder
  vừa bán app và đang có lợi khi kể câu chuyện này. Toàn bộ số liệu là lời kể, không có dashboard.
analyzed: 2026-11-15
cases:
- id: runafy
  depth: full
  product: 'Runafy: app chạy bộ có xếp hạng kiểu game (ranked), bản chuyển ý tưởng LiftOff (gym) sang
    chạy bộ'
  what: Theo dõi chạy bộ bằng GPS, xếp hạng với bạn bè và người lạ; nối dữ liệu từ Garmin, Strava, Apple
    Watch; có home feed và leaderboard
  type:
  - mobile-app
  customer: Người chạy bộ muốn thi đua và xếp hạng với bạn bè
  founder:
    who: Caleb Dean
    base: null
    technical: null
    team: có CTO (dev thứ ba, làm chính phần code) và nhóm dev; Caleb lo thiết kế và quyết định sản phẩm
    background: App đầu cho người mắc chứng tiểu không được (FlutterFlow); từng chạy agency content/shortform;
      từng làm CMO bán thời gian cho 10X của Blake Anderson
  revenue:
    amount: 3000
    unit: usd
    basis: mrr
    note: MRR ước tính lúc định giá khi chưa đủ một tháng doanh thu (dựa trên trial), không phải số đo
      đầy đủ; host gọi định giá là 180k nhưng video không nêu con số cuối
    q: pretty much we calculated it to be 3K MRR
    ts: 00:05:24
    evidence: claimed
  pricing: Subscription; early adopter trả 5 USD trọn đời trước khi app ra mắt; khi launch gửi mã giảm
    nửa giá cho danh sách waitlist
  idea_origin:
  - passion_skin
  - revenue_scouting
  scale_channels:
  - instagram_reels
  - tiktok_organic
  - platform_marketplace
  community_at_discovery:
    value: chạy bộ là sở thích chính của founder lúc đó, và thích game; không phải người trong nhóm chạy
      bộ theo nghề
    insider: true
    q: probably my like my only hobby, which I was getting into was like running
    ts: 00:21:30
  demand_signal:
    kind: paid
    level: 8
    what: 'trước khi app tồn tại: landing 2 câu có nút Stripe, 2.000 waitlist và hơn 90 người trả 5 USD
      làm early adopter'
    q: 90 people paid $5 for an app that didn't even exist yet
    ts: 00:01:27
  prior_failures:
    count: 1
    what: 'App đầu (cho người mắc chứng tiểu không được): kiếm khoảng 5–10k USD nhưng niche quá hẹp, marketing
      khó, không có đam mê với vấn đề; đã build nhiều tháng trước khi validate'
    q: I spent months like building a product
    ts: 00:20:40
  unfair_advantage:
  - value: domain_expertise
    what: Từng chạy agency content và shortform, có nhiều kinh nghiệm organic
    q: So, I had like quite a lot of experience in terms of like organic stuff
    ts: 00:14:21
  - value: network
    what: Nhờ agency cũ có sẵn danh sách editor giỏi để thuê ngay
    q: I already had like a portfolio of cracked editors which I could just bring on instantly
    ts: 00:16:47
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: platform_marketplace
    what: App Store pre-order mở khoảng 2 tuần; lúc launch App Store tự tải về khoảng 3.000 máy
    q: So, we had 3,000 downloads.
    ts: 00:01:58
  build:
    time: UI làm trong 3 ngày bằng Figma; CTO code khoảng 1,5 tháng (14 giờ/ngày); hai dev đầu làm 2–3
      tuần không thành
    cut:
    - 'Bản V1 gửi Apple duyệt: hai tab, không onboarding'
    q: he just grinded like 14 hours a day for like a month and a half straight
    ts: 00:07:19
steps:
- stage: find-idea
  ts: 00:21:30
  case: runafy
  what: Lấy LiftOff (ranked cho gym, khoảng 200–300k USD/tháng) làm mẫu và đổi sang chạy bộ.
  tactic: s11-copy-or-localize-proven
  tactic_note: 'Remix app đã chạy tốt: đổi ngách từ gym sang chạy bộ'
  threshold: LiftOff khoảng 200–300k USD/tháng, trên 100k/tháng ít nhất 12 tháng
- stage: find-idea
  ts: 00:20:59
  case: runafy
  what: Chọn ý tưởng gắn với đam mê (chạy bộ và game ranked) thay vì nỗi đau như app đầu.
  tactic: s5-insider
  tactic_note: Đam mê chạy bộ và game, không phải nỗi đau
- stage: validate
  ts: 00:01:07
  case: runafy
  what: Copy đúng format reels của LiftOff, đăng khoảng 50 video trong 2 tuần để đo nhu cầu khi app chưa
    tồn tại.
  tactic: s8-content-demand-test
  tactic_note: Đăng nội dung về ý tưởng trước khi build xong, copy format reels của app đã chạy
- stage: validate
  ts: 00:01:27
  case: runafy
  what: Landing 2 câu có nút Stripe bán 5 USD early adopter khi app chưa tồn tại; hơn 90 người trả.
  tactic: s7-preorder-buy-button
  tactic_note: Thu tiền trước khi có app qua trang bán và nút Stripe; không phải pre-order App Store
- stage: launch
  ts: 00:01:58
  case: runafy
  what: Đặt app lên App Store pre-order khoảng 2 tuần; khi launch App Store tự tải về khoảng 3.000 máy
    và gửi email thông báo.
  tactic: g9-launch-platforms
  tactic_note: Pre-order App Store để seed người dùng và leaderboard trước launch
- stage: build
  ts: 00:07:19
  case: runafy
  what: Hai dev đầu làm 2–3 tuần không thành; sau đó CTO nhận phần code, founder làm UI trong 3 ngày bằng
    Figma.
- stage: validate
  ts: 00:35:14
  case: runafy
  what: Nhắn riêng khoảng 20 early adopter qua WhatsApp, gửi TestFlight để làm tester; dùng poll Instagram
    hỏi tính năng cần làm.
  tactic: s10-customer-interviews
  tactic_note: Poll story và nhắn riêng người đã trả tiền, dùng để chọn tính năng và tìm tester
- stage: monetize
  ts: 00:27:05
  case: runafy
  what: Early adopter được gói trọn đời; khi launch gửi mã giảm nửa giá cho waitlist, phần lớn doanh thu
    ngày launch đến từ đó.
  tactic: g4-pricing-paywall
  tactic_note: Mã giảm nửa giá gửi cho waitlist ngay khi launch
- stage: launch
  ts: 00:40:55
  case: runafy
  what: 'Ngày launch: story Instagram (khoảng 2.000 follower), post Reddit, video launch cá nhân, email
    cho waitlist; nhắn riêng từng early adopter để kích hoạt tài khoản.'
  tactic: g1-first-10-users
  tactic_note: Dùng audience sẵn có (story, email, Reddit) và nhắn riêng người đã mua
- stage: grow
  ts: 00:29:39
  case: runafy
  what: Đăng 9 reels mỗi ngày trên Instagram vì Instagram không phạt; CTO làm tool sinh 10.000 biến thể
    video trong một phút.
  tactic: g3-organic-content-formats
  tactic_note: Khối lượng lớn trên Instagram; TikTok thì bị giảm view khi đăng nhiều
- stage: grow
  ts: 00:43:33
  case: runafy
  what: Tweet rằng app sắp đạt 100k/tháng khi app mới khoảng 2 tuần; buyer thấy tweet và liên hệ sau đó.
  tactic: g3-organic-content-formats
  tactic_note: Founder-led content trên Twitter; chưa rõ bao nhiêu phần đến từ tweet này
- stage: scale
  ts: 00:47:17
  case: runafy
  what: 'Bán app: giữ 30% equity, thêm earn-out 6 tháng và tiền thưởng; định giá khoảng 5x ARR trên 3k
    MRR ước tính.'
  threshold: 5x ARR
rules:
- ts: 00:36:15
  who: Joseph Choi
  stage: validate
  theme:
  - sell-before-build
  text: Yeah, if someone pays $5 for a landing page that has like two sentences on it, like, they're probably
    like very interested and they're and pretty bought in. Even if it's only $5, like that's a very strong
    signal.
  vi: Nếu có người trả 5 USD cho một landing chỉ hai câu, họ rất quan tâm và đã cam kết; dù chỉ 5 USD,
    đó là tín hiệu rất mạnh.
  evidence: opinion
- ts: 00:23:02
  who: Joseph Choi
  stage: find-idea
  theme:
  - revenue-first
  text: This is interesting validation framework. So, you wanted to see does an existing app that's already
    made like make a lot of money? Check.
  vi: 'Khung kiểm chứng: xem app hiện có đã kiếm được nhiều tiền chưa, rồi mới xem họ làm marketing thế
    nào.'
  evidence: opinion
quotes:
- ts: 00:20:40
  who: Caleb Dean
  stage: validate
  theme:
  - builder-trap
  text: I really wanted to like validate what I'm going to work on before I like commit too much time
    to it
  vi: Tôi muốn kiểm chứng việc sắp làm trước khi dồn quá nhiều thời gian vào nó; app đầu tiên tôi đã mất
    nhiều tháng để build.
- ts: 00:20:59
  who: Caleb Dean
  stage: find-idea
  theme:
  - passion-fuel
  text: I wanted a product that was like tied directly to my passions.
  vi: Tôi muốn một sản phẩm gắn trực tiếp với đam mê của mình.
- ts: 00:50:47
  who: Caleb Dean
  stage: scale
  theme: []
  text: you're better off having 10% of a watermelon rather than like 80% of a grape
  vi: Giữ 10% quả dưa hấu tốt hơn 80% quả nho.
- ts: 00:54:06
  who: Caleb Dean
  stage: find-idea
  theme:
  - revenue-first
  text: I want to be getting into a space where there's like anywhere from one to three apps that are
    at least doing 100k a month.
  vi: 'Tiêu chí của tôi: chọn ngách đang có một đến ba app đạt ít nhất 100k/tháng; không cần đối thủ cạnh
    tranh trực tiếp.'
numbers:
- ts: 00:05:24
  metric: MRR ước tính lúc định giá
  value: 3000
  unit: usd_per_month
  evidence: claimed
- ts: 00:01:27
  metric: người trả 5 USD làm early adopter trước khi app tồn tại
  value: 90
  unit: count
  evidence: claimed
- ts: 00:01:58
  metric: lượt tải từ App Store pre-order lúc launch
  value: 3000
  unit: count
  evidence: claimed
- ts: 00:46:44
  metric: số ngày doanh thu có lúc định giá
  value: 27
  unit: days
  evidence: claimed
- ts: 00:47:17
  metric: equity founder giữ lại khi bán
  value: 30
  unit: percent
  evidence: claimed
frameworks:
- content-before-product
- sell-before-build
- platform-marketplace-distribution
idea_patterns:
- passion-skin
- niche-inside-hot-category
---
## Một câu

Caleb chép format reels và ý tưởng ranked của LiftOff (gym) sang chạy bộ; đo nhu cầu bằng landing 2 câu có nút Stripe (hơn 90 người trả 5 USD) trước khi app tồn tại; pre-order App Store mang về khoảng 3.000 lượt tải lúc launch; app được bán sau khoảng 26 ngày doanh thu với định giá khoảng 5x ARR.

## Bài học cho tôi

- Đo nhu cầu bằng tiền thật trước khi build: landing 2 câu và nút Stripe 5 USD đã có hơn 90 người trả (`00:01:27`).
- Soi app đã chạy trước khi chọn ngách: LiftOff khoảng 200–300k USD/tháng là lý do để chép ý tưởng sang chạy bộ (`00:21:30`).

## Đừng tin vội

- Số liệu là lời kể: MRR 3k là ước tính từ trial khi chưa đủ một tháng doanh thu; không có dashboard. Video không nêu giá bán cuối cùng.
- Tiêu đề "26 ngày" là số ngày doanh thu lúc định giá, không phải toàn bộ thời gian build (CTO làm khoảng 1,5 tháng); dễ hiểu sai.
- Thương vụ phụ thuộc vào người mua cụ thể (app studio có đội distribution, ngách wellness); không sao chép được. Doanh thu ngày launch chủ yếu từ mã giảm giá cho waitlist.
- Host bán buổi Consumer Club và dinner, Superwall tài trợ kênh: đây là phễu, không phải bằng chứng độc lập.
- Video không nêu chi phí, retention đầy đủ hay thời gian từ ý tưởng đến launch.
