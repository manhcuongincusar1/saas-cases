---
schema: 2
video_id: DPb-M0Vt4uI
channel: starter-story
title: I Make $50K Per Month Working 5 Hours A Week
date: 2026-07-23
url: https://www.youtube.com/watch?v=DPb-M0Vt4uI
transcript: starter-story-kb/videos/2026-07-23_i-make-50k-per-month-working-5-hours-a-week/transcript.md
kind: founder_case
speakers:
- name: Timo
  role: founder
- name: Pat Walls
  role: host
- name: Gus
  role: host
bias: Starter Story có cheat sheet 'Mobile App Growth' miễn phí (link trong mô tả và giữa video) làm phễu;
  founder bán app và kể cách chạy ads; số liệu tự báo, không thấy dashboard được mở; ChartDetector là
  app của chính founder.
analyzed: 2026-11-15
cases:
- id: chartdetector
  depth: full
  product: ChartDetector AI (chụp ảnh biểu đồ chứng khoán/crypto, AI phân tích hướng đi)
  what: 'App iOS/mobile: người dùng chụp ảnh biểu đồ, AI đưa gợi ý hướng đi; gói tuần $12.99, gói 6 tháng
    $59.99, paywall cứng không dùng thử'
  type:
  - mobile-app
  customer: Người xem biểu đồ chứng khoán và crypto
  founder:
    who: Timo
    base: null
    technical: true
    team: '2 người: Timo và anh/em trai'
    background: Software engineer 9-5 ở hãng xe lớn tại Đức; nghỉ việc sau 6 tháng làm app
  revenue:
    amount: 56000
    unit: usd
    basis: monthly
    note: doanh thu hiện tại theo lời founder (intro nói 'more than 50K'); không thấy dashboard được mở
    q: We are currently at $56,000 per month
    ts: 01:51
    evidence: claimed
  pricing: Gói tuần $12.99; gói 6 tháng $59.99; hard paywall, không free trial
  idea_origin:
  - timing_trigger
  scale_channels:
  - paid_tiktok
  community_at_discovery: null
  demand_signal: null
  prior_failures:
    count: null
    what: Đã thử nhiều mô hình kinh doanh khác trước khi app này chạy (không nêu số)
    q: tried a lot of different businesses but mobile apps were the first thing that really worked out
    ts: 03:08
  unfair_advantage:
  - value: technical_skill
    what: Từng là software engineer 9-5 ở hãng xe lớn ở Đức
    q: Before I started this app I was working a 9-5 as a software engineer at a big car brand in Germany.
    ts: 02:53
  - value: cofounder
    what: Anh/em trai cùng khởi động và làm app
    q: Me and my brother launched the app a little over a year ago
    ts: 00:49
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 13
      value: 13 tháng từ lúc ra mắt tới nay
      q: last 13 months, we've gone from zero to more than 90K in downloads
      ts: 01:05
  first_users:
  - channel: paid_tiktok
    what: Chạy quảng cáo TikTok trả tiền là kênh chính từ đầu
    q: Essentially, what we are doing is paid ads.
    ts: 04:23
  - channel: paid_tiktok
    what: Video quảng cáo TikTok kiểu demo app; một video tạo hơn 15K doanh thu, gần 5 triệu view
    q: This ad alone generated us over $15,000 in
    ts: 05:27
  build: null
steps:
- stage: find-idea
  ts: 03:23
  case: chartdetector
  what: 'Ý tưởng từ tính năng upload ảnh mới của ChatGPT: làm bot Telegram phân tích biểu đồ, rồi chuyển
    thành app di động.'
  tactic: s12-timing-shift
  tactic_note: 'Bắt sóng tính năng AI mới ra (timing_trigger): thử Telegram bot trước rồi làm app'
- stage: grow
  ts: 04:23
  case: chartdetector
  what: 'Chạy quảng cáo trả tiền làm kênh chính; mục tiêu là chi cho một lượt tải thấp hơn doanh thu trung
    bình mỗi người dùng (ví dụ $1.50 mỗi lượt tải, $3 mỗi người: ROAS 2x).'
  tactic: g6-paid-ads
  tactic_note: Quảng cáo trả tiền TikTok từ đầu; theo dõi ROAS, không chạy ads cho lượt tải đơn thuần
- stage: grow
  ts: 05:27
  case: chartdetector
  what: Video quảng cáo TikTok chỉ cho thấy app đang được dùng (demo thật); video tốt nhất tạo hơn 15K
    doanh thu.
  tactic: g3-organic-content-formats
  tactic_note: Format quảng cáo 'demo app' (người dùng dùng app trực tiếp), không phải diễn kịch
- stage: monetize
  ts: 06:46
  case: chartdetector
  what: Trước khi chạy ads, làm onboarding bán kết quả của app, có nhiều social proof; tham khảo onboarding
    app thành công qua Screens; paywall cứng không free trial.
  tactic: g4-pricing-paywall
  tactic_note: Onboarding bán kết quả + social proof; hard paywall không free trial để thu tiền ngay khi
    chạy ads
  tool: Screens
- stage: launch
  ts: 07:34
  case: chartdetector
  what: Tạo TikTok Business Manager; tích hợp AppsFlyer (MMP) để gửi dữ liệu mua hàng về TikTok; thuê
    freelancer Upwork để cài đặt vì dễ cấu hình sai.
  tactic: g8-funnel-measurement
  tactic_note: 'Thiết lập tracking: MMP (AppsFlyer) gắn sự kiện mua hàng vào TikTok; thuê freelancer Upwork
    cài đặt'
  tool: AppsFlyer
- stage: grow
  ts: 08:05
  case: chartdetector
  what: Chạy chiến dịch Smart Plus với ít nhất 6 video; tối ưu theo subscription event (không theo install);
    ngân sách tối thiểu $50 mỗi ngày; targeting rộng, chỉ chọn quốc gia; thử nước khác thay vì Mỹ.
  tactic: g6-paid-ads
  tactic_note: Smart Plus, tối ưu subscription event, ngân sách ~$50/ngày, targeting rộng; để chiến dịch
    7 ngày học trước khi đổi
  threshold: 6 video để bắt đầu; ngân sách tối thiểu $50/ngày
- stage: grow
  ts: 09:57
  case: chartdetector
  what: 'Theo dõi ROAS mỗi tuần: ổn định và có lãi thì tăng ngân sách, không lãi thì làm video mới; tăng
    ngân sách không quá 20% mỗi 3 ngày; luôn có pipeline video mới để chống mỏi creative.'
  tactic: g8-funnel-measurement
  tactic_note: Quyết định tăng ngân sách bằng ROAS hàng tuần; chống creative fatigue bằng pipeline video
    mới
quotes:
- ts: 02:53
  who: Timo
  stage: mindset
  theme:
  - persistence
  text: we both always wanted to start a business and tried a lot of different businesses but mobile apps
    were the first thing that really worked out and allowed us to quit our jobs and pursue this full time
  vi: Hai anh em luôn muốn kinh doanh và thử nhiều thứ; app di động là thứ đầu tiên thực sự chạy, cho
    phép nghỉ việc làm toàn thời gian.
- ts: '11:50'
  who: Timo
  stage: mindset
  theme:
  - action-over-research
  text: I would tell you I recommend you to start now the execution, because I always watched too many
    YouTube videos and procrastinated, and I thought I was productive.
  vi: Hãy bắt đầu làm ngay; tôi xem quá nhiều video YouTube, trì hoãn, và tưởng mình đang năng suất.
rules:
- ts: 06:16
  who: Pat Walls hoặc Gus
  stage: grow
  theme: []
  text: benefit of paid ads is that you don't spend a whole lot of time on it.
  vi: Lợi ích của ads trả tiền là không tốn nhiều thời gian; host cho rằng con số 25% biên lợi nhuận là
    bình thường với ads.
  evidence: opinion
- ts: '12:54'
  who: Pat Walls hoặc Gus
  stage: grow
  theme: []
  text: But what's so genius about this is it's doing all the work for you.
  vi: Chạy ads trả tiền là để công cụ làm việc thay mình; đổi lại biên lợi nhuận thấp hơn.
  evidence: opinion
numbers:
- ts: 01:05
  metric: tổng doanh thu từ khi ra mắt (tự báo)
  value: 260000
  unit: lifetime_usd
  evidence: claimed
- ts: 01:05
  metric: lượt tải trong 13 tháng
  value: 90000
  unit: count
  evidence: claimed
- ts: 01:51
  metric: lượt tải mỗi tháng
  value: 13–14k
  unit: count_per_month
  evidence: claimed
- ts: 02:06
  metric: lượt xem 30 ngày gần nhất
  value: 7800000
  unit: views
  evidence: claimed
- ts: 05:58
  metric: doanh thu tháng 4 (tự báo)
  value: 43700
  unit: usd_per_month
  evidence: claimed
- ts: 05:58
  metric: chi quảng cáo mỗi tháng (ước lượng)
  value: 20000
  unit: usd_per_month
  evidence: claimed
- ts: '11:35'
  metric: chi TikTok Ads mỗi tháng (hiện tại)
  value: 18000
  unit: usd_per_month
  evidence: claimed
frameworks: []
idea_patterns:
- snap-and-get-result
---

## Một câu

Timo và anh/em trai làm ChartDetector AI (chụp ảnh biểu đồ, AI gợi ý hướng đi), khoảng 56K/tháng theo lời tự báo nhờ quảng cáo TikTok trả tiền, tối ưu theo subscription; founder nói chỉ làm app khoảng 20 giờ/tháng.

## Bài học cho tôi

- Chạy ads từ đầu với paywall cứng, không free trial, và đo bằng ROAS: chi cho một lượt tải thấp hơn doanh thu trung bình mỗi người (`04:23`, `07:17`).
- Tối ưu chiến dịch theo sự kiện mua (subscription) thay vì lượt cài, và tăng ngân sách chậm (không quá 20% mỗi 3 ngày) để không quay lại giai đoạn học (`08:53`, `10:12`).

## Đừng tin vội

- Doanh thu, lượt tải và chi quảng cáo đều là lời tự báo; video không mở dashboard; tháng 4 là $43,700 với chi ads ~$20K và biên lợi nhuận ~25% sau phí Apple 15% (`05:58`), chưa kiểm chéo.
- Mô hình này cần vốn để chi $18–20K/tháng cho ads trước khi có lãi; video không nói chi phí ban đầu, ROAS thực tế, CAC hay thời gian hoà vốn của chiến dịch.
- Founder là software engineer nên tự làm được app; video không nói thời gian build; cheat sheet miễn phí là phễu của Starter Story. Transcript tự động ghi tên là "Teemo", tiêu đề và mô tả ghi "Timo".
