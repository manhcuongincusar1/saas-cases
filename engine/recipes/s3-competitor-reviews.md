---
id: s3-competitor-reviews
strategy: S3
title: "Đọc review đối thủ để tìm nỗi đau và nhóm khách bị bỏ sót"
label: auto            # review SaaS (G2, Capterra, AppSumo) và comment YouTube là chrome
time: "2–3 giờ cho 3–5 đối thủ"
cost: "$0"
evidence: corpus
signal_level_when_pass: 4     # "người ta tự khai nỗi đau/dữ liệu của mình" của thang VALIDATE.md
tools: [engine/tools/reviews.py]
status: draft
---

## Dùng khi
Đã có 1–5 đối thủ (từ `s2` hoặc `s1`) và muốn biết: **ai đang dùng họ, họ ghét gì, nhóm nào đang xin một bản hẹp hơn**. Đây là công thức đã giết Hairmint khi bị bỏ qua (`VALIDATE.md` cổng 2).

## Đầu vào
3–5 đối thủ: App Store id (app) hoặc tên sản phẩm (SaaS).

## Các bước
1. **[auto] Lấy review gần nhất của từng app.** `python3 -I engine/tools/reviews.py <appId> --cc us --pages 5 --show 50`. RSS chỉ trả review **gần nhất**, đủ cho cổng 2 (≥100) nhưng không phải toàn bộ lịch sử. Ghi phân bố sao.
2. **[auto] Đọc cho từng review ba thứ**, như `VALIDATE.md` 2.1–2.2: *người viết là ai* (tuổi, vai trò, "tôi là X"), *họ ghét gì* (tiền, sai kết quả, lỗi, huỷ gói), *họ muốn gì* ("I wish", "I'd pay", "does it do X?").
3. **[auto] Gom và cụm.** Đưa toàn bộ review vào Claude để cụm theo chủ đề và nhóm người viết (cách đã có người dùng: xem bằng chứng bên dưới). Đừng chỉ đọc 1–2★: đọc cả 4–5★ để biết ai trả tiền và hài lòng.
4. **[auto] Loại nhiễu rating.** Kiểm app có xin đánh giá ngay sau khi người dùng vừa thấy kết quả không (rating sẽ bị đẩy lên). Chỉ tin review có chữ, đọc phân bố sao của review có chữ riêng.
5. **[chrome] Mở rộng ngoài App Store** nếu sản phẩm là SaaS/web: review trên G2, Capterra, AppSumo; video YouTube trong ngách **ít view nhưng nhiều comment** (nhiều comment = nỗi đau chưa được giải).
6. **Ghi ứng viên**: mỗi nhóm khách + nỗi đau lặp lại thành một file trong `journey/ideas/` (`status: inbox`), kèm trích nguyên văn vài review làm bằng chứng (ghi app, ngày, số sao).

## Đầu ra
Bảng: đối thủ · nhóm người viết · nỗi đau/mong muốn · số review chứa nó / tổng số review có chữ · trích nguyên văn (app, ngày, sao) · cổng 2.x tương ứng. Rồi các file ứng viên.

## Ngưỡng qua
Cổng **2.1, 2.2, 2.6** của `VALIDATE.md`, không viết lại ở đây (≥100 review gần nhất; người dùng thật trùng nhóm mình sẽ bán; có chỗ yếu mình làm tốt hơn). Hai số tạm của riêng công thức này, **chưa có nguồn từ kho, sẽ chỉnh sau lần chạy thật đầu tiên**: một chủ đề phải lặp ở khoảng ≥10% review có chữ; nhóm xin "bản hẹp hơn" phải tự nhận danh tính rõ ràng.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
Nhãn bằng chứng: **mỏng**. 5 step, 4 case founder; 1 step là host/expert mô tả. Mọi số trung vị/tỉ lệ ở bảng dưới có n nhỏ (≤4).

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 5 step trong 5 video |
| Case (video, case) có step này | 4, trong đó 4 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/5 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 4/4 |
| Case full không nêu existing_audience | 4/4 |
| Case full video không kể bằng chứng nhu cầu trước launch | 1/4 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.8 tháng (7.2–18.4), n=2 |
| Kênh scale trả tiền / thuần organic / không nêu | 0 / 3 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s3-competitor-reviews.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
23 câu trích đã dò nguyên văn + mốc giây ở `engine/evidence/s3-competitor-reviews.yaml`. Chọn lọc:

| Ai · video · mốc | Nguyên văn (rút gọn) | Dùng cho |
|---|---|---|
| Founder Rooted · `2025-08-31_this-app-made-over-1m` · 00:02:07 | "I noticed a common theme in the user reviews that there was this gap" | đọc review đối thủ để tìm khoảng trống, rồi làm MVP lấp nó |
| Founder app peptide/GLP · `2026-05-24_i-built-a-30k-month-in-35-days` · 09:02 | "I would literally go through every single review on all these apps." | đọc hết, không lấy mẫu |
| cùng video · 09:19 | "find what people like, what they don't like, what they wish the app had, and then take all that and give it to Claude or ChatGPT" | gom rồi nhờ Claude cụm |
| Founder Signature League · `2025-10-01_my-two-apps-made-30m` · 00:04:23 | "go look at the one and two star reviews and see what people are complaining about… Our twist is what people dislike about the biggest companies in the space because those are the easiest customers to go after and acquire." | chọn góc: làm đúng điều khách ghét ở ông lớn |
| Founder app ngách 16K · `2026-02-05_i-make-16k-month-even-in-a-tiny-niche` · 00:10:02 | "Research their G2 reviews, maybe Absumo reviews, Capterara." | nguồn cho SaaS |
| Bikash · `2026-02-11_how-i-built-a-12k-month-micro-saas` · 00:08:19 | "find out videos that has not high views but high number of comments. High comments signals customer pain which is unresolved" | comment YouTube làm tín hiệu nỗi đau |
| Founder Rooted · cùng video với dòng đầu · 00:09:44 | "Oftentimes everything you need to know is written in the user reviews and sometimes your own assumption of what a user needs might not actually be what they do need." | bằng chứng thắng giả định của mình |

## Bẫy và phản ví dụ
- **Rating không nói ai đang trả tiền.** Hairmint: nhìn điểm rating mà không đọc ai để lại rating (xem `VALIDATE.md` 2.1, 2.6; review toàn teen trong khi người trả tiền là 25–45).
- **App xin review đúng lúc người dùng vui.** Founder Glow Up (`2025-12-17_my-mobile-app-made-800k-in-365-days` · 00:09:36): "we do ask to leave a rating… Usually they leave a fivestar review. Then the reviews gets pretty high in the app store". Rating cao có thể là hệ quả của cách xin, không phải của sản phẩm.
- **Cộng đồng có thể bác một hướng.** Founder Shepherd (`he-made-22m-from-building-simple-apps-heres-how-no-code` · 00:28:09): thêm tính năng chat AI và "we had like some backlash in our Discord", họ bỏ nó.
- **RSS chỉ cho review gần nhất.** Đủ để thấy xu hướng hiện tại, không đủ để đếm lịch sử.
- **Chưa phải nhu cầu của khách mình.** Review nói về đối thủ. Tối đa tới mức 4 (người ta tự khai nỗi đau), chưa phải mức 5 (hỏi mua).

## Quyết định
- **QUA** nếu có một nhóm người rõ danh tính trùng nhóm sẽ trả tiền, một nỗi đau lặp lại mà đối thủ làm tệ, và mình làm được tốt hơn. Việc tiếp theo là hỏi/nhắn thẳng nhóm đó (mức 5–6) hoặc `s7`.
- **DỪNG** nếu người dùng thật không trùng nhóm sẽ trả tiền (bài học Hairmint), hoặc nỗi đau chỉ là lỗi kỹ thuật mà đối thủ sửa được trong một bản cập nhật.
- **TEST THÊM** nếu chủ đề lặp nhưng chưa rõ ai viết: trong 7 ngày đọc thêm review của 2 đối thủ khác, hoặc mở tay `r/<ngách>` (`s3-reddit-pain-mining`) để xem cùng nỗi đau có xuất hiện ngoài App Store không.

## Cho solo founder bán global (từ VN)
- **Chép được:** đọc review/comment công khai của đối thủ là việc làm từ xa, $0, và không đòi mình là người trong ngách; hợp với solo đứng ngoài.
- **Rào cản thật:** chỉ 4 case founder trong kho dùng cách này, nên đừng coi là đã kiểm chứng rộng. Review bị bóp méo bởi app nhắc chấm 5 sao (`VALIDATE.md` cổng 2.1); review SaaS (G2, Capterra) cần mở bằng Chrome.
- **KHÔNG nên làm** khi đối thủ quá mới/ít review (không đủ dữ liệu) hoặc khi nhóm viết review không phải nhóm sẽ trả tiền cho mình (cổng 2.6).
