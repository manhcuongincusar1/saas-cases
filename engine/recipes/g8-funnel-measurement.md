---
id: g8-funnel-measurement
strategy: G8
title: "Đo và quyết bằng số: phễu view tới cài tới trả, CAC/LTV/P&L, attribution theo nguồn"
label: manual                  # gắn công cụ và đọc số bằng tay; công cụ đo chỉ lấy số, quyết định là của mình
time: "2–3 giờ để gắn đo và dựng bảng; đọc bảng 15 phút mỗi tuần"
cost: "$0 để dựng bảng; công cụ đo tuỳ nhà cung cấp (một founder nêu Mixpanel khoảng $100/tháng)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: [posthog, mixpanel, revenuecat, superwall, appsflyer]
status: draft
---

## Dùng khi
Đã có kênh mang người vào (`g1-first-10-users`, `g3`, hoặc quảng cáo) và đã có cách thu tiền (`g4-pricing-paywall`), nhưng mình chưa biết **bước nào của phễu rò, kênh nào mang người trả tiền, và mỗi khách có lãi hay không**. Nếu chưa có người dùng nào, quay lại `g1`: không có gì để đo. Nếu mục tiêu là biết ý tưởng có ai muốn mua không, dùng `VALIDATE.md`, không dùng công thức này.

## Đầu vào
Một sản phẩm đã có người dùng thật (dù ít), danh sách kênh đang đăng hoặc chạy (mỗi kênh một dòng), và quyền cài công cụ đo vào app hoặc web (SDK/script).

## Các bước
1. **[manual] Vẽ phễu 4–5 bước và chọn một chỉ số chính** (≤15 phút). Steven (PuffCount) coi mỗi bước là phễu: view, click, cài đặt, mua; tối ưu từ trên xuống, chỉ chạm bước dưới khi bước trên đã đủ dữ liệu. Symmetry chọn activation làm chỉ số chính và đặt OKR theo quý. Visualizee (web) ghi phễu: landing ~300 lượt xem mỗi ngày, 5–10 trial mới mỗi ngày, khoảng 25% sang trả tiền (founder nêu). Veed chỉ theo dõi một việc: traffic và doanh thu kỳ này phải cao hơn kỳ trước.
2. **[chrome] Gắn đo vào sản phẩm** (≤15 phút mỗi công cụ). Kho nêu: RevenueCat cho doanh thu trong app và Mixpanel cho hành vi (Stoppr; Mixpanel khoảng $100/tháng); PostHog cho thí nghiệm (Symmetry, Career Hound); Superwall hoặc RevenueCat cho CPI, tỉ lệ dùng thử, đăng ký, retention, LTV (PuffCount); Amplitude một case. Clear 30 chuyển việc thu dữ liệu lên sớm trong onboarding (trước đó chỉ thu số điện thoại ở cuối) để thấy bỏ dở từng màn; màn giới thiệu giữ khoảng 85–90% (founder nêu). ChartDetector tích hợp AppsFlyer để gửi sự kiện mua về TikTok và thuê freelancer cài vì dễ cấu hình sai.
3. **[manual] Gắn attribution cho từng nguồn** (≤15 phút mỗi nguồn). Arvow: UTM riêng và mã coupon riêng cho từng video YouTube, thêm câu hỏi "đến từ đâu" trong onboarding. Elephas: UTM theo tính năng, ngày và subreddit. Payout: ManyChat nhận link qua comment và custom product page trên App Store, để đo lượt tải theo từng influencer. Pep AI: creator code và link riêng trong bio. Khi không gắn được link (Instagram không cho): Locked quy kết theo spike lượt tải sau khi video nổ; Early nói khó đo và tìm đỉnh view trùng đỉnh cài và mua. Expert (Jetpack, mention) dùng tên miền riêng trỏ về app; expert Sizzle AI đo lift bằng cách tắt rồi bật lại quảng cáo và ước 10–20% mua hàng đến từ nguồn attribution khác (expert nêu, không phải số của founder).
4. **[manual] Mỗi tuần tính P&L theo kênh** (≤15 phút). Habit tracker mỗi sáng tính LTV thực trừ CPA, phí Apple 15% (5% nếu vào chương trình small business), revenue cap 1% và VAT khoảng 20% nếu khách EU, và chỉ chạy ads khi hoà vốn ngay ở giao dịch đầu. Clear 30 đo ROAS và chi phí mỗi trial theo kênh sau thuế Apple. ChartDetector xem ROAS mỗi tuần, tăng ngân sách không quá 20% mỗi 3 ngày. Locked giữ CPM influencer dưới RPM (khoảng $3–4). Late tính doanh thu trên mỗi đô quảng cáo. Brainrot so kênh nào đưa người dùng rẻ hơn và nhóm nào mang doanh thu nhiều hơn. Mọi con số trên là con số founder nêu, một case một con số, không phải chuẩn của kho.
5. **[manual] Đọc theo ngưỡng của chính mình và ghi quyết định.** Ngưỡng founder nêu (không phải chuẩn): Flame dưới 300 view thì xem lỗi tài khoản, 300–1.000 sửa nội dung, 1.000–5.000 giữ format đổi copy; Nomad Table giữ format khi tỉ lệ xem quá 3 giây ổn định ở 75–80%; Noise tạm dừng một playbook sau 446 bài và 200.000 view không bật. Pingo thấy người dùng Nga chiếm nửa user base nhưng không trả tiền được (Google Play và Apple chặn thanh toán) nên dừng marketing tiếng Nga; Lobby thấy khoảng 60% người dùng ở Israel có đủ 5 bạn trong ngày đầu, nơi khác khoảng 20%, và quyết đầu tư vào mật độ mạng. Symmetry chạy mỗi A/B ít nhất 2 tuần, biến thể không đổi chỉ số thì bỏ. Expert Sizzle AI: tìm bước rơi trên 50% rồi sửa trước (ngưỡng expert).
6. **[manual] Ghi bảng "kênh × phễu × P&L"** (một dòng mỗi kênh mỗi tuần): số người vào, cài, trial, trả, chi phí, doanh thu, ghi chú quyết định (giữ, sửa, dừng).

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): một bảng hằng tuần mỗi kênh một dòng gồm số người ở từng bước phễu, chi phí, doanh thu và quyết định (giữ, sửa, dừng); kèm một dòng P&L theo khách nếu có chi phí mua người dùng. Đầu vào để chọn kênh cho `g6-paid-ads` và `g7-creator-ops` và để biết sửa ở đâu trong `g4-pricing-paywall`.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 7 ngày có bảng phễu ≥4 bước có số thật, mỗi kênh đang chạy có một nguồn gắn attribution, và ≥1 dòng P&L. Chỉ trỏ: nếu mục tiêu là xác nhận có người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8).

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 42 step trong 32 video |
| Case (video, case) có step này | 30, trong đó 26 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 4/42 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 11/26 |
| Case full không nêu existing_audience | 23/26 |
| Case full video không kể bằng chứng nhu cầu trước launch | 19/26 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.5 tháng (6.5–24.0), n=16 |
| Kênh scale trả tiền / thuần organic / không nêu | 14 / 11 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g8-funnel-measurement.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Mục con (câu truy vấn: `engine/recipes/g8-funnel-measurement.extra.sql`; các nhóm chồng lấn nhau): trong 26 case full, step về attribution ở 8 case, về công cụ đo ở 8, về đo nội dung (view, 3 giây, playbook) ở 7, về chi phí và lợi nhuận ở 6, về phễu và bước rơi ở 5, về thí nghiệm hoặc OKR ở 3. Theo `community_insider`: 14 trong cuộc, 3 **outsider**, 9 **không nêu**; đừng gộp 3 và 9. Phần lớn step ở chặng grow (35/42) và từ video 2026 (29/42 so với 13 ở 2025). 4/42 step là lời của host hoặc expert (cả bốn ở kênh Superwall); 20 step đến từ kênh Superwall và 22 từ Starter Story (kể cả Starter Story Build), nên công thức dựa chủ yếu vào việc founder đã làm. Tỉ lệ có kênh trả tiền ở giai đoạn scale (14/26) cao hơn mức chung của kho, hợp lý vì đo ROAS và CPA chỉ có nghĩa khi chi tiền.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Steven (PuffCount) (founder) · `2025-09-20_the-1m-mobile-app-playbook` · 17:46 | "Everything is a funnel." | founder kể: coi mỗi bước là một phễu và tối ưu từ trên xuống |
| Frederick (habit tracker) (founder) · `2026-10-25_88-days-10k-app` · 10:29 | "I'd recommend aiming for profitability on the initial transactions alone." | founder kể: nhắm hoà vốn ngay ở giao dịch đầu khi tính P&L từng khách |
| Frederick (habit tracker) (founder) · `2026-10-25_88-days-10k-app` · 12:40 | "Paid ads take a lot of money upfront. I was not profitable for the first like couple of weeks. You need to have a little bit of risk tolerance when you're going into it because you might not see profit at all." | bẫy: quảng cáo cần tiền trước, vài tuần đầu của founder này chưa có lãi |
| Mauro (Symmetry) (founder) · `2026-09-09_how-i-built-this-160k-month-gym-app` · 12:27 | "It increased 3% retention adding one screen. That is why you have to AB test everything." | founder kể: thêm một màn hình ở cuối onboarding, retention tăng 3% nhờ A/B test |
| An (Flame) (founder) · `2026-02-16_full-app-growth-guide-2026-how-to-make-viral-con` · 00:52:39 | "I realized that views don't matter if your product if your videos don't convert." | founder kể: lượt xem không có nghĩa nếu video không đưa tới chuyển đổi |
| Evan (Locked) (founder) · `2026-06-07_the-14-year-old-who-built-a-14kmonth-ai-app` · 00:19:03 | "I would just care about followers and views, but in reality, that's a huge mistake." | founder kể: từng chỉ để ý follower và lượt xem, sau coi là sai lầm lớn |
| Flo (MonAI) (founder) · `2026-04-05_how-this-app-makes-35k-month` · 06:00 | "We don't get millions of views mostly, but those that we get, they do convert at a fairly high rate." | founder kể: ít video nhiều view nhưng số đó chuyển đổi khá cao |
| Morrie (Pingo) (founder) · `2026-04-19_how-i-built-a-500kmo-ai-app-so-you-can-just-copy` · 00:24:44 | "The top 20-30% of creators are doing most of the views. The bottom percent are doing none of them and they're kind of dead spend." | founder kể: 20-30% creator đứng đầu tạo phần lớn lượt xem, phần cuối là tiền chi bỏ đi |
| PropGPT (founder) · `2025-11-18_how-we-built-it-30k-month-mobile-app` · 06:04 | "Using analytics platforms like Posthog and simply talking to enough users, you see that there is a pattern of human behavior that doesn't align with how the app is designed." | founder kể: đọc analytics và nói chuyện với người dùng để thấy chỗ hành vi không khớp thiết kế |
| Jake (Early) (founder) · `2026-07-05_this-insanely-simple-app-makes-50k-month` · 14:59 | "Focus on top of funnel only. That is the most valuable skill right now is marketing." | ý kiến ngược của founder: chỉ tập trung đầu phễu, vì marketing là kỹ năng đáng giá nhất lúc này |
| Nick Lawton (host/expert) · `2026-08-03_1-ugc-expert-reveals-how-to-market-consumer-apps` · 00:00:17 | "AI UGC, great for vanity views, terrible for conversions at the end of the day. I've not seen it convert." | lời của expert (bán nền tảng UGC): UGC tạo bằng AI nhiều view nhưng chuyển đổi kém |
| Joseph Choi (host/expert) · `2026-10-11_start-1m-app-from-scratch` · 00:07:41 | "However, if one creator is getting a lot of views, but I'm not getting any paying users, there's no point in spending money there." | lời khuyên của host: creator nhiều view mà không có người trả tiền thì đừng chi thêm |
| Dawson Gibbs (host/expert) · `2026-10-05_dawson-ugc-1b-views` · 00:43:17 | "Whenever a video gets like 10,000 to 20,000 views and it has an engagement rate of like at least 3%, we will then tell those creators to double down and repost that same video" | ngưỡng của expert (chủ agency UGC): khi nào bảo creator đăng lại video |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 26 case full dùng g8 và lên được kênh; founder đo kỹ mà vẫn thất bại không có trong kho. Dữ liệu đo trong kho cũng tự khai: không có dashboard.
- **Nhiều case chỉ kể, không cho số.** Chỉ 6/42 step có số cụ thể ở trường ngưỡng hoặc chi phí (truy vấn mục (6) của `extra.sql`). Các ngưỡng ở bước 5 (Flame, Nomad Table, Noise) là của một founder đo nội dung video trên một nền tảng, không áp được sang web hay kênh khác.
- **Đo view không đủ, nhưng không phải ai cũng đồng ý.** An, Evan, host Joseph Choi nói lượt xem không có nghĩa nếu không ra người trả (các câu ở bảng), expert Nick Lawton nói UGC AI nhiều view mà chuyển đổi kém (ông bán nền tảng UGC). Phản ví dụ: Jake (Early) khuyên chỉ tập trung đầu phễu. Hai ý kiến cùng có trong kho; kho không cho biết bên nào đúng.
- **Quảng cáo cần chịu lỗ lúc đầu.** Frederick (habit tracker) nhắm hoà vốn ngay giao dịch đầu nhưng vài tuần đầu vẫn chưa có lãi (câu ở bảng): đo P&L không bảo đảm lãi.
- **Attribution thường không chính xác.** Early nói khó đo influencer; Locked dựa vào spike lượt tải; Sizzle ước 10–20% mua hàng đến từ nguồn khác (ước của expert). Đừng cắt kênh vì một con số lẻ.
- **Video của kênh Superwall có lợi ích thương mại.** 20/42 step từ kênh này; hai expert nói trong đó (Dawson điều hành agency UGC, Nick Lawton đồng sáng lập nền tảng UGC) bán dịch vụ UGC.
- **Người đứng ngoài ngách.** 3/26 case full ghi rõ outsider và 9 không nêu; số 3 quá nhỏ.

## Quyết định
- **QUA** nếu có bảng phễu ≥4 bước có số thật, mỗi kênh có nguồn gắn attribution và ≥1 dòng P&L (đề xuất, chưa có số của kho). Dùng bảng để chọn một thứ sửa trong tuần.
- **DỪNG** dựng thêm dashboard nếu phễu có <100 người vào mỗi tuần (đề xuất, chưa có số của kho: kho không nêu cỡ mẫu tối thiểu); lúc đó nói chuyện trực tiếp với từng người dùng sẽ cho nhiều hơn (xem `g1-first-10-users`, `g5-retention`).
- **TEST THÊM** nếu bước rơi rõ nhưng chưa biết vì sao: chạy một A/B ≥14 ngày (đề xuất, chưa có số của kho; Symmetry dùng ít nhất 2 tuần), đổi đúng một thứ.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ bước 1–6, làm từ xa, công cụ có bản chạy cho sản phẩm nhỏ. Bảng tính tay là đủ cho vài chục người dùng đầu.
- **Rào cản thật:** (1) phí và thuế chen vào P&L: phí Apple 15% hoặc 5% (small business), VAT khoảng 20% với khách EU (habit tracker nêu); thuế VAT/GST khi bán web cần kiểm lại theo từng thị trường, kho không nêu cách xử lý từ Việt Nam. (2) cỡ mẫu nhỏ: ít người dùng thì A/B chậm; dùng khoảng thời gian dài hơn hoặc đo thủ công. (3) quy định bảo mật dữ liệu ở EU/UK có thể áp khi cài đo hành vi chi tiết: kho không nêu, cần kiểm riêng trước khi cài. (4) Instagram không cho gắn link riêng (Locked), nên attribution phải bằng spike lượt tải hoặc custom product page (Payout).
- **KHÔNG nên làm** khi chưa có người dùng thật (đo số 0 không dạy gì), hoặc khi mình định bỏ cả kênh vì một con số attribution lẻ: kho cho thấy ngay founder cũng nói khó đo (Early) hoặc ước thô (Sizzle).
