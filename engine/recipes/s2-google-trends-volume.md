---
id: s2-google-trends-volume
strategy: S2
title: "Đo lượng tìm kiếm trên web (Google Trends, Ahrefs) cho một ý tưởng đã có"
label: chrome                  # công cụ web, nhiều bước cần đăng nhập hoặc trả phí
time: "30–60 phút cho một ý tưởng"
cost: "$0 (Google Trends); Ahrefs/Keyword Everywhere có phí hoặc bản giới hạn"
evidence: corpus
signal_level_when_pass: 2      # chỉ cho biết có người tìm; chưa phải nhu cầu trả tiền (mức 2 của thang VALIDATE.md: chủ đề có nhiều view)
tools: []
status: draft
---

> **Bằng chứng founder còn ít (4 case).** Một trang mỏng: công thức này chỉ đo "có người tìm không", không chọn ý tưởng và không chứng minh có người trả tiền.

## Dùng khi
Đã có một ý tưởng và cần biết có cụm từ web cụ thể mà người ta gõ khi gặp vấn đề không (`VALIDATE.md` cổng 1.3). Với app trên App Store dùng `s2-aso-keyword-gap`, không phải công thức này.

## Các bước
1. **[chrome] Google Trends** cho cụm từ gốc, 5 năm gần nhất: ổn định, tăng hay giảm. Founder Stoppr xem cụm "stop sugar" trong 5 năm gần đây.
2. **[chrome] Volume và độ khó:** Ahrefs Keywords Explorer (hoặc Keyword Everywhere). Ngưỡng founder trong kho đã dùng: Neural Frames chỉ coi là có nhu cầu khi có hơn 1.000 lượt tìm mỗi tháng và độ khó thấp; SiteGPT lọc volume ≥1.000/tháng và KD <10 (mỗi ngưỡng chỉ từ một case, không phải số của kho).
3. **[chrome] Lập bảng ưu tiên** theo volume, độ khó, công sức build, độ liên quan tới sản phẩm chính (SiteGPT).
4. **[manual] Đặt từ khoá vào landing page** (Setter AI chọn từ khoá có volume mà ít đối thủ rồi dùng làm H1).
5. Chuyển sang `s8-content-demand-test` hoặc `s7-preorder-buy-button`: volume không phải tiền (xem bẫy).

## Đầu ra
Một dòng cho mỗi cụm: volume · độ khó · xu hướng · quyết định.

## Ngưỡng qua
Ngưỡng ở `VALIDATE.md` cổng 1.3. Con số founder nêu ở bước 2 chỉ để tham khảo.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
8 step, 4 case full, 1 step chỉ do host/expert mô tả. Tháng tới doanh thu hiện tại chỉ có n=1: không rút ra gì về tốc độ. Trong 4 case, 3 video không kể bằng chứng nhu cầu trước launch; Setter AI kể một khoản $500 đầu tiên qua Stripe.

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 8 step trong 5 video |
| Case (video, case) có step này | 4, trong đó 4 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/8 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 3/4 |
| Case full không nêu existing_audience | 3/4 |
| Case full video không kể bằng chứng nhu cầu trước launch | 2/4 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 5.0 tháng (5.0–5.0), n=1 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 3 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s2-google-trends-volume.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| David Attias (founder) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-break` · 05:02 | "So, I validated by keyword research and by content research on TikTok and Instagram" | founder kể: kiểm bằng nghiên cứu từ khoá và nội dung TikTok/Instagram, rồi clone app đã thành công (Stoppr) |
| Joseph hoặc Timo (founder) · `2025-09-27_how-we-built-a-10k-mo-saas` · 04:07 | "I think the only way to validate is when buyers swipe their credit card." | giới hạn từ founder Setter AI: chỉ khi người mua quẹt thẻ mới là validate |
| Pat Walls (host/expert) · `2025-09-27_how-we-built-a-10k-mo-saas` · 06:26 | "Collecting cash before writing code is definitely the way to go, especially if you want to ship a successful app as a solo founder." | lời khuyên của host: thu tiền trước khi viết code |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Volume không phải tiền.** Chính founder Setter AI nói validate là khi người mua quẹt thẻ (bảng), và host nhắc thu tiền trước khi viết code.
- **Từ khoá trống có thể nghĩa là chưa ai kiếm được tiền ở đó** (`VALIDATE.md` cổng 1.3).
- **Kho chỉ chứa người thắng** và chỉ 4 case; ngưỡng ở bước 2 mỗi cái từ một founder.
- **Phụ thuộc công cụ có phí.** Các con số volume/KD do Ahrefs; bản miễn phí khác.

## Quyết định
- **QUA** nếu có cụm từ cụ thể, volume và độ khó chấp nhận được theo `VALIDATE.md` 1.3. Chỉ mức tín hiệu 2; chưa đủ để build.
- **DỪNG** nếu không có cụm từ nào gọi được tên vấn đề.
- **TEST THÊM** nếu có volume nhưng chưa thấy ai trả tiền: chạy `s7-preorder-buy-button` hoặc `s8-content-demand-test` trong 1–2 tuần.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ, từ xa, không cần là người trong ngách; hợp với lựa chọn organic (SEO).
- **Rào cản thật:** Ahrefs/Keyword Everywhere có phí; volume ở Mỹ/UK khác volume toàn cầu, nên đặt vùng cho đúng thị trường bán.
- **KHÔNG nên làm** khi sản phẩm chỉ sống ở App Store (dùng `s2-aso-keyword-gap`) hoặc khi khách không tìm bằng Google (B2B truyền miệng, cộng đồng kín).
