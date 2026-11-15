---
schema: 2
video_id: 88BbTpbWVpY
channel: starter-story
title: "I rebuilt a $1B app and now make $14K/month"
date: 2025-10-16
url: https://www.youtube.com/watch?v=88BbTpbWVpY
transcript: starter-story-kb/videos/2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month/transcript.md
kind: founder_case
speakers:
  - {name: "Denis Yurchak", role: founder}
  - {name: "Pat Walls", role: host}
bias: "Starter Story quảng bá khoá Starter Story Build (AI build) ngay trong video. Câu chuyện kể sau thành công nên có survivorship bias."
analyzed: 2026-11-15
cases:
  - id: yaphone
    depth: full
    product: "Yadaphone (yadaphone.com): gọi quốc tế rẻ ngay trên trình duyệt"
    what: "Gọi điện quốc tế qua trình duyệt, tính tiền theo credit trả trước, không subscription"
    type: [web-app]
    customer: "Người gọi quốc tế thường xuyên: du lịch, expat, doanh nghiệp (gọi cơ quan, ngân hàng, di trú ở nước ngoài)"
    founder: {who: "Denis Yurchak", base: "không nêu", technical: true, team: "không nêu rõ", background: "Học ngoại giao ở Nga, tự học code trong 2 tháng, freelance nhiều dự án trước khi làm Yadaphone"}
    revenue: {amount: 14000, unit: usd, basis: monthly, note: "Lời founder: khoảng $14k/tháng; video không mở dashboard hay Stripe", q: "It makes $14,000 a month", ts: "00:46", evidence: claimed}
    pricing: "Pay-as-you-go: nạp credit trả trước, dùng chung số dư cho cả tổ chức; so với đối thủ SaaS khoảng $30/tháng trở lên"
    idea_origin: [own_pain, timing_trigger]
    scale_channels: [seo, reddit, b2b_deals]
    community_at_discovery: {value: "Chính Denis là người gọi quốc tế thường xuyên cho cơ quan, ngân hàng, di trú ở nước ngoài (nhóm khách của Skype)", insider: true, q: "I've been their loyal client", ts: "04:24"}
    demand_signal: {kind: built_first, level: 0, what: "Build prototype cuối tuần rồi mới launch công khai trên Reddit và X. Video không nêu tín hiệu nhu cầu nào trước launch ngoài tweet của Peter Levels", q: "I just built a quick prototype over the weekend", ts: "04:55"}
    prior_failures: {count: null, what: "Các dự án freelance trước đó xấu, không có người dùng; học dần qua từng dự án (số lượng không nêu)", q: "my first projects, they were ugly. They had no users", ts: "03:38"}
    unfair_advantage:
      - {value: technical_skill, what: "Tự học code trong 2 tháng rồi làm được sản phẩm", q: "I taught myself how to code in two months mainly with books and courses", ts: "03:22"}
      - {value: luck, what: "Founder tự nhận timing đúng (Microsoft đóng Skype)", q: "a combination of a very good timing because at the time Microsoft announced it was closing Skype down", ts: "08:02"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: {months: 3, value: "khoảng tháng 2-3 đạt $10.800", q: "Two months three, we've climbed to $10,800", ts: "01:18"}
      to_current: {months: 7, value: "7 tháng từ con số 0 tới $14k/tháng", q: "In just 7 months, he went from nothing to a $14,000 per month app", ts: "00:16"}
    first_users:
      - {channel: reddit, what: "Đăng Reddit: subreddit du lịch bị chặn nhanh nhưng vẫn có sale trong vài phút", q: "I got the first sales minutes after my first Reddit post", ts: "07:15"}
      - {channel: reddit, what: "Chuyển sang subreddit khởi nghiệp (được tự giới thiệu sản phẩm); tuần đầu có 150 user (video không tách theo kênh)", q: "In the first week, I got 150 users", ts: "07:46"}
    build: {time: "Một cuối tuần cho prototype", cut: [], q: "I just built a quick prototype over the weekend", ts: "04:55"}
steps:
  - {stage: find-idea, ts: "04:09", case: yaphone, what: "Denis đi công tác nhiều, phải gọi cơ quan và ngân hàng nước ngoài; là người dùng Skype lâu năm nên ý tưởng xuất phát từ nỗi đau của chính nhóm khách đó.", tactic: s5-insider, tactic_note: "Founder thuộc nhóm khách: người gọi quốc tế thường xuyên cho cơ quan, ngân hàng (pain)"}
  - {stage: find-idea, ts: "04:40", case: yaphone, what: "Microsoft thông báo đóng Skype (tháng 3/2025); thấy tweet của Peter Levels kêu gọi làm thay thế Skype, Denis quyết làm.", tactic: s12-timing-shift, tactic_note: "Bắt thay đổi của nền tảng lớn: Skype đóng cửa"}
  - {stage: launch, ts: "04:55", case: yaphone, what: "Build prototype trong một cuối tuần, đăng Reddit và X, có sale đầu tiên trong vài phút.", tactic: g1-first-10-users, tool: "Reddit, X", tactic_note: "Đăng bài cộng đồng Reddit, không phải nền tảng launch"}
  - {stage: grow, ts: "07:30", case: yaphone, what: "Sau subreddit du lịch bị chặn, chuyển sang đăng subreddit khởi nghiệp, nơi được tự giới thiệu sản phẩm.", tactic: g1-first-10-users, tactic_note: "Cộng đồng Reddit khởi nghiệp"}
  - {stage: monetize, ts: "02:36", case: yaphone, what: "Đặt giá theo credit trả trước (pay-as-you-go) thay vì subscription khoảng $30/tháng.", tactic: g4-pricing-paywall, threshold: "subscription khoảng $30/tháng của đối thủ"}
  - {stage: monetize, ts: "11:24", case: yaphone, what: "Khách doanh nghiệp nhắn hỏi có gói enterprise không; Denis làm gói trong một đêm, khách trả khoảng $1.000/tháng.", tactic: g4-pricing-paywall, tactic_note: "Gói enterprise (B2B) làm ngay khi khách hỏi", cost: "khoảng $1.000/tháng từ một khách"}
  - {stage: grow, ts: "09:50", case: yaphone, what: "Khi đối thủ lớn rời đi, nhắm từ khoá 'Skype alternative': tìm bài blog đang xếp hạng, nhắn tác giả xin nhắc tới Yadaphone hoặc thay Skype bằng Yadaphone.", tactic: g2-aso-seo-organic, tactic_note: "Xin backlink từ các bài blog đang xếp hạng cho từ khoá thay thế"}
  - {stage: grow, ts: "13:13", case: yaphone, what: "Sitemap thiếu tiền tố www nên Google bỏ qua các trang muốn xếp hạng; sửa lại.", tactic: g2-aso-seo-organic, tactic_note: "Lỗi kỹ thuật SEO: sitemap thiếu www"}
  - {stage: retain, ts: "10:38", case: yaphone, what: "Nhắn từng khách trả tiền trong 6 tháng để hỏi phản hồi, phát hiện user segment và review xấu sớm.", tactic: g5-retention, tactic_note: "Nhắn tay từng khách đã trả để hỏi phản hồi"}
quotes:
  - {ts: "08:49", who: "Denis Yurchak", stage: find-idea, theme: [], text: "I would say that the first step is find a market where your competitors are dinosaurs. They are old-fashioned and slowmoving.", vi: "Bước đầu tiên là tìm thị trường mà đối thủ là khủng long: già nua và chậm chạp."}
  - {ts: "08:02", who: "Denis Yurchak", stage: validate, theme: [], text: "It's a validated market which was first validated with the tweet by Peter levels I saw and then by sales I got from my Reddit post", vi: "Đây là thị trường đã được kiểm chứng: đầu tiên qua tweet của Peter Levels, sau đó qua doanh số từ bài Reddit."}
  - {ts: "07:15", who: "Denis Yurchak", stage: launch, theme: [emotional-bottleneck], text: "I got blocked there really fast and it was quite demotivating.", vi: "Bị chặn rất nhanh ở đó, và khá nản."}
  - {ts: "12:41", who: "Denis Yurchak", stage: grow, theme: [persistence], text: "I would advise to do search engine optimization from day one and you have to be very patient with it.", vi: "Tôi khuyên làm SEO từ ngày đầu và phải rất kiên nhẫn."}
  - {ts: "10:38", who: "Denis Yurchak", stage: retain, theme: [], text: "I used to text every single paying customer for 6 months asking for feedback.", vi: "Tôi từng nhắn từng khách trả tiền suốt 6 tháng để hỏi phản hồi."}
rules:
  - {ts: "13:44", who: "Pat Walls", stage: find-idea, theme: [], text: "And this is proof that building in proven markets is the way to build an app in 2025.", vi: "Đây là bằng chứng rằng làm app ở thị trường đã được kiểm chứng là cách đúng trong 2025.", evidence: opinion}
numbers:
  - {ts: "01:18", metric: "doanh thu tháng đầu sau launch", value: 4000, unit: usd_per_month, evidence: claimed}
  - {ts: "01:18", metric: "doanh thu khoảng tháng 2-3", value: 10800, unit: usd_per_month, evidence: claimed}
  - {ts: "01:33", metric: "người đăng ký trong 7 tháng", value: 10000, unit: count, evidence: claimed}
  - {ts: "01:33", metric: "khách trả tiền cá nhân", value: 4500, unit: count, evidence: claimed}
  - {ts: "01:33", metric: "khách doanh nghiệp", value: 20, unit: count, evidence: claimed}
frameworks: [niche-down-proven-category]
idea_patterns: []
---

## Một câu

Denis (Yadaphone) bắt đúng lúc Microsoft đóng Skype, làm bản gọi quốc tế trên trình duyệt trong một cuối tuần, bán được vài phút sau khi đăng Reddit, và đạt khoảng $14k/tháng sau 7 tháng.

## Bài học cho tôi

- Bắt một thay đổi lớn của nền tảng khác (Skype đóng cửa) rồi có bản thay thế ngay trong tuần: thời điểm kéo nhu cầu tới (`04:40`).
- Ý tưởng đến từ nỗi đau của chính Denis: ông là người gọi quốc tế thường xuyên và đã trả tiền cho Skype để làm việc đó (`04:24`).

## Đừng tin vội

- Thời điểm Skype đóng cửa là lợi thế một lần, không lặp lại. Video kể sau khi thành công, không nêu bao nhiêu dự án khác đã thất bại cùng thời điểm.
- Denis tự nói ông không có audience (chỉ khoảng 60 follower X), nên đây không phải lợi thế có sẵn; nhưng video không nêu chi phí marketing. Ông nói chi phí chính là Twilio, khoảng 35% doanh thu (lời ông, chưa kiểm).
- Doanh thu $14k là lời founder, không có dashboard hay Stripe; host không yêu cầu mở.
- Không có tín hiệu nhu cầu đo được trước launch ngoài tweet của Peter Levels; mọi bằng chứng bán hàng đến sau khi đăng công khai.
