---
schema: 2
video_id: TUN8Y8__QGU
channel: starter-story
title: "I was stuck at $100 for 2 years until I made one change. Now my app makes $10K/month"
date: 2026-09-02
url: https://www.youtube.com/watch?v=TUN8Y8__QGU
transcript: starter-story-kb/videos/2026-09-02_i-was-stuck-at-100-for-2-years-until-i-made-one-chan/transcript.md
kind: founder_case
speakers:
  - {name: Piotr, role: founder}
  - {name: Pat Walls, role: host}
  - {name: Gus, role: host}
bias: "Starter Story (đối tác HubSpot) quảng bá database 50+ AI wrapper miễn phí ở giữa và cuối video (`05:17`, `12:54`). Piotr tự báo số liệu; doanh thu 10k gộp cả thanh toán một lần."
analyzed: 2026-11-15
cases:
  - id: visualizee
    depth: full
    product: "Visualizee (visualizee.ai): AI render cho kiến trúc sư và nhà thiết kế nội thất"
    what: "Upload phác thảo hoặc mô hình, chọn phong cách, AI ra ảnh/video render thực tế để trình bày khách; có trợ lý chat 'Vizi' hỏi để hiểu ý khách"
    type: [web-app]
    customer: "Kiến trúc sư và nhà thiết kế nội thất trình bày ý tưởng cho khách"
    founder:
      who: Piotr
      base: "Ba Lan"
      technical: true
      team: solo
      background: "Hơn 20 năm làm software developer; tech lead ở một software house Ba Lan, làm app ngoài giờ"
    revenue:
      amount: 10000
      unit: usd
      basis: monthly
      note: "MRR hiện tại 8,2k; cộng thanh toán một lần thì gần 10k/tháng. Founder đọc số từ dashboard."
      q: "but the combining with one-time payments, we are close to 10,000 per month"
      ts: "02:29"
      evidence: measured
    pricing: "Trial 7 ngày miễn phí; sau đó $35/tháng hoặc $80/tháng tuỳ số lượt render"
    idea_origin: [timing_trigger, niche_down]
    community_at_discovery: null
    demand_signal:
      kind: built_first
      level: 0
      what: "Làm V1 khoảng 5 tháng ngoài giờ rồi mới nhận phản hồi người dùng"
      q: "The first version took approximately 5 months after hours"
      ts: "04:09"
    prior_failures:
      count: 1
      what: "V1 (giao diện node kiểu ComfyUI) bị người dùng chê quá khó; trước đó hai năm dậm chân ở ~$100/tháng"
      q: "Okay, it's too hard to understand for us."
      ts: "04:09"
    unfair_advantage:
      - {value: technical_skill, what: "Software developer hơn 20 năm, tự build sản phẩm", q: "I'm a software developer with over 20 years of experience", ts: "03:18"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 36, value: "gần 3 năm từ lúc ra mắt", q: "I launched almost 3 years ago", ts: "01:08"}
    first_users: []
    build:
      time: "khoảng 5 tháng ngoài giờ cho V1"
      cut: ["Giao diện node kiểu ComfyUI (đổi sang chat trợ lý AI)", "Thanh toán một lần (đổi sang đăng ký hàng tháng)"]
      q: "The first version took approximately 5 months after hours"
      ts: "04:09"
steps:
  - stage: find-idea
    ts: "03:35"
    case: visualizee
    what: "Ý tưởng đến khi AI tạo ảnh bắt đầu nổi; chọn ngách kiến trúc sư và nhà thiết kế nội thất thay vì một AI toy chung chung."
    tactic: s9-niche-narrowing
  - stage: build
    ts: "04:09"
    case: visualizee
    what: "V1 kiểu node (giống ComfyUI) làm khoảng 5 tháng ngoài giờ; người dùng chê khó hiểu nên đổi sang chat trợ lý AI giúp viết prompt."
  - stage: monetize
    ts: "03:01"
    case: visualizee
    what: "Trial 7 ngày miễn phí, sau đó $35 hoặc $80 mỗi tháng tuỳ số lượt render."
    tactic: g4-pricing-paywall
    threshold: "$35 hoặc $80/tháng"
  - stage: monetize
    ts: "07:33"
    case: visualizee
    what: "Đổi từ thanh toán một lần sang thuê bao hàng tháng vì thanh toán một lần không tạo doanh thu lặp lại; sau đó doanh thu tăng."
    tactic: g4-pricing-paywall
    tactic_note: "Chuyển one-time sang subscription"
  - stage: grow
    ts: "03:01"
    case: visualizee
    what: "Đo phễu: landing page ~300 lượt xem mỗi ngày, 5–10 trial mới mỗi ngày, khoảng 25% chuyển sang trả tiền."
    tactic: g8-funnel-measurement
quotes:
  - ts: "06:58"
    who: Piotr
    stage: mindset
    theme: [builder-trap, stuck-on-one-thing]
    text: "I think I stick too long that my idea was great and that was hard for me to pivot earlier."
    vi: "Tôi giữ quá lâu niềm tin rằng ý tưởng của mình tuyệt, nên rất khó để đổi hướng sớm hơn."
  - ts: "07:16"
    who: Piotr
    stage: mindset
    theme: [clarity]
    text: "The data always said the truth."
    vi: "Dữ liệu luôn nói sự thật."
  - ts: "08:05"
    who: Piotr
    stage: mindset
    theme: []
    text: "friction in your product is killing your conversion."
    vi: "Ma sát trong sản phẩm đang giết chết tỉ lệ chuyển đổi của bạn."
  - ts: "08:24"
    who: Piotr
    stage: monetize
    theme: [revenue-first]
    text: "Subscriptions are the thing that drive the growth. You need to start charging from day one, and don't be afraid that someone will not pay."
    vi: "Thuê bao là thứ thúc đẩy tăng trưởng. Hãy thu tiền ngay từ ngày đầu và đừng sợ có người không trả."
  - ts: "08:41"
    who: Piotr
    stage: mindset
    theme: [persistence]
    text: "One, this is my first product ever released. So, it was really hard for me to you know, just remove it from the internet."
    vi: "Thứ nhất, đây là sản phẩm đầu tiên tôi phát hành, nên rất khó để gỡ nó khỏi internet."
  - ts: "10:04"
    who: Piotr
    stage: build
    theme: [clarity]
    text: "Don't build the most powerful product you can. Build the simplest product your customer needs."
    vi: "Đừng làm sản phẩm mạnh nhất có thể. Hãy làm sản phẩm đơn giản nhất mà khách hàng cần."
rules:
  - ts: "12:02"
    who: Gus
    stage: mindset
    theme: [persistence]
    text: "sort of stayed in it, he was able to like slowly pivot his way to the right path."
    vi: "Vì anh ấy kiên trì ở lại, anh ấy có thể từ từ đổi hướng đến con đường đúng."
    evidence: opinion
  - ts: "12:20"
    who: "Pat Walls hoặc Gus"
    stage: mindset
    theme: []
    text: "I don't think willpower will ever work."
    vi: "Tôi không nghĩ ý chí đơn thuần sẽ có tác dụng."
    evidence: opinion
numbers:
  - {ts: "00:00", metric: "MRR bị kẹt ở mức này trong 2 năm đầu", value: 100, unit: usd_per_month, evidence: claimed}
  - {ts: "02:12", metric: "MRR hiện tại (dashboard)", value: 8200, unit: usd_per_month, evidence: measured}
  - {ts: "02:29", metric: "doanh thu gần 10k/tháng (MRR cộng thanh toán một lần)", value: 10000, unit: usd_per_month, evidence: measured}
  - {ts: "03:01", metric: "thuê bao đang hoạt động", value: 300, unit: count, evidence: claimed}
  - {ts: "03:01", metric: "tỉ lệ trial chuyển sang trả tiền", value: 25, unit: percent, evidence: claimed}
  - {ts: "04:09", metric: "thời gian làm V1 (ngoài giờ)", value: 5, unit: months, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Piotr, tech lead có việc full-time ở Ba Lan, làm Visualizee (AI render cho kiến trúc sư và nhà thiết kế) và dậm chân ở ~$100/tháng hai năm; khi đổi từ giao diện node sang chat trợ lý AI và thu thuê bao hàng tháng, doanh thu lên gần 10k/tháng.

## Bài học cho tôi

- Người dùng chê V1 quá khó; đơn giản hoá sản phẩm (chat thay node) là thứ đưa doanh thu lên (`04:09`, `07:33`).
- Thu thuê bao ngay từ đầu, không chỉ bán một lần (`08:24`).

## Đừng tin vội

- Piotr là tech lead có việc full-time và làm app ngoài giờ trong gần 3 năm; ta không có điều kiện đó thì không sao chép đúng được (`01:08`, `03:18`).
- Doanh thu "gần 10k" gồm cả thanh toán một lần; MRR thuần là 8,2k (`02:12`, `02:29`).
- Video không nêu kênh tìm khách, chi phí GPU/API, hay tỉ lệ rời bỏ; con số 25% trial→trả và 300 thuê bao là tự báo.
- Gus khen sản phẩm trong phần kết (`10:37`), nhưng đó là cảm nhận của host, không phải dữ liệu.
