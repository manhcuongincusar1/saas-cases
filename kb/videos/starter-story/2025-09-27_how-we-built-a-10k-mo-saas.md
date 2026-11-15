---
schema: 2
video_id: 3eY71OS4MFw
channel: starter-story
title: "How We Built a $10K/mo SaaS"
date: 2025-09-27
url: https://www.youtube.com/watch?v=3eY71OS4MFw
transcript: starter-story-kb/videos/2025-09-27_how-we-built-a-10k-mo-saas/transcript.md
kind: founder_case
speakers:
  - {name: Joseph, role: founder}
  - {name: Timo, role: founder}
  - {name: Pat Walls, role: host}
bias: "Kênh Starter Story có sponsor (Mobin) và quảng cáo chương trình Starter Story Build trong video; founder được lợi nếu người xem tin rằng landing page giả là cách làm an toàn."
analyzed: 2026-11-15
cases:
  - id: setter-ai
    depth: full
    product: "Setter AI: AI đặt lịch hẹn và sàng lọc lead cho doanh nghiệp B2B"
    what: "AI appointment setter: theo dõi và sàng lọc lead ngay lập tức, thay sales rep để đặt lịch"
    type: [web-app]
    customer: "Doanh nghiệp B2B giá trị cao: năng lượng mặt trời, coach, tài chính"
    founder: {who: "Joseph và Timo", base: "Timo sống ở Bangkok; video không nêu Joseph", technical: true, team: "2 co-founder", background: "Joseph từng freelance làm software engineer; Timo không nêu"}
    revenue: {amount: 10000, unit: usd, basis: mrr, note: "Khoảng 10K trong tháng gần nhất; lời founder, không mở dashboard", q: "Pretty much exactly 10K last month.", ts: "09:46", evidence: claimed}
    pricing: "Gói đăng ký từ khoảng $50/tháng; có khách trả khoảng $500, khách lớn nhất tới $5.000/tháng (lời founder)"
    idea_origin: null
    scale_channels: [seo, youtube_founder]
    community_at_discovery: null
    demand_signal: {kind: paid, level: 8, what: "Landing page giả với demo AI giả; trước khi có sản phẩm, một khách trả $500 qua Stripe", q: "When we got our first uh Stripe payment of $500", ts: "04:07"}
    prior_failures: {count: 1, what: "Nghỉ việc và dành cả năm build mà không có traction", q: "spent a whole year building without any traction", ts: "00:00"}
    unfair_advantage:
      - {value: cofounder, what: "Hai người cùng làm, gặp nhau ở coworking rồi cùng khởi nghiệp", q: "together we started Setai", ts: "01:02"}
      - {value: technical_skill, what: "Joseph từng làm freelance software engineer", q: "I quit freelancing as a software engineer to start indie hacking", ts: "00:46"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: seo, what: "Khách đầu tiên đến từ SEO và content (lời founder). Video không nói 10 người đầu tiên cụ thể", q: "that's where our first customers came from and that was SEO", ts: "08:43"}
    build: null
steps:
  - {stage: find-idea, ts: "03:04", case: setter-ai, what: "Tìm từ khoá có lượng tìm kiếm nhưng ít đối thủ bằng Ahrefs, rồi đặt làm H1 của landing page.", tactic: s2-google-trends-volume, tool: "Ahrefs (hrefs)"}
  - {stage: validate, ts: "01:47", case: setter-ai, what: "Dựng landing page dưới domain cũ đã được Google index, có H1 từ khoá, demo AI giả và nút đặt lịch, khi chưa có sản phẩm.", tactic: s8-content-demand-test, tactic_note: "Landing page về ý tưởng trước khi build; đo bằng xếp hạng Google và lượt đặt lịch"}
  - {stage: validate, ts: "04:07", case: setter-ai, what: "Nhận khoản thanh toán Stripe $500 khi sản phẩm chưa tồn tại.", tactic: s7-preorder-buy-button, tactic_note: "Đặt cọc hoàn lại 100% trước khi có sản phẩm (deposit framework)"}
  - {stage: launch, ts: "03:35", case: setter-ai, what: "Gửi yêu cầu index trang trong Google Search Console để Google index trong khoảng 24 giờ.", tactic: g2-aso-seo-organic}
  - {stage: grow, ts: "08:43", case: setter-ai, what: "Tăng trưởng hoàn toàn inbound qua SEO và content; website mới lên top 1 Google trong khoảng một tuần.", tactic: g2-aso-seo-organic}
  - {stage: grow, ts: "09:14", case: setter-ai, what: "Làm video YouTube dài; phần lớn khách chốt đã xem ít nhất một video trước khi đặt lịch.", tactic: g3-organic-content-formats}
  - {stage: monetize, ts: "01:17", case: setter-ai, what: "Gói đăng ký theo tháng từ khoảng $50/tháng; khách lớn nhất trả tới $5.000/tháng.", tactic: g4-pricing-paywall, cost: "từ khoảng $50/tháng"}
  - {stage: grow, ts: "11:20", case: setter-ai, what: "Thử chạy ads (không nêu nền tảng) và thuê freelancer; biên lợi nhuận giảm từ trên 90% xuống khoảng 80%.", tactic: g6-paid-ads, tactic_note: "Không nêu nền tảng ads (paid_unspecified)"}
quotes:
  - {ts: "01:47", who: "Joseph hoặc Timo", stage: validate, theme: [sell-before-build], text: "So, as soon as I had the idea, I set up a landing page.", vi: "Ngay khi có ý tưởng, tôi dựng landing page, vài tháng trước khi khởi nghiệp."}
  - {ts: "04:07", who: "Joseph hoặc Timo", stage: validate, theme: [sell-before-build], text: "I think the only way to validate is when buyers swipe their credit card.", vi: "Tôi nghĩ cách duy nhất để xác nhận là khi khách thật quẹt thẻ."}
  - {ts: "04:54", who: "Joseph hoặc Timo", stage: find-idea, theme: [], text: "I think the best pain point to find B2B ideas is not look around on Reddit or something because business owners, frankly, they don't really check Reddit.", vi: "Điểm đau tốt nhất để tìm ý tưởng B2B không phải là lướt Reddit, vì chủ doanh nghiệp thật ra không xem Reddit."}
  - {ts: "12:07", who: "Joseph hoặc Timo", stage: monetize, theme: [revenue-first], text: "charge because charging creates urgency and commitment not only from you but also your customer.", vi: "Hãy thu tiền, vì thu tiền tạo sự khẩn cấp và cam kết từ cả bạn lẫn khách."}
rules:
  - {ts: "06:26", who: "Pat Walls", stage: validate, theme: [sell-before-build], text: "Collecting cash before writing code is definitely the way to go, especially if you want to ship a successful app as a solo founder.", vi: "Thu tiền trước khi viết code là hướng đi đúng, nhất là khi muốn ra một app thành công với tư cách solo founder.", evidence: opinion}
numbers:
  - {ts: "09:46", metric: "tổng lượt đăng ký của doanh nghiệp", value: 2000, unit: count, evidence: claimed}
  - {ts: "10:01", metric: "khách trả tiền", value: 38, unit: count, evidence: claimed}
  - {ts: "11:20", metric: "biên lợi nhuận khi không chạy ads", value: "90+%", unit: percent, evidence: claimed}
frameworks: [sell-before-build, seo-landing-page]
idea_patterns: []
---

## Một câu

Landing page giả (từ khoá ít đối thủ, demo AI giả) lên Google và thu $500 qua Stripe trước khi có sản phẩm; SEO và YouTube đưa Setter AI lên khoảng 10K MRR với 38 khách trả tiền (lời founder).

## Bài học cho tôi

- Tín hiệu mức 8 là khi có người quẹt thẻ thật, không phải lượt xem: $500 qua Stripe trước khi có sản phẩm (`04:07`).
- Khách đầu tiên đến từ SEO và content, không từ kênh trả tiền; trang được Google index trong khoảng 24 giờ nhờ domain cũ (`08:43`, `03:35`).

## Đừng tin vội

- Founder dựng landing page trên domain cũ đã được Google index từ trước; founder khuyên dùng domain đã online từ trước, không phải domain mới; video không nói điều gì xảy ra nếu không có domain đó.
- Video không nói người trả $500 là ai, và không nêu thêm khách trả tiền nào trong giai đoạn đó.
- Video không nói thời gian build, 10 khách đầu tiên là ai, hay bao lâu để đạt 10K MRR; host nói "just over a year" nhưng founder không xác nhận.
- Số 2.000 lượt đăng ký, 38 khách trả tiền, 10K MRR đều là lời founder, không có dashboard. Starter Story có sponsor và bán chương trình Starter Story Build trong video.
