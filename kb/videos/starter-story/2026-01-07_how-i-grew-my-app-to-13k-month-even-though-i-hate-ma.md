---
schema: 2
video_id: Adl5_lJfkEE
channel: starter-story
title: "How I Grew My App to $13K/month (Even Though I Hate Marketing)"
date: 2026-01-07
url: https://www.youtube.com/watch?v=Adl5_lJfkEE
transcript: "starter-story-kb/videos/2026-01-07_how-i-grew-my-app-to-13k-month-even-though-i-hate-ma/transcript.md"
kind: founder_case
speakers: [{name: "Banu", role: founder}, {name: "Pat Walls", role: host}]
bias: "Starter Story bán Starter Story Build (bootcamp) và có mã giảm giá riêng cho Banu (`07:14`). Banu quảng bá SiteGPT; con số 13K MRR và 1 triệu lượt truy cập là lời founder kể."
analyzed: 2026-11-15
cases:
  - id: sitegpt
    depth: full
    product: "SiteGPT: chatbot AI đặt trên website, trả lời theo nội dung của chủ website"
    what: "Chatbot AI cho website; khách trả phí theo tháng theo số chatbot, lượng nội dung và số tin nhắn"
    type: [web-app]
    customer: "Doanh nghiệp có website muốn chatbot trả lời theo nội dung của họ (khoảng 130 khách)"
    founder: {who: "Banu", base: "Ấn Độ", technical: true, team: "solo (host nói 'solo dev')", background: "Software engineer sau đại học; nghỉ việc ở một startup lớn sau 8 tháng; trước đó làm Feather rồi bán $250.000"}
    revenue: {amount: 13000, unit: usd, basis: mrr, note: "Khoảng 130 khách x khoảng $100/tháng", q: "grew the other one, SiteGPT, to 13,000 MRR", ts: "01:17", evidence: claimed}
    pricing: "Theo tháng, tính theo số chatbot, lượng nội dung và số tin nhắn; ARPU khoảng $100; LTV khoảng $1.700–1.800"
    idea_origin: [adjacent_expansion, timing_trigger]
    scale_channels: [seo]
    community_at_discovery: {value: "Đang làm Feather với 100 khách; thấy các công cụ AI mới xuất hiện trên Twitter", insider: false, q: "Okay, I have 100 Feather customers", ts: "04:38"}
    demand_signal: null
    prior_failures: null
    unfair_advantage:
      - {value: technical_skill, what: "Software engineer, tự build sản phẩm", q: "I was a software engineer", ts: "03:50"}
      - {value: prior_success, what: "Đã bán SaaS trước đó (Feather) $250.000", q: "I sold my previous SaaS product, Feather, for $250,000", ts: "05:11"}
      - {value: existing_audience, what: "100 khách của Feather có sẵn để làm sản phẩm mới", q: "Okay, I have 100 Feather customers", ts: "04:38"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: {months: 1, value: "trong tháng đầu sau khi ra mắt", q: "It got to like 10,000 MRR within the first month itself", ts: "04:55"}
      to_current: null
    first_users:
      - {channel: seo, what: "Gần 50 free tool trên Google: khoảng 50.000 click/tháng, gần 90% đến từ tool, khoảng 300 lead; video không nói 10 người dùng đầu tiên", q: "we get around 50,000 clicks from Google every month and almost 90% of it is because of these", ts: "05:56"}
    build: {time: "khoảng 2 tuần từ ý tưởng đến lúc launch", cut: [], q: "I took two weeks from an idea to get it to launch", ts: "04:55"}
steps:
  - stage: find-idea
    ts: "04:22"
    case: sitegpt
    what: "Thấy các công cụ AI mới liên tục xuất hiện trên Twitter; dựng thử chatbot để học AI."
    tactic: s12-timing-shift
    tactic_note: "Khả năng AI mới là thay đổi vừa xảy ra"
  - stage: find-idea
    ts: "04:38"
    case: sitegpt
    what: "Từ 100 khách của Feather, xây chatbot trả lời nội dung blog; rồi nhận ra nên mở cho mọi người."
    tactic: s9-niche-narrowing
    tactic_note: "Mở từ khách Feather sang mọi chủ blog (ngách kề của sản phẩm đang chạy)"
  - stage: grow
    ts: "05:41"
    case: sitegpt
    what: "Xây gần 50 free tool, mỗi tool gắn một từ khoá và liên quan tới sản phẩm chính."
    tactic: g2-aso-seo-organic
    tactic_note: "Free tool làm SEO (free tools marketing)"
  - stage: find-idea
    ts: "08:32"
    case: sitegpt
    what: "Tìm từ khoá bằng Ahrefs Keywords Explorer: để trống từ khoá gốc rồi lọc theo từ chứa 'AI' và 'generator'."
    tactic: s2-google-trends-volume
    tool: "Ahrefs Keywords Explorer"
    tactic_note: "Lọc keyword rồi chọn tool để xây"
  - stage: find-idea
    ts: "09:21"
    case: sitegpt
    what: "Lọc keyword có độ khó dưới 10 để chọn từ khoá dễ xếp hạng."
    tactic: s2-google-trends-volume
    tool: "Ahrefs Keywords Explorer"
    threshold: "KD < 10"
  - stage: find-idea
    ts: "09:53"
    case: sitegpt
    what: "Lọc thêm volume tìm kiếm tối thiểu 1.000 mỗi tháng."
    tactic: s2-google-trends-volume
    tool: "Ahrefs Keywords Explorer"
    threshold: "volume >= 1.000/tháng"
  - stage: find-idea
    ts: "11:13"
    case: sitegpt
    what: "Lập bảng ưu tiên: volume, độ khó, công sức build và mức liên quan tới sản phẩm chính."
    tactic: s2-google-trends-volume
    tactic_note: "Bảng ưu tiên theo volume, KD, công sức build và mức liên quan"
  - stage: grow
    ts: "10:42"
    case: sitegpt
    what: "Dưới mỗi free tool thêm một CTA dẫn về sản phẩm chính (ví dụ tool chat-with-PDF dẫn tới SiteGPT)."
    tactic: g2-aso-seo-organic
    tactic_note: "CTA trong tool miễn phí dẫn về sản phẩm chính"
quotes:
  - {ts: "05:11", who: "Banu", stage: mindset, theme: [focus-one-thing], text: 'sell this to like someone who is actually capable of making it better." So, I sold my previous SaaS product, Feather, for $250,000.', vi: "Vì không còn thời gian làm sản phẩm cũ, tôi bán Feather cho người làm tốt hơn để tập trung SiteGPT."}
  - {ts: "04:22", who: "Banu", stage: find-idea, theme: [], text: "The best way for me to learn is to build something with it.", vi: "Cách học tốt nhất của tôi là tự làm một thứ với nó."}
  - {ts: "12:48", who: "Banu", stage: launch, theme: [ship-ugly], text: "not spend months and months on launching something. I would say just launch with a very core feature of your product. And then let users' feedback guide you to figure out how the product should go forward.", vi: "Đừng mất nhiều tháng để ra mắt; ra mắt với một tính năng lõi rồi để phản hồi người dùng dẫn hướng sản phẩm."}
rules:
  - {ts: "13:34", who: "Pat Walls", stage: mindset, theme: [builder-trap], text: "If you hate marketing and you suck at marketing, it's going to be a long road to get good at it. Why not just do the thing that you're already good at, which is building stuff and finding a way to market that way?", vi: "Nếu ghét và kém marketing thì sẽ là con đường dài; sao không làm điều mình giỏi là build rồi tìm cách marketing bằng chính điều đó?", evidence: opinion}
numbers:
  - {ts: "01:49", metric: "lượt truy cập website từ khi ra mắt", value: 1000000, unit: count, evidence: claimed}
  - {ts: "02:50", metric: "khách truy cập website/tháng", value: 50000, unit: count, evidence: claimed}
  - {ts: "03:05", metric: "số khách trả tiền (business)", value: 130, unit: count, evidence: claimed}
  - {ts: "03:20", metric: "LTV khách (USD, ước tính của founder)", value: 1750, unit: usd, evidence: claimed}
  - {ts: "05:56", metric: "click từ Google/tháng (gần 90% từ free tool)", value: 50000, unit: count, evidence: claimed}
  - {ts: "06:12", metric: "lead/tháng chủ yếu từ Google", value: 300, unit: count, evidence: claimed}
frameworks: [free-tools-seo]
idea_patterns: [adjacent-platform-expansion]
---

## Một câu

Banu (SiteGPT, chatbot AI cho website) đạt khoảng $13K MRR bằng gần 50 free tool SEO trên Google, không chi quảng cáo; ý tưởng mở rộng từ 100 khách Feather khi làn sóng AI mới xuất hiện.

## Bài học cho tôi

- Chọn từ khoá bằng Ahrefs (KD dưới 10, volume từ 1.000/tháng), xây free tool cho từ khoá đó, và dưới mỗi tool đặt một CTA về sản phẩm chính (`09:21`, `10:42`).
- Bắt đầu từ khách sẵn có (100 khách Feather) và dựng thử thứ mới với công nghệ mới để học, rồi mới mở rộng (`04:22`, `04:38`).

## Đừng tin vội

- Điều kiện riêng khó chép: software engineer và đã bán một SaaS $250.000 trước đó, có 100 khách sẵn (`03:50`, `05:11`).
- Doanh thu $13K MRR và 130 khách là lời founder; host nhắc tới analytics (`02:20`), nhưng doanh thu không được đọc từ dashboard theo yêu cầu của host.
- Video không nói: 10 người dùng đầu tiên, chi phí, thời gian làm free tool, và tỉ lệ click từ tool sang trả tiền.
- Video là phễu của Starter Story Build, có mã giảm giá riêng cho Banu (`07:14`).
