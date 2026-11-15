---
schema: 2
video_id: tv5hEdmbUTM
channel: superwall
title: How to Build an $18M/Year Apple Watch App (FREE MASTERCLASS)
date: 2026-08-30
url: https://www.youtube.com/watch?v=tv5hEdmbUTM
transcript: superwall/youtube-transcript/superwall/how-to-build-an-18myear-apple-watch-app-free-masterclass/transcript.md
kind: expert_talk
speakers:
- name: Joseph Choi
  role: host
- name: Assia Poloni
  role: expert
bias: Podcast của Superwall (tài trợ paywall tool) và Consumer Club (host điều hành) được quảng bá giữa
  video. Nhân vật là CPO của công ty 10 năm tuổi, không phải founder kể khởi nghiệp. Số liệu là lời kể,
  không có dashboard.
analyzed: 2026-11-15
cases:
- id: welltory
  depth: mention
  product: Welltory (đọc tín hiệu Apple Watch để chỉ ra lúc nào năng lượng bị rút)
  what: App sức khoẻ ~10 năm tuổi; onboarding xin đồng bộ dữ liệu sức khoẻ, cho người dùng thấy stress
    trên chính dữ liệu của họ, rồi dẫn tới paywall
  revenue:
    amount: 18000000
    unit: other
    basis: arr
    note: 'ARR ~18 triệu, ~18 triệu lượt tải; video không nêu tiền tệ (unit gốc: unspecified)'
    q: Our ARR is around 18 million and we have about 17 million downloads.
    ts: 00:00:00
    evidence: claimed
  pricing: Gần như chỉ bán gói năm (CPO đọc 99,99/năm, quy đổi ~8,83/tháng); đôi khi có gói tháng; không
    có trial
  scale_channels:
  - paid_meta
steps:
- stage: monetize
  ts: 00:26:52
  case: welltory
  what: Màn đầu của onboarding là nút kết nối dữ liệu sức khoẻ, đặt trước mọi màn giới thiệu; CPO nói
    trên 90% người dùng kết nối.
  tactic: g4-pricing-paywall
  tactic_note: 'Onboarding dẫn tới trả tiền: CTA đầu tiên là cấp quyền dữ liệu, không phải tính năng'
- stage: monetize
  ts: 00:35:18
  case: welltory
  what: Paywall thử lời hứa lợi ích (năng lượng, cảm thấy tốt hơn) thì kém hơn; câu 'bạn sẽ mất gì ngay
    bây giờ' bán tốt hơn.
  tactic: g4-pricing-paywall
- stage: monetize
  ts: 00:39:30
  case: welltory
  what: Gần như chỉ bán gói năm, không có trial; paywall cứng nhưng người dùng vẫn có thể đóng.
  tactic: g4-pricing-paywall
- stage: grow
  ts: 00:06:21
  case: welltory
  what: 'Quảng cáo Meta: lời hứa lợi ích dài hạn kém hiệu quả, nên hook bằng ''có gì đó đáng sợ đang diễn
    ra trong cơ thể bạn'' (cortisol, động mạch).'
  tactic: g6-paid-ads
  tactic_note: Quảng cáo trả tiền trên Meta, hook nỗi sợ trong cơ thể thay vì lợi ích
- stage: retain
  ts: 00:40:27
  case: welltory
  what: Hơn 60% chuyển đổi xảy ra trong vài tháng sau ngày đầu; theo host, app chủ động đưa số liệu của
    ngày hôm đó để kéo người dùng quay lại.
  tactic: g5-retention
quotes: []
rules:
- ts: 00:18:27
  who: Assia Poloni
  stage: monetize
  theme: []
  text: The formula, I think has to have six key ingredients, especially during the onboarding. You have
    to understand the human problem. You have to make some sort of product promise that makes people keep
    going.
  vi: Công thức onboarding có sáu thành phần; thành phần đầu là hiểu vấn đề của con người, rồi đến lời
    hứa khiến người ta đi tiếp.
  evidence: opinion
- ts: 00:20:28
  who: Assia Poloni
  stage: monetize
  theme: []
  text: that is the biggest mistake we make is not spending enough time really describing the human problem
  vi: Sai lầm lớn nhất khi viết pitch là không mô tả đủ vấn đề của con người, không hiểu nó ở tầng cảm
    xúc.
  evidence: opinion
- ts: 00:23:11
  who: Assia Poloni
  stage: monetize
  theme: []
  text: I think the most powerful proof that we use actually is that we are showing you your own data.
  vi: Bằng chứng mạnh nhất là cho người dùng thấy chính dữ liệu của họ, không phải social proof.
  evidence: opinion
- ts: 00:27:13
  who: Assia Poloni
  stage: monetize
  theme: []
  text: I think probably we haven't tested it enough, but every time I tried to like do like a little
    like prelude, it didn't do as well.
  vi: Chưa test đủ, nhưng mỗi lần thêm màn mở đầu dài thì chuyển đổi kém hơn, nên CTA đi thẳng vào.
  evidence: opinion
- ts: 00:35:18
  who: Assia Poloni
  stage: monetize
  theme: []
  text: I think with the onboarding when you want people to buy, I don't want to say this is kind of mean,
    but scare tactics, like what you're going to lose right here and now works a little bit better.
  vi: Khi muốn người ta mua trong onboarding, lời kiểu 'bạn sẽ mất gì ngay bây giờ' hiệu quả hơn, dù nghe
    hơi gắt.
  evidence: opinion
- ts: 00:40:27
  who: Assia Poloni
  stage: retain
  theme: []
  text: we're quite unique in that sense in that most of our conversions don't happen on day one, which
    is a bit unusual for health and fitness apps.
  vi: Khác đa số app sức khoẻ, phần lớn chuyển đổi của họ không xảy ra ngày đầu.
  evidence: opinion
numbers:
- ts: 00:27:29
  metric: người dùng kết nối dữ liệu sức khoẻ ở màn đầu (lời CPO)
  value: '>90%'
  unit: ratio
  evidence: claimed
- ts: 00:40:27
  metric: tỉ lệ chuyển đổi xảy ra sau ngày đầu, trong vài tháng (lời CPO)
  value: '>60%'
  unit: ratio
  evidence: claimed
- ts: 00:21:46
  metric: phút stress trong dữ liệu mẫu dùng để minh hoạ onboarding
  value: 192
  unit: minutes
  evidence: claimed
frameworks:
- funnel-message-consistency
- annual-plan-push
- product-as-main-character
idea_patterns: []
---
## Một câu

Welltory (app đọc dữ liệu Apple Watch, khoảng 18 triệu ARR sau 10 năm) dẫn người dùng qua onboarding bằng chính dữ liệu của họ, bán nỗi sợ "mất gì ngay bây giờ" thay vì lời hứa lợi ích, và phần lớn chuyển đổi đến sau ngày đầu.

## Bài học cho tôi

- Đưa bằng chứng từ chính dữ liệu của người dùng lên trước khi bán; CPO nói cách này mạnh hơn đánh giá sao hay số người dùng (`00:23:11`).
- Ở paywall, thử lời hứa lợi ích thì kém hơn nỗi sợ mất mát ngay bây giờ (`00:35:18`).

## Đừng tin vội

- Người kể là CPO, không phải founder: không có chi phí, thời gian build, số khách trả đầu tiên hay kênh người dùng đầu tiên. ARR 18 triệu và 18 triệu lượt tải là lời kể, không có dashboard, và video không nêu tiền tệ.
- Superwall (tài trợ kênh, `00:02:14`) và Consumer Club (`00:01:47`) được quảng bá giữa video. Chính CPO cũng nói họ "chưa test đủ" CTA đi thẳng (`00:27:13`), nên đây là chuỗi thử nghiệm kéo dài của một app đã lớn, không phải bằng chứng đối chứng.
- Điều kiện riêng: app có nguồn dữ liệu Apple Watch để cho người dùng thấy stress của chính họ ngay trong onboarding. Một app không có nguồn dữ liệu đó không sao chép được phần bằng chứng này.
