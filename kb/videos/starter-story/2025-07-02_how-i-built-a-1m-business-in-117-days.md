---
schema: 2
video_id: "E_sPvPHwpuk"
channel: starter-story
title: "How I Built A $1M Business in 117 Days"
date: 2025-07-02
url: "https://www.youtube.com/watch?v=E_sPvPHwpuk"
transcript: "starter-story-kb/videos/2025-07-02_how-i-built-a-1m-business-in-117-days/transcript.md"
kind: founder_case
speakers: [{name: "Yasser", role: founder}, {name: "Pat Walls", role: host}]
bias: "Starter Story có ad read Brex và quảng bá chương trình Starter Story Build (link mô tả). Câu chuyện thành công này bán chương trình; số ARR là lời founder, không có dashboard."
analyzed: 2026-11-15
cases:
  - id: chatbase
    depth: full
    product: "Chatbase (chat với tài liệu của bạn bằng AI)"
    what: "Tải tài liệu (ví dụ PDF) lên rồi chat với nó; bán gói đăng ký theo tháng qua nút Stripe trên web"
    type: [web-app]
    customer: "Người muốn chat với tài liệu của mình; khoảng 10.000 khách trả $40–$500 mỗi tháng (lời founder)"
    founder: {who: "Yasser", base: null, technical: null, team: "solo", background: "Thực tập ở công ty FAANG rồi thấy không hợp; làm Chatbase trong năm cuối đại học rồi bỏ học"}
    revenue: {amount: 6800000, unit: usd, basis: arr, note: "Lúc phỏng vấn. Đầu video nói 7 triệu ARR, không khớp; không có dashboard", q: "right now we're exactly at 6.8 million ARR", ts: "07:03", evidence: claimed}
    pricing: "Đăng ký theo tháng, từ $40 đến $500 (lời founder; video không nói gói năm)"
    idea_origin: [timing_trigger]
    scale_channels: [founder_led_content, reddit, influencer_paid]
    community_at_discovery: {value: "Theo dõi phong trào bootstrap và các demo AI trên X; video không nói nhóm khách cụ thể", insider: false, q: "So I followed the bootstrapping movement on X like Peter Levels", ts: "01:04"}
    demand_signal: {kind: built_first, level: 0, what: "Build xong rồi đưa cho 16 follower; không validate trước", q: "I didn't do any validation or anything.", ts: "01:35"}
    prior_failures: null
    unfair_advantage: []
    time_to_revenue: {first_dollar: null, to_1k_mrr: null, to_10k_mrr: null, to_current: {months: 30, value: "khoảng 2,5 năm từ lúc ra mắt", q: "I launched it 2 and a half years ago", ts: "00:48"}}
    first_users:
      - {channel: founder_led_content, what: "Tweet demo gửi tới 16 follower rồi lan truyền; video không nói 10 người dùng đầu đến từ đâu", q: "I released chatbase to my 16 followers. It went viral.", ts: "01:35"}
      - {channel: reddit, what: "Làm chatbot miễn phí cho từng cuốn sách rồi đăng vào subreddit sách để có lượt mở domain; chấp nhận lỗ tiền", q: "going into subreddits of books, I would create a chat GPT for their book", ts: "06:16"}
      - {channel: influencer_paid, what: "Sponsored post trả tiền qua một trang LinkedIn lớn, khoảng 4.000 USD một bài", q: "I think we did $4,000", ts: "06:46"}
    build: null
steps:
  - {stage: find-idea, ts: "01:20", case: chatbase, what: "Thấy demo 'ChatGPT cho dữ liệu của bạn' trên mạng mà chưa ai làm thành sản phẩm, nên quyết làm ngay", tactic: s12-timing-shift, tactic_note: "làn sóng AI mới: đã có demo, chưa có sản phẩm"}
  - {stage: validate, ts: "01:35", case: chatbase, what: "Build xong rồi tung cho 16 follower, không đo nhu cầu trước", tactic: other, tactic_note: "build trước rồi đưa cho audience nhỏ sẵn có; không có bước validate"}
  - {stage: launch, ts: "02:05", case: chatbase, what: "Tweet thứ ba: giao diện streaming kiểu ChatGPT, demo cho thấy sản phẩm trong 20 giây đầu, nhắc LangChain và Pinecone để các hãng đó đẩy lên", tactic: g3-organic-content-formats, tactic_note: "tweet demo kèm tên công cụ AI mà hãng đang muốn quảng bá"}
  - {stage: grow, ts: "06:01", case: chatbase, what: "Mỗi lần thêm tính năng được đăng như một lần ra mắt mới, có bối cảnh cho người chưa biết sản phẩm", tactic: g3-organic-content-formats}
  - {stage: grow, ts: "06:16", case: chatbase, what: "Làm chatbot miễn phí cho từng cuốn sách rồi đăng vào subreddit sách", tactic: g3-organic-content-formats, tactic_note: "tool miễn phí theo chủ đề cộng đồng; mục đích là lượt mở domain, lỗ tiền"}
  - {stage: grow, ts: "06:46", case: chatbase, what: "Trả tiền để một trang LinkedIn lớn đăng sponsored post về sản phẩm trong ngày ra mắt", tactic: g7-creator-ops, cost: "khoảng 4.000 USD cho một bài (lời founder, ước lượng)"}
  - {stage: monetize, ts: "07:33", case: chatbase, what: "PLG: người dùng tự đăng ký và trả tiền qua nút Stripe trên web; marketing làm ở ngoài website", tactic: g4-pricing-paywall}
quotes:
  - {ts: "01:35", who: "Yasser", stage: validate, theme: [action-over-research], text: "I didn't do any validation or anything. I just like said if I don't do this someone else will.", vi: "Tôi không validate gì cả. Tôi chỉ nghĩ: nếu mình không làm thì người khác sẽ làm."}
  - {ts: "01:50", who: "Yasser", stage: launch, theme: [risk-and-leap], text: "I had like two or three sales every day and uh I dropped out.", vi: "Mỗi ngày có hai ba đơn, và tôi bỏ học."}
  - {ts: "11:08", who: "Yasser", stage: mindset, theme: [], text: "I wasn't thinking big enough in the beginning.", vi: "Lúc đầu tôi không nghĩ đủ lớn."}
  - {ts: "11:23", who: "Yasser", stage: mindset, theme: [emotional-bottleneck], text: "I was too worried that because everyone was saying it's like a chat GPT rapper. It's not going to work.", vi: "Tôi quá lo vì ai cũng nói đó chỉ là app bọc ChatGPT, không làm nên chuyện."}
rules:
  - {ts: "11:55", who: "Pat Walls", stage: mindset, theme: [], text: "Yaser is proof that you don't need a big audience to get started.", vi: "Yaser chứng minh bạn không cần khán giả lớn mới bắt đầu được.", evidence: opinion}
numbers:
  - {ts: "00:48", metric: "số follower Twitter khi tweet đầu", value: 16, unit: count, evidence: claimed}
  - {ts: "05:28", metric: "thời gian từ 0 đến 1 triệu ARR (host nói lại)", value: 117, unit: days, evidence: claimed}
  - {ts: "07:18", metric: "khách trả tiền", value: 10000, unit: count, evidence: claimed}
  - {ts: "07:18", metric: "người đăng ký (registered users)", value: 600000, unit: count, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Yasser làm Chatbase (chat với tài liệu bằng AI): build rồi tung cho 16 follower mà không validate, tweet demo lan truyền, và hiện chỉ có PLG (nút Stripe trên web) với khoảng 10.000 khách trả tiền, 6,8 triệu ARR theo lời kể.

## Bài học cho tôi

- Tweet đầu lan nhờ demo cho thấy sản phẩm trong 20 giây đầu và nhắc tên công cụ AI mà các hãng đang muốn quảng bá (`02:05`).
- PLG: người dùng tự đăng ký và trả tiền qua nút Stripe trên web, marketing làm ở ngoài website (`07:33`).

## Đừng tin vội

- Số liệu lệch và không có dashboard: đầu video nói 7 triệu ARR (`00:48`), giữa video nói 6,8 triệu (`07:03`). "1 triệu ARR trong 117 ngày" là host nói lại (`05:28`).
- Đợt viral đầu gắn với làn sóng AI lúc đó: các hãng AI (LangChain, Pinecone) đẩy lại tweet vì muốn chứng minh có người dùng thật. Hoàn cảnh này khó lặp lại nguyên xi.
- Video không nói thời gian build, chi phí, nhóm 10 người dùng đầu, hay giá gói năm. Founder có thực tập FAANG và học đại học, không phải ai cũng có.
- Video quảng bá Brex và Starter Story Build.
