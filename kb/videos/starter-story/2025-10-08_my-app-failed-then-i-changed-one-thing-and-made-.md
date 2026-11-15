---
schema: 2
video_id: hYW9YDwHE20
channel: starter-story
title: My app failed, then I changed one thing, and made $80K
date: 2025-10-08
url: https://www.youtube.com/watch?v=hYW9YDwHE20
transcript: starter-story-kb/videos/2025-10-08_my-app-failed-then-i-changed-one-thing-and-made-80k/transcript.md
kind: founder_case
speakers:
- name: Praneeth
  role: founder
- name: Pat Walls
  role: host
bias: Video có CTA sang Starter Story Build (chương trình bán của kênh) ở đầu và cuối; founder đang bán
  lifetime deal nên khuyên LTD là lợi cho chính anh. Số liệu là lời founder.
analyzed: 2026-11-15
cases:
- id: rabbit-holes
  depth: full
  product: 'Rabbit Holes AI (sau đổi tên Canvas Mode): app chat AI dạng canvas, mỗi nhánh hội thoại là
    một node, cho power AI user'
  what: Thay vì chat tuyến tính, cho người dùng rẽ nhánh cuộc trò chuyện với ChatGPT, Claude, Perplexity
    trong một tab
  type:
  - desktop-app
  customer: Power AI user muốn hội thoại dài và nhiều nhánh; khoảng 1.200 khách trả tiền, 60% là mua một
    lần
  founder:
    who: Praneeth
    base: Ấn Độ (theo lời dẫn video)
    technical: null
    team: null
    background: UX designer; trước đó làm kỹ sư phần mềm (theo lời dẫn video); 6–7 năm làm nhiều sản phẩm
  revenue:
    amount: 80000
    unit: usd
    basis: other
    note: '''gross revenue'' tại lúc phỏng vấn, không nêu là tháng hay tổng; câu ''$80,000 in the last
      6 months'' ở 01:00 là 6 tháng sau khi đổi sang mua một lần'
    q: around 80k-ish in gross revenue as we speak
    ts: 08:47
    evidence: claimed
  pricing: Mua một lần (lifetime deal) $29 khi dưới 100 user, lên $49 sau khi qua 100 user; BYOK (khách
    tự trả API AI); định hướng chuyển sang gói định kỳ khi có ~1.200 user
  idea_origin:
  - own_pain
  - domain_expertise
  scale_channels:
  - founder_led_content
  community_at_discovery:
    value: là power AI user, dùng ChatGPT, Perplexity và Claude cùng lúc, mỗi tab một thế mạnh
    insider: true
    q: I was using ChatGPT, and I was using Perplexity, and I was using Claude
    ts: 01:46
  demand_signal: null
  prior_failures:
    count: 1
    what: bản web app freemium/free trial, không có traction; founder cho rằng thiếu personal brand và
      ICP đã bão hoà subscription
    q: but that didn't get much traction
    ts: 02:48
  unfair_advantage:
  - value: domain_expertise
    what: là UX designer, thấy trải nghiệm nhiều tab AI bị vỡ mạch suy nghĩ
    q: the UX designer in me thought
    ts: 02:17
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users: []
  build:
    time: null
    cut:
    - bỏ mô hình web app đăng ký (subscription/freemium)
    - 'không gánh chi phí server và AI: đưa về máy người dùng (BYOK, desktop app)'
    q: I had to build a desktop app
    ts: 04:09
steps:
- stage: find-idea
  ts: 01:46
  case: rabbit-holes
  what: Dùng ChatGPT, Perplexity và Claude cùng lúc, mỗi tab một thế mạnh; là UX designer, thấy trải nghiệm
    nhiều tab bị vỡ nên ý tưởng là gom vào một canvas.
  tactic: s5-insider
  tactic_note: nỗi đau riêng của power AI user, kết hợp nghề UX designer
- stage: monetize
  ts: 02:48
  case: rabbit-holes
  what: 'Ra mắt web app freemium: vài câu hỏi miễn phí rồi phải trả tiền sau một lúc dùng; không có traction.'
  tactic: g4-pricing-paywall
- stage: monetize
  ts: 03:53
  case: rabbit-holes
  what: Đổi sang mua một lần (lifetime deal) với BYOK; chuyển app sang desktop để không có chi phí server,
    người dùng tự trả tiền AI.
  tactic: g4-pricing-paywall
  tactic_note: lifetime deal + bring-your-own-keys + desktop app chạy trên máy người dùng
- stage: build
  ts: 04:09
  case: rabbit-holes
  what: 'Bỏ server: đưa app về máy người dùng bằng desktop app để bán một lần mà không phải duy trì chi
    phí hạ tầng.'
- stage: monetize
  ts: 07:12
  case: rabbit-holes
  what: Đặt giá LTD $29 khi dưới 100 user, lên $49 khi qua 100 user; định hướng gói định kỳ khi khoảng
    1.200 user.
  tactic: g4-pricing-paywall
  tactic_note: giá thấp cho người mua sớm, tăng giá theo mốc user
- stage: grow
  ts: 08:00
  case: rabbit-holes
  what: 'Viết lại landing page cho đúng ICP (power AI user): gọi tên ICP trong H1 và nhiều chỗ khác trên
    trang.'
  tactic: g11-positioning-messaging
  tactic_note: landing page viết riêng cho một ICP, không phải SEO hay quảng cáo
- stage: grow
  ts: 08:16
  case: rabbit-holes
  what: Nói về chủ đề AI trên Twitter, trả lời các cuộc trò chuyện liên quan và gợi ý sản phẩm, không
    bán thẳng.
  tactic: g3-organic-content-formats
quotes:
- ts: 02:48
  who: Praneeth
  stage: launch
  theme: []
  text: The top ones are that I did not have a huge personal brand trying to do the building public thing
    where I was talking on Twitter or kind of posting everywhere where I got a chance.
  vi: Lý do chính là tôi không có personal brand đủ lớn để build in public, nói về nó trên Twitter hay
    đăng ở khắp nơi khi có cơ hội.
- ts: 04:25
  who: Praneeth
  stage: monetize
  theme: []
  text: As soon as they changed it, a lot of people actually started paying.
  vi: Ngay khi tôi đổi mô hình, nhiều người bắt đầu trả tiền.
- ts: 05:25
  who: Praneeth
  stage: monetize
  theme: []
  text: So, almost every bootstrap business should do a lifetime deal along with whatever they are doing.
  vi: Hầu hết doanh nghiệp bootstrap nên làm lifetime deal song song với mô hình hiện tại.
- ts: '11:24'
  who: Praneeth
  stage: mindset
  theme:
  - right-audience
  text: what I was doing was appealing to my peers, which is totally not the mindset that I need to have
    as an entrepreneur
  vi: Điều tôi làm là lấy lòng đồng nghiệp, và đó hoàn toàn không phải tư duy cần có của một founder.
rules:
- ts: 00:30
  who: Pat Walls
  stage: monetize
  theme: []
  text: I would not recommend starting with a subscription model if you're bootstrapping.
  vi: Tôi không khuyên bắt đầu bằng mô hình đăng ký nếu đang bootstrap.
  evidence: opinion
- ts: 06:10
  who: Pat Walls
  stage: launch
  theme: []
  text: At its core, it's as simple as creating something valuable and putting a Stripe payment link on
    it.
  vi: Về cốt lõi, kiếm tiền online đơn giản như tạo ra thứ có giá trị rồi gắn một link thanh toán Stripe.
  evidence: opinion
numbers:
- ts: 08:47
  metric: gross revenue tại lúc phỏng vấn (lời founder)
  value: 80000
  unit: usd
  evidence: claimed
- ts: 08:47
  metric: lợi nhuận ước tính sau hoàn tiền (lời founder 'about 75')
  value: khoảng 75k
  unit: usd
  evidence: claimed
- ts: 09:02
  metric: khách trả tiền
  value: 1200
  unit: count
  evidence: claimed
- ts: 09:19
  metric: unique visitors của website
  value: 38000
  unit: count
  evidence: claimed
- ts: '10:37'
  metric: 'chi phí hằng tháng: hosting landing page (~$50) và Cursor (~$200)'
  value: ~250
  unit: usd_per_month
  evidence: claimed
- ts: 07:12
  metric: giá lifetime deal ban đầu khi dưới 100 user
  value: 29
  unit: usd
  evidence: claimed
frameworks: []
idea_patterns: []
---
## Một câu

Praneeth ra mắt một app chat AI dạng canvas theo kiểu web subscription và không có traction; anh đổi sang mua một lần kèm BYOK và desktop app, rồi đạt gần $80k doanh thu gộp (lời founder).

## Bài học cho tôi

- Đổi mô hình giá trước khi đổi tính năng: cùng một sản phẩm, bán một lần kèm BYOK thì người trả tiền nhiều hơn (`04:25`).
- Viết landing page cho đúng một ICP (gọi tên ICP ngay H1) trước khi đẩy traffic (`08:00`).

## Đừng tin vội

- Số liệu là lời founder, không có dashboard. "Gross revenue" không nói là tổng hay theo tháng; "80k trong 6 tháng" là mốc sau khi đổi mô hình, không tính từ lúc bắt đầu.
- Lời khuyên "mọi bootstrap business nên làm LTD" đến từ người đang bán LTD. Video không có dữ liệu giữ chân hay churn; anh cũng nói đang chuyển sang gói định kỳ nhưng không nói kết quả.
- Host Starter Story bán Starter Story Build (CTA ở 06:10 và 12:10): phễu của kênh.
- Điều kiện riêng: nghề UX designer, và ICP là power AI user, một nhóm đã có nhiều subscription (lời founder). Video không nói thời gian build, chi phí phát triển, hay cách có 10 khách đầu tiên.
