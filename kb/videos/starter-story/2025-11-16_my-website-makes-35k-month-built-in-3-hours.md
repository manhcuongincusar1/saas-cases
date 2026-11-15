---
schema: 2
video_id: LWPN-PAhtLA
channel: starter-story
title: "My website makes $35K/month (built in 3 hours)"
date: 2025-11-16
url: https://www.youtube.com/watch?v=LWPN-PAhtLA
transcript: starter-story-kb/videos/2025-11-16_my-website-makes-35k-month-built-in-3-hours/transcript.md
kind: founder_case
speakers:
  - {name: Pontus Abrahamsson, role: founder}
  - {name: Pat Walls, role: host}
bias: "Starter Story bán Starter Story Build (CTA giữa và cuối video); founder quảng bá Cursor Directory và các startup khác. Tỉ lệ lợi nhuận 99.8% là tự nói. Video kể về một thành công đã đạt (survivor bias)."
analyzed: 2026-11-15
cases:
  - id: cursor-directory
    depth: full
    product: "Cursor Directory: thư mục gom rules cho Cursor (công cụ AI coding); người dùng tìm và copy rules vào editor"
    what: "Gom các cursor rules vào một nơi để tìm, lọc, bình chọn và copy; có tài khoản người dùng, tin tuyển dụng và rules được featured trả phí; có tính năng sinh rules từ package.json"
    type: [web-app]
    customer: "Lập trình viên dùng Cursor cần rules có sẵn; công ty đăng tin tuyển dụng trả phí; tác giả rules trả phí để được featured"
    founder: {who: "Pontus Abrahamsson", base: null, technical: true, team: "Co-founder Victor (bạn thân, làm chung nhiều năm); làm song song với startup chính", background: "Developer có nhiều kinh nghiệm build app và website; có startup chính khác đang làm"}
    revenue: {amount: 35000, unit: usd, basis: monthly, note: "Founder nói 35k/tháng; host nói 34k/tháng với biên lợi nhuận 99.8% (tự nói)", q: "now it makes 35k [snorts] per month", ts: "02:25", evidence: claimed}
    pricing: "Không có gói thuê bao. Người dùng đăng ký miễn phí; trả phí cho tin tuyển dụng (job ads) và rules được featured"
    idea_origin: [own_pain]
    scale_channels: [founder_led_content, word_of_mouth]
    community_at_discovery:
      value: "Developer đang học Cursor qua video kỹ thuật trên máy bay, thấy rules rải rác trên gist và forum"
      insider: true
      q: "then I discovered this common pattern about rules"
      ts: "03:28"
    demand_signal: null
    prior_failures: null
    unfair_advantage:
      - {value: technical_skill, what: "Hai co-founder có nhiều kinh nghiệm build app và website qua nhiều năm", q: "a lot of experience building apps and websites through the years", ts: "03:43"}
      - {value: cofounder, what: "Co-founder Victor, làm chung nhiều năm, chung cách làm về thiết kế và code", q: "Victor and I have been working together for several years", ts: "04:30"}
      - {value: existing_audience, what: "Đã có lượng follower developer trên X từ đầu, nhờ build in public", q: "So we have a developer following uh from the beginning", ts: "06:00"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: founder_led_content, what: "Đăng X trong lúc build in public, mã nguồn mở; một bài đạt khoảng 1 triệu impression", q: "So I think we had like 1 million impressions on one of the posts", ts: "06:00"}
      - {channel: word_of_mouth, what: "Sau khi lên front page, nhiều YouTuber phủ sóng sản phẩm (video không nói có trả tiền hay không)", q: "a lot of YouTubers started to cover uh curs directly into the uh videos", ts: "06:00"}
    build:
      time: "3 giờ cho bản đầu tiên (founder nói 'trong một cuối tuần')"
      cut: ["Rules để hard-code trong file JSON thay vì hệ thống quản lý nội dung"]
      q: "So we built the site completing three hours"
      ts: "04:15"
steps:
  - stage: find-idea
    ts: "03:28"
    case: cursor-directory
    what: "Trên máy bay đang học Cursor, thấy rules rải rác trên gist và forum, không có chỗ tập trung; ý tưởng là gom về một chỗ"
    tactic: s5-insider
    tactic_note: "Developer đang dùng Cursor, gặp nỗi đau ngay trong cộng đồng mình"
  - stage: build
    ts: "03:59"
    case: cursor-directory
    what: "Gọi Victor, thiết kế trên Figma, dựng Next.js với file JSON hard-code các rules nhặt từ mạng; lên Vercel trong khoảng nửa giờ"
  - stage: launch
    ts: "06:00"
    case: cursor-directory
    what: "Đăng X nhiều bài trong tuần đầu, chia sẻ tiến trình và mã nguồn mở"
    tactic: g3-organic-content-formats
    tactic_note: "Build in public trên X, chia sẻ code"
  - stage: launch
    ts: "06:00"
    case: cursor-directory
    what: "Đăng Hacker News và lên front page, kéo theo YouTuber phủ sóng"
    tactic: g9-launch-platforms
    tactic_note: "Hacker News (cộng đồng dev có sẵn người đọc) rồi front page"
  - stage: monetize
    ts: "10:54"
    case: cursor-directory
    what: "Kiếm tiền từ tin tuyển dụng (job ads) trả phí và rules được featured trả phí, không có gói thuê bao"
    tactic: other
    tactic_note: "Bán listing cho bên thứ ba (nhà tuyển dụng và tác giả rules) thay vì thu từ người dùng cuối"
  - stage: grow
    ts: "11:09"
    case: cursor-directory
    what: "Thêm tìm kiếm qua MCP và tính năng sinh rules từ package.json; founder coi đây là lần adoption lớn thứ hai"
    tactic: other
    tactic_note: "Tính năng sản phẩm (MCP, sinh rules từ package.json) được coi là kênh adoption"
quotes:
  - {ts: "03:28", who: "Pontus Abrahamsson", stage: find-idea, theme: [], text: "it was kind of mind-blowing for me that there were no uh place to find these rules in one specific place", vi: "Với tôi thật bất ngờ là không có chỗ nào gom các rules lại một nơi."}
  - {ts: "04:15", who: "Pontus Abrahamsson", stage: build, theme: [], text: "So we built the site completing three hours and but then we just continued to iterate.", vi: "Chúng tôi dựng xong trong ba giờ, rồi tiếp tục lặp lại."}
  - {ts: "05:00", who: "Pontus Abrahamsson", stage: mindset, theme: [action-over-research], text: "We find these ideas and that comes together when you dial in and work fully on something you're committed to", vi: "Ý tưởng đến khi bạn tập trung làm hết mình vào thứ mình cam kết và thấy một giải pháp mình làm được."}
  - {ts: "13:02", who: "Pontus Abrahamsson", stage: mindset, theme: [persistence], text: "You create your own luck by constantly finding ways to move forward, shipping, sharing, and iterate.", vi: "Bạn tự tạo may mắn bằng cách liên tục tìm cách tiến lên: ship, chia sẻ, lặp lại."}
rules:
  - {ts: "13:32", who: "Pat Walls", stage: launch, theme: [action-over-research], text: "There's no way to know that without actually getting started building something and seeing what happens.", vi: "Không có cách nào biết điều đó nếu không thật sự bắt đầu làm và xem điều gì xảy ra.", evidence: opinion}
numbers:
  - {ts: "02:41", metric: "người dùng đăng ký", value: 49000, unit: count, evidence: claimed}
  - {ts: "02:41", metric: "unique visitor từ khi ra mắt", value: 2200000, unit: count, evidence: claimed}
  - {ts: "02:57", metric: "biên lợi nhuận gộp (tự nói)", value: 99.8, unit: percent, evidence: claimed}
  - {ts: "02:57", metric: "chi phí vận hành mỗi tháng (dưới)", value: 500, unit: usd_per_month, evidence: claimed}
  - {ts: "02:57", metric: "giờ bảo trì mỗi tháng", value: 3, unit: hours_per_month, evidence: claimed}
  - {ts: "06:00", metric: "impression một bài trên X", value: 1000000, unit: count, evidence: claimed}
  - {ts: "12:29", metric: "tổng chi phí công cụ mỗi tháng", value: 525, unit: usd_per_month, evidence: claimed}
frameworks: [build-in-public-waitlist]
idea_patterns: [single-feature-on-platform]
---
## Một câu

Developer đang học Cursor thấy rules rải rác khắp nơi, dựng một thư mục gom rules trong khoảng 3 giờ, đăng X và lên front page Hacker News; nay khoảng 35k/tháng từ tin tuyển dụng và rules được featured (tự nói).

## Bài học cho tôi

- Ý tưởng đến từ nỗi đau khi chính mình dùng công cụ mỗi ngày (`03:28`); bản đầu chỉ gom thứ đang rải rác về một chỗ và ship trong vài giờ (`04:15`).
- Kiếm tiền từ phía nhà tuyển dụng và tác giả được featured, không thu phí người dùng cuối (`10:54`).

## Đừng tin vội

- Survivor bias: chỉ kể cái đã thành, và gặp đúng làn sóng Cursor và MCP. Hai founder có kinh nghiệm build và có startup chính khác, không phải người mới bắt đầu.
- 35k và 99.8% là tự nói (host đọc 34k). Video không nói sau bao lâu đạt mức này, không nói bao nhiêu tin tuyển dụng, không nói chi phí marketing.
- "3 giờ" là bản đầu, không tính kinh nghiệm nhiều năm và design system có sẵn từ các startup trước.
