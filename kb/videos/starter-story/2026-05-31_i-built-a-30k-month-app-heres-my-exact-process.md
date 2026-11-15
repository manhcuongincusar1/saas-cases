---
schema: 2
video_id: P4QodeA_lQ0
channel: starter-story
title: "I Built A $30K/Month App: Here's My Exact Process"
date: 2026-05-31
url: https://www.youtube.com/watch?v=P4QodeA_lQ0
transcript: starter-story-kb/videos/2026-05-31_i-built-a-30k-month-app-heres-my-exact-process/transcript.md
kind: founder_case
speakers: [{name: Benji, role: founder}, {name: Pat Walls, role: host}, {name: Gus, role: host}]
bias: "Benji quảng bá Snag (app của chính anh). Video và kênh Starter Story quảng bá Free iOS App Bootcamp (phễu bán khoá). Số dashboard được đọc trong video nhưng không kiểm chứng ngoài."
analyzed: 2026-11-15
cases:
  - id: snag
    depth: full
    product: "Snag (app tìm đồ miễn phí gần nhà)"
    what: "App iOS giúp người dùng tìm đồ miễn phí gần họ, có tìm kiếm, lọc và mục yêu thích"
    type: [mobile-app]
    customer: "Người muốn tìm đồ miễn phí gần nhà; trả gói subscription"
    founder: {who: Benji, base: "Không nêu rõ (mô tả video ghi sinh viên NYU; lớn lên ở châu Á)", technical: true, team: "10X Studio (Benji và nhóm)", background: "Đã bán công ty media đầu tiên với giá sáu chữ số; từng làm Congress, công ty đầu tư, quant research; làm hơn 45 app trong khoảng một năm"}
    revenue: {amount: 30000, unit: usd, basis: mrr, note: "Khoảng 30k MRR, Benji đọc từ dashboard theo yêu cầu của host", q: "we have around 30,000 US dollars in monthly recurring revenue", ts: "01:35", evidence: measured}
    pricing: "Subscription tuần, tháng, năm và một lần; không nêu giá cụ thể (Benji nói 'a few dollars a month')"
    idea_origin: []
    scale_channels: [ugc_creators, paid_tiktok, paid_meta]
    community_at_discovery: null
    demand_signal: null
    prior_failures: {count: 2, what: "Pillar và Hi GPT bị bỏ giữa chừng vì 'shiny object syndrome' (video nêu tên hai app này)", q: "basically stopped because I had shiny object syndrome", ts: "02:55"}
    unfair_advantage:
      - {value: prior_success, what: "Đã bán công ty media đầu tiên với giá sáu chữ số trước khi làm app", q: "sold my first media company for six figures", ts: "02:39"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 4, value: "khoảng 4 tháng từ lúc ra mắt tới 30k MRR", q: "had launched around 4 months ago and we've gone from zero to 30k MRR ever since", ts: "01:04"}
    first_users: []
    build: {time: "khoảng 4–5 giờ cho bản app có giao diện (quy trình chung của Benji, chưa tính back end)", cut: [], q: "The entire process usually takes around 4 to 5 hours to actually get a good app built out", ts: "03:56"}
steps:
  - {stage: find-idea, ts: "05:47", tactic: s1-revenue-spy, tool: "Sensor Tower", tactic_note: "Benji mô tả cách chung để tìm ý tưởng (video không nói Snag bắt nguồn từ đâu)", what: "Tìm ý tưởng bằng cách xem YouTube, Twitter để thấy người ta kiếm tiền từ gì, hoặc tìm app kiếm tiền trên Sensor Tower"}
  - {stage: find-idea, ts: "06:02", tactic: s11-copy-or-localize-proven, tactic_note: "Benji mô tả cách chung, không phải nguồn ý tưởng của Snag", what: "Chép app đã kiếm tiền rồi làm tốt hơn khoảng 10% về giao diện, marketing và phễu"}
  - {stage: build, ts: "03:41", what: "Bắt đầu từ marketing: viết giá trị đề xuất của app trước (đọc trong 3 giây), wireframe trên Figma, đưa thiết kế vào Claude Code trong IDE để code"}
  - {stage: build, ts: "10:40", what: "Làm app đơn tính năng kiểu wrapper API, đảm bảo app chạy được và có cách đăng nhập để qua duyệt App Store"}
  - {stage: monetize, ts: "01:50", tactic: g4-pricing-paywall, what: "Đa gói subscription: tuần, tháng, năm và một lần"}
  - {stage: monetize, ts: "05:16", tactic: g4-pricing-paywall, tool: "Superwall", tactic_note: "A/B test paywall bằng Superwall", what: "Dùng Superwall để A/B test paywall"}
  - {stage: retain, ts: "04:59", tactic: g5-retention, tool: "Loops", what: "Gửi email qua Loops cho người dùng đã churn để kéo họ quay lại app"}
  - {stage: grow, ts: "06:47", tactic: g7-creator-ops, tactic_note: "Benji nói về chiến dịch chung của mình; không nêu riêng cho Snag", what: "Tuyển UGC creator: liên hệ nhiều người rồi phỏng vấn từng người để lọc người có khả năng viral; trả monthly retainer cộng CPM và test video"}
  - {stage: grow, ts: "07:02", case: snag, tactic: g6-paid-ads, tool: "Meta Ads", threshold: "video trên 50k view; ROAS trên 1 là có lãi", what: "Với video creator đã đạt trên 50k view, chạy campaign test trên Meta để đo ROAS; khi ads mệt thì làm thêm creative"}
  - {stage: grow, ts: "08:52", case: snag, tactic: g6-paid-ads, tool: "TikTok Ads", cost: "$50/ngày để test", threshold: "ROAS trên 1 hoặc CTR cao", what: "Chạy paid trên video TikTok đã thắng: test $50/ngày rồi tăng dần 100, 200, 300 nếu ROAS tốt; một ad tốn khoảng $3.000 trước khi ROAS âm"}
  - {stage: grow, ts: "11:12", tactic: g3-organic-content-formats, tactic_note: "Benji nói về các app trước của mình ('my previous apps'), không riêng Snag", what: "Không có tiền thuê UGC thì tự quay video; Benji nói đã tự quay hàng nghìn video cho app trước, rồi thuê editor cắt theo gói"}
quotes:
  - {ts: "03:11", who: Benji, stage: mindset, theme: [focus-one-thing], text: "decided to really lock in and focus on building one specific product that could scale over time", vi: "Tôi quyết định tập trung vào đúng một sản phẩm có thể lớn dần theo thời gian."}
  - {ts: "03:11", who: Benji, stage: mindset, theme: [focus-one-thing], text: "Again, shiny object syndrome, just proceeded to build the next 43 products", vi: "Lại là hội chứng 'shiny object', tôi cứ thế làm tiếp 43 sản phẩm nữa."}
  - {ts: "06:17", who: Benji, stage: find-idea, theme: [], text: "So ideas don't really worth much if you cannot provide the product to the end user in a better way.", vi: "Ý tưởng không có giá trị nhiều nếu bạn không đưa sản phẩm tới người dùng theo cách tốt hơn."}
  - {ts: "12:12", who: Benji, stage: mindset, theme: [learn-from-others], text: "Definitely create your own luck and meet the right people.", vi: "Hãy tự tạo may mắn và gặp đúng người."}
rules:
  - {ts: "13:27", who: Gus, stage: mindset, theme: [builder-trap], text: "And this is how smart builders act. It's like instead of worrying about, is my idea not going to work? What are people going to think about me? Build apps.", vi: "Đó là cách người làm sản phẩm thông minh hành động: thay vì lo ý tưởng có thất bại không, hãy làm app.", evidence: opinion}
numbers:
  - {ts: "01:35", metric: "người dùng đã xác thực trên Snag", value: "trên 100.000", unit: count, evidence: measured}
  - {ts: "01:35", metric: "lượt chuyển đổi (conversions) trên Snag", value: 9000, unit: count, evidence: measured}
  - {ts: "01:35", metric: "tổng doanh thu gộp (total proceeds)", value: 80000, unit: usd, evidence: measured}
  - {ts: "02:07", metric: "số đánh giá trên App Store", value: "khoảng 3.300", unit: count, evidence: claimed}
  - {ts: "07:02", metric: "số creator tốt trên 100 người phỏng vấn (tỉ lệ khoảng 10%)", value: "9–10", unit: count, evidence: claimed}
  - {ts: "08:21", metric: "view của một video UGC (ví dụ soft-sell)", value: 240000, unit: views, evidence: claimed}
  - {ts: "08:21", metric: "doanh thu trực tiếp mỗi 100.000 view (theo Benji)", value: "1.000–2.000", unit: usd, evidence: claimed}
  - {ts: "09:22", metric: "tổng chi cho một ad TikTok trước khi ROAS âm", value: 3000, unit: usd, evidence: claimed}
---
## Một câu

Benji (20 tuổi, từng bán công ty media đầu tiên) làm Snag, app tìm đồ miễn phí gần nhà, lên khoảng 30k MRR sau khoảng 4 tháng. Video nói về UGC và paid ads nhưng không nói kênh nào mang phần lớn doanh thu của Snag.

## Bài học cho tôi

- Lọc creator bằng phỏng vấn (khoảng 9–10 trên 100 người), rồi chỉ chạy paid trên video đạt trên 50k view và ROAS trên 1 (`07:02`).
- Benji nói ông đã làm hơn 40 app và bỏ nhiều cái vì "shiny object syndrome", chỉ tập trung một sản phẩm mới ra 30k MRR (`03:11`, `02:55`).

## Đừng tin vội

- Nguồn có lợi ích: Benji quảng bá chính Snag, và phễu Free iOS App Bootcamp là của Starter Story. Số dashboard được đọc trong video nhưng không kiểm chứng ngoài.
- Thời gian "4–5 giờ" là quy trình chung của Benji, không riêng Snag, và chưa tính back end.
- Video không nói người dùng đầu tiên của Snag đến từ đâu, cũng không nêu tỉ trọng các kênh (UGC, Meta, TikTok) trong doanh thu.
- Benji đã có kinh nghiệm bán công ty trước và làm hơn 45 app, nên điều kiện này không dễ chép nguyên xi. Các app không thành công không được kể.
