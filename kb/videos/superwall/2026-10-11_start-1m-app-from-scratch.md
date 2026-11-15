---
schema: 2
video_id: TCRUvJ-Fq9U
channel: superwall
title: If I Had to Start a $1M App From Scratch, I'd Do This
date: 2026-10-11
url: https://www.youtube.com/watch?v=TCRUvJ-Fq9U
transcript: superwall/youtube-transcript/superwall/if-i-had-to-start-a-1m-app-from-scratch-id-do-this/transcript.md
kind: host_essay
speakers:
- name: Joseph Choi
  role: host
bias: 'Kịch bản giả định (app cai thói quen), không phải chuyện có thật. Video kết bằng lời mời buổi live
  miễn phí 12/10 (không ghi lại): phễu tiềm năng cho host; video không nói bán gì trong buổi đó. Số liệu
  về tổng doanh thu và số founder là tự nói.'
analyzed: 2026-11-15
cases: []
steps:
- stage: find-idea
  ts: 00:00:30
  what: Vào top charts App Store, tìm app giải đúng một vấn đề cụ thể (máy quét thẻ bóng chày, cai thuốc);
    không chép app phổ biến nhất.
  tactic: s1-revenue-spy
  tool: App Store top charts
- stage: find-idea
  ts: 00:00:47
  what: 'Tra Sensor Tower để ước download và doanh thu của ngách: xem ngách có tiền thật hay không và
    có bao nhiêu người quan tâm.'
  tactic: s1-revenue-spy
  tool: Sensor Tower
- stage: find-idea
  ts: 00:00:47
  what: 'Đọc review của người dùng: họ thích gì, bực gì, nhóm nào chưa được phục vụ tốt.'
  tactic: s3-competitor-reviews
- stage: validate
  ts: 00:01:09
  what: 'Lên TikTok/Instagram xem khán giả ngách đang xem gì, rồi đọc comment: họ hỏi cách giải, kể nỗi
    đau hay chỉ cười? Video hài nhiều view chưa chắc bán được.'
  tactic: s4-tiktok-comment-mining
  tool: TikTok, Instagram
- stage: validate
  ts: 00:01:52
  what: Comment cho thấy thông điệp còn thiếu (ví dụ người ta kể cảm giác qua hai ngày đầu khi cai rồi
    lại bắt đầu lại); từ đó hình dung được một video thật.
  tactic: s4-tiktok-comment-mining
- stage: validate
  ts: 00:02:16
  what: 'Trước khi build: lưu khoảng 20 video người ta đang xem quanh vấn đề, thử vài cách nói; không
    nghĩ ra video nào làm app hấp dẫn đúng người thì bỏ ý tưởng.'
  tactic: s4-tiktok-comment-mining
  tactic_note: Xem khoảng 20 video đang được xem quanh vấn đề trước khi build; không tìm được video làm
    app hấp dẫn đúng người thì bỏ ý tưởng
  threshold: ~20 video
- stage: launch
  ts: 00:03:41
  what: Đăng nội dung trong lúc build, trước khi app ra, để biết người ta quan tâm phần nào của app.
  tactic: g3-organic-content-formats
  tactic_note: Đăng nội dung trước khi app ra mắt để thử khán giả; dùng comment để chọn tính năng và thông
    điệp
- stage: launch
  ts: 00:04:09
  what: 'Khi có vài người dùng đầu tiên, ngồi xem họ mở app: họ có tới được phần video đã hứa không, có
    hiểu việc phải làm không.'
  tactic: other
  tactic_note: Quan sát vài người dùng đầu tiên mở app, xem họ có tới được phần video đã hứa và hiểu việc
    phải làm không
- stage: grow
  ts: 00:05:08
  what: Bắt đầu với 3–5 ý tưởng nội dung khác nhau (ví dụ một người kể chuyện, một cái cho thấy vấn đề),
    không đăng một kiểu mỗi ngày cả tháng.
  tactic: g3-organic-content-formats
  threshold: 3–5 ý tưởng nội dung
- stage: grow
  ts: 00:05:30
  what: 'Đừng ám ảnh view: một founder (kể lại) trả khoảng $8 cho mỗi download mà khoảng 70% người đó
    bỏ ngay.'
  tactic: g8-funnel-measurement
  tactic_note: Đo theo download và người ở lại, không đo theo view
  cost: khoảng $8/download; khoảng 70% bỏ ngay
- stage: grow
  ts: 00:06:08
  what: 'Câu người xem phản hồi đúng (ví dụ ''app này là gì?'', ''tôi cũng đang gặp chuyện này'') đưa
    vào cả phễu: ảnh App Store đầu tiên và onboarding.'
  tactic: g11-positioning-messaging
  tactic_note: 'Lấy câu người xem phản hồi đúng làm thông điệp xuyên suốt: video, ảnh App Store, onboarding'
- stage: grow
  ts: 00:06:40
  what: Khi có format thắng, test từng biến (hook, giọng, lúc xuất hiện app) bằng vài bản khác nhau trước
    khi scale sản xuất.
  tactic: g3-organic-content-formats
- stage: grow
  ts: 00:07:03
  what: Trước khi thêm creator, đưa cho họ đối tượng, vấn đề và kiểu nội dung; creator vẫn có tự do kể
    bằng giọng của họ.
  tactic: g3-organic-content-formats
- stage: grow
  ts: 00:07:41
  what: Chỉ tăng đầu tư cho creator khi video của họ kéo được người trả tiền; nhiều view mà không có người
    trả tiền thì không đáng chi tiền.
  tactic: g7-creator-ops
  tactic_note: Trả thêm cho creator theo hợp đồng chỉ khi video kéo được người trả tiền, không theo view
- stage: grow
  ts: 00:07:41
  what: Tiền đầu tiên tái đầu tư vào format đang thắng (thêm creator, cùng góc), không nhảy sang kênh
    hay phong cách video mới.
  tactic: g7-creator-ops
- stage: grow
  ts: 00:08:07
  what: Khi một góc chạy được qua nhiều video, test bản mạnh nhất bằng paid với ngân sách nhỏ; organic
    vẫn tiếp tục thử creator và góc khác.
  tactic: g6-paid-ads
quotes: []
rules:
- ts: 00:02:16
  who: Joseph Choi
  stage: validate
  theme:
  - sell-before-build
  text: If I can't come up with any video that makes the app interesting to the right people, I would
    just scrap the entire idea and keep working on the idea itself.
  vi: Nếu không nghĩ ra được video nào làm app hấp dẫn với đúng người, tôi bỏ luôn ý tưởng và tiếp tục
    làm việc trên chính ý tưởng đó.
  evidence: opinion
- ts: 00:02:42
  who: Joseph Choi
  stage: validate
  theme:
  - builder-trap
  text: Because once I've built the app, the problem of trying to find a market for it doesn't just magically
    go away.
  vi: Build xong rồi thì việc tìm thị trường cũng không tự biến mất.
  evidence: opinion
- ts: 00:03:19
  who: Joseph Choi
  stage: build
  theme:
  - focus-one-thing
  text: When you're starting a brand new consumer app, you haven't earned that right yet.
  vi: App mới tinh chưa có quyền làm nhiều tính năng như app lớn.
  evidence: opinion
- ts: 00:03:41
  who: Joseph Choi
  stage: validate
  theme:
  - sell-before-build
  text: A lot of founders wait until launch to find out which part of their app people actually care about.
  vi: Nhiều founder đợi đến lúc ra mắt mới biết người ta quan tâm phần nào của app.
  evidence: opinion
- ts: 00:04:34
  who: Joseph Choi
  stage: validate
  theme:
  - right-audience
  text: Can I get the right person interested in this result? And can the app actually deliver it?
  vi: 'Bản đầu chỉ cần trả lời: có kéo được đúng người quan tâm tới kết quả này không, và app có giao
    được kết quả đó không?'
  evidence: opinion
- ts: 00:05:08
  who: Joseph Choi
  stage: grow
  theme: []
  text: Now, one of the easiest mistakes to get pulled into now is getting obsessed with views.
  vi: Một trong những lỗi dễ mắc nhất là ám ảnh với view.
  evidence: opinion
- ts: 00:05:30
  who: Joseph Choi
  stage: grow
  theme:
  - revenue-first
  text: There's no point in having a video with 10 million views if it's not reaching the right audience,
    increasing downloads, and bringing in more revenue.
  vi: Video 10 triệu view mà không tới đúng người, không tăng download và doanh thu thì vô nghĩa.
  evidence: opinion
- ts: 00:07:03
  who: Joseph Choi
  stage: grow
  theme: []
  text: The important thing is to have a winning format before you bring on more creators because that
    way you've got all the tested information at hand.
  vi: Điều quan trọng là có format thắng trước khi thêm creator, để có đủ thông tin đã kiểm tra.
  evidence: opinion
- ts: 00:07:41
  who: Joseph Choi
  stage: grow
  theme:
  - revenue-first
  text: However, if one creator is getting a lot of views, but I'm not getting any paying users, there's
    no point in spending money there.
  vi: Creator nhiều view mà không có người trả tiền thì không đáng chi tiền ở đó.
  evidence: opinion
- ts: 00:08:36
  who: Joseph Choi
  stage: grow
  theme:
  - many-bets
  text: The advantage here is that I'm no longer waiting for one video to go viral.
  vi: Lợi thế là không còn phải chờ một video nổ tung; có hệ thống hiểu vì sao video thắng.
  evidence: opinion
numbers:
- ts: 00:00:00
  metric: doanh thu các app mà host nói đã xây hệ thống organic growth cho (host tự nói, không kiểm)
  value: 6000000
  unit: usd
  evidence: claimed
- ts: 00:05:30
  metric: giá mỗi download của một founder (kể lại, không nêu tên)
  value: 8
  unit: usd_per_download
  evidence: claimed
- ts: 00:05:30
  metric: tỉ lệ người vừa tải bỏ ngay (cùng ví dụ)
  value: 70
  unit: percent
  evidence: claimed
frameworks:
- content-before-product
- one-feature-per-app
- organic-find-format-then-paid-scale
- funnel-message-consistency
idea_patterns: []
---

## Một câu

Kịch bản giả định của host: top charts → Sensor Tower → đọc review → đọc comment TikTok/Instagram → lưu khoảng 20 video trước khi build → đăng nội dung trong lúc build → nhân format thắng bằng creator, rồi mới chạy paid với ngân sách nhỏ.

## Bài học cho tôi

- Điều kiện dừng trước khi build: lưu khoảng 20 video người ta đang xem quanh vấn đề; không nghĩ ra video nào làm app hấp dẫn đúng người thì bỏ ý tưởng, chưa viết code. [00:02:16]
- Đo bằng người tới rồi trả tiền, không đo view: một founder (kể lại) trả khoảng $8 mỗi download và khoảng 70% bỏ ngay. [00:05:30]

## Đừng tin vội

- Đây là kịch bản giả định ("If I had to..."), chưa có số nào từ một app thật đi theo đúng quy trình này.
- Ví dụ $8/download và 70% bỏ ngay là kể lại từ một founder không nêu tên; không kiểm được.
- Sensor Tower chỉ là ước lượng; video không nói độ chính xác của nó. Chỉ dùng để so thứ tự lớn nhỏ giữa các ngách.
- Video chỉ nói về TikTok và Instagram; không có ví dụ web/SaaS hay kênh nào khác. Áp vào sản phẩm của mình (Reddit, tìm kiếm, YouTube...) là suy luận của tôi, chưa có trong video.
- Video kết bằng lời mời buổi live miễn phí 12/10 (không ghi lại), nên các số về doanh thu và số founder host đã làm việc cùng là lời tự nói.
