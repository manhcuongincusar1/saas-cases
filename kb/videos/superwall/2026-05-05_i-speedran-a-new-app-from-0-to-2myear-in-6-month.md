---
schema: 2
video_id: ukGtpnfBpvU
channel: superwall
title: "I speedran a new app from 0 to $2m/year in 6 months (here's how)"
date: 2026-05-05
url: https://www.youtube.com/watch?v=ukGtpnfBpvU
transcript: superwall/youtube-transcript/superwall/i-speedran-a-new-app-from-0-to-2myear-in-6-months-heres-how/transcript.md
kind: founder_case
speakers:
- name: Daniel
  role: founder
- name: Joseph Choi
  role: host
bias: "Podcast của Superwall (công cụ paywall), host Joseph Choi bán Consumer Club; Superwall, Rork, SpyTok là nhà tài trợ trong video. Daniel đang là Head of Product của Cal AI (vừa được MyFitnessPal mua), nên kể chuyện có lợi cho Cal AI. Số liệu Cal AI và các app khác là lời kể."
analyzed: 2026-11-15
cases:
- id: sway-ai
  depth: full
  product: "Sway AI (app phân tích hồ sơ hẹn hò bằng AI, chấm ảnh và góp ý prompt)"
  what: "Chấm và góp ý hồ sơ hẹn hò (ảnh, prompt) bằng AI, bán thêm gói photo pack AI"
  type: [mobile-app]
  customer: "Người dùng app hẹn hò muốn hồ sơ tốt hơn, sẵn sàng trả tiền để được góp ý riêng tư"
  founder: {who: Daniel, base: null, technical: false, team: "3 người: Daniel (design và product), Charles (iOS, làm app), Luis (marketing và vận hành)", background: "Design và product ở Snap, Robinhood (flow giao dịch crypto), Meta (team growth)"}
  revenue: {amount: 2000000, unit: usd, basis: arr, note: "Host nêu lúc mở đầu, Daniel không đọc từ dashboard", q: "Co-founder Sway AI, uh you boosted to $2 million ARR in 6 months.", ts: "00:01:49", evidence: claimed}
  pricing: "Gói năm làm mặc định để thu tiền trước; đã thử gói tuần nhưng tăng trưởng chậm; upsell photo pack AI (gói 1 ảnh và gói 10 ảnh, giá khoảng $14.99 và $49.99)"
  idea_origin: [revenue_scouting]
  scale_channels: [tiktok_organic, instagram_reels, paid_unspecified]
  community_at_discovery: {value: "Ý tưởng đến khi xem Reddit của Hinge, thấy người ta đăng ảnh hồ sơ xin góp ý; video không nói Daniel có dùng app hẹn hò không", insider: null, q: "If you just look up like the Hinge Reddit and you see like what people are searching on there", ts: "00:03:30"}
  demand_signal: {kind: paid, level: 8, what: "Trước khi có app, nhận $15 cho review hồ sơ thủ công qua DM Instagram (người ta trả tiền trước khi app tồn tại)", q: "asking for like $15 and if you send us screenshots of your profile, we'll give you like feedback manually. People were actually paying us", ts: "00:05:51"}
  prior_failures: {count: 1, what: "Ý tưởng cố vấn tài chính AI bị bỏ vì app tài chính khó kiếm tiền (video nói 'a lot of different ideas' nhưng không đếm)", q: "one of the ideas that we were exploring was like an AI personal fi- financial advisor but we learned that uh personal finance apps are a little bit hard to monetize", ts: "00:02:12"}
  unfair_advantage:
  - {value: cofounder, what: "Co-founder Charles là iOS engineer, làm app; Luis lo marketing và vận hành", q: "Yeah, two co-founders, Luis and Charles. And Charles is more like a iOS engineer, so he built the app.", ts: "00:14:42"}
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: {months: 6, value: "6 tháng từ 0 tới $2M ARR", q: "He took a dating profile analyzer app from zero to $2 million ARR in 6 months.", ts: "00:00:00"}
  first_users:
  - {channel: instagram_reels, what: "Co-founder mở Instagram đăng video gợi ý cách viết hồ sơ hẹn hò; vài tuần sau có video chạy tốt", q: "One of my co-founders started like an Instagram account and started posting like these videos.", ts: "00:05:01"}
  - {channel: own_audience, what: "Follower được mời DM để được review hồ sơ thủ công, rồi bị hỏi thanh toán", q: "we asked our followers to DM us for a profile review and then we'd ask them like for payment.", ts: "00:05:30"}
  build: null
- id: cal-ai
  depth: mention
  product: "Cal AI (app đếm calo bằng ảnh chụp)"
  what: "App theo dõi calo; Daniel làm Head of Product và kể Cal AI tăng trưởng chủ yếu qua influencer"
  type: [mobile-app]
  revenue: {amount: 2000000, unit: usd, basis: monthly, note: "'a couple million a month' lúc Daniel gia nhập (không nêu năm; không phải số dashboard)", q: "they were already doing like a couple million a month", ts: "00:25:49", evidence: claimed}
steps:
- stage: find-idea
  ts: "00:02:12"
  case: sway-ai
  what: "Thử ý tưởng cố vấn tài chính AI rồi bỏ vì app tài chính khó kiếm tiền; chuyển sang ngách hẹn hò vì app hẹn hò có nhiều app kiếm tiền cao (Tinder, Hinge)."
  tactic: s1-revenue-spy
- stage: find-idea
  ts: "00:03:30"
  case: sway-ai
  what: "Đọc Reddit của Hinge, thấy người ta đăng ảnh hồ sơ xin góp ý, và biến nhu cầu đó thành app chấm hồ sơ."
  tactic: s3-reddit-pain-mining
- stage: validate
  ts: "00:05:01"
  case: sway-ai
  what: "Trước khi có app: co-founder đăng Instagram video mẹo viết hồ sơ hẹn hò và gắn link đặt trước (pre-order) app ở bio."
  tactic: s8-content-demand-test
  tactic_note: "Đăng nội dung theo chủ đề trước khi có app, rồi gắn link pre-order"
- stage: validate
  ts: "00:05:30"
  case: sway-ai
  what: "Mời follower DM để được review hồ sơ thủ công, rồi xin thanh toán (khoảng $15) trước khi có app."
  tactic: s7-preorder-buy-button
  tactic_note: "Dịch vụ làm tay được trả tiền trước khi có app (không phải waitlist miễn phí)"
- stage: grow
  ts: "00:06:30"
  case: sway-ai
  what: "Lần đầu đăng TikTok: làm slideshow theo khuôn các video viral của một trang khác, nền thiết kế bằng Figma, chữ tự điền bằng Excel; batch cả tháng nội dung trong 1–2 giờ."
  tactic: g3-organic-content-formats
  tactic_note: "Chép khuôn nội dung đã viral của trang khác; batch bằng Excel tự điền"
- stage: grow
  ts: "00:08:10"
  case: sway-ai
  what: "Khởi động tài khoản mới bằng slide không thương hiệu, chỉ có CTA ở slide cuối; khi có traction mới thêm thương hiệu."
  tactic: g3-organic-content-formats
- stage: grow
  ts: "00:09:22"
  case: sway-ai
  what: "Một video TikTok có CTA được đăng đúng ngày Giáng sinh, lên vài triệu view và cho ngày doanh thu cao nhất đến lúc đó (khoảng 5–6K trong một ngày)."
  tactic: g3-organic-content-formats
- stage: grow
  ts: "00:10:45"
  case: sway-ai
  threshold: "30–40K/tháng organic trước khi chạy ads"
  what: "Doanh thu organic đạt khoảng 30–40K/tháng rồi mới chạy paid ads; sau khi chạy ads thì tăng trưởng dễ hơn nhiều."
  tactic: g6-paid-ads
  tactic_note: "Video không nêu nền tảng ads nào"
- stage: grow
  ts: "00:11:05"
  case: sway-ai
  what: "Hợp tác một influencer để làm video quảng cáo chạy trên trang của anh; video organic anh quảng bá mạnh được đem chạy quảng cáo và hiệu quả hơn."
  tactic: g7-creator-ops
  tactic_note: "Video không nói hình thức trả tiền cho influencer; chỉ một creator nên thiếu đa dạng creative"
- stage: monetize
  ts: "00:15:47"
  case: sway-ai
  what: "Onboarding cho xem kết quả mơ ước và hỏi câu cá nhân hoá trước paywall; paywall là carousel tám slide về quyền lợi của gói."
  tactic: g4-pricing-paywall
- stage: monetize
  ts: "00:18:39"
  case: sway-ai
  what: "Thêm credit cho người dùng quay lại flow nhiều lần, và bán photo pack AI (gói 1 ảnh và gói 10 ảnh) cho người chi tiêu nhiều."
  tactic: g4-pricing-paywall
- stage: monetize
  ts: "00:19:45"
  case: sway-ai
  what: "Đặt gói năm làm mặc định để thu tiền trước và đẩy tăng trưởng; đã thử gói tuần nhưng tăng trưởng chậm hơn hẳn."
  tactic: g4-pricing-paywall
- stage: grow
  ts: "00:35:33"
  case: cal-ai
  what: "Cal AI tăng trưởng chủ yếu qua influencer: mỗi video influencer đăng chiếu ba màn hình (camera, loading, chi tiết món ăn) để người xem hiểu app làm gì."
  tactic: g7-creator-ops
  tactic_note: "Làm việc với influencer fitness; video không nói hình thức trả tiền"
- stage: grow
  ts: "00:47:10"
  case: cal-ai
  what: "Cal AI bước ngoặt tăng trưởng khi bắt đầu chạy paid ads mạnh (video không nêu nền tảng)."
  tactic: g6-paid-ads
quotes:
- {ts: "00:02:12", who: Daniel, stage: find-idea, theme: [revenue-first], text: "we learned that uh personal finance apps are a little bit hard to monetize and so we were thinking of like what are some apps that do really good at monetization", vi: "Chúng tôi học được rằng app tài chính cá nhân khó kiếm tiền, nên tìm xem app nào kiếm tiền giỏi."}
- {ts: "00:03:30", who: Daniel, stage: find-idea, theme: [], text: "If you just look up like the Hinge Reddit and you see like what people are searching on there, you'll notice that people are just uploading pictures of themselves and their profile", vi: "Cứ vào Reddit của Hinge xem người ta tìm gì: bạn sẽ thấy họ đăng ảnh hồ sơ và xin góp ý."}
- {ts: "00:05:51", who: Daniel, stage: validate, theme: [sell-before-build], text: "People were actually paying us before we built the app to get feedback on their profile", vi: "Người ta thực sự trả tiền cho chúng tôi trước khi làm app, để được góp ý về hồ sơ."}
- {ts: "00:13:08", who: Daniel, stage: grow, theme: [], text: "Since we're only relying on like one influencer to create videos for us, it was hard to like get a a big variety of creative.", vi: "Chỉ dựa vào một influencer để làm video nên khó có nhiều dạng creative."}
- {ts: "00:17:56", who: Daniel, stage: find-idea, theme: [right-audience], text: "Um the idea is people don't want to ask like their friend or like people that they know, and so like using a product to get feedback in a more private way made more sense.", vi: "Ý tưởng là người ta không muốn hỏi bạn bè; dùng sản phẩm để góp ý riêng tư thì hợp lý hơn."}
- {ts: "00:19:45", who: Daniel, stage: monetize, theme: [revenue-first], text: "We default to the annual plan in order to like collect more revenue up front to fuel the growth.", vi: "Mặc định gói năm để thu nhiều tiền ngay từ đầu, nuôi tăng trưởng."}
- {ts: "00:23:55", who: Daniel, stage: monetize, theme: [], text: "And what we would get a lot of questions about is like what does this app even do?", vi: "Chúng tôi nhận rất nhiều câu hỏi kiểu 'app này làm gì, mình đang đăng ký cái gì'."}
- {ts: "00:38:55", who: Daniel, stage: find-idea, theme: [], text: "But if you have anecdotal evidence of like another big app, I think that's a helpful indicator that this is something that people will want.", vi: "Nếu đã có một app lớn làm chứng (dù chỉ là bằng chứng kể lại), đó là dấu hiệu hữu ích rằng người ta sẽ muốn."}
rules:
- {ts: "00:07:52", who: Joseph Choi, stage: grow, theme: [], text: "I feel like a lot of these slideshows are like I imagine they're kind of low converting cuz they don't actually plug the app, but yours actually plugs the app in every slide, not just like the last slide or anything.", vi: "Tôi đoán nhiều slideshow kiểu này chuyển đổi kém vì không gắn app; còn của Sway gắn app ở mọi slide, không chỉ slide cuối.", evidence: opinion}
- {ts: "00:14:42", who: Joseph Choi, stage: build, theme: [], text: "I feel like there's a lot of teams that kind of have the engineering and then the marketing, but then to actually build like a good product, you need someone It could be a third person or it could be like one one or the other of, you know, the marketing or the coding person, but someone needs to like worry about, okay, what is the user experience actually going to be like?", vi: "Nhiều đội có kỹ sư và marketing, nhưng làm sản phẩm tốt cần một người lo trải nghiệm người dùng sẽ thế nào.", evidence: opinion}
numbers:
- {ts: "00:18:53", metric: "phần doanh thu từ paywall upsell (lời Daniel: khoảng 11%)", value: 11, unit: percent, evidence: claimed}
- {ts: "00:10:45", metric: "doanh thu organic của Sway trước khi chạy ads (lời Daniel)", value: "30000–40000", unit: usd_per_month, evidence: claimed}
- {ts: "00:05:51", metric: "giá review hồ sơ thủ công trước khi có app", value: 15, unit: usd, evidence: claimed}
- {ts: "00:09:22", metric: "doanh thu một ngày từ video TikTok Giáng sinh", value: "5000–6000", unit: usd, evidence: claimed}
frameworks: [sell-before-build, content-before-product, organic-find-format-then-paid-scale, annual-plan-push, niche-down-proven-category]
idea_patterns: [niche-inside-hot-category]
---
## Một câu

Daniel (Sway AI, app chấm hồ sơ hẹn hò, sau đó làm Head of Product ở Cal AI) kể Sway đi từ 0 tới khoảng $2M ARR trong 6 tháng: thu $15 cho review hồ sơ thủ công trước khi có app, dùng slideshow TikTok và Instagram để kéo người dùng, chạy ads khi organic đã đạt 30–40K/tháng, và đặt gói năm làm mặc định.

## Bài học cho tôi

- Nhận tiền trước khi có app: tín hiệu mức 8 đến từ dịch vụ làm tay ($15, qua DM Instagram) (`00:05:51`).
- Chọn ngách có app đã kiếm tiền (hẹn hò: Tinder, Hinge), rồi làm một góc mới trong ngách đó (`00:02:12`).

## Đừng tin vội

- Host Joseph Choi bán Consumer Club, và podcast được tài trợ bởi Superwall, Rork, SpyTok; Daniel làm cho Cal AI (đã được MyFitnessPal mua). Kể chuyện có lợi cho các bên này.
- Các con số ($2M ARR, 30–40K/tháng organic, khoảng 11% doanh thu từ upsell, "a couple million a month" của Cal AI) đều là lời kể, không có dashboard. Video không nói chi phí ads hay ads chạy trên nền tảng nào.
- Điều kiện riêng khó chép: Sway có một co-founder iOS engineer và đã có sẵn đội ba người. Ngược lại, Daniel tự nói ngách hẹn hò khó với influencer marketing vì creator hẹn hò đang bán dịch vụ của họ, nên bước influencer ở Sway không dễ lặp lại.
