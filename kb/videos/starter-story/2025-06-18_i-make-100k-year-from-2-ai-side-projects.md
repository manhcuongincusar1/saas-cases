---
schema: 2
video_id: CoqAxV6b6j4
channel: starter-story
title: I Make $100K/Year From 2 AI Side Projects
date: 2025-06-18
url: https://www.youtube.com/watch?v=CoqAxV6b6j4
transcript: starter-story-kb/videos/2025-06-18_i-make-100k-year-from-2-ai-side-projects/transcript.md
kind: founder_case
speakers:
- name: Ramsri
  role: founder
- name: Pat Walls
  role: host
bias: Semrush tài trợ (ad read, link trial 7 ngày); Starter Story Build được quảng bá. Founder là người
  được kể câu chuyện; số liệu lifetime và người dùng là lời tự báo, không có dashboard.
analyzed: 2026-11-15
cases:
- id: superme
  depth: full
  product: 'SuperMeme (superme.ai): meme generator bằng AI'
  what: Tạo meme bằng AI; xây công khai trên LinkedIn và X trước khi có viral; ra mắt trên Product Hunt
  type:
  - web-app
  customer: Người tạo meme; khoảng 400 người trả tiền (lời founder)
  founder:
    who: Ramsri
    base: Ấn Độ
    technical: null
    team: có đồng sáng lập là fullstack developer và một người làm marketing
    background: Học các khoá kỹ thuật online 2015–2018; viết nội dung về khởi nghiệp 2018–2020; làm việc
      full-time và dành khoảng 2 giờ mỗi tuần cho app
  revenue:
    amount: 130000
    unit: usd
    basis: lifetime
    note: Doanh thu trọn đời (lời founder)
    q: Superme has done lifetime revenue of about 130k USD
    ts: 01:03
    evidence: claimed
  pricing: null
  idea_origin: []
  scale_channels:
  - founder_led_content
  - platform_marketplace
  community_at_discovery: null
  demand_signal: null
  prior_failures: null
  unfair_advantage:
  - value: cofounder
    what: Đồng sáng lập là fullstack developer; có thêm một người marketing
    q: I partnered with the fullstack developer
    ts: 04:43
  - value: domain_expertise
    what: Tự nhận là người làm mảng AI
    q: I'm the AI guy
    ts: 04:58
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: founder_led_content
    what: Đăng bài founder hằng ngày trên mạng xã hội về việc đang làm; người theo dõi thành người dùng
      đầu và cả đồng sáng lập. Video nói chung cho hai app
    q: That's how we got all of our first users.
    ts: 08:24
  - channel: platform_marketplace
    what: Launch trên Product Hunt cùng nhóm người dùng đầu từ mạng xã hội; app đứng số 1 ngày ra mắt
    q: After that we launched on product hunt
    ts: 08:41
  build: null
- id: question-ai
  depth: full
  product: 'Question.ai: tạo câu hỏi trắc nghiệm từ văn bản bằng AI'
  what: Tạo quiz tự động từ văn bản; bản đầu chỉ là hai ô nhập liệu (no-code), sau đó làm lại bản đầy
    đủ
  type:
  - web-app
  customer: Công ty công nghệ và nhà xuất bản làm nhiều quiz (lời founder)
  founder:
    who: Ramsri
    base: Ấn Độ
    technical: null
    team: có đồng sáng lập full-stack từ giai đoạn sau
    background: Học các khoá kỹ thuật online 2015–2018; làm full-time song song với hai app
  revenue:
    amount: 100000
    unit: usd
    basis: lifetime
    note: Doanh thu trọn đời (lời founder, 'around')
    q: question is around 100k USD
    ts: 01:19
    evidence: claimed
  pricing: null
  idea_origin:
  - timing_trigger
  scale_channels:
  - founder_led_content
  community_at_discovery:
    value: Thấy công ty công nghệ và nhà xuất bản tự làm quiz; founder đứng ngoài nhóm đó
    insider: false
    q: large tech companies and publishing companies do a lot of quiz creation
    ts: 06:48
  demand_signal:
    kind: content_views
    level: 2
    what: Đăng bài xây công khai về sản phẩm trước khi có viral; bài nhận từ 10 đến 400 like
    q: Sometimes I used to get 10 likes, sometimes 100 likes, 400 likes.
    ts: 08:07
  prior_failures: null
  unfair_advantage:
  - value: domain_expertise
    what: Tự nhận là người làm mảng AI
    q: I'm the AI guy
    ts: 04:58
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users:
  - channel: founder_led_content
    what: Đăng bài founder hằng ngày trên mạng xã hội; video nói đây là cách có người dùng đầu cho cả
      hai app
    q: That's how we got all of our first users.
    ts: 08:24
  build:
    time: 6 tháng để làm lại bản đầy đủ
    cut: []
    q: spent 6 months and fully ported question to modern tech stack
    ts: 04:43
steps:
- stage: find-idea
  ts: 06:31
  case: question-ai
  what: Chọn việc thủ công người ta đang trả tiền, rồi xét xem AI mới có làm được tốt hơn không
  tactic: s12-timing-shift
  tactic_note: việc thủ công có người trả tiền + khả năng AI mới thay thế
- stage: find-idea
  ts: 06:48
  case: question-ai
  what: Thấy công ty công nghệ và nhà xuất bản làm quiz rất nhiều; đoán AI sẽ tự động hoá được trong vài
    năm
  tactic: s13-others-pain-or-inbound
  tactic_note: nhu cầu của nhóm khác (công ty, nhà xuất bản); founder không thuộc nhóm đó
- stage: validate
  ts: 07:52
  case: question-ai
  what: Viết blog và làm video về tạo quiz trước khi dựng sản phẩm
  tactic: s8-content-demand-test
- stage: build
  ts: 04:43
  case: question-ai
  what: Làm lại bản đầu sang stack mới trong 6 tháng
- stage: launch
  ts: 08:24
  case: superme
  what: Đăng bài founder về sản phẩm hằng ngày trên mạng xã hội; người theo dõi thành người dùng đầu và
    đồng sáng lập
  tactic: g3-organic-content-formats
- stage: launch
  ts: 08:41
  case: superme
  what: Launch trên Product Hunt cùng nhóm người dùng đầu từ mạng xã hội; app lên số 1 ngày ra mắt
  tactic: g9-launch-platforms
quotes:
- ts: 07:04
  who: Ramsri
  stage: find-idea
  theme: []
  text: You should always keep a tab on where generative AI is headed so that you can
  vi: Luôn theo dõi generative AI đang đi về đâu để nhận ra các trường hợp dùng mới.
- ts: 07:36
  who: Ramsri
  stage: mindset
  theme:
  - sell-before-build
  text: Build distribution before building a product.
  vi: Xây kênh phân phối trước khi xây sản phẩm.
- ts: 08:07
  who: Ramsri
  stage: mindset
  theme:
  - persistence
  text: But consistency matters a lot.
  vi: Nhưng kiên trì rất quan trọng.
- ts: 08:24
  who: Ramsri
  stage: launch
  theme: []
  text: That's how I found even co-founders for my app.
  vi: Đó là cách tôi tìm được cả đồng sáng lập cho app.
rules:
- ts: '12:24'
  who: Pat Walls
  stage: mindset
  theme: []
  text: I personally love his approach to building lots of different side projects, not taking the huge
    leap
  vi: Tôi thích cách anh ấy làm nhiều dự án phụ, không nhảy vọt bằng việc nghỉ việc chính.
  evidence: opinion
numbers:
- ts: 01:19
  metric: MRR cộng hai app (lời founder)
  value: 8500
  unit: usd_per_month
  evidence: claimed
- ts: 01:19
  metric: người dùng SuperMeme
  value: 1500000
  unit: count
  evidence: claimed
- ts: 01:35
  metric: người dùng Question
  value: 150000
  unit: count
  evidence: claimed
- ts: 01:35
  metric: người trả tiền SuperMeme
  value: 400
  unit: count
  evidence: claimed
- ts: 09:42
  metric: biên lợi nhuận
  value: 70–75
  unit: percent
  evidence: claimed
- ts: 01:03
  metric: giờ mỗi tuần cho hai app
  value: 2
  unit: hours_per_week
  evidence: claimed
frameworks:
- content-before-product
idea_patterns: []
---
## Một câu

Ramsri, người làm AI, có hai app phụ bên cạnh việc làm chính: SuperMeme và Question. Mỗi app đã có doanh thu trọn đời khoảng 100–130k USD (lời kể). Họ đưa app ra bằng cách viết nội dung về chính vấn đề trước rồi lên Product Hunt.

## Bài học cho tôi

- Viết về chính vấn đề và xây công khai trước khi có sản phẩm; người theo dõi bài đó sau này thành người dùng và đồng sáng lập (`07:36`, `08:24`).
- Tìm việc thủ công người ta đang trả tiền rồi xét xem AI mới có làm tốt hơn không (`06:31`).

## Đừng tin vội

- Doanh thu trọn đời và số người dùng là lời tự báo, không có dashboard. Video không nói rõ số người trả tiền của Question ("18 to 200" không rõ).
- Founder có đồng sáng lập full-stack, có audience trên LinkedIn/Twitter và tự nhận là người làm AI; đây là lợi thế không dễ sao chép.
- Video không nói chi phí, giá gói, hay thời gian làm bản đầu. Founder làm full-time và chỉ dành khoảng 2 giờ mỗi tuần, đây là điều kiện riêng.
- Hai app đều nằm trong làn sóng AI lúc đó; video không nói cạnh tranh ra sao.
- Video có Semrush tài trợ.
