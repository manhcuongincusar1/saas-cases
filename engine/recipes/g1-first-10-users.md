---
id: g1-first-10-users
strategy: G1
title: "Có 10 đến 100 người dùng đầu tiên: Reddit, nhóm Facebook, DM, audience hoặc đối tác có sẵn"
label: manual                  # tìm nơi bằng Chrome, đăng và nhắn bằng tay; agent chỉ giúp lập danh sách và ghi nhật ký
time: "2 giờ để dựng danh sách nơi và chuẩn bị tài khoản; 14 ngày đăng đều"
cost: "$0"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

## Dùng khi
Sản phẩm (hoặc bản MVP) đã chạy được và mình **chưa có người dùng nào**. Nếu đã có audience hay đối tác có sẵn khách, dùng Nhánh B ngay bên dưới. Đây là việc **trước** kênh dài hạn (`g2`, `g3`, `g6`) và trước ngày launch trên nền tảng (`g9`).

## Đầu vào
Một sản phẩm đã dùng được, một câu mô tả khách là ai, và 5–15 từ khoá/sở thích của nhóm khách đó.

## Các bước (Nhánh A: không có audience, đi tìm người ở nơi họ tụ tập)
1. **[manual] Viết 5–15 từ khoá, sở thích, nhân khẩu học của khách** (Avneesh, Savewise, làm đúng bước này trước khi đăng gì).
2. **[chrome] Lập bảng ≥15 nơi họ tụ tập.** Dùng "Map of Reddit": nhập một subreddit đã biết để ra các subreddit liên quan (Savewise, Elephas). Elephas coi subreddit trên 5.000 thành viên là đủ, nhỏ hơn đôi khi tốt hơn. AppAlchemy dùng công cụ tìm community của Reddit Ads mà **không** chạy quảng cáo. Mỗi dòng ghi: tên nơi, số thành viên, luật đăng có cho tự giới thiệu không.
3. **[manual] Làm nóng tài khoản, đọc luật.** GojiBerry: mỗi trình duyệt một tài khoản; 7–14 ngày đầu chỉ comment và upvote để có karma, sau đó mới đăng; trả lời mọi comment. AppAlchemy dùng Reddit hằng ngày vì bài từ tài khoản mới bị lọc. Savewise quan sát và comment trước, chưa đăng bài quảng bá.
4. **[manual] Đăng, mỗi lần một nơi.** Elephas: mỗi ngày một subreddit, chỉnh copy rồi lặp ở nơi khác trong 14–15 ngày. Stagetimer: mỗi subreddit một bài, không spam. Yadaphone: khi subreddit du lịch chặn, chuyển sang subreddit khởi nghiệp được tự giới thiệu. Savewise: vào thread hỏi đáp hằng tuần để đăng website và xin feedback; khoảng 3,5 tháng sau xin mod cho đăng bài chính, bài đó nổ. Postiz: đăng ở r/selfhosted kiểu build in public, nói "I" không nói "we", mỗi bản mới đăng lại.
5. **[manual] Ngoài Reddit, chọn một đường trực tiếp.** Nhóm Facebook đúng đối tượng (Savewise đăng một bảng tính ưu đãi có link về web; MagicSlides có đơn đầu từ một group). DM người vừa tương tác với một tweet viral (Jungle). DM lạnh theo hashtag (Once: 250–300 người, khoảng 15 trả lời, 12 sự kiện được đặt trong một tháng). Đây là các việc thủ công, không mở rộng được, và đúng ý là để học.
6. **[manual] Ghi nhật ký mỗi lượt:** nơi, ngày, nội dung, số phản hồi, số người thật sự dùng thử. Không có bảng này thì không biết kênh nào mang người.

## Nhánh B: khi đã có audience hoặc đối tác có sẵn khách
Trong 52 case full, 13 case nêu `existing_audience`; nhóm này không cần bước 2–4. Cách họ làm: email nuôi audience cũ (Floga, chuỗi email pre-launch khoảng một tháng một tuần), waitlist nuôi bằng email (Cleo), mở waitlist cho 100–150k follower Instagram trước khi launch (Brainrot), đổi equity lấy quyền tiếp cận khách của một đối tác (Launch Fast). Lưu ý: audience sẵn có không bảo đảm bền; Symmetry ra mắt nhờ kênh YouTube fitness của nhóm, tải tăng nhỏ rồi không bền.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "người dùng đầu theo kênh": mỗi kênh một dòng gồm số lượt đăng/DM, số phản hồi, số người dùng thử, số người trả tiền (nếu đã thu tiền). Đây là đầu vào của `g8-funnel-measurement` và của việc chọn kênh dài hạn.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 14 ngày đăng đều (Elephas lặp 14–15 ngày), có ≥10 người ngoài vòng bạn bè dùng thử, và ít nhất một kênh mang ≥3 người. Chỉ trỏ: nếu mục tiêu là xác nhận có người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8) chứ không dùng bảng này.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 73 step trong 57 video |
| Case (video, case) có step này | 54, trong đó 52 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 3/73 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 24/52 |
| Case full không nêu existing_audience | 39/52 |
| Case full video không kể bằng chứng nhu cầu trước launch | 19/52 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.0 tháng (4.0–30.0), n=36 |
| Kênh scale trả tiền / thuần organic / không nêu | 11 / 35 / 6 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g1-first-10-users.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Mục con (câu truy vấn: `engine/recipes/g1-first-10-users.extra.sql`; các nhóm chồng lấn nhau): trong 52 case full, step nhắc Reddit ở 22 case (cả kho có 26 case full ghi Reddit là kênh người dùng đầu); audience/waitlist/email/đối tác có sẵn ở 18; DM, cold, gõ cửa, gặp trực tiếp ở 12; bạn bè, người quen, beta nhỏ ở 12; step nhắc bị chặn, bị khoá hoặc bị giận ở 5. Trong 22 case có Reddit làm kênh đầu, 20 case không nêu `existing_audience` ("không nêu", không phải "không có"). Theo `community_insider`: 39 case là người trong cuộc, 5 case ghi rõ **outsider** (không phải người trong cuộc), 8 case không nêu; đừng gộp 5 và 8. Chỉ 3/73 step là lời của host; công thức này dựa chủ yếu vào việc founder đã làm. Các step phân bố 61 ở chặng launch, 9 ở grow, 3 ở validate; 29 step từ video 2025, 44 từ video 2026.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Roman (GojiBerry) (founder) · `2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas` · 02:22 | "One of our main ways to get users or at least at the beginning was Reddit." | founder kể: Reddit là một trong các cách chính lấy người dùng lúc đầu |
| Denis Yurchak (Yadaphone) (founder) · `2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month` · 07:46 | "In the first week, I got 150 users" | founder kể: chuyển sang subreddit khởi nghiệp được tự giới thiệu, tuần đầu có 150 người dùng |
| Denis Yurchak (Yadaphone) (founder) · `2025-10-16_i-rebuilt-a-1b-app-and-now-make-14k-month` · 07:15 | "I got blocked there really fast and it was quite demotivating." | bẫy: subreddit du lịch chặn bài rất nhanh; kênh Reddit có thể mất ngay |
| Ayush (Elephas) (founder) · `2026-01-21_how-i-built-a-13k-month-saas` · 03:50 | "we posted a lot on niche subreddits asking for feedback, showcasing the product, giving demos, which led to initial initial revenue customers." | founder kể: đăng nhiều bài ở subreddit ngách xin feedback và demo, ra khách trả tiền đầu tiên |
| Avneesh (Savewise) (founder) · `2025-08-09_how-i-used-reddit-to-build-a-25k-month-business` · 09:37 | "I had over 1,500 people visit the website just from posting this spreadsheet in this Facebook group" | founder kể: bảng tính ưu đãi đăng vào nhóm Facebook đúng chủ đề, hơn 1.500 lượt vào web |
| Kourosh (Voicy) (founder) · `2026-10-14_app-for-dad-18k` · 08:49 | "I posted that like five, six times until I got blocked" | bẫy: đăng lặp nhiều lần tới khi bị chặn; kết quả khoảng 200–300 người, không bền |
| Sam Adeniyi (Algrow) (founder) · `2026-01-14_i-built-a-14k-month-saas-using-discord` · 08:34 | "I think the main thing you have to do first is build maybe a bit of rapport in the community." | founder kể: làm quen trong cộng đồng trước khi giới thiệu sản phẩm |
| Julian Alvarez (Jungle) (founder) · `2025-11-02_this-ai-study-app-makes-100kmo-heres-how-no-code` · 00:03:54 | "we basically got our first 100 users by DMing everyone that engaged with that tweet." | founder kể: nhắn DM mọi người đã tương tác với một tweet viral để có 100 người dùng đầu |
| Sanskar Tiwari (MagicSlides) (founder) · `2026-11-08_sanskar-30-micro-apps` · 10:22 | "I got my first sale through Facebook. I was going into Facebook groups, and I found a group which had the target audience" | founder kể: đơn đầu tiên đến từ một Facebook group có đúng đối tượng |
| Tom (Avenue) (founder) · `2026-09-20_this-simple-widget-makes-50k-month` · 06:21 | "Door-to-door sales, essentially" | founder kể: gõ cửa bán trực tiếp từng tiệm nhỏ, không qua kênh online |
| Hassam (Launch Fast) (founder) · `2026-01-04_how-i-built-my-first-saas-without-an-audience-25` · 04:16 | "And I guess I would be giving up equity, but I would get instant access to my target customers." | founder kể: đổi equity lấy quyền tiếp cận ngay khách của một đối tác đã có audience |
| Yoni Smolyar (Brainrot) (founder) · `2026-11-01_brainrot-400k-month` · 04:10 | "I had amassed like some 100,000 or 150,000 followers on Instagram before the launch of the app" | founder kể: có 100–150k follower Instagram từ trước khi ra mắt (nhóm audience sẵn có) |
| Angus Cheng (Bank Statement Converter) (founder) · `2025-07-20_i-make-40k-month-with-this-one-website` · 03:05 | "Don't show it to your friends and family, you know, they will just lie to you and they're probably not going to buy your product anyway." | bẫy/ý kiến ngược: founder khuyên đừng đem sản phẩm cho bạn bè và người nhà vì họ sẽ nói dối |
| Pat Walls (host/expert) · `2026-08-30_the-insanely-obvious-secret-behind-this-69k-mont` · 10:01 | "talking to customers isn't the solution, but it is the mechanism to figuring out where to market." | lời khuyên của host: nói chuyện với khách là cơ chế để biết nên quảng bá ở đâu |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 52 case full dùng g1 và đã thành công đủ để lên kênh. Người đăng Reddit mà bị xoá bài, không ai nhắn lại hoặc bị chặn thì không có trong kho. 22/52 case nêu Reddit, nên con số này cũng phản ánh việc founder hay kể Reddit, không chứng minh Reddit hơn kênh khác.
- **Bị chặn là chuyện thường.** Yadaphone bị subreddit du lịch chặn rất nhanh (câu ở bảng); Voicy đăng lặp 5–6 lần tới khi bị chặn và được khoảng 200–300 người; Jungle bị khoá tài khoản Twitter sau khi DM hàng loạt; Julian (Jungle) nói cách đó không hiệu quả để tăng trưởng nhưng hiệu quả để lấy feedback. Khi đã đăng nhiều chỗ, ghi rõ nơi nào còn mở.
- **Cold outreach có thể gần như vô ích.** Bank Statement Converter gửi cold email trong 3 tháng chỉ được 1 đơn và nhiều phản hồi giận dữ (step ghi trong kho). Once lại có 15/250–300 trả lời với DM 2–3 câu theo hashtag. Hai kết quả ngược nhau; kho không cho biết vì sao.
- **Bạn bè nói dối hay giúp?** Angus (câu ở bảng) khuyên đừng đưa cho bạn bè và người nhà; Wishlists thì chủ động xin bạn bè và người quen viết đánh giá App Store. Hai việc khác nhau (đánh giá nhận miễn phí so với phản hồi để quyết định), nhưng đừng coi một lượt "bạn bè dùng thử" là bằng chứng nhu cầu.
- **Có người dùng đầu không nghĩa là có người trả tiền.** Cardstock có 12 lượt tải trả phí ngày đầu từ một bài Reddit; về sau founder kể tăng mạnh nhờ tối ưu từ khoá App Store (xem `g2-aso-seo-organic`), tức kênh đầu và kênh scale khác nhau. Host trong video GojiBerry nói Reddit không phải nền tảng để scale (lời host trong kho). g1 trả lời "có người dùng đầu chưa", không trả lời "có bền không".
- **Người đứng ngoài ngách rất ít.** Trong 52 case chỉ 4 case ghi rõ là outsider; 8 không nêu. Số 4 quá nhỏ để rút quy luật cho người đứng ngoài.

## Quyết định
- **QUA** nếu sau 14 ngày (đề xuất, chưa có số của kho) có ≥10 người ngoài vòng bạn bè dùng thử và một kênh mang ≥3 người (đề xuất, chưa có số của kho). Ghi kênh đó vào `g2`/`g3` để làm dài hơi.
- **DỪNG** nếu đăng ở ≥15 nơi mà 0 người nhắn lại hoặc dùng thử: sản phẩm hoặc nhóm khách sai, quay về `VALIDATE.md`.
- **TEST THÊM** nếu có phản hồi nhưng chưa ai dùng: đổi dòng đầu bài (nói nỗi đau, không nói tính năng), thử một nơi nhỏ hơn, chạy lại 7 ngày.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ Nhánh A bằng chữ: Reddit, nhóm Facebook, DM, cộng đồng build in public. Không cần pháp nhân hay tiền.
- **Rào cản thật:** (1) tiếng Anh bản xứ: bài Reddit bị đọc và vote ngay, bài dịch vụng dễ bị bỏ qua; (2) tài khoản mới bị lọc nên phải mất 1–2 tuần làm nóng (GojiBerry 7–14 ngày); (3) GojiBerry nhờ nhóm bạn upvote/comment trong 5–10 phút đầu, tức cần vài người sẵn sàng đúng giờ, múi giờ Mỹ/Âu có thể bất lợi; (4) muốn biết có người trả tiền thật cần cổng thu tiền: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN), nên dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN; dựng sớm nếu muốn đo trả tiền.
- **KHÔNG nên làm** nếu khách không tụ tập online bằng chữ (như Avenue: gõ cửa từng tiệm, không làm được từ xa), hoặc nếu mình định đăng cùng một nội dung lặp ở hàng chục nơi chỉ để lấy số lượt: kho có 5 case có bị chặn, khoá hoặc bị giận.
