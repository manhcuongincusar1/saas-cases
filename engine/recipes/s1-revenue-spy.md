---
id: s1-revenue-spy
strategy: S1
title: "Soi doanh thu để tìm ngách đang có tiền, rồi chọn góc riêng"
label: auto            # bước kiểm doanh thu (TrustMRR, Sensor Tower) là chrome
time: "1–2 giờ cho 1–3 genre"
cost: "$0 (Sensor Tower bản miễn phí chỉ cho ước tính thô)"
evidence: corpus
signal_level_when_pass: 3     # "app tương tự đang bán được, có doanh thu"
tools: [engine/tools/topgrossing.py, engine/tools/kw.py]
status: draft
---

## Dùng khi
Chưa có ngách nào. Thay vì ngồi nghĩ, đi xem **người ta đang trả tiền cho cái gì** rồi tìm góc hẹp hơn hoặc khác đi. Đây là cách nhanh nhất được nhắc nhiều nhất trong kho, nhưng cũng là cách dễ ra bản sao thua app gốc nhất (xem bẫy).

## Đầu vào
1–3 genre (Health & Fitness, Education, Productivity…) hoặc một cụm vấn đề đã có từ `s2`.

## Các bước
1. **[auto] Lấy app đang có tiền, ra mắt gần đây.** `python3 -I engine/tools/topgrossing.py --genre <id> --limit 100 --since 2025-06-01` (genre id ở đầu file công cụ). Mục tiêu là các app **ra mắt gần đây và còn ít rating mà đã vào top-grossing**: chart đánh giá thấp số app nhỏ đang ăn nên làm ra. Chạy cả `--cc gb`.
2. **[auto] Xem cả ngách chứ không chỉ một app.** Với mỗi app, gõ cụm mô tả việc nó làm vào `engine/tools/kw.py` (và `autofill.py` của `s2`), xem còn ai cùng làm việc đó ở top 20. Founder Pray Screen: bước 1 là xem top 1 từng category, rồi tìm các app cùng làm một việc ở top 20.
3. **[chrome] Kiểm doanh thu.** TrustMRR (số đã xác minh) trước; Sensor Tower bản miễn phí chỉ để xếp thứ tự lớn nhỏ vì lệch 10–30 lần. Ghi rõ từng con số là *đã xác minh* hay *ước tính*.
4. **[auto] Tính cả ngách có nhiều app cùng kiếm tiền không.** Lino chỉ chọn ngách mà "a ton of apps… consistently doing over 10k a month". Một app lẻ có tiền có thể là ngoại lệ.
5. **[chrome] Chợ bán lại.** Acquire.com / Flippa: app tương tự đang rao bán kèm MRR là app đã được người khác trả tiền để mua. Đọc kỹ listing (MRR, số khách, nguồn khách).
6. **Tìm góc, đừng sao chép.** Chạy tiếp `s3-competitor-reviews` trên các app của bước 1–5 để tìm nhóm khách bị bỏ sót hoặc nỗi đau mà họ làm tệ.
7. **Ghi ứng viên** vào `journey/ideas/` (`status: inbox`): ngách, app tham chiếu + doanh thu (đã xác minh hay ước tính), góc dự định.

## Đầu ra
Bảng: app · genre · ngày ra mắt · rating · doanh thu (số, nguồn, xác minh/ước tính) · số app cùng việc ở top 20 · góc còn trống. Rồi các file ứng viên.

## Ngưỡng qua
Cổng **1.1 (tiền đã có ngay cạnh)** của `VALIDATE.md`. Số tham chiếu từ kho, **mỗi người dùng một ngưỡng khác nhau vì mục tiêu khác nhau**:

| Ai | Ngưỡng họ dùng | Mục tiêu của họ |
|---|---|---|
| Founder Pray Screen (flip 4 app, $500k) | các app cùng ngách "over 100k MRR or over 500k MRR" | làm app lớn rồi bán |
| Lino (~50k/tháng) | "a ton of apps in that niche consistently doing over 10k a month" | ngách để build |
| Max (28 app, 10k/tháng gộp) | doanh thu đối thủ "at least 100 or €200 per month" | app nhỏ, vòng đời ngắn |
| `VALIDATE.md` 1.1 | 1–3 app ≥$100k/tháng **trong đúng ngách con** | luật của Caleb |

**Chưa quyết:** mốc $1k MRR nên dùng hàng nào trong bảng. Đề nghị `me` hoặc tôi chọn trước khi chạy thử.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
Nhãn bằng chứng: **pha trộn**. Trong 20 step, 7 là host/expert mô tả cách soi doanh thu; 13 là việc founder đã làm. Số tháng tới doanh thu hiện tại chỉ có n=6, chưa đủ để nói gì về tốc độ.

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 20 step trong 18 video |
| Case (video, case) có step này | 13, trong đó 12 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 7/20 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 9/12 |
| Case full không nêu existing_audience | 11/12 |
| Case full video không kể bằng chứng nhu cầu trước launch | 4/12 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 7.0 tháng (6.0–11.0), n=6 |
| Kênh scale trả tiền / thuần organic / không nêu | 6 / 6 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s1-revenue-spy.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
30 câu trích đã dò nguyên văn + mốc giây ở `engine/evidence/s1-revenue-spy.yaml`. Chọn lọc:

| Ai · video · mốc | Nguyên văn (rút gọn) | Dùng cho |
|---|---|---|
| David (Stoppr) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-breakdown` · 00:01:05 | "I cloned a very successful app, and first month of revenue, I made $5,000." | kết quả (ông nói $12k/tháng sau 5 tháng) |
| David · cùng video · 00:06:04 | "To confirm the revenue, you have to go to Sensor Tower" | công cụ |
| Founder Pray Screen · `2025-11-09_i-flipped-4-apps-and-made-500-000` · 00:07:05 | "step one is spotting trends in the App Store… who is currently number one in the different categories." | bước 1 |
| Lino · `2026-10-04_this-crazy-simple-app-makes-50k-month` · 08:49 | "if there are a ton of apps in that niche consistently doing over 10k a month, then that's a niche you want to build in." | ngưỡng |
| Founder app chiều cao · `2026-07-19_this-stupidly-simple-app-makes-100k-month` · 04:40 | "I was like I don't know any good ideas. I want to find a validated idea and I saw an app that's pretty similar to this for sale for around $20,000." | acquire.com làm nguồn ý tưởng đã kiểm chứng |
| Adrian · `2025-10-19_i-found-a-business-for-sale-and-rebuilt-it-into-20k` · 00:03:23 | "they were doing 30,000 monthly recurring… only got their customers from SEO, and they had less than 100 customers. So doing that math in my head, I was like, I could probably do that." | đọc listing: MRR, số khách, nguồn khách |
| Puff Count · `2024-09-24_how-i-built-it-40k-month-iphone-app` · 00:04:11 | "I looked at sensor Tower looked at other you know quit drinking or quit smoking cigarettes apps and I saw that they were crushing it looked at Google Trends saw that vaping was on the rise" | kết hợp doanh thu + xu hướng (một trong 4 lần Google Trends xuất hiện trong kho) |
| Founder clone Cal AI (Israel) · `2026-08-09_i-copied-a-huge-app-now-i-make-80k-month` · 04:06 | "the chance to take a proven winner and be the first to localize it to my local market was the simplest zero to one move" | biến thể: đổi thị trường/ngôn ngữ |

## Bẫy và phản ví dụ
- **Được chép app, đừng chép ngách.** Pat Walls cho David (`…stoppr-breakdown` · 00:08:26): "don't copy the niche. You don't want to go and take their customers".
- **Khác biệt không nằm ở sản phẩm.** Founder bản địa hoá Cal AI (`…i-copied-a-huge-app…` · 05:58): "The real differentiation… is the brand and distribution. Almost anyone can build an app with cursor in 2 weeks".
- **Ngách có thể đã bão hoà khi mình vào.** Sway AI (`i-speedran-a-new-app-from-0-to-2myear-in-6-months-heres-how` · 00:02:59): "By the time we had started working on this, there was already so many clones." Họ chọn hướng khác thay vì copy y hệt.
- **Chép được sản phẩm không chép được khách.** Người phỏng vấn Adrian (`…rebuilt-it-into-20k` · 00:04:24): phần khó là "getting customers, growing, scaling this and replicating what this business that you sort of cloned had already done".
- **Số liệu lệch.** Sensor Tower, AppMagic ước tính; số trong listing acquire.com do người bán tự khai; định giá "two to four X EBITDA" của Pray Screen là ước lượng của một founder. Chỉ TrustMRR là xác minh.
- **Doanh thu không tỉ lệ với lượt tải.** Waking Up: "this app only gets around 25k downloads a month, but it's pumping over a million dollars in revenue a month" (`172m-of-app-building-advice-in-50-minutes` · 00:00:00). Đừng đo ngách bằng số lượt tải.
- **Ví dụ ngược của "đã có người làm thì bỏ".** Calorie tracker vẫn có app kiếm khoảng 30K/tháng dù đã có Cal AI (`…this-stupidly-simple-app-makes-100k-month` · 06:42).
- **Với tôi (từ VN):** mua lại hoặc clone ngách US cần kênh phân phối ở US; công thức này tìm ngách, không giải bài toán đó.

## Quyết định
- **QUA** nếu có ≥1 ngách có nhiều app cùng kiếm tiền (số xác minh ít nhất ở app tham chiếu chính) VÀ một góc rõ mà đối thủ đang bỏ ngỏ (từ `s3`). Tối đa mức 3.
- **DỪNG** nếu app có tiền chỉ là ngoại lệ lẻ trong ngách, hoặc mọi app mới trong top đều cùng một "xưởng template", hoặc không tìm được góc nào ngoài việc sao chép y hệt.
- **TEST THÊM** nếu ngách tốt nhưng chưa có số xác minh: trong 7 ngày kiểm TrustMRR cho top 3 app; nếu vẫn thiếu thì chạy `s7` (trang pre-order) để lấy tín hiệu trực tiếp thay cho số của người khác.

## Cho solo founder bán global (từ VN)
- **Chép được:** các bước 1–5 (top grossing theo genre, kiểm doanh thu, chợ bán lại) chạy từ xa, miễn phí hoặc gần miễn phí; bước 6 nối sang `s3-competitor-reviews`.
- **Rào cản thật:** chép sản phẩm không chép được phân phối (lời phỏng vấn Adrian ở bảng bằng chứng). Số doanh thu bên thứ ba lệch xa (Sensor Tower 10–30 lần); chỉ TrustMRR là số xác minh. Solo không audience cần một đường organic gọi được tên trước khi chọn ngách (`s2`, `s4`).
- **KHÔNG nên làm** khi ngách chỉ có một app có tiền (ngoại lệ lẻ) hoặc mọi app mới trong top đều cùng một xưởng template, hoặc khi ngách cần giấy phép/pháp nhân mà mình chưa có (y tế, tài chính).
