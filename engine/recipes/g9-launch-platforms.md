---
id: g9-launch-platforms
strategy: G9
title: "Launch và lấy khách qua nền tảng có sẵn người dùng: Product Hunt, Hacker News, marketplace, lifetime deal, directory"
label: manual                  # đăng, chờ và đo bằng tay; agent chỉ giúp lập bảng chọn nền tảng và ghi kết quả
time: "2 giờ chuẩn bị cho một nền tảng; 1 ngày đăng; 7 ngày đo"
cost: "$0 để đăng; lifetime deal tốn một phần doanh thu cho nền tảng (RocketHub lấy 40% theo kho)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

## Dùng khi
Đã có sản phẩm dùng được và đã qua `g1-first-10-users` (có vài người dùng thật để sửa lỗi), và mình muốn một đợt người vào cùng lúc hoặc một nguồn khách đều từ nền tảng nơi khách đã sẵn có mặt. Không dùng thay cho `g1` khi sản phẩm chưa chạy: kho có nhiều đợt traffic không giữ được người.

## Đầu vào
Một sản phẩm dùng được, một trang đích rõ (một câu nói làm gì cho ai), và danh sách nơi khách mục tiêu đã có mặt (nền tảng nào họ dùng hằng ngày).

## Các bước
1. **[manual] Chọn nền tảng theo nơi khách đang ở, không theo độ nổi tiếng.** Bảng 5 dòng: nền tảng, khách ở đó có phải khách mình không, chi phí, thời gian chuẩn bị. Mẫu hình trong kho: công cụ cho developer thì Hacker News và GitHub (ChartDB mở mã nguồn rồi đăng Show HN; Postiz đăng Show HN dẫn tới link GitHub); sản phẩm gắn vào một nền tảng khác thì marketplace của nền tảng đó (Data Fetcher trên Airtable, Sync2sheets trên Google Workspace, Profit AI trên Shopify); app người dùng cuối thì pre-order App Store (Runafy, Wrestle AI) hoặc Product Hunt; cần tiền sớm thì lifetime deal (xem bước 5).
2. **[manual] Chuẩn bị tài khoản và trang đích trước ngày đăng.** Postiz đăng ký Hacker News khoảng 2 tuần trước, Reddit cần karma, thêm Lemmy; mục tiêu là lên trending GitHub. Trang đích viết theo `g11-positioning-messaging` hoặc ít nhất một câu "làm gì cho ai".
3. **[manual] Chọn một ngày, đăng một nền tảng mỗi lần.** ChartDB chuẩn bị rồi chọn một ngày đăng Show HN. Neural Frames đăng Hacker News khoảng một tuần sau khi đưa sản phẩm lên mạng. SuperMeme launch Product Hunt cùng nhóm người dùng đầu từ mạng xã hội.
4. **[manual] Gắn đo trước khi đăng:** mỗi nền tảng một link riêng (UTM hoặc tên miền phụ) để sau 7 ngày biết lượt vào, đăng ký, người trả tiền, và còn lại bao nhiêu sau 7 ngày. Savewise có traffic từ Product Hunt, Hacker News, Indie Hackers nhưng bounce khoảng 95–96%; nếu không đo thì chỉ thấy số lượt vào.
5. **[manual] Nếu chọn lifetime deal, theo thứ tự của playbook trong kho** (Thrill, do founder Mike mô tả; một phần là bước chỉ host mô tả): bán LTD một lần giá khoảng $59–100 để có tiền đầu; bán private LTD qua nhóm Reddit, Facebook, X và nhóm LTD; sau đó lên AppSumo (marketplace phí thấp hơn, hoặc gói chọn lọc qua đội sales); cuối cùng một private LTD giá cao hơn, gửi danh sách email rồi đóng hẳn. Cách khác: SuperGrow lên RocketHub với ba gói $79, $199, $299, RocketHub lấy 40% và làm phần marketing, rồi mới lên Product Hunt (Product of the Week, khoảng 50 khách mới). MagicSlides launch hai sản phẩm bằng LTD: doanh thu trong 2 ngày bằng lương của founder, làm hai lần rồi nghỉ việc.
6. **[manual] Sau 7 ngày ghi kết quả** vào bảng ở mục Đầu ra, rồi quyết định theo mục Quyết định.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng mỗi nền tảng một dòng: ngày, số lượt vào, số đăng ký, số người trả tiền, số người còn dùng sau 7 ngày, công sức (giờ). Dòng nào có người trả tiền hoặc người còn dùng thì ghi vào `g2`/`g3` để lặp lại; dòng chỉ có lượt vào thì ghi "traffic, chưa là người dùng".

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 7 ngày, một nền tảng cho ít nhất 10 người dùng thật còn dùng hoặc ít nhất 1 người trả tiền (tham chiếu để hình dung: Journable có 2 người trả tiền từ vài trăm lượt cài; Shipper có $50 MRR đầu tiên). Muốn xác nhận nhu cầu thật thì dùng `VALIDATE.md` (cổng 1–4, thang 0–8), không dùng bảng này.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 37 step trong 30 video |
| Case (video, case) có step này | 28, trong đó 27 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 4/37 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 17/27 |
| Case full không nêu existing_audience | 26/27 |
| Case full video không kể bằng chứng nhu cầu trước launch | 15/27 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 19.0 tháng (15.5–42.0), n=15 |
| Kênh scale trả tiền / thuần organic / không nêu | 8 / 18 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g9-launch-platforms.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Mục con (câu truy vấn: `engine/recipes/g9-launch-platforms.extra.sql`; các nhóm chồng lấn một phần): trong 27 case full, step nhắc **Product Hunt** ở 10 case (9 case đã launch ở đó; Neural Frames nhắc để nói đó không phải kênh họ dùng), **Hacker News/Show HN** ở 6, **lifetime deal/AppSumo/RocketHub** ở 3, **marketplace/chợ ứng dụng** của một nền tảng (không tính hai kênh trên) ở 8, **directory** ở 3, **pre-order/crowdfunding/hackathon** ở 4. Trên cả kho (mọi tactic), 12 case full nhắc Product Hunt, 7 nhắc Hacker News, 16 nhắc ít nhất một trong hai; hai case trong số 16 chỉ nhắc để nói về chuyện khác (Uneed: drama Product Hunt làm ý tưởng; Blog to Pin: host nói đừng trốn sau Product Hunt). Trong 186 case full toàn kho, đó là một phần nhỏ, và 4/37 step là lời của host. Theo `community_insider`: 20 case là người trong cuộc, 0 case ghi rõ outsider, 7 không nêu. Các step phân bố 30 ở chặng launch và 7 ở grow; 21 step từ video 2025, 16 từ video 2026.

**Kết quả founder nêu (tự khai, không phải số kiểm).** Product Hunt, 9 case đã launch: có người trả tiền hoặc khách được nêu ở 4 (Journable 2 người trả tiền trên vài trăm lượt cài; Shipper $50 MRR đầu tiên; AngelMatch khoảng $4.000 trong tháng đó sau khi dựng database khoảng 40.000 nhà đầu tư; SuperGrow khoảng 50 khách mới, đến sau lifetime deal); chỉ traffic hoặc thứ hạng ở 4 (Savewise bounce khoảng 95–96%; Links nhiều traffic; SuperMeme số 1 ngày ra mắt; Sync2sheets có traffic nhưng không thành khách trả tiền, launch khoảng một năm rưỡi sau khi ra mắt); 1 không nêu kết quả (Sunflower). Hacker News: ChartDB nói hàng nghìn kỹ sư vào sản phẩm trong một ngày; Cursor Directory lên front page và nhiều YouTuber nhắc tới; Neural Frames lên top; Massive đẩy HN kèm lấy email thủ công và nhắn cá nhân để có 100–500 người dùng trả tiền đầu; Savewise và Sync2sheets (HN) có traffic nhưng không giữ hoặc không trả tiền; Postiz kỳ vọng khoảng 10.000 lượt xem nếu lên trang chính (kết quả không nêu trong step).

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các con số kết quả ở trên lấy từ step của kho (tóm tắt lời founder), không phải câu trích trong bảng.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Steve (Journable) (founder) · `2026-03-25_i-built-a-100k-month-android-app` · 05:43 | "We started by launching on Product Hunt." | founder kể: launch Product Hunt làm marketing ngày 0 (theo step của kho: vài trăm lượt cài, 2 người trả tiền) |
| Charlie Clark (Links) (founder) · `2026-10-21_quit-job-micro-saas-30k` · 07:11 | "launched on Product Hunt. And I got quite a bit of traffic from it" | founder kể: launch Product Hunt sau khi sửa theo feedback, có nhiều traffic (không nêu số người trả tiền) |
| David (Shipper) (founder) · `2026-05-28_i-built-a-micro-version-of-a-1b-saas-now-i-make-` · 06:24 | "To this day, we haven't used any paid channels at all." | founder kể: tới nay không dùng kênh trả tiền nào; Shipper launch MVP lên Product Hunt tuần đầu và có $50 MRR đầu tiên (con số từ step của kho) |
| Pat Walls hoặc Gus (host/expert) · `2026-02-05_i-make-16k-month-even-in-a-tiny-niche` · 17:04 | "Just like Nick said, it wasn't about hiding behind a Product Hunt launch. It was about getting it in the hands of one user that was genuinely solving their problem." | lời khuyên của host: launch Product Hunt không thay được việc đưa sản phẩm tới một người đang thật sự cần |
| Deven Bhooshan (SuperGrow) (founder) · `2025-09-10_how-i-made-65k-in-3-days` · 12:44 | "Launching on LTD is not just for cash." | founder nói: lifetime deal không chỉ để lấy tiền mặt (SuperGrow qua RocketHub, sau đó Product Hunt) |
| Pat Walls (host/expert) · `2025-09-10_how-i-made-65k-in-3-days` · 12:59 | "lifetime helps build community around your product which led to a really big product hunt launch." | lời khuyên của host: lifetime deal gây cộng đồng và dẫn tới một đợt Product Hunt lớn (SuperGrow) |
| Pat Walls hoặc Gus (host/expert) · `2026-03-29_my-app-made-120k-in-24-hours` · 17:17 | "Sometimes I think about lifetime deals as just a pricing strategy." | lời khuyên của host: nhìn lifetime deal như một chiến lược giá |
| Andy Cloak (Data Fetcher) (founder) · `2025-08-13_how-i-built-it-23k-month-micro-saas` · 03:40 | "So, the main benefit I guess is distribution, right?" | founder nói: lợi ích chính của marketplace là phân phối |
| Andy Cloak (Data Fetcher) (founder) · `2025-08-13_how-i-built-it-23k-month-micro-saas` · 06:58 | "I got the first customer after a few days" | founder kể: khách đầu tiên đến sau vài ngày nhờ đứng trên marketplace Airtable từ sớm |
| Leandro (Sync2sheets) (founder) · `2025-06-11_how-i-built-it-9k-month-micro-saas` · 09:52 | "So, the first source of installs was of course the marketplace" | founder kể: marketplace Google Workspace là nguồn cài đặt đầu tiên |
| Pat Walls (host/expert) · `2025-04-19_my-apps-make-4-5m-year-with-0-marketing` · 06:32 | "And that's maybe the secret, building on top of a marketplace." | lời khuyên của host: xây trên một marketplace có thể là bí quyết (nói về Kaching Bundles trên Shopify) |
| Julian Alvarez (Jungle) (founder) · `2025-11-02_this-ai-study-app-makes-100kmo-heres-how-no-code` · 00:04:24 | "we posted our thing on AI tool directories, kind of like future tools, for example." | founder kể: đăng lên các thư mục công cụ AI; step của kho ghi founder đoán giờ các thư mục này đã bão hoà |
| Caleb Dean (Runafy) (founder) · `2026-03-09_i-speedran-an-ai-app-from-0-to-100k-exit-in-26-d` · 00:01:58 | "So, we had 3,000 downloads." | founder kể: App Store pre-order mở khoảng 2 tuần, lúc launch tải về khoảng 3.000 máy |
| Ryan Chen và Kent Yoshimura (NeuroGum) (founder) · `2025-02-07_the-underdog-from-life-changing-accident-to-100m` · 06:54 | "launched on Indiegogo" | founder kể: lần ra mắt công khai đầu là chiến dịch crowdfunding Indiegogo (sản phẩm vật lý, không phải app) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 27 case full dùng g9 và đã thành công đủ để lên kênh. Người launch Product Hunt mà không có ai vào, hoặc có traffic mà không giữ được ai, không có trong kho; 9 case Product Hunt ở trên chỉ là những người chịu kể. Trong 4 case Product Hunt chỉ có traffic hoặc thứ hạng, hai case nói rõ không thành người trả tiền hoặc không ở lại.
- **Traffic không phải người dùng.** Savewise bounce khoảng 95–96% từ Product Hunt, HN và Indie Hackers; Sync2sheets cũng có đợt HN lên trang chủ, traffic tăng vọt và có backlink nhưng không thành khách trả tiền. Host trong video Blog to Pin nói không phải trốn sau Product Hunt mà phải đưa sản phẩm tới một người đang thật sự cần (câu ở bảng).
- **Đi sau chưa chắc có ích.** Sync2sheets launch trên Product Hunt khoảng một năm rưỡi sau khi ra mắt; kết quả là traffic không ra khách. Kho không cho biết nếu launch sớm hơn thì khác không.
- **Marketplace và directory không đều nhau.** Data Fetcher có khách đầu sau vài ngày nhờ vào Airtable marketplace từ sớm; Jungle đăng lên các thư mục công cụ AI và founder đoán giờ các thư mục này đã bão hoà. Kho có 8 case marketplace, 3 case directory: bằng chứng directory mỏng.
- **Lifetime deal trả trước, không phải khách đều.** MagicSlides và Thrill dùng LTD để có tiền đầu; kho không nêu họ còn bao nhiêu khách sau LTD, nên không biết churn hay chi phí hỗ trợ. Host nói LTD như một chiến lược giá (câu ở bảng): coi nó là quyết định về giá (xem `g4-pricing-paywall`) trước khi coi là kênh.
- **Crowdfunding và hackathon là sản phẩm/ngữ cảnh đặc thù.** NeuroGum (Indiegogo) là sản phẩm vật lý; Payout vào hackathon RevenueCat. Ít chép được cho SaaS thuần phần mềm.

## Quyết định
- **QUA** nếu sau 7 ngày, một nền tảng cho ≥10 người dùng thật còn dùng hoặc ≥1 người trả tiền (đề xuất, chưa có số của kho). Lặp lại nền tảng đó (marketplace: cập nhật listing; HN: bài khi có bản lớn, như Postiz đăng lại mỗi bản mới) và chuyển nguồn đó sang `g2`/`g3`.
- **DỪNG** nếu traffic không giữ (kiểu bounce ~95% của Savewise) và không ai trả tiền sau lượt thứ hai: sản phẩm hoặc nhóm khách sai, quay `g1` hoặc `VALIDATE.md`. Dừng LTD nếu mình không muốn bán trọn đời giá thấp.
- **TEST THÊM** nếu là marketplace (khách đến chậm): theo dõi 30 ngày (đề xuất, chưa có số của kho; Data Fetcher có khách đầu sau vài ngày) trước khi kết luận.

## Cho solo founder bán global (từ VN)
- **Chép được:** Product Hunt, Hacker News, marketplace của Airtable/Google/Shopify, directory, pre-order App Store đều đăng được từ xa bằng tiếng Anh, không cần pháp nhân để đăng.
- **Rào cản thật:** (1) nhận tiền: marketplace, AppSumo, RocketHub đều trả qua tài khoản nhận tiền của nền tảng; kiểm điều kiện nhận tiền cho quốc gia mình trước khi đầu tư; nếu bán trực tiếp: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ; (2) người thắng ở kho thường có audience hoặc cộng đồng đi cùng: Cursor Directory có developer following từ đầu (ghi trong kho), nên một bài Show HN không cô lập được tác dụng của riêng nó; (3) tiếng Anh bản xứ cho tiêu đề và phần trả lời comment ngày launch; (4) múi giờ: ngày launch bám giờ Mỹ.
- **KHÔNG nên làm** khi sản phẩm chưa giữ chân được vài người dùng đầu (traffic sẽ trôi), khi khách không có mặt ở nền tảng đó (HN không dành cho khách phổ thông), hoặc với crowdfunding sản phẩm vật lý khi chưa có pháp nhân và logistics giao hàng.
