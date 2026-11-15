---
schema: 2
video_id: EF3uyvHHBfM
channel: starter-story
title: "I make $40K/month with this one website"
date: 2025-07-20
url: https://www.youtube.com/watch?v=EF3uyvHHBfM
transcript: starter-story-kb/videos/2025-07-20_i-make-40k-month-with-this-one-website/transcript.md
kind: founder_case
speakers: [{name: Angus Cheng, role: founder}, {name: Pat Walls, role: host}]
bias: "Video có đoạn tài trợ Brex (ngân hàng cho startup) và quảng bá Starter Story Build. Số liệu là Angus tự báo, không có dashboard."
analyzed: 2026-11-15
cases:
  - id: bank-statement-converter
    depth: full
    product: "Bank Statement Converter (đổi sao kê ngân hàng dạng PDF thành bảng giao dịch)"
    what: "Chuyển sao kê PDF của ngân hàng thành dữ liệu giao dịch, chỉ làm một việc"
    type: [web-app]
    customer: "Người muốn xem chi tiêu qua nhiều năm từ sao kê PDF; video không nói nhóm trả tiền nhiều nhất"
    founder: {who: Angus Cheng, base: "Hong Kong", technical: true, team: "solo (một người bạn làm cùng vài tuần đầu, sau đó rời)", background: "Lập trình viên; làm ngân hàng đầu tư ở Hong Kong 2017–2019, công ty crypto 2020"}
    revenue: {amount: 40000, unit: usd, basis: mrr, note: "Angus tự báo; không mở dashboard", q: "And today it's at 40,000 USD MR.", ts: "03:36", evidence: claimed}
    pricing: null
    idea_origin: [own_pain]
    scale_channels: []
    community_at_discovery: {value: "Chính Angus: vừa nghỉ việc, cần biết tiền trong ngân hàng dùng được bao lâu", insider: true, q: "I wanted multiple years of bank data", ts: "01:04"}
    demand_signal: {kind: built_first, level: 0, what: "Làm MVP khoảng một tuần, đưa lên mạng rồi mua Google Ads; người upload sao kê ngay sau đó", q: "me and a friend worked on it for about a week", ts: "01:34"}
    prior_failures: null
    unfair_advantage:
      - {value: technical_skill, what: "Angus là lập trình viên từ lâu, tự viết code để lấy dữ liệu từ sao kê", q: "I've always been a developer", ts: "07:45"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: paid_google, what: "Mua quảng cáo Google Search để người ta bấm vào domain mới; ngay sau đó có người upload sao kê", q: "we bought Google ads to get people to start clicking into", ts: "01:34"}
    build: {time: "khoảng một tuần cho MVP, làm cùng một người bạn", cut: [], q: "me and a friend worked on it for about a week", ts: "01:34"}
steps:
  - {stage: find-idea, ts: "01:04", case: bank-statement-converter, what: "Vừa nghỉ việc, cần sao kê nhiều năm dạng Excel để biết mình tiêu bao nhiêu; ngân hàng chỉ có PDF nên tự viết code tách giao dịch.", tactic: s5-insider, tactic_note: "Nỗi đau riêng: chính Angus cần dữ liệu từ sao kê"}
  - {stage: validate, ts: "01:34", case: bank-statement-converter, what: "Làm MVP khoảng một tuần rồi đưa lên production và cho người dùng thật dùng, không kiểm chứng nhu cầu trước khi build.", tactic: other, tactic_note: "MVP trong 1–2 tuần, đưa lên mạng ngay; Angus cho rằng rủi ro thấp nên không validate trước"}
  - {stage: launch, ts: "01:34", case: bank-statement-converter, what: "Mua quảng cáo Google Search đưa người vào domain mới ngay khi ra mắt.", tactic: g6-paid-ads, tool: "Google Ads", tactic_note: "Chạy quảng cáo từ ngày đầu, trước khi có organic"}
  - {stage: grow, ts: "04:07", case: bank-statement-converter, what: "Chạy Google Ads khoảng 6 tháng không có lời; một đợt khoảng 1.000 USD chi quảng cáo chỉ mang về khoảng 300 USD doanh thu; sau đó cắt quảng cáo.", tactic: g6-paid-ads, cost: "khoảng $1.000 chi quảng cáo (một đợt được nêu)", tactic_note: "Chi ads không hoà vốn, cắt sau khoảng 6 tháng"}
  - {stage: grow, ts: "04:23", case: bank-statement-converter, what: "Thử viết blog và build in public: nhiều lượt chú ý nhưng ít người dùng, vì khách không đọc blog hay Twitter.", tactic: g3-organic-content-formats}
  - {stage: grow, ts: "04:23", case: bank-statement-converter, what: "Gửi cold email trong 3 tháng: chỉ được 1 đơn, và nhiều người phản hồi giận dữ.", tactic: g1-first-10-users}
quotes:
  - {ts: "02:19", who: Angus Cheng, stage: validate, theme: [ship-ugly], text: "You can try to validate before launching, but if it takes you like one or two weeks to make an MVP, it's not that much of a risk anyway.", vi: "Bạn có thể kiểm chứng trước khi ra mắt, nhưng nếu làm MVP chỉ mất một hai tuần thì rủi ro không lớn."}
  - {ts: "03:05", who: Angus Cheng, stage: validate, theme: [], text: "Don't show it to your friends and family, you know, they will just lie to you and they're probably not going to buy your product anyway.", vi: "Đừng cho bạn bè và gia đình xem; họ sẽ nói dối và chắc chắn không mua sản phẩm."}
  - {ts: "03:21", who: Angus Cheng, stage: retain, theme: [], text: "If people are not using a certain feature, maybe don't continue working on it.", vi: "Nếu người ta không dùng một tính năng, có thể đừng làm tiếp nó."}
  - {ts: "04:39", who: Angus Cheng, stage: grow, theme: [], text: "After about 6 months of running Google search ads, I decided, you know, I'm just not going to do this anymore. I might not even do this app anymore.", vi: "Sau khoảng 6 tháng chạy quảng cáo Google, tôi quyết định thôi và có thể cả việc làm app này."}
  - {ts: "09:03", who: Angus Cheng, stage: mindset, theme: [persistence], text: "And what I realized was that those first two years of hard work, you don't get paid much, but you kind of get the money for that hard work in like years four and onwards.", vi: "Tôi nhận ra hai năm đầu làm việc chăm chỉ hầu như không được trả, nhưng tiền cho công sức đó đến từ năm thứ tư trở đi."}
  - {ts: "09:18", who: Angus Cheng, stage: mindset, theme: [], text: "SAS is an excellent business model. Make sure you save enough money to survive multiple years of no income.", vi: "SaaS là mô hình kinh doanh rất tốt; hãy tiết kiệm đủ tiền để sống nhiều năm không có thu nhập."}
rules:
  - {ts: "10:04", who: Pat Walls, stage: find-idea, theme: [], text: "He found a tiny problem, built a solution for himself, and then turned it into a life-changing business.", vi: "Anh ấy tìm một vấn đề nhỏ, tự làm giải pháp cho mình, rồi biến nó thành một việc kinh doanh đổi đời.", evidence: opinion}
numbers:
  - {ts: "03:36", metric: "MRR năm 2022 (USD)", value: 6000, unit: usd_mrr, evidence: claimed}
  - {ts: "03:51", metric: "tổng số người dùng", value: 75000, unit: count, evidence: claimed}
  - {ts: "03:51", metric: "lượt truy cập mỗi tháng", value: 40000, unit: count, evidence: claimed}
  - {ts: "04:55", metric: "đăng ký mới mỗi ngày sau khi cắt quảng cáo (kênh không nêu)", value: "2–3", unit: count_per_day, evidence: claimed}
  - {ts: "08:33", metric: "lợi nhuận trên doanh thu hàng tháng", value: "39.000 / 40.000 USD", unit: usd_per_month, evidence: claimed}
frameworks: [one-feature-per-app]
idea_patterns: [snap-and-get-result]
---

## Một câu

Angus Cheng làm Bank Statement Converter, một việc duy nhất là đổi sao kê PDF thành bảng giao dịch: làm MVP khoảng một tuần, chạy Google Ads không có lời, cắt quảng cáo, và tự báo 40.000 USD MRR khi làm một mình.

## Bài học cho tôi

- Bắt đầu từ nỗi đau riêng: Angus cần chính dữ liệu đó để biết mình tiêu bao nhiêu (`01:04`).
- Quảng cáo không có lời thì cắt; sau khi cắt vẫn có 2–3 đăng ký mỗi ngày, nhưng video không nói từ kênh nào (`04:55`).

## Đừng tin vội

- Số liệu (40.000 USD MRR, 75.000 người dùng, 40.000 lượt/tháng) là Angus tự báo, không có dashboard. Video không nói con số trả tiền, giá, hay churn.
- Video không nói kênh nào đưa người dùng organic sau khi cắt quảng cáo; vì vậy không ghi thành step.
- Angus có lợi thế là biết code (đã ghi ở unfair_advantage) và nói chính ngách này "chỉ đủ cho một người", VC sẽ không quan tâm; người không biết code phải thuê, video không bàn chi phí đó.
- Video có đoạn tài trợ Brex và quảng bá Starter Story Build.
