---
id: s8-content-demand-test
strategy: S8
title: "Đăng nội dung hoặc dựng một trang về ý tưởng trước khi build xong, để đo nhu cầu"
label: chrome                  # soạn bài và đăng bằng tay; đọc comment/DM bằng Chrome hoặc tay; chưa có bước nào máy làm hết
time: "1–2 giờ để dựng; 14 ngày để đăng và đọc phản hồi"
cost: "$0 nếu không chạy quảng cáo"
evidence: corpus
signal_level_when_pass: 5      # QUA chỉ khi có comment/DM hỏi mua (mức 5); view hoặc waitlist miễn phí không đủ (mức 2 và 4)
tools: []
status: draft
---

## Dùng khi
Mình đã có một ý tưởng gọi tên được nỗi đau và muốn biết người ta có phản ứng bằng hành động hay không, trước khi build xong. Muốn thu tiền ngay thì chọn `s7-preorder-buy-button`; muốn nghe giọng khách thì chọn `s10-customer-interviews`. Công thức này cho tín hiệu *rẻ và rộng*, không cho tín hiệu *sâu*. Host Joseph Choi (về Beam) và Pat Walls (về Coherence) mô tả đây là cách validate trước khi build, với nội dung đi trước code.

## Đầu vào
Một ý tưởng một câu (ai, đau gì, giải bằng gì) và ít nhất một kênh đăng được mà không phụ thuộc vùng (X, LinkedIn, Reddit, Instagram Reels; TikTok bị lệch vùng từ VN, xem cuối `VALIDATE.md`).

## Các bước
1. **[manual] Viết nỗi đau thành một câu người lạ hiểu trong vài giây.** Pushscroll, Runafy và Bro đều đăng thứ *chưa tồn tại* dưới dạng video 'cái này sẽ làm được gì'. Setter AI viết nỗi đau vào tiêu đề H1 của landing page.
2. **[manual] Chọn một dạng đo, không chọn cả ba.**
   - *Nội dung theo kênh* (video, tweet, bài LinkedIn): Pushscroll quay video demo bằng footage giả; Runafy chép định dạng reels của LiftOff và đăng khoảng 50 video trong 2 tuần; Stronger dựng video bằng Canva khi app chưa xong; Beam (nhắc qua, depth mention) đăng TikTok về ý tưởng trước khi có app và đếm waitlist; Cleo đăng nhiều bài LinkedIn giáo dục về vấn đề, cuối bài mới dẫn vào waitlist; Coherence dùng X làm chiến trường ý tưởng, bài nào hút tương tác mới biến thành video và mới build app; Glow Up làm nội dung trước vì các app trước build mãi đều thất bại.
   - *Trang một câu hoặc landing page*: Setter AI dựng landing page với demo AI giả trên tên miền cũ đã được Google index; Canary mở một page nội dung riêng không gắn tên mình để đo nhu cầu chủ đề trước khi làm app.
   - *Bài hỏi thẳng cộng đồng*: Cardstock đăng lên subreddit về thẻ bóng chày; Kaching Bundles đăng ảnh thiết kế (chưa có app) vào nhóm Facebook, Discord của dân drop shipping.
3. **[chrome] Đăng và mở sẵn một bảng đếm** (3 cột: view, comment hỏi mua hoặc DM, đăng ký). Việc cụ thể ≤15 phút/lần: đọc toàn bộ comment, gạch ra những câu hỏi giá, hỏi 'ở đâu', xin bản dùng thử. CodeGuide kể kết quả theo kiểu đó: 400 retweet và khoảng 300 đăng ký, anh mới coi là tín hiệu.
4. **[manual] Làm nóng trong khoảng 14 ngày rồi dừng để đọc** (CJ Zafir: đẩy nội dung 14 ngày để làm nóng audience và chọn nỗi đau cốt lõi từ phản hồi; số ngày này là việc một founder làm, không phải mốc của kho). Nếu comment lặp lại cùng một câu xin ('I need this' ở Curiosity Quench) thì đăng thêm video cùng chủ đề trước khi kết luận.
5. **[manual] Gắn đuôi một hành động tốn công hơn xem.** Waitlist miễn phí, form email, nút 'xin bản dùng thử'; Jack Friks dặn đo bằng việc người ta có bấm mua hay không (lời khuyên, không phải việc đã đo). Đừng dừng ở view: Massive thu 40 đến 50 nghìn đăng ký waitlist miễn phí mà không ai trả tiền; Bro có một video mockup 7,9 triệu view (xem Thực tế bên dưới).
6. **[manual] Ghi mức tín hiệu** theo thang 0–8 của `VALIDATE.md` và quyết định ở mục Quyết định.

## Đầu ra
Mỗi ý tưởng một dòng: nội dung/trang đã đăng (link) · số view · số người xin hoặc hỏi mua (trích câu) · số đăng ký miễn phí · mức tín hiệu 0–8 · việc làm tiếp (`s7` thu tiền, `s10` gọi những người đã comment).

## Ngưỡng qua
Mốc view, tỉ lệ giữ chân và số bài nằm ở cổng 3 của `VALIDATE.md`, không chép lại. Điều kiện riêng của công thức này: QUA chỉ khi có người hỏi mua hoặc xin sản phẩm bằng chữ của họ (mức 5 trở lên); view (mức 2) và waitlist miễn phí (mức 4) chỉ cho phép TEST THÊM.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 41 step trong 36 video |
| Case (video, case) có step này | 28, trong đó 26 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 8/41 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 13/26 |
| Case full không nêu existing_audience | 19/26 |
| Case full video không kể bằng chứng nhu cầu trước launch | 2/26 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 10.5 tháng (4.5–24.0), n=14 |
| Kênh scale trả tiền / thuần organic / không nêu | 10 / 16 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s8-content-demand-test.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Trong 26 case full có s8, theo trường nhu cầu của kho: waitlist miễn phí hoặc tự kể nỗi đau 10, view nội dung 7, trả tiền 4, comment hỏi mua 2, không nêu 3. Tức là chỉ 6/26 đạt mức 5 trở lên, và 4 trong 6 là case có thêm bước thu tiền (Setter AI, Audio Pen, Sway AI, Runafy; xem `s7-preorder-buy-button`). Phần còn lại dừng ở view hoặc waitlist miễn phí. 8/41 step chỉ do host/expert mô tả (landing page bằng Lovable, newsletter trước khi có app, waitlist 100 đăng ký rồi mới gửi email chào pre-sale), nên khoảng một phần năm công thức là lời khuyên, không phải việc founder đã làm. Số tháng tới mức doanh thu hiện tại ở trên có n=14, không dùng để kết luận tốc độ.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Joseph hoặc Timo (founder) · `2025-09-27_how-we-built-a-10k-mo-saas` · 01:47 | "So, as soon as I had the idea, I set up a landing page." | founder kể (Setter AI): dựng landing page ngay khi có ý tưởng, trước khi có sản phẩm |
| CJ Zafir (founder) · `2025-05-21_from-zero-to-42k-month-in-90-days-with-ai` · 10:29 | "I would literally go push content for next 14 days, warm up my audience and then from there I pick up what are their main core pain points" | founder kể cách làm lại (CodeGuide): đẩy nội dung 14 ngày để làm nóng audience rồi chọn nỗi đau cốt lõi từ phản hồi |
| CJ Zafir (founder) · `2025-05-21_from-zero-to-42k-month-in-90-days-with-ai` · 07:21 | "we got like 400 retweets and I got like 300 signups, that was a different feeling for me and I knew like okay I am up to something." | founder kể kết quả (CodeGuide): tweet có demo đạt khoảng 400 retweet và 300 đăng ký, anh coi là tín hiệu để đi tiếp |
| Jack hoặc Nick Sweeney (founder) · `2025-11-20_our-mobile-app-made-85k-in-8-months` · 04:14 | "Once we saw what went viral, then we built the app." | founder kể (Coherence): thấy nội dung nào lan rồi mới build app |
| Ben (founder) · `2026-11-04_canary-language-songs` · 03:16 | "Okay, this is like a social proof that people want this kind of content and want to learn with songs." | founder kể (Canary): dựng page nội dung riêng, coi đó là bằng chứng xã hội cho nhu cầu học bằng bài hát |
| Ben (founder) · `2026-11-04_canary-language-songs` · 04:06 | "Like having an audience can help, but you can also like create an audience from scratch in order to like see if your idea is good and it can go like really viral pretty fast." | founder nói: không có audience vẫn tạo được audience từ đầu để thử ý tưởng (Canary) |
| Louis (founder) · `2025-12-17_my-mobile-app-made-800k-in-365-days` · 03:38 | "So we did content first [music] because for most of my other apps before we were just building and building without showing to user what we had and it always failed." | founder kể (Glow Up): làm nội dung trước vì các app trước build mãi mà không cho người dùng xem và đều thất bại |
| Lara Acosta (founder) · `2026-01-11_how-my-app-hit-60k-month-in-2-months` · 04:27 | "Everybody's doing it the opposite way, where they launch something and they promote it. We did it the opposite way, which was the most important part for us." | founder kể (Cleo): đi ngược cách thường làm: đăng nội dung trước rồi mới ra mắt |
| Dan (founder) · `2025-08-03_this-app-makes-2myear-using-this-ridiculously-ea` · 00:06:22 | "If I could do it all over again, I wouldn't do weight list at all." | bẫy (Massive): waitlist miễn phí 40–50 nghìn người nhưng không ai trả tiền; Dan nói nếu làm lại sẽ không làm waitlist (transcript ghi 'weight list', nghĩa là waitlist) |
| Jack Friks (founder) · `2026-08-02_how-i-work-40k-month-solo-app-builder` · 06:18 | "If they don't click buy and a thousand people come, clearly the idea is probably not that good" | lời khuyên của founder (không phải việc đã làm): đo bằng việc người ta có bấm mua hay không, không bằng số người ghé |
| Joseph Choi (host/expert) · `2026-11-14_100-profitable-apps` · 00:01:24 | "But Lily showed that you can go even earlier than that. You can make content about the idea and see whether people want it before you've even finished building anything." | lời khuyên của host: có thể đi sớm hơn cả build, làm nội dung về ý tưởng rồi xem người ta có muốn không (kể về Beam) |
| Pat Walls (host/expert) · `2025-11-20_our-mobile-app-made-85k-in-8-months` · 06:34 | "Well, this video isn't about the coding, it's about the content. It's about validating before you build." | lời của host: đây là cách validate trước khi build, trọng tâm là nội dung chứ không phải code |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **View không phải tiền.** Massive (bảng trên): 40 đến 50 nghìn đăng ký waitlist miễn phí, không ai trả; Dan nói nếu làm lại sẽ không làm waitlist. `VALIDATE.md` nguyên tắc 2 nêu cùng loại số (Flame, Massive); trong kho không tìm thấy số riêng của Flame.
- **Nội dung nổ vì chủ đề, không vì sản phẩm.** Bro có video mockup 7,9 triệu view trước khi có app, đăng trên tài khoản thương hiệu và có mua quảng cáo cho video đầu để lấy phản hồi; case này không có số doanh thu trong kho. Dùng mức 2 để quyết định build là đi ngược `VALIDATE.md` cổng 3.
- **Có audience thì tín hiệu bị thổi.** 7 trong 26 case full kể có audience sẵn (bảng stats: 19/26 không nêu). CJ Zafir tự nói anh dùng audience công cụ lập trình AI đã có; Audio Pen dựa vào cộng đồng build-in-public đã xây trước đó. Với solo không audience, số của họ không cùng thang.
- **Nhiều case ghi mơ hồ.** Zoom University (nhắc qua, depth mention) có waitlist khoảng 40.000 nhưng video không nói lúc đó đã có app chưa; Nomad Table không nói có thu phí hay không. Đừng đếm hai ví dụ này là bằng chứng mức 4 sạch.
- **Kho chỉ chứa người thắng.** 26 founder full dùng s8 và lên được kênh. Người đăng nội dung không ai phản ứng, bỏ ý tưởng, không có mặt; vì vậy 6/26 đạt mức 5 là con số của người thắng, không phải xác suất.
- **Phần lớn là việc founder, nhưng có một phần năm là lời host** (8/41 step không gắn case): các bước dựng landing page bằng công cụ AI, newsletter trước khi có app là mô tả của host, không phải việc case nào trong kho đã làm.

## Quyết định
- **QUA** nếu có người hỏi mua hoặc xin sản phẩm bằng chữ của họ (mức 5 trở lên) trong lượt đăng, và họ không phải người quen. Sang `s7-preorder-buy-button` để lên mức 8, hoặc `VALIDATE.md` cổng 4.
- **DỪNG** nếu sau cả lượt đăng chỉ có người xem mà không ai hỏi giá hoặc xin bản, và đã thử đổi một lần cách nêu nỗi đau.
- **TEST THÊM** nếu có view hoặc waitlist nhưng chưa có câu hỏi mua: đăng thêm 14 ngày (số ngày đề xuất, chưa có số của kho) kèm một lời mời hành động cụ thể, hoặc chuyển ngay sang `s10-customer-interviews` với những người đã comment.

## Cho solo founder bán global (từ VN)
- **Chép được:** bảng đếm ba cột và bước 5. Làm từ xa, không tốn vốn. X, LinkedIn, Reddit, Reels ít bị khoá vùng hơn TikTok (xem mục rào cản trong `VALIDATE.md`).
- **Rào cản thật:** (a) không audience: đăng nhiều bài mà không ai thấy là kết quả mặc định; trong 26 case full, 18 là người trong cuộc ở ngách và 7 kể có audience sẵn. (b) Nội dung cho thị trường US cần giọng tiếng Anh tự nhiên, nhất là video có người nói. (c) Người đứng ngoài ngách còn ít ví dụ: 2 case full tự ghi không phải người trong cuộc và 6 case không nêu, so với 18 case insider (đó là hai nhóm khác nhau, không gộp). Bằng chứng cho nhóm người ngoài còn mỏng.
- **KHÔNG nên làm** nếu ý tưởng cần giải thích dài mới hiểu (đó là dấu hiệu 'vitamin', cổng 1.2), hoặc nếu mình không đăng đều được ít nhất vài tuần mà không bỏ cuộc: một lượt đăng nhỏ không đo được gì.
