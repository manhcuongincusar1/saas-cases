---
id: g6-paid-ads
strategy: G6
title: "Quảng cáo trả tiền cho nền tảng (Meta, TikTok, Google, Apple Search Ads): khuếch đại cái đã thắng ở organic, hoặc thử từ đầu"
label: manual                  # dựng tài khoản, creative và đọc số bằng tay; agent chỉ giúp lập bảng chi và kết quả
time: "1 ngày dựng đo lường và creative; 14 ngày chạy test (đề xuất, chưa có số của kho)"
cost: "$250–500 để thử một nền tảng (tính lại từ số founder nêu, xem mục dự toán; không phải số của kho)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

> **Công thức này là TUỲ CHỌN, và theo lựa chọn organic của người dùng thì làm sau, không làm trước.** Kho không bảo đảm paid có lãi; 53 case full nhắc paid là những người thắng đã kể nó. Phần lớn bằng chứng là founder (19/109 step là của host, 18 trong số đó từ podcast Superwall); các host đó và video có tài trợ có động cơ bán hàng, xem mục Bẫy.

## Dùng khi
Đã có ít nhất một video hoặc format **organic cho thấy người trả tiền** (không chỉ view), và muốn đẩy nhanh bằng tiền. Nếu chưa có format organic thắng, quay về `g3-organic-content-formats`; nếu cần trả người làm nội dung, dùng `g7-creator-ops`; nếu chỉ cần được tìm thấy mà không trả tiền, `g2-aso-seo-organic`.

## Đầu vào
Một sản phẩm có paywall hoặc đường tới tiền đo được, một hoặc nhiều video organic đã chạy có số (view, lượt vào, người trả), thẻ thanh toán quốc tế và một khoản tiền thử mình chấp nhận mất.

## Điều kiện trước (đọc trước khi chi đồng nào)
Trong 53 case full dùng g6, 20 case có step nói rõ chạy paid **sau** khi có organic hoặc video thắng, và 5 case nói rõ chạy **từ đầu**, trước organic (2 case nằm ở cả hai nhóm vì chạy cả hai giai đoạn; câu truy vấn: `engine/recipes/g6-paid-ads.extra.sql`, mục 5). Chỉ tính khi step hoặc ghi chú nói rõ; 30 case còn lại không nêu thứ tự, đó là "không nêu", không phải "không có". Ngưỡng "đã có format thắng" của các founder khác nhau: Cedric (Pep AI) đợi tới khi có video thắng; Dan Kwon nói không chạm paid trước khi có ít nhất năm format thắng (con số của anh, không phải số của kho); Steven (Puffcount) đăng nhiều organic rồi scale cái thắng bằng paid.

## Các bước
1. **[manual] Kiểm điều kiện trước:** ≥1 video organic có người trả tiền (Snag chạy campaign test trên Meta với video creator đã trên 50k view). Chưa có thì dừng.
2. **[chrome] Dựng đo lường trước khi chi.** Journable gửi về Google Ads các sự kiện cài, vào paywall, dùng thử, mua (kèm giá trị) trước khi chạy chiến dịch; Chartdetector tối ưu theo sự kiện đăng ký chứ không theo lượt cài; Puffcount gửi sự kiện cài qua một MMP. Không có bước này thì số ROAS ở bước 5 không đáng tin.
3. **[manual] Lấy creative từ cái đã thắng, không làm mới.** Pep AI đưa video organic thắng trên TikTok và Instagram lên Meta; Bloom giữ nguyên format và cách kể, chỉ thêm dòng nhỏ "download" ở cuối; Yev (Sizzle AI, kho ghi là expert; case chỉ được nhắc) lấy 20 bài organic, bỏ vài đô vào mỗi bài để xem bài nào có tín hiệu bất thường.
4. **[manual] Chạy test nhỏ một nền tảng.** Số founder nêu: Habit Tracker 5 format, mỗi post ~$50 (~$250 tổng) trên TikTok Ads; Snag $50/ngày; Prayer Lock $20/ngày; Journable 10–15 USD/ngày.
5. **[manual] Đọc bằng ROAS hoặc chi phí mỗi lượt dùng thử so với giá trị khách.** Snag coi ROAS trên 1 là có lãi; Chartdetector chi $1,50 mỗi lượt tải khi mỗi người mang $3 (ROAS 2x); Puffcount CAC khoảng 20–24 USD so với LTV 55–70 USD (tự khai).
6. **[manual] Tăng ngân sách từng bậc, tắt cái thua.** Glowly +20% mỗi 3 ngày tới khi chạm trần; Habit Tracker đặt CPA mục tiêu để nền tảng tự tăng, từ ~$200/ngày lên ~$1K/ngày; Snag một ad tiêu ~$3.000 trước khi ROAS âm.
7. **[manual] Ghi bảng chi và kết quả mỗi nền tảng:** ngày, chi, số lượt dùng thử, số người trả, ROAS.

## Các mục con (theo nền tảng và ý đồ; nhóm chồng lấn, số là case full)
Đếm trên trường `scale_channels` của 53 case full dùng g6 (một case có thể có nhiều nền tảng; câu truy vấn mục 3): Meta 19, TikTok 13, Google 8, Apple Search Ads 4, "paid nhưng video không nêu nền tảng" 16; 5 case full không có paid nào trong `scale_channels` dù có step g6.

**A. Khuếch đại video organic đã thắng (20 case full, xem điều kiện trước).** Gồm Meta ads từ video TikTok/Instagram đã thắng (Pep AI, Preycreen) và Spark/partnership ads trên video của creator (Prayer Lock chạy Spark Ads trên video của creator, khoảng $3 mỗi lượt dùng thử). Preycreen: CPI tốt nhất 0,39 USD, trung bình khoảng 0,70–0,80 USD ở Mỹ. Bước tiếp theo: bước 3–6 ở trên.

**B. Meta (19 case) và TikTok Ads (13 case).** Meta: Pep AI chi ~$400/ngày; Abmax đạt ROAS 2–2,5x trên Meta rồi chuyển cùng creative sang TikTok đạt ROAS 4–5x. TikTok: Puffcount dồn phần lớn ngân sách vào TikTok vì nội dung đã làm cho TikTok (tổng chi 82.000 USD, MRR từ 3K lên 44K theo founder, app sau đó đã bán); Habit Tracker từ ~$250 test lên ~$1K/ngày. Cả hai nền tảng: founder chọn một nền tảng trước khi mở nền tảng khác (Puffcount).

**C. Google: Search, App Campaigns, YouTube (8 case).** Dùng khi khách gõ từ khoá có ý định cao. Late chi khoảng 8.000 USD/tháng với CPA mục tiêu 120 USD; Links (công cụ link-in-bio) dùng Google Search Ads như kênh tăng trưởng chính khoảng 4 năm (~$100/ngày). Hoà vốn hoặc lỗ cũng có: Journable tổng chi gần 500k USD và doanh thu gắn với Google Ads gần bằng số đó; Bank Statement Converter chi một đợt khoảng 1.000 USD thu về khoảng 300 USD rồi cắt.

**D. Apple Search Ads (4 case).** Habit Tracker bắt đầu với $100 và đặt keyword là tên app lớn; HabitKit chi ~100 USD/tháng chủ yếu để thử giả thuyết ranking; Waitly báo CAC khoảng $130 mỗi khách (B2B nhỏ); Pep AI thêm ~$150/ngày bên cạnh Meta. Số case nhỏ.

**E. Chạy từ ngày đầu (5 case: Bank Statement Converter, Story Short, Canary, Habit Tracker, Chartdetector).** Kết quả khác nhau: Bank Statement Converter cắt sau khoảng 6 tháng; Habit Tracker coi Apple Search Ads là bước đột phá nhưng nói cũng không có lãi những tuần đầu (câu ở bảng); Story Short nói luôn bắt đầu bằng quảng cáo Google và Meta để thử thị trường nhanh, sau đó mới làm SEO. Đây là nhánh ít bằng chứng và trái với lựa chọn organic của người dùng.

## Dự toán thô (tính lại từ số founder nêu; không phải số của kho)
| Hạng mục | Cách tính | Ghi chú |
|---|---|---|
| Test một nền tảng | ~$250 (5 format × ~$50, Habit Tracker) | số founder |
| Test theo ngày | $20/ngày × 14 ngày = $280 (Prayer Lock: $20/ngày; 14 ngày là đề xuất, chưa có số của kho) | tính lại |
| Khởi động Google | 10–15 USD/ngày × 14 ngày = 140–210 USD (Journable) | tính lại |
| Nếu thành công | mỗi bước +20% mỗi 3 ngày (Glowly) hoặc $200 → $1K/ngày (Habit Tracker) | số founder, một case mỗi con số |
| Mức đã thấy ở người thắng | Puffcount 82.000 USD tổng; Journable gần 500k USD tổng | số founder, tự khai |

Mục tiêu tối thiểu của dự toán là biết một creative có ROAS trên 1 hay không; không phải để có doanh thu.

## Số tiền do founder nêu (một case, một con số; tự khai, không có dashboard)
| Nền tảng hoặc ý đồ | Case | Số founder nêu |
|---|---|---|
| Google | Journable | tổng chi gần 500k USD, doanh thu gắn với Google Ads gần bằng số đó |
| Google | Late | ~8.000 USD/tháng, CPA mục tiêu 120 USD |
| Google | Bank Statement Converter | ~1.000 USD chi một đợt, ~300 USD doanh thu; cắt sau khoảng 6 tháng |
| Google | Stagetimer | 1.400 USD/tháng; vợ founder chạy Google Ads |
| Apple Search Ads | Waitly | CAC ~$130 mỗi khách |
| Apple Search Ads | HabitKit | ~100 USD/tháng |
| Meta và Apple | Pep AI | ~$400/ngày Meta, ~$150/ngày Apple; cost per download dưới $5 là ổn, đang ~$2,50 |
| Meta | Preycreen | CPI trung bình 0,70–0,80 USD (Mỹ) |
| Meta rồi TikTok | Abmax | ROAS 2–2,5x trên Meta, 4–5x trên TikTok |
| TikTok | Habit Tracker | ~$250 test; ~$200 → ~$1K/ngày |
| TikTok | Puffcount | 82.000 USD tổng; CAC 20–24 USD, LTV 55–70 USD |
| TikTok | Prayer Lock | ~$4 mỗi lượt dùng thử; founder bỏ ~$4.000 tiền tiết kiệm; thêm $6K |
| Không nêu nền tảng | Letterly | ~$200.000/tháng |
| Không nêu nền tảng | Wrestle AI | ~$500, thêm ~$250 khi audience của influencer bão hoà |

Số do host nêu (không gộp với số founder): DcDOgW (podcast Superwall): $10–20 mỗi video ở bậc test đầu, $100–500 ở bậc hai; qnDdab và F2dVvz (người bán nền tảng creator): $20 ban đầu, $50–100/ngày mỗi video, và $100/ngày trong 14 ngày.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "chi và kết quả theo nền tảng": mỗi dòng gồm nền tảng, creative, ngày, chi, số lượt dùng thử, số người trả, ROAS hoặc CAC so với LTV. Đây là đầu vào của `g8-funnel-measurement`.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: tiêu hết ngân sách test của bước 4 (mục dự toán) mà ≥1 creative có ROAS trên 1 hoặc CAC thấp hơn LTV; ngưỡng ROAS trên 1 lấy từ Snag, một founder, không phải số chung của kho. Chỉ trỏ: nếu mục tiêu là xác nhận có người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8) chứ không dùng bảng này.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 109 step trong 68 video |
| Case (video, case) có step này | 62, trong đó 53 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 19/109 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 35/53 |
| Case full không nêu existing_audience | 48/53 |
| Case full video không kể bằng chứng nhu cầu trước launch | 27/53 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 9.0 tháng (6.0–18.0), n=33 |
| Kênh scale trả tiền / thuần organic / không nêu | 48 / 3 / 2 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g6-paid-ads.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Trong 53 case full, 48 có ít nhất một kênh trả tiền ở giai đoạn scale (do định nghĩa: g6 là paid), và chỉ 3 là thuần organic: số này phản ánh việc g6 chọn đúng nhóm có paid, không cho biết paid hơn organic. Theo `community_insider`: 33 case là người trong cuộc, 6 case ghi rõ **outsider** (không phải người trong cuộc), 14 case không nêu; đừng gộp 6 và 14. 24 case full dùng cả g6 và g7 (trả creator rồi chạy paid, hoặc ngược lại), nên hai công thức này hay đi cùng nhau. Các step: 105 ở chặng grow, 4 ở launch; 41 step từ video 2025, 68 từ video 2026. 19/109 step là lời host (18 trong podcast Superwall, 1 ở Starter Story): công thức dựa chủ yếu vào việc founder đã làm, phần host dùng để làm ngưỡng thử.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các dòng của người bán nền tảng creator (Sideshift) và video có tài trợ (Arcads) được gắn nhãn trong cột cuối.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Cedric (Pep AI) (founder) · `2026-06-28_i-speedran-an-ai-app-to-100k-in-70-days` · 00:05:35 | "And so I didn't want to start running ads until we had winners." | founder kể: không chạy ads cho tới khi có video organic thắng |
| Dan Kwon (founder) · `2025-10-26_he-made-22m-from-building-simple-apps-heres-how-` · 00:31:58 | "don't touch paid until you've cracked at least five winning formats." | founder kể (Dan Kwon): không chạm paid trước khi tìm được ít nhất năm format thắng; con số năm là của anh, kho không có số tương ứng |
| Steven (Puffcount) (founder) · `2025-09-20_the-1m-mobile-app-playbook` · 02:38 | "So, we have market research, post volume, organically, scale the winners with paid ads." | founder kể: nghiên cứu thị trường, đăng nhiều video organic, rồi scale cái thắng bằng paid |
| Frederick (Habit Tracker) (founder) · `2026-10-25_88-days-10k-app` · 12:40 | "Paid ads take a lot of money upfront. I was not profitable for the first like couple of weeks. You need to have a little bit of risk tolerance when you're going into it because you might not see profit at all." | founder kể: paid tốn tiền trước, có thể vài tuần đầu chưa có lãi; cần chịu được rủi ro |
| Julian (Gravl) (founder) · `2025-11-13_how-i-built-it-400k-month-mobile-app-gravl` · 07:42 | "The tip number one for sure will be to validate before spending money on ads." | founder kể: lời khuyên số một là xác nhận ý tưởng trước khi tiêu tiền vào ads |
| Angus Cheng (Bank Statement Converter) (founder) · `2025-07-20_i-make-40k-month-with-this-one-website` · 04:39 | "After about 6 months of running Google search ads, I decided, you know, I'm just not going to do this anymore. I might not even do this app anymore." | founder kể: sau khoảng sáu tháng chạy Google Search Ads thì dừng, thậm chí tính bỏ luôn app |
| Jay (Bloom) (founder) · `2025-07-07_this-app-makes-2myear-with-this-viral-tiktok-str` · 00:14:34 | "organic growth obviously has like ups and downs of you know something goes viral and then you know it will be on viral for months but then after that it will tailor down" | founder kể: organic lúc lên lúc xuống, viral vài tháng rồi giảm; đó là lúc thêm paid với cùng video |
| Alex (Boost App Social) (founder) · `2026-04-26_copy-this-facebook-ads-strategy-itll-blow-up-you` · 00:20:29 | "one video out of 85 would would get all the ad spend and work." | founder kể: trong 85 video, chỉ một video nhận gần hết ngân sách ads và chạy được |
| Dan Kwon (founder) · `2025-10-26_he-made-22m-from-building-simple-apps-heres-how-` · 00:10:32 | "We did test paid, but didn't like the margins on it" | founder kể (Dan Kwon): có thử paid nhưng không thích biên lợi nhuận |
| Tibo (Outrank) (founder) · `2025-12-07_i-built-4-saas-apps-to-100k-mrr-heres-my-exact-p` · 10:53 | "you will spend a lot of energy pushing people to your software, and 99% of those people are going to flow away directly after trying your software. You need to make sure that your retention is good." | bẫy do founder nêu: đẩy người về sản phẩm tốn công, 99% rời đi nếu retention không tốt |
| Yev (Sizzle AI) (host/expert) · `2025-06-23_how-i-grow-viral-apps-to-1m-downloads-just-copy-` · 00:12:14 | "You take all of your organic pieces and just put a few dollars into them." | lời khuyên của host/expert: lấy các bài organic và bỏ vài đô vào mỗi bài để xem bài nào có tín hiệu |
| Drew Levin (Sideshift) (host/expert) · `2026-06-01_i-studied-1000000-ugc-ads-this-is-what-will-grow` · 00:37:16 | "You should not preemptively spark a video." | lời khuyên của người bán nền tảng creator (có động cơ bán hàng): không nên chạy Spark cho video trước khi organic cho thấy tín hiệu |
| Jason Lee (host/expert) · `2026-09-23_silent-ugc-100k-apps` · 00:13:42 | "you will start to collect data and see what videos are getting views and then you can take those videos and put an ad spend behind them and get even more traffic" | lời khuyên của host (video có tài trợ Arcads): đăng organic trước không phải cách duy nhất vì nhiều app cũng chạy ads, nhưng là cách tốt để bắt đầu từ số 0 |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 53 founder full nhắc paid và đủ thành công để lên kênh; người chi tiền mà không có lãi thì vắng mặt. Vẫn có người kể lỗ: Bank Statement Converter (chi ~1.000 USD, thu ~300 USD, cắt sau khoảng 6 tháng), Journable (tổng chi gần 500k USD, doanh thu gần bằng số đó) và Prayer Lock (bỏ ~$4.000 tiền tiết kiệm vào TikTok Ads, thêm $6K sau đó; video không nói kết quả cuối).
- **Biên lợi nhuận và nền tảng đổi.** Dan Kwon thử paid nhưng không thích biên lợi nhuận (câu ở bảng) và Setter AI thấy biên giảm từ trên 90% xuống khoảng 80% sau khi chạy ads và thuê freelancer; Links thấy Instagram ads tốt lúc đầu rồi nền tảng đổi thuật toán và kênh không còn hiệu quả (chuyển sang Google Search); dbli thấy TikTok ads ban đầu rất hiệu quả rồi lợi nhuận giảm khi chi nhiều; Bloom giảm quảng cáo TikTok cuối 2023 vì CAC xấu đi và quay về organic.
- **Tài khoản quảng cáo bị khoá.** Boost App Social bị khoá tài khoản Meta vĩnh viễn 6–8 lần, mỗi lần phải khiếu nại; đây là rủi ro vận hành, không chỉ chuyện số.
- **Đẩy người về khi giữ chân kém.** Tibo (Outrank) nhắc 99% người được đẩy về rời đi nếu retention không tốt (câu ở bảng); chi ads vào sản phẩm giữ chân kém là đốt tiền. Xem `g5-retention`.
- **Bias của nguồn.** 13 step g6 nằm ở 6 video mà bias nêu công ty bán nền tảng creator, UGC hoặc phân phối (Sideshift, Pebble, Arcads), trong đó 8 step là lời host: Canyon, Drew Levin và Nick Lawton (Sideshift) khuyên bỏ tiền "spark" lên video organic của creator, tức khuyến nghị dẫn tới việc mua thêm nội dung từ nền tảng họ bán. Video Jason Lee (kênh jason-lee) có tài trợ Arcads và toàn bộ cách làm chạy trên Arcads; kho chỉ lấy một step g6 của video này (organic trước rồi bỏ tiền ads sau, không phụ thuộc Arcads), thuộc case chỉ được nhắc, không phải founder kể kỹ. Podcast Superwall (18/19 step chỉ host) do công ty bán paywall tài trợ: họ được lợi khi app chi nhiều.
- **Chạy paid ngay từ đầu không phải mặc định.** Chỉ 5 case full nói rõ làm vậy, và kết quả lẫn lộn (nhánh E).

## Quyết định
- **QUA** (nâng ngân sách) nếu sau test nhỏ có ≥1 creative với ROAS trên 1 hoặc CAC dưới LTV (ngưỡng đề xuất, ROAS trên 1 lấy từ Snag; chưa có số chung của kho). Tăng từng bậc (Glowly +20% mỗi 3 ngày).
- **DỪNG** nếu chưa có format organic thắng ở bước 1, hoặc đã tiêu hết ngân sách test mà không creative nào ROAS trên 1 (đề xuất, chưa có số của kho): quay về `g3-organic-content-formats`; đừng thêm tiền để "học".
- **TEST THÊM** nếu ROAS gần 1: đổi creative lớn, không tinh chỉnh nhỏ (Journable làm nội dung khác biệt lớn), chạy lại 7 ngày; hoặc thử nền tảng khác với cùng creative (Abmax chuyển Meta sang TikTok).

## Cho solo founder bán global (từ VN)
- **Chép được:** bước 1–7 làm hoàn toàn từ xa; Apple Search Ads dùng tên app đối thủ làm keyword (Habit Tracker) là việc nhỏ ($100). Chạy ads ở thị trường rẻ hơn cũng có tiền lệ (Gravl dịch app sang tiếng Tây Ban Nha và chạy ads ở Nam Mỹ, dưới 50 USD/ngày, vì Mỹ đắt và cạnh tranh), nhưng chỉ ghi nhận như một case.
- **Rào cản thật:** (1) vốn: đây là công thức trả tiền ngay, runway ngắn thì mỗi $250 là một phần; (2) thanh toán: cần thẻ quốc tế cho Meta/TikTok/Google/Apple Search Ads, và nếu thu USD ngoài store: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ; (3) tài khoản quảng cáo bị khoá (Boost App Social) mà hỗ trợ đa phần theo múi giờ Mỹ/Âu; (4) tiếng Anh cho creative và landing page, creative dịch vụng giảm chuyển đổi; (5) mục tiêu mặc định của người dùng là organic, nên chỉ chạy sau khi có format thắng.
- **KHÔNG nên làm** khi chưa có format organic thắng, khi giữ chân kém (xem `g5-retention`), khi không thể chịu mất khoản test, hoặc khi chưa có cách đo người trả tiền (bước 2).
