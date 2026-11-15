---
schema: 2
video_id: npcL7oRZQlI
channel: starter-story
title: "How I Built It: $9K/Month Micro-SaaS"
date: 2025-06-11
url: https://www.youtube.com/watch?v=npcL7oRZQlI
transcript: starter-story-kb/videos/2025-06-11_how-i-built-it-9k-month-micro-saas/transcript.md
kind: founder_case
speakers: [{name: Leandro, role: founder}, {name: Pat Walls, role: host}]
bias: "Monday.com trả tiền cho đoạn quảng cáo marketplace giữa video; Starter Story Build quảng bá cuối video. Founder được lợi khi thành case nổi."
analyzed: 2026-11-15
cases:
  - id: sync2sheets
    depth: full
    product: "Sync2sheets: add-on Google Sheets đồng bộ dữ liệu Notion vào bảng tính"
    what: "Add-on chạy trên Google Sheets, đưa cơ sở dữ liệu Notion vào Sheets; làm đúng một việc"
    type: [workspace-addon]
    customer: "Người dùng Notion cần làm việc với dữ liệu trong Google Sheets (video nói hơn 450 khách trả tiền)"
    founder: {who: Leandro, base: "Buenos Aires, Argentina", technical: true, team: null, background: "Học kỹ thuật điện tử rồi tự học JavaScript; freelance nhiều năm trước khi tự làm sản phẩm"}
    revenue: {amount: 9000, unit: usd, basis: monthly, note: "Host Pat Walls nêu 9.000 USD/tháng; Leandro không xác nhận con số này, chỉ nói lifetime khoảng 120k ('probably')", q: "you built a plugin that makes $9,000 a month", ts: "01:02", evidence: claimed}
    pricing: "Trước có gói miễn phí; sau đó bỏ hẳn gói miễn phí. Video không nêu giá hay các gói cụ thể."
    idea_origin: [domain_expertise, timing_trigger]
    scale_channels: [platform_marketplace, seo, reddit]
    community_at_discovery: {value: "Đang làm tích hợp Google Sheets với một dịch vụ khác, dùng Sheets API, nên thấy khoảng trống khi Notion ra API chính thức", insider: true, q: "I was building an integration between Google Sheets and", ts: "01:36"}
    demand_signal: {kind: self_reported_pain_or_free_waitlist, level: 4, what: "Trên Reddit (subreddit Notion) thấy nhiều người muốn xuất dữ liệu Notion ra Sheets, trước khi build MVP", q: "I found a lot of people like trying to export the information from notion into sheets", ts: "02:23"}
    prior_failures: null
    unfair_advantage:
      - {value: domain_expertise, what: "Đã làm nhiều với Sheets API trước khi có ý tưởng", q: "I was working with the sheets API", ts: "01:53"}
      - {value: technical_skill, what: "Tự học JavaScript và biết code trước khi nghỉ việc", q: "I already know how to code", ts: "04:12"}
      - {value: capital, what: "Có chút tiền tiết kiệm trước khi nghỉ làm freelance", q: "I already have some savings", ts: "04:12"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 48, value: "khoảng 4 năm từ lúc làm sản phẩm tới nay", q: "lifetime revenue probably around 120k for the last four years", ts: "01:20"}
    first_users:
      - {channel: platform_marketplace, what: "Đưa lên marketplace của Google Workspace trước; founder nói đây là nguồn cài đặt đầu tiên quan trọng nhất", q: "So, the first source of installs was of course the marketplace", ts: "09:52"}
      - {channel: reddit, what: "Đăng vào nhiều nhóm lớn liên quan Notion và Reddit, trò chuyện trong nhóm và DM để có người thử đầu tiên (video không nói cụ thể nhóm nào)", q: "I started to spam a lot of famous groups related to notion and Reddit", ts: "09:06"}
    build: {time: "2 tuần cho bản đầu, không dùng AI, chỉ tra Stack Overflow và Google", cut: ["Định dạng dữ liệu, dropdown, kéo và ẩn cột: để sau khi bản đầu chỉ chuyển được dữ liệu"], q: "it took me yeah two two weeks no AI", ts: "04:58"}
steps:
  - stage: find-idea
    ts: "01:53"
    case: sync2sheets
    what: "Khi làm tích hợp Sheets, Notion ra API chính thức; Leandro thấy khoảng trống giữa nhu cầu người dùng và những gì Notion có sẵn."
    tactic: s12-timing-shift
    tactic_note: "Notion vừa ra API chính thức, tạo khoảng trống cho tích hợp Sheets"
  - stage: validate
    ts: "02:08"
    case: sync2sheets
    what: "Vào subreddit Notion, tìm từ khoá (sheets, Google sheets, excel, CSV) và thấy nhiều người muốn đưa dữ liệu Notion ra Sheets."
    tactic: s3-reddit-pain-mining
  - stage: validate
    ts: "05:46"
    case: sync2sheets
    what: "Trước khi build: xem đã có sản phẩm tương tự chưa và bảng giá của họ để ước tiềm năng; không tìm được góc khác biệt thì bỏ."
    tactic: other
    tactic_note: "Kiểm đối thủ và bảng giá của họ trước khi build"
  - stage: build
    ts: "06:49"
    case: sync2sheets
    what: "Bản đầu chỉ chuyển dữ liệu từ Notion sang Sheets, chưa định dạng; sau đó thêm định dạng giống Notion, dropdown, kéo và ẩn cột."
  - stage: launch
    ts: "09:06"
    case: sync2sheets
    what: "Đăng trong nhiều nhóm lớn về Notion và Reddit; trò chuyện trong nhóm và DM để có người dùng thử đầu tiên."
    tactic: g1-first-10-users
  - stage: launch
    ts: "09:36"
    case: sync2sheets
    what: "Đặt khung chat trên landing page để trò chuyện trực tiếp với khách và hiểu họ cần gì."
    tactic: other
    tactic_note: "Chat trực tiếp trên landing page, không phải phỏng vấn có cấu trúc"
  - stage: launch
    ts: "09:52"
    case: sync2sheets
    what: "Đưa lên marketplace của Google Workspace; đây là nguồn cài đặt đầu tiên quan trọng nhất."
    tactic: g9-launch-platforms
  - stage: grow
    ts: "09:52"
    case: sync2sheets
    what: "Nhận ra cần làm SEO: viết blog về Notion và Google Sheets; hiện là một trong các kênh traffic chính."
    tactic: g2-aso-seo-organic
  - stage: grow
    ts: "10:08"
    case: sync2sheets
    what: "Theo dõi từ khoá trên Reddit bằng F5Bot; khi có bài mới thì vào trả lời, chỉ giới thiệu sản phẩm khi thật sự giúp được, không spam."
    tactic: other
    tool: "F5Bot"
    tactic_note: "Theo dõi từ khoá Reddit rồi trả lời hữu ích, nêu mình là founder"
  - stage: grow
    ts: "10:41"
    case: sync2sheets
    what: "Launch trên Product Hunt khoảng một năm rưỡi sau khi ra mắt; mang traffic nhưng không thành khách trả tiền."
    tactic: g9-launch-platforms
  - stage: grow
    ts: "10:56"
    case: sync2sheets
    what: "Đăng Hacker News và lên trang chủ; traffic tăng vọt và có backlink nhưng không thành khách trả tiền."
    tactic: other
    tactic_note: "Hacker News front page: traffic và backlink, không ra khách trả tiền"
  - stage: monetize
    ts: "12:47"
    case: sync2sheets
    what: "Bỏ hẳn gói miễn phí vì nhiều người chỉ dùng gói free và thấy đủ dùng; sau đó số liệu tăng từ 5K lên 8K trong vài tháng (video không nói đơn vị)."
    tactic: g4-pricing-paywall
quotes:
  - {ts: "06:17", who: Leandro, stage: validate, theme: [], text: "If I can't find that angle, I maybe look for something else because if you're not able to differentiate yourself, it's going to be hard to enter into the market.", vi: "Nếu không tìm được góc khác biệt, tôi có thể đổi ý tưởng, vì không khác biệt thì khó vào thị trường."}
  - {ts: "09:36", who: Leandro, stage: launch, theme: [right-audience], text: "because that way you can have real conversations with customers and with users and try to understand what they need.", vi: "Vì như vậy bạn trò chuyện thật với khách và người dùng, và hiểu họ cần gì."}
  - {ts: "14:18", who: Leandro, stage: validate, theme: [revenue-first], text: "Do not waste time building something that no one is going to be willing to pay for.", vi: "Đừng mất thời gian build thứ mà không ai chịu trả tiền."}
rules: []
numbers:
  - {ts: "01:02", metric: "người dùng đã đăng ký (sign-up)", value: 70000, unit: count, evidence: claimed}
  - {ts: "01:20", metric: "khách trả tiền", value: 450, unit: count, evidence: claimed}
  - {ts: "01:20", metric: "lượt truy cập mỗi tháng", value: 5000, unit: count, evidence: claimed}
  - {ts: "01:20", metric: "doanh thu trọn đời (founder ước 'probably')", value: 120000, unit: usd, evidence: claimed}
  - {ts: "12:00", metric: "biên lợi nhuận", value: 90, unit: percent, evidence: claimed}
frameworks: []
idea_patterns: [single-feature-on-platform, platform-marketplace-distribution]
---
## Một câu

Sync2sheets: add-on Google Sheets làm đúng một việc, đưa dữ liệu Notion vào bảng tính, bán trên marketplace của Google Workspace. Ý tưởng từ khoảng trống khi Notion ra API chính thức, kiểm bằng Reddit trước khi build; 9K/tháng theo host (founder chỉ xác nhận lifetime khoảng 120k).

## Bài học cho tôi

- Khoảng trống khi nền tảng lớn ra API mới là nguồn ý tưởng; kiểm bằng cách đọc Reddit trước khi build (`01:53`, `02:23`).
- Đưa sản phẩm lên marketplace trước, rồi trò chuyện trực tiếp với người dùng trong nhóm, DM và chat trên landing page để biết họ cần gì (`09:52`, `09:36`).

## Đừng tin vội

- Bias: Monday.com trả tiền cho đoạn quảng cáo marketplace (`07:35`–`08:51`); Starter Story Build quảng bá cuối video (`15:03`).
- Con số 9K/tháng do host nêu (`01:02`); founder không xác nhận con số đó, chỉ nói lifetime khoảng 120k và 450 khách trả tiền. Không có màn hình.
- Video không nói giá, các gói, kênh cụ thể của 10 người dùng đầu tiên, hay nhóm nào trong số các nhóm Notion đã thành khách trả tiền.
- Điều kiện riêng: đã biết Sheets API và JavaScript, có chút tiết kiệm để nghỉ freelance (`04:12`). Người chưa có kỹ năng đó khó chép đúng cách này.
- Sản phẩm một việc trên marketplace có sẵn người đang tìm; đây không phải bằng chứng cho mọi ý tưởng một việc.
