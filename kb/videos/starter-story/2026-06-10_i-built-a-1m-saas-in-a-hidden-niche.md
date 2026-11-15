---
schema: 2
video_id: NPpky92ZfjA
channel: starter-story
title: "I Built A $1M SaaS In A Hidden Niche"
date: 2026-06-10
url: https://www.youtube.com/watch?v=NPpky92ZfjA
transcript: starter-story-kb/videos/2026-06-10_i-built-a-1m-saas-in-a-hidden-niche/transcript.md
kind: founder_case
speakers:
- {name: Zach, role: founder}
- {name: Pat Walls, role: host}
- {name: Gus, role: host}
bias: "Starter Story bán database '30+ Business Ideas in Unsexy Niches' (quảng cáo giữa và cuối video, link trong mô tả) và chọn founder để kể; chỉ thấy một case đang chạy tốt, không có số khách rời hay chi phí bán hàng. Founder có nền 10 năm (agency, ETL, Amazon), khác xa người mới bắt đầu."
analyzed: 2026-11-15
cases:
- id: hero-analytics
  depth: full
  product: "Hero Analytics (hiroanalytics.com): dashboard analytics và báo cáo cho agency email/SMS marketing"
  what: "Một dashboard cho agency xem toàn bộ client, kéo dữ liệu từ các nền tảng họ chạy cho khách, theo dõi team so với mục tiêu"
  type: [web-app]
  customer: "Agency email/SMS marketing quản lý nhiều brand (10–30 brand mỗi agency); trả theo số client và seat cho nhân viên và khách của họ"
  founder:
    who: Zach
    base: null
    technical: null
    team: "2 người: Zach và đồng sáng lập Brendan"
    background: "Từng làm data visualization startup (được Amazon mua), làm việc tại Amazon, một newsletter thất bại, rồi chạy agency email marketing ~6 năm"
  revenue:
    amount: 96200
    unit: usd
    basis: mrr
    note: "MRR khoảng 96.2k trên Stripe 4 tuần gần nhất; founder nói tổng ARR đã vượt $1M trong 19 tháng"
    q: "We're at about 96.2K"
    ts: "02:05"
    evidence: measured
  pricing: "Subscription, trial 30 ngày; giá theo số client của agency (ví dụ 10 client ~$500/tháng, 20 client ~$600); agency lớn đàm phán riêng; thêm seat ~$10/tháng mỗi người"
  idea_origin: [own_pain, domain_expertise]
  scale_channels: [b2b_deals]
  community_at_discovery:
    value: "Đang vận hành agency email marketing ~6 năm, có ~30 client là ICP; Brendan bực với điểm nghẽn của agency nên quyết tự build"
    insider: true
    q: "We had around 30 clients who were kind of like our ICP for this app."
    ts: "03:06"
  demand_signal: null
  prior_failures:
    count: 1
    what: "Newsletter business thất bại sau khi rời Amazon; từ đó học email marketing rồi làm agency"
    q: "We started a failed newsletter business."
    ts: "09:36"
  unfair_advantage:
  - {value: domain_expertise, what: "Chạy agency email marketing ~6 năm, biết nền tảng và người chơi trong ngách", q: "So, we knew the platforms, we knew the players, we knew what mattered.", ts: "08:04"}
  - {value: technical_skill, what: "Nền tảng ETL cũ, tự dựng bảng dữ liệu; sau đó chuyển sang cloud code", q: "we like had this oddly specific old background in ETL", ts: "04:24"}
  - {value: cofounder, what: "Đồng sáng lập Brendan", q: "partner Brendan and I built a analytics platform", ts: "01:00"}
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: {months: 19, value: "19 tháng từ lúc ra mắt tới mức ~$1M ARR", q: "Gone from zero to over a million in ARR over those 19 months", ts: "00:00"}
  first_users: []
  build:
    time: "ra mắt khoảng 19 tháng trước; founder nói để có Hero phải mất khoảng 10 năm kinh nghiệm trước đó"
    cut: []
    q: "We launched it about 19 months ago"
    ts: "00:00"
steps:
- stage: find-idea
  ts: "03:06"
  case: hero-analytics
  what: "Chạy agency email marketing ~6 năm với ~30 client là ICP; Brendan bực với các điểm nghẽn của agency nên tự build công cụ."
  tactic: s5-insider
  tactic_note: "Loại: nghề (agency email marketing ~6 năm) và pain của Brendan với điểm nghẽn agency"
- stage: monetize
  ts: "02:36"
  case: hero-analytics
  what: "Thu phí theo số client của agency (ví dụ 10 client ~$500/tháng), trial 30 ngày, thêm seat cho nhân viên."
  tactic: g4-pricing-paywall
- stage: find-idea
  ts: "05:28"
  case: hero-analytics
  what: "Bán cho agency (mỗi agency kéo 10–30 brand) thay vì bán lẻ từng brand; agency cấp seat cho khách của họ."
  tactic: s9-niche-narrowing
  tactic_note: "Chọn đối tượng là agency thay vì brand: một khách mang nhiều khách"
- stage: launch
  ts: "06:13"
  case: hero-analytics
  what: "Lấy danh sách agency từ thư mục partner của Shopify và nền tảng Claio, xếp hạng theo quy mô để tiếp cận."
  tactic: g9-launch-platforms
  tactic_note: "Dùng thư mục partner của nền tảng để tìm agency, không chạy quảng cáo"
quotes:
- ts: "05:58"
  who: Zach
  stage: find-idea
  theme: []
  text: "agencies are really easy to find."
  vi: "Agency rất dễ tìm: vào thư mục partner của nền tảng là có danh sách xếp hạng theo quy mô và ảnh hưởng."
- ts: "05:28"
  who: Zach
  stage: find-idea
  theme: [right-audience]
  text: "Each of the agencies have 10, 20, 30 brands as customers. And so in effect, I'm getting 30 brands onto the platform by going through one agency."
  vi: "Mỗi agency có 10, 20, 30 brand làm khách; bán qua một agency là đưa được 30 brand lên nền tảng."
- ts: "08:19"
  who: Zach
  stage: find-idea
  theme: []
  text: "is there an agency layer here that I could do this with?"
  vi: "Hãy xem trong ngành mình đang làm có một lớp agency nào mà mình có thể làm sản phẩm cho họ không."
- ts: "09:20"
  who: Zach
  stage: mindset
  theme: []
  text: "The path to finding like the business that really works is never linear."
  vi: "Con đường tìm ra việc kinh doanh thực sự chạy không bao giờ thẳng."
- ts: "09:51"
  who: Zach
  stage: mindset
  theme: [learn-from-others]
  text: "But through the newsletter business, we learned email marketing. And then through email marketing, we built the agency."
  vi: "Qua việc làm newsletter, họ học được email marketing; từ email marketing mới làm được agency."
- ts: "10:06"
  who: Zach
  stage: mindset
  theme: [persistence]
  text: "You never know which one might be super relevant to the business that finally takes off a decade later."
  vi: "Không bao giờ biết kinh nghiệm nào sẽ hữu ích cho việc kinh doanh cuối cùng thành công, có khi sau cả thập kỷ."
rules:
- ts: "11:06"
  who: Gus
  stage: find-idea
  theme: []
  text: "Go to chat GPT right now or claude and ask it, hey, I learned about this business model."
  vi: "Hỏi ChatGPT hoặc Claude: tôi vừa học mô hình kinh doanh này, hãy chỉ ra nơi tôi có thể áp dụng vào các lớp agency khác."
  evidence: opinion
- ts: "12:58"
  who: Pat Walls
  stage: find-idea
  theme: []
  text: "focus on unsexy niches, especially if you're doing something in B2B like this."
  vi: "Muốn kiếm tiền thật, hãy chọn ngách không hấp dẫn, nhất là B2B như ví dụ này."
  evidence: opinion
numbers:
- ts: "02:05"
  metric: "MRR hiện tại (Stripe 4 tuần gần nhất)"
  value: 96200
  unit: usd
  evidence: measured
- ts: "02:05"
  metric: "MRR tăng thêm mỗi tháng (ước tính của founder)"
  value: 10000
  unit: usd
  evidence: claimed
- ts: "00:00"
  metric: "ARR đã đạt trong 19 tháng (lời founder)"
  value: 1000000
  unit: usd
  evidence: claimed
- ts: "02:36"
  metric: "giá tháng của agency có 10 client"
  value: 500
  unit: usd
  evidence: claimed
frameworks: []
idea_patterns: []
---

## Một câu

Hero Analytics: dashboard báo cáo cho agency email/SMS marketing, bán theo số client và seat, đạt khoảng $96k MRR sau 19 tháng; ý tưởng đến từ 6 năm tự vận hành agency.

## Bài học cho tôi

- Chọn khách là agency (mỗi agency kéo được 10–30 brand): một lần bán mở được nhiều người dùng (`05:28`).
- Ý tưởng đến từ nỗi đau khi tự làm nghề (agency, ~30 client), không phải từ xu hướng (`03:06`).

## Đừng tin vội

- Founder có nền 10 năm (data, Amazon, ETL, agency) và đồng sáng lập; lợi thế này không sao chép được cho người mới.
- Chỉ kể case đang chạy tốt; không có số khách rời, CAC, số agency đã thử và bỏ, hay tỉ lệ chốt trial.
- Video không nói khách đầu tiên đến từ đâu, và không nói agency có tự làm được không. Phụ thuộc vào nền tảng (Shopify, Claio) có thể đổi điều khoản; video không bàn.
- Dữ liệu MRR là màn hình founder đưa ra, chưa có kiểm chứng độc lập; "churn thấp nhất" là lời host.
