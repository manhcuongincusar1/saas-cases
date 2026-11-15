---
schema: 2
video_id: PFfo4JySptw
channel: superwall
title: "0 to $300k/mo in 45 days with my ai app (just copy me)"
date: 2026-03-29
url: https://www.youtube.com/watch?v=PFfo4JySptw
transcript: superwall/youtube-transcript/superwall/0-to-300kmo-in-45-days-with-my-ai-app-just-copy-me/transcript.md
kind: founder_case
speakers:
  - {name: Dillion, role: founder}
  - {name: Joseph Choi, role: host}
bias: "Podcast của Superwall (công cụ paywall) và Joseph Choi (Consumer Club có phí tham gia; dinner cho app $100k/tháng). Video quảng cáo SpyTok ('tôi 100% vouch'). Số 300k MRR là lời founder kể, không có dashboard trên màn hình."
analyzed: 2026-11-15
cases:
  - id: halo-ai
    depth: full
    product: "Halo AI: app chỉnh và tạo ảnh bằng AI, bán theo tuần và năm; growth bằng UGC do creator đăng TikTok"
    what: "Người dùng tải ảnh lên, nhập prompt và nhận ảnh AI đã chỉnh; màn hình dashboard cho xem các mẫu (chân dung, phòng, tóc, hình xăm)"
    type: [mobile-app]
    customer: "Người dùng phổ thông muốn chỉnh hoặc tạo ảnh bằng AI; khách đến từ video TikTok do creator đăng"
    founder: {who: Dillion, base: null, technical: null, team: "hai đồng sáng lập (Dillion và Krishan) cộng với khoảng 85 creator làm UGC", background: "Làm startup toàn thời gian từ 2022, nhiều sản phẩm B2B và developer tools không thành; đây là app consumer đầu tiên"}
    revenue: {amount: 300000, unit: usd, basis: mrr, note: "MRR đạt 300k trong 45 ngày, rồi đi ngang ở mức này. Lời founder kể, không có dashboard trên màn hình", q: "Actually, we forecasted that it would plateau at 300k like in the very beginning, and actually hit exactly that that mark.", ts: "00:39:59", evidence: claimed}
    pricing: "Gói tuần $8.99 (có dùng thử miễn phí) là mặc định; gói năm đã thử rồi bỏ, đang thử lại"
    idea_origin: [timing_trigger]
    scale_channels: [ugc_creators]
    community_at_discovery: {value: "Đang làm nhiều sản phẩm cùng đối tác; đồng sáng lập để ý Gemini API mới ra; founder không nói mình thuộc nhóm khách của chỉnh ảnh AI", insider: false, q: "Krishan brought up that the Gemini API came out recently", ts: "00:03:17"}
    demand_signal: {kind: built_first, level: 0, what: "Build bản đầu 2–3 tuần rồi ra mắt; video không nêu tín hiệu nhu cầu nào trước đó", q: "we spent two or three weeks building the app and went live", ts: "00:03:17"}
    prior_failures: {count: null, what: "18 tháng ra nhiều sản phẩm thất bại, gần như không còn tiền trong tài khoản (video không nêu số sản phẩm)", q: "he had just spent 18 months launching failed products", ts: "00:00:00"}
    unfair_advantage:
      - {value: cofounder, what: "Có đồng sáng lập Krishan cùng làm sản phẩm trước đó", q: "My partner, Krishan, and I were working on a bunch of products", ts: "00:03:17"}
      - {value: capital, what: "Vay cá nhân khoảng $100k rồi đổ hết vào trả creator (vốn vay, không phải vốn có sẵn)", q: "The way we got by in the beginning was I took out a loan", ts: "00:48:20"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 1.5, value: "45 ngày từ lúc bắt đầu tới 300k MRR (lời host, founder xác nhận)", q: "You bootstrapped your first app to 300,000 MRR in 45 days", ts: "00:02:55"}
    first_users:
      - {channel: ugc_creators, what: "Bắt đầu UGC quanh lúc có $5 MRR đầu (founder tự test app); creator tăng từ khoảng 10 lên 25 rồi 85; video không nêu 10 người dùng đầu tiên đến từ đâu", q: "around then we also started doing UDC", ts: "00:04:19"}
    build:
      time: "2–3 tuần để build bản đầu"
      cut: []
      q: "we spent two or three weeks building the app and went live"
      ts: "00:03:17"
steps:
  - {stage: find-idea, ts: "00:03:17", case: halo-ai, what: "Đồng sáng lập đề xuất làm app dựa trên Gemini API vừa ra; hai người quyết định 'thử một phát' mà không nêu nghiên cứu nhu cầu.", tactic: s12-timing-shift, tactic_note: "API nền tảng mới (Gemini API) làm lý do làm app"}
  - {stage: launch, ts: "00:04:19", case: halo-ai, what: "Sau khoản $5 MRR đầu (chính founder test app), bắt đầu UGC: gom một nhóm người đăng video về app; lúc đầu tăng chậm, sau khi quen cách làm thì tăng nhanh.", tactic: g7-creator-ops, tactic_note: "Gom creator đăng video ngay khi app đã có doanh thu đầu tiên"}
  - {stage: grow, ts: "00:00:20", case: halo-ai, what: "Một creator đăng một TikTok trả lại 6x ROI; founder vay $100k cá nhân rồi đổ hết vào trả creator đăng tiếp.", tactic: g7-creator-ops, tactic_note: "Trả creator đăng video; lấy ROI của một video làm căn cứ rót vốn", threshold: "6x ROI (một video)", cost: "$100,000 vay cá nhân"}
  - {stage: grow, ts: "00:11:44", case: halo-ai, what: "Đăng tin tuyển UGC lên các nhóm Facebook và Reddit; nhận khoảng 500–600 hồ sơ; sàng lọc người đã làm UGC và ở Mỹ (hoặc dùng VPN Mỹ).", tactic: g7-creator-ops, tool: "Nhóm Facebook và Reddit về UGC"}
  - {stage: grow, ts: "00:12:26", case: halo-ai, what: "Trả trial: creator làm 5 video trong khoảng 5 ngày, mỗi video $20 (tổng $100); ai đạt mới được giữ.", tactic: g7-creator-ops, threshold: "$20/video", cost: "$100 mỗi creator trial"}
  - {stage: grow, ts: "00:15:52", case: halo-ai, what: "Đưa creator vào Discord, mỗi người một kênh riêng; trial đăng cùng một format trên 4 nền tảng; không đặt ngưỡng view tối thiểu để qua trial, mà đánh giá tính đều đặn, giao tiếp và cảm giác viral.", tactic: g7-creator-ops, tactic_note: "Quy trình trial và đánh giá creator qua Discord, không chỉ theo view"}
  - {stage: grow, ts: "00:22:17", case: halo-ai, what: "Một format duy nhất cho mọi creator: hook kỳ quặc (ảnh AI kèm caption trò đùa), demo app, màn hình loading hiện tên app to, rồi câu chuyện nhắn tin có twist.", tactic: g3-organic-content-formats, tactic_note: "Một format cố định cho mọi creator, không biến tấu"}
  - {stage: grow, ts: "00:25:47", case: halo-ai, what: "Khi một video viral, tự động gửi cho toàn bộ creator trong Discord để quay lại đúng video đó trên tài khoản của họ cùng ngày.", tactic: g7-creator-ops, tactic_note: "Nhân bản video viral qua toàn bộ creator bằng automation"}
  - {stage: grow, ts: "00:26:55", case: halo-ai, what: "Huấn luyện AI agent (OpenClaw) trên các video có trên 1 triệu view để làm coach và sinh kịch bản cho creator; nối TikTok API để lấy trend.", tactic: g7-creator-ops, tactic_note: "AI agent làm coach và sinh ý tưởng cho creator, không phải kênh đăng"}
  - {stage: monetize, ts: "00:40:52", case: halo-ai, what: "Paywall mặc định là gói tuần $8.99 có dùng thử miễn phí; gói năm từng thử rồi bỏ, đang thử lại.", tactic: g4-pricing-paywall, threshold: "$8.99/tuần", tactic_note: "Gói tuần là mặc định; gói năm đang thử lại"}
  - {stage: monetize, ts: "00:41:52", case: halo-ai, what: "Hai paywall trong onboarding: paywall đầu cho bỏ qua để vào app xem; paywall thứ hai chặn khi người dùng bấm gửi prompt. Kết hợp hai cái cho conversion cao hơn một cái (mỗi cái 16.5%).", tactic: g4-pricing-paywall, tactic_note: "Paywall mềm trước, paywall chặn khi người dùng thực hiện hành động"}
quotes:
  - {ts: "00:49:35", who: Dillion, stage: mindset, theme: [persistence], text: "So, the pressure behind us was we needed this to work. Otherwise, like we're screwed. Like this is this is like the the last uh Hail Mary.", vi: "Áp lực là phải làm cho được. Không thì coi như xong; đây là cơ hội cuối cùng."}
  - {ts: "00:47:15", who: Dillion, stage: mindset, theme: [], text: "Anyone can make apps and post TikToks and just like have a profitable growing business like very very quickly.", vi: "Ai cũng làm được app và đăng TikTok, rất nhanh có thể có một công việc kinh doanh có lãi đang tăng."}
  - {ts: "00:55:49", who: Dillion, stage: mindset, theme: [], text: "make the hard decision like as early as possible. As soon as you recognize something's not working or like you have to change course, don't delay that.", vi: "Đưa ra quyết định khó càng sớm càng tốt. Khi thấy có gì không ổn hoặc phải đổi hướng thì đừng trì hoãn."}
rules:
  - {ts: "00:43:58", who: Joseph Choi, stage: monetize, theme: [], text: "I feel like a lot of people just do like onboarding questions multiple choice hit with the paywall and then the people who aren't sure they just kind of they don't have anywhere to go.", vi: "Nhiều người chỉ làm câu hỏi onboarding trắc nghiệm rồi chặn bằng paywall; ai chưa chắc thì không có chỗ nào để đi.", evidence: opinion}
  - {ts: "00:51:35", who: Joseph Choi, stage: grow, theme: [], text: "Yeah, I feel like with mass UGC, you're able to get much better margins than something like influencer marketing.", vi: "UGC hàng loạt cho biên lợi nhuận tốt hơn influencer marketing, vì chỉ trả thưởng theo mốc.", evidence: opinion}
numbers:
  - {ts: "00:00:20", metric: "ROI một video của creator (trước khi vay)", value: 6, unit: ratio, evidence: claimed}
  - {ts: "00:01:05", metric: "lượt xem UGC sau 60 ngày", value: 600000000, unit: views, evidence: claimed}
  - {ts: "00:12:08", metric: "hồ sơ creator ứng tuyển", value: "500–600", unit: count, evidence: claimed}
  - {ts: "00:12:26", metric: "giá base mỗi video creator trial", value: 20, unit: usd, evidence: claimed}
  - {ts: "00:24:22", metric: "tỉ lệ video vượt 100k view (ước)", value: "5%", unit: ratio, evidence: claimed}
  - {ts: "00:39:59", metric: "MRR đạt và đi ngang", value: 300000, unit: usd_per_month, evidence: claimed}
  - {ts: "00:41:52", metric: "conversion của mỗi paywall onboarding", value: "16.5%", unit: ratio, evidence: claimed}
  - {ts: "00:48:04", metric: "margin hiện tại (founder tự nói, đang reinvest hết)", value: 0, unit: percent, evidence: claimed}
  - {ts: "00:50:25", metric: "ROAS/LTV:CAC thời kỳ đầu", value: "5–6", unit: ratio, evidence: claimed}
frameworks: []
idea_patterns: [snap-and-get-result]
---

## Một câu

Halo AI (app chỉnh ảnh AI, làm sau khi Gemini API ra): founder vay $100k để trả khoảng 85 creator đăng một format TikTok duy nhất; lời kể đạt 300k MRR trong 45 ngày, không có dashboard trên màn hình.

## Bài học cho tôi

- Trả creator theo cấu trúc base cộng thưởng mốc view: 29 trên 30 creator chọn cấu trúc có mốc dù trả thấp hơn (`00:33:45`).
- Chỉ dựa vào ROI 6x của một video để rót vốn vay là cược lớn; founder nói thẳng đó là cơ hội cuối cùng (`00:00:20`, `00:49:35`).

## Đừng tin vội

- Bias: Superwall và Joseph Choi bán dịch vụ và phễu (Consumer Club, dinner, SpyTok). Số 300k MRR và 600 triệu view là lời founder; không thấy dashboard.
- Mâu thuẫn trong video: founder nói "You don't need capital to do this" (`00:47:15`), nhưng chính họ vay $100k để trả creator (`00:48:20`). Không có vốn thì khó có 85 creator chạy liên tục.
- Lợi nhuận: founder nói đang reinvest hết, margin gần 0 (`00:48:04`); con số ~50% là host đoán, founder không xác nhận (`00:51:15`).
- Video không nói nền tảng paid ads (đang lên kế hoạch), không nói 10 người dùng đầu tiên đến từ đâu, không có tỉ lệ creator viral chính xác. Tỉ lệ 5% vượt 100k view là ước lượng.
- Nhịp tăng trưởng dựa vào 85 creator chạy liên tục cộng với vốn vay; người không có quỹ chạy trước khó sao chép đúng nhịp này.
