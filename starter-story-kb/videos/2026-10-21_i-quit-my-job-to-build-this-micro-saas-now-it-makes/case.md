---
id: RSlhgyAXsBI
slug: liinks
product: Liinks
founder: Charlie Clark — software engineer từng làm ở Squarespace, bỏ việc hai lần (2019 và 08/2024) để làm side project của mình
tagline: Link-in-bio kiêm website builder siêu rẻ ($5/tháng) cạnh Linktree — sống nhờ Google Search Ads và giá thấp, MRR ~$31.500 sau nhiều năm
revenue_usd_month: 31500
revenue_basis: MRR theo dashboard Stripe, founder nói "about 31,500 MRR" (và "about $31,500 in monthly recurring revenue"). Tiêu đề ghi $30K, mô tả "over $30K", nên gần khớp. Là doanh thu định kỳ gộp, chưa trừ ads (~$100/ngày) và chi phí khác
model: micro-saas-subscription
category: link-in-bio / website builder
audience: B2C và prosumer — cá nhân và brand muốn kiếm tiền online, trả $5/tháng, cộng gói pro $12/tháng trở lên
started: ~cuối 2019 (làm Liinks sau khoảng một năm làm dự án trước, Visual), bản trả phí ra sau đó
time_to_first_sale: premium ~$3/tháng, đạt khoảng $100 MRR trong vài tháng sau khi mở bản trả phí
time_to_scale: ~6 năm từ lúc làm tới $31.500 MRR, đủ thay lương từ mùa hè 2024 (người viết suy ra từ mốc 2019-2020) — rất chậm so với phần lớn case khác
team_size: 1 (solo)
funding: bootstrapped
main_channel: Google Search Ads (từ khoá có ý định mua cao) — đã dựa vào kênh này khoảng 4 năm, trước đó là Instagram ads
tech_stack: [DigitalOcean, AWS, Resend, Tinybird, ClickHouse, OpenAI, Stripe, Google Ads]
key_metrics:
  mrr_usd: 31500
  price_before_usd: 4
  price_after_usd: 5
  mrr_gain_from_price_increase_usd: 5000
  pro_plan_start_usd: 12
  highest_paying_customer_usd_month: 100
  google_ads_spend_usd_per_day: 100
  coding_agent_spend_usd_month_low: 100
  coding_agent_spend_usd_month_high: 200
  first_build_weeks: 2
  initial_premium_price_usd: 3
difficulty: 3
video_url: https://www.youtube.com/watch?v=RSlhgyAXsBI
published: 2026-10-21
views: 147610
tags: [micro-saas, saas, paid-ads, solo-founder, bootstrapped, side-project, subscription, validation, clone-idea, boring-business]
---

# Liinks — "Linktree rẻ hơn" làm $31.500 MRR sau 6 năm bằng Google Ads và giá $5

> **Tóm tắt 30 giây:** Charlie Clark, kỹ sư phần mềm, bỏ việc lần đầu năm 2019 để làm Visual (marketplace print-on-demand cho nghệ sĩ) nhưng không tìm được market fit. Thấy nghệ sĩ dùng Linktree, anh tự cho mình 2 tuần để làm bản thay thế đẹp hơn, nhắn trực tiếp từng người dùng thử, ra Product Hunt rồi mở gói premium ~$3/tháng. Khi Visual và Liinks đều chưa đủ tiền và COVID tới, anh quay lại Squarespace làm toàn thời gian trong khi Liinks tiếp tục lớn. Đến mùa hè 2024 doanh thu ngang lương nên anh nghỉ hẳn (08/2024). Hiện Stripe cho thấy ~$31.500 MRR; riêng đợt tăng giá từ $4 lên $5 ở cuối tháng 6 mang thêm gần $5.000 MRR. Chiến lược định giá: neo dưới Linktree, "nhiều khách trả ít" — kèm gói pro từ $12/tháng cho domain riêng và nhiều trang, vài khách trả tới ~$100/tháng. Tăng trưởng: Instagram ads thời đầu, rồi Google Search Ads với khoảng $100/ngày là kênh chủ lực suốt ~4 năm. Đây là case chậm mà chắc: không có hack, chỉ có một sản phẩm đơn giản, kênh trả phí có ROI rõ, và nhiều năm kiên nhẫn.

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR Stripe | **~$31.500** ([03:37](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=217s)) |
| Giá cơ bản | **$5/tháng** (từ $4, tăng cuối tháng 6; ban đầu ~$3) |
| MRR tăng từ đợt đổi giá | **gần $5.000** ([03:54](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=234s)) |
| Gói pro | **từ $12/tháng** (5 trang; thêm trang trả thêm); vài khách trả "upwards of 100 a month" ([09:07](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=547s)) |
| Ad spend lớn nhất | **~$100/ngày Google Ads** ([13:12](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=792s)) |
| Chi phí coding agent | **$100-200/tháng** trong ~1 năm gần đây |
| Thời gian build bản đầu | **2 tuần** |
| Thời gian tới hiện tại | ~6 năm (gồm giai đoạn làm bán thời gian) |
| Nhân sự | 1 (solo) |
| Số khách trả phí, churn, CAC | **không nêu** |

**Tên riêng:** caption ghi "Links", tôi theo mô tả (Liinks).

**Về con số headline:**
- $31.500 MRR đọc trực tiếp từ Stripe, khớp tiêu đề "$30K" và mô tả; đây là một trong số ít case trong loạt này khá sạch về định nghĩa.
- Điểm yếu: không có số khách, churn hay CAC. Ước tính thô của người viết: nếu hầu hết khách ở $5/tháng thì cần hàng nghìn khách trả tiền (video không nêu con số), vì thế churn là biến số lớn; ad spend ~$100/ngày ≈ $3.000/tháng nếu duy trì (phép nhân của người viết) cho thấy margin có vẻ cao nhưng video không có P&L.
- MRR sau tăng giá "on an upward trend since then" — video không cho biết bao nhiêu khách rời đi sau khi giá tăng.

---

## 2. Sản phẩm giải quyết vấn đề gì

Liinks là công cụ link-in-bio ([01:39](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=99s)): gom các phần của danh tính online vào một trang mobile-first, nhưng tiến gần website builder hơn: nhiều trang, block mạnh hơn, tuỳ biến nhiều hơn. URL dạng `liinks.co/yourusername` (caption ghi `links.co`, tôi theo mô tả cho thương hiệu).

Khách hàng đa dạng nhưng "fundamentally these are all either people or brands that are trying to make money online". Onboarding thông minh: nhập Instagram để app scrape ảnh đại diện, tên, thông tin công khai rồi tự dựng banner, chọn theme ([13:32](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=812s)). Có thêm form độc lập, QR code, short link, và một mock-up builder anh làm riêng rồi gộp vào.

Điểm khác biệt: trang "đẹp hơn" so với Linktree ("the pages don't look very good") — một điểm khác biệt chủ quan, không đo được. Cạnh tranh trực tiếp với một đối thủ có hàng triệu user.

---

## 3. Ý tưởng đến từ đâu

Từ quan sát khi làm dự án khác ([05:17](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=317s)): trong lúc làm Visual (marketplace print-on-demand cho nghệ sĩ) và nói chuyện với nhiều nghệ sĩ, anh thấy họ dùng Linktree rất nhiều. Lúc đó anh đang "struggling a bit" với Visual nên quyết định "give myself 2 weeks to build a Linktree alternative".

Cú rẽ: sản phẩm phụ (Liinks) cuối cùng trở thành sản phẩm chính, còn Visual thì "Neither product was really like making much money" ([09:55](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=595s)).

---

## 4. Cách validate

Một cách validate thủ công, đáng học ([06:06](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=366s)):
1. Làm bản nhanh trong 2 tuần.
2. **Nhắn trực tiếp cho người** — "I built this for you. Like, do you want to use it?" — tặng họ dựng sẵn trang; một số bạn vẫn dùng đến nay trên gói free "grandfathered".
3. Lấy feedback, sửa, rồi ra Product Hunt để có traffic.
4. Mở gói premium (~$3/tháng) để thử "would people be willing to pay for this?". Đạt khoảng $100 MRR sau vài tháng.

Host nhận xét: đây là cách thực tế để có khách và validation đầu tiên, và việc không bỏ cuộc dù Linktree đã tồn tại, mà tìm một góc "simpler, maybe smaller" để làm bản thay thế. Anh nói rõ outreach thủ công là "Not scalable, but like a good way to just gauge interest".

---

## 5. Go-to-market ⭐ — phần giá trị nhất của case này

Chuỗi kênh theo thứ tự thời gian ([07:11](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=431s) đến [08:17](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=497s)):
1. **Outreach thủ công** để đo hứng thú.
2. **Product Hunt:** có traffic, từ đó nghĩ đến việc thu phí.
3. **Instagram ads:** thắng sớm, "quite a bit of growth early on"; rồi Instagram đổi thuật toán (anh không nhớ là 2021 hay 2022) nên kênh này không còn hiệu quả.
4. **Google Search Ads:** kênh dễ nhất vì là traffic có ý định cao — người đang tìm một công cụ link-in-bio hay trình tạo web — "it was quite easy to just, you know, put money in and get money out". Đây là kênh anh dựa vào nhiều nhất "over the last 4 years".

Điều đáng nhấn: đây là chiến lược **mua traffic có ý định mua trên một danh mục có sẵn nhu cầu tìm kiếm**, không cần sản phẩm khác biệt về công nghệ. Nó chạy được vì khoảng cách giữa ARPU và CAC đủ dương; video không nêu con số CAC hay payback để người xem kiểm lại.

Chi tiết không được nêu: từ khoá cụ thể, CPC, tỷ lệ chuyển đổi trang đích -> trả tiền, SEO hay organic có đóng góp không.

---

## 6. Mô hình kiếm tiền & giá

([08:34](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=514s)) Cấu trúc giá:
- **Gói cơ bản: $5/tháng** (từng $3 rồi $4). Neo thấp hơn Linktree ("sort of undercut them").
- **Pro từ $12/tháng:** domain riêng, quản lý nhiều trang (5 trang, thêm tuỳ ý). Một vài khách trả tới ~$100/tháng vì quản nhiều trang.
- **Triết lý giá:** "I would much rather have lots of customers paying like a small amount than fewer customers paying more."
- **Đòn bẩy giá:** tăng từ $4 lên $5 chỉ $1 nhưng, vì nhiều khách trả ít, "translated to nearly 5,000 in additional MRR" ([03:54](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=234s)). Nếu quy ngược thô (phép chia của người viết), nó gợi ý một cơ sở khách trả phí cỡ vài nghìn người, nhưng video không xác nhận.

Đáng chú ý cho người đọc: giá của sản phẩm cuối năm thứ 5-6 chỉ cao hơn $2 so với ban đầu — tức dư địa tăng giá lớn đã bị bỏ trống nhiều năm; gói pro là tầng ARPU cao hơn.

---

## 7. Tech stack & chi phí

Theo [12:38](https://www.youtube.com/watch?v=RSlhgyAXsBI&t=758s):

| Hạng mục | Công cụ / chi phí |
|---|---|
| Host | **VPS trên DigitalOcean** (caption ghi "Digital Ocean") |
| Lưu asset (ảnh upload) | **AWS** |
| Email thông báo và marketing | **Resend** |
| Analytics | **Tinybird** (bọc ClickHouse) |
| AI trong sản phẩm | **OpenAI API** |
| Thanh toán | **Stripe** (dashboard) |
| Quảng cáo | **Google Ads ~$100/ngày** — khoản chi lớn nhất |
| Coding agent | **$100-200/tháng**, trong khoảng 1 năm gần đây |

Tổng chi phí tháng: không nêu; hạng mục lớn nhất rõ là ads.

---

## 8. Bài học & trích dẫn

- **Chọn danh mục đã được chứng minh rồi cạnh tranh bằng một góc "đẹp hơn/rẻ hơn":** lời khuyên cuối của anh ("pick a space that's validated").
- **Đo hứng thú bằng outreach thủ công** trước khi đổ tiền.
- **Kênh có intent cao là cách mua tăng trưởng dễ nhất,** miễn unit economics dương.
- **Thời gian là biến số:** gần 6 năm, hai lần nghỉ việc, một lần phải quay lại làm công ăn lương vì COVID và gia đình.
- **Nghỉ việc theo mốc, không phải đốt thuyền:** lần hai khi MRR tương đương lương; lần đầu không có plan vững thì quay lại đi làm.

> **"I would much rather have lots of customers paying like a small amount than fewer customers paying more."**

> **"It was quite easy to just, you know, put money in and get money out."** — về Google Search Ads.

> **"Pick a space that's validated, iterate until you feel like you got something, and then lock in if you feel like it's what you want to be working on."**

**Điều video không nói / cần tỉnh táo:**
- **Survivorship bias và thời gian:** đây là sản phẩm của một kỹ sư làm 6 năm, có lương Squarespace nuôi dự án suốt thời kỳ chưa kiếm đủ tiền.
- **Hỗ trợ tài chính:** lần nghỉ việc đầu anh nói đối tác có việc lương cao, tức có "safety net" khó có với mọi người.
- **Số thiếu:** churn, số khách, CAC, payback, margin sau ads — không có.
- **Kênh trả phí thay đổi:** Instagram ads sụp khi thuật toán đổi; Google Ads cũng có thể đổi (CPC, AI Overviews, chính sách) — nhận định của người viết.
- **Phụ thuộc đối thủ lớn:** Linktree là mốc định giá; nếu họ giảm giá hoặc nâng tính năng, vị thế "rẻ hơn" yếu đi.

---

## 9. Áp dụng cho tôi (indie hacker ở VN, bán global)

**Sao chép được gì:**
- **Quy trình validate thủ công trong 2 tuần:** build bản nhỏ, tặng dùng thử trực tiếp cho vài chục người đúng đối tượng, thu feedback, rồi mới ra Product Hunt và mở gói trả phí rẻ.
- **Mua traffic high-intent bằng Google Search Ads** cho một công cụ có nhu cầu tìm kiếm rõ ràng, khi biết ROI dương; kiểm chứng bằng ngân sách nhỏ trước.
- **Định giá neo vào đối thủ lớn, chấp nhận ARPU thấp,** kèm một gói pro đắt hơn cho nhóm dùng nặng (nhiều trang, domain riêng).
- **Cách nghỉ việc/giữ job theo mốc doanh thu** (MRR ≈ lương) thay vì "đốt thuyền".

**Rào cản thật:**
- **Phân phối bằng tiền:** Google Ads ~$100/ngày cần vốn đệm và kỹ năng quản lý chiến dịch; CPC ở thị trường Mỹ/EU cho từ khoá "link in bio" cạnh tranh thế nào, video không nói.
- **Cạnh tranh:** một thị trường đông với đối thủ có hàng triệu user; sản phẩm dễ clone; khác biệt ("đẹp hơn") khó giữ.
- **Thời gian:** case này mất ~6 năm; nếu bạn cần tăng trưởng nhanh thì mô hình này không phù hợp.
- **Kỹ năng:** thấp-trung bình, nhưng anh là kỹ sư Squarespace nên có nền web builder rất mạnh; AI coding giờ giảm bớt phần này.
- **Tiếng Anh:** quảng cáo và landing page cho khách Mỹ/EU cần tiếng Anh chuẩn; hỗ trợ khách theo múi giờ Mỹ/EU là chi phí ẩn của một sản phẩm có hàng nghìn khách trả ít.
- **Thanh toán/pháp nhân:** gói thuê bao $5/tháng qua Stripe là chuẩn, nhưng thuế bán hàng quốc tế và vị thế pháp nhân của bạn cần được xử lý (merchant of record là một lựa chọn); video không nêu cách anh làm.

**Biến thể đáng thử ở thị trường trả cao:**
1. **Link-in-bio/mini-site dọc cho một nghề trả cao** thay vì "ai cũng dùng": ví dụ môi giới bất động sản, thợ ảnh cưới, huấn luyện viên cá nhân ở Mỹ/UK/Úc; gói $12-29/tháng (ước lượng của người viết) vì mỗi lead đáng nhiều tiền, và khoảng giá của Linktree không còn là mốc duy nhất.
2. **Dùng cơ chế "tầng pro nhiều trang/nhiều tài khoản"** để bán cho agency quản lý nhiều khách; anh nói đã có vài khách trả ~$100/tháng, đây là tín hiệu cho một gói agency ($50-200/tháng, ước lượng của người viết).
3. **Áp dụng cùng chuỗi "outreach -> Product Hunt -> Google Ads"** cho một công cụ nhỏ khác có từ khoá tìm kiếm rõ ràng (ví dụ trình tạo form, QR, short link), chọn ngách mà Linktree chưa làm tốt.

**Khi nào KHÔNG nên làm:**
- Bạn cần doanh thu đáng kể trong dưới 12 tháng.
- Bạn không có vốn chịu được vài tháng chạy ads chưa có lãi hoặc không muốn học quản lý Google Ads.
- Bạn chỉ có lợi thế "đẹp hơn" mà không có góc dọc hoặc kênh phân phối riêng; trong thị trường có ông lớn, tính năng khó giữ.
- Bạn muốn ARPU cao ngay từ đầu; đây là mô hình khối lượng lớn, giá thấp, cần churn thấp (video không nêu churn).

---

## Nguồn

- Video: [I quit my job to build this micro-saas. Now it makes $30K/month](https://www.youtube.com/watch?v=RSlhgyAXsBI) — Starter Story, 21/10/2026, 15:58, 148K views
- Transcript: [`transcript.md`](transcript.md)
