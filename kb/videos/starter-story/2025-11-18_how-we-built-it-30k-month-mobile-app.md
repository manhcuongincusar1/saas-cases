---
schema: 2
video_id: rCV-TVCnF6Q
channel: starter-story
title: "How We Built It: $30K/month Mobile App"
date: 2025-11-18
url: https://www.youtube.com/watch?v=rCV-TVCnF6Q
transcript: starter-story-kb/videos/2025-11-18_how-we-built-it-30k-month-mobile-app/transcript.md
kind: founder_case
speakers:
  - {name: Eyal Hazan, role: founder}
  - {name: Yahli Hazan, role: founder}
  - {name: Pat Walls, role: host}
bias: "Starter Story bán Starter Story Build và danh sách Black Friday VIP (CTA trong video); founder quảng bá Prop GPT, ứng dụng phân tích cá cược thể thao. Video có disclaimer không phải lời khuyên cờ bạc."
analyzed: 2026-11-15
cases:
  - id: prop-gpt
    depth: full
    product: "Prop GPT: app phân tích cá cược thể thao dùng mô hình ML để chọn kèo"
    what: "Người dùng xem các kèo đã được phân tích sẵn mỗi ngày, hoặc tự nhập cược để mô hình phân tích"
    type: [mobile-app]
    customer: "Người cá cược thể thao muốn được cho đáp án (founder: khách 'wanted to be given the right answers to the test')"
    founder: {who: "Eyal Hazan và Yahli Hazan", base: null, technical: null, team: "2 co-founder", background: "Tự nói hai sinh viên đại học; từng làm việc với nhiều founder app thành công trước đó"}
    revenue: {amount: 30000, unit: usd, basis: monthly, note: "Founder nói 'about $30,000 a month'; kèm 3.000+ khách trả tiền và 40.000 lượt tải (tự nói)", q: "We do about $30,000 a month", ts: "01:37", evidence: claimed}
    pricing: "Không nêu giá gói. Founder nói tỉ lệ download sang trial 48% và khoảng 3,30 USD doanh thu trên mỗi lượt tải"
    idea_origin: []
    scale_channels: [influencer_paid]
    community_at_discovery: null
    demand_signal: null
    prior_failures:
      count: 1
      what: "Bản đầu tải nhiều (~20 lượt/ngày) nhưng gần như không ai ở lại sau trial; kẹt ở 1–2k MRR, dừng marketing và làm lại 4 tháng"
      q: "Almost nobody stayed after the trial ended"
      ts: "00:00"
    unfair_advantage:
      - {value: network, what: "Trước đó đã làm việc với nhiều founder app thành công, có quan hệ với họ", q: "I had worked with other really successful app founders before", ts: "02:55"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 12, value: "khoảng một năm kể từ khi ra mắt", q: "We launched it around a year ago", ts: "01:04"}
    first_users:
      - {channel: influencer_paid, what: "Trả vài nghìn USD cho influencer ban đầu để đo số lượt tải trên mỗi USD; ~20 lượt tải và 5–10 lượt vào trial mỗi ngày. Video không nói 10 người dùng đầu cụ thể", q: "We started spending a few thousand dollars on influencer marketing", ts: "03:11"}
    build:
      time: "khoảng 5 tháng cho bản đầu tiên"
      cut: []
      q: "We spent like 5 months building the first version of Prop GPT"
      ts: "01:52"
steps:
  - stage: launch
    ts: "03:11"
    case: prop-gpt
    what: "Chạy influencer trả tiền vài nghìn USD để đo số lượt tải trên mỗi đồng chi"
    tactic: g7-creator-ops
    tactic_note: "Influencer trả tiền, đo tải theo chi phí"
  - stage: grow
    ts: "04:15"
    case: prop-gpt
    what: "Bật lại marketing đúng mùa NBA playoffs (sự kiện có sẵn), tỉ lệ chuyển sang trả tiền vượt 50%; không nêu kênh cụ thể"
    tactic: other
    tactic_note: "Đẩy marketing đúng mùa playoffs NBA (sự kiện có sẵn); video không nói kênh nào"
  - stage: retain
    ts: "03:58"
    case: prop-gpt
    what: "Dừng marketing, dành 4 tháng làm lại app bằng engineering và design theo điều khách thật sự muốn; ra bản mới 15/4 với ~1.700 USD MRR"
    tactic: g8-funnel-measurement
    tactic_note: "Quyết định làm lại sản phẩm từ số liệu phễu, không từ kênh"
  - stage: retain
    ts: "06:04"
    case: prop-gpt
    what: "Theo dõi analytics và trò chuyện với người dùng để tìm chỗ hành vi không khớp thiết kế (ví dụ nhiều người vào trial nhưng không ai ở lại)"
    tactic: g8-funnel-measurement
    tool: "PostHog"
    tactic_note: "Đọc phễu onboarding và hành vi người dùng bằng analytics"
  - stage: grow
    ts: "07:53"
    case: prop-gpt
    what: "Video organic thứ ~70 của họ đạt 600 nghìn view, ARR từ ~8k lên ~38k trong khoảng 3 ngày (tự nói)"
    tactic: g3-organic-content-formats
    tactic_note: "Video organic của chính founder bùng lên; không nêu quy trình"
quotes:
  - {ts: "03:58", who: "Eyal Hazan hoặc Yahli Hazan", stage: retain, theme: [clarity], text: "We realized that what our customers actually wanted was just to be given the right answers to the test", vi: "Chúng tôi nhận ra khách thật sự muốn được cho đáp án, không muốn tự vào nhà cái nhập cược."}
  - {ts: "05:48", who: "Eyal Hazan hoặc Yahli Hazan", stage: mindset, theme: [], text: "The most important thing is to have an extremely humble attitude about your product.", vi: "Điều quan trọng nhất là có thái độ khiêm tốn tuyệt đối về sản phẩm của mình."}
  - {ts: "06:04", who: "Eyal Hazan hoặc Yahli Hazan", stage: validate, theme: [], text: "Using analytics platforms like Posthog and simply talking to enough users, you see that there is a pattern of human behavior that doesn't align with how the app is designed.", vi: "Dùng công cụ analytics như Posthog và nói chuyện đủ với người dùng, bạn sẽ thấy hành vi không khớp với thiết kế."}
  - {ts: "09:29", who: "Eyal Hazan hoặc Yahli Hazan", stage: validate, theme: [sell-before-build], text: "be honest with yourself and scientific about whether what you're working on has enough demand", vi: "Thành thật với bản thân và khoa học: việc bạn đang làm có đủ nhu cầu không."}
  - {ts: "09:29", who: "Eyal Hazan hoặc Yahli Hazan", stage: mindset, theme: [], text: "have a co-founder who you will be able to lean on, and that will be able to lean on you when things get hard", vi: "Lời khuyên lớn nhất: có một co-founder để dựa vào, và họ cũng dựa vào bạn khi khó khăn."}
rules:
  - {ts: "10:15", who: "Pat Walls", stage: retain, theme: [], text: "you have to have both figured out if you actually want to build something that can last.", vi: "Phải làm chắc cả phân phối lẫn sản phẩm nếu muốn xây thứ bền.", evidence: opinion}
numbers:
  - {ts: "01:37", metric: "lượt tải", value: 40000, unit: count, evidence: claimed}
  - {ts: "01:37", metric: "khách trả tiền", value: 3000, unit: count, evidence: claimed}
  - {ts: "01:37", metric: "tỉ lệ download sang trial", value: 48, unit: percent, evidence: claimed}
  - {ts: "01:52", metric: "doanh thu trên mỗi lượt tải", value: 3.3, unit: usd, evidence: claimed}
  - {ts: "04:15", metric: "MRR khi ra bản làm lại (15/4)", value: 1700, unit: usd_per_month, evidence: claimed}
  - {ts: "04:31", metric: "đỉnh MRR sau ~2,5 tháng", value: 40000, unit: usd_per_month, evidence: claimed}
  - {ts: "07:05", metric: "tỉ lệ download sang trial (trước khi làm lại)", value: 45, unit: percent, evidence: claimed}
  - {ts: "07:05", metric: "tỉ lệ trial sang trả tiền (trước khi làm lại)", value: 13, unit: percent, evidence: claimed}
  - {ts: "07:53", metric: "lượt xem video organic thứ ~70", value: 600000, unit: views, evidence: claimed}
  - {ts: "07:53", metric: "ARR sau video đó (từ ~8k)", value: 38000, unit: usd, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Eyal và Yahli Hazan làm Prop GPT, app phân tích cá cược thể thao: bản đầu tải nhiều nhưng gần như không ai ở lại sau trial; họ dừng marketing 4 tháng để làm lại theo điều khách thật sự muốn và lên khoảng 30k/tháng (tự nói).

## Bài học cho tôi

- Đọc phễu trước khi đổ tiền: 45% vào được trial nhưng chỉ 13% trả tiền, nên vấn đề là sản phẩm chứ không phải kênh (`07:05`).
- Hỏi khách thật sự muốn gì: họ muốn có đáp án sẵn, không muốn tự nhập cược để kiểm tra (`03:58`).

## Đừng tin vội

- Số liệu tự nói. Video không nêu tổng chi phí influencer, không nêu 10 người dùng đầu từ đâu; câu "30k MRR trong 10 tuần" (host nói) tính từ lần làm lại, không tính từ ngày đầu.
- Ngành cá cược có rủi ro pháp lý và trách nhiệm với người dùng riêng; video có disclaimer. Lợi thế dữ liệu và mô hình không dễ sao chép.
- Video không nói ý tưởng đến từ đâu. Survivor bias: chỉ kể câu chuyện đã thành, không có số bản thất bại khác.
