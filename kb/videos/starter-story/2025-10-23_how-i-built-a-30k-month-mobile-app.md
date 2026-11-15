---
schema: 2
video_id: T5zMsTw8GWQ
channel: starter-story
title: "How I built a $30K/month mobile app"
date: 2025-10-23
url: https://www.youtube.com/watch?v=T5zMsTw8GWQ
transcript: starter-story-kb/videos/2025-10-23_how-i-built-a-30k-month-mobile-app/transcript.md
kind: founder_case
speakers:
  - {name: John, role: founder}
  - {name: Pat Walls, role: host}
bias: "Video có đoạn quảng cáo Doula (LLC, kế toán) và mời dùng Starter Story Build; Starter Story bán dịch vụ và khoá học, nên kể câu chuyện app thành công là có lợi. Số $30K, 5,2 triệu lượt tải là lời founder kể."
analyzed: 2026-11-15
cases:
  - id: momego
    depth: full
    product: "Momego: app xem xe buýt/tàu theo thời gian thực, 160+ thành phố"
    what: "App cho hành khách xem xe trên bản đồ, bấm vào trạm để theo dõi xe chạy thật; khi đi tàu/xe thì bật trợ lý chuyến đi báo trễ và gợi ý tuyến thay thế"
    type: [mobile-app]
    customer: "Hành khách đi xe buýt/tàu ở nhiều thành phố; người ta tải app khi đang đứng ở trạm hoặc ga"
    founder: {who: John, base: Scotland, technical: true, team: solo, background: "Làm thiết kế đồ hoạ, tự học code; trước đó làm cho một công ty xe buýt ở Edinburgh"}
    revenue: {amount: 30000, unit: usd, basis: mrr, note: "Khoảng 30K MRR, gần như toàn bộ là gói đăng ký (founder kể)", q: "right now it's around $30,000 monthly recurring revenue", ts: "01:04", evidence: claimed}
    pricing: "Gói năm có dùng thử 7 ngày, gói tuần, gói trọn đời; ai đóng paywall được tặng 1 tuần Pro (reverse trial)"
    idea_origin: [own_pain]
    scale_channels: [app_store_search]
    community_at_discovery: {value: "Làm cho công ty xe buýt ở Edinburgh, phải đứng chờ xe 10–20 phút dưới mưa", insider: true, q: "At the time, I was working for a bus company in Edinburgh in Scotland.", ts: "02:06"}
    demand_signal: null
    prior_failures: null
    unfair_advantage:
      - {value: domain_expertise, what: "Làm trong công ty xe buýt, hiểu nỗi đau chờ xe", q: "At the time, I was working for a bus company in Edinburgh in Scotland.", ts: "02:06"}
      - {value: technical_skill, what: "Tự học code, có kinh nghiệm code web từ trước nhưng chưa làm app di động", q: "I turned to some of some of my coding experience in the past for websites.", ts: "03:10"}
    time_to_revenue: {first_dollar: null, to_1k_mrr: null, to_10k_mrr: null, to_current: null}
    first_users:
      - {channel: app_store_search, what: "ASO theo địa phương: thêm từ khoá theo thành phố (ví dụ 'New York subway', 'Chicago train') vào tiêu đề, subtitle, keyword; ảnh chụp riêng từng thành phố", q: "location specific keywords, things like New York subway, Chicago train.", ts: "04:57"}
    build:
      time: "Nhiều tháng cho bản đầu; sau đó vài tháng để làm lại cho gọn"
      cut: []
      q: "It was, you know, months of building, failing,"
      ts: "03:25"
steps:
  - stage: find-idea
    ts: "02:06"
    case: momego
    what: "Ý tưởng từ nỗi đau riêng: làm cho công ty xe buýt, muốn thấy xe trên bản đồ thay vì đứng chờ dưới mưa"
    tactic: s5-insider
    tactic_note: "Loại pain + nghề (làm trong công ty xe buýt)"
  - stage: grow
    ts: "04:57"
    case: momego
    what: "Thêm từ khoá theo thành phố vào tiêu đề, subtitle, keyword; mỗi bản địa hoá có ảnh chụp riêng; tải tăng rõ rệt"
    tactic: g2-aso-seo-organic
    tactic_note: "ASO theo địa phương (hyper-local)"
  - stage: grow
    ts: "06:02"
    case: momego
    what: "Tìm từ khoá bằng cách gõ đầu từ trên App Store xem gợi ý tự động; chọn từ ít người cạnh tranh để lên top 5"
    tactic: g2-aso-seo-organic
    tool: "gợi ý tìm kiếm App Store (video nêu thêm Apple Search Ads là lựa chọn khác)"
  - stage: grow
    ts: "06:48"
    case: momego
    what: "Xin đánh giá trong app đúng lúc người dùng thấy xe chạy trên bản đồ, để thứ hạng từ khoá tăng"
    tactic: g2-aso-seo-organic
    tactic_note: "Xin rating đúng 'khoảnh khắc vàng' để đẩy thứ hạng ASO"
  - stage: monetize
    ts: "08:54"
    case: momego
    what: "Quảng cáo banner mất hết sau đại dịch; làm lại app theo gói đăng ký, thêm tính năng cao cấp để người ta trả theo năm"
    tactic: g4-pricing-paywall
    tactic_note: "Chuyển từ banner ads sang subscription, đẩy gói năm"
  - stage: grow
    ts: "09:09"
    case: momego
    what: "A/B test onboarding và paywall qua ~10 thử nghiệm trong 2–3 tháng: tỉ lệ chuyển đổi từ 0.5% lên 8%, doanh thu từ ~8K lên hơn 30K/tháng"
    tactic: g4-pricing-paywall
    tactic_note: "A/B test paywall và onboarding, đo bằng analytics theo sự kiện"
  - stage: monetize
    ts: "10:28"
    case: momego
    what: "Paywall có 3 gói: dùng thử 7 ngày cho gói năm, gói tuần ít cam kết, gói trọn đời; đóng paywall thì tặng 1 tuần Pro"
    tactic: g4-pricing-paywall
    tactic_note: "Neo gói năm, reverse trial khi người dùng đóng paywall"
quotes:
  - {ts: "00:00", who: John, stage: find-idea, theme: [], text: "I had a problem I needed to solve, so I built it.", vi: "Tôi có một vấn đề cần giải quyết, nên tôi đã làm ra nó."}
  - {ts: "02:39", who: John, stage: find-idea, theme: [], text: "For any developer, any idea you have has to be something that you a problem that you yourself have and if it works for you, there's a good chance it'll work for lots of other people.", vi: "Với bất kỳ lập trình viên nào, ý tưởng phải là vấn đề mà chính mình gặp; nếu nó hợp với mình thì nhiều người khác cũng có thể cần."}
  - {ts: "13:06", who: John, stage: mindset, theme: [persistence], text: "you need something to keep you going. And solving your own problem is probably the best way to get past that block each time.", vi: "Bạn cần thứ gì đó để giữ bạn đi tiếp; giải quyết chính vấn đề của mình là cách tốt nhất để vượt qua bế tắc."}
  - {ts: "13:22", who: John, stage: grow, theme: [clarity], text: "And secondly, for the first couple of years, I was relying on kind of vanity metrics to see how well I was doing things like monthly active users. That wasn't really moving the needle. It was only when I moved to eventbased analytics that growth really happened.", vi: "Vài năm đầu tôi dựa vào chỉ số phù phiếm như MAU; nó không làm tăng trưởng. Chỉ khi chuyển sang analytics theo sự kiện thì tăng trưởng mới đến."}
  - {ts: "13:38", who: John, stage: grow, theme: [right-audience], text: "Being able to set up AB tests for different pay walls to see which one is more effective by trusting the data that you get from these kind of analytics, you will have a much better idea of who your customers are and what they want.", vi: "Chạy A/B test paywall và tin vào dữ liệu analytics sẽ giúp bạn hiểu khách hàng là ai và họ muốn gì."}
rules: []
numbers:
  - {ts: "01:04", metric: "MRR (chủ yếu gói đăng ký)", value: 30000, unit: usd_per_month, evidence: claimed}
  - {ts: "01:20", metric: "tổng lượt tải lũy kế", value: 5200000, unit: count, evidence: claimed}
  - {ts: "01:20", metric: "người dùng hoạt động hằng tháng", value: 400000, unit: count, evidence: claimed}
  - {ts: "08:38", metric: "doanh thu quảng cáo banner mỗi tháng trước đại dịch", value: 8000, unit: usd_per_month, evidence: claimed}
  - {ts: "09:09", metric: "tỉ lệ chuyển đổi paywall sau ~10 thử nghiệm (xuất phát từ 0.5%)", value: 8, unit: percent, evidence: claimed}
  - {ts: "12:33", metric: "chi phí ~20 server riêng mỗi tháng", value: 2500, unit: usd_per_month, evidence: claimed}
frameworks: [aso-hyperlocal-keywords, annual-plan-push]
idea_patterns: [utility-own-problem]
---

## Một câu

Graphic designer tự học code làm app xem xe buýt/tàu Momego, ý tưởng từ chuyện đứng chờ xe dưới mưa; tải về nhờ ASO theo từng thành phố (lời founder: 5 triệu lượt tải), doanh thu khoảng 30K/tháng nhờ gói đăng ký và A/B test paywall.

## Bài học cho tôi

- Ý tưởng bắt nguồn từ nỗi đau của chính mình, ngay trong nghề: chờ xe 10–20 phút dưới mưa (`02:06`).
- Tăng trưởng không tốn quảng cáo: từ khoá App Store theo từng thành phố, như 'New York subway', 'Chicago train' (`04:57`).

## Đừng tin vội

- Số $30K MRR, 5,2 triệu lượt tải, 400K MAU là lời founder kể, không có dashboard (evidence: claimed). Video không nói tỉ lệ người dùng trả tiền.
- Video không nói có bước kiểm nhu cầu trước khi build; founder chỉ nói "có vấn đề cần giải, nên làm". Vì vậy `demand_signal` để null.
- Video không nói thời gian từ lúc làm đến $30K bằng số tháng (chỉ nói "since 2017", "vài năm đầu"), nên G5 để null.
- Điều kiện riêng: app xem xe theo từng thành phố cần dữ liệu và bản địa hoá từng nơi; ngách này khó chép sang app không có nỗi đau tương tự.
- Video có quảng cáo Doula và nhắc kênh phụ Starter Story Build, đó là bias của nền tảng.
