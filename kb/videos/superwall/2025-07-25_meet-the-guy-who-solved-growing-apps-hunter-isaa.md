---
schema: 2
video_id: DTree0unT_0
channel: superwall
title: "Meet The Guy Who Solved Growing Apps (Hunter Isaacson Interview)"
date: 2025-07-25
url: https://www.youtube.com/watch?v=DTree0unT_0
transcript: superwall/youtube-transcript/superwall/meet-the-guy-who-solved-growing-apps-hunter-isaacson-interview/transcript.md
kind: founder_case
speakers: [{name: Hunter Isaacson, role: founder}, {name: Joseph Choi, role: host}]
bias: "Joseph Choi bán Superwall (paywall, tài trợ tập này) và điều hành Consumer Club; Hunter là thành viên Consumer Club. Số liệu app là lời kể, không có dashboard."
analyzed: 2026-11-15
cases:
  - id: ngl
    depth: full
    product: "NGL (app nhắn tin ẩn danh gắn vào link story Instagram)"
    what: "Người nhận tin ẩn danh qua link trong story Instagram, trả lời rồi đăng lại thành story"
    type: [mobile-app]
    customer: "Thanh thiếu niên và sinh viên ở nhiều nước; đa số dùng free, một phần nhỏ trả gói tuần"
    founder: {who: Hunter Isaacson, base: null, technical: null, team: "Hunter cùng vài bạn bè lúc đầu", background: "Đã làm nhiều app social trước đó"}
    revenue: null
    pricing: "Gói subscription theo tuần, giá khác nhau theo vùng (theo GDP bình quân), khoảng 1–7 USD; phần lớn người dùng dùng free"
    idea_origin: [timing_trigger, adjacent_expansion]
    scale_channels: [tiktok_organic, word_of_mouth]
    community_at_discovery: null
    demand_signal: {kind: built_first, level: 0, what: "Build app khoảng một tháng, rồi gần 6 tháng không ai dùng", q: "We built the app in about a month, but then it was like 6 months of nobody using it.", ts: "00:02:38"}
    prior_failures: {count: null, what: "6 tháng đầu rất khó khăn: thử nhiều cách, đổi thiết kế và đổi tên app", q: "That 6 months was very hard. We tried a lot of different things.", ts: "00:02:58"}
    unfair_advantage:
      - {value: domain_expertise, what: "Hunter tự nhận giỏi hiểu hành vi người dùng trên mạng xã hội", q: "I think that's why I've been successful in social because I'm really good at understanding", ts: "00:01:41"}
      - {value: prior_success, what: "Hơn 70 triệu lượt tải từ các app trước đó (video không nói về exit)", q: "Prior to NGL, I had like over 70 million downloads on other apps that I had built", ts: "00:07:38"}
    time_to_revenue:
      first_dollar: null
      to_1k_mrr: null
      to_10k_mrr: null
      to_current: null
    first_users:
      - {channel: influencer_paid, what: "Trả influencer đăng link lên story; khoảng 4 tháng sau có một đợt lan nhỏ từ một influencer ở nước khác", q: "it was from an influencer who we paid to post the link", ts: "00:03:06"}
      - {channel: tiktok_organic, what: "Một TikTok viral đưa khoảng 1.000 người dùng trong một ngày (video không nói TikTok đó có trả tiền hay không)", q: "And that's what activated like our first thousand users in one day was from that Tik Tok.", ts: "00:04:47"}
    build: {time: "khoảng một tháng để làm bản app đầu tiên", cut: [], q: "We built the app in about a month", ts: "00:02:38"}
  - id: zoom-university
    depth: mention
    product: "Zoom University (app hẹn hò đôi cho sinh viên đại học)"
    what: "Hai bạn gái và hai bạn trai vào ghép đôi; cả hai bên phải cùng đồng ý mới ghép"
    demand_signal: {kind: self_reported_pain_or_free_waitlist, level: 4, what: "Waitlist khoảng 40.000 người sau khi đăng nội dung meme về ý tưởng", q: "we had a weight list of like 40,000 people", ts: "00:14:55"}
  - id: wink
    depth: mention
    product: "Wink (app kết bạn kiểu vuốt, thêm người qua Snapchat)"
    what: "Vuốt người để thêm họ vào Snapchat thay vì thêm trong app"
steps:
  - {stage: find-idea, ts: "00:02:04", case: ngl, what: "Instagram vừa mở tính năng link cho mọi người; nhóm Hunter quyết định làm sản phẩm ngay trên tính năng đó.", tactic: s12-timing-shift}
  - {stage: find-idea, ts: "00:11:22", case: ngl, what: "Lấy ý tưởng nhắn tin ẩn danh đã có sẵn (YOLO, Yik Yak, Formspring) rồi chuyển sang Instagram, kênh phân phối lớn hơn.", tactic: s11-copy-or-localize-proven, tactic_note: "Ý tưởng cũ đã có người dùng + đổi kênh phân phối sang Instagram graph"}
  - {stage: validate, ts: "00:14:55", case: zoom-university, what: "Đăng nội dung meme về ý tưởng hẹn hò đôi trên các trang meme; thu waitlist khoảng 40.000 người (video không nói rõ lúc đó đã có app chưa).", tactic: s8-content-demand-test, tactic_note: "Đăng meme về ý tưởng, đếm waitlist"}
  - {stage: launch, ts: "00:03:06", case: ngl, what: "Trả vài influencer, mỗi người khoảng 100 USD, để đăng link NGL lên story nhằm kích hoạt graph.", tactic: g7-creator-ops, cost: "khoảng $100 mỗi người"}
  - {stage: launch, ts: "00:04:28", case: ngl, what: "Thử nhiều tin nhắn gây tranh cãi, hài hước làm nội dung TikTok; một video viral đưa khoảng 1.000 người dùng trong một ngày.", tactic: g3-organic-content-formats}
  - {stage: monetize, ts: "00:06:11", case: ngl, what: "Bán gói tuần theo vùng, giá theo GDP bình quân; chỉ một tỉ lệ nhỏ người dùng trả tiền, chủ yếu là power user.", tactic: g4-pricing-paywall}
  - {stage: grow, ts: "00:05:16", case: ngl, what: "Người đã rời app vẫn quay lại vì bạn bè tiếp tục đăng link NGL nên tỉ lệ tải lại cao.", tactic: g10-referral-viral-loop}
  - {stage: grow, ts: "00:10:36", case: ngl, what: "Đổi nút chia sẻ thành 'get your own messages' thay vì 'tải app'; tỉ lệ người từ màn này sang App Store rất cao.", tactic: g3-organic-content-formats}
quotes:
  - {ts: "00:02:38", who: Hunter Isaacson, stage: launch, theme: [], text: "So it's like our assumption that everybody saw the opportunity was like so wrong.", vi: "Chúng tôi đã nghĩ ai cũng thấy cơ hội, giả định đó sai hoàn toàn."}
  - {ts: "00:02:58", who: Hunter Isaacson, stage: mindset, theme: [persistence], text: "That 6 months was very hard. We tried a lot of different things.", vi: "6 tháng đó rất khó. Chúng tôi thử rất nhiều cách."}
  - {ts: "00:10:36", who: Hunter Isaacson, stage: grow, theme: [], text: "And it's way easier to get a download by saying get your own messages than saying, hey, download this app.", vi: "Dễ được tải app hơn nhiều khi nói 'get your own messages' thay vì 'tải app này'."}
  - {ts: "00:14:15", who: Hunter Isaacson, stage: mindset, theme: [passion-fuel], text: "Even though this app failed, I just loved the process of designing it so much that I realized that like this is what I should be doing with my life.", vi: "Dù app đó thất bại, tôi yêu quá trình thiết kế đến mức nhận ra đó là việc tôi nên làm cả đời."}
  - {ts: "00:27:58", who: Hunter Isaacson, stage: grow, theme: [], text: "Don't spend all the money on like, you know, one specific creative. I would just test like a dozen of them.", vi: "Đừng dồn tiền vào một creative; tôi sẽ thử cả chục cái."}
  - {ts: "00:29:27", who: Hunter Isaacson, stage: mindset, theme: [persistence], text: "It's a fun industry because you're constantly able to take L's and like just redo it again.", vi: "Đây là ngành vui vì bạn liên tục thua và được làm lại."}
rules:
  - {ts: "00:11:22", who: Joseph Choi, stage: launch, theme: [right-audience], text: "So I feel like nailing that first kind of core set of users is really important.", vi: "Tôi nghĩ việc làm chắc nhóm người dùng đầu tiên rất quan trọng.", evidence: opinion}
  - {ts: "00:10:15", who: Joseph Choi, stage: grow, theme: [], text: "When you think about it, the result of that call to action, you sell the end result, right?", vi: "Khi nghĩ kỹ, lời kêu gọi hành động đó bán kết quả cuối cùng, đúng không.", evidence: opinion}
numbers:
  - {ts: "00:01:17", metric: "người dùng hoạt động hàng tháng của NGL", value: 150000000, unit: count, evidence: claimed}
  - {ts: "00:06:11", metric: "doanh thu NGL", value: "multi-8 figure mỗi năm (không có con số cụ thể)", unit: usd_per_year, evidence: claimed}
  - {ts: "00:16:33", metric: "lượt tải app Wink (app trước đó)", value: 70000000, unit: count, evidence: claimed}
frameworks: [content-before-product, many-small-bets]
idea_patterns: [adjacent-platform-expansion, single-feature-on-platform]
---

## Một câu

Hunter Isaacson kể về NGL, app nhắn tin ẩn danh gắn vào link story Instagram: ý tưởng bắt nhịp một thay đổi nền tảng, 6 tháng đầu không ai dùng, rồi một TikTok viral đưa khoảng 1.000 người dùng trong một ngày.

## Bài học cho tôi

- Bắt nhịp thay đổi nền tảng: Instagram mở link cho mọi người là lúc nhóm làm NGL bắt đầu (`00:02:04`).
- Build xong rồi mới chờ thì 6 tháng không ai dùng (`00:02:38`).

## Đừng tin vội

- Hunter có hơn 70 triệu lượt tải từ các app trước, nên ông ấy không phải người mới; kinh nghiệm đó khó sao chép.
- Doanh thu NGL chỉ là "multi-8 figure" mỗi năm, không có con số cụ thể; không có dashboard. Video không nói TikTok viral là tự nhiên hay có trả tiền.
- NGL dựa trên Instagram graph. Video thừa nhận đây là nền tảng lớn; nếu nền tảng đổi quy tắc thì cơ chế này mất.
- Zoom University và Wink là lời kể (lượt tải, waitlist 40.000); waitlist không phải tiền. Chủ video bán paywall và tư vấn qua Consumer Club.
