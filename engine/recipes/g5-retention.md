---
id: g5-retention
strategy: G5
title: "Giữ chân và kích hoạt lại: nói chuyện với người dùng, nhắc, cứu người sắp huỷ, đo ai ở lại"
label: manual                  # nhắn, gọi, đặt nhắc và đọc số bằng tay; công cụ chỉ gửi và đếm
time: "2–3 giờ dựng kênh phản hồi và nhắc đầu tiên; đọc số 15 phút mỗi tuần"
cost: "$0 để làm tay; công cụ gửi tin (Twilio, Loops, Intercom) tuỳ nhà cung cấp, kho không nêu giá"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: [twilio, loops, intercom, mixpanel, posthog]
status: draft
---

## Dùng khi
Sản phẩm đã có người dùng và có người trả tiền, nhưng họ **không quay lại hoặc huỷ sớm**. Chạy sau `g1-first-10-users` và `g4-pricing-paywall`; đo kết quả bằng `g8-funnel-measurement`. Nếu chưa ai dùng thử thì chưa có gì để giữ: quay lại `g1`. Bằng chứng trong kho là các việc thủ công nhỏ, không có hệ thống giữ chân nào mà nhiều founder cùng dùng.

## Đầu vào
Danh sách người dùng đang hoạt động và người đã bỏ (có email hoặc số điện thoại nếu đã xin đồng ý), một cách đếm "quay lại sau 7 và 30 ngày" (từ `g8`), và 1–2 giờ mỗi tuần để nói chuyện với người dùng.

## Các bước
1. **[manual] Mở một đường liên lạc trực tiếp và trả lời nhanh.** Oceans trả lời email trong khoảng 5 phút, khi có lỗi thì xin lỗi và tặng một tháng dịch vụ, và bám sát 20–50 khách đầu qua điện thoại. Yadaphone nhắn từng khách đã trả tiền trong 6 tháng để xin phản hồi (câu ở bảng). Cleo gọi onboarding VIP cho khách đầu và ghi âm để tìm lỗi lặp lại. Tibo cho link hỗ trợ trong app dẫn thẳng vào DM Twitter của anh cho tới khi app đạt 10k mỗi tháng. Gravl có chat hỗ trợ 24/7 do người thật trả lời.
2. **[manual] Xem người dùng thật làm gì rồi sửa trong ngày.** Blog to Pin xem video ghi màn hình khi người dùng gặp vấn đề (câu ở bảng) và làm tính năng họ cần trong vài giờ đến vài ngày. Data Fetcher nói chuyện trực tiếp với người dùng, tìm ra nhiều lỗi UX trong một buổi chiều và sửa; founder nêu doanh thu và usage tăng gần như ngay. Wishlists lưu yêu cầu tính năng của từng người rồi nhắn riêng khi làm xong.
3. **[manual] Đặt một nhắc hoặc trigger cho khoảng thời gian dễ bỏ.** Clear 30 xin số điện thoại trong onboarding, nhắn SMS qua Twilio và bật thông báo tự động sau 2 ngày. Flame đưa câu hỏi hằng ngày thành tính năng chính và đặt thông báo theo giờ (carrot buổi sáng, stick buổi chiều); founder nêu retention ngày 30 từ 4.2% lên khoảng 50% (tự khai, một case). Wrestle AI chia thông báo theo hành vi, có thông báo sau khi mua, bắt chước Duolingo. Flame cũng thêm widget lock screen.
4. **[manual] Cứu người sắp huỷ hoặc đã huỷ.** Coconote khi người dùng bấm huỷ thì gia hạn trial thêm 7 ngày, giữ khoảng 27% người vào flow huỷ (founder nêu). Một founder Starter Story (video không gắn case) gửi email qua Loops cho người đã churn để kéo họ quay lại. Barn2 gửi email giảm 50% plugin kế tiếp sau 3 ngày mua. Floga lập nhóm Telegram cho người mua lifetime.
5. **[manual] Biết ai là người ở lại.** Brainrot đọc analytics tìm power user và gửi sự kiện về Mixpanel hoặc PostHog; Fastlane theo dõi power user rồi gọi hỏi nền tảng giúp họ thế nào. Expert (người mua app, kênh Superwall) lấy top 20% người dùng theo engagement, vẽ đường retention và tìm chỗ đường cong phẳng. Kết quả của bước này là danh sách người để nói chuyện ở bước 1.
6. **[manual] Ghi nhật ký:** ngày, việc làm, nhóm người dùng, số quay lại ngày 7 và 30 (từ `g8`), số huỷ. Chỉ đổi một việc mỗi 2 tuần (đề xuất, chưa có số của kho).

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "nhóm người dùng × số quay lại sau ngày 7 và 30 × số huỷ trong tháng", mỗi hàng ghi việc giữ chân đã làm. Đầu vào của `g8-funnel-measurement` và của việc sửa onboarding trong `g4-pricing-paywall`.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 30 ngày làm một việc ở bước 1–4, tỉ lệ quay lại ngày 30 của nhóm làm việc đó cao hơn nhóm không làm hoặc cao hơn chính mình tháng trước. Kho không có chuẩn retention dùng chung: các số (Flame khoảng 50% ngày 30, Pray Screen khoảng 60% ngày 30, Postiz churn 13,7%) là lời một founder cho một sản phẩm, không phải mốc.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 36 step trong 29 video |
| Case (video, case) có step này | 25, trong đó 24 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 4/36 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 11/24 |
| Case full không nêu existing_audience | 19/24 |
| Case full video không kể bằng chứng nhu cầu trước launch | 13/24 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 20.0 tháng (10.8–42.0), n=16 |
| Kênh scale trả tiền / thuần organic / không nêu | 7 / 16 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g5-retention.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
**Bằng chứng founder còn mỏng:** 36 step, 24 case full. Mục con (câu truy vấn: `engine/recipes/g5-retention.extra.sql`; các nhóm chồng lấn nhau): trong 24 case full, step về nói chuyện, hỗ trợ, xin phản hồi hoặc review ở 17 case, về huỷ, churn, bán chéo hoặc cộng đồng người mua ở 6, về thông báo, nhắc, SMS, widget ở 5, về đo power user hoặc analytics ở 4. Theo `community_insider`: 17 trong cuộc, 4 **outsider**, 3 **không nêu**; đừng gộp outsider với không nêu. 34/36 step ở chặng retain. Có 4 step không gắn case: 1 là expert (kênh Superwall), 3 nằm trong video founder của Starter Story (founder kể, không có hồ sơ case); 13 step đến từ kênh Superwall (11 founder, 2 expert) và 23 từ Starter Story. Số tháng tới mức doanh thu hiện tại có trung vị cao hơn g4 (11.0) và g8 (12.5) (20.0 tháng, n=16), nghĩa là retention được kể nhiều ở sản phẩm chạy lâu; không đọc thành "retention làm chậm".

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Denis (Yadaphone) (founder) · `2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month` · 10:38 | "I used to text every single paying customer for 6 months asking for feedback." | founder kể: nhắn từng khách đã trả tiền trong 6 tháng để xin phản hồi |
| Nick (Blog to Pin) (founder) · `2026-02-05_i-make-16k-month-even-in-a-tiny-niche` · 07:43 | "I take a deep care about everyone using the app. I review screen recordings of what they do when something happens with their account" | founder kể: xem video ghi màn hình hành vi người dùng khi họ gặp vấn đề |
| Erikas (Kaching Bundles) (founder) · `2025-04-19_my-apps-make-4-5m-year-with-0-marketing` · 11:16 | "So, once we said that it's crucial for us to get those five-star reviews, we optimized all of our processes towards it." | founder kể: coi review 5 sao là mục tiêu và dồn quy trình hỗ trợ vào đó |
| Tibo (founder) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 10:53 | "you will spend a lot of energy pushing people to your software, and 99% of those people are going to flow away directly after trying your software. You need to make sure that your retention is good." | founder kể: đẩy người dùng vào mà không giữ chân thì 99% bỏ đi sau khi thử |
| Tibo (founder) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 17:09 | "Talk to your user every day and understand their core situation." | founder kể: nói chuyện với người dùng mỗi ngày để hiểu tình huống của họ |
| George (Wrestle AI) (founder) · `2026-10-12_ex-wrestler-41k-ai-apps` · 00:40:21 | "You're never exiting if you don't care about retention." | founder kể: coi retention là điều kiện để có đường thoát (exit) |
| Josh (host/expert) · `2026-07-08_172m-of-app-building-advice-in-50-minutes` · 00:14:49 | "To put it quite simply, revenue multiples are really just present value math on LTV. And the leading indicator of your LTV is cohort retention." | lời của expert (người mua app, kênh Superwall): chỉ báo sớm của LTV là retention theo cohort |
| Pat Walls (host/expert) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 18:12 | "Talk to customers every single day. Be on X and have that direct line of communication with your customers." | lời khuyên của host: nói chuyện với khách hằng ngày, có đường liên lạc trực tiếp |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 24 case full dùng g5; founder giữ chân thất bại không có trong kho. Truy vấn mục (4) của `extra.sql` chỉ tìm được 4 case full có số retention hoặc churn (Flame, Pray Screen, Postiz, Coconote); đều tự khai, không có dashboard.
- **Phần lớn là việc thủ công, không mở rộng được.** Nhắn từng khách, gọi điện, gửi email: hợp với vài chục đến vài trăm người dùng đầu. Kho không cho thấy cách làm này còn chạy khi có hàng chục nghìn người.
- **Giữ chân và onboarding là việc khác nhau.** Nhiều founder làm sửa bằng cách nói chuyện, nhưng lời hứa sản phẩm (xem `g4-pricing-paywall`, mục D) quyết định ai ở lại từ đầu; nhắc và thông báo không cứu một sản phẩm không có nhu cầu. Tibo nói 99% người bị đẩy vào sẽ bỏ nếu giữ chân kém (câu ở bảng): kết luận của một founder, không phải số của kho.
- **Thông báo có thể đổi thành sự phiền.** Flame mô tả stick là làm người yêu buồn chứ không phải mất streak (ghi trong step); kho không có số về khiếu nại hay tắt thông báo.
- **Người đứng ngoài ngách.** 3/24 case full ghi rõ outsider và 3 không nêu; không rút quy luật riêng được.

## Quyết định
- **QUA** nếu có cách đếm quay lại ngày 7 và 30, ít nhất một kênh nói chuyện trực tiếp đang chạy hằng tuần, và một việc giữ chân đã thử có so sánh (đề xuất, chưa có số của kho).
- **DỪNG** thêm nhắc, ưu đãi huỷ nếu sau 3 lần đổi (đề xuất, chưa có số của kho) ngày 30 không nhích: nguyên nhân nằm ở sản phẩm hoặc nhóm khách, quay lại `VALIDATE.md`.
- **TEST THÊM** nếu người dùng nói chuyện cho thấy một lý do bỏ lặp lại: sửa đúng lý do đó trong 14 ngày (đề xuất, chưa có số của kho) rồi đo lại ngày 30.

## Cho solo founder bán global (từ VN)
- **Chép được:** nói chuyện với người dùng, xem video ghi màn hình, email churn, nhắc trong app. Toàn bộ làm được từ xa, không cần pháp nhân riêng.
- **Rào cản thật:** (1) **múi giờ**: Oceans trả lời trong khoảng 5 phút và Gravl có chat 24/7; ở VN, phản hồi nhanh cho khách Mỹ có thể rơi vào ban đêm, nên đặt giờ trả lời rõ ràng thay vì hứa chung. (2) **SMS và email cho khách quốc tế**: nhắn SMS qua Twilio hoặc email churn có thể cần đồng ý và tuân quy định từng nước (kho không nêu; cần kiểm riêng). (3) Tiếng Anh bản xứ trong tin nhắn hỗ trợ ảnh hưởng độ tin cậy. (4) Gọi điện cho người dùng từ VN tốn chi phí và gặp lệch giờ; dùng video call hẹn trước.
- **KHÔNG nên làm** khi chưa có người trả tiền để giữ (làm `g1` trước), hoặc khi chỉ định dùng thông báo dày để kéo người dùng không có nhu cầu quay lại.
