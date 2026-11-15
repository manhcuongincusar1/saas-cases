---
id: g12-outbound-b2b
strategy: G12
title: "Bán hoặc hợp tác với doanh nghiệp một cách chủ động: cold email, đề xuất hợp tác bằng bằng chứng, chốt gói cho công ty hoặc agency"
label: manual                  # viết email và gọi bằng tay; agent chỉ giúp lập danh sách công ty và ghi nhật ký
time: "3 giờ dựng danh sách và mẫu email; 30 ngày gửi và theo dõi"
cost: "$0 (kho không nêu chi phí cho tactic này)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

> **Bằng chứng founder còn ít:** 5 case, cả 5 là founder kể kỹ (full), 1 step của host. Không có số liệu so sánh (tỉ lệ trả lời, số email gửi) trong kho. Đây là công thức mỏng: một trang, đọc như "ai đã làm gì", không như quy trình đã chứng minh.

## Dùng khi
Khách trả tiền là **doanh nghiệp hoặc agency** (không phải người dùng lẻ), và `g1-first-10-users` (đăng ở group, DM người dùng) không chạm được người ra quyết định. Nếu khách là người dùng cuối, dùng `g1`, `g3` hoặc `g9`.

## Đầu vào
Một sản phẩm đã dùng được, một câu "công ty nào trả tiền và vì sao" (ví dụ: chuỗi bán lẻ có khách xếp hàng, agency phải gửi dữ liệu cho nhiều thương hiệu, văn phòng trị liệu), và bằng chứng mình có thể đưa ra (công việc đã làm, số liệu, hoặc bản dùng thử miễn phí).

## Các bước
1. **[manual] Chọn nhóm công ty và viết lý do họ trả tiền.** Waitly bán cho chuỗi bán lẻ có khách chờ ngoài cửa (founder Joe Rozek nói đưa Waitly vào hơn 700 địa điểm trong thời COVID và việc đó làm doanh thu năm đó tăng gấp 10); Profit AI chốt một agency ở Miami có văn phòng ở New York; Rootd ký vài hợp đồng với nhóm trị liệu và văn phòng tâm lý. Viết một dòng cho mỗi nhóm: ai gặp việc này, hiện xử lý bằng gì.
2. **[chrome] Lập danh sách ≥20 công ty trong một nhóm (số 20 là đề xuất, chưa có số của kho)** (website, tên người quyết định, email hoặc LinkedIn). Làm tay trong 15 phút một lượt; UpLead là công ty bán dữ liệu liên hệ B2B nên có công cụ riêng, kho không nêu công cụ nào cho solo.
3. **[manual] Chuẩn bị "bằng chứng" trước khi gửi.** Milly (Generalist World) không chờ đối tác mời: đưa Beehive toàn bộ công việc đã làm và kết quả rồi đề xuất hợp tác; kết quả là hợp đồng một năm, lớn nhất của cô. Host Ryan (Superwall) nói bán B2B cần chứng minh ROI bằng khảo sát. Ghi ra 3 dòng bằng chứng của mình (số liệu, ảnh chụp, một khách đang dùng).
4. **[manual] Viết email ngắn theo mẫu UpLead:** tiêu đề có tên người nhận, dòng mở nhắc một điểm chung (LinkedIn), so với đối thủ lớn nhất nhưng rẻ hơn, mời dùng thử miễn phí. Số email mỗi ngày: không có số trong kho.
5. **[manual] Gửi, theo dõi lại, rồi chuyển sang gọi hoặc demo.** Kho không kể chi tiết cách Rootd tiếp cận nhóm trị liệu (video không nói). Profit AI sau khi chốt agency cho họ gửi yêu cầu dữ liệu qua bot Slack, tức bước "dùng thật" phải rất nhẹ.
6. **[manual] Ghi nhật ký:** công ty, ngày gửi, trả lời hay không, cuộc gọi, trả tiền hay không.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "công ty đã liên hệ": mỗi dòng là một công ty gồm ngày, kênh, có trả lời không, có cuộc gọi không, có thử miễn phí không, có trả tiền không.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 30 ngày, ≥2 cuộc gọi hoặc demo với người quyết định và ≥1 công ty thử có theo dõi. Nếu mục tiêu là xác nhận có người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 6 step trong 6 video |
| Case (video, case) có step này | 5, trong đó 5 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/6 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 4/5 |
| Case full không nêu existing_audience | 5/5 |
| Case full video không kể bằng chứng nhu cầu trước launch | 5/5 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 26.5 tháng (15.8–37.3), n=2 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 4 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g12-outbound-b2b.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Cả 5 case full là người trong cuộc (insider); không có case outsider hay "không nêu" (câu truy vấn: `engine/recipes/g12-outbound-b2b.extra.sql`). Trong 5 case, UpLead nói triệu đô ARR đầu tiên chỉ từ cold email (tự khai); Generalist World là hợp tác lớn nhất sau đề xuất chủ động; Waitly và Rootd là khách trả theo nhóm công ty. Số tháng tới mức doanh thu hiện tại chỉ có ở 2/5 case nên đừng đọc trung vị. Cả 6 video là kênh có bán chương trình hoặc quảng bá (Starter Story, Superwall): số liệu là lời founder.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Kho có ít câu nguyên văn cho tactic này, nên bảng ngắn.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Will Cannon (UpLead) (founder) · `2025-10-01_my-two-apps-made-30m` · 08:29 | "Uple got its first 1 million in annual recurring revenue strictly from cold email" | founder kể: triệu đô ARR đầu tiên của UpLead chỉ đến từ cold email (founder tự khai, không có dashboard) |
| Will Cannon (UpLead) (founder) · `2025-10-01_my-two-apps-made-30m` · 02:04 | "That's what we did for about 10 years from 2007ish to 2017" | founder kể: khoảng mười năm làm agency cold email trước khi làm UpLead, tức đã có kỹ năng này sẵn |
| Will Cannon (Signaturely) (founder) · `2025-10-01_my-two-apps-made-30m` · 03:36 | "we used our SEO and cold email and other skill sets to acquire customers" | founder kể: dùng SEO, cold email và các kỹ năng có sẵn để lấy khách |
| Ryan (host/expert) · `2026-01-17_meet-the-guy-dominating-the-app-store` · 00:42:55 | "It can take six to 12 months to get one contract, but one contract could be, you know, a quarter of your revenue uh in the year if played well." | lời khuyên của host/expert (video của công ty bán paywall): một hợp đồng B2B có thể mất sáu đến mười hai tháng nhưng đáng bằng một phần tư doanh thu năm |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 5 founder làm B2B chủ động và đủ thành công để lên kênh; không có số người gửi email lạnh mà không ai trả lời. Số 5 quá nhỏ để nói tỉ lệ.
- **Cold email có thể gần như vô ích.** Bank Statement Converter gửi cold email trong 3 tháng chỉ được 1 đơn và nhiều phản hồi giận dữ (step thuộc `g1-first-10-users`, cùng cảnh báo ở công thức đó). UpLead thì nói cold email là nguồn của triệu đô ARR đầu tiên, nhưng đó là công ty bán dữ liệu cho người làm cold email, và founder làm agency cold email khoảng mười năm trước (câu ở bảng): kỹ năng có sẵn khác với một solo mới bắt đầu.
- **Chu kỳ chốt dài.** Host Ryan nói mất 6 đến 12 tháng cho một hợp đồng (câu ở bảng; đoạn này nói về app thiền chuyển sang B2B). Với solo đang đo "có ai trả tiền không" trong vài tuần, đây là lệch tốc độ.
- **Đề xuất chủ động cần bằng chứng có sẵn.** Milly đưa "toàn bộ công việc đã làm"; nếu chưa có công việc nào, bước 3 trắng.

## Quyết định
- **QUA** nếu sau 30 ngày có ≥2 cuộc gọi hoặc demo với người quyết định và ≥1 công ty thử có theo dõi (ngưỡng đề xuất, chưa có số của kho). Ghi kênh và mẫu email có phản hồi vào `g1` để làm đều.
- **DỪNG** nếu gửi tới ≥40 công ty đúng nhóm mà 0 người trả lời (đề xuất, chưa có số của kho): sai nhóm, sai bằng chứng, hoặc khách thật không phải doanh nghiệp; quay về `VALIDATE.md`.
- **TEST THÊM** nếu có trả lời nhưng chưa có cuộc gọi: đổi dòng mở (nói nỗi đau của họ, không nói tính năng), thử nhóm công ty khác nhỏ hơn, chạy lại 14 ngày.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ bước 1–6 làm từ xa bằng email và LinkedIn; không cần có mặt. Hợp tác với agency hoặc chuỗi có thể chỉ cần một khách đầu để thành "bằng chứng" cho khách sau.
- **Rào cản thật:** (1) tiếng Anh viết cho người quyết định, email lạnh dở bị xoá ngay; (2) múi giờ khi gọi demo, phải có lịch linh hoạt; (3) công ty Mỹ/EU thường hỏi hóa đơn, điều khoản, đôi khi cần pháp nhân hoặc tài khoản Stripe/ngân hàng nhận USD; (4) chu kỳ chốt dài so với runway; chi phí sống thấp giúp chịu được.
- **KHÔNG nên làm** nếu sản phẩm chưa có ít nhất một khách dùng thật để làm bằng chứng, hoặc nếu khách là người dùng lẻ (đi `g1`, `g9`), hoặc nếu mình không thể chịu chu kỳ chốt nhiều tháng.
