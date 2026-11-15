---
schema: 2
video_id: CwHD6Fg-Mjs
channel: starter-story
title: "I vibe coded a $20K/month mobile app in 14 days"
date: 2025-10-26
url: https://www.youtube.com/watch?v=CwHD6Fg-Mjs
transcript: starter-story-kb/videos/2025-10-26_i-vibe-coded-a-20k-month-mobile-app-in-14-days/transcript.md
kind: founder_case
speakers:
- {name: "Pat Walls", role: host}
- {name: "Connor Burd", role: founder}
bias: "Starter Story bán Starter Story Build (chương trình dựng app bằng AI, khoá mới 'bắt đầu tuần này'); video quảng bá cả chương trình này và guide miễn phí trong mô tả."
analyzed: 2026-11-15
cases:
- id: payout
  depth: full
  product: "Payout: app tìm các vụ kiện tập thể (class action) mà người dùng đủ điều kiện nhận tiền, rồi điền mẫu và tạo PDF để gửi thư"
  what: "Liệt kê vụ kiện tập thể đang mở; người dùng chọn vụ, điền form, app chuẩn bị PDF để gửi thư nhận tiền; có ví theo dõi vụ kiện đã đăng ký"
  type: [mobile-app]
  customer: "Người muốn nhận tiền từ các vụ kiện tập thể"
  founder: {who: "Connor Burd", base: null, technical: null, team: "solo (lời founder: làm một mình)", background: "23 tuổi, không có nền khoa học máy tính; bắt đầu làm app khoảng 3 năm trước bằng YouTube; hiện làm app bằng AI"}
  revenue: {amount: 20000, unit: usd, basis: monthly, note: "20k/tháng sau khi ra mắt đầu tháng 8; founder nói tổng các app trên 1 triệu (không chi tiết từng app)", q: "just scaled it up to doing 20,000 a month in revenue.", ts: "01:17", evidence: claimed}
  pricing: "Gói tuần và gói năm; founder nói gói năm được đẩy vì LTV mỗi khách cao nhất; video không nêu giá"
  idea_origin: null
  scale_channels: [ugc_creators]
  community_at_discovery: null
  demand_signal: null
  prior_failures: {count: 1, what: "Hotspot Events: app xã hội làm mất 6–8 tháng rồi thất bại", q: "This app took me 6 to 8 months to build kind of failed.", ts: "02:19"}
  unfair_advantage: []
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: null
  first_users: []
  build: {time: "dưới 2 tuần, viết bằng AI", cut: [], q: "I built my latest app in less than 2 weeks", ts: "00:00"}
steps:
- stage: build
  ts: "03:08"
  case: payout
  what: "Tải khoảng 20 app trong ngách và vài app đẹp để lấy cảm hứng; chụp mọi màn onboarding vào Figma rồi thiết kế lại theo theme của mình."
- stage: build
  ts: "04:41"
  case: payout
  what: "Viết một tài liệu mô tả dữ liệu cùng file JSON mẫu trước khi code, để AI không phải đoán cấu trúc."
- stage: build
  ts: "05:27"
  case: payout
  what: "Đưa ảnh màn hình vào Claude để viết code từng màn; làm chức năng lõi trước, bỏ onboarding ở bản đầu; không cầu toàn để ra bản nhanh."
- stage: validate
  ts: "07:31"
  case: payout
  what: "Với ý tưởng mới, xem TikTok và Instagram xem người ta có nói về vấn đề không, đọc comment xem có ai hỏi cách giải quyết không."
  tactic: s4-tiktok-comment-mining
- stage: validate
  ts: "07:46"
  case: payout
  what: "Với ý tưởng mới, bỏ các bước xác nhận 'vô bổ' và build luôn vì build bằng AI nhanh."
  tactic: other
  tactic_note: "Build trước, không có bước xác nhận nhu cầu riêng"
- stage: launch
  ts: "01:17"
  case: payout
  what: "Đưa Payout vào cuộc thi hackathon của RevenueCat (đưa app lên store trong thời gian thi); đoạt giải nhất hạng mục build & grow theo lời founder."
  tactic: g9-launch-platforms
  tactic_note: "Cuộc thi do RevenueCat tổ chức, thưởng theo tăng trưởng trong hai tháng"
- stage: grow
  ts: "08:46"
  case: payout
  what: "Hợp tác với một content creator trong ngách; video của họ đưa về hàng nghìn lượt tải."
  tactic: g7-creator-ops
- stage: grow
  ts: "09:01"
  case: payout
  what: "Khi một video chạy tốt, làm thêm video theo đúng format với các creator khác (UGC campaign)."
  tactic: g7-creator-ops
- stage: monetize
  ts: "10:16"
  case: payout
  what: "Onboarding hỏi quyền thông báo, hiện social proof rồi đến paywall; paywall có gói tuần và gói năm, đẩy người dùng sang gói năm vì LTV cao hơn."
  tactic: g4-pricing-paywall
quotes:
- {ts: "02:04", who: "Connor Burd", stage: find-idea, theme: [], text: "I woke up and I just had a random app idea and I wrote down the whole app idea in my notes.", vi: "Tôi thức dậy với một ý tưởng app ngẫu nhiên và ghi toàn bộ ý tưởng vào ghi chú."}
- {ts: "02:19", who: "Connor Burd", stage: find-idea, theme: [], text: "I quickly realized that apps that are social are super hard", vi: "Sau app đầu tiên, tôi nhận ra app xã hội rất khó scale."}
- {ts: "02:36", who: "Connor Burd", stage: find-idea, theme: [], text: "So I eventually moved on to utilities and tools and these are much more easy to scale as a oneman person.", vi: "Tôi chuyển sang tiện ích và công cụ vì dễ scale hơn khi làm một mình."}
- {ts: "03:40", who: "Connor Burd", stage: monetize, theme: [], text: "Realistically, 90% of users will probably only ever see your onboarding if you have a paywalled section in your app.", vi: "Thực tế, phần lớn người dùng chỉ thấy onboarding nếu app có phần paywall."}
- {ts: "07:16", who: "Connor Burd", stage: validate, theme: [], text: "If you're creating a modified version of an existing app, then congrats, your app is already validated by other people.", vi: "Nếu làm bản chỉnh sửa của một app có sẵn thì app đó đã được người khác kiểm chứng."}
- {ts: "07:46", who: "Connor Burd", stage: mindset, theme: [revenue-first], text: "I really believe that any app can make thousands of dollars these days.", vi: "Tôi tin rằng bất kỳ app nào cũng có thể kiếm vài nghìn đô mỗi tháng."}
- {ts: "12:22", who: "Connor Burd", stage: mindset, theme: [focus-one-thing], text: "My number one piece of advice would be to build something simple with a great onboarding.", vi: "Lời khuyên số một của tôi: làm một app đơn giản với onboarding thật tốt."}
- {ts: "12:37", who: "Connor Burd", stage: build, theme: [focus-one-thing], text: "three good features and your onboarding will pull most of the weight for you.", vi: "Ba tính năng tốt là đủ; onboarding sẽ gánh phần lớn việc."}
rules:
- {ts: "06:15", who: "Pat Walls", stage: build, theme: [], text: "a lot of people get into vibe coding, try to oneshot something real quick, get lost, not be able to deploy, and then give up.", vi: "Nhiều người vào vibe coding, cố làm xong một lần cho nhanh, rồi lạc, không deploy được và bỏ cuộc.", evidence: opinion}
- {ts: "08:16", who: "Pat Walls", stage: grow, theme: [], text: "building it is not enough. We have to focus on one very important thing, which is distribution.", vi: "Build xong chưa đủ; phải tập trung vào phân phối.", evidence: opinion}
numbers:
- {ts: "01:02", metric: "tổng doanh thu các app (lời founder)", value: 1000000, unit: usd, evidence: claimed}
- {ts: "01:17", metric: "MRR của Payout", value: 20000, unit: usd_per_month, evidence: claimed}
- {ts: "01:17", metric: "lượt tải Payout (transcript chép 'over 12,000')", value: 12000, unit: count, evidence: claimed}
- {ts: "01:33", metric: "số người tham gia hackathon", value: 55000, unit: count, evidence: claimed}
- {ts: "01:33", metric: "tổng giải thưởng build & grow", value: 65000, unit: usd, evidence: claimed}
frameworks: []
idea_patterns: []
---

## Một câu

Connor Burd (23 tuổi, không có nền khoa học máy tính) làm Payout, app giúp tìm vụ kiện tập thể mà người dùng đủ điều kiện nhận tiền; founder nói app đạt 20k/tháng sau khi ra mắt đầu tháng 8, và làm bản đầu trong dưới 2 tuần bằng AI.

## Bài học cho tôi

- Muốn làm app nhanh bằng AI: chụp mọi màn onboarding của khoảng 20 app cùng ngách, thiết kế lại theo phong cách của mình, rồi đưa ảnh màn hình vào AI để viết code từng màn; bỏ onboarding ở bản đầu (`03:08`, `05:27`).
- Founder coi onboarding là thứ quyết định chuyển đổi, vì phần lớn người dùng chỉ thấy onboarding khi có paywall; dành công sức cho nó như cho tính năng (`03:40`).

## Đừng tin vội

- Số 20k/tháng và 12k lượt tải là lời founder, không có dashboard. Transcript chép lỗi câu về đăng ký ("over 12,000 over,300 new subscriptions") nên không ghi số đăng ký. Câu "0 đến 20k trong 50 ngày" là của host đặt câu hỏi, founder không xác nhận.
- Video không nói kênh nào đem 10 người dùng đầu tiên, và không nói ý tưởng Payout đến từ đâu. Mô tả video nói founder "chỉ dùng Facebook ads", nhưng transcript chỉ nói mục tiêu chạy paid ads; chưa rõ kênh trả tiền nào đang chạy. Hợp tác creator không nói rõ có trả tiền hay không.
- Founder đã làm nhiều app trước (khoảng 6 app, có app thất bại); đây không phải trường hợp người mới bắt đầu. Video có quảng bá Starter Story Build và cuộc thi hackathon của RevenueCat.
