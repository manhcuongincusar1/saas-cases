---
schema: 2
video_id: W48emwbUlUE
channel: starter-story
title: How I Built a $12K/Month Micro-SaaS
date: 2026-02-11
url: https://www.youtube.com/watch?v=W48emwbUlUE
transcript: starter-story-kb/videos/2026-02-11_how-i-built-a-12k-month-micro-saas/transcript.md
kind: founder_case
speakers:
- name: Vikash
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: 'Starter Story bán chương trình Starter Story Build (video có link và mã TINY, lặp lại ở cuối):
  đây là phễu bán chương trình. Con số $12k/tháng là lời founder kèm dashboard Gumroad.'
analyzed: 2026-11-15
cases:
- id: bulkmockup
  depth: full
  product: BulkMockup, plugin Photoshop tạo mockup hàng loạt
  what: Plugin Photoshop đặt thiết kế vào template mockup hàng loạt; làm tay mất 30–60 phút, plugin làm
    khoảng 2 phút
  type:
  - desktop-plugin
  customer: Người bán print-on-demand (Etsy) cần mockup hàng loạt
  founder:
    who: Vikash
    base: Ấn Độ
    technical: true
    team: solo; sau đó thuê developer trên Upwork để polish
    background: Freelance Photoshop trên Upwork và Freelancer
  revenue:
    amount: 12000
    unit: usd
    basis: monthly
    note: khoảng 12–13k/tháng, đọc từ dashboard Gumroad (doanh số một năm gần nhất)
    q: So, I've been constantly hitting around 12,000 13,000 a month.
    ts: 02:02
    evidence: measured
  pricing: Ban đầu bán một lần, sau đó lifetime deal vài năm; hiện thu phí hàng tháng
  idea_origin:
  - user_request
  - domain_expertise
  scale_channels:
  - youtube_founder
  - seo
  community_at_discovery:
    value: Freelancer Photoshop trên Upwork/Freelancer, làm việc cho khách print-on-demand
    insider: true
    q: I started doing freelance work on Upwork
    ts: 02:02
  demand_signal:
    kind: paid
    level: 8
    what: Khách freelance trả $300 cho kết quả của một script (1.800 mockup trong khoảng 30 phút) khi
      chưa có sản phẩm
    q: the customer wired me $300
    ts: 02:52
  prior_failures:
    count: 1
    what: Bán script một lần rồi nhận ra không phòng thủ được; bản UI/UX đầu chưa có license validation
      nên phải bán lifetime deal vài năm
    q: soon realized that it cannot be defensible
    ts: 03:40
  unfair_advantage:
  - value: domain_expertise
    what: 'Làm freelance Photoshop: các job nhận được toàn là việc Photoshop'
    q: These were all Photoshop jobs
    ts: 02:19
  - value: technical_skill
    what: Tự học JavaScript trong một ngày rồi viết được script Photoshop chạy được việc
    q: I hacked out a Photoshop script that did the job
    ts: 02:35
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: youtube_founder
    what: Video không nói 10 khách đầu tiên; khách hiện tới qua YouTube của founder (video hướng dẫn trả
      lời đúng một vấn đề)
    q: Customers find us through YouTube
    ts: 01:46
  build:
    time: khoảng 2 tháng nhốt mình viết lại thành bản UI/UX
    cut: []
    q: I locked myself into my room for two straight months
    ts: 03:40
steps:
- stage: find-idea
  ts: 02:19
  case: bulkmockup
  what: Nhận việc freelance Photoshop trên Upwork/Freelancer; khi khách muốn tự động hoá một phần việc,
    anh viết script thay vì bỏ việc.
  tactic: s6-upwork-demand
- stage: validate
  ts: 02:52
  case: bulkmockup
  what: Làm 1.800 mockup cho khách bằng script trong khoảng 30 phút; khách trả $300 ngay.
  tactic: s7-preorder-buy-button
  tactic_note: 'dịch vụ làm tay: Bán kết quả thủ công (script chạy một lần) cho khách freelance trước
    khi có sản phẩm'
- stage: build
  ts: 03:40
  case: bulkmockup
  what: Nhốt mình khoảng 2 tháng để biến script hack thành bản có UI/UX.
- stage: monetize
  ts: 03:56
  case: bulkmockup
  what: Bán một lần rồi lifetime deal vài năm vì chưa làm được license validation và quản lý user.
  tactic: g4-pricing-paywall
  tactic_note: Lifetime deal (bán một lần) do chưa có license
- stage: build
  ts: 04:12
  case: bulkmockup
  what: Dùng tiền từ lifetime deal thuê developer trên Upwork để polish sản phẩm.
- stage: find-idea
  ts: 07:02
  case: bulkmockup
  what: Đọc lặng lẽ các cộng đồng khách hay tụ tập, ghi lại nỗi đau lặp lại; chỉ trò chuyện khi thấy lặp
    lại, không bán hàng trong đó.
  tactic: s3-reddit-pain-mining
- stage: find-idea
  ts: 07:17
  case: bulkmockup
  what: Gửi email onboarding hỏi khách muốn hướng dẫn riêng về gì; câu trả lời thành ý tưởng video.
  tactic: s10-customer-interviews
  tactic_note: 'sau launch: Hỏi khách mới qua email onboarding để lấy ý tưởng nội dung'
- stage: find-idea
  ts: 07:32
  case: bulkmockup
  what: Trong hỗ trợ khách, đề nghị khách gửi file rồi quay video hướng dẫn riêng hoặc gọi để làm cùng;
    các buổi này thành nội dung.
  tactic: s10-customer-interviews
  tactic_note: Support call và hướng dẫn riêng cho khách; ghi lại để làm nội dung
- stage: find-idea
  ts: 08:19
  case: bulkmockup
  what: Tìm video YouTube trong ngách có ít view nhưng nhiều comment (comment là nỗi đau chưa được giải),
    liệt kê các phản đối rồi làm video trả lời tốt hơn.
  tactic: s4-tiktok-comment-mining
  tactic_note: Comment YouTube trong ngách, không phải TikTok
- stage: grow
  ts: 06:01
  case: bulkmockup
  what: Quay video ngắn, không intro, đi thẳng vào giải pháp cho một vấn đề cụ thể; một video ~370 view
    mang 3 khách (~$45 MRR), video 12k view ~$213 trong 6 tháng.
  tactic: g3-organic-content-formats
- stage: grow
  ts: '10:07'
  case: bulkmockup
  what: 'Trước khi đăng, tối ưu video cho tìm kiếm Google: từ khoá trong tiêu đề, mô tả và 30 giây đầu
    transcript.'
  tactic: g2-aso-seo-organic
quotes:
- ts: 04:42
  who: Vikash
  stage: grow
  theme: []
  text: My growth or marketing is what I call a content flywheel, and the fuel of this content flywheel
    is customer pain.
  vi: Tăng trưởng của tôi là thứ tôi gọi là content flywheel; nhiên liệu của nó là nỗi đau của khách.
- ts: 05:12
  who: Vikash
  stage: grow
  theme: []
  text: You do not need to get a viral video to be successful at marketing a product.
  vi: Bạn không cần video viral để marketing thành công.
- ts: 06:01
  who: Vikash
  stage: grow
  theme: []
  text: People love when you speak to the problem directly.
  vi: Người ta thích khi bạn nói thẳng vào vấn đề của họ.
- ts: '13:42'
  who: Vikash
  stage: mindset
  theme: []
  text: I had been grinding 14-16 hours a day in my past and that resulted in a spine surgery last year.
  vi: Trước đây tôi làm 14–16 giờ mỗi ngày và năm ngoái đã phải phẫu thuật cột sống.
- ts: '13:58'
  who: Vikash
  stage: mindset
  theme: []
  text: Just be obsessed with your customer's problem.
  vi: Hãy ám ảnh với vấn đề của khách hàng.
rules:
- ts: 08:35
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme: []
  text: The ones that solve one problem for one very specific type of customer.
  vi: Những app giải một vấn đề cho một kiểu khách rất cụ thể.
  evidence: opinion
- ts: '10:54'
  who: Pat Walls
  stage: find-idea
  theme: []
  text: What I think is really special about what you do is that you actually talk to customers.
  vi: Điều đặc biệt ở anh là anh thực sự nói chuyện với khách.
  evidence: opinion
- ts: '12:26'
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme:
  - revenue-first
  text: does your tool make people more money? Does it save them more money? Or does it save them time?
  vi: Công cụ của bạn giúp người ta kiếm thêm tiền, tiết kiệm tiền, hay tiết kiệm thời gian?
  evidence: opinion
- ts: '14:28'
  who: Gus
  stage: validate
  theme:
  - emotional-bottleneck
  text: a lot of people are afraid to talk to customers or kind of hear from customers.
  vi: Nhiều người sợ nói chuyện hoặc lắng nghe khách.
  evidence: opinion
- ts: '16:29'
  who: Pat Walls hoặc Gus
  stage: find-idea
  theme: []
  text: I think that's a great place to start rather than building a SaaS that boils the whole ocean
  vi: Đó là chỗ bắt đầu tốt, thay vì xây một SaaS muốn giải cả đại dương.
  evidence: opinion
numbers:
- ts: 05:44
  metric: MRR từ một video ~370 view (3 khách, ~$15/tháng mỗi khách)
  value: 45
  unit: usd_per_month
  evidence: claimed
- ts: 05:44
  metric: doanh thu một video 12.000 view trong 6 tháng
  value: 213
  unit: usd
  evidence: claimed
- ts: 08:03
  metric: số video đã ghi từ support call trong 3 năm
  value: 1500
  unit: count
  evidence: claimed
- ts: '10:23'
  metric: tỉ lệ lượt xem YouTube của kênh đến từ Google Search
  value: 22
  unit: percent
  evidence: claimed
frameworks:
- one-feature-per-app
- customer-pain-content-flywheel
idea_patterns:
- single-feature-on-platform
---
## Một câu

Vikash làm plugin Photoshop tạo mockup hàng loạt (~$12–13k/tháng), ý tưởng từ việc làm freelance Photoshop; khách đến từ YouTube của chính anh, nội dung lấy từ nỗi đau của khách (cộng đồng, email onboarding, support call, comment YouTube).

## Bài học cho tôi

- Khách đầu tiên trả $300 cho kết quả của một script còn thô, trước khi có sản phẩm (`02:52`).
- Video không cần viral: một video giải đúng một nỗi đau kiếm được vài trăm USD sau nhiều tháng (`05:44`).

## Đừng tin vội

- $12k/tháng là dashboard Gumroad của một năm gần nhất, không nói chi phí, churn hay lợi nhuận. Video không nói bao lâu để đạt mức này, cũng không nói 10 khách đầu tiên đến từ đâu.
- Starter Story bán Starter Story Build (mã TINY) nên video là phễu bán chương trình; mọi thứ về "tự động" và "vài ngày" là lời quảng bá.
- Điều kiện riêng: founder có nghề Photoshop và nhiều năm làm việc cho khách print-on-demand; 1.500 video support call và kênh YouTube là tài sản tích luỹ, không phải thứ có ngay.
