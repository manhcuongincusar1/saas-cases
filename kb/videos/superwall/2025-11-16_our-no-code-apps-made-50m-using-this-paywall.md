---
schema: 2
video_id: 24QMRDXck70
channel: superwall
title: "Our No-Code Apps Made $50M Using THIS Paywall"
date: 2025-11-16
url: https://www.youtube.com/watch?v=24QMRDXck70
transcript: superwall/youtube-transcript/superwall/our-no-code-apps-made-50m-using-this-paywall/transcript.md
kind: expert_talk
speakers:
- {name: Joseph Choi, role: host}
- {name: Vahe Baghdasaryan, role: expert}
bias: "Video quảng bá Superwall (công cụ A/B test paywall, được nhắc kèm link) và Consumer Club (host mời tham gia Discord). Vahe làm dịch vụ tối ưu paywall (link ở mô tả). Số liệu app khác là nghe kể, không có chứng từ."
analyzed: 2026-11-15
cases:
- id: entertainment-app-unnamed
  depth: mention
  product: "App giải trí (không nêu tên)"
  what: "Khách có ~40–50k lượt cài/tháng, không chạy ads; Vahe tối ưu paywall để install-to-paid tăng từ 1.1% lên gần 4%"
- id: claim
  depth: mention
  product: "Claim (app đòi bồi thường settlement)"
  what: "Paywall nhiều bước khi còn free trial; sau đó bỏ trial và chuyển sang trả ngay"
- id: cal-ai
  depth: mention
  product: "Cal AI (app sức khoẻ, giảm cân)"
  what: "Ví dụ vòng quay giảm giá khi mở app và toggle trial ở paywall huỷ giao dịch"
- id: quitter
  depth: mention
  product: "Quitter (app bỏ thói quen)"
  what: "Paywall 3 bước không có trial, không hiện giá cho tới khi người dùng bấm nút"
- id: riz
  depth: mention
  product: "Riz (app gợi ý câu trả lời hẹn hò bằng AI)"
  what: "Toggle bỏ free trial, đổi sang giá thấp hơn khi mua thẳng"
steps:
- stage: monetize
  ts: "00:06:56"
  case: entertainment-app-unnamed
  what: "Tối ưu paywall (onboarding và các placement) cho app đang có lượt cài đều, không thêm người dùng: install-to-paid từ 1.1% (tháng 4) lên gần 4% (tháng 9)."
  tactic: g4-pricing-paywall
  tactic_note: "Tối ưu paywall trên app đã có người dùng, không tăng người dùng mới"
- stage: monetize
  ts: "00:09:50"
  case: claim
  what: "Paywall nhiều bước khi app còn free trial: màn 1 'try for free', màn 2 báo nhắc trước khi trial kết thúc, màn 3 hiện timeline và nút 'Try for $0'; gói năm ghi là 'try it free', không ghi 'annual plan'."
  tactic: g4-pricing-paywall
  tactic_note: "Nhắc chữ 'free' nhiều lần (khoảng 5–7 lần); bỏ thời hạn trial khỏi chữ chính"
- stage: monetize
  ts: "00:16:07"
  case: claim
  what: "Bỏ free trial sau khi đã đạt trial start 34%, chuyển sang app trả ngay; trial-to-paid sau đó được nêu 50–55%."
  tactic: g4-pricing-paywall
  threshold: "trial start 34%"
- stage: monetize
  ts: "00:18:55"
  case: cal-ai
  what: "Hiện vòng quay giảm giá khi mở app: người dùng quay ra một % rồi bấm nhận; A/B test cho tăng conversion 'double digit' so với đưa giảm giá thẳng."
  tactic: g4-pricing-paywall
  tactic_note: "Vòng quay giảm giá, mượn logic e-commerce"
- stage: monetize
  ts: "00:23:03"
  case: riz
  what: "Free trial bật mặc định (7 ngày rồi $9.99/tuần); công tắc 'skip free trial' đổi sang $6.99/tuần để mua thẳng."
  tactic: g4-pricing-paywall
  tactic_note: "Toggle trial: bỏ trial thì giá thấp hơn; Vahe nói hợp app có ý định mua thấp (không phải app sức khoẻ)"
- stage: monetize
  ts: "00:27:14"
  case: quitter
  what: "Paywall 3 bước không trial: màn 1–2 visual và review, màn 3 không hiện giá; giá gói năm/tháng chỉ hiện sau nút 'Start my journey today', kèm nhãn 'giảm 60%' và 'limited spots'."
  tactic: g4-pricing-paywall
  tactic_note: "Ẩn giá tới khi bấm nút; nhãn khuyến mãi mượn từ e-commerce"
- stage: monetize
  ts: "00:33:55"
  what: "Paywall huỷ giao dịch (transaction abandonment): chỉ giảm gói năm; có trial giảm ví dụ 80%, không trial giảm 90%; gói tháng/tuần giữ nguyên giá."
  tactic: g4-pricing-paywall
  tactic_note: "Chỉ giảm gói năm; gói tháng/tuần không giảm để làm mốc so sánh"
- stage: monetize
  ts: "00:37:32"
  what: "Định giá theo ROAS (khi đã có dữ liệu chi quảng cáo): chọn giá sao cho ROAS dương hoặc hoàn vốn trong khoảng một tháng, giữ tỉ lệ chuyển đổi ổn định."
  tactic: g4-pricing-paywall
  tactic_note: "Cách khác: lấy giá đối thủ, hoặc cộng biên lợi nhuận lên chi phí AI/vận hành mỗi người dùng"
- stage: monetize
  ts: "00:41:09"
  what: "Thêm các placement cơ bản: paywall huỷ giao dịch, paywall khi mở app (ít nhất mỗi ngày một lần), và paywall sau một số hành động miễn phí (ví dụ 5 lượt quét)."
  tactic: g4-pricing-paywall
  tactic_note: "Placement trong app là nơi thêm doanh thu mà không cần người dùng mới"
quotes: []
rules:
- ts: "00:17:32"
  who: Vahe Baghdasaryan
  stage: monetize
  theme:
  - revenue-first
  text: "This is like a prerequisite like if you don't have a high volume coming in, you will not be able to make a lot of money if you remove your free trial."
  vi: "Bỏ free trial chỉ kiếm được nhiều tiền khi lượng người vào đã lớn; đó là điều kiện tiên quyết."
  evidence: opinion
- ts: "00:34:17"
  who: Vahe Baghdasaryan
  stage: monetize
  theme:
  - revenue-first
  text: "You should discount only an annual product. Don't discount weekly. Don't discount monthly. It doesn't work."
  vi: "Chỉ giảm giá gói năm. Không giảm gói tuần, không giảm gói tháng; đã test hàng chục lần và không hiệu quả."
  evidence: opinion
- ts: "00:26:30"
  who: Vahe Baghdasaryan
  stage: monetize
  theme:
  - many-bets
  text: "My general advice is you test both, see which one works for you the best."
  vi: "Lời khuyên chung: test cả hai cách, cách nào hợp app thì giữ."
  evidence: opinion
- ts: "00:39:04"
  who: Vahe Baghdasaryan
  stage: monetize
  theme: []
  text: "The best way is to just get some sense, right? Just see what your competitors are pricing."
  vi: "Cách đơn giản nhất là xem đối thủ đang bán giá bao nhiêu, rồi cộng với chi phí và chi phí quảng cáo."
  evidence: opinion
- ts: "00:41:09"
  who: Vahe Baghdasaryan
  stage: monetize
  theme: []
  text: "The one is on session start like showing a payable on every session start at least like once per day."
  vi: "Một placement quan trọng là paywall khi mở app, ít nhất mỗi ngày một lần."
  evidence: opinion
- ts: "00:42:10"
  who: Vahe Baghdasaryan
  stage: monetize
  theme: []
  text: "You don't need to experiment. You just need to build your foundation that you can experiment later."
  vi: "Chưa cần thử nghiệm: trước hết xây đủ nền (đủ placement), thử nghiệm để sau."
  evidence: opinion
numbers:
- ts: "00:00:00"
  metric: "doanh thu thêm cho các app khách (Vahe nói; hơn 10.000 thí nghiệm paywall)"
  value: 50000000
  unit: usd
  evidence: claimed
- ts: "00:01:14"
  metric: "install-to-paid app giải trí, tháng 4 → tháng 9 (không chạy ads)"
  value: "1.1% → ~4%"
  unit: ratio
  evidence: claimed
- ts: "00:04:51"
  metric: "trial start rate: trên 15% là tốt"
  value: "15%"
  unit: ratio
  evidence: opinion
- ts: "00:04:51"
  metric: "trial-to-paid: trên 30% là tốt"
  value: "30%"
  unit: ratio
  evidence: opinion
- ts: "00:05:37"
  metric: "install-to-paid (người dùng Mỹ): trên 10% là tốt, dưới 4% là có vấn đề"
  value: "4–10%"
  unit: ratio
  evidence: opinion
- ts: "00:14:38"
  metric: "uplift trial start khi chuyển sang paywall nhiều bước"
  value: "20–40%"
  unit: ratio
  evidence: claimed
- ts: "00:15:56"
  metric: "trial start rate app Claim (trước khi bỏ trial)"
  value: "34%"
  unit: ratio
  evidence: claimed
- ts: "00:16:39"
  metric: "trial-to-paid sau khi Claim bỏ trial"
  value: "50–55%"
  unit: ratio
  evidence: claimed
- ts: "00:34:44"
  metric: "tỉ lệ người dùng chọn mua không trial khi có paywall huỷ giao dịch"
  value: "~10%"
  unit: ratio
  evidence: claimed
frameworks: [annual-plan-push]
idea_patterns: []
---

## Một câu

Vahe (chuyên gia tối ưu paywall) kể cách kiếm thêm tiền từ app đã có bằng paywall, không cần thêm người dùng: paywall nhiều bước nhắc trial, bỏ trial khi trial start đủ cao, giảm giá chỉ gói năm, và đặt paywall ở đúng placement.

## Bài học cho tôi

- Với app đang có lượt cài đều, install-to-paid từ 1.1% lên ~4% trong vài tháng là đòn bẩy doanh thu không cần người dùng mới (`00:06:56`).
- Trước khi A/B test, đặt đủ placement cơ bản (huỷ giao dịch, mở app, sau hành động miễn phí) (`00:41:09`).

## Đừng tin vội

- Video là phễu bán: Superwall và Consumer Club được quảng bá; Vahe bán dịch vụ tối ưu paywall. Lời khuyên nghiêng về việc mua tool/dịch vụ.
- Đa số case là `mention`: không có doanh thu, chi phí, hay thời gian làm của từng app; các con số Claim, Cal AI, Quitter, Riz là nghe kể từ expert, chưa kiểm.
- Điều kiện khó chép: lượng cài 40–50k/tháng và trial start cao (Claim 34%). Vahe nói rõ phải test theo ngành và đối tượng (app sức khoẻ khác app tiện ích); không có "con số đúng" chung.
- Video không nói thời điểm các app này đạt doanh thu, nên không có tín hiệu nhu cầu trước khi build.
