---
schema: 2
video_id: _a4ch3pk_U0
channel: superwall
title: "The Secret Behind Weirdly Viral Apps"
date: 2025-07-17
url: https://www.youtube.com/watch?v=_a4ch3pk_U0
transcript: superwall/youtube-transcript/superwall/the-secret-behind-weirdly-viral-apps/transcript.md
kind: expert_talk
speakers: [{name: Canyon, role: expert}, {name: Joseph Choi, role: host}]
bias: "Canyon là đồng sáng lập Sideshift, nền tảng bán creator UGC; video plug Sideshift, Consumer Club, Spytok và Superwall (Superwall tài trợ pod). Số liệu là lời kể, không có dashboard."
analyzed: 2026-11-15
cases:
- id: sideshift
  depth: mention
  product: "Sideshift: nền tảng kết nối sinh viên tìm việc UGC với công ty app (Canyon là đồng sáng lập)"
  what: "Chạy 'high volume organic' bằng creator sinh viên đăng video TikTok gần như mỗi ngày để kéo người dùng về nền tảng"
  type: [marketplace]
  customer: "Sinh viên tìm việc UGC (phía cung) và công ty app thuê creator (phía cầu)"
  founder: {who: Canyon, base: null, technical: null, team: null, background: "đồng sáng lập Sideshift (lời host giới thiệu)"}
  scale_channels: [tiktok_organic, ugc_creators]
  first_users:
  - {channel: word_of_mouth, what: "Đi trực tiếp tới 25 trường đại học để onboard 10–20k người dùng đầu; sau đó word of mouth trong trường. Từ vựng không có kênh 'trực tiếp tới trường', nên gắn word_of_mouth", q: "we physically went to 25 different college campuses in person to onboard kind of that first 10 to 20,000 users", ts: "00:40:43"}
- id: photogenic
  depth: mention
  product: "Photogenic: app AI làm album từ ảnh (ảnh tốt nghiệp, ảnh thẻ, ảnh chân dung), do một solo founder làm"
  what: "Lần đầu chạy organic: thuê một creator qua Sideshift và để creator tự chạy chiến lược; kết quả ~35 triệu view và lượt tải tăng ~10x mỗi tuần (lời Canyon)"
  type: [mobile-app]
  customer: "Người cần ảnh tốt nghiệp, ảnh thẻ, ảnh chân dung (use case do Canyon nêu)"
  founder: {who: "solo founder (không nêu tên)", base: null, technical: null, team: solo, background: "đã làm nhiều sản phẩm mobile; chưa từng chạy organic (lời Canyon)"}
  scale_channels: [tiktok_organic, ugc_creators]
- id: vert-ventures
  depth: mention
  product: "Vert Ventures: studio làm nhiều app; Astro (app chiêm tinh) và Haven (app học Kinh Thánh)"
  what: "Tìm format thắng trong organic rồi đưa chính format đó sang paid; creator đa dạng về giới và tuổi. Canyon nói cả hai app nằm trong top 5 ngách 'in and out'"
  type: [app-studio]
  customer: null
  founder: null
  scale_channels: [tiktok_organic, paid_unspecified]
steps:
- stage: grow
  ts: "00:00:00"
  case: sideshift
  what: "Chuyển sang 'high volume organic' khoảng 4 tháng trước: thuê creator đăng video TikTok nhiều, số người dùng nền tảng từ ~10k lên hơn 150k (lời Canyon)."
  tactic: g3-organic-content-formats
  tactic_note: "High-volume organic: nhiều bài và nhiều creator cùng lúc; chi phí khoảng 10k (lời Canyon)"
- stage: grow
  ts: "00:03:33"
  case: sideshift
  what: "5 creator đăng gần như mỗi ngày, phần lớn 2 bài/ngày; mất 2–3 tuần mới có format thắng, sau đó dồn vào format đó."
  tactic: g7-creator-ops
  threshold: "5 creator, khoảng 2 bài/ngày mỗi người"
  tactic_note: "Chấp nhận 2–3 tuần đầu chưa có format thắng; khi có thì nhân đôi format đó"
- stage: grow
  ts: "00:07:37"
  case: sideshift
  what: "Tạo không khí hỏi đáp trong phần bình luận để kéo engagement và đẩy video ra feed; sau đó plug sản phẩm kín đáo trong comment."
  tactic: g3-organic-content-formats
  tactic_note: "Engagement trong comment; CTA kín đáo, không nói thẳng sản phẩm"
- stage: grow
  ts: "00:10:21"
  case: sideshift
  what: "Brief cho creator: nói công ty làm gì bằng lời của mình, xác định đối tượng/persona, cho video viral mẫu và vài hook; giữ brief ngắn, không đưa brief hàng chục trang."
  tactic: g7-creator-ops
  tactic_note: "Brief ngắn một trang: công ty là gì, đối tượng, video mẫu, hook; quy định rõ nhắc công ty, không nhắc đối thủ"
- stage: grow
  ts: "00:14:01"
  case: sideshift
  what: "Trả creator theo kiểu hybrid: retainer cơ bản + khoảng $15–20 mỗi video + thưởng hiệu suất để kéo engagement."
  tactic: g7-creator-ops
  threshold: "$15–20 mỗi video + retainer"
  tactic_note: "Thưởng hiệu suất gắn với bình luận sau khi đăng; mô hình hybrid (lời Canyon, 'pretty common')"
- stage: grow
  ts: "00:18:17"
  case: sideshift
  what: "Warm-up tài khoản creator 3–5 ngày trước khi đăng; thường bắt đầu đăng vào thứ Hai. Creator phải xem, bình luận, thích như người thật trong ngách."
  tactic: g7-creator-ops
  threshold: "3–5 ngày warm-up"
  tactic_note: "Warm-up tài khoản TikTok theo hướng 'act human'; thời lượng tuỳ ngày onboard"
- stage: grow
  ts: "00:20:42"
  case: photogenic
  what: "Founder nhận khoảng 600 ứng viên qua Sideshift, mất nhiều thời gian xem tài khoản TikTok rồi chọn một creator có lịch sử viral và phản hồi tốt."
  tactic: g7-creator-ops
  threshold: "khoảng 600 ứng viên, chọn 1"
  tactic_note: "Tuyển creator theo lịch sử viral trên TikTok và độ phản hồi khi trò chuyện"
- stage: grow
  ts: "00:22:03"
  case: photogenic
  what: "Sau khi tuyển, founder để creator tự chạy chiến lược; các ý tưởng do founder đưa ra trước đó kém hiệu quả."
  tactic: g7-creator-ops
  tactic_note: "Cho creator có ý tưởng riêng quyền tự chạy; mức hands-on hay hands-off tuỳ từng người"
- stage: grow
  ts: "00:24:16"
  case: photogenic
  what: "Đăng cảnh AI làm sai (ví dụ hình có thêm chân) kèm sản phẩm; creator trả lời bình luận 'app là gì' rồi nhắc tên app."
  tactic: g3-organic-content-formats
  tactic_note: "Format 'AI làm sai' tạo nhiều engagement; CTA nhắc tên app trong comment"
- stage: grow
  ts: "00:27:21"
  case: vert-ventures
  what: "Tìm format thắng trong organic rồi đưa sang chạy quảng cáo trả tiền (paid); studio này làm việc này để phát huy kết quả organic."
  tactic: g6-paid-ads
  tactic_note: "Organic trước để tìm format, paid sau; video không nêu nền tảng paid nào"
- stage: validate
  ts: "00:31:06"
  what: "Canyon kiểm chứng ý tưởng bằng phân phối (UGC organic) trên sản phẩm đã ship: vài trăm người dùng, xem họ có ở lại và trả tiền không."
  tactic: other
  tactic_note: "Dùng phân phối (UGC organic) để kiểm chứng ý tưởng trên sản phẩm đã ship: vài trăm người dùng, xem họ có ở lại và trả tiền không"
- stage: validate
  ts: "00:33:36"
  what: "Chạy organic 2 tuần để đọc tín hiệu: nếu có view nhưng không chuyển đổi thì tìm nguyên nhân và đổi; nếu 2 tuần vẫn kém thì đặt lại thesis."
  tactic: other
  tactic_note: "Test organic 2 tuần: nếu có view nhưng không chuyển đổi thì tìm nguyên nhân và đổi; nếu 2 tuần vẫn kém thì nghi ngờ thesis và đổi sản phẩm"
- stage: grow
  ts: "00:33:18"
  what: "Với paid: thuê creator theo tuần, làm 5–10 format và chạy quảng cáo để xem format nào có người tải; dồn vào 1–2 format thắng rồi so với organic."
  tactic: g6-paid-ads
  threshold: "5–10 format mỗi tuần"
  tactic_note: "Test paid theo tuần: thuê creator làm 5–10 format, chạy quảng cáo để xem format nào có tải; so với organic"
quotes: []
rules:
- {ts: "00:04:49", who: Canyon, stage: grow, theme: [persistence], text: "sometimes it takes 300 posts before you find that winning format, but when you do, you know, you're able to just double down on that", vi: "Đôi khi phải đăng tới 300 bài mới có format thắng; khi tìm được thì dồn vào nó.", evidence: opinion}
- {ts: "00:07:11", who: Canyon, stage: grow, theme: [], text: "I think the beauty of UGC is you can get so many more reps and so much more practice for just such a cheap cost", vi: "UGC cho phép làm nhiều lượt hơn, luyện tập nhiều hơn với chi phí rẻ.", evidence: opinion}
- {ts: "00:10:21", who: Canyon, stage: grow, theme: [clarity], text: "So, I think one thing that is important to touch on is like who is your company?", vi: "Điều quan trọng trong brief là nói rõ công ty là gì.", evidence: opinion}
- {ts: "00:11:20", who: Canyon, stage: grow, theme: [right-audience], text: "they have a product that could really just be targeted at anyone and they don't focus on any specific niche", vi: "Sản phẩm 'ai cũng hợp' không chọn ngách thì nội dung nghe nhạt và không đẩy đi đúng người.", evidence: opinion}
- {ts: "00:12:00", who: Canyon, stage: grow, theme: [], text: "like link those videos, you know, give your creators a starting point", vi: "Đưa video viral cũ của mình hoặc đối thủ cho creator làm điểm xuất phát.", evidence: opinion}
- {ts: "00:14:01", who: Canyon, stage: grow, theme: [], text: "We kind of recommend like a hybrid model. So $15 to $20 per video with a base retainer is is pretty common.", vi: "Canyon khuyên mô hình hybrid: $15–20 mỗi video cộng retainer, là mức khá phổ biến.", evidence: opinion}
- {ts: "00:17:12", who: Canyon, stage: grow, theme: [], text: "You need you need to act human.", vi: "Creator phải hành xử như người thật trong ngách để tài khoản không bị coi là bot.", evidence: opinion}
- {ts: "00:24:16", who: Canyon, stage: grow, theme: [], text: "organic I I think is starting to become, you know, leaps and bounds more effective than even paid ads", vi: "Canyon cho rằng organic đang hiệu quả hơn cả quảng cáo trả tiền với nhiều sản phẩm consumer.", evidence: opinion}
- {ts: "00:28:05", who: Canyon, stage: grow, theme: [many-bets], text: "you just need to experiment and throw a ton of shots on goal", vi: "Cần thử nghiệm nhiều và ném thật nhiều cú sút.", evidence: opinion}
- {ts: "00:33:36", who: Canyon, stage: validate, theme: [], text: "I think like a two week timeline is pretty pretty sufficient.", vi: "Canyon thấy 2 tuần là đủ để có tín hiệu từ organic.", evidence: opinion}
- {ts: "00:35:30", who: Canyon, stage: grow, theme: [], text: "these algorithms reward quality content and so you no longer need to have hundreds of thousands of followers", vi: "Thuật toán thưởng nội dung chất lượng nên không cần hàng trăm nghìn follower.", evidence: opinion}
numbers:
- {ts: "00:01:02", metric: "người dùng (job seekers) trên Sideshift sau ~3–4 tháng organic (lời Canyon)", value: 150000, unit: count, evidence: claimed}
- {ts: "00:01:02", metric: "chi phí marketing ước tính cho playbook organic (lời Canyon: 'around 10k across the board')", value: 10000, unit: usd, evidence: claimed}
- {ts: "00:02:39", metric: "view chiến dịch gần nhất (lời Canyon: 16 triệu, rồi nói 20 triệu; khoảng 300 bài, lúc nói 60)", value: 16000000, unit: count, evidence: claimed}
- {ts: "00:20:42", metric: "số ứng viên creator của Photogenic", value: 600, unit: count, evidence: claimed}
- {ts: "00:22:26", metric: "tổng view của creator Photogenic (lời Canyon: '40 46 posts'; host nói 50 video)", value: 35000000, unit: count, evidence: claimed}
- {ts: "00:22:59", metric: "lượt tải tăng mỗi tuần sau khi chạy organic (Photogenic)", value: 10, unit: x, evidence: claimed}
- {ts: "00:23:27", metric: "tỉ lệ tải trên App Store: trước organic 5–10%, sau organic trên 50% (Photogenic)", value: ">50", unit: percent, evidence: claimed}
frameworks: [organic-find-format-then-paid-scale, many-small-bets]
idea_patterns: []
---

## Một câu

Canyon (đồng sáng lập Sideshift) kể cách đẩy app bằng UGC organic: nhiều creator đăng video gần như mỗi ngày, chờ 2–3 tuần mới có format thắng rồi dồn vào format đó; brief ngắn và thù lao hybrid là cách quản creator. Số liệu chủ yếu là lời kể.

## Bài học cho tôi

- Đừng kỳ vọng format thắng ngay: thường phải 2–3 tuần, có lần 300 bài mới ra, rồi dồn vào format đó (`00:03:33`, `00:04:49`).
- Brief cho creator ngắn, nói rõ công ty làm gì và đối tượng là ai; trả hybrid khoảng $15–20 mỗi video cộng retainer và thưởng hiệu suất (`00:10:21`, `00:14:01`).

## Đừng tin vội

- Phễu bán: Canyon là đồng sáng lập nền tảng Sideshift, và video plug Sideshift, Consumer Club, Spytok, Superwall. Mọi con số (150k người dùng, 16–20 triệu view, 35 triệu view, tỉ lệ tải trên 50%) là lời kể, không có dashboard; chính Canyon nói lộn số bài và số view.
- Chỉ kể case thắng (Photogenic, Vert Ventures). Các creator không ra format thắng không được nhắc, nên đây là survivor bias.
- Photogenic và Vert Ventures là case do Canyon kể, không có founder nào nói; không có doanh thu, không có chi phí quảng cáo cụ thể.
- Điều kiện riêng: Sideshift có 25 trường đại học và đội ngũ đi trực tiếp để có 10–20k người dùng đầu (lời Canyon); solo founder không có kênh này khó sao chép y nguyên.
- Video không nói: giá bán, doanh thu của Sideshift, tỉ lệ creator thắng trên tổng số creator, và chi phí paid cụ thể của Vert Ventures.
