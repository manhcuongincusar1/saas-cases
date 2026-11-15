---
schema: 2
video_id: Y6RstwPUWdU
channel: superwall
title: Beginners Guide to Buying & Selling Apps 2026
date: 2026-07-19
url: https://www.youtube.com/watch?v=Y6RstwPUWdU
transcript: superwall/youtube-transcript/superwall/beginners-guide-to-buying-selling-apps-2026/transcript.md
kind: expert_talk
speakers:
- name: Steve Young
  role: expert
- name: Joseph Choi
  role: host
bias: Steve làm consulting/agency (AppMasters) và mua app để lãi; host Joseph Choy là founder Superwall/Consumer
  Club; video có nhiều sponsor (ASO Mobile, ROR, Superwall, Consumer Club). Ai được lợi nếu tin 'mua app
  bằng vay' hoặc dùng công cụ được quảng bá.
analyzed: 2026-11-15
cases:
- id: indie-app-santa
  depth: mention
  product: App Steve mua tháng 3/2024 (transcript ghi 'Indie App Santa')
  what: Mua app đã có ASO và lượt tải organic; đổi tiêu đề/subtitle, thêm các keyword biến thể; giảm Apple
    Ads từ khoảng 10.000 xuống khoảng 5.000
  type:
  - ios-app
  customer: Người dùng iOS tìm app qua App Store (organic chiếm phần lớn)
  revenue:
    amount: 500000
    unit: usd
    basis: annual
    note: Câu này không có ký hiệu tiền; ngữ cảnh cùng đoạn dùng $
    q: Last year alone, it did about 500,000
    ts: 00:00:00
    evidence: claimed
  scale_channels:
  - app_store_search
  - paid_apple_search
- id: purchased-2022-app
  depth: mention
  product: 'App Steve mua năm 2022 (tên không nêu), từng có hai keyword ~30 lượt tìm và #1 trên App Store'
  what: Mua app có 100–150 lượt tải/ngày, đổi sang hard paywall và tăng giá lên $60/năm; doanh thu tăng
    từ khoảng $1–2k lên khoảng $8–10k/tháng theo lời Steve
  type:
  - ios-app
  scale_channels:
  - app_store_search
- id: client-keyword-named-app
  depth: mention
  product: App của một client, đặt tên theo keyword ít cạnh tranh (ví dụ 'Super Wall' hai từ, lượt tìm
    ~30)
  what: 'Đặt tên app theo keyword; đạt #1 trong tuần đầu, khoảng 100 lượt tải/ngày, khoảng $1.600 trong
    tháng đầu, không có free trial'
  type:
  - ios-app
  revenue:
    amount: 20000
    unit: usd
    basis: mrr
    note: 'Lời Steve: gần 20K MRR sau vài năm (không phải thời điểm launch); cùng đoạn có $1,600'
    q: It's now close to 20K MRR a few years later
    ts: 00:15:56
    evidence: claimed
  scale_channels:
  - app_store_search
steps:
- stage: find-idea
  ts: 00:11:06
  what: Thu hẹp ngách từ danh mục rộng (meditation) sang ngách con (green noise, binaural beats), rồi
    tìm 'painkiller keyword' (ví dụ migraine tracker) mà người ta dễ trả tiền.
  tactic: s9-niche-narrowing
- stage: find-idea
  ts: 00:12:31
  what: 'Xem top 3 kết quả tìm kiếm của keyword: số review, có keyword trong title không; nếu top 2–3
    chỉ có khoảng 100+ review và ít người nhắm keyword thì coi là có thể vượt.'
  tactic: s2-aso-keyword-gap
  threshold: top 2–3 chỉ ~100+ review
- stage: find-idea
  ts: 00:13:08
  what: 'Dùng Sensor Tower xem app migraine: có app ~5k lượt tải/10k doanh thu tháng; Migraine Buddy ~70k/tháng
    từ ~30k lượt tải iOS, onboarding và paywall kém → ngách có tiền nhưng chưa tối ưu.'
  tactic: s1-revenue-spy
  tool: Sensor Tower
- stage: find-idea
  ts: 00:14:45
  what: Đưa app đối thủ vào ASO Mobile (hoặc App Follow) xem app đang index keyword nào và lượt tìm; lọc
    keyword có lượt tìm khoảng 30 trở lên mà đối thủ yếu.
  tactic: s2-aso-keyword-gap
  tool: ASO Mobile / App Follow
  threshold: lượt tìm ~30 trở lên
- stage: validate
  ts: 00:31:54
  what: 'Đang làm với một client: build test flight chỉ có tính năng viral, đưa cho creator quay video;
    nếu video có nhiều view thì có tín hiệu nhu cầu trước khi app hoàn thiện.'
  tactic: s8-content-demand-test
  tactic_note: Test flight chỉ có tính năng viral, creator quay video trước khi app xong (không phải đăng
    nội dung của sản phẩm đã xong)
- stage: launch
  ts: 00:21:11
  what: 'Lúc ra app ''green noise'', đặt subtitle theo gợi ý autofill (green noise for better sleep) và
    gom các từ khoá autofill vào title/subtitle vì team chờ; app có lúc đạt #1.'
  tactic: g2-aso-seo-organic
- stage: launch
  ts: 00:24:01
  case: client-keyword-named-app
  what: 'Với client: tìm keyword ~57.700 lượt tìm mà ít người đặt làm tên app, đặt làm tên app; đạt #1,
    khoảng 100 lượt tải/ngày, khoảng $1.600 trong 21 ngày đầu.'
  tactic: g2-aso-seo-organic
  threshold: ~57.700 lượt tìm
- stage: monetize
  ts: 00:20:02
  case: purchased-2022-app
  what: 'Sau khi mua: tháng 5 bật paywall mới, tháng 6 chuyển sang hard paywall (bỏ nút X) và tăng giá
    $60/năm, không thêm download hay tính năng; start-trial từ 6% lên 13%, trial→trả tiền giữ nguyên.'
  tactic: g4-pricing-paywall
  threshold: start-trial 6% → 13%
- stage: grow
  ts: 00:09:23
  case: indie-app-santa
  what: 'App vừa mua: giảm Apple Ads từ khoảng 10.000 tháng trước xuống khoảng 5.000, chuyển ngân sách
    sang tối ưu ASO vì còn nhiều keyword chưa khai thác.'
  tactic: g6-paid-ads
  tool: Apple Ads
  cost: ~5.000/tháng (tháng trước ~10.000)
- stage: grow
  ts: 00:34:25
  what: 'Thử Meta cho một app ~3k/tháng (trước đó toàn organic): RPI khoảng $1 nên không đủ kinh tế; thử
    hard paywall nhưng kém hơn.'
  tactic: g6-paid-ads
  tool: Meta
  threshold: RPI ~$3 (hoặc 10–15 cost/trial)
- stage: grow
  ts: 00:32:26
  what: 'Video TikTok/Reels organic để kéo tải: quay bằng hai máy (một quay, một demo app), có hook chữ
    hoặc phản ứng UGC, rồi cho thấy tính năng ''wow'' (thường có AI) trên màn hình app.'
  tactic: g3-organic-content-formats
- stage: scale
  ts: 00:43:03
  case: indie-app-santa
  what: Mua app đã có doanh thu và lượt tải organic bằng khoản vay (vay 10 năm, trả khoảng 5k/tháng);
    trả nợ bằng lợi nhuận. Đây là phép tính giả định của Steve.
quotes: []
rules:
- ts: 00:04:39
  who: Steve Young
  stage: mindset
  theme: []
  text: Don't just copy what you're seeing other people do because they already have an advantage over
    you.
  vi: Đừng chỉ chép thứ người khác đang làm, vì họ đã có lợi thế sẵn.
  evidence: opinion
- ts: 00:07:34
  who: Steve Young
  stage: find-idea
  theme: []
  text: It's like my ASO strategy is to focus on keywords that nobody is going after not that ones that
    are everybody is going after.
  vi: Chiến lược ASO của tôi là nhắm từ khoá mà không ai nhắm, không phải những từ mọi người đang nhắm.
  evidence: opinion
- ts: 00:07:56
  who: Steve Young
  stage: find-idea
  theme: []
  text: It's just the ones that were like we find the keyword first, Joseph, and then build the app.
  vi: Những app làm ra tiền nhanh là app mà chúng tôi tìm keyword trước rồi mới build.
  evidence: opinion
- ts: 00:11:53
  who: Steve Young
  stage: find-idea
  theme: []
  text: So you try to find these painkiller keywords that people are more likely to pay.
  vi: Hãy tìm những keyword 'giảm đau' mà người ta dễ trả tiền hơn.
  evidence: opinion
- ts: 00:25:50
  who: Steve Young
  stage: grow
  theme: []
  text: For me, I think it's partly about optimization, title and subtitle first and foremost.
  vi: Với tôi, phần lớn là tối ưu hoá title và subtitle trước hết.
  evidence: opinion
- ts: 00:29:15
  who: Steve Young
  stage: monetize
  theme: []
  text: And there's no better way to force a product market fit test than doing a hard pay wall. That
    means no X.
  vi: Không có cách nào kiểm tra product-market fit tốt hơn hard paywall. Nghĩa là không có nút X.
  evidence: opinion
- ts: 00:29:55
  who: Steve Young
  stage: monetize
  theme: []
  text: Now, if I'm not hitting my 30 to 40, which is industry average for trial to paid, then I know
    I have a product problem.
  vi: Nếu không đạt tỉ lệ trial→trả tiền 30–40% (mức trung bình ngành) thì tôi biết sản phẩm có vấn đề.
  evidence: opinion
- ts: 00:30:14
  who: Steve Young
  stage: monetize
  theme: []
  text: I feel like monetization should be close behind distribution but should still be secondary to
    distribution.
  vi: Tôi nghĩ monetization nên theo sát distribution nhưng vẫn đứng sau distribution.
  evidence: opinion
- ts: 00:33:57
  who: Steve Young
  stage: grow
  theme: []
  text: I think you got to be somewhere around at least a 10 to 15 cost per trial or a $3 revenue per
    install to even consider it.
  vi: Theo ông, cần ít nhất khoảng 10–15 chi phí/trial hoặc RPI $3 mới nên cân nhắc Meta.
  evidence: opinion
numbers:
- ts: 00:20:02
  metric: start-trial rate sau khi chuyển hard paywall (trước là 6%)
  value: 13
  unit: '%'
  evidence: claimed
- ts: 00:33:57
  metric: RPI tối thiểu để cân nhắc Meta (theo Steve)
  value: 3
  unit: usd
  evidence: opinion
- ts: 00:34:25
  metric: RPI của app đã thử chạy Meta
  value: 1
  unit: usd
  evidence: claimed
- ts: 00:15:56
  metric: doanh thu tháng đầu của app client đặt tên theo keyword
  value: 1600
  unit: usd
  evidence: claimed
frameworks:
- niche-down-proven-category
idea_patterns:
- niche-inside-hot-category
---
## Một câu
Steve Young, người mua và vận hành app, cho rằng phân phối (ASO và Apple Ads) là lợi thế chính: tìm keyword ít người nhắm, mua app đã có lượt tải organic bằng khoản vay, rồi đổi sang hard paywall và tăng giá để nhân đôi doanh thu mà không thêm tính năng.

## Bài học cho tôi
- Chọn ngách bằng keyword: lượt tìm khoảng 30 trở lên, và nếu top 2–3 kết quả ít review, keyword không có trong title thì có thể vượt (`00:12:31`).
- Đổi paywall cho app có sẵn lượt tải: start-trial 6% → 13% với trial→trả tiền giữ nguyên thì doanh thu gấp đôi trên cùng lượt tải (`00:20:02`).

## Đừng tin vội
- Người nói bán consulting/agency và là người mua app; video có nhiều sponsor. Các ví dụ là app mua có sẵn lượt tải, không phải app tự build từ đầu.
- Survivor bias: các ví dụ là app thành công. Steve chỉ nhắc qua một lần mua app $18.000 "flopped" (`00:42:06`).
- Con số doanh thu (500k/năm, gần 20k MRR, $1.600) là lời kể, không có dashboard được mở theo yêu cầu host nên ghi `claimed`; câu 500k không có ký hiệu tiền.
- Mô hình mua app bằng vay (giá $350k, lãi khoảng $5k/tháng, trả 10 năm) là phép tính Steve tự nói "take this with a grain of salt" (`00:42:29`); không có chi phí lãi, thuế, vận hành hay rủi ro giảm doanh thu.
- Điều kiện tài chính riêng: ông nói vay mua app ở Mỹ là lợi thế ("this is the beauty of the US"); khó sao chép nếu không có nguồn vốn/vay tương tự.
- Video không nói: giá mua thực tế các app ví dụ (chỉ dùng số 350 "to keep the math easy"), thời gian app mua hoàn vốn thực tế, và chi phí cụ thể của Meta.
