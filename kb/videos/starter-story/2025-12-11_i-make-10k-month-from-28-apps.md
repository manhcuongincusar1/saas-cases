---
schema: 2
video_id: vw2Yc4Y1PsU
channel: starter-story
title: "I make $10K/month from 28 apps"
date: 2025-12-11
url: https://www.youtube.com/watch?v=vw2Yc4Y1PsU
transcript: starter-story-kb/videos/2025-12-11_i-make-10k-month-from-28-apps/transcript.md
kind: founder_case
speakers:
  - {name: "Max", role: founder}
  - {name: "Pat Walls", role: host}
bias: "Starter Story bán Starter Story Build (boot camp, có mã giảm giá 20%); The Hustle tài trợ video. Max được chọn làm câu chuyện mẫu. Số liệu là lời Max."
analyzed: 2026-11-15
cases:
  - id: 28-apps-portfolio
    depth: full
    product: "Danh mục 28 app iOS nhỏ (portfolio), mỗi app một tính năng chính"
    what: "Ship nhiều app đơn giản: tìm từ khoá ASO, ghép màn hình/onboarding/paywall từ app cũ, nộp App Store trong vài giờ đến vài ngày"
    type: [mobile-app]
    customer: "Người dùng App Store tìm theo từ khoá (ví dụ nhận diện cây, học tập)"
    founder: {who: "Max", base: null, technical: true, team: "không nêu (làm ngoài giờ)", background: "Kỹ sư iOS khoảng 8 năm, làm full-time ở công việc chính; app làm ngoài giờ"}
    revenue: {amount: 10000, unit: usd, basis: monthly, note: "Lời Max, tổng 28 app. Phần lớn từ 4 app (mỗi app ~1.500); không có dashboard", q: "I've built a portfolio of 28 simple mobile apps that are now bringing me $10,000 monthly revenue.", ts: "01:21", evidence: claimed}
    pricing: null
    idea_origin: [revenue_scouting, adjacent_expansion]
    scale_channels: [app_store_search, paid_unspecified]
    community_at_discovery: {value: "Kỹ sư iOS có app pet project chưa lên; học chiến lược nhiều app nhỏ từ video YouTube của Adam", insider: true, q: "that literally changed my entire understanding of how to build apps.", ts: "02:24"}
    demand_signal: null
    prior_failures: {count: 1, what: "App pet (mobile) nhiều năm, thử nhiều kỹ thuật, không lên", q: "Nothing worked out.", ts: "02:09"}
    unfair_advantage:
      - {value: technical_skill, what: "Kỹ sư iOS khoảng 8 năm", q: "I started my career in software engineering as an iOS developer.", ts: "01:53"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: {months: 8, value: "8 tháng (làm ngoài giờ) để tới ~10k/tháng", q: "During my off work hours in 8 month time, I've built a portfolio of 28 simple mobile apps that are now bringing me $10,000 monthly revenue.", ts: "01:21"}
      to_current: {months: 8, value: "8 tháng (làm ngoài giờ) tới ~10k/tháng", q: "During my off work hours in 8 month time", ts: "01:21"}
    first_users:
      - {channel: app_store_search, what: "Boost App Store ngay sau khi ra mắt rồi giảm dần (lời Max). Video không nói 10 người dùng đầu", q: "when you just ship the app you get this famous app store boost", ts: "10:14"}
    build: {time: "kỷ lục 2 giờ từ ý tưởng tới khi nộp review; app khác có thể mất cả tuần", cut: [], q: "I have a record one app I've built like in two hours", ts: "07:35"}
steps:
  - {stage: find-idea, ts: "03:10", case: 28-apps-portfolio, what: "Dùng Astro (công cụ ASO) tìm từ khoá trong danh mục mình muốn làm, lấy các từ khoá liên quan cùng nhóm người dùng.", tactic: s2-aso-keyword-gap, tool: "Astro", threshold: "độ phổ biến ≥20%, độ khó 60–70 (lời Max)"}
  - {stage: find-idea, ts: "03:57", case: 28-apps-portfolio, what: "Với từ khoá thú vị, xem doanh thu tháng của đối thủ (Sensor Tower hoặc công cụ tương tự); bỏ qua nếu đối thủ dưới ~100 USD/tháng.", tactic: s1-revenue-spy, tool: "Sensor Tower", threshold: ">=100 USD/tháng (hoặc €200)"}
  - {stage: build, ts: "06:19", case: 28-apps-portfolio, what: "Nghiên cứu 2–3 đối thủ, chỉ lấy một tính năng chính liên quan từ khoá và bỏ qua phần còn lại; nhờ ChatGPT hoặc Gemini viết kế hoạch triển khai."}
  - {stage: build, ts: "06:49", case: 28-apps-portfolio, what: "Ghép app từ project có sẵn: kéo thả màn hình, nút, onboarding, paywall; có app copy khoảng 90% code."}
  - {stage: grow, ts: "07:20", case: 28-apps-portfolio, what: "Viết mô tả app và metadata bằng AI, bám theo từ khoá đã chọn từ đầu.", tactic: g2-aso-seo-organic}
  - {stage: launch, ts: "10:14", case: 28-apps-portfolio, what: "Nộp app ngay khi dùng được, rồi để thứ hạng App Store cho biết app nào không chìm và đáng đi tiếp.", tactic: other, tactic_note: "Ship MVP rồi đọc thứ hạng organic theo thời gian; không chờ nhu cầu được xác nhận trước khi build"}
  - {stage: grow, ts: "10:29", case: 28-apps-portfolio, what: "Quay lại app có organic: polish, sửa lỗi rồi chạy ads để nhân kết quả.", tactic: g6-paid-ads, tactic_note: "Chạy ads trên app đã có organic; nền tảng ads không nêu"}
quotes:
  - {ts: "02:24", who: "Max", stage: mindset, theme: [many-bets], text: "The old understanding was you have your one project, you have to grow it and just focus all your effort, all your time into it.", vi: "Cách hiểu cũ là có một dự án, phải lớn nó lên, dồn hết công sức và thời gian vào đó."}
  - {ts: "02:39", who: "Max", stage: mindset, theme: [many-bets], text: "You create one app, one feature, ship it, forget about it, and jump onto another app.", vi: "Tạo một app, một tính năng, ship, rồi bỏ và nhảy sang app khác."}
  - {ts: "12:32", who: "Max", stage: mindset, theme: [ship-ugly], text: "The most important advice would be not to be afraid of shipping. Don't waste your time on polishing it up, thinking about adding one more killer feature that would definitely get you a ton of users.", vi: "Lời khuyên quan trọng nhất: đừng sợ ship. Đừng mất thời gian đánh bóng hay thêm một tính năng 'giết' để có nhiều người dùng."}
rules:
  - {ts: "13:20", who: "Pat Walls", stage: mindset, theme: [many-bets], text: "build stuff fast, reuse different components, and just try a lot of different things. Building that shipping muscle is super, super important.", vi: "Phải build nhanh, tái dùng thành phần, thử nhiều thứ. Cơ bắp ship là thứ rất quan trọng.", evidence: opinion}
numbers:
  - {ts: "01:21", metric: "doanh thu/tháng cả portfolio (lời Max)", value: 10000, unit: usd_per_month, evidence: claimed}
  - {ts: "01:38", metric: "tổng số subscriber các app (lời Max)", value: 1000, unit: count, evidence: claimed}
  - {ts: "01:38", metric: "doanh thu mỗi app trong 4 app lớn nhất (lời Max, khoảng)", value: 1500, unit: usd_per_month, evidence: claimed}
  - {ts: "03:57", metric: "ngưỡng doanh thu đối thủ tối thiểu để chọn ngách (benchmark của Max)", value: 100, unit: usd_per_month, evidence: claimed}
  - {ts: "07:35", metric: "thời gian ship app nhanh nhất (ý tưởng tới nộp review)", value: 2, unit: hours, evidence: claimed}
frameworks: [many-small-bets, one-feature-per-app]
idea_patterns: [adjacent-platform-expansion]
---
## Một câu

Max (kỹ sư iOS làm app ngoài giờ) ship 28 app nhỏ trong 8 tháng. Anh chọn từ khoá ASO có người tìm, kiểm doanh thu đối thủ, mỗi app một tính năng chính. Tổng khoảng 10k/tháng, phần lớn từ 4 app.

## Bài học cho tôi

- Chọn ý tưởng từ từ khoá ASO và kiểm doanh thu đối thủ trước khi build (`03:10`, `03:57`).
- Ship nhanh một tính năng, để thứ hạng App Store cho biết app nào đáng đầu tư. Chỉ chạy ads cho app đã có organic (`10:14`, `10:29`).

## Đừng tin vội

- Số liệu là lời Max, không có dashboard. 10k là tổng 28 app và phần lớn đến từ 4 app. Video không nói bao nhiêu app không có doanh thu.
- Video chỉ kể app thành công. Không có số app bỏ hoặc thất bại trong 28 app.
- Ngưỡng từ khoá trong transcript mâu thuẫn: độ khó '60 hoặc 70', rồi '70', rồi 'very low' cho từ khoá tốt. Không chắc ngưỡng đúng.
- Điều kiện riêng: 8 năm làm iOS và làm app trong vài giờ. Người không biết code khó lặp lại tốc độ này.
- Video không nói giá app, cách marketing ngoài ASO và ads, hay cách kiểm nhu cầu trước khi build.
- Có tài trợ The Hustle (`04:28`) và quảng cáo Starter Story Build kèm mã giảm giá (`08:23`).
