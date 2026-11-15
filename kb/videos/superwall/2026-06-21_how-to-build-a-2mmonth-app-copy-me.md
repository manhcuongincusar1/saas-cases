---
schema: 2
video_id: GUkXzJ2S6Z8
channel: superwall
title: How to Build a $2M/Month App (Copy Me)
date: 2026-06-21
url: https://www.youtube.com/watch?v=GUkXzJ2S6Z8
transcript: superwall/youtube-transcript/superwall/how-to-build-a-2mmonth-app-copy-me/transcript.md
kind: expert_talk
speakers:
- name: Joseph Choi
  role: host
- name: Marcus Burke
  role: expert
bias: Marcus làm tư vấn Meta ads cho app (dịch vụ có tính phí), có link tư vấn/LinkedIn/Substack; video
  giới thiệu công cụ có link trong mô tả (Spy Talk, Rork có mã giảm giá) và kênh Superwall (paywall) cùng
  Consumer Club. Không nói có được trả tiền hay không.
analyzed: 2026-11-15
cases:
- id: moonate-creative
  depth: mention
  product: Moonate (app âm thanh, theo mô tả trong video)
  what: 'Concept quảng cáo ''quả cầu xanh'' cho Moonate: khoảng 400 phiên bản thử; chi hơn $1M cho riêng
    concept này (chi tiêu quảng cáo, không phải doanh thu)'
steps:
- stage: grow
  ts: 00:24:27
  what: 'Nghiên cứu copy trước khi viết quảng cáo: gom các thread Reddit có nhiều engagement, nhờ Claude
    tách sub-audience, nỗi đau và cách họ tự mô tả.'
  tactic: s3-reddit-pain-mining
  tactic_note: Dùng để viết copy quảng cáo, không phải chọn ý tưởng app
  tool: Reddit + Claude
- stage: grow
  ts: 00:25:43
  what: 'Nghiên cứu visual: xem ad library đối thủ, feed/Reels/Shorts và comment để tìm format trông tự
    nhiên trên đúng placement.'
  tactic: s4-tiktok-comment-mining
  tactic_note: Lấy format cho quảng cáo, không phải chọn ý tưởng; đây là bước thứ hai trong quy trình
    5 bước của Marcus
- stage: grow
  ts: 00:32:37
  what: Viết copy bằng Claude với file context riêng cho từng sub-audience (khoảng 5 nhóm), kèm mô tả
    sản phẩm, tính năng và social proof.
  tactic: other
  tactic_note: Chuẩn bị context file theo sub-audience trước khi nhờ LLM viết copy quảng cáo
  tool: Claude
- stage: grow
  ts: 00:35:25
  what: Sinh ảnh trước (GPT Image, Nano Banana) để chốt cảnh, rồi mới dùng ảnh đó làm tham chiếu cho video
    model; không prompt thẳng video model vì tốn credit.
  tactic: other
  tactic_note: 'Quy trình tạo creative AI: ảnh trước, video sau; chỉ nêu cách làm, không nêu chi phí thực
    tế'
  tool: GPT Image, Nano Banana, Higgsfield
- stage: grow
  ts: 00:47:48
  what: Tìm quảng cáo outlier (CPT tốt nhưng chạy chủ yếu trên Facebook feed) rồi tách ra ad set riêng
    để Meta không dồn tiền vào một quảng cáo.
  tactic: g6-paid-ads
  tactic_note: Phân tích phân bổ placement theo CPT để tách ad set; áp dụng cho Meta
  tool: Meta Ads Manager
- stage: grow
  ts: 00:50:40
  what: 'Chia account theo bucket: mỗi cụm (format/media + thông điệp) một ad set có ngân sách riêng,
    đặt mục tiêu cost-per-target cho từng bucket.'
  tactic: g6-paid-ads
  tactic_note: Cấu trúc ad set theo format và thông điệp, ép ngân sách vào từng nhóm (không để Meta chọn
    một nhóm)
  tool: Meta Ads Manager
quotes: []
rules:
- ts: 00:08:14
  who: Marcus Burke
  stage: grow
  theme: []
  text: One thing on the app side of things is that you want to prepare people for that they are going
    to land on the app store otherwise your install rate tends to suffer
  vi: Với quảng cáo app, phải báo trước cho người xem rằng họ sẽ được đưa tới App Store, nếu không tỉ
    lệ cài đặt giảm.
  evidence: opinion
- ts: 00:13:52
  who: Marcus Burke
  stage: grow
  theme:
  - right-audience
  text: So ultimately the algorithm is going to pick your targeting based on the engagement and conversion
    signal coming in.
  vi: Thuật toán tự chọn đối tượng theo tín hiệu tương tác và chuyển đổi; càng cụ thể về người nó nhắm
    càng đúng.
  evidence: opinion
- ts: 00:23:39
  who: Marcus Burke
  stage: grow
  theme:
  - action-over-research
  text: What we're doing in order to come up with an ad is first we spend most of the time on research
    which is I think where already a lot of this tends to go wrong where people they feel like I want
    to make an ad so they start going into like a generative AI tool and they start making ads.
  vi: Việc đầu tiên là dành phần lớn thời gian nghiên cứu; nhiều người sai ở đây khi mở công cụ AI để
    làm quảng cáo ngay.
  evidence: opinion
- ts: 00:43:03
  who: Marcus Burke
  stage: grow
  theme:
  - revenue-first
  text: A trial isn't a subscription. It doesn't mean you made any money.
  vi: Trial không phải gói đăng ký; có trial không có nghĩa là đã kiếm được tiền.
  evidence: opinion
- ts: 00:47:48
  who: Marcus Burke
  stage: grow
  theme: []
  text: If you compile all your ads in one adset, then Meta is going to not diversify for you.
  vi: Dồn mọi quảng cáo vào một ad set thì Meta không phân bổ đa dạng; nó sẽ dồn tiền vào một quảng cáo.
  evidence: opinion
- ts: 00:57:13
  who: Marcus Burke
  stage: grow
  theme:
  - right-audience
  text: So in the end, make sure that you talk to the people that are using your app because that can
    be very inspiring
  vi: Hãy nói chuyện với người đang dùng app; họ cho bạn ngôn ngữ để viết copy, đó là cách nhắm đúng người.
  evidence: opinion
numbers:
- ts: 00:00:00
  metric: năm chạy Meta ads (theo lời Marcus)
  value: 14
  unit: years
  evidence: claimed
- ts: 00:00:00
  metric: doanh thu/tháng từng đạt ở app Marcus từng scale (theo lời Marcus)
  value: 2000000
  unit: usd_per_month
  evidence: claimed
- ts: 00:09:51
  metric: số phiên bản thử của concept Moonate
  value: 400
  unit: count
  evidence: claimed
- ts: 00:10:32
  metric: chi tiêu quảng cáo trọn đời cho riêng concept Moonate (không phải doanh thu)
  value: 1000000
  unit: usd
  evidence: claimed
frameworks:
- organic-find-format-then-paid-scale
- right-audience-over-views
idea_patterns: []
---

## Một câu

Marcus Burke (14 năm chạy Meta ads cho app): quảng cáo app nên giống nội dung tự nhiên, nhắm đúng người bằng ngôn ngữ nỗi đau của họ, nghiên cứu copy trước khi viết, và chia ad set theo format/thông điệp để Meta không dồn tiền vào một quảng cáo.

## Bài học cho tôi

- Dành phần lớn thời gian nghiên cứu ngôn ngữ khách (Reddit, comment) trước khi nhờ AI viết quảng cáo (`00:23:39`).
- Chia ad set theo format và thông điệp, đặt ngân sách riêng cho từng nhóm để không bị dồn tiền vào một quảng cáo (`00:47:48`).

## Đừng tin vội

- Đây là lời khuyên của người bán dịch vụ Meta ads (tư vấn) cho app đã có quy mô lớn, không phải founder kể case của chính mình. Không có số doanh thu của app nào do founder tự báo cáo.
- "$1M" và "400 phiên bản" là chi tiêu và số lần thử cho một concept quảng cáo, không phải doanh thu; không biết concept đó đem về bao nhiêu.
- Chuyên môn là Meta ads cho app subscription (trial, value rules, CPT theo tuổi). Ví dụ con số (45+ "có thể giá trị hơn 30–40%") là minh hoạ, chưa kiểm chứng.
- Survivor bias: chỉ kể concept và tài khoản đã thắng; video không nói tỉ lệ thất bại hay chi phí tạo creative bằng AI.
- Video có công cụ được giới thiệu (Spy Talk, Rork, Superwall, Consumer Club) nên cần đọc các khuyến nghị công cụ với góc nhìn đó.
