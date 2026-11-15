---
id: g4-pricing-paywall
strategy: G4
title: "Thu tiền: chọn giá và gói, thiết kế paywall và trial, onboarding dẫn tới trả tiền, khuyến mãi, thí nghiệm giá"
label: manual                  # chọn giá, dựng paywall và đọc số bằng tay; công cụ paywall/thanh toán chỉ là chỗ đặt thí nghiệm
time: "2–4 giờ để chọn gói và dựng paywall đầu; thí nghiệm giá chạy nhiều tuần"
cost: "$0 để thiết kế; phí công cụ paywall/thanh toán tuỳ nhà cung cấp (kho không nêu số)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: [superwall, revenuecat, stripe]
status: draft
---

## Dùng khi
Sản phẩm đã dùng được và mình cần quyết bốn việc: **thu tiền theo mô hình nào, giá bao nhiêu, hiện paywall ở đâu, và thử gì trước**. Chạy sau `g1-first-10-users` khi đã có người dùng đầu tiên (mục con A, B có thể làm trước để đặt sơ giá), và trước khi trả tiền cho ads (`g6-paid-ads`). **Không dùng** để biết có nhu cầu hay không: việc đó nằm ở `VALIDATE.md`. Tối ưu paywall khi chưa ai trả tiền chỉ làm đẹp một phễu rỗng.

## Đầu vào
Một sản phẩm dùng được; một câu mô tả ai trả tiền; giá công khai của ≥3 sản phẩm gần nhất (App Store/Play hoặc trang giá web); nơi thu tiền (App Store/Play qua RevenueCat/Superwall, hoặc Stripe trên web); nếu có: số người đã cài/truy cập mỗi tuần.

## Cách chia công thức này (6 mục con)
Công thức lớn (206 step) nên chia theo nội dung step. Mỗi step được xếp vào đúng một nhóm theo từ khoá trên mô tả step (thứ tự ưu tiên D, E, F, C, B, A; xấp xỉ, đọc step để chắc). Câu truy vấn: `engine/recipes/g4-pricing-paywall.extra.sql`, mục (3).

| Mục con | Step | Không gắn case | Kênh Superwall / Starter Story | Case full | Tháng tới mức doanh thu hiện tại (trung vị, n) |
|---|---|---|---|---|---|
| A. Chọn giá và gói | 35 | 2 | 9 / 26 | 29 | 6.0 (n=17) |
| B. Mô hình và thời điểm thu tiền | 41 | 2 | 4 / 37 | 37 | 15.5 (n=24) |
| C. Paywall và trial | 45 | 3 | 24 / 21 | 32 | 16.0 (n=28) |
| D. Onboarding dẫn tới paywall | 38 | 3 | 26 / 12 | 24 | 12.0 (n=11) |
| E. Khuyến mãi, ưu đãi khi thoát | 17 | 5 | 9 / 8 | 10 | 4.0 (n=5) |
| F. Thí nghiệm giá và đo | 30 | 4 | 20 / 10 | 19 | 14.0 (n=17) |

Tổng 206 step. Cột "Không gắn case" là step case_id null (host/expert, hoặc founder không có hồ sơ case). Cột case full chỉ đếm case có ≥1 step trong nhóm, một case có thể nằm ở nhiều nhóm nên cột này cộng lại lớn hơn 120. Cột tháng là mức doanh thu founder đang kể trong video (không phải mốc $1k) và n nhỏ ở E, nên không đọc thành "mục con nào nhanh hơn".

**Mọi số tiền, giá, tỉ lệ chuyển đổi ở dưới là con số founder (hoặc expert) nêu, một case một con số, không phải chuẩn của kho.** Nhiều con số là một lần test, không nêu cỡ mẫu.

## Các bước

### A. Chọn giá và gói (35 step; 29 case full)
1. **[chrome] Ghi giá ≥3 đối thủ gần nhất** (≤15 phút): tên gói, giá tuần/tháng/năm, có trial không. Waitly đặt gói phẳng $100/tháng để đối đầu Yelp và OpenTable (founder nêu hàng trăm $/tháng); Links đặt gói phổ thông thấp hơn Linktree và thêm gói Pro $12 cho khách nhiều trang.
2. **[manual] Chọn khung gói theo loại khách.** App tiêu dùng (iOS/Android): gói năm cộng gói tuần hoặc tháng. Trong 20 dòng giá năm mà founder nêu (xem bảng dưới), mức từ $24.99 (Maxed AI) đến $99.99 (Pingo); giá tuần từ $5 (Go Tall) đến $10 (ToneAdapt) ở 9 dòng. SaaS web B2B: theo tháng hoặc theo số đơn vị dùng (Lancer theo số proposal $79/$300/$500; Hero Analytics theo số client agency; Once theo số khách mời).
3. **[manual] Đặt một gói làm mặc định và giải thích vì sao.** Sunflower đưa gói năm lên mặc định kèm tuỳ chọn trả trước và thêm gói tuần; Pingo đẩy gói năm vì LTV và ARPU cao hơn, giấu gói tháng sau nút xem tất cả gói; Maxed AI chỉ bán gói năm $24.99 vì không muốn sống nhờ người quên huỷ. Canary: 60% người dùng chọn gói năm ($79 so với $10/tháng).
4. **[manual] Ghi lại bằng một dòng: "ai trả, vì sao mức này".** Links chọn nhiều khách trả ít (câu ở bảng); Profit AI đặt $5.000/tháng nhưng ít người mua, hạ xuống $800; Setter AI bán từ khoảng $50/tháng, khách lớn nhất tới $5.000/tháng. Nếu khách là doanh nghiệp, đừng sao khung giá app tiêu dùng.

Giá founder nêu (một case một con số, tự khai; mỗi dòng là một video, nên cùng tên sản phẩm có thể hai giá):

| Gói | Giá founder nêu (USD) |
|---|---|
| Tuần (9 dòng) | Go Tall 5; Locked 7 (hai video cùng nêu 7); Career Hound 7; Halo AI 8.99; GlowUp 9.99; Prayer Lock 9.99; Social Wizard khoảng 10; ToneAdapt 10 |
| Năm (20 dòng) | Maxed AI 24.99; Clear 30: 30 (chốt sau thử 30/40/50); Pushscroll khoảng 30; 3AK 30; Locked 30 và 40 (hai video khác nhau); Go Tall 35; GlowUp 39.99; Coherence 40; Pep AI 40 và 45 (hai video khác nhau); Prayer Lock 49.99; Career Hound 50; FollowBuddy 50; Wrestle AI 59.99; ToneAdapt khoảng 60; Canary 79; Social Wizard khoảng 80; Audio Pen 99; Pingo 99.99 |
| Web B2B, khung giá khác | Subscribr 49–300/tháng; Algrow 25/45/80 (video không nêu đơn vị tiền); GojiBerry đa số khách ở $99; Lancer 79/300/500; Setter AI từ khoảng 50 tới 5.000; Yadaphone một khách enterprise khoảng 1.000/tháng; Oceans 3.000–4.000 mỗi headcount |

Bảng giá này gồm hầu hết app tiêu dùng trên iOS; không dùng để suy ra giá web B2B. Câu truy vấn lấy danh sách: mục (5) của `extra.sql`.

**Quyết định A.** QUA khi đã có bảng ≥3 đối thủ, một khung gói và một gói mặc định ghi rõ lý do. Chưa phải QUA về doanh thu: số người trả ở mức giá đó chỉ biết sau mục F. DỪNG nếu không tìm được ≥3 đối thủ để so (thị trường quá mới hoặc không có ai thu tiền: quay về `VALIDATE.md`).

### B. Mô hình và thời điểm thu tiền (41 step; 37 case full)
1. **[manual] Chọn một trong bốn mô hình và ghi lý do.** Kho có cả bốn: (a) subscription tuần/tháng/năm (đa số app tiêu dùng); (b) lifetime/mua một lần (19 case full nhắc lifetime, trọn đời, LTD, mua một lần); (c) credit hoặc theo usage (9 case nhắc credit, usage hoặc pay-as-you-go: ScrapeCreators gói $10/$50/$500 theo credit, Parakeet AI, Yadaphone prepaid thay vì khoảng $30/tháng của đối thủ, Shipper, Task Magic); (d) retainer, theo đầu người, enterprise (5 case: Skale retainer khoảng $20k/tháng, Vector 3, Oceans, Yadaphone, Papermark).
2. **[manual] Quyết định có gói miễn phí hay không.** 16 case full có step nhắc gói miễn phí hay freemium (một số là nói rõ KHÔNG có gói miễn phí, nên con số này không phải số case freemium). Có gói miễn phí: Youform (nêu khoảng 90% tính năng miễn phí, chuyển đổi trả phí khoảng 1.5 đến dưới 2%), Stagetimer, Audio Pen, Canary. Không có gói miễn phí: Magai, Shipper, Career Hound, PostBridge. CodeGuide không dùng free trial (khác với gói miễn phí). Sync2sheets bỏ hẳn gói miễn phí vì nhiều người chỉ dùng bản free (số liệu sau đó "tăng từ 5K lên 8K", video không nêu đơn vị). Rabbit Holes ra freemium, không có traction, rồi chuyển sang mua một lần chạy desktop.
3. **[manual] Nếu chọn lifetime, ghi giá, giới hạn suất và đường chuyển sang subscription.** Savewise: gói trọn đời từ khách xin, về sau chiếm khoảng 97% doanh thu (founder nêu); Floga ba bậc $109/$199/$349 và không hiện giá trước ngày launch (câu ở bảng); Voicy gói trọn đời khoảng $260 bán tốt; Cat on Chair $29.99 là phần lớn doanh thu; SuperGrow giới hạn 300 suất trong 3 ngày rồi nâng khách lifetime lên subscription; Blog to Pin launch bằng lifetime, rồi chuyển sang subscription và có khách thật trong khoảng một tháng.
4. **[manual] Chọn thời điểm bật thu tiền, ghi lại điều gì gây ra nó.** Kaching Bundles bật khi có review đầu và lên thứ hạng từ khoá; Sheets Resume bật khoảng một tuần sau ra mắt; Packager sau khi sửa lỗi beta; ChartDB khi người dùng hỏi cộng tác nhóm; Fastlane bán bản beta trả phí trước launch (founder nêu khoảng 16k ARR); Waitly khoảng hai năm mới bật in-app purchase; Flame bật thu tiền vì hết tiền.
5. **[chrome] Nếu bán qua web, dựng cổng thu tiền trước khi launch** (Stripe nếu mở được cho mình, nếu không thì merchant-of-record như Polar, Lemon Squeezy, Paddle; xem `VALIDATE.md` mục rào cản VN). 6 case full có step nhắc Stripe hoặc web app (Chatbase thu qua nút Stripe trên web; Sprout thu qua Stripe thay vì App Store; ToneAdapt bán cả web lẫn app; Excel Exercises, PostBridge, Rabbit Holes chỉ nhắc là web). Kho không có số so sánh doanh thu web với store: không nêu lợi hay hại.

Hai hướng ngược nhau cùng có trong kho: Visualizee và Cardstock bỏ mua một lần để sang subscription vì doanh thu lặp lại và tăng sau đó (founder nêu); Savewise, Floga, Voicy sống bằng lifetime. Host Pat Walls khuyên bootstrap đừng bắt đầu bằng subscription (câu ở bảng); Avneesh (Savewise) nói người dùng ghét subscription.

**Quyết định B.** QUA khi có mô hình, giá và ngày bật thu tiền ghi trên một dòng. DỪNG mô hình freemium nếu 30 ngày sau ra mắt vẫn không ai trả (đề xuất, chưa có số của kho; Rabbit Holes và Sync2sheets là hai case đã bỏ gói miễn phí hoặc đổi mô hình). TEST THÊM: nếu chưa ai trả sau khi bật, đổi một thứ (giá hoặc mô hình), không đổi cả hai.

### C. Paywall và trial (45 step; 32 case full)
1. **[manual] Chọn kiểu chặn: cứng (không cho vào), mềm (đóng được) hay chặn theo hành động.** 16 case full nhắc hard paywall hoặc không có gói miễn phí. Gravl đặt paywall cứng trước khi người dùng thấy sản phẩm; Pushscroll cứng, khoảng 300k lượt tải và khoảng 4.000 người trả ở khoảng $30/năm (founder nêu, tức khoảng 1,3%); Stronger chuyển sang hard paywall bắt đầu trial mới dùng phần miễn phí (founder nêu doanh thu tăng khoảng 25% sau một đêm, sau lỗi bật paywall); Halo AI dùng hai paywall, một đóng được ở onboarding và một chặn khi bấm gửi prompt, mỗi cái 16.5% và kết hợp cao hơn một cái.
2. **[manual] Đặt điểm chặn sau khoảnh khắc người dùng thấy giá trị, không phải trước.** Coconote đặt paywall sau khi người dùng ghi âm trọn bài giảng (founder nêu là bước thắng lớn) và chuyển đăng nhập xuống sau paywall; Sprout chỉ hiện paywall khi người dùng vuốt phải; YourMove chờ khoảng 6 tháng mới thu tiền, soft paywall cho sản phẩm chính và hard cho ảnh AI.
3. **[manual] Chọn trial hay không và độ dài.** 30 case full nhắc trial. Độ dài founder nêu: 3 ngày (Clear 30, Pep AI, Coherence, Locked), 7 ngày (PostBridge, Momego, Visualizee), 14 ngày (Tech Lockdown), 30 ngày (Hero Analytics, Profit AI). Push Scroll test 3 so với 7 ngày: 7 ngày đưa nhiều người vào app hơn rõ rệt; Pingo: ở Mỹ chuyển đổi gần như bằng nhau, quốc tế 7 ngày cao hơn khoảng 2%.
4. **[manual] Thêm nhắc trước khi hết trial.** Sunflower: doanh thu +48% (video có chỗ nói 56%) sau khi thêm nhắc; Pingo test nhắc trước 1 ngày so với 2 ngày. Đây là con số tự khai; hai video của một founder có thể lệch nhau.
5. **[manual] Đừng sao copy paywall từ app khác khi nền tảng khác.** Expert (kênh Superwall) kể template SwiftUI giống giao diện iOS thắng bản custom; video app kèm review thắng danh sách tính năng; hai lời expert nói trên iOS và Android cho kết quả ngược nhau (Used: iOS thích review, Android cần danh sách tính năng). Tất cả đến từ expert, không phải founder.

Phản ví dụ về hard paywall: Lovely chuyển từ paywall cứng sang freemium vì nhiều review xấu; Fitted đang hard paywall nhưng định làm app miễn phí hoàn toàn; Preycreen bỏ paywall, dùng bản miễn phí có quảng cáo (khoảng 5 cent/người dùng/ngày, hoàn vốn quảng cáo khoảng 14–15 ngày, founder nêu). Expert Steve Young coi hard paywall là phép thử product-market fit (câu ở bảng): lời khuyên, không phải số của kho. Peter (Stronger) nói lý do chuyển cứng ngắn gọn (câu ở bảng). Expert Jonathan Parra (Superwall) nói có app người dùng trả ở gói tuần nhiều hơn gói năm (câu ở bảng): chỉ là quan sát của một expert.

**Quyết định C.** QUA khi paywall hiện ra ở đúng một điểm đã chọn và đo được ba con số: người thấy paywall, người bắt đầu trial, người trả. DỪNG kiểu chặn cứng nếu review tụt hoặc người dùng không quay lại (Lovely). TEST THÊM: đổi một biến mỗi thí nghiệm (độ dài trial hoặc điểm chặn), xem mục F.

### D. Onboarding dẫn tới paywall (38 step; 24 case full)
1. **[chrome] Xem 3 onboarding của app thành công cùng nhóm khách** (≤15 phút mỗi app, chụp từng màn). Founder trong kho làm đúng việc này: Wrestle AI học onboarding của các app đang convert cao, Stoppr sao gần nguyên xi một onboarding rồi đổi sang ngách đường, Clear 30 làm lại onboarding sau khi học từ một app lớn.
2. **[manual] Viết luồng: câu hỏi nỗi đau, kết quả cá nhân hoá, rồi paywall.** Wrestle AI hỏi nỗi đau, dựng chương trình riêng rồi mới paywall; Sway AI hỏi câu cá nhân hoá và cho xem kết quả mơ ước; Savvy Nomad hiện mức thuế tiết kiệm dự kiến trước khi bán gói; DBLI cho quét mặt trước paywall.
3. **[manual] Quyết định dài hay ngắn.** Dài: Prayer Lock nâng onboarding từ khoảng 5 lên 15 phút (founder nêu tỉ lệ chuyển đổi tự nhiên tăng hơn 3 lần); Coconote từ khoảng 5 lên khoảng 13 màn; Go Tall onboarding rất dài và paywall hiện cho khoảng 91% người dùng; Glowly 12–15 bước. Ngắn theo nhóm: Pep AI cho người dưới 25 tuổi onboarding ngắn hơn. Clear 30 nói phần lớn người dùng quyết định trả tiền trong 5 phút đầu (câu ở bảng); Connor (Payout) nói đa số người dùng chỉ thấy onboarding nếu app có phần bị khoá (câu ở bảng).
4. **[manual] Đo "tỉ lệ tới paywall".** Copia: từ 50–60% lên 85–90% sau khi thêm onboarding (founder nêu); Push Scroll: khoảng 7% lên 16% với onboarding hội thoại (lời founder). Đây là tỉ lệ hiện paywall, không phải tỉ lệ trả tiền.

Phản ví dụ: Clear 30 thử quiz, founder nói chưa hiệu quả với họ lúc đó; Celebs (expert nêu) bỏ paywall cuối onboarding để đưa người dùng tới điểm hấp dẫn sớm hơn và doanh thu trên người dùng tăng; stealth app (Superwall) thử bỏ trang chủ, hard paywall ngay sau onboarding, conversion tăng khoảng 50% trong một lần test không nêu cỡ mẫu. Host Joseph Choi (đoạn host_essay) nói phải giữ tiếp lời hứa của video khi người dùng mở app (câu ở bảng) và quiz phải nối tới kết quả riêng của từng người; host này bán buổi Zoom và dịch vụ agency, nên đọc như lời khuyên có lợi ích.

**Quyết định D.** QUA khi luồng có câu hỏi nỗi đau, kết quả cá nhân hoá, paywall và đo được tỉ lệ người đến paywall. DỪNG thêm màn nếu tỉ lệ bỏ giữa chừng tăng (đề xuất, chưa có số của kho: kho không nêu ngưỡng bỏ giữa chừng). TEST THÊM: so một bản dài với một bản ngắn trên cùng nguồn người dùng.

### E. Khuyến mãi, ưu đãi khi thoát, winback (17 step; 10 case full; 5 step của expert)
1. **[manual] Chọn một ưu đãi khi người dùng đóng paywall.** Glam Up hiện paywall giảm 50% (khoảng 4,49–6,49 USD mỗi tuần) ngay sau khi bấm thoát; Locked hiện ưu đãi $20/năm so với $40/năm; Momego tặng 1 tuần Pro khi đóng paywall. Expert kể one-time offer giảm gói năm khoảng 25–33% tuỳ app.
2. **[manual] Chỉ giảm gói năm.** Lời expert Vahe (câu ở bảng): không giảm gói tuần hay tháng; giảm gói năm có trial khoảng 80%, không trial khoảng 90% (ví dụ của expert). Lời expert, không phải việc founder làm.
3. **[manual] Dùng khan hiếm có hạn cho lần launch.** Cleo giới hạn 500 suất giảm 50% trọn đời; SuperGrow giới hạn 300 suất trong 3 ngày rồi nâng lifetime lên subscription; Runafy gửi mã nửa giá cho waitlist, phần lớn doanh thu ngày launch đến từ đó; Voicy giảm 20% cho người khuyết tật qua email.
4. **[manual] Thử một chiêu mượn từ e-commerce, coi như thí nghiệm nhỏ.** Cal AI hiện vòng quay giảm giá (expert nêu A/B test cho conversion tăng hai chữ số, không nêu số); Quitter hiện nhãn giảm 60% và số chỗ giới hạn (expert nêu).

Phần khuyến mãi trong kho mỏng và nghiêng về lời expert: 5/17 step là lời expert, và 9/17 step đến từ video kênh Superwall. Khuyến mãi sau khi người dùng đã huỷ gói (winback) thuộc `g5-retention`, không nằm ở đây.

**Quyết định E.** QUA khi có một ưu đãi hiện ở một điểm duy nhất và đo được tỉ lệ nhận. DỪNG nếu ưu đãi làm gói không giảm bị bỏ trống (người trả giá đầy chuyển sang đợi giảm; kho không có số, đây là rủi ro hợp lý, chưa phải số của kho). TEST THÊM: giảm một mức trong 14 ngày (đề xuất, chưa có số của kho) rồi so doanh thu mỗi người thấy paywall.

### F. Thí nghiệm giá và đo (30 step; 19 case full)
1. **[chrome] Cài công cụ đo trước khi đổi gì.** Kho nêu: Superwall (3 step ở kênh Superwall, 3 ở Starter Story), RevenueCat (CardStock), xuất thanh toán Stripe ra bảng tính (Excel Exercises). Không có công cụ nào là bắt buộc.
2. **[manual] Đổi một biến mỗi lần, theo thứ tự thiết kế rồi giá.** Momego, Pingo, ToneAdapt, Push Scroll và Symmetry là các case nhắc A/B test paywall hoặc giá; Momego làm khoảng 10 thử nghiệm trong 2–3 tháng, chuyển đổi từ 0.5% lên 8%, doanh thu khoảng 8K lên hơn 30K mỗi tháng (founder nêu). Habit tracker (không nêu tên) test paywall trước rồi mới tới giá. Host Joseph Choi nói (step của kho, không trích) nên làm phễu nhất quán rồi mới test giá và các lựa chọn.
3. **[manual] Thử giá theo hướng cụ thể.** Excel Exercises: LTV:CAC trung bình ~3:1 nhưng gói tháng hoà vốn sau 4–5 tháng, nên tăng gấp đôi giá tháng và giữ giá năm, tăng trưởng bật lên (founder nêu). Links: tăng $4 lên $5 (founder nêu mỗi $1 tăng thêm gần $5.000 MRR). Stealth app: tăng 20% gói tháng và năm, conversion và doanh thu mỗi lượt tải đều tăng, đang thử thêm 20%. Clear 30 thử $30, $40, $50 một năm rồi chốt $30. Harpagia (game): người chơi chấp nhận $4.99–$9.99, trên $9.99 khó chuyển đổi. Hai hướng ngược nhau đều ghi doanh thu tăng: Sunflower hạ giá vì người dùng nhạy giá và doanh thu tăng.
4. **[manual] Ghi nhật ký thí nghiệm:** ngày, biến đổi, số người thấy paywall, số trial, số trả, cỡ mẫu. Phần lớn số trong kho không nêu cỡ mẫu (Momego, stealth app, Steve), nên đừng sao kết quả của người khác thành kỳ vọng.
5. **[manual] Nối với đo phễu.** Từ view → cài → trial → trả là việc của `g8-funnel-measurement`.

Hai đoạn expert đáng đọc kèm cảnh báo: Jonathan Parra (từng làm designer cho Superwall) nói thiết kế và đóng gói giá là một trong những đòn bẩy lớn nhất khi thử paywall (câu ở bảng); và host Joseph Choi nói trong ba video rằng các app kiếm nhiều nhất đều chạy A/B. Cả hai nói trong video của kênh bán công cụ A/B.

**Quyết định F.** QUA một thí nghiệm khi có phiên bản thắng được ghi cùng cỡ mẫu và thời gian chạy. DỪNG thí nghiệm giá nếu lưu lượng không đủ để phân biệt hai bản (đề xuất, chưa có số của kho: kho không nêu cỡ mẫu tối thiểu; expert Vahe nói bỏ free trial cần lượng người dùng lớn). TEST THÊM: nếu ít người dùng, đổi theo thời gian (hai tuần mỗi bản) thay vì chia ngẫu nhiên, ghi rõ là yếu hơn.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): một trang "bảng thu tiền" gồm: mô hình + giá từng gói + gói mặc định (A, B); kiểu paywall + điểm chặn + độ dài trial (C); tỉ lệ người thấy paywall, bắt đầu trial, trả tiền (C, D); danh sách thí nghiệm đã chạy kèm cỡ mẫu và kết quả (F). Đầu vào của `g8-funnel-measurement`.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau khi bật thu tiền, có ≥1 giao dịch trả tiền của người ngoài vòng bạn bè trong 14 ngày, và đo được ba tỉ lệ (thấy paywall, bắt đầu trial, trả). Nếu mục tiêu là xác nhận có người trả tiền cho ý tưởng, quay về `VALIDATE.md` (cổng 1–4, thang 0–8) chứ không dùng công thức này.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 206 step trong 128 video |
| Case (video, case) có step này | 136, trong đó 120 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 19/206 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 73/120 |
| Case full không nêu existing_audience | 102/120 |
| Case full video không kể bằng chứng nhu cầu trước launch | 56/120 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 11.0 tháng (5.0–24.0), n=76 |
| Kênh scale trả tiền / thuần organic / không nêu | 46 / 63 / 11 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g4-pricing-paywall.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Mục con (câu truy vấn: `engine/recipes/g4-pricing-paywall.extra.sql`): trong 120 case full, theo `community_insider` có 77 người trong cuộc, 17 **outsider** (tự ghi đứng ngoài), 26 **không nêu** (null); đừng gộp 17 và 26. Mốc 10k MRR có số ở 7 case full dùng g4 (Launch Fast và 3AK khoảng 1 tháng, Magai, Yadaphone và habit tracker 3 tháng, Lancer 4, Stoppr 6; tự khai); kho không ghi mốc $1k ở case nào nên không có số cho mục tiêu đó. Công thức này dựa chủ yếu vào việc founder đã làm (19/206 step không gắn case: 16 là lời expert hoặc host ở kênh Superwall, 3 nằm trong video founder của Starter Story) nhưng có **thiên lệch theo kênh**: 92 step đến từ video kênh Superwall và 114 từ Starter Story; ở mục C, D, F phần lớn step đến từ video Superwall (24/45, 26/38, 20/30), còn mục A và B chủ yếu đến từ Starter Story (26/35, 37/41). Case full ở Superwall gần như chỉ là app di động (27/29) trong khi Starter Story rộng hơn (37/91 là di động hoặc iOS, 54 loại khác như web app, API, agency): kết luận về paywall và onboarding vì vậy chủ yếu là kinh nghiệm app tiêu dùng trên điện thoại.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các số khác trong công thức này lấy từ step trong kho, không trích nguyên văn.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Morrie (Pingo) (founder) · `2026-04-19_how-i-built-a-500kmo-ai-app-so-you-can-just-copy` · 00:46:33 | "We really push the annual plan. Like you just higher LTV, higher ARPU." | founder kể: đẩy gói năm vì LTV và ARPU cao hơn (mục con A) |
| Kobe (Sunflower) (founder) · `2026-03-23_i-speedran-an-ai-app-from-0-to-1myr-in-10-months` · 00:44:16 | "put the thing you want them to do as the default option." | founder kể: đặt điều mình muốn người dùng chọn làm mặc định, gói năm (mục con A) |
| Charlie (Links) (founder) · `2026-10-21_quit-job-micro-saas-30k` · 08:51 | "I would much rather have lots of customers paying like a small amount than fewer customers paying more." | founder kể: chọn giá thấp để nhiều khách trả ít hơn là ít khách trả nhiều (mục con A) |
| Avneesh (Savewise) (founder) · `2025-08-09_how-i-used-reddit-to-build-a-25k-month-business` · 11:25 | "I learned consumers hate subscriptions" | founder kể: lý do chuyển hướng bán gói trọn đời, khách ghét subscription (mục con B) |
| Umberto (Floga) (founder) · `2026-03-29_my-app-made-120k-in-24-hours` · 10:16 | "I never ever show the price of the product before the the day of launch because otherwise people are going to make the purchase decision based on price." | founder kể: không hiện giá trước ngày launch lifetime để người ta không quyết theo giá (mục con B) |
| Pat Walls (host/expert) · `2025-10-08_my-app-failed-then-i-changed-one-thing-and-made-` · 00:30 | "I would not recommend starting with a subscription model if you're bootstrapping." | lời khuyên của host: bootstrap thì đừng bắt đầu bằng subscription (mục con B, phản ví dụ cho paywall subscription) |
| Peter (Stronger) (founder) · `2025-08-15_my-app-makes-600kyear-using-this-easy-growth-str` · 00:24:12 | "if you can give people an excuse to not pay, they won't" | founder kể: lý do chuyển sang hard paywall (mục con C) |
| Steve Young (host/expert) · `2026-07-19_beginners-guide-to-buying-selling-apps-2026` · 00:29:15 | "And there's no better way to force a product market fit test than doing a hard pay wall. That means no X." | lời khuyên của expert: hard paywall như một phép thử product-market fit (mục con C) |
| Jonathan Parra (host/expert) · `2026-02-08_i-made-4000-app-paywalls-and-learned-this` · 00:12:57 | "a lot of the time weekly, you know, our users will pay more in the weekly plan than if they would have just paid for the annual plan." | lời khuyên của expert (Superwall): có app người dùng trả ở gói tuần nhiều hơn so với gói năm (mục con C) |
| Clear 30 (founder) · `2025-08-28_i-built-a-30kmo-app-that-helps-you-quit-smoking` · 00:09:07 | "85% of users decide if they're going to pay for your app in the first 5 minutes." | founder kể: phần lớn người dùng quyết định trả tiền trong 5 phút đầu, nên onboarding là việc chính (mục con D) |
| Connor Burd (Payout) (founder) · `2025-10-26_i-vibe-coded-a-20k-month-mobile-app-in-14-days` · 03:40 | "Realistically, 90% of users will probably only ever see your onboarding if you have a paywalled section in your app." | founder kể: đa số người dùng chỉ thấy onboarding nếu có phần bị khoá sau paywall (mục con D) |
| Vahe Baghdasaryan (host/expert) · `2025-11-16_our-no-code-apps-made-50m-using-this-paywall` · 00:34:17 | "You should discount only an annual product. Don't discount weekly. Don't discount monthly. It doesn't work." | lời khuyên của expert: chỉ giảm giá gói năm, không giảm gói tuần hoặc tháng (mục con E) |
| Jonathan Parra (host/expert) · `2026-02-08_i-made-4000-app-paywalls-and-learned-this` · 00:01:05 | "Price and packaging design is one of the biggest levers that you can pull for payw wall experimentation." | lời khuyên của expert (Superwall): thiết kế và đóng gói giá là đòn bẩy lớn khi thử paywall (mục con F) |
| Joseph Choi (host/expert) · `2026-10-08_500m-downloads-psychology` · 00:07:51 | "If somebody downloads because your video promised them a particular result, keep that promise going when they open the app." | lời khuyên của host: giữ lời hứa của video khi người dùng mở app, trước khi tối ưu paywall (mục con D) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Phần lớn step về paywall đến từ kênh có lợi ích thương mại.** Superwall bán công cụ paywall và A/B test: 92 trong 206 step (45%) đến từ 36 video của kênh này, so với 114 step từ 92 video Starter Story (Starter Story cũng có lợi ích riêng: bán chương trình Starter Story Build theo trường bias của kho). Trong 92 step Superwall có 16 step chỉ host/expert (11 từ expert_talk, 5 từ host_essay); phần founder kể (57 step, 29 case full) cũng nằm trong podcast do Superwall tài trợ, với host bán cộng đồng Consumer Club, nên là câu chuyện thành công được chọn. Starter Story: 3 step không gắn case, nằm trong video founder (đọc như việc founder kể, không phải lời host). Đọc mọi con số "tăng conversion" như lời tự khai trong một nền tảng khuyến khích test paywall.
- **Con số tiền không phải chuẩn.** Giá ở mục A là con số một founder nêu cho một app trong một thời điểm. Hai video khác nhau của cùng tên (Locked, Pep AI) nêu hai giá khác nhau. Giá tuần $5–$10 là của app tiêu dùng iOS; không áp cho SaaS web.
- **Kho chỉ chứa người thắng.** 120 case full dùng g4 đều đủ thành công để lên kênh; không có founder đặt cùng mức giá mà không ai trả. Số 4.000 người trả trên 300k lượt tải của Pushscroll chỉ cho biết một kết quả, không cho biết xác suất.
- **Tăng và giảm giá đều ghi tăng doanh thu.** Stealth app tăng 20% và thấy conversion tăng; Sunflower hạ giá và thấy doanh thu tăng; Profit AI hạ từ $5.000 xuống $800 vì ít người mua. Không có hướng đúng chung: nó phụ thuộc phân khúc khách và không có cỡ mẫu.
- **Hard paywall có phản ví dụ.** Lovely quay lại freemium vì review xấu; Fitted định bỏ chặn; Celebs bỏ paywall cuối onboarding. Pushscroll cứng nhưng khoảng 1,3% trả.
- **Lifetime và subscription cãi nhau trong kho.** Savewise khoảng 97% doanh thu từ lifetime; Visualizee và Cardstock bỏ mua một lần sang subscription và thấy doanh thu tăng. Host Pat Walls khuyên đừng bắt đầu bằng subscription khi bootstrap; Visualizee là một founder làm ngược lại.
- **Số "chuyển đổi tăng" ở onboarding không so được với nhau.** Có cái đo tỉ lệ hiện paywall (Copia, Push Scroll), có cái đo chuyển đổi tự nhiên (Prayer Lock), có cái là một lần test (stealth app); không có cái nào nêu cỡ mẫu.
- **Người đứng ngoài ngách.** 16/120 case full tự ghi outsider và 26 không nêu; số 16 quá nhỏ để rút quy luật riêng cho người đứng ngoài.

## Quyết định
- **QUA** nếu sau khi bật thu tiền và đo ba tỉ lệ (thấy paywall, bắt đầu trial, trả), có ≥1 giao dịch của người ngoài vòng bạn bè trong 14 ngày (đề xuất, chưa có số của kho). Ghi bảng thu tiền vào nhật ký; tiếp tục F để cải thiện.
- **DỪNG** nếu có người đến paywall (đề xuất: ≥100 người thấy paywall, chưa có số của kho) mà 0 người trả: sản phẩm hoặc nhóm khách có vấn đề, quay về `VALIDATE.md` thay vì đổi giá tiếp.
- **TEST THÊM** nếu có người trả nhưng ít: đổi một biến (điểm chặn hoặc độ dài trial hoặc giá), chạy 14 ngày (đề xuất, chưa có số của kho), ghi cỡ mẫu.

## Cho solo founder bán global (từ VN)
- **Chép được:** toàn bộ thiết kế gói, paywall, onboarding và nhật ký thí nghiệm; làm từ xa, không cần vốn lớn. Giá bằng USD theo mức thị trường Mỹ/EU; NGL đặt giá tuần theo GDP bình quân từng vùng (founder nêu), expert Sizzle AI test paywall theo từng quốc gia. Với mục tiêu bán giá cao, đặt giá cho khách Mỹ/EU rồi mới thử vùng khác.
- **Rào cản thật:** (1) **thanh toán và pháp nhân**: bán qua App Store/Play thì tiền đi qua Apple/Google nhưng cần tài khoản nhà phát triển và thông tin thuế; bán qua web cần cổng thu tiền: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ (kho chỉ nêu founder dùng Stripe, không nêu nơi đặt pháp nhân). (2) **lưu lượng**: thí nghiệm A/B cần nhiều người dùng; solo mới ra mắt ít người thì thí nghiệm chậm (expert nói bỏ trial cần lượng lớn). (3) **tiếng Anh bản xứ** cho copy paywall và onboarding: kho cho thấy copy là một biến thắng thua. (4) Kho thiên về app tiêu dùng điện thoại; nếu bán web B2B, dùng mục A (khung B2B), B và F, ít dùng C, D.
- **KHÔNG nên làm** khi chưa có ai dùng sản phẩm (làm g1 trước), khi cả luồng chưa đo được số người thấy paywall, hoặc khi định sao nguyên giá và con số chuyển đổi của app khác mà không kiểm cùng nền tảng và nhóm khách. Cũng đừng coi khuyến nghị trong video của kênh bán công cụ A/B là thứ phải mua công cụ đó mới làm được.
