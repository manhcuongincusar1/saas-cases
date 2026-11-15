---
schema: 2
video_id: oxr_Dz1vhdU
channel: superwall
title: '$16M AI CEOs: How to Make $1.3M/Month With AI Apps'
date: 2026-07-28
url: https://www.youtube.com/watch?v=oxr_Dz1vhdU
transcript: superwall/youtube-transcript/superwall/16m-ai-ceos-how-to-make-13mmonth-with-ai-apps/transcript.md
kind: expert_talk
speakers:
- name: Joseph Choi
  role: host
- name: Patrick
  role: expert
- name: Pablo
  role: expert
bias: Host Joseph Choy bán Consumer Club (Discord) và dinner cho founder; Superwall, Ror, paywallexperiments
  và WiseSam được quảng cáo trong video; WiseSam là sản phẩm của chính studio. Số liệu app khác là lời
  kể, chưa kiểm.
analyzed: 2026-11-15
cases:
- id: font-maker
  depth: mention
  product: Font Maker (biến chữ viết tay thành font bàn phím)
  what: App font bàn phím thuộc nhóm utility của studio; khoảng 7 triệu lượt tải tổng
  revenue:
    amount: 200000
    unit: other
    basis: monthly
    note: không nêu tiền tệ; founder nói about 200k a month
    q: This one makes um about 200k a month.
    ts: 00:08:47
    evidence: claimed
- id: litstick
  depth: mention
  product: LitStick (sticker iMessage)
  what: App biến thứ người dùng muốn thành sticker iMessage; studio sở hữu
  revenue:
    amount: 300000
    unit: other
    basis: monthly
    note: không nêu tiền tệ; founder nói north of 300K, tức trên 300k (cận dưới)
    q: this one's doing just uh north of 300K a month.
    ts: 00:08:58
    evidence: claimed
- id: celebs
  depth: mention
  product: Celebs (app tìm người giống người nổi tiếng)
  what: Upload ảnh để biết mình giống sao nào; studio mua sau khi đỉnh viral đã xuống, rồi tăng trưởng
    lại đều; nay sáu năm tuổi
  pricing: gói tuần; host nói khoảng $6.99 đến $14.99/tuần, founder không đính chính
- id: wisesam
  depth: mention
  product: WiseSam (agent trợ lý cá nhân kiểu OpenClaw, dễ dùng hơn)
  what: Agent cho người tiêu dùng; onboarding nhiều câu hỏi để cá nhân hoá; kênh iMessage/WhatsApp; sản
    phẩm mới, còn đang tìm góc đầu tư
  pricing: dùng thử 1 tuần $1, sau đó $10/tuần; huỷ bất cứ lúc nào; thanh toán qua Stripe ngay
steps:
- stage: find-idea
  ts: 00:09:38
  case: celebs
  what: Mua app đã qua đỉnh viral (lượt tải và doanh thu đang giảm, người bán không biết tăng tiếp) rồi
    tăng trưởng lại đều; chọn bằng dữ liệu hiệu suất.
  tactic: other
  tactic_note: Mua app đã sụt sau đỉnh viral thay vì tự nghĩ ý tưởng mới; tìm bằng dữ liệu, không bằng
    trải nghiệm
- stage: validate
  ts: 00:06:53
  what: Chạy quảng cáo cho app chưa tồn tại hoặc đang cân nhắc mua để đo nhu cầu; quảng cáo làm chuẩn
    hoá để so benchmark; kết hợp top-down (cấu trúc thị trường, mức sẵn sàng trả).
  tactic: other
  tactic_note: Chạy quảng cáo trả tiền cho app chưa có để đo nhu cầu bằng quảng cáo chuẩn hoá; không phải
    pre-order hay waitlist
- stage: monetize
  ts: 00:16:00
  case: celebs
  what: Bỏ paywall cuối onboarding (ngược quy tắc ngành) để đưa người dùng tới điểm hấp dẫn nhất nhanh
    hơn; doanh thu trên người dùng tăng.
  tactic: g4-pricing-paywall
  tactic_note: Bỏ paywall ở cuối onboarding, kiểm bằng AB test (test cũ có thể làm lại trong cấu hình
    mới)
- stage: grow
  ts: 00:13:28
  what: 'Vòng lặp: mua user (quảng cáo) → mỗi app chạy hàng chục AB test/tháng → tăng doanh thu trên mỗi
    người dùng → lại có tiền mua user; RPU danh mục tăng khoảng 3 lần trong 18 tháng.'
  tactic: g8-funnel-measurement
  tactic_note: Vòng lặp UA → AB test → RPU → tái đầu tư UA
- stage: grow
  ts: 00:15:27
  case: celebs
  what: 'Chạy khoảng 20 AB test trên Celebs: 10 trung tính, 5 tệ, 3 có vẻ thú vị, 2 tốt; test quy mô nhỏ
    trước rồi tăng dần.'
  tactic: g8-funnel-measurement
  tactic_note: Test quy mô nhỏ trước rồi tăng dần theo kết quả
- stage: grow
  ts: 00:19:11
  what: Mỗi AB test ghi lý do (giả thuyết, kết quả, bài học) thành backlog để làm dữ liệu cho AI agent.
  tactic: g8-funnel-measurement
  tactic_note: Gắn lý do (tag) cho từng AB test rồi lưu backlog giả thuyết-kết quả-bài học; đưa cho AI
    agent
- stage: grow
  ts: 00:04:13
  what: Chạy khoảng 4.000 video quảng cáo AI mỗi tháng, cộng hàng trăm playable và hàng nghìn static;
    khoảng 100 AB test/tháng.
  tactic: g6-paid-ads
  tactic_note: Quảng cáo trả tiền từ nhiều năm, nền tảng không nêu; chạy cả cho app chưa tồn tại
- stage: grow
  ts: 00:43:39
  what: Team quảng cáo 6 người nghĩ ý tưởng và chuẩn bị chất liệu; agency Pool Day làm phần lớn video
    editing; editor nội bộ và playable ads cho việc lẻ.
  tactic: g7-creator-ops
  tactic_note: Team quảng cáo nội bộ kết hợp agency edit video; người nghĩ ý tưởng, AI làm thực thi
- stage: grow
  ts: 00:50:18
  what: Dùng AI lọc video TikTok và quảng cáo từ ngành khác để lấy cảm hứng; creative analyst chuyển thành
    ý tưởng quảng cáo cho ngách.
  tool: Spy Talk
  tactic: g3-organic-content-formats
  tactic_note: Ý tưởng format/hook lấy từ ngành khác; không chép đối thủ dẫn đầu vì studio đã là leader
- stage: monetize
  ts: 00:27:53
  case: wisesam
  what: 'WiseSam: quảng cáo → onboarding nhiều câu hỏi để cá nhân hoá → gói dùng thử 1 tuần $1 rồi $10/tuần,
    huỷ bất cứ lúc nào; thanh toán Stripe ngay.'
  tool: Stripe
  threshold: $1 tuần đầu, sau đó $10/tuần
  tactic: g4-pricing-paywall
  tactic_note: Onboarding dài tạo ma sát có chủ đích, rồi trial giá thấp để thu tiền ngay
quotes: []
rules:
- ts: 00:11:07
  who: Patrick hoặc Pablo
  stage: find-idea
  theme:
  - revenue-first
  text: if we can buy an app and we can 20x its revenue and make a lot of money doing it
  vi: 'Tiêu chí mua: nếu có thể tăng gấp 20 lần doanh thu và kiếm nhiều tiền thì đáng mua.'
  evidence: opinion
- ts: 00:06:53
  who: Patrick hoặc Pablo
  stage: validate
  theme: []
  text: they're very standardized ads so that the data is as comparable as possible
  vi: Quảng cáo phải chuẩn hoá để dữ liệu so sánh được với nhau.
  evidence: opinion
- ts: 00:16:00
  who: Joseph Choi
  stage: grow
  theme: []
  text: I think a lot of teams AB test something once it doesn't work and they won't ever AB test it again
  vi: Nhiều đội test một lần, không ra kết quả rồi bỏ, không bao giờ test lại.
  evidence: opinion
- ts: 00:19:11
  who: Patrick hoặc Pablo
  stage: grow
  theme: []
  text: we try to give it a reason and that's also even more important nowadays that we try to feed all
    that information to an agent.
  vi: Mỗi test phải có lý do; ngày nay càng quan trọng vì đưa toàn bộ thông tin đó cho agent.
  evidence: opinion
- ts: 00:19:30
  who: Patrick hoặc Pablo
  stage: grow
  theme: []
  text: it's more of methodology and nearly a philosophy of continual testing which is the most important
  vi: Quan trọng nhất là phương pháp và tư duy test liên tục, không phải chiến thắng nhỏ lẻ.
  evidence: opinion
- ts: 00:23:11
  who: Patrick hoặc Pablo
  stage: monetize
  theme: []
  text: if you don't have that clarity keep your on boarding payable and maybe it's a hard payable
  vi: Nếu chưa rõ điểm tốt nhất để hỏi trả tiền thì giữ paywall ở onboarding, có thể là paywall cứng.
  evidence: opinion
- ts: 00:41:00
  who: Patrick hoặc Pablo
  stage: grow
  theme: []
  text: it's having a lot of human creativity in like coming up with the ad ideas
  vi: Ý tưởng quảng cáo là phần người làm; AI làm thực thi.
  evidence: opinion
- ts: 00:48:41
  who: Patrick hoặc Pablo
  stage: grow
  theme: []
  text: you do need this sort of mix of taste, data, and process to efficiently explore uh the the uh
    the search space.
  vi: Khám phá hiệu quả cần kết hợp gu (taste), dữ liệu và quy trình; brute force thì không đủ.
  evidence: opinion
numbers:
- ts: 00:04:13
  metric: video quảng cáo AI mỗi tháng
  value: 4000
  unit: count
  evidence: claimed
- ts: 00:04:13
  metric: AB test mỗi tháng (toàn danh mục)
  value: 100
  unit: count
  evidence: claimed
- ts: 00:03:42
  metric: doanh thu annualized của studio (không nêu tiền tệ)
  value: 16000000
  unit: annualized
  evidence: claimed
- ts: 00:08:31
  metric: lượt tải tổng Font Maker (không nêu tiền tệ, là lượt tải)
  value: 7000000
  unit: count
  evidence: claimed
- ts: 00:13:45
  metric: RPU trung bình danh mục tăng trong 18 tháng
  value: 3
  unit: lần
  evidence: claimed
- ts: 00:14:21
  metric: LTV:CAC trung bình danh mục
  value: 3
  unit: ratio
  evidence: claimed
- ts: 00:15:27
  metric: 'AB test: trong 20 test có 2 tốt, 3 thú vị, 5 tệ, 10 trung tính'
  value: 20
  unit: count
  evidence: claimed
- ts: 00:43:39
  metric: số người trong team quảng cáo
  value: 6
  unit: count
  evidence: claimed
frameworks:
- many-small-bets
idea_patterns: []
---

## Một câu

Studio khoảng 16 triệu doanh thu năm (lời founder) mua app đã qua đỉnh viral, đo bằng dữ liệu, chạy 4.000 video quảng cáo AI mỗi tháng và test liên tục; đây là mô hình mua và tăng trưởng app, không phải tự nghĩ ý tưởng.

## Bài học cho tôi

- Mỗi AB test nên có lý do (giả thuyết) và được ghi lại thành backlog; đây là cách biến "thắng một lần" thành bài học dùng lại (`00:19:11`).
- Tiêu chí mua app là khả năng tăng doanh thu gấp nhiều lần; app đã qua đỉnh viral có thể rẻ nhưng phải có lý do để tăng lại (`00:09:38`).

## Đừng tin vội

- Host bán Consumer Club và dinner, và Superwall, Ror, paywallexperiments, WiseSam đều là quảng cáo hoặc sản phẩm của chính studio; video là phễu cho nhiều thứ cùng lúc.
- Studio có vốn (1 triệu equity), 11–20 người, ngân sách quảng cáo lớn để test 4.000 video mỗi tháng; solo founder không sao chép được điều kiện này.
- Video không nói giá mua app, chi phí quảng cáo, ROAS hay CAC từng app; số liệu Font Maker, LitStick, Celebs là lời kể, chưa kiểm.
