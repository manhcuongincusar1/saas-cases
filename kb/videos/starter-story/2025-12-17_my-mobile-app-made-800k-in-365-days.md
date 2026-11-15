---
schema: 2
video_id: LYdJ3dfNCVs
channel: starter-story
title: "My mobile app made $800K in 365 days"
date: 2025-12-17
url: https://www.youtube.com/watch?v=LYdJ3dfNCVs
transcript: starter-story-kb/videos/2025-12-17_my-mobile-app-made-800k-in-365-days/transcript.md
kind: founder_case
speakers:
  - {name: Pat Walls, role: host}
  - {name: Louis, role: founder}
bias: "Starter Story bán khoá TikTok playbook (Starter Story Build) và nhận tài trợ Xero (giảm 90%); số liệu app là lời founder, không có dashboard."
analyzed: 2026-11-15
cases:
  - id: glowup
    depth: full
    product: "GlowUp: app thử trang điểm bằng AI (iOS và Android), thu phí theo tuần hoặc năm"
    what: "Người dùng tải ảnh lên, AI thử các look trang điểm; onboarding cá nhân hoá rồi xin đánh giá 5 sao"
    type: [mobile-app]
    customer: "Phụ nữ muốn thử look trang điểm trước khi mua sản phẩm"
    founder: {who: "Louis", base: "Canada (host giới thiệu)", technical: true, team: "Louis và một đồng sáng lập", background: "Học phần mềm khoảng 2 năm rồi bỏ học; trước GlowUp đã làm nhiều app không có người dùng"}
    revenue: {amount: 800000, unit: usd, basis: lifetime, note: "Tổng doanh thu từ lúc launch khoảng một năm (lời founder); hiện khoảng 15k/tháng", q: "generated a total of 800K in revenue", ts: "01:18", evidence: claimed}
    pricing: "Subscription: $9.99/tuần hoặc $39.99/năm; không có gói nào khác"
    idea_origin: [user_request]
    scale_channels: [tiktok_organic]
    community_at_discovery: {value: "Louis không phải người trong ngành makeup; đọc comment TikTok makeup để tìm nhu cầu", insider: false, q: "I don't know anything about it", ts: "11:53"}
    demand_signal: {kind: content_views, level: 2, what: "Nội dung TikTok về look trang điểm và sản phẩm (đúng vấn đề của app) nổ trước khi build app", q: "it kind of just went viral", ts: "03:38"}
    prior_failures: {count: 10, what: "Làm khoảng 10 app trước đều thất bại (không có người dùng)", q: "I built probably 10 apps that all failed", ts: "00:00"}
    unfair_advantage:
      - {value: technical_skill, what: "Học phần mềm khoảng 2 năm rồi tự làm app", q: "I did software engineering for around 2 years and just dropped out", ts: "02:21"}
      - {value: cofounder, what: "Làm app cùng một đồng sáng lập", q: "me and my co-founder wanted to create a new app together", ts: "03:08"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 12, value: "khoảng 1 năm từ lúc launch (lời founder)", q: "I launched it a year ago as a side project", ts: "01:03"}
    first_users:
      - {channel: tiktok_organic, what: "Nút tải (anchor link) gắn vào video; phần lớn lượt tải đến từ đó", q: "Most of our downloads came from our anchor link", ts: "07:18"}
      - {channel: tiktok_organic, what: "Một video ~48 triệu view: ~60k lượt tải và khoảng 12,5k$ doanh thu trong một ngày", q: "we made around 12.5K in [music] sales in like one day with 60K downloads", ts: "08:20"}
    build: {time: "không nêu số ngày hay tuần; làm 'super quickly, super MVP style'", cut: [], q: "kind of just built the app super quickly, super MVP style", ts: "03:54"}
steps:
  - {stage: find-idea, ts: "03:23", case: glowup, what: "Xem video TikTok makeup và comment để tìm thứ người ta đang xin (look, sản phẩm); chọn ngách makeup vì nó lớn.", tactic: s4-tiktok-comment-mining}
  - {stage: validate, ts: "03:38", case: glowup, what: "Làm nội dung về look trang điểm và sản phẩm trước khi build app; nội dung nổ rồi mới làm app.", tactic: s8-content-demand-test, tactic_note: "Đăng nội dung về ý tưởng trước khi build xong; đo view"}
  - {stage: launch, ts: "07:02", case: glowup, what: "Gắn nút 'download now' (anchor link) vào video khi video đã có vài nghìn đến 100k view.", tactic: g3-organic-content-formats, tactic_note: "Nút tải ngay trong video"}
  - {stage: grow, ts: "07:33", case: glowup, what: "Mở thêm tài khoản (2–3 tài khoản mỗi điện thoại, thêm điện thoại nếu cần); đỉnh ~7 tài khoản đăng 8–12 video/ngày.", tactic: g3-organic-content-formats, tactic_note: "Nhiều tài khoản đăng lại một format"}
  - {stage: grow, ts: "08:35", case: glowup, what: "Trong app: mời 3 bạn để nhận một look miễn phí; người xem đăng mã mời trong comment video, làm engagement bùng.", tactic: g10-referral-viral-loop}
  - {stage: monetize, ts: "09:52", case: glowup, what: "Chỉ một gói subscription ($9.99/tuần hoặc $39.99/năm); onboarding dài và xin đánh giá 5 sao trước khi cho kết quả.", tactic: g4-pricing-paywall, tactic_note: "Onboarding cá nhân hoá rồi xin review trước khi cho kết quả"}
quotes:
  - {ts: "00:00", who: Louis, stage: mindset, theme: [builder-trap], text: "I built probably 10 apps that all failed.", vi: "Tôi làm khoảng 10 app và cái nào cũng thất bại."}
  - {ts: "03:38", who: Louis, stage: validate, theme: [sell-before-build], text: "So we did content first [music] because for most of my other apps before we were just building and building without showing to user what we had and it always failed.", vi: "Làm nội dung trước vì các app trước tôi chỉ làm rồi làm, không cho ai xem, và luôn thất bại."}
  - {ts: "03:54", who: Louis, stage: find-idea, theme: [right-audience], text: "by looking at comment section, you really just feel what people are wanting and you just try to come in and solve whatever they're asking for", vi: "Đọc comment là cảm được người ta muốn gì; rồi giải đúng cái họ xin."}
  - {ts: "11:23", who: Louis, stage: mindset, theme: [action-over-research], text: "It would be to move first and adjust later. Never wait for the perfect time because there's [music] no perfect time.", vi: "Hãy làm trước, chỉnh sau; đừng chờ thời điểm hoàn hảo vì nó không bao giờ đến."}
  - {ts: "11:38", who: Louis, stage: mindset, theme: [], text: "My other piece of advice is that you can have your capitalistic endeavor in whatever niche, you don't have to be an expert.", vi: "Bạn có thể làm kinh doanh ở bất kỳ ngách nào, không cần là chuyên gia."}
  - {ts: "11:53", who: Louis, stage: mindset, theme: [revenue-first], text: "Makeup is like not my passion. I don't know anything about it, but it's my capitalistic endeavor and it's lovely to make money out of it.", vi: "Makeup không phải đam mê của tôi, tôi không biết gì về nó, nhưng đó là việc kinh doanh và kiếm tiền từ nó thì tuyệt."}
rules:
  - {ts: "12:08", who: Pat Walls, stage: grow, theme: [], text: "Building a successful app [music] in 2025 is not about your tech stack or what tools you use. The secret, as you're seeing in this video right now, is content.", vi: "Xây app thành công năm 2025 không nằm ở tech stack; bí mật là nội dung, cụ thể là TikTok.", evidence: opinion}
  - {ts: "12:24", who: Pat Walls, stage: grow, theme: [], text: "is the number one thing I've realized after interviewing hundreds of founders on this channel. If you can get this part right, everything else just works.", vi: "Đây là điều số một host rút ra sau khi phỏng vấn hàng trăm founder: làm đúng phần này thì mọi thứ khác tự chạy.", evidence: opinion}
numbers:
  - {ts: "01:50", metric: "người dùng tổng (lời founder)", value: 2000000, unit: count, evidence: claimed}
  - {ts: "01:50", metric: "khách trả tiền (lời founder)", value: 70000, unit: count, evidence: claimed}
  - {ts: "01:50", metric: "doanh thu hàng tháng hiện tại (lời founder)", value: 15000, unit: usd, evidence: claimed}
  - {ts: "08:20", metric: "doanh thu một video TikTok trong một ngày (sau launch)", value: 12500, unit: usd, evidence: claimed}
  - {ts: "10:38", metric: "biên lợi nhuận (lời founder, nói 'phụ thuộc người dùng')", value: 90, unit: percent, evidence: claimed}
frameworks:
  - content-before-product
  - organic-find-format-then-paid-scale
idea_patterns:
  - snap-and-get-result
---

## Một câu

Louis (Canada) đọc comment TikTok makeup, làm nội dung về look trang điểm trước khi build GlowUp (thử look bằng AI), rồi dùng video TikTok có nút tải và nhiều tài khoản để đạt khoảng 800k$ doanh thu trong ~1 năm (lời founder).

## Bài học cho tôi

- Đọc comment để biết người ta đang xin gì, rồi làm nội dung về đúng thứ đó trước khi build (`03:23`, `03:38`).
- Nút tải ngay trong video (anchor link) là cầu nối từ view sang lượt tải; theo lời Louis, nên gắn khi video đã có vài nghìn view trở lên (`07:02`).

## Đừng tin vội

- Các số 800k, 48 triệu view, 12,5k$/ngày, 90% biên lợi nhuận là lời founder, không có dashboard. Video không nói chi phí, lợi nhuận thực tế hay giờ làm việc.
- Starter Story nhận tài trợ Xero và bán khoá TikTok playbook; câu "content là bí mật" (`12:08`) là lời quảng bá gói học của họ.
- Video chỉ kể app thành công. Khoảng 10 app trước đều thất bại (`00:00`) nhưng không có số liệu để so sánh.
- Điều kiện riêng: Louis tự nhận không biết gì về makeup (`11:53`) và dựa vào nhiều tài khoản TikTok, nên không đảm bảo sao chép được; video không nói có chạy quảng cáo trả tiền hay không.
