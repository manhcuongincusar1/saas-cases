---
schema: 2
video_id: xWnqY2Mav4s
channel: starter-story
title: I Built Two Apps That Make $120K/Month
date: 2026-06-07
url: https://www.youtube.com/watch?v=xWnqY2Mav4s
transcript: starter-story-kb/videos/2026-06-07_i-built-two-apps-that-make-120k-month/transcript.md
kind: founder_case
speakers:
- name: Kyle Fowler
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story bán database ý tưởng (quảng cáo giữa video) và tuyển dụng; kênh có lợi khi founder
  thành công. Số doanh thu do founder đọc 'up to like' theo yêu cầu host; không có chi phí, churn hay
  giá gói.
analyzed: 2026-11-15
cases:
- id: cardstock
  depth: full
  product: 'CardStock (openbraceapps.com): app quét thẻ thể thao để nhận diện và xem giá trị thẻ'
  what: Dùng camera điện thoại nhận diện thẻ, xem giá trị và lịch sử bán gần đây, thêm vào bộ sưu tập
    để theo dõi giá
  type:
  - mobile-app
  customer: Người sưu tập thẻ thể thao
  founder:
    who: Kyle Fowler
    base: null
    technical: true
    team: ban đầu 3 người trong tầng hầm, nay 5 người
    background: Tự học code từ nhỏ, làm một game iOS nhỏ (Snake In) trước khi làm CardStock
  revenue:
    amount: 75000
    unit: usd
    basis: mrr
    note: founder nói 'about 15,000 subscriptions' và 'up to like 75k' MRR; đọc theo yêu cầu host mở dashboard
    q: up to like 75k monthly recurring revenue
    ts: 02:05
    evidence: measured
  pricing: null
  idea_origin:
  - own_pain
  - passion_skin
  scale_channels: []
  community_at_discovery:
    value: Người sưu tập thẻ thể thao từ nhỏ, tự gặp vấn đề quản lý bộ sưu tập
    insider: true
    q: I've been collecting cards since I was a kid.
    ts: 06:34
  demand_signal:
    kind: built_first
    level: 0
    what: Build xong rồi mới đăng bài cập nhật lên Reddit; có lượt tải gần như ngay (video không nêu số)
    q: and so then I finished it and gave a Reddit update post about having completed it.
    ts: 05:31
  prior_failures: null
  unfair_advantage:
  - value: technical_skill
    what: Thích lập trình từ nhỏ, học iOS và làm game iOS nhỏ trước khi làm CardStock
    q: I definitely really always loved anything coding development-related when I was younger.
    ts: 02:52
  - value: cofounder
    what: Bạn bè làm cùng từ đầu, được chia doanh thu ba cách (video không gọi họ là co-founder)
    q: wanted to come help and split the rev three ways
    ts: 03:41
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 72
      value: 6 năm từ lúc ra mắt tới nay
      q: I launched Card Stock 6 years ago
      ts: 01:02
  first_users:
  - channel: reddit
    what: Đăng bài cập nhật lên Reddit khi vừa build xong; lượt tải đầu đến ngay sau đó (video không nói
      Reddit mang về bao nhiêu người)
    q: gave a Reddit update post about having completed it
    ts: 05:31
  build:
    time: khoảng 6 tháng từ ý tưởng tới khi hoàn thành, có khoảng nghỉ ~3 tháng ở giữa
    cut: []
    q: probably like six months from idea to completion
    ts: 05:31
- id: scanemon
  depth: full
  product: 'Scanemon (scanemon.com): cùng loại với CardStock nhưng cho thẻ Pokémon'
  what: Quét thẻ Pokémon để nhận diện và xem giá trị, giống CardStock
  type:
  - mobile-app
  customer: Người sưu tập thẻ Pokémon
  founder:
    who: Kyle Fowler
    base: null
    technical: true
    team: null
    background: null
  revenue:
    amount: 17000
    unit: usd
    basis: mrr
    note: founder đọc '17k monthly recurring revenue' theo yêu cầu host mở dashboard
    q: 17k monthly recurring revenue
    ts: 02:36
    evidence: measured
  pricing: null
  idea_origin:
  - adjacent_expansion
  scale_channels: []
  community_at_discovery: null
  demand_signal: null
  prior_failures: null
  unfair_advantage: []
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 12
      value: khoảng 1 năm từ lúc ra mắt tới nay
      q: We launched it only a year ago
      ts: 02:20
  first_users: []
  build:
    time: MVP xong trong một ngày, nhờ AI agent sinh gần như toàn bộ app
    cut: []
    q: The MVP for Scanemon I made in a day.
    ts: 05:47
steps:
- stage: find-idea
  ts: 06:34
  case: cardstock
  what: 'Ý tưởng từ nỗi đau của chính Kyle: sưu tập thẻ từ nhỏ, muốn catalog và sắp xếp nhưng không biết
    thẻ nào là thẻ nào; kiểm App Store không thấy app nên tự làm.'
  tactic: s5-insider
- stage: find-idea
  ts: 02:20
  case: scanemon
  what: Làm Scanemon bằng cách giữ nguyên app của CardStock và đổi sang thẻ Pokémon.
  tactic: s9-niche-narrowing
  tactic_note: 'Mở sang ngách kề của sản phẩm đang chạy: cùng app, đổi chủ đề thẻ'
- stage: build
  ts: 05:31
  case: cardstock
  what: Làm bản đầu trong khoảng 6 tháng, có khoảng nghỉ ~3 tháng, rồi hoàn thiện.
- stage: build
  ts: 05:47
  case: scanemon
  what: Dùng AI agent sinh gần như toàn bộ app; MVP xong trong một ngày.
- stage: launch
  ts: 05:31
  case: cardstock
  what: Đăng bài cập nhật lên Reddit khi vừa xong bản build; lượt tải đầu đến ngay sau đó.
  tactic: g1-first-10-users
  tactic_note: Bài cập nhật trên cộng đồng Reddit; video không nói số người dùng đầu tiên
- stage: monetize
  ts: 04:59
  case: cardstock
  what: Sau bản đầu thì thêm RevenueCat để quản lý gói đăng ký (subscription).
  tactic: g4-pricing-paywall
  tool: RevenueCat
- stage: grow
  ts: 09:25
  what: 'Làm slideshow TikTok theo một format lặp lại: thử format nào vừa có view vừa convert, rồi cân
    bằng hai thứ để kéo lượt tải.'
  tactic: g3-organic-content-formats
  tactic_note: Slideshow TikTok lặp format; video không gắn riêng cho app nào
- stage: grow
  ts: 09:41
  what: 'Trả creator theo view qua nền tảng Noise: creator nhận template slideshow, đăng, và được trả
    theo số view.'
  tactic: g7-creator-ops
  tool: Noise
  tactic_note: Trả theo view kiểu clipping; áp dụng chung cho marketing app 2026, không gắn riêng sản
    phẩm nào
- stage: scale
  ts: 03:41
  what: Khi chưa có doanh thu, chia doanh thu ba cách cho các bạn để cùng làm; sau đó đội lên 5 người.
quotes:
- ts: 07:05
  who: Kyle Fowler
  stage: mindset
  theme:
  - passion-fuel
  text: I've just always wanted to work for myself doing something I love, and what better way than solving
    your own problems to do that.
  vi: Tôi luôn muốn làm việc cho chính mình, làm việc mình yêu thích; và cách tốt nhất là giải quyết vấn
    đề của chính mình.
- ts: 08:08
  who: Kyle Fowler
  stage: find-idea
  theme: []
  text: Step one is to find a problem or opportunity, create some sort of notes document or anything in
    your phone where you can write down ideas.
  vi: 'Bước một: tìm vấn đề hoặc cơ hội, ghi ý tưởng vào ghi chú hoặc bất cứ thứ gì trên điện thoại.'
- ts: 08:25
  who: Kyle Fowler
  stage: build
  theme: []
  text: Most people, I think, have been overestimating how hard it is to build apps, and AI just makes
    them realize that it's actually easy.
  vi: Tôi nghĩ hầu hết người ta đánh giá quá cao độ khó làm app; AI khiến họ thấy nó thật ra dễ.
- ts: 07:21
  who: Kyle Fowler
  stage: find-idea
  theme: []
  text: regardless of whether you make money after doing all these steps and building your app, publishing
    it, trying to market it, if you can solve a problem for yourself, the odds are other people have that
    problem.
  vi: Dù có kiếm được tiền hay không, nếu giải quyết được vấn đề của chính mình thì khả năng người khác
    cũng có vấn đề đó.
- ts: '11:13'
  who: Kyle Fowler
  stage: mindset
  theme:
  - learn-from-others
  text: I think my best advice to myself in the past would definitely be that people are usually happy
    to help and share information.
  vi: 'Lời khuyên tôi tự nhủ ngày trước: người ta thường sẵn lòng giúp và chia sẻ thông tin.'
rules:
- ts: 03:57
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme: []
  text: Personally, I love Kyle's approach to building. It's proof that the best app ideas come from personal
    problems that you notice in your own life.
  vi: 'Tôi thích cách Kyle làm: đó là bằng chứng rằng ý tưởng app hay nhất đến từ vấn đề cá nhân bạn gặp
    trong đời sống.'
  evidence: opinion
- ts: 07:21
  who: Pat Walls hoặc Gus
  stage: validate
  theme: []
  text: I think that's a good lesson for anyone watching this that you still have to go through all those
    learnings to figure out if this thing can actually work.
  vi: 'Đó là bài học cho người xem: vẫn phải đi qua tất cả những bước học để biết ý tưởng có thật sự chạy
    được không.'
  evidence: opinion
- ts: '13:49'
  who: Pat Walls hoặc Gus
  stage: validate
  theme: []
  text: AI has enabled you to have an like see a problem right now that you're experiencing in your daily
    life and ship it within a few hours and then test it in the market
  vi: AI cho phép bạn thấy vấn đề đang gặp hằng ngày, làm ra bản đầu trong vài giờ rồi thử trên thị trường.
  evidence: opinion
numbers:
- ts: 02:05
  metric: 'CardStock: số đăng ký đang trả (active subscriptions)'
  value: 15000
  unit: count
  evidence: measured
- ts: 02:20
  metric: 'CardStock: lượt tải mỗi tháng'
  value: 13000
  unit: count
  evidence: measured
- ts: 02:20
  metric: 'Scanemon: số đăng ký đang trả (active subscriptions)'
  value: 3400
  unit: count
  evidence: measured
- ts: 02:36
  metric: 'Scanemon: khách mới mỗi tháng'
  value: 16000
  unit: count
  evidence: measured
frameworks: []
idea_patterns:
- passion-skin
---

## Một câu

Một dev tự học làm hai app từ nỗi đau sưu tập thẻ của chính mình: CardStock (~75k MRR, "up to like") và Scanemon (bản đổi sang thẻ Pokémon, ~17k MRR), đều đọc số từ dashboard theo yêu cầu host.

## Bài học cho tôi

- Sau khi có một app chạy, Kyle mở ngách kề bằng cách giữ nguyên sản phẩm và đổi chủ đề thẻ, thay vì làm lại từ đầu (`02:20`, `06:34`).
- Thời gian thật: bản đầu CardStock mất khoảng 6 tháng, app thứ hai chỉ một ngày nhờ AI sinh gần như toàn bộ; nhưng video không có bằng chứng nhu cầu trước khi build (`05:31`, `05:47`).

## Đừng tin vội

- Đây là case build-first (mức 0): lượt tải đến ngay sau bài Reddit, nhưng video không cho biết Reddit mang về bao nhiêu người dùng đầu tiên.
- Số liệu là "about"/"up to like" và không có lịch sử theo tháng; chi phí, churn, tỉ lệ chuyển đổi và giá gói đều không được nêu.
- Kênh phễu: đoạn giữa quảng cáo database 90+ ý tưởng; founder kể thành công nên có động lực làm câu chuyện đẹp.
- Điều kiện riêng khó chép: Kyle có sẵn kỹ năng code và đam mê sưu tập thẻ từ nhỏ; ngách thẻ thể thao/Pokémon đã có người trả tiền (điều video không chứng minh cho ngách khác).
