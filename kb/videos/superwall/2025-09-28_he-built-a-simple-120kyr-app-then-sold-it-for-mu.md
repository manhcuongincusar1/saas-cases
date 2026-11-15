---
schema: 2
video_id: NmIHgCRd04E
channel: superwall
title: "He Built a Simple $120k/Yr App, Then Sold It For Multiple 6 Figures!"
date: 2025-09-28
url: https://www.youtube.com/watch?v=NmIHgCRd04E
transcript: superwall/youtube-transcript/superwall/he-built-a-simple-120kyr-app-then-sold-it-for-multiple-6-figures/transcript.md
kind: founder_case
speakers:
  - {name: "Host (không nêu tên)", role: host}
  - {name: Lots, role: founder}
bias: "Podcast của Superwall (công ty paywall, tài trợ video); mô tả có link cộng đồng và buổi private dinner trả phí. Founder vừa bán app trong video."
analyzed: 2026-11-15
cases:
  - id: preycreen
    depth: full
    product: "Preycreen: app bắt người dùng cầu nguyện trước khi mở khoá điện thoại"
    what: "App chặn ứng dụng; người dùng phải cầu nguyện vài giây mới mở được app. Là bản Kitô giáo của One Sec"
    type: [mobile-app]
    customer: "Kitô hữu muốn cầu nguyện đều đặn hơn"
    founder: {who: Lots, base: null, technical: null, team: "không nêu; có agency quản 10–12 tài khoản TikTok", background: "Đã làm app Kitô giáo trước (Bible Buddy, theo host); bán nhiều app trước đó"}
    revenue: {amount: 120000, unit: usd, basis: arr, note: "120K ARR sau khoảng 5–6 tháng chạy quảng cáo; lời founder, không có dashboard", q: "it hit 120K AR in 6 months", ts: "00:00:47", evidence: claimed}
    pricing: "Bản miễn phí có quảng cáo trong app, không đặt paywall vì tỉ lệ trả tiền từ lượt cài thấp (lời founder)"
    idea_origin: [trend_copy, passion_skin]
    scale_channels: [tiktok_organic, ugc_creators, paid_meta]
    community_at_discovery: {value: "Đã làm app trong mảng đức tin, là Kitô hữu", insider: true, q: "I've normally built in the faith space myself", ts: "00:04:48"}
    demand_signal: {kind: similar_product_revenue, level: 3, what: "Thấy One Sec (bắt người ta hít thở 3 giây trước khi mở Instagram) được cho là kiếm khoảng 100k/tháng, rồi chép cơ chế đó", q: "they're making 100k a month", ts: "00:04:48"}
    prior_failures: null
    unfair_advantage:
      - {value: prior_success, what: "Đã bán nhiều sản phẩm trước đó", q: "because I've sold multiple things before", ts: "00:02:09"}
      - {value: domain_expertise, what: "Đã làm app Kitô giáo trước (Bible Buddy)", q: "I created Bible body to be more so like a therapist for Christians", ts: "00:12:43"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 6, value: "khoảng 5–6 tháng để tới 120K ARR", q: "it hit 120K AR in 6 months", ts: "00:00:47"}
    first_users:
      - {channel: tiktok_organic, what: "TikTok là kênh tăng trưởng chính (lời founder). Video không nói 10 người dùng đầu tiên đến từ đâu", q: "I would say Tik Tok was", ts: "00:06:02"}
      - {channel: ugc_creators, what: "Scale nhanh bằng UGC trên TikTok qua agency quản 10–12 tài khoản", q: "using obviously UGC on Tik Tok", ts: "00:02:09"}
    build: null
  - id: bible-buddy
    depth: mention
    product: "Bible Buddy: app chat trị liệu cho Kitô hữu (trước là bot WhatsApp)"
    what: "Trả lời như nhà trị liệu, rồi gợi ý chương Kinh Thánh; host nói có khoảng 100k người dùng hằng tháng"
  - id: magic-music
    depth: mention
    product: "Magic Music: app tạo nhạc bằng AI, làm trong khoảng 4 ngày sau khi Suno ra mắt"
    what: "App tạo nhạc AI; founder nói không có API. Ý tưởng chép từ một app chat-AI của bạn đang kiếm nửa triệu/tháng"
    idea_origin: [trend_copy, timing_trigger]
  - id: car-spotter
    depth: mention
    product: "Car Spotter (của Sha): kiểu Pokemon cho xe, chụp ảnh xe để khám phá"
    what: "App của một người trong cộng đồng founder; chỉ có một TikTok và một Instagram"
    revenue: {amount: 8000, unit: usd, basis: mrr, note: "Nghe kể, khoảng 4 tháng sau khi làm", q: "he recently just hit 8K MR", ts: "00:10:01", evidence: claimed}
steps:
  - {stage: find-idea, ts: "00:04:48", case: preycreen, what: "Tải thử One Sec, thấy app này được cho là kiếm khoảng 100k/tháng; quyết chép cơ chế đó sang Kitô hữu.", tactic: s11-copy-or-localize-proven, tactic_note: "Chép cơ chế đã chạy của One Sec, đổi ngách sang Kitô giáo"}
  - {stage: grow, ts: "00:02:09", case: preycreen, what: "Dùng agency quản khoảng 10–12 tài khoản TikTok để đăng và mở rộng nội dung.", tactic: g7-creator-ops}
  - {stage: grow, ts: "00:03:02", case: preycreen, what: "Thử nhiều hook; chọn hook đối lập với tôn giáo, gây tranh cãi để người xem bình luận, rồi cho thấy màn hình splash và màn hình kết quả.", tactic: g3-organic-content-formats, tactic_note: "Hook gây sốc/tranh cãi để tăng bình luận"}
  - {stage: grow, ts: "00:06:02", case: preycreen, what: "Chạy Meta ads (Instagram) từ video TikTok đã thắng; CPI tốt nhất 0.39 USD, trung bình khoảng 0.70–0.80 USD ở Mỹ.", tactic: g6-paid-ads, cost: "CPI trung bình 0.70–0.80 USD (Mỹ)"}
  - {stage: monetize, ts: "00:08:34", case: preycreen, what: "Đổi sang bản miễn phí có quảng cáo thay vì paywall; kiếm khoảng 5 cent/người dùng/ngày, hoàn vốn quảng cáo sau khoảng 14–15 ngày.", tactic: g4-pricing-paywall, tactic_note: "Freemium có quảng cáo thay cho trả tiền, dựa vào retention 60% ngày 30", threshold: "hoàn vốn 14–15 ngày"}
  - {stage: scale, ts: "00:02:09", case: preycreen, what: "Đăng tweet về việc bán app sau khi đạt khoảng 120K ARR; người mua đã nhắn DM và chốt trong khoảng một tuần."}
  - {stage: grow, ts: "00:13:21", case: bible-buddy, what: "Chạy Twitter ads nhắm follower của các mục sư nổi tiếng (trước đó dùng bot WhatsApp, phí tin nhắn cao).", tactic: g6-paid-ads, tool: "Twitter Ads (target follower của tài khoản)"}
  - {stage: find-idea, ts: "00:14:50", case: magic-music, what: "Ngay khi Suno ra mắt AI tạo nhạc, làm Magic Music trong khoảng 4 ngày, dựa trên một app chat-AI đã kiếm được nhiều.", tactic: s12-timing-shift, tactic_note: "Bắt AI mới ra mắt và làm ngay; kết hợp chép app đã chạy của bạn"}
quotes:
  - {ts: "00:04:48", who: Lots, stage: find-idea, theme: [learn-from-others], text: "And I was just like wait hold on they're making 100k a month. What the hell?", vi: "Tôi tải thử One Sec rồi nghĩ: chờ đã, họ kiếm 100k một tháng sao?"}
  - {ts: "00:03:44", who: Lots, stage: grow, theme: [], text: "I think what you need to do is find that one emotion specifically that you want people to feel after that content and that one thing it is.", vi: "Cần tìm đúng một cảm xúc muốn người xem có sau nội dung đó."}
  - {ts: "00:18:30", who: Lots, stage: mindset, theme: [revenue-first], text: "I always told people, yo, like get your first nut first.", vi: "Tôi luôn nói với mọi người: có chiến thắng đầu tiên đã, rồi mới nghĩ tới lớn."}
  - {ts: "00:21:37", who: Lots, stage: scale, theme: [], text: "I'm just like, bro, most deals fall through, like 90% plus", vi: "Đa số thương vụ bán app đổ bể, khoảng 90%; tôi thà nhận giá thấp hơn mà chốt trong vài ngày."}
  - {ts: "00:20:11", who: Lots, stage: mindset, theme: [], text: "I know like 20 people who will fund an entire thing", vi: "Tôi biết khoảng 20 người sẵn sàng tài trợ cả một dự án vì họ đã thấy tôi làm đi làm lại."}
rules:
  - {ts: "00:19:43", who: "Host (không nêu tên)", stage: mindset, theme: [], text: "I feel like a lot of people like they see the big success and they just want to have the same thing", vi: "Nhiều người thấy thành công lớn rồi muốn có y như vậy, mà không thấy họ cần kỹ năng trước.", evidence: opinion}
  - {ts: "00:19:16", who: "Host (không nêu tên)", stage: find-idea, theme: [learn-from-others], text: "Yeah, I mean with all these things, these were all like kind of a twist on something that already existed, right?", vi: "Các ý tưởng này đều là biến tấu của thứ đã có sẵn.", evidence: opinion}
  - {ts: "00:20:42", who: "Host (không nêu tên)", stage: scale, theme: [], text: "I feel like people don't think about exits nearly enough", vi: "Tôi thấy người ta không nghĩ đủ về chuyện bán app.", evidence: opinion}
numbers:
  - {ts: "00:05:33", metric: "retention ngày 30 của người cầu nguyện 4 lần mỗi ngày", value: 0.6, unit: ratio, evidence: claimed}
  - {ts: "00:06:02", metric: "CPI Meta ads trung bình ở Mỹ", value: "0.70–0.80", unit: usd, evidence: claimed}
  - {ts: "00:10:01", metric: "MRR app Car Spotter (nghe kể)", value: 8000, unit: usd_per_month, evidence: claimed}
frameworks: [organic-find-format-then-paid-scale]
idea_patterns: [passion-skin]
---

## Một câu

Founder chép cơ chế app chặn màn hình 3 giây (One Sec) sang Kitô hữu: đăng TikTok gây tranh cãi rồi chạy Meta ads, đạt khoảng 120K ARR trong 6 tháng (lời founder), sau đó bán app qua một tweet và chốt trong một tuần.

## Bài học cho tôi

- Chép cơ chế đã chạy rồi đổi ngách: người dùng cầu nguyện 4 lần mỗi ngày và giữ 60% sau 30 ngày (`00:05:33`).
- Chọn bán nhanh hơn là bán giá cao nhất: founder thà nhận giá thấp hơn mà chốt trong vài ngày (`00:21:37`).

## Đừng tin vội

- Video là podcast của Superwall (công ty paywall, tài trợ video), nên nội dung hướng tới việc làm app bằng paywall và quảng cáo; tên host không được nêu trong transcript.
- Doanh thu 120K ARR, CPI, retention 60% và việc One Sec kiếm 100k/tháng đều là lời kể, không có dashboard. Car Spotter (8K MR) là nghe kể về người khác.
- Điều kiện riêng: Preycreen là app tôn giáo có khán giả Kitô hữu sẵn và hook gây tranh cãi; một video TikTok chiếm khoảng 70% lượt cài (`00:06:56`), đó là trúng số, khó lặp lại.
- Video không nói 10 người dùng đầu tiên đến từ đâu, không nói ngân sách, không nói thời gian build, và không nói giá bán app.
