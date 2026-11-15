---
schema: 2
video_id: lkwX_kc0NS8
channel: superwall
title: I made 4,000 app paywalls and learned this
date: 2026-02-08
url: https://www.youtube.com/watch?v=lkwX_kc0NS8
transcript: superwall/youtube-transcript/superwall/i-made-4000-app-paywalls-and-learned-this/transcript.md
kind: expert_talk
speakers:
- name: Jonathan Parra
  role: expert
- name: Joseph Choi
  role: host
bias: Superwall (công ty bán công cụ paywall) tài trợ kênh và Jonathan từng làm designer cho Superwall;
  host quảng bá Consumer Club và bữa tối cho founder $100k/tháng. Số liệu app khác là kể lại, chưa kiểm.
analyzed: 2026-11-15
cases:
- id: clear-30
  depth: mention
  product: Clear 30 (app bỏ nghiện có hành trình nhiều ngày/tuần)
  what: Paywall kiểu Clear 30 có hành trình nhiều ngày; Jonathan nói chạy tốt ở nhiều ngách có hành trình
    rõ
- id: pyometer-plus
  depth: mention
  product: Pyometer Plus+
  what: App giữ giao diện kiểu Swift UI của Apple; paywall theo phong cách native thắng các bản thiết
    kế custom
- id: mojo
  depth: mention
  product: Mojo
  what: Dùng nhiều kiểu paywall có bố cục phong cách Swift UI; video paywall của Jonathan lấy cảm hứng
    từ Mojo
- id: blinkist
  depth: mention
  product: Blinkist
  what: Paywall free trial có timeline (ngày 5 thông báo, ngày 7 bắt đầu tính tiền), vẫn hiệu quả nhiều
    năm
steps:
- stage: monetize
  ts: 00:05:47
  case: null
  what: 'Thử bản gọn: đổi tên gói ngắn gọn, bỏ dòng ''limited time'', thêm ''No commitment, cancel anytime'',
    nút ''Continue'' thay vì mô tả; bản gọn thắng.'
  tactic: g4-pricing-paywall
  tactic_note: AB test thiết kế và cách trình bày gói trên paywall
- stage: monetize
  ts: 00:10:18
  what: Bỏ gói tháng, đặt gói tuần kèm nút 'Start my 3-day trial' làm lựa chọn chính; bản có trial thắng
    rõ rệt.
  tactic: g4-pricing-paywall
- stage: monetize
  ts: 00:10:40
  what: Ẩn nhóm gói phụ sau nút 'view all plans'; highlight gói năm; sắp gói theo độ dài (dài tới ngắn
    hoặc ngược lại), không xen kẽ.
  tactic: g4-pricing-paywall
- stage: monetize
  ts: 00:16:20
  what: Gói năm được chọn sẵn; khi người dùng đóng paywall, hiện drawer gợi ý gói tháng và so sánh giá
    theo tuần với gói năm.
  tactic: g4-pricing-paywall
  tactic_note: Exit drawer sau khi đóng paywall gói năm
- stage: monetize
  ts: 00:17:34
  what: Khi người dùng vẫn bấm 'not now', hiện offer một lần giảm giá gói năm (ví dụ từ 40 xuống 30 USD/năm);
    thường giảm 25–33% tuỳ app.
  tactic: g4-pricing-paywall
  tactic_note: One-time offer giảm giá gói năm sau khi đóng paywall
- stage: monetize
  ts: 00:18:09
  what: Thêm một màn trung gian đổi cách hiển thị cùng mức giá (39 USD/năm thành 76 cent/tuần) trước khi
    đưa ưu đãi giảm giá.
  tactic: g4-pricing-paywall
- stage: monetize
  ts: 00:43:55
  what: Paywall dùng video app (làm bằng Rotato từ quay màn hình điện thoại) + social proof + vài bullet;
    bản này thắng test.
  tactic: g4-pricing-paywall
  tool: Rotato
- stage: monetize
  ts: 00:46:40
  case: pyometer-plus
  what: 'Làm paywall theo template SwiftUI (gần với giao diện gốc iOS), thử so với bản custom: bản SwiftUI
    thắng rõ.'
  tactic: g4-pricing-paywall
  tactic_note: Paywall giống giao diện native iOS thay vì thiết kế custom
- stage: monetize
  ts: 00:51:27
  what: Khi chuyển sang gói Pro cao hơn, đổi nền paywall sang tương phản (đen) để gói cao cấp trông premium;
    theo lời Jonathan, nhiều người chọn Pro hơn.
  tactic: g4-pricing-paywall
  tactic_note: Đổi nền paywall theo tầng gói để gói cao cấp trông premium
quotes: []
rules:
- ts: 00:00:16
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: I think the most surprising one across the board for everyone was that there is no perfect payw
    wall.
  vi: Điều bất ngờ nhất với mọi người là không có paywall hoàn hảo dùng cho mọi app.
  evidence: opinion
- ts: 00:00:57
  who: Joseph Choi
  stage: monetize
  theme: []
  text: What he also figured out was that most founders are testing the wrong things. They obsess over
    pricing when the biggest lever is actually the design and packaging.
  vi: 'Điều ông ấy rút ra: đa số founder test sai thứ. Họ ám ảnh về giá, trong khi đòn bẩy lớn nhất là
    thiết kế và cách đóng gói.'
  evidence: opinion
- ts: 00:01:05
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: Price and packaging design is one of the biggest levers that you can pull for payw wall experimentation.
  vi: Thiết kế giá và cách đóng gói là một trong những đòn bẩy lớn nhất khi thử nghiệm paywall.
  evidence: opinion
- ts: 00:12:57
  who: Jonathan Parra
  stage: monetize
  theme:
  - revenue-first
  text: a lot of the time weekly, you know, our users will pay more in the weekly plan than if they would
    have just paid for the annual plan.
  vi: Nhiều khi, người dùng trả cho gói tuần còn nhiều hơn là họ trả gói năm.
  evidence: opinion
- ts: 00:31:41
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: the best thing that we ended up doing was just creating a component system uh that you you have
    things that work across all payw walls
  vi: 'Việc tốt nhất họ làm là xây hệ thống component: có những phần chạy được trên mọi paywall và thả
    vào từng paywall.'
  evidence: opinion
- ts: 00:32:47
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: Bullet list payw walls just uh actually are one of the few payw walls that perform well across
    the board.
  vi: Paywall dạng bullet list là một trong số ít loại chạy tốt ở hầu hết các ngách.
  evidence: opinion
- ts: 00:36:37
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: So design tests really are the bread and butter of any one that wants to improve their KPIs with
    AB testing for uh payw walls.
  vi: Test thiết kế là nền tảng của bất kỳ ai muốn cải thiện KPI bằng AB test paywall.
  evidence: opinion
- ts: 00:37:27
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: So it's not something that I like to do immediately.
  vi: Test giá không phải việc ông ấy làm ngay; để sau khi đã chạy nhiều test thiết kế.
  evidence: opinion
- ts: 00:54:23
  who: Jonathan Parra
  stage: monetize
  theme: []
  text: So apps that are making I would say 100,000 a month and they haven't done a ton of payw wall experimentation
    because they've been working so much on products, those are I see the best gains for those kinds of
    apps.
  vi: Các app đạt khoảng 100k/tháng mà chưa test paywall nhiều (vì bận làm sản phẩm) là nhóm được lợi
    nhiều nhất từ AB test.
  evidence: opinion
numbers:
- ts: 00:00:00
  metric: số paywall Jonathan đã thiết kế (ước tính, 'closer to 4,500')
  value: 4500
  unit: count
  evidence: claimed
- ts: 00:00:34
  metric: tăng chuyển đổi khi paywall đơn giản với nút 'continue' so với bản mô tả chi tiết
  value: 111
  unit: percent
  evidence: claimed
- ts: 00:54:23
  metric: tỉ lệ chuyển đổi paywall trung bình trước khi test (theo Jonathan)
  value: 8
  unit: percent
  evidence: claimed
- ts: 00:54:23
  metric: tỉ lệ chuyển đổi sau vài vòng test (app 10–50k/tháng)
  value: 15–20
  unit: percent
  evidence: claimed
- ts: 00:21:15
  metric: giá tháng của app chat AI có prompt riêng (ước lượng)
  value: 20–22
  unit: usd_per_month
  evidence: claimed
frameworks:
- annual-plan-push
idea_patterns: []
---

## Một câu

Jonathan Parra (thiết kế hơn 4.000 paywall cho Superwall) kể: không có paywall hoàn hảo cho mọi app; thiết kế và cách đóng gói gói giá thường là đòn bẩy lớn hơn việc đổi giá; bản đơn giản với nút "Continue" hay thắng; nên test thiết kế trước, test giá sau.

## Bài học cho tôi

- Test thiết kế paywall (bố cục, nút, số trang) trước khi test giá; test giá để sau khi đã có nhiều vòng test thiết kế (`00:36:37`).
- Với paywall có gói năm: chọn sẵn gói năm, khi đóng thì drawer gợi ý gói tháng, rồi offer giảm giá một lần (`00:16:20`).

## Đừng tin vội

- Bias: Superwall tài trợ kênh và Jonathan từng làm designer cho Superwall; host quảng bá Consumer Club và bữa tối cho founder $100k/tháng. Các ví dụ app khác (Clear 30, Pyometer, Mojo, Blinkist, app chat AI 20–22 USD/tháng) là kể lại, không kiểm được từ video.
- Điều kiện riêng: mỗi test phụ thuộc lưu lượng và ngách của từng app. "Không có paywall hoàn hảo" nghĩa là kết quả không sao chép y nguyên được; con số 111% là một test cụ thể, không phải kỳ vọng chung.
- Video không nói: chi phí và thời gian chạy test, số mẫu mỗi nhánh, ý nghĩa thống kê của các kết quả "thắng", và app nào của Jonathan có doanh thu bao nhiêu.
