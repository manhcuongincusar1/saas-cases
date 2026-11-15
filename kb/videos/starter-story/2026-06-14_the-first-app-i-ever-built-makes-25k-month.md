---
schema: 2
video_id: Q4k8JNYKJT0
channel: starter-story
title: "The First App I Ever Built Makes $25K/Month"
date: 2026-06-14
url: https://www.youtube.com/watch?v=Q4k8JNYKJT0
transcript: starter-story-kb/videos/2026-06-14_the-first-app-i-ever-built-makes-25k-month/transcript.md
kind: founder_case
speakers:
- {name: Kian, role: founder}
- {name: Pat Walls, role: host}
- {name: Gus, role: host}
bias: "Starter Story bán tài nguyên (guide '$1M Attention Guide' quảng cáo giữa video, có link trong mô tả) và chọn founder để kể; chỉ thấy một case đang thắng, không có số tháng sau. Số liệu đọc trên Stripe nhưng không có chi phí, churn hay tỉ lệ trả tiền."
analyzed: 2026-11-15
cases:
- id: toneadapt
  depth: full
  product: "ToneAdapt (toneadapt.com): chỉnh tone guitar theo bài hát và gear của người chơi"
  what: "Đưa cài đặt ampli, pickup, pedal để giống tone một bài hát, theo gear của người dùng; có web và app iOS"
  type: [web-app, mobile-app]
  customer: "Guitarist muốn có tone giống bài hát trên chính gear của mình; trả gói tuần hoặc năm"
  founder:
    who: Kian
    base: "San Diego, Mỹ (đang học CS tại San Diego State University, theo transcript)"
    technical: false
    team: null
    background: "Sinh viên CS, chưa từng build gì trước đó; làm UGC cho brand; chơi guitar hằng ngày"
  revenue:
    amount: 25000
    unit: usd
    basis: last_28_days
    note: "Web + app trong 4 tuần gần nhất; web ~$11.5k (Stripe), app ~$14k, theo lời founder đọc từ dashboard"
    q: "we've done over $25,000 in the past"
    ts: "02:22"
    evidence: measured
  pricing: "Hai gói: tuần $10 và năm khoảng $60/năm, dùng cho cả web và app"
  idea_origin: [own_pain, passion_skin]
  scale_channels: [founder_led_content, tiktok_organic, instagram_reels, youtube_founder]
  community_at_discovery:
    value: "Guitarist đang chơi hằng ngày; dùng ChatGPT lấy tone nhưng không chính xác, hỏi người chơi khác trên mạng"
    insider: true
    q: "I was using ChatGPT at the time to figure out how to get guitar tones, but it wasn't really all that accurate."
    ts: "03:54"
  demand_signal:
    kind: self_reported_pain_or_free_waitlist
    level: 4
    what: "Guitarist trong comment Reddit và Instagram tự kể gặp đúng vấn đề, chưa có giải pháp; chưa có tiền trước khi build"
    q: "I talked to other guitarists on Reddit, on Instagram, mainly in comment sections, and many of them had the exact"
    ts: "03:54"
  prior_failures: null
  unfair_advantage:
  - {value: domain_expertise, what: "Chơi guitar gần như mỗi ngày hơn một năm trước khi build", q: "I've been playing the guitar almost every day for over a year", ts: "08:43"}
  time_to_revenue:
    first_dollar: null
    to_1k_mrr: null
    to_10k_mrr: null
    to_current: {months: 5, value: "dưới 5 tháng từ lúc build tới $25k/tháng", q: "in under 5 months by just vibe coding and posting on social media", ts: "01:19"}
  first_users:
  - {channel: founder_led_content, what: "Video đầu tiên về app viral qua đêm; founder đưa mặt mình lên từ đầu", q: "The first video I actually ever posted about Tone Adapt went viral overnight.", ts: "06:56"}
  - {channel: tiktok_organic, what: "Đăng 3 video/ngày, repost sang Instagram, TikTok, YouTube, Facebook; video không tách được nền tảng nào mang người dùng đầu tiên", q: "I posted media three times a day, reposted across as many platforms as I can", ts: "07:12"}
  build:
    time: "khoảng 1 tuần cho bản web V1; founder ước hiện nay vài giờ"
    cut: []
    q: "it took me about a week to build everything"
    ts: "05:26"
steps:
- stage: monetize
  ts: "02:06"
  case: toneadapt
  what: "Hai gói: tuần $10 và năm khoảng $60, bán trên cả web và app."
  tactic: g4-pricing-paywall
- stage: find-idea
  ts: "03:38"
  case: toneadapt
  what: "Cần project cho CV khi chưa có thực tập, nên chọn thứ mình đang chơi hằng ngày là guitar để tìm nỗi đau."
  tactic: s5-insider
  tactic_note: "Loại: pain (nỗi đau khi chơi guitar) và đam mê guitar của chính founder"
- stage: find-idea
  ts: "03:54"
  case: toneadapt
  what: "Hỏi guitarist trên Reddit và trong comment Instagram; nhiều người gặp đúng vấn đề và chưa có giải pháp."
  tactic: s3-reddit-pain-mining
  tactic_note: "Hỏi trực tiếp trong comment Instagram của người chơi guitar, không chỉ đọc"
- stage: build
  ts: "05:26"
  case: toneadapt
  what: "Build bản web V1 trong khoảng 1 tuần, code do AI viết (vibe coding); sau đó làm app iOS."
- stage: monetize
  ts: "06:11"
  case: toneadapt
  what: "Dùng Superwall cho paywall và A/B test các thí nghiệm giá/paywall trên app."
  tactic: g4-pricing-paywall
  tactic_note: "A/B test paywall bằng Superwall"
  tool: Superwall
- stage: grow
  ts: "07:12"
  case: toneadapt
  what: "Đăng 3 video/ngày trên Instagram, TikTok, YouTube, Facebook; đưa mặt founder lên ngay từ ngày đầu để xây niềm tin."
  tactic: g3-organic-content-formats
  threshold: "3 video/ngày"
- stage: grow
  ts: "07:27"
  case: toneadapt
  what: "Khi một format có chuyển đổi, nhân mạnh format đó thay vì làm lại từ đầu."
  tactic: g3-organic-content-formats
quotes:
- ts: "07:58"
  who: Kian
  stage: mindset
  theme: [ship-ugly]
  text: "once you get over that first video and it's on the internet for everyone to see, you realize it doesn't actually matter"
  vi: "Sau khi vượt qua video đầu tiên và nó đã lên mạng cho mọi người xem, bạn sẽ thấy điều đó không thực sự quan trọng."
- ts: "08:28"
  who: Kian
  stage: find-idea
  theme: []
  text: "I would tell them to pick a hobby or a niche that they already know."
  vi: "Tôi sẽ bảo họ chọn một sở thích hoặc ngách mà họ đã biết."
- ts: "08:43"
  who: Kian
  stage: find-idea
  theme: []
  text: "you understand and face the exact pain points that you're trying to solve without doing any market research."
  vi: "Bạn hiểu và trực tiếp gặp nỗi đau mình muốn giải quyết mà không cần nghiên cứu thị trường."
- ts: "09:45"
  who: Kian
  stage: find-idea
  theme: []
  text: "there are at least thousands if not tens of thousands of people out there with the exact same problem that you have."
  vi: "Nếu bạn có một vấn đề nhỏ, có ít nhất hàng nghìn người khác đang gặp đúng vấn đề đó."
- ts: "10:18"
  who: Kian
  stage: launch
  theme: [sell-before-build, ship-ugly]
  text: "Don't spend hours picking a logo, don't polish anything, just build something, put it on the internet and charge money for it. You'll be getting revenue from day one and feedback for improvements when you eventually build out the mobile app."
  vi: "Đừng mất hàng giờ chọn logo, đừng đánh bóng gì; cứ build, đưa lên mạng và thu tiền. Bạn có doanh thu từ ngày đầu và có phản hồi để cải thiện khi làm app di động."
- ts: "10:35"
  who: Kian
  stage: grow
  theme: [persistence]
  text: "Commit to posting three times every single day for at least a month and I guarantee you will make money and get users."
  vi: "Cam kết đăng ba lần mỗi ngày ít nhất một tháng, tôi đảm bảo bạn sẽ kiếm được tiền và có người dùng."
- ts: "11:20"
  who: Kian
  stage: grow
  theme: [focus-one-thing]
  text: "Once you find this format that converts, you need to ride it until it dies."
  vi: "Khi đã tìm được format chuyển đổi, hãy đi theo nó tới khi nó hết tác dụng."
- ts: "14:26"
  who: Kian
  stage: mindset
  theme: [persistence]
  text: "It doesn't have to be for a specific product, or you don't have to be selling anything."
  vi: "Không cần phải là cho một sản phẩm cụ thể hay phải đang bán gì; cứ bắt đầu đăng lên mạng."
rules:
- ts: "14:41"
  who: "Pat Walls hoặc Gus"
  stage: grow
  theme: []
  text: "Feels like eight or nine out of 10 founders I ask"
  vi: "Cảm giác như 8–9 trên 10 founder được hỏi đều nói mạng xã hội là cách tăng trưởng."
  evidence: opinion
- ts: "15:57"
  who: "Pat Walls hoặc Gus"
  stage: validate
  theme: []
  text: "There are enough guitar players out there that want to match their tone and need to solve that problem enough to pay for it"
  vi: "Có đủ người chơi guitar muốn khớp tone và đủ cần giải quyết để trả tiền; ngách nhỏ vẫn đủ."
  evidence: opinion
- ts: "16:27"
  who: "Pat Walls hoặc Gus"
  stage: find-idea
  theme: []
  text: "as long as it solves like a painful problem even if it's just for you"
  vi: "Ý tưởng nào cũng tốt miễn là giải được một nỗi đau thật, kể cả chỉ là nỗi đau của chính mình."
  evidence: opinion
numbers:
- ts: "02:22"
  metric: "doanh thu web + app trong 4 tuần gần nhất (theo dashboard)"
  value: 25000
  unit: usd
  evidence: measured
- ts: "02:37"
  metric: "người đăng ký trả phí đang hoạt động trên app (sau khi ra mắt app)"
  value: 397
  unit: count
  evidence: measured
- ts: "02:37"
  metric: "subscriber mới trong 3 tháng qua (web)"
  value: 1400
  unit: count
  evidence: claimed
frameworks:
- one-feature-per-app
idea_patterns: []
---

## Một câu

Kian (sinh viên CS, từng làm UGC) chơi guitar mỗi ngày, thấy ChatGPT cho tone không chính xác, build web ToneAdapt trong khoảng 1 tuần rồi đăng 3 video/ngày; web + app đạt khoảng $25k trong 4 tuần theo dashboard Stripe.

## Bài học cho tôi

- Chọn nỗi đau từ thứ mình làm hằng ngày và hỏi người khác trong comment trước khi build (`03:54`, `08:43`).
- Đăng đều (3 video/ngày) và nhân format đã chuyển đổi, không dừng ở một video viral (`10:35`, `11:20`).

## Đừng tin vội

- Video là bản kể lúc đang thắng; không có tháng thất bại, chi phí quảng cáo, churn hay tỉ lệ người dùng trả tiền. "$25k" là doanh thu 4 tuần, chưa trừ chi phí.
- Điều kiện riêng: founder đã có nền UGC và chơi guitar hằng ngày, sẵn lòng đăng mặt lên mạng từ đầu. Ngách guitar nhỏ, và số app khác không được nêu.
- Host nói app đứng thứ 2 cho từ khoá "guitar tone" sau kết quả quảng cáo; thứ hạng đó không đo được tác động của đăng bài.
- Không biết sản phẩm giữ được doanh thu sau tháng đầu; "5 tháng" là khoảng thời gian founder tự nói.
