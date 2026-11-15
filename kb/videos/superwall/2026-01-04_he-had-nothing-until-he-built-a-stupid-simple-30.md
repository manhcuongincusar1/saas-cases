---
schema: 2
video_id: CyaWU1qxQg4
channel: superwall
title: he had nothing.. until he built a stupid simple $30k/mo app with AI
date: 2026-01-04
url: https://www.youtube.com/watch?v=CyaWU1qxQg4
transcript: superwall/youtube-transcript/superwall/he-had-nothing-until-he-built-a-stupid-simple-30kmo-app-with-ai/transcript.md
kind: founder_case
speakers:
- name: Dmitri
  role: founder
- name: Joseph Choi
  role: host
bias: Superwall (paywall) là nhà tài trợ của kênh; host Joseph Choi quảng bá Consumer Club, công cụ paywall
  experiment và Spytok. Số liệu của founder là tự báo, không mở dashboard.
analyzed: 2026-11-15
cases:
- id: yourmove-ai
  depth: full
  product: 'YourMove AI: AI gợi ý tin nhắn, viết hồ sơ, chọn và tạo ảnh cho người dùng app hẹn hò'
  what: Đọc tin nhắn từ app hẹn hò (Hinge) rồi gợi ý câu trả lời; sau đó viết và chấm hồ sơ, tạo ảnh AI
  type:
  - web-app
  customer: Người dùng app hẹn hò; soft paywall cho phần chat, hard paywall cho tạo ảnh AI
  founder:
    who: Dmitri
    base: New York (trước đó làm remote ở Mỹ Latinh)
    technical: true
    team: solo lúc đầu; về sau 10–12 contractor trên Upwork
    background: Kỹ sư cơ khí, làm tư vấn rồi strategy, data analyst; data science manager ở Open Door,
      làm side project nhiều năm
  revenue:
    amount: 30000
    unit: usd
    basis: best_month
    note: Đỉnh khoảng 30K/tháng (margin ~80%); lúc ngừng làm còn ~28K/tháng; đã bán công ty 4–5 tháng
      trước, giá không nêu
    q: at peak recently, it's been making 30K a month, about 80% margin
    ts: 00:03:09
    evidence: claimed
  pricing: Soft paywall cho sản phẩm chính; hard paywall cho tính năng tạo ảnh AI vì chi phí compute cao
  idea_origin:
  - own_pain
  - timing_trigger
  scale_channels:
  - seo
  - paid_google
  community_at_discovery:
    value: Đang ở trong nhóm người dùng hẹn hò (muốn nhờ AI nhắn tin trên app hẹn hò), bạn bè cũng vậy
    insider: true
    q: I was like actually what if I use this uh to text on dating apps
    ts: 00:05:02
  demand_signal:
    kind: friends_praise
    level: 1
    what: Bản thử làm trong một cuối tuần, đưa lên web; nhiều bạn bè xin dùng ngay
    q: there was like a lot of friends that were like, "Wait, can I use this?
    ts: 00:05:42
  prior_failures:
    count: 3
    what: 3 dự án trước thất bại hoàn toàn; dự án đầu có TAM dưới 1 triệu USD
    q: I tried like three different things, all of which failed catastrophically
    ts: 00:34:52
  unfair_advantage:
  - value: technical_skill
    what: Biết Python và ML, tự build được phần AI
    q: I knew how to build the AI stuff cuz I knew Pi like I knew Python
    ts: 00:10:09
  - value: luck
    what: Tự nhận là may mắn khi nói về tăng trưởng của công ty này
    q: the honest answer um with this particular company is I I got lucky
    ts: 00:11:46
  time_to_revenue:
    first_dollar:
      months: 6
      value: Khoảng 6 tháng từ lúc bắt đầu build tới khi bắt đầu thu tiền
      q: it took me like 6 months to even monetize
      ts: 00:06:35
    to_1k_mrr: null
    to_10k_mrr: null
    to_current:
      months: 30
      value: Khoảng 2,5 năm (tới mức ~28–30K/tháng)
      q: This took me like two and a half years
      ts: 00:07:28
  first_users:
  - channel: reddit
    what: Đăng trong vài subreddit nhỏ về tối ưu hẹn hò; nhận được chú ý ban đầu
    q: I started posting on those and I got some early attention on those
    ts: 00:12:59
  build:
    time: Một cuối tuần cho bản thử đầu tiên; sau đó khoảng 6 tháng tới khi thu tiền
    cut: []
    q: spent a weekend seeing if we could get the uh then like GBT2 AI to flirt
    ts: 00:05:02
steps:
- stage: find-idea
  ts: 00:05:02
  case: yourmove-ai
  what: Tự thấy mình tán tỉnh kém nên dựng bản thử một cuối tuần để AI gợi ý tin nhắn trên app hẹn hò.
  tactic: s5-insider
  tactic_note: Nỗi đau riêng (tán tỉnh kém), founder là người dùng app hẹn hò
- stage: find-idea
  ts: 00:03:45
  case: yourmove-ai
  what: Làm sản phẩm trên đợt AI mới (Davinci-2, trước ChatGPT) khi gần như chưa ai làm; đi sớm nhưng
    chưa chiếm được nhiều thị phần.
  tactic: s12-timing-shift
- stage: validate
  ts: 00:05:42
  case: yourmove-ai
  what: Đưa bản thử còn thô lên web; bạn bè xin dùng ngay, không cần sản phẩm hoàn chỉnh.
  tactic: other
  tactic_note: Ship bản thô, không thu tiền, đếm người xin dùng (không phải pre-order)
- stage: launch
  ts: 00:12:09
  case: yourmove-ai
  what: Phát tờ rơi ở công viên Washington Square; không hiệu quả.
  tactic: other
  tactic_note: Phát tờ rơi offline tại công viên
- stage: launch
  ts: 00:12:59
  case: yourmove-ai
  what: Đăng trong vài subreddit nhỏ về tối ưu hẹn hò; nhận được chú ý ban đầu và các bài đó còn mang
    SEO.
  tactic: g1-first-10-users
  tactic_note: Subreddit nhỏ đúng nhóm người dùng
- stage: launch
  ts: 00:13:26
  case: yourmove-ai
  what: Báo chí lớn (WSJ, Washington Post, Fox Business...) đưa tin vì sản phẩm mới lạ; lượng khách từ
    PR ít nhưng cho domain authority.
  tactic: g14-press-pr
  tactic_note: PR báo chí tự đến do sản phẩm AI mới, không nêu trả tiền
- stage: monetize
  ts: 00:06:35
  case: yourmove-ai
  what: 'Sau khoảng 6 tháng mới thu tiền: soft paywall cho sản phẩm chính, hard paywall cho tạo ảnh AI.'
  tactic: g4-pricing-paywall
- stage: grow
  ts: 00:14:25
  case: yourmove-ai
  what: Viết blog nhắm các từ khoá cạnh tranh thấp mà volume cao; nội dung đó kéo gần nửa traffic.
  tactic: g2-aso-seo-organic
- stage: grow
  ts: 00:15:09
  case: yourmove-ai
  what: Chạy Google Ads cho nhiều sản phẩm; có cái hiệu quả, có cái không chạy được.
  tactic: g6-paid-ads
- stage: scale
  ts: 00:43:18
  case: yourmove-ai
  what: Thuê 10–12 contractor trên Upwork (email, SEO, ads, thiết kế, hỗ trợ khách), phần lớn vài giờ
    mỗi tuần, trả bằng lương công việc chính.
- stage: scale
  ts: 00:07:03
  case: yourmove-ai
  what: Đã bán công ty 4–5 tháng trước; video không nêu giá bán.
quotes:
- ts: 00:05:42
  who: Dmitri
  stage: validate
  theme: []
  text: I've never felt that like that pull.
  vi: 'Tôi chưa bao giờ thấy sức kéo như vậy: không phải mình đẩy người ta dùng, mà họ đòi dùng.'
- ts: 00:10:39
  who: Dmitri
  stage: mindset
  theme:
  - learn-from-others
  text: I think the biggest failure point that I see is people trying to take lessons from big tech and
    apply it here
  vi: Điểm thất bại lớn nhất tôi thấy là người ta đem bài học từ big tech áp vào đây.
- ts: 00:12:23
  who: Dmitri
  stage: launch
  theme: []
  text: This was before most people had been exposed to AI, so most people that saw the product like were
    super excited about it.
  vi: Lúc đó hầu hết người chưa tiếp xúc với AI, nên ai thấy sản phẩm cũng rất hào hứng.
- ts: 00:49:58
  who: Dmitri
  stage: mindset
  theme:
  - passion-fuel
  text: Like building this stuff is so much fun.
  vi: Xây những thứ này vui quá.
- ts: 00:51:01
  who: Dmitri
  stage: mindset
  theme:
  - revenue-first
  text: I told myself that once it was making like 20,000 a month and quit.
  vi: 'Tôi tự nhủ: khi nó đạt khoảng 20.000 đô/tháng thì nghỉ việc.'
- ts: 00:51:54
  who: Dmitri
  stage: mindset
  theme:
  - emotional-bottleneck
  text: I found it very very terrifying to like leave something that was like secure up until I knew that
    like I had like something resembling an infinite runway.
  vi: Tôi thấy rất đáng sợ khi rời một thứ đang an toàn, cho tới khi có một đường băng gần như vô hạn.
rules:
- ts: 00:06:10
  who: Joseph Choi
  stage: validate
  theme:
  - revenue-first
  text: To me, that's a strong signal that it's highly monetizable, too, cuz it sounds like people have
    it's like very high intent.
  vi: Với tôi, đó là tín hiệu mạnh rằng sản phẩm dễ kiếm tiền, vì người ta có ý định mua rất cao.
  evidence: opinion
- ts: 00:21:30
  who: Joseph Choi
  stage: grow
  theme: []
  text: I think a lot of people try to just randomly try every channel, but it's important to remember
    what the purpose of each channel is.
  vi: Nhiều người thử ngẫu nhiên mọi kênh; điều quan trọng là nhớ mỗi kênh dùng để làm gì.
  evidence: opinion
- ts: 00:29:13
  who: Joseph Choi
  stage: find-idea
  theme:
  - revenue-first
  text: I would just start with a painkiller problem and solution rather than trying to go after something
    that has less of that extreme uh pain point
  vi: Nếu mới bắt đầu, tôi sẽ chọn vấn đề kiểu thuốc giảm đau thay vì thứ có nỗi đau nhẹ hơn.
  evidence: opinion
numbers:
- ts: 00:03:09
  metric: MRR đỉnh (margin ~80%)
  value: 30000
  unit: usd_per_month
  evidence: claimed
- ts: 00:07:03
  metric: doanh thu khi founder ngừng làm
  value: 28000
  unit: usd_per_month
  evidence: claimed
- ts: 00:53:15
  metric: lợi nhuận hàng tháng khi quit (sau khi trả chi phí)
  value: 10000
  unit: usd_profit_per_month
  evidence: claimed
- ts: 00:06:35
  metric: tháng từ lúc build tới khi bắt đầu thu tiền
  value: 6
  unit: months
  evidence: claimed
- ts: 00:14:25
  metric: tỉ lệ traffic đến từ blog SEO
  value: gần 50%
  unit: ratio
  evidence: claimed
frameworks:
- seo-landing-page
idea_patterns: []
---
## Một câu

Dmitri làm YourMove AI, một công cụ AI gợi ý tin nhắn hẹn hò, từ một bản thử làm trong một cuối tuần; mất khoảng 6 tháng mới thu tiền và khoảng 2,5 năm mới tới mức ~30K/tháng (tự báo), nhờ blog SEO và PR.

## Bài học cho tôi

- Ý tưởng bắt đầu từ nỗi đau riêng (tán tỉnh kém) cộng với một đợt AI mới; bản thử thô đã có bạn bè xin dùng ngay (`00:05:02`, `00:05:42`).
- Kênh bền nhất là SEO trên từ khoá cạnh tranh thấp, volume cao; PR lớn nhưng ít khách trực tiếp (`00:14:25`, `00:13:26`).

## Đừng tin vội

- Số liệu (30K đỉnh, 28K, 10K lợi nhuận) là tự báo, host không yêu cầu mở dashboard. Founder có nói "I can pull it up on Stripe" nhưng không mở.
- Transcript lỗi số ("$,000", "a,000 bucks", "like 10"), nên mốc 1K và 10K MRR để null; "6 tháng" và "2,5 năm" là lời kể.
- Founder tự nhận "I got lucky" và "we were early to this" (đợt AI 2022–2023). Đây là thời điểm không lặp lại được, và công ty có sẵn kỹ năng Python/ML.
- Video không nói chi phí, churn, tỉ lệ người trả tiền, hay nguồn khách đầu tiên ngoài subreddit và PR.
- Việc bán công ty và mức thu được là lời kể, không có giá bán để kiểm.
- Superwall tài trợ kênh và host quảng bá sản phẩm của mình (bias).
