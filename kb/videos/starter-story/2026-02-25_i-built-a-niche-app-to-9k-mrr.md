---
schema: 2
video_id: 7vz6b_Ohdl0
channel: starter-story
title: "I Built a Niche App to $9K MRR"
date: 2026-02-25
url: https://www.youtube.com/watch?v=7vz6b_Ohdl0
transcript: starter-story-kb/videos/2026-02-25_i-built-a-niche-app-to-9k-mrr/transcript.md
kind: founder_case
speakers:
  - {name: Jonathan Fishner, role: founder}
  - {name: Pat Walls, role: host}
  - {name: Gus, role: host}
bias: "Video là phễu của Starter Story: quảng bá guide tìm ý tưởng và Starter Story Build (link trong mô tả và video). Số MRR là lời founder, không kiểm toán."
analyzed: 2026-11-15
cases:
  - id: chartdb
    depth: full
    product: "ChartDB: công cụ mã nguồn mở trực quan hoá database cho developer; bản cloud trả phí (video gọi là Chartbrew)"
    what: "Biến database thành sơ đồ/biểu đồ trực quan: developer chạy một câu query rồi dán kết quả JSON vào, không cần cấp quyền truy cập DB hay cài phần mềm"
    type: [developer-tool]
    customer: "Developer dùng miễn phí qua GitHub; một phần lên gói cloud trả phí khi cần làm việc nhóm"
    founder: {who: Jonathan Fishner, base: null, technical: true, team: "có đồng sáng lập (co-founder)", background: "Developer"}
    revenue: {amount: 9000, unit: usd, basis: mrr, note: "Founder: about 9,000 in MRR (01:20). Host intro nói $9,000 a month (00:00). Ở 02:23 founder nói passed almost 9400 (không rõ tháng hay đơn vị).", q: "we just make about 9,000 in MRR.", ts: "01:20", evidence: claimed}
    pricing: "Mã nguồn mở miễn phí; bản cloud trả phí theo gói, có gói cho team. Video không nêu giá cụ thể."
    idea_origin: [domain_expertise]
    scale_channels: [reddit]
    community_at_discovery: {value: "Là developer, làm sản phẩm cho developer; biết engineer không chịu cấp quyền truy cập DB", insider: true, q: "I'm a developer, and I'm the co-founder of Chartbrew.", ts: "01:02"}
    demand_signal: null
    prior_failures: {count: 1, what: "Thử hướng database client có AI trước; dừng vì người dùng không chấp nhận cấp quyền truy cập DB và cài phần mềm", q: "we had like big stop because people don't really adopt that", ts: "02:55"}
    unfair_advantage:
      - {value: technical_skill, what: "Là developer, làm sản phẩm cho developer", q: "I'm a developer, and I'm the co-founder of Chartbrew.", ts: "01:02"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 16, value: "16 tháng từ lúc mở mã nguồn tới ~9k MRR", q: "We launched the open-source uh 16 months ago", ts: "01:02"}
    first_users: []
    build:
      time: "khoảng 3 tuần phát triển trước khi đăng Show HN"
      cut: []
      q: "after three weeks of development, we decided to go for launch"
      ts: "04:27"
steps:
  - {stage: find-idea, ts: "03:10", case: chartdb, what: "Bỏ hướng database client có AI vì người dùng không chịu cấp quyền truy cập DB và cài phần mềm; chuyển sang ý tưởng biến database thành biểu đồ, không cần cấp quyền hay cài gì.", tactic: other, tactic_note: "Pivot sản phẩm theo ràng buộc của người dùng (dev không cấp quyền, không cài phần mềm)"}
  - {stage: launch, ts: "01:52", case: chartdb, what: "Mở mã nguồn trên GitHub; developer tìm thấy qua GitHub, dùng miễn phí rồi lên gói cloud khi quy trình ổn định.", tactic: g9-launch-platforms, tactic_note: "GitHub là nơi developer đã có sẵn"}
  - {stage: launch, ts: "04:27", case: chartdb, what: "Chuẩn bị rồi chọn một ngày đăng Show HN trên Hacker News; bài lên trang chủ và đưa hàng nghìn kỹ sư vào sản phẩm trong một ngày.", tactic: g9-launch-platforms, tactic_note: "Show HN trên Hacker News"}
  - {stage: launch, ts: "08:53", case: chartdb, what: "Đưa sản phẩm vào nơi developer đang có mặt: Reddit (subreddit self-hosted và các subreddit developer hay dùng).", tactic: g1-first-10-users, tactic_note: "Cộng đồng developer trên Reddit"}
  - {stage: monetize, ts: "08:04", case: chartdb, what: "Lúc đầu chưa thu tiền; bắt đầu thu khi người dùng hỏi làm việc nhóm và cần cộng tác real-time.", tactic: g4-pricing-paywall}
quotes:
  - {ts: "11:59", who: Jonathan Fishner, stage: mindset, theme: [focus-one-thing], text: "I would tell myself like to pick one core value and defend it and like aggressively.", vi: "Nếu quay lại, tôi sẽ tự nhủ: chọn một giá trị cốt lõi và bảo vệ nó thật quyết liệt."}
  - {ts: "06:48", who: Jonathan Fishner, stage: find-idea, theme: [], text: "we start with like be the user or ideally build for yourself.", vi: "Chúng tôi bắt đầu từ việc: hãy là người dùng, hoặc lý tưởng nhất là tự xây cho chính mình."}
  - {ts: "08:37", who: Jonathan Fishner, stage: monetize, theme: [revenue-first], text: "monetization should not be a guess and should be response to your behavior.", vi: "Thu tiền không nên là phỏng đoán; nó phải phản ứng theo hành vi của người dùng."}
rules:
  - {ts: "00:16", who: "Pat Walls hoặc Gus", stage: find-idea, theme: [right-audience], text: "Instead, he built something with just one type of person in mind.", vi: "Thay vào đó, anh xây cho đúng một kiểu người.", evidence: opinion}
  - {ts: "05:45", who: "Pat Walls hoặc Gus", stage: find-idea, theme: [], text: "My best advice is don't start coding just yet. The best businesses actually [music] solve problems that are hiding in plain sight right in front of you right now.", vi: "Lời khuyên của tôi: đừng code vội. Những doanh nghiệp tốt nhất giải quyết vấn đề nằm ngay trước mắt bạn.", evidence: opinion}
  - {ts: "13:15", who: Gus, stage: find-idea, theme: [], text: "so that's my takeaway is like building stuff in the spaces that you know about.", vi: "Điều tôi rút ra là: xây thứ gì đó trong lĩnh vực bạn hiểu.", evidence: opinion}
numbers:
  - {ts: "01:20", metric: "MRR (lời founder)", value: 9000, unit: usd_per_month, evidence: claimed}
  - {ts: "02:08", metric: "sao GitHub (lời founder)", value: 21000, unit: count, evidence: claimed}
  - {ts: "02:08", metric: "developer đã dùng sản phẩm trong năm (lời founder)", value: 250000, unit: count, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Developer làm ChartDB, công cụ mã nguồn mở biến database thành biểu đồ mà không cần cấp quyền truy cập hay cài phần mềm; sau Show HN và GitHub, sản phẩm đạt khoảng 9k MRR sau 16 tháng.

## Bài học cho tôi

- Bỏ hướng đầu vì ràng buộc của người dùng (dev không cấp quyền DB, không cài phần mềm), rồi chọn bản bỏ được ràng buộc đó (`03:10`).
- Chọn một giá trị cốt lõi và đẩy đến cùng, thay vì làm mọi thứ cùng lúc (`11:59`).

## Đừng tin vội

- Founder là developer, làm cho chính cộng đồng mình. Đây là lợi thế thật, người không làm dev khó chép.
- Số 9k MRR là lời founder; video có mở analytics nhưng không rõ là dashboard hay ảnh. Để claimed.
- Show HN là cú nổ một lần: hàng nghìn lượt trong một ngày. Video không nói có bao nhiêu lần đăng khác không lên trang chủ.
- GitHub và Hacker News không có trong vocab.channel nên first_users để trống; các kênh này được ghi trong steps (tactic g9). Từ vựng thiếu.
- Bias: Starter Story bán guide tìm ý tưởng và Starter Story Build; khuyên "đừng code vội" là phần quảng cáo trong video.
