---
schema: 2
video_id: RPM4ImzcIFc
channel: starter-story
title: "How I Built It: $17K/Month Open Source SaaS"
date: 2026-01-28
url: https://www.youtube.com/watch?v=RPM4ImzcIFc
transcript: starter-story-kb/videos/2026-01-28_how-i-built-it-17k-month-open-source-saas/transcript.md
kind: founder_case
speakers:
  - {name: Nevo, role: founder}
  - {name: Pat Walls, role: host}
bias: "Starter Story có tài trợ (Delve, giảm $1,000) và giới thiệu playbook miễn phí cùng bootcamp Starter Story Build. Nevo bán Postiz và, theo video, còn làm tư vấn open-source marketing cho nhiều công ty; lời khuyên 'làm open source' có lợi cho chính anh và dịch vụ đó."
analyzed: 2026-11-15
cases:
  - id: postiz
    depth: full
    product: "Postiz (postiz.com): app lên lịch đăng mạng xã hội, mã nguồn mở, bán theo gói SaaS"
    what: "Lên lịch đăng bài cho 25 nền tảng mạng xã hội, có công cụ AI tạo ảnh/video và public API; bản self-host giống hệt bản cloud."
    type: [web-app]
    customer: "Người cần lên lịch đăng nhiều mạng xã hội (marketing, creator); developer tự self-host; doanh nghiệp cần self-host kèm hỗ trợ (theo anh)"
    founder:
      who: Nevo
      base: null
      technical: true
      team: "không nêu rõ (anh dùng 'we')"
      background: "Developer nhiều năm; 2 năm ở một công ty open source tăng 0 → 32k sao; sau đó tư vấn open-source marketing khoảng một năm"
    revenue:
      amount: 17000
      unit: usd
      basis: mrr
      note: "Anh nói 'we're currently on 17K MR'; host yêu cầu mở dashboard nhưng video không rõ có đọc số từ dashboard không"
      q: "we're currently on 17K MR"
      ts: "02:54"
      evidence: claimed
    pricing: "Nhiều gói (Standard, Team, Pro, Ultimate), phân tầng theo số kênh và tính năng; video không nêu giá"
    idea_origin: []
    scale_channels: [word_of_mouth, seo, reddit]
    community_at_discovery:
      value: "Developer làm trong co-working space, gặp nhóm đang làm công cụ open source hạ tầng; vào làm cho công ty đó"
      insider: true
      q: "I met some few cool people that building uh an open-source uh infrastructure"
      ts: "04:15"
    demand_signal: null
    prior_failures:
      count: null
      what: "Trước đó có nhiều startup thất bại ('so many failures in so many startups'); video không đếm số"
      q: "I had so many failures in so many startups at first"
      ts: "20:51"
    unfair_advantage:
      - {value: domain_expertise, what: "Tư vấn open-source marketing ngách khoảng một năm vì 'chỉ mình tôi nói về việc đó'", q: "in the second year I started to do a lot of consulting very nichy consulting because I was the only person talking about that", ts: "04:31"}
      - {value: technical_skill, what: "Developer nhiều năm, tự build Postiz", q: "just a developer for many many many years", ts: "04:15"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: reddit, what: "Video không nói 10 người đầu. Anh đăng r/selfhosted và đăng lại mỗi bản mới", q: "go to Reddit and post it on /r/selfosted", ts: "14:25"}
      - {channel: word_of_mouth, what: "Video không nói 10 người đầu. Anh nói developer tự giới thiệu và làm nội dung cho sản phẩm", q: "They will talk to a lot of people", ts: "07:35"}
    build: null
steps:
  - {stage: launch, ts: "10:45", case: postiz, tactic: other, tactic_note: "Chuẩn bị GitHub như landing page: README rõ sản phẩm, chọn license, mở issue cho tính năng, Discord, hướng dẫn deploy/docker", what: "Trước launch biến GitHub thành landing page: README, license, issue, Discord, docker để developer deploy được."}
  - {stage: launch, ts: "12:19", case: postiz, tactic: g9-launch-platforms, tactic_note: "Hacker News, Reddit, Lemmy; tài khoản chuẩn bị trước; mục tiêu lên trending GitHub", what: "Chuẩn bị tài khoản trước: đăng ký Hacker News khoảng 2 tuần trước, Reddit cần karma, thêm Lemmy."}
  - {stage: launch, ts: "13:06", case: postiz, tactic: g3-organic-content-formats, tactic_note: "Bài trên dev.to, Medium, Hashnode; tiêu đề và ảnh bìa quyết định traffic từ Google Discover", what: "Viết bài trên dev.to, Medium, Hashnode về cách làm sản phẩm; đầu tư tiêu đề và ảnh bìa vì traffic đến từ Google Discover."}
  - {stage: launch, ts: "14:10", case: postiz, tactic: g9-launch-platforms, threshold: "lên trang chính khoảng 10,000 view (lời anh)", tactic_note: "Show HN dẫn tới link GitHub, không dẫn tới website", what: "Đăng Show HN với link GitHub; nếu lên trang chính, anh kỳ vọng khoảng 10,000 view."}
  - {stage: launch, ts: "14:40", case: postiz, tactic: g1-first-10-users, tactic_note: "r/selfhosted; đăng lại mỗi bản mới; dùng 'I' không 'we'", what: "Đăng r/selfhosted theo kiểu build in public, khiêm tốn và xin star; mỗi bản mới đăng lại."}
  - {stage: launch, ts: "15:42", case: postiz, tactic: g3-organic-content-formats, tactic_note: "X, LinkedIn, newsletter đều dẫn về GitHub; cả 5 bước cùng một tuần", what: "Đưa traffic từ X, LinkedIn, newsletter về GitHub; cả 5 bước phải chạy trong cùng một tuần."}
  - {stage: monetize, ts: "02:38", case: postiz, tactic: g4-pricing-paywall, tactic_note: "Phân tầng theo tính năng, không chỉ theo số kênh", what: "Các gói Standard, Team, Pro, Ultimate; muốn người ta dùng Standard nhưng nâng cấp theo tính năng chứ không theo số kênh."}
quotes:
  - {ts: "04:31", who: "Nevo", stage: find-idea, theme: [], text: "I've never seen growth like that before in open source in my life.", vi: "Tôi chưa bao giờ thấy tăng trưởng như vậy trong open source."}
  - {ts: "07:04", who: "Nevo", stage: monetize, theme: [], text: "Developers are not buying persona and they will probably not pay you.", vi: "Developer ít khi trả tiền cho bạn; đừng cố tìm cách bắt họ trả."}
  - {ts: "09:28", who: "Nevo", stage: grow, theme: [], text: "today the only thing that is winning usually is brand", vi: "Ngày nay thứ thắng thường chỉ là thương hiệu."}
  - {ts: "20:51", who: "Nevo", stage: mindset, theme: [action-over-research], text: "I think you should learn a lot before you build. But you don't also want to get into this analysis paralysis state.", vi: "Nên học nhiều trước khi build, nhưng đừng rơi vào trạng thái phân tích tê liệt."}
rules:
  - {ts: "01:02", who: "Pat Walls", stage: launch, theme: [], text: "this episode is not about building, it's about distribution", vi: "Tập này không nói về build mà nói về phân phối.", evidence: opinion}
  - {ts: "22:10", who: "Pat Walls", stage: find-idea, theme: [], text: "you don't need to reinvent the wheel to build something successful", vi: "Bạn không cần phát minh lại bánh xe để làm được thứ thành công.", evidence: opinion}
numbers:
  - {ts: "00:15", metric: "lượt tải app (lời founder)", value: 5000000, unit: count, evidence: claimed}
  - {ts: "02:54", metric: "MRR (lời founder)", value: 17000, unit: usd_per_month, evidence: claimed}
  - {ts: "02:54", metric: "subscriber", value: 472, unit: count, evidence: claimed}
  - {ts: "02:54", metric: "churn (anh nói đang cố giảm)", value: 0.19, unit: ratio, evidence: claimed}
  - {ts: "02:54", metric: "lượt trial từ tháng 8/2025", value: 3830, unit: count, evidence: claimed}
  - {ts: "02:54", metric: "tỉ lệ trial → trả tiền", value: 0.21, unit: ratio, evidence: claimed}
  - {ts: "14:25", metric: "lượt xem kỳ vọng khi lên trang chính Hacker News", value: 10000, unit: count, evidence: claimed}
  - {ts: "20:03", metric: "chi phí công cụ chuyển đổi video (lớn nhất)", value: 600, unit: usd, evidence: claimed}
  - {ts: "20:18", metric: "biên lợi nhuận gộp", value: 0.8, unit: ratio, evidence: claimed}
frameworks: []
idea_patterns: []
---
## Một câu

Nevo làm Postiz (lên lịch đăng cho 25 mạng xã hội, mã nguồn mở, bán theo gói SaaS) lên khoảng 17k MRR bằng cách biến GitHub thành landing page và launch qua Hacker News, Reddit và các cộng đồng open source; video không nói có chạy quảng cáo hay không.

## Bài học cho tôi

- Launch theo chuỗi: chuẩn bị tài khoản HN/Reddit trước, rồi dồn 5 kênh vào cùng một tuần để lên trending GitHub (`"12:19"`, `"15:42"`).
- Bản self-host và bản cloud giống nhau, nên developer tự dùng rồi giới thiệu; anh coi đó là kênh truyền miệng chính (`"03:11"`, `"07:35"`).

## Đừng tin vội

- 17k MRR và các số trial, churn, subscriber là anh tự báo. Host yêu cầu mở dashboard nhưng video không cho thấy rõ số nào đọc từ dashboard, nên để `claimed`. Churn 19% anh nói đang cố giảm, chưa chứng minh giữ chân được.
- Nhà tài trợ: Delve (compliance) và Starter Story Build (playbook, bootcamp). Anh cũng làm tư vấn open-source marketing, nên lời khuyên "làm open source" có lợi cho dịch vụ đó.
- Điều kiện riêng: 2 năm ở công ty open source tăng 0 → 32k sao, và một năm tư vấn ngách với vị trí "người duy nhất nói về việc đó". Không phải developer nào cũng có nền này.
- Video không nói vì sao chọn social media scheduling, thời gian build, chi phí ban đầu, thời gian tới 1k/10k MRR, và 10 người dùng đầu tiên là ai.
