---
id: s2-aso-keyword-gap
strategy: S2
title: "Khe hở từ khoá trên App Store (ASO)"
label: auto            # bước đọc doanh thu đối thủ là chrome
time: "1–2 giờ cho 5–10 cụm gốc"
cost: "$0"
evidence: corpus
signal_level_when_pass: 3     # "app tương tự đang bán được" của thang VALIDATE.md; chưa phải nhu cầu của khách riêng
tools: [engine/tools/autofill.py, engine/tools/kw.py]
status: draft
---

## Dùng khi
Muốn biết **người ta gõ chính xác gì khi gặp vấn đề** và liệu có chỗ chen vào không, chưa cần video hay audience. Hợp với ý tưởng đi bằng tìm kiếm (app tiện ích, có từ khoá rõ). Không hợp khi vấn đề người ta không tự gõ ra được (nhu cầu gợi ra bằng video, xem `s4`).

## Đầu vào
5–10 **cụm gốc mô tả vấn đề hoặc việc cần làm** ("quit zyn", "baseball card scanner", "sleep sounds"), không phải tên tính năng.

## Các bước
1. **[auto] Lấy cụm người ta thực sự gõ.** `python3 -I engine/tools/autofill.py --cc us "<cụm gốc>" ...` Ghi danh sách gợi ý. Nguồn: John McEvoy gõ vài ký tự vào ô tìm kiếm rồi xem danh sách gợi ý để biết cụm nào có tác động cao nhất (Momego, 5 triệu lượt tải).
2. **[auto] Mở rộng sang cụm lân cận cùng nhóm khách.** Cùng khách hàng, vấn đề khác một chút (Max: study app → "physics AI", "chemistry AI", "math AI"). Lặp bước 1 với các cụm đó.
3. **[auto] Đo cạnh tranh từng cụm.** `python3 -I engine/tools/kw.py --cc us --n 8 "<cụm>" ...` In top app: rating, ngày ra mắt, seller. Ghi cho mỗi cụm: rating của #1, #2, #3; số app trong top 8 có đúng cụm trong tên; số app ra mắt ≤12 tháng.
4. **[auto] Đọc cái autofill nói.** Nếu gợi ý toàn là tên app chứa đúng cụm (như "quit zyn": 9/10 gợi ý là app) nghĩa là đã có nhiều app nhắm đúng từ khoá này. Đó là tín hiệu cạnh tranh, không phải lượng tìm kiếm.
5. **[chrome] Kiểm doanh thu đối thủ.** Với top 2–3 của cụm còn hứa hẹn: TrustMRR (doanh thu xác minh) hoặc Sensor Tower bản miễn phí (ước tính, lệch 10–30 lần). Chỉ cần biết có tiền hay không (xem ngưỡng).
6. **Ghi ứng viên**: mỗi cụm còn hứa hẹn thành một file trong `journey/ideas/` (`status: inbox`), kèm bảng số của bước 3.

## Đầu ra
Bảng: cụm · autofill có không · rating #1/#2/#3 · số app có cụm trong tên · số app mới ≤12 tháng · doanh thu đối thủ (nguồn, đã xác minh hay ước tính) · ghi chú. Rồi các file ứng viên.

## Ngưỡng qua
Dùng đúng **cổng 1.3 (kênh) và 1.1 (tiền ở cạnh)** của `VALIDATE.md`, không viết lại ở đây. Số tham chiếu từ kho để đặt cạnh số của mình:

| Số | Ai nói | Mốc |
|---|---|---|
| Lượng tìm kiếm từ khoá | Steve | "around 30ish and up" (ông không chắc 30 là lượt/ngày) |
| Rating của app #2–3 | Steve | "a 100 plus reviews" và ít app đặt cụm trong tiêu đề → "I could probably beat them" |
| Popularity / difficulty (Astro) | Max | popularity từ 20; difficulty "70" (Max nói "starting from 20 and difficulty uh 70", hướng so sánh không rõ trong bản chép lời) |
| Doanh thu đối thủ | Max | "at least 100 or €200 per month" (ngưỡng thấp vì ông làm app nhỏ, 28 app, 10k/tháng gộp lại) |

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
Nhãn bằng chứng: **chủ yếu expert**. 2 trong 3 step là host/expert mô tả; chỉ 1 case founder dùng (n=1 cho mọi con số). Giữ công thức vì đây là một trong ít cách tìm ý tưởng không cần là người trong cuộc và không bị khoá vùng, hợp với lựa chọn organic.

<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 3 step trong 2 video |
| Case (video, case) có step này | 1, trong đó 1 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/3 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 1/1 |
| Case full không nêu existing_audience | 1/1 |
| Case full video không kể bằng chứng nhu cầu trước launch | 1/1 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 8.0 tháng (8.0–8.0), n=1 |
| Kênh scale trả tiền / thuần organic / không nêu | 1 / 0 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s2-aso-keyword-gap.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->

## Bằng chứng từ kho
21 câu trích đã dò nguyên văn + mốc giây ở `engine/evidence/s2-aso-keyword-gap.yaml`. Chọn lọc:

| Ai · video · mốc | Nguyên văn (rút gọn) | Dùng cho |
|---|---|---|
| Steve · `beginners-guide-to-buying-selling-apps-2026` · 00:12:42 | "I don't care what any ASO tool says about the difficulty… if there's not a lot of people targeting that keyword in their title and the number two or three apps only have a 100 plus reviews, then I know I could probably beat them." | ngưỡng, bỏ tin điểm độ khó của tool |
| Steve · cùng video · 00:21:51 | "when you search for green noise, the the autofill result is green noise for better sleep. So, I was just like, let's just call the subtitle that." | dùng autofill đặt subtitle |
| Kyle · `how-i-make-42kmo-passively-with-simple-no-code-apps-copy-me` · 00:00:43 | "He spent two weeks researching keywords like baseball card scanner and find value for baseball cards." | thời gian nghiên cứu thật |
| Kyle · cùng video · 00:15:27 | "probably like 9 or 10K recurring revenue, but for a long time without any marketing for like a couple years" | kết quả (trích nguyên văn: nghe kể, không phải số xác minh) |
| John McEvoy · `2025-10-23_how-i-built-a-30k-month-mobile-app` · 00:04:57 | "location specific keywords, things like New York subway, Chicago train. Add those to the title and metadata" | từ khoá cụ thể ít cạnh tranh |
| John McEvoy · cùng video · 00:06:33 | "they don't have a huge popularity. So by targeting those keywords specifically… you can quite easily get into … the top five for a keyword." | kết quả |
| Max · `2025-12-11_i-make-10k-month-from-28-apps` · 00:03:10 | "my main source of ideas is a well-known ASO tool Astro." | công cụ |
| Sebastian · `2025-06-21_how-i-built-it-15k-month-mobile-app` · 00:07:12 | "I only spent $100 per month on it." (Apple Search Ads) | chi phí tối thiểu để tăng tốc |

## Bẫy và phản ví dụ
- **Trống trơn chưa chắc là cơ hội.** Top 3 chỉ 0–1 review có thể nghĩa là chưa ai kiếm được tiền (Hairmint; xem `VALIDATE.md` 1.3). Phải qua bước 5.
- **ASO có trần.** Steve: "you can do that with ASO. To get to like a seven figure it's a little bit harder." Với mục tiêu $1k MRR thì trần không phải vấn đề, nhưng đừng kỳ vọng cho cả hành trình.
- **ASO chậm.** John McEvoy: "it's really just about research and patience."
- **Nhiễu đo lường.** Người xem TikTok rồi tự tìm app trên App Store bị tính thành tải "organic/ASO" (video `172m-of-app-building-advice-in-50-minutes` · 00:22:04). Đừng gán toàn bộ lượt tải cho từ khoá khi sau này có chạy kênh video.
- **Công cụ này chỉ xấp xỉ.** `kw.py` dùng iTunes Search API, thứ hạng có thể khác ô tìm kiếm thật; `autofill.py` cho thứ tự gợi ý, không cho lượng tìm kiếm. Doanh thu Sensor Tower lệch rất xa.
- **Chưa phải bằng chứng khách của mình.** Mức tối đa công thức này đưa tới là mức 3 (có app tương tự đang bán được).

## Quyết định
- **QUA** nếu có ≥1 cụm đạt cổng 1.3 và 1.1 của `VALIDATE.md`, kèm doanh thu đối thủ có nguồn. Việc tiếp theo là `s3-competitor-reviews` cho các đối thủ đó.
- **DỪNG** nếu mọi cụm: top 3 đều rất nhiều rating và app cũ vững, hoặc autofill không có cụm của mình, hoặc top 3 trống mà không đối thủ nào có doanh thu.
- **TEST THÊM** nếu cụm qua số liệu nhưng doanh thu đối thủ chưa kiểm được: đến ngày +7 (kể từ lần chạy) hoàn tất bước 5 bằng TrustMRR/Sensor Tower; nếu vẫn không có số thì đặt trang pre-order (`s7`) và xem ≥1 người trả tiền.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ các bước chạy bằng công cụ, từ xa, không cần là người trong ngách và không bị khoá vùng; hợp với lựa chọn organic. Đây là lý do công thức được giữ dù bằng chứng founder mỏng.
- **Rào cản thật:** chỉ 1 case founder trong kho, phần lớn còn lại là lời expert (nhãn ở đầu). Từ khoá trống trơn có thể nghĩa là chưa ai kiếm được tiền ở đó (xem `VALIDATE.md` cổng 1.3). Cần US/GB/CA/AU làm store chính để số volume có nghĩa.
- **KHÔNG nên làm** khi từ khoá có đối thủ top 3 đã có hàng nghìn review (không còn khe), hoặc khi sản phẩm cần giải thích dài mới hiểu (không ai gõ cụm từ đó).
