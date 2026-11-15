---
schema: 2
video_id: 3X4VneEHvig
channel: starter-story
title: "How I Used Reddit To Build a $25K/Month Business"
date: 2025-08-09
url: https://www.youtube.com/watch?v=3X4VneEHvig
transcript: starter-story-kb/videos/2025-08-09_how-i-used-reddit-to-build-a-25k-month-business/transcript.md
kind: founder_case
speakers:
- {name: Avneesh, role: founder}
- {name: Pat Walls, role: host}
bias: "Starter Story bán chương trình Starter Story Build (dạy làm app bằng AI), quảng cáo giữa video; founder được chọn làm case; số liệu founder tự nêu, không có dashboard."
analyzed: 2026-11-15
cases:
- id: savewise
  depth: full
  product: "Savewise: gom ưu đãi hoàn tiền và điểm thẻ tín dụng/dặm bay cho thứ người ta mua online"
  what: "Tra cứu ưu đãi hoàn tiền (Rakuten, Amex...) và điểm thẻ theo từng cửa hàng; dữ liệu đến từ hệ thống của founder trên web"
  type: [web-app]
  customer: "Người săn ưu đãi, mua sắm online và dùng thẻ tín dụng để lấy điểm/dặm"
  founder: {who: Avneesh, base: null, technical: true, team: null, background: "Làm kỹ thuật lâu năm ở các công ty tech lớn (Microsoft, Instagram, Foursquare, Dropbox)"}
  revenue: {amount: 25000, unit: usd, basis: monthly, note: "Doanh thu hiện tại mỗi tháng, founder nói bằng 'revenue a month'", q: "approximately $25,000 of revenue a month", ts: "11:10", evidence: claimed}
  pricing: "Ban đầu có gói subscription; khách xin gói trọn đời trả trước 2+ năm; hiện phần lớn doanh thu từ gói trọn đời (không nêu giá)"
  idea_origin: [own_pain]
  scale_channels: [reddit, facebook_groups]
  community_at_discovery:
    value: "Chính founder là người săn ưu đãi thủ công (coupon, điểm thẻ); thấy việc này quá thủ công"
    insider: true
    q: "I am really good at figuring out how to find deals and stack coupons"
    ts: "01:49"
  demand_signal:
    kind: built_first
    level: 0
    what: "Founder build sản phẩm cho chính mình trước; sau đó mới đi tìm người dùng"
    q: "I built a product that was kind of working for me, but then I had to go and find people to actually use it"
    ts: "02:35"
  prior_failures:
    count: 2
    what: "Đăng Product Hunt, Hacker News, Indie Hackers: có traffic nhưng bounce khoảng 95–96%; gửi 300–400 tin cho influencer, chỉ 1 người trả lời"
    q: "I got a single email back out of all of those"
    ts: "03:05"
  unfair_advantage:
  - {value: domain_expertise, what: "Giỏi tìm ưu đãi và xếp chồng coupon, điểm thẻ: đúng nghiệp vụ mà sản phẩm làm", q: "I am really good at figuring out how to find deals and stack coupons", ts: "01:49"}
  - {value: technical_skill, what: "Làm trong ngành tech nhiều năm ở các công ty lớn", q: "I've always worked in the tech industry", ts: "01:34"}
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: {months: 15, value: "15 tháng (host nói ở phần mở; founder không nhắc lại)", q: "built a $25,000 per month business in just 15 months", ts: "00:00"}
  first_users:
  - {channel: facebook_groups, what: "Đăng một bảng tính ưu đãi (lấy từ dữ liệu của sản phẩm), có link về web, vào nhóm Facebook về ưu đãi Rakuten; hơn 1.500 lượt vào web", q: "I had over 1,500 people visit the website just from posting this spreadsheet in this Facebook group", ts: "09:37"}
  - {channel: reddit, what: "Trả lời trong comment Q&A tuần của một subreddit, đăng website và xin feedback; sau đó được mod cho đăng bài chính", q: "Every week or so, I would join that weekly comment thread, post the website, and ask for feedback", ts: "10:07"}
  build: {time: "khoảng 3,5 tháng kể từ lúc xin feedback trong thread tới khi có đủ tính năng cốt lõi", cut: [], q: "after about three and a half months, I had built out all of the core functionality", ts: "10:22"}
steps:
- stage: find-idea
  ts: "02:04"
  case: savewise
  what: "Tự săn ưu đãi thủ công, thấy không có công cụ nào làm việc đó; quyết định tự build cho chính mình."
  tactic: s5-insider
  tactic_note: "nỗi đau riêng: chính founder là người dùng"
- stage: launch
  ts: "02:35"
  case: savewise
  what: "Đăng Product Hunt, Hacker News, Indie Hackers: có traffic nhưng người dùng không ở lại (bounce khoảng 95–96%)."
  tactic: g9-launch-platforms
- stage: launch
  ts: "02:50"
  case: savewise
  what: "Gửi khoảng 300–400 tin nhắn/email cho influencer và người có audience lớn; chỉ có 1 hồi âm."
  tactic: g7-creator-ops
  tactic_note: "tiếp cận influencer lạnh khi sản phẩm còn thô; không có kết quả"
- stage: launch
  ts: "04:23"
  case: savewise
  what: "Brainstorm 5–15 từ khoá, sở thích, nhân khẩu học của người sẽ dùng sản phẩm."
  tactic: g1-first-10-users
- stage: launch
  ts: "04:39"
  case: savewise
  what: "Dùng công cụ 'map of Reddit' nhập một subreddit để tìm các subreddit liên quan."
  tactic: g1-first-10-users
  tool: "map of Reddit"
- stage: launch
  ts: "05:12"
  case: savewise
  what: "Vào các nhóm Reddit/Facebook và quan sát, không đăng ngay; xác định mục tiêu từng nhóm và bắt đầu bằng comment trước khi đăng bài chính."
  tactic: g1-first-10-users
  tactic_note: "quan sát và comment trước, chưa đăng bài quảng bá"
- stage: launch
  ts: "06:45"
  case: savewise
  what: "Đặt cảnh báo từ khoá để nhận email khi có người nhắc tới chủ đề; đọc từng bài và trả lời nếu phù hợp."
  tactic: g1-first-10-users
  tool: "F5bot"
- stage: launch
  ts: "07:15"
  case: savewise
  what: "Trả lời hữu ích bằng mẹo thật trước; sau đó mới nhắc sản phẩm trong comment."
  tactic: g3-organic-content-formats
  tactic_note: "giúp đỡ trước, nhắc sản phẩm sau"
- stage: launch
  ts: "08:49"
  case: savewise
  what: "Đăng một bảng tính ưu đãi (từ dữ liệu sản phẩm) vào nhóm Facebook về ưu đãi Rakuten, có link về web; hơn 1.500 lượt vào."
  tactic: g1-first-10-users
  tactic_note: "bảng tính có link web đăng trong nhóm Facebook"
- stage: launch
  ts: "10:07"
  case: savewise
  what: "Đăng website và xin feedback trong comment Q&A tuần của subreddit; sau khoảng 3,5 tháng xin mod đăng bài chính, bài đó nổ."
  tactic: g1-first-10-users
- stage: monetize
  ts: "11:25"
  case: savewise
  what: "Ra gói subscription; khách xin gói trọn đời trả trước 2+ năm; từ đó gói trọn đời chiếm phần lớn doanh thu."
  tactic: g4-pricing-paywall
  threshold: "khoảng 97% doanh thu từ gói trọn đời"
quotes:
- {ts: "02:04", who: Avneesh, stage: find-idea, theme: [action-over-research], text: "So let me just try building it and see where it goes", vi: "Vậy thì cứ thử build xem nó đi đâu."}
- {ts: "02:35", who: Avneesh, stage: launch, theme: [builder-trap], text: "I built a product that was kind of working for me, but then I had to go and find people to actually use it", vi: "Tôi build một sản phẩm chạy được cho mình, nhưng rồi phải đi tìm người thật sự dùng nó."}
- {ts: "03:05", who: Avneesh, stage: launch, theme: [right-audience], text: "So at that point, I knew I needed to take a very different approach, a very targeted approach", vi: "Lúc đó tôi biết cần cách làm khác hẳn: nhắm rất trúng người."}
- {ts: "11:25", who: Avneesh, stage: monetize, theme: [], text: "I learned consumers hate subscriptions", vi: "Tôi học được rằng người dùng ghét subscription."}
- {ts: "13:14", who: Avneesh, stage: launch, theme: [right-audience], text: "understanding your target customer and everything about them is even more useful for the marketing part of it", vi: "Hiểu khách hàng mục tiêu và mọi thứ về họ còn hữu ích hơn cho phần marketing."}
rules:
- {ts: "04:07", who: Pat Walls, stage: launch, theme: [], text: "I think that's a huge realization that a lot of people who come on the channel talk about.", vi: "Tôi nghĩ đó là một nhận ra lớn mà nhiều người lên kênh này hay nói tới.", evidence: opinion}
numbers:
- {ts: "11:10", metric: "doanh thu mỗi tháng", value: 25000, unit: usd_per_month, evidence: claimed}
- {ts: "11:25", metric: "khách trả tiền", value: 1500, unit: count, evidence: claimed}
- {ts: "11:41", metric: "tỉ lệ doanh thu từ gói trọn đời", value: 0.97, unit: ratio, evidence: claimed}
- {ts: "09:37", metric: "lượt vào web từ một bài trong nhóm Facebook", value: 1500, unit: count, evidence: claimed}
- {ts: "02:50", metric: "tỉ lệ bounce khi đăng Product Hunt/HN/Indie Hackers", value: "95–96%", unit: ratio, evidence: claimed}
frameworks: [right-audience-over-views]
idea_patterns: []
---

## Một câu

Avneesh làm Savewise, công cụ gom ưu đãi hoàn tiền và điểm thẻ cho thứ người ta mua online. Không quảng cáo; anh đi tìm người dùng bằng cách vào nhóm Facebook và comment Reddit đúng ngách. Hiện khoảng 25K USD/tháng với khoảng 1.500 khách trả tiền.

## Bài học cho tôi

- Vào cộng đồng thì quan sát và trả lời hữu ích trong comment trước khi đăng bài chính; bài chính trên Reddit nổ sau khoảng 3,5 tháng (`10:07`).
- Khi khách tự xin gói trọn đời trả trước, founder chuyển sang bán gói đó; giờ khoảng 97% doanh thu đến từ gói này (`11:25`).

## Đừng tin vội

- Số liệu founder tự nêu (25K/tháng, 1.500 khách, 97%), không có dashboard. Host nói "15 tháng" ở phần mở, founder không nhắc lại con số này.
- Cách làm này dựa vào ngách có cộng đồng hỏi-đáp rõ (săn ưu đãi thẻ tín dụng); điều kiện riêng của ngách, không chắc chép sang ngách khác.
- Video chèn quảng cáo Starter Story Build (bias). Founder là khách được chọn để kể case, nên không thấy các case thất bại.
