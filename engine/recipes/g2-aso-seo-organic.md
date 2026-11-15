---
id: g2-aso-seo-organic
strategy: G2
title: "Để người ta tìm thấy sản phẩm đang có: ASO cho app, SEO cho web"
label: manual                  # viết và chỉnh bằng tay; Search Console, Sensor Tower, Keyword Planner dùng qua Chrome
time: "3 giờ cho một lượt đặt nền (từ khoá, trang, metadata); sau đó 1 bài hoặc 1 trang mỗi ngày"
cost: "$0 (Sensor Tower, Ahrefs... tuỳ chọn, ngoài kho)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

## Dùng khi
Sản phẩm **đã có và chạy được**, đã qua `g1-first-10-users`, và mình muốn được tìm thấy mà không trả tiền. App trên App Store/Play: mục A (ASO). Web hoặc SaaS: mục B (SEO). Đây là kênh **chậm** (xem Thực tế); không dùng nếu cần người dùng trong tuần này. Chọn từ khoá để chọn ý tưởng không thuộc đây: xem `s2-aso-keyword-gap`.

## Đầu vào
Một sản phẩm đã dùng được, 10–20 cụm từ mà khách thật sự gõ (từ review, comment, hoặc gợi ý tự động), và quyền sửa tiêu đề/subtitle (app) hoặc trang/blog (web).

## Mục A. ASO cho app đã có (8 case full)
1. **[manual] Tìm từ khoá bằng gợi ý tự động:** gõ đầu từ trên App Store xem gợi ý, chọn từ ít người cạnh tranh để lên top 5 (Momego). Cardstock nghiên cứu bằng Sensor Tower, đặt các cụm như "baseball card scanner" vào tiêu đề, và theo step giữ vị trí số 1 cho từ khoá đó 2–3 năm.
2. **[manual] Đặt từ khoá vào tiêu đề, subtitle, trường keyword:** HabitKit đặt "habit tracker" ngay đầu tên app; Momego thêm từ khoá theo thành phố ở tiêu đề, subtitle, keyword, mỗi bản địa hoá có ảnh chụp riêng và tải tăng rõ rệt; app trong danh mục 28 app viết mô tả và metadata bằng AI nhưng bám theo từ khoá đã chọn từ đầu.
3. **[manual] Dùng đúng chữ của người dùng:** Rootd dùng từ khoá người dùng viết trong review để mô tả sản phẩm; Coconote ghi "great for ADHD" ở tiêu đề và ảnh store, nói lại điều người dùng đã viết trong review và khi được phỏng vấn.
4. **[manual] Trang store đẹp:** một habit tracker cao cấp (không nêu tên) nói ảnh trên store là creative hiện ra khi người ta tìm kiếm; làm bằng AI hoặc thuê designer.
5. **[manual] Xin đánh giá đúng lúc người dùng vui:** Momego xin rating khi người dùng vừa thấy xe chạy trên bản đồ; Wishlists hiện hộp đánh giá sau khi người dùng vừa thêm hoặc hoàn thành một điều ước; đánh giá đẩy thứ hạng.

## Mục B. SEO cho web, kể cả YouTube (26 case full)
1. **[chrome] Chọn từ khoá cuối phễu, ý định mua cao:** Late chọn từ khoá 300–800 lượt tìm mỗi tháng, cạnh tranh thấp, và viết hướng dẫn sâu cho từng từ khoá (theo step, mảng này cho khoảng 8k MRR). Shipper nhắm "alternatives to X" và "how much does X cost" (X là đối thủ). Elephas lọc độ khó dưới 20 và lượng tìm trên 500, lập 30–50 chủ đề, viết 2–3 bài mỗi tuần rồi lên 6–7 bài.
2. **[manual] Một trang cho một nhu cầu cụ thể:** Barn2 viết hướng dẫn khoá danh mục WooCommerce bằng mật khẩu, lên top Google ngay vì sản phẩm độc nhất; Stagetimer viết trang tài liệu cho một thiết bị (Stream Deck); Excel Exercises viết 1.500–2.000 chữ ngay trên landing page và giữ lại dù một "chuyên gia marketing" bảo sai; Super Demo viết trang so sánh từng đối thủ.
3. **[manual] Free tool làm phễu, mỗi tool một từ khoá:** SiteGPT dựng gần 50 free tool và thêm CTA dưới mỗi tool dẫn về sản phẩm chính; Signaturely dựng công cụ ký miễn phí rồi viết template hợp đồng xếp hạng cao.
4. **[chrome] Kiểm kỹ thuật:** Setter AI gửi yêu cầu index trong Search Console; Yadaphone phát hiện sitemap thiếu tiền tố www nên Google bỏ qua các trang cần xếp hạng, rồi sửa.
5. **[manual] CTA đặt ở chỗ người đọc kết thúc bài, rồi đo chuyển đổi:** Vault Air cho khoảng 10% lượt từ web chuyển sang tải app; mỗi sáng một script đọc Keyword Planner tìm từ khoá có impression mà không có click (hạng khoảng 50), tạo guide mới và nối internal link.
6. **[manual] YouTube theo từ khoá (nếu web chưa đủ):** FollowBuddy lập 10–20 từ khoá YouTube theo nỗi đau, kiểm lượt tìm mỗi tháng, xem video nào đang xếp hạng, làm bản ngắn hơn và nhiều giá trị hơn, tối ưu tiêu đề, mô tả, tag.
7. **[manual] Xin backlink khi có cơ hội thay thế:** Yadaphone nhắm "Skype alternative" khi đối thủ lớn rời đi, nhắn tác giả bài blog đang xếp hạng xin nhắc tới sản phẩm.
(SEO theo lập trình/programmatic có ở AngelMatch, Subscribr, Veed.io, Super Demo; đó là bước nâng cao, chưa đủ bằng chứng để thành bước riêng.)

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng mỗi từ khoá hoặc trang một dòng: thứ hạng hiện tại, lượt hiển thị, click (Search Console hoặc App Store Connect), số đăng ký hoặc lượt tải đến từ đó, số người trả tiền nếu đo được. Cập nhật mỗi tuần.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 30 ngày, có ít nhất một từ khoá hoặc trang lên top 10 và ít nhất một đăng ký hoặc lượt tải đo được từ tìm kiếm. Tham chiếu để hình dung (từ kho, không phải ngưỡng): Barn2 và Setter AI lên top rất nhanh với từ khoá hẹp; AngelMatch phải chờ 6–8 tháng mới thấy traffic tăng. Muốn xác nhận nhu cầu thì dùng `VALIDATE.md` (cổng 1–4, thang 0–8).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 59 step trong 40 video |
| Case (video, case) có step này | 38, trong đó 34 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 6/59 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 18/34 |
| Case full không nêu existing_audience | 29/34 |
| Case full video không kể bằng chứng nhu cầu trước launch | 15/34 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 30.0 tháng (13.0–54.0), n=19 |
| Kênh scale trả tiền / thuần organic / không nêu | 11 / 23 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g2-aso-seo-organic.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Mục con (câu truy vấn: `engine/recipes/g2-aso-seo-organic.extra.sql`): **ASO** có 12 step, 8 case full (4 case có số tháng, nên không rút trung vị); **SEO/web** có 47 step, 26 case full (15 case có số tháng: trung vị 30,0 tháng, p25–p75 21,0–48,0). Mục B chia theo kiểu (từ khoá trên mô tả step, đếm gần đúng, các kiểu chồng lấn): blog/hướng dẫn/nội dung dài ở 12 case full, YouTube hoặc video theo từ khoá ở 7, trang so sánh/alternative/ý định mua ở 6, free tool ở 4, SEO theo lập trình ở 4, xin backlink ở 2. Trong cả kho, 12 case full ghi SEO làm kênh người dùng đầu (11 trong số đó dùng g2) và 7 case full ghi tìm kiếm trong App Store (4 dùng g2). Theo `community_insider`: 22 case là người trong cuộc, 4 case ghi rõ **outsider**, 8 không nêu; đừng gộp 4 và 8. Chỉ 6/59 step là lời host/expert (không gắn case), phần lớn là việc founder đã làm; các step phân bố 52 ở chặng grow, 7 ở launch; 26 step từ video 2025, 33 từ video 2026. **Số tháng tới mức doanh thu hiện tại ở đầu bảng (30 tháng, so với 12 tháng của cả kho) không phải thời gian để SEO có kết quả:** nó đo thời gian tới mức doanh thu founder đang kể. 19 case trải từ 3 tháng (habit tracker) tới 120 tháng (Barn2 Plugins; Excel Exercises 66, Boot.dev 48), tức nhiều case là doanh nghiệp đã chạy nhiều năm và còn kể số hiện tại; trong khi Vault Air (6), Yadaphone (7) và Late (7) ngắn hơn nhiều.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các số kết quả trong mục Các bước lấy từ step của kho (tóm tắt lời founder).

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Denis Yurchak (Yadaphone) (founder) · `2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month` · 12:41 | "I would advise to do search engine optimization from day one and you have to be very patient with it." | founder khuyên: làm SEO từ ngày đầu và phải rất kiên nhẫn |
| Rashid (AngelMatch) (founder) · `2026-08-23_i-make-32k-month-from-3-simple-boring-websites` · 07:18 | "we grew through SEO" | founder kể: tăng trưởng nhờ SEO (theo step của kho: thuê 6 content writer, traffic chỉ tăng sau 6–8 tháng) |
| Katie Keith (Barn2 Plugins) (founder) · `2026-02-08_i-make-150k-month-from-20-tiny-apps` · 05:57 | "we got to the top of Google straight away, and we got our first sales within a few days" | founder kể: bài hướng dẫn cho một sản phẩm độc nhất lên top Google ngay, đơn đầu trong vài ngày |
| Banu (SiteGPT) (founder) · `2026-01-07_how-i-grew-my-app-to-13k-month-even-though-i-hate-ma` · 05:56 | "we get around 50,000 clicks from Google every month and almost 90% of it is because of these" | founder kể: khoảng 50.000 click Google mỗi tháng, gần 90% nhờ gần 50 free tool |
| Will Cannon (Signaturely) (founder) · `2025-10-01_my-two-apps-made-30m` · 09:48 | "that was how we got our first thousand plus customers" | founder kể: công cụ ký miễn phí làm phễu, rồi template hợp đồng xếp hạng, mang hơn 1.000 khách đầu |
| Mickey (Late) (founder) · `2026-03-04_zero-to-40k-month-with-one-marketing-channel-no-` · 03:57 | "There are people that are actively searching for social media scavening API or Twitter automation tool that they have a 10x higher intent to buy." | founder nói: người đang tìm đúng công cụ có ý định mua cao hơn nhiều (lý do chọn từ khoá cuối phễu) |
| Jake (Excel Exercises) (founder) · `2026-10-28_excel-exercises-boring-website` · 07:07 | "real growth came from SEO" | founder kể: tăng trưởng thật đến từ SEO dù cũng đăng Reddit vài lần |
| Pat Walls hoặc Gus (host/expert) · `2026-03-19_i-make-17k-month-with-one-strategy` · 06:12 | "I do tell people all the time, you can make a crappy video and it can rank number one." | lời khuyên của host (YouTube SEO): video dở vẫn có thể xếp hạng một |
| Rasty Turek (Vault Air) (founder) · `2026-10-18_app-2k-per-day` · 06:41 | "my approach was like what if I try to pull in every keyword that is out there" | founder kể: thử phủ mọi từ khoá liên quan trên web thay vì quảng cáo (trang marketing và loạt guide) |
| Kyle Fowler (Cardstock) (founder) · `2025-11-28_how-i-make-42kmo-passively-with-simple-no-code-a` · 00:13:46 | "We optimized for that pretty early." | founder kể (ASO): tối ưu từ khoá App Store từ sớm |
| John (Momego) (founder) · `2025-10-23_how-i-built-a-30k-month-mobile-app` · 04:57 | "location specific keywords, things like New York subway, Chicago train." | founder kể (ASO): từ khoá theo thành phố (New York subway, Chicago train) trong tiêu đề, subtitle, keyword |
| Sebastian (HabitKit) (founder) · `2025-06-21_how-i-built-it-15k-month-mobile-app` · 07:43 | "I'm focusing on the habit tracker keyword" | founder kể (ASO): đặt từ khoá habit tracker ngay đầu tên app |
| Max (28 app iOS) (founder) · `2025-12-11_i-make-10k-month-from-28-apps` · 10:14 | "when you just ship the app you get this famous app store boost" | bẫy (ASO): đợt tăng đầu sau khi ship app rồi giảm dần |
| Steve Young (host/expert) · `2026-07-19_beginners-guide-to-buying-selling-apps-2026` · 00:07:34 | "It's like my ASO strategy is to focus on keywords that nobody is going after not that ones that are everybody is going after." | lời khuyên của expert (ASO): nhắm từ khoá không ai nhắm; phần chọn từ khoá thuộc s2-aso-keyword-gap |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 34 case full dùng g2 đã thành công đủ để lên kênh. Người làm SEO nhiều tháng mà không có traffic không có trong kho; các câu "lên top Google ngay" (Barn2: sản phẩm độc nhất; Setter AI: website mới lên top 1 trong khoảng một tuần, video không kể vì sao) là điều founder chọn kể.
- **SEO chậm.** AngelMatch thuê 6 content writer và đợi 6–8 tháng mới thấy traffic tăng; Yadaphone khuyên làm từ ngày đầu và rất kiên nhẫn (câu ở bảng). Nếu cần tiền trong 1 tháng thì đây không phải kênh.
- **Đợt tăng đầu của ASO không bền.** App trong danh mục 28 app có đợt tăng sau khi ship rồi giảm dần (câu ở bảng). Cardstock giữ vị trí số 1 cho một từ khoá 2–3 năm là kết quả của một từ khoá hẹp, không phải quy luật.
- **Nhiều case kết hợp kênh.** Excel Exercises đăng Reddit vài lần nhưng nói tăng trưởng thật đến từ SEO; Blog to Pin viết nhiều bài, đăng Reddit, làm backlink và video không tách được kênh nào mang khách đầu. Đừng gán toàn bộ kết quả cho SEO.
- **Tìm kiếm AI (GEO) mới chỉ có lời host.** Một video host mô tả seeding bài và comment Reddit vào thread mà AI search trích dẫn; đó là step không gắn case founder, chưa có bằng chứng founder.
- **Chọn từ khoá để chọn ý tưởng khác công thức này.** Steve Young nói về ASO bằng cách tìm từ khoá không ai nhắm (câu ở bảng); phần "tìm từ khoá rồi build app" thuộc `s2-aso-keyword-gap`, chủ yếu là expert.

## Quyết định
- **QUA** nếu sau 30 ngày có ≥1 từ khoá hoặc trang lên top 10 và ≥1 đăng ký hoặc lượt tải đo được từ tìm kiếm (đề xuất, chưa có số của kho). Tiếp tục: 1 bài hoặc 1 trang mỗi ngày như Vault Air, hoặc thêm free tool (SiteGPT, Signaturely).
- **DỪNG** nếu không có từ khoá nào có người tìm đủ để đo (0 hiển thị sau 30 ngày dù đã được index): sản phẩm hoặc từ khoá sai, quay lại `s2-aso-keyword-gap` hoặc `VALIDATE.md`.
- **TEST THÊM** nếu đã lên top 10 mà không có đăng ký: sửa CTA và trang đích 14 ngày (đề xuất, chưa có số của kho), rồi đo lại. Nếu trang chưa được index, kiểm kỹ thuật (bước B4) trước.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ, làm từ xa, chi phí gần như bằng không nếu tự viết; không cần pháp nhân để có traffic. SEO là kênh solo dev hợp vì chữ viết một lần, lặp lại mãi.
- **Rào cản thật:** (1) tiếng Anh bản xứ cho blog và trang so sánh, nội dung dịch vụng sẽ khó xếp hạng; (2) kênh này chậm (AngelMatch 6–8 tháng) nên cần runway, chi phí sống thấp ở VN là lợi thế thật; (3) cạnh tranh với người đã có domain authority; từ khoá hẹp, độc nhất như Barn2 mới lên nhanh; (4) ASO cần app đã lên store (tài khoản nhà phát triển, thanh toán/thuế); web cần cổng thu tiền: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ; (5) ASO theo địa phương (Momego: từ khoá thành phố) chỉ hợp khi mình hiểu địa phương đó.
- **KHÔNG nên làm** khi sản phẩm không có từ khoá nào được tìm (sản phẩm tạo nhu cầu mới) hoặc khi cần doanh thu trong tháng đầu.
