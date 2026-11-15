---
schema: 2
video_id: F8i0kkrQ8_o
channel: starter-story
title: "How We Built It: $900K Open Source SaaS"
date: 2025-08-16
url: https://www.youtube.com/watch?v=F8i0kkrQ8_o
transcript: starter-story-kb/videos/2025-08-16_how-we-built-it-900k-open-source-saas/transcript.md
kind: founder_case
speakers:
  - {name: Iuliia, role: founder}
  - {name: Marc, role: founder}
  - {name: Pat Walls, role: host}
bias: "Starter Story chèn quảng cáo Vanta (giảm $1.000, giữa video) và Starter Story Build (cuối video). Papermark bán bản hosted và license enterprise, nên câu chuyện open source có lợi cho việc bán của họ."
analyzed: 2026-11-15
cases:
  - id: papermark
    depth: full
    product: "Papermark: nền tảng chia sẻ và phân tích tài liệu, open-source, thay thế DocSend"
    what: "Chia sẻ tài liệu qua link có mật khẩu và watermark, xem thống kê người đọc; bản self-host miễn phí và bản hosted trả phí"
    type: [web-app]
    customer: "Người cần chia sẻ tài liệu và data room; khách trả tiền dùng bản hosted hoặc license enterprise"
    founder: {who: "Iuliia và Marc (vợ chồng, đồng sáng lập)", base: null, technical: null, team: "2 đồng sáng lập, thuê freelancer", background: null}
    revenue: {amount: 75000, unit: usd, basis: mrr, note: "Transcript ghi 'MR' (ASR, hiểu là MRR); founder nói ở đầu video 'bootstrapped to 75K'. Mô tả YouTube ghi $900K/năm", q: "We bootstrapped Papermark to 75K MR.", ts: "00:00", evidence: claimed}
    pricing: "Open-core: self-host miễn phí; bản hosted (papermark.com) trả phí; license enterprise để chạy self-host đủ tính năng"
    idea_origin: [audience_signal]
    scale_channels: [founder_led_content, word_of_mouth]
    community_at_discovery: {value: "Đăng ý định làm bản open-source thay DocSend lên Twitter; người xem nói muốn có bản open source", insider: null, q: "Lots of people mentioned that they would love to see this as an open source project.", ts: "01:35"}
    demand_signal: {kind: content_views, level: 2, what: "Tweet nói sẽ làm bản open-source thay DocSend, đăng trước khi build: khoảng 40.000 view trong vài giờ", q: "hours it got like 40,000 views.", ts: "01:35"}
    prior_failures: null
    unfair_advantage:
      - {value: cofounder, what: "Hai đồng sáng lập là vợ chồng", q: "This husband and wife duo built a near million dollar business", ts: "00:00"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: {months: 18, value: "khoảng một năm rưỡi (host nói, không phải founder)", q: "In just a year and a half, they took a weekend open source project to $75,000 MR.", ts: "00:16"}
    first_users:
      - {channel: founder_led_content, what: "Tweet ra mắt MVP (khoảng 100.000 view); khách đầu tiên tới hỏi có thể trả tiền để dùng dịch vụ", q: "soon after their first customers came and were asking like", ts: "01:51"}
    build: {time: "Một cuối tuần cho MVP dùng được", cut: [], q: "over the weekend, I actually built it at least their first MVP", ts: "01:35"}
steps:
  - stage: find-idea
    ts: "01:20"
    case: papermark
    what: "Chọn làm bản open-source thay thế một sản phẩm đã có (DocSend)."
    tactic: s11-copy-or-localize-proven
    tactic_note: "Làm bản open-source thay thế DocSend, sản phẩm đã chạy trên thị trường"
  - stage: validate
    ts: "01:20"
    case: papermark
    what: "Đăng tweet nói sẽ làm bản open-source thay DocSend trước khi build; tweet chạy khoảng 40.000 view trong vài giờ."
    tactic: s8-content-demand-test
    tactic_note: "Tweet ý tưởng trước khi build để đo nhu cầu"
  - stage: launch
    ts: "01:35"
    case: papermark
    what: "Làm MVP dùng được trong một cuối tuần, rồi đăng tweet ra mắt vào thứ Hai (khoảng 100.000 view)."
    tactic: g3-organic-content-formats
    tactic_note: "Tweet ra mắt MVP, nội dung organic"
  - stage: monetize
    ts: "04:15"
    case: papermark
    what: "Mô hình open-core: self-host miễn phí, bản hosted trả phí, license enterprise để chạy self-host đủ tính năng."
    tactic: g4-pricing-paywall
  - stage: grow
    ts: "09:13"
    case: papermark
    what: "Build in public: chia sẻ tiến độ lên Twitter và LinkedIn, kể cả tính năng chưa hoàn thiện, để gom cộng đồng."
    tactic: g3-organic-content-formats
    tactic_note: "Build in public bằng tiến độ dở dang"
  - stage: grow
    ts: "09:43"
    case: papermark
    what: "Tham gia Hacktoberfest (cuộc thi open source kéo dài một tháng) để đẩy tính năng và thu hút người tham gia."
    tactic: other
    tactic_note: "Sự kiện open source (Hacktoberfest) có sẵn cộng đồng developer"
quotes:
  - {ts: "01:20", who: "Iuliia hoặc Marc", stage: find-idea, theme: [action-over-research], text: "It started as a tweet. I pushed out a tweet and I basically said like I'm going to build an open source alternative to Docsend and it went just like crazy.", vi: "Nó bắt đầu từ một tweet. Tôi đăng tweet và nói rằng sẽ làm một bản open-source thay thế Docsend, và nó lan rất mạnh."}
  - {ts: "01:35", who: "Iuliia hoặc Marc", stage: launch, theme: [ship-ugly], text: "the first version that was usable and pushed out on Monday the launch tweet", vi: "Bản đầu dùng được được đẩy ra vào thứ Hai cùng tweet ra mắt."}
  - {ts: "07:53", who: "Iuliia hoặc Marc", stage: find-idea, theme: [], text: "With the era of AI, founders can target much smaller niches and like smaller markets.", vi: "Thời AI, founder có thể nhắm vào các ngách nhỏ hơn và thị trường nhỏ hơn."}
  - {ts: "09:28", who: "Iuliia hoặc Marc", stage: grow, theme: [ship-ugly], text: "there's no downside to sharing the small progress even that you're making even if the features are not 100% complete share that on Twitter on LinkedIn just with anyone", vi: "Chia sẻ tiến độ nhỏ không có điểm bất lợi gì, kể cả khi tính năng chưa hoàn thiện 100%; cứ chia sẻ lên Twitter, LinkedIn."}
  - {ts: "12:54", who: "Iuliia hoặc Marc", stage: mindset, theme: [action-over-research], text: "I didn't know how to code at all and I decided okay I'm going to build the first project.", vi: "Tôi hoàn toàn không biết code, nhưng quyết định làm dự án đầu tiên."}
  - {ts: "13:24", who: "Iuliia hoặc Marc", stage: mindset, theme: [action-over-research], text: "Just do it open source from the beginning. Try to be part of the community.", vi: "Làm open source từ đầu luôn. Hãy tham gia cộng đồng."}
rules:
  - {ts: "13:54", who: "Pat Walls", stage: find-idea, theme: [], text: "However, I must remind you that it all still started with a simple idea. And nowadays, that's all you need to potentially build something that changes your life.", vi: "Nhưng tôi phải nhắc rằng tất cả vẫn bắt đầu từ một ý tưởng đơn giản; ngày nay đó là tất cả những gì bạn cần để có thể xây thứ thay đổi cuộc đời.", evidence: opinion}
numbers:
  - {ts: "09:59", metric: "MRR năm đầu (lời founder; transcript ghi 'MR')", value: 20000, unit: usd_per_month, evidence: claimed}
  - {ts: "10:15", metric: "MRR giữa năm thứ hai (lời founder)", value: 75000, unit: usd_per_month, evidence: claimed}
  - {ts: "10:30", metric: "GitHub stars", value: 7000, unit: count, evidence: claimed}
  - {ts: "10:30", metric: "số contributor", value: 60, unit: count, evidence: claimed}
  - {ts: "11:48", metric: "chi phí freelancer và lương founder trên doanh thu", value: 80, unit: percent, evidence: claimed}
frameworks: [content-before-product]
idea_patterns: []
---
## Một câu

Vợ chồng Iuliia và Marc tweet ý định làm bản open-source thay DocSend, làm MVP dùng được trong một cuối tuần, rồi đạt khoảng 75K MR (transcript ghi 'MR') nhờ mô hình open-core và build in public.

## Bài học cho tôi

- Đo nhu cầu bằng tweet trước khi build: ý định làm bản thay thế một sản phẩm đã có nhận khoảng 40.000 view trong vài giờ (`01:35`).
- Chia sẻ tiến độ dở dang để gom cộng đồng; founder nói không có gì phải giấu và không mất gì khi share tính năng chưa xong (`09:28`).

## Đừng tin vội

- Thành công này gắn với open source trong ngành developer (GitHub stars, contributor miễn phí, Hacktoberfest). Ngách không có cộng đồng dev, hoặc không có sản phẩm để mở mã nguồn, không chép được nguyên.
- Số liệu là lời founder. 'MR' là ASR, chưa chắc là MRR; mô tả YouTube ghi $900K/năm. Video không nói tỉ lệ free -> trả tiền, số khách trả tiền chính xác.
- Tweet 40.000 view và 100.000 view là lượt xem, không phải tiền; ở giai đoạn đó chưa có ai trả tiền.
- Video chèn quảng cáo Vanta và Starter Story Build; host kết bằng lời kêu gọi Starter Story Build (`13:54`).
- Transcript ghi tên founder là 'Ule', 'Julia', 'Mark' (ASR); ghi theo mô tả là Iuliia và Marc. Không rõ ai nói câu nào, nên quote ghi 'Iuliia hoặc Marc'.
- Survivorship: video kể một dự án thành công; không kể các dự án open source không đạt.
- Video không nói chi phí ban đầu, thời gian có khách trả tiền đầu tiên, hay bao nhiêu khách hàng trả tiền.
