---
id: s7-preorder-buy-button
strategy: S7
title: "Thu tiền khi sản phẩm chưa tồn tại: trang bán có nút mua, pre-sale, hoặc bán dịch vụ làm tay trước"
label: manual                  # dựng trang và nhận tiền là việc của người; agent chỉ giúp soạn chữ và đếm đơn
time: "2–4 giờ dựng trang hoặc đề nghị; 3–14 ngày chờ đơn"
cost: "$0–100 (tên miền, công cụ thanh toán)"
evidence: corpus
signal_level_when_pass: 8      # QUA khi có người lạ trả tiền thật lúc sản phẩm chưa có hoặc còn thô (mức 8)
tools: []
status: draft
---

## Dùng khi
Mình đã có một nỗi đau gọi được tên và ít nhất một cách tiếp cận được người đúng nhóm (email list, người đã comment, một cộng đồng). Đây là công thức nhắm thẳng vào mức 8: có người trả tiền khi sản phẩm còn chưa xong. Chưa có ai để đưa trang tới thì quay lại `s8-content-demand-test`; chỉ muốn nghe khách nói thì `s10-customer-interviews`. Cổng 3 của `VALIDATE.md` yêu cầu mức tín hiệu trước khi viết code, và công thức này là cách rõ nhất để đạt. Host Pat Walls nói thu tiền trước khi viết code là hướng đi cho solo founder (lời khuyên, câu ở bảng bằng chứng).

## Đầu vào
Một ý tưởng một câu, một nhóm người nhận được tin (email list, bài đăng, DM), và cách nhận tiền hợp lệ cho người bán từ VN (xem mục Cho solo founder bên dưới).

## Các bước
Ba hình thức đều có trong kho; chọn một.
1. **[manual] Hình thức A, trang bán một câu cộng nút mua.** Setter AI dựng landing page với demo AI giả và nhận $500 qua Stripe khi chưa có sản phẩm (Joseph và Timo nói cách validate duy nhất là khi người mua quẹt thẻ). Runafy dựng landing hai câu có nút Stripe bán gói early adopter 5 USD khi app chưa tồn tại; hơn 90 người trả (trong khoảng 2.000 người trong waitlist); host Joseph Choi nói $5 trên trang hai câu vẫn là tín hiệu mạnh. Sanskar (kho gắn vào case MagicSlides) dặn: đặt nút mua kèm ngày giao 10–30 ngày, có đơn đầu tiên mới bắt đầu build; anh nói chính mình làm vậy ở các sản phẩm về sau, nên chưa chắc đã áp cho MagicSlides. Việc cụ thể ≤15 phút: viết tiêu đề + 3 dòng lợi ích + giá + ngày giao + nút mua.
2. **[manual] Hình thức B, pre-sale giới hạn số suất.** Subscribr (Gil) mở 50 suất lifetime giá rẻ: 10 suất đầu rẻ nhất, mỗi 10 suất sau giá tăng; trước đó là chuỗi 7 email mỗi ngày nêu lợi ích và báo ngày mở bán. Hết sạch trong 2–3 ngày, founder nói khoảng $20k (Gil nói cách duy nhất để có validation là thu tiền của người ta, và đừng yêu ý tưởng khi chưa pre-sale); cam kết giao bản đầu trong 60 ngày và hoàn tiền bất kỳ lúc nào trước khi giao.
3. **[manual] Hình thức C, dịch vụ làm tay bán trước** (không viết sản phẩm). Sway AI mời follower DM rồi thu khoảng $15 cho một lần review hồ sơ hẹn hò làm tay, trước khi có app. Sheets Resume (Colin McIntosh dặn validate bằng cách làm cho người ta theo kiểu không scale) làm review CV bằng tay, giá bắt đầu vài trăm đô và tăng lên 300 rồi 400 vì nhu cầu vượt thời gian. BulkMockup làm 1.800 mockup bằng script trong khoảng 30 phút cho một khách freelance trả $300. Make Logo AI thu thông tin và tiền qua một form, chưa có backend, làm tay (Nico: không tự động hoá, không scale được, nhưng có đơn đầu tiên).
4. **[manual] Chọn điều kiện hoàn tiền trước và ghi rõ trên trang.** Kho có ba kiểu: Setter AI đặt cọc hoàn lại 100% trước khi có sản phẩm; Subscribr hoàn tiền bất kỳ lúc nào trước khi giao; Floga bán lifetime khi app còn dở và nói rõ không hoàn tiền (Umberto: người mua lifetime là người cam kết, người trả theo tháng có đường lui). Đây là chọn lựa pháp lý và uy tín; công thức không khuyên kiểu nào.
5. **[manual] Gửi tới đúng người trong 3–5 ngày (số ngày là đề xuất, chưa có số của kho), rồi đếm đơn.** Subscribr dựng email list hơn 1.000 người trước (qua X và giveaway); Floga làm nóng khách cũ vài tuần rồi quay video demo các tính năng đang có; Sway AI dùng Instagram video mẹo hồ sơ kèm link pre-order. Đếm: bao nhiêu người lạ (không phải bạn bè, người quen) trả tiền.
6. **[manual] Giao đúng điều đã hứa, bằng tay nếu chưa có sản phẩm.** Subscribr chỉ có 60 ngày; chuyên gia John Rush mô tả cách giao giải pháp bằng tay, lặp lại cho tới khi khách hài lòng rồi mới build (step không gắn case, không phải việc của một case đo được).

## Đầu ra
Mỗi ý tưởng một dòng: hình thức (A/B/C) · giá · số người lạ đã trả · số người xem trang (nếu biết) · điều kiện hoàn tiền · mức tín hiệu 0–8 (8 khi có người lạ trả) · quyết định.

## Ngưỡng qua
Tỉ lệ người đăng ký trả tiền và mốc tham khảo nằm ở cổng 3 và mức 8 của `VALIDATE.md`, không chép lại. Điều kiện riêng của công thức này: QUA khi có người lạ trả tiền thật (không phải bạn bè, người quen). Số đơn tối thiểu: kho chỉ có một step host nói 5 đơn pre-sale thì mới build (đề xuất, chưa có số của founder trong kho).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 14 step trong 13 video |
| Case (video, case) có step này | 12, trong đó 11 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 1/14 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 5/11 |
| Case full không nêu existing_audience | 8/11 |
| Case full video không kể bằng chứng nhu cầu trước launch | 2/11 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.0 tháng (6.0–18.0), n=5 |
| Kênh scale trả tiền / thuần organic / không nêu | 5 / 6 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s7-preorder-buy-button.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Số nhỏ: 11 case full. Theo trường nhu cầu của kho, 7 có `paid`, 1 `similar_product_revenue` (MagicSlides), 3 không nêu (Floga, Sheets Resume, Make Logo AI; video có kể pre-sale hay thu tiền trước trong step nhưng trường nhu cầu để trống, nên số 'paid' có thể thấp hơn thực tế). Trong 9 case `paid` của toàn kho, 7 có step s7. Dịch vụ làm tay: 5 step ở 4 case có tactic_note nhắc dịch vụ làm tay (Sway AI, Sheets Resume, BulkMockup, Make Logo AI) và 1 step host (John Rush). 1/14 step chỉ do host/expert. Số tháng tới mức doanh thu hiện tại ở trên có n=5, không dùng để kết luận tốc độ. Xem chương VALIDATE mục Tín hiệu nhu cầu để biết 9 case `paid` thật sự là gì và khi nào tiền đến.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể hoặc lời họ khuyên.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Joseph hoặc Timo (founder) · `2025-09-27_how-we-built-a-10k-mo-saas` · 04:07 | "I think the only way to validate is when buyers swipe their credit card." | founder nói (Setter AI): cách validate duy nhất là khi người mua quẹt thẻ; khoản $500 đến khi chưa có sản phẩm |
| Pat Walls (host/expert) · `2025-09-27_how-we-built-a-10k-mo-saas` · 06:26 | "Collecting cash before writing code is definitely the way to go, especially if you want to ship a successful app as a solo founder." | lời khuyên của host: thu tiền trước khi viết code, nhất là với solo founder |
| Gil (founder) · `2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-br` · 08:27 | "So, the only way to really get validation is to collect money from people." | founder nói (Subscribr): cách duy nhất để có validation là thu tiền của người ta |
| Gil (founder) · `2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-br` · 14:24 | "the first thing is you cannot fall in love with your idea without validating it by doing some sort of pre-sale, validating that people are willing to pay for it." | founder khuyên: đừng yêu ý tưởng khi chưa validate bằng một dạng pre-sale |
| Gil (founder) · `2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-br` · 08:57 | "step one is you have to build an audience because if you don't have an audience, you don't have anyone to sell to." | bẫy: pre-sale cần audience trước (Gil dựng email list hơn 1.000 người rồi mới bán) |
| Joseph Choi (host/expert) · `2026-03-09_i-speedran-an-ai-app-from-0-to-100k-exit-in-26-d` · 00:36:15 | "Yeah, if someone pays $5 for a landing page that has like two sentences on it, like, they're probably like very interested and they're and pretty bought in. Even if it's only $5, like that's a very strong signal." | lời của host về Runafy: $5 trên trang hai câu vẫn là tín hiệu mạnh |
| Sanskar (founder) · `2026-11-08_sanskar-30-micro-apps` · 13:55 | "put more buy buttons on the internet. If you don't have an option for people to pay you're not even letting the God make the magic happen." | founder khuyên: đặt nhiều nút mua hơn trên mạng, không có chỗ để trả tiền thì không có câu trả lời |
| Sanskar (founder) · `2026-11-08_sanskar-30-micro-apps` · 14:29 | "would have told myself, Sanskar, stop trying to add more features. Put the buy button." | founder tự dặn mình: thôi thêm tính năng, đặt nút mua |
| Daniel (founder) · `2026-05-05_i-speedran-a-new-app-from-0-to-2myear-in-6-month` · 00:05:51 | "People were actually paying us before we built the app to get feedback on their profile" | founder kể (Sway AI): người ta trả tiền cho review hồ sơ làm tay trước khi app tồn tại |
| John Rush (founder) · `2025-05-31_i-make-250k-month-from-20-apps` · 04:13 | "I don't even build a product. I actually deliver the solution manually." | chuyên gia mô tả cách làm của mình (step không gắn case): không build, giao giải pháp bằng tay |
| Colin McIntosh (founder) · `2025-01-22_how-i-built-it-20k-month-ai-app-as-a-non-technic` · 07:09 | "first validate the idea by doing it for people in a way that either isn't for sale or doesn't scale" | founder khuyên (Sheets Resume): validate bằng cách làm cho người ta theo kiểu không scale |
| Nico (founder) · `2025-03-31_i-locked-myself-in-a-room-made-17-apps-sold-2-fo` · 07:21 | "it was not automated it's definitely not scalable but I was able to get something going" | founder kể (Make Logo AI): chưa tự động hoá, làm tay qua form nhưng có đơn |
| Umberto (founder) · `2026-03-29_my-app-made-120k-in-24-hours` · 16:13 | "Monthly subscribers have optionality, okay? Lifetime buyer has commitment. And this change everything." | founder nói (Floga): người mua lifetime là người cam kết, người trả theo tháng thì có đường lui |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Số 'paid' chưa chắc là 'trước khi build'.** Wrestle AI có pre-order '8K tuần đầu' nhưng kho ghi đơn vị không rõ (lượt hay tiền), nên không dùng làm bằng chứng. Audio Pen thu tiền khi beta mở ngay trong buổi build 12 giờ, không phải nút pre-order. Xem chương.
- **Pre-sale cần có người để bán.** Gil: không có audience thì không có ai để bán (bảng trên); Subscribr dựng email list hơn 1.000 người trước pre-sale. Setter AI có sẵn một tên miền cũ đã được Google index. Với solo không audience, phần 'đưa trang tới người' là bước kẹt, không phải bước dựng trang.
- **Tiền sớm là cam kết giao hàng.** Subscribr có 60 ngày để giao và cam kết hoàn tiền; founder tự nói nếu làm không đúng thì tiền sẽ mất. Floga bán lifetime không hoàn tiền: người mua được nhiều tính năng sau này nhưng founder chịu rủi ro uy tín.
- **Một khách không phải thị trường.** Setter AI nhận $500 từ một khách B2B; BulkMockup $300 từ một khách freelance. Đây là mức 8 theo chữ của thang nhưng chỉ 1 người; `VALIDATE.md` cổng 1.5 dặn tính cỡ ngách riêng.
- **Giá thấp có thể chỉ chứng minh sự tò mò.** Runafy: $5, 90+ người, nhưng doanh thu hiện tại trong kho là khoảng $3.000 MRR; chưa đủ để kết luận gì về giá cuối.
- **Kho chỉ chứa người thắng.** 11 founder full dùng s7 và lên được kênh. Người mở trang bán và không ai trả tiền (hoặc trả rồi hoàn lại) không có mặt; vì thế 7/11 'paid' là mẫu của người thắng, không phải tỉ lệ.
- **Phần lớn là việc founder** (13/14 step có case); chỉ 1 step là mô tả của host.

## Quyết định
- **QUA** nếu có người lạ trả tiền thật cho thứ chưa có hoặc còn thô (mức 8) và mình giao được điều đã hứa trong thời hạn đã nói. Sang `VALIDATE.md` cổng 4 (build).
- **DỪNG** nếu đã đưa trang tới đúng nhóm người (đủ số xem để biết) mà không ai trả tiền, và đã thử đổi giá hoặc lời mời một lần.
- **TEST THÊM** nếu chỉ có đơn từ người quen hoặc một khách duy nhất: trong 7 ngày (đề xuất, chưa có số của kho) đưa trang tới 30 người lạ đúng nhóm (số này cũng là đề xuất) hoặc chạy `s10-customer-interviews` với người đã trả để hiểu vì sao.

## Cho solo founder bán global (từ VN)
- **Chép được:** hình thức A (trang + nút mua) và hình thức C (dịch vụ làm tay). Cả hai làm từ xa, vốn gần như không. Sway AI nhận tiền sau khi chat DM; Sheets Resume dựa vào kinh nghiệm cá nhân.
- **Rào cản thật:** (a) **thanh toán và pháp nhân**: `VALIDATE.md` mục rào cản VN nói Stripe thường không mở cho pháp nhân VN; kho ghi các case dùng Stripe (Setter AI, Runafy), nên cần merchant-of-record hoặc cách khác và kiểm điều kiện người bán từ VN trước khi hứa nhận tiền. (b) Không audience: pre-sale là bước khó nhất. (c) Người đứng ngoài ngách: trong 11 case full, 1 tự ghi không phải người trong cuộc, 3 không nêu, 7 là người trong cuộc (nhóm 'không phải' và 'không nêu' không gộp); bằng chứng cho người ngoài còn rất ít.
- **KHÔNG nên làm** nếu không có cách nhận tiền hợp lệ từ khách US (lúc đó 'trả tiền' chỉ còn là đăng ký email); nếu ngành có luật bán trước (y tế, tài chính); hoặc nếu mình không giao được điều đã hứa trong thời hạn đã nói.
