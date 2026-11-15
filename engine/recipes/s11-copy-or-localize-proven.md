---
id: s11-copy-or-localize-proven
strategy: S11
title: "Chép, bản địa hoá hoặc remix một sản phẩm đã chạy (ba biến thể)"
label: manual                  # soi mẫu, đọc review, đếm bản sao bằng tay; agent chỉ giúp liệt kê
time: "2–3 giờ cho một lượt chọn mẫu và chọn biến thể"
cost: "$0 để tìm; chi phí build tuỳ sản phẩm"
evidence: corpus
signal_level_when_pass: 3      # QUA đòi mẫu có doanh thu kiểm được: mức 3 của thang (VALIDATE.md); nhu cầu của KHÁCH MÌNH chưa kiểm
tools: []
status: draft
---

## Dùng khi
Mình không phải người trong ngách (nhánh B của `s5-insider`) và muốn bắt đầu từ thứ đã có người trả tiền thay vì ý tưởng mới. Chọn `s12-timing-shift` thay công thức này nếu cái hấp dẫn là một thay đổi vừa xảy ra, không phải một sản phẩm cụ thể; chọn `s9-niche-narrowing` nếu mình đã có sản phẩm và chỉ muốn thu hẹp.

## Đầu vào
Danh sách 5–10 sản phẩm đã chạy (con số đề xuất, chưa có số của kho) mà mình thấy được (bảng top grossing, podcast, thread X, danh sách đối thủ), mỗi dòng có nguồn.

## Ba biến thể (phân loại tay của người viết theo mô tả step; câu truy vấn ở `engine/recipes/s11-copy-or-localize-proven.extra.sql`)
| Biến thể | Là gì | Số founder (case) | Ví dụ trong kho |
|---|---|---|---|
| A. Chép nguyên mẫu | cùng việc, cùng nhóm khách, khác rất ít | 6 (6) | Boost App Social (đối thủ Hashtag Expert), Papermark (bản open-source thay DocSend), Payout, Glowly, DuckMath, Sunflower |
| B1. Bản địa hoá thị trường/ngôn ngữ | cùng app, đổi nước và ngôn ngữ | 1 (1) | Cal Buddy (Cal AI sang tiếng Hebrew, Israel) |
| B2. Chuyển nền tảng hoặc kênh | cùng ý tưởng, đổi nơi bán | 3 (3) | NGL (sang Instagram), Data Fetcher (từ Google Sheets sang Airtable), Stronger (từ web app sang mobile) |
| C1. Remix đổi ngách, đối tượng, chủ đề | giữ cơ chế, đổi khách | 7 (9) | Glam Up (UMAX nam sang nữ; một founder, hai video), Preycreen (One Sec sang Kitô hữu), Runafy (LiftOff gym sang chạy bộ), Stoppr (Quitter sang thèm đường), Copia, GeoSports, Veed.io, Scanamon (chỉ được nhắc) |
| C2. Làm tốt hơn, đẹp hơn, đơn giản hơn cùng ngách | giữ khách, đổi cách làm | 10 (10) | Gravl, SuperGrow, Signaturely, Letterly, Oceans, Prayer Lock, Shipper, Bible Buddy, habit tracker của Frederick, CutCoach (chỉ lấy bố cục) |

Chỉ **1 founder** làm bản địa hoá đúng nghĩa (đổi thị trường/ngôn ngữ): bằng chứng cho B1 mỏng. Ranh giới giữa A và C2 mờ (Boost App Social và Prayer Lock đều nói "làm tốt hơn"); coi bảng là cách đọc, không phải nhãn của kho.

## Các bước
1. **[manual] Lập danh sách mẫu** (≤15 phút). Nguồn founder trong kho thật sự đi qua: nghe podcast founder kể doanh thu (Cal Buddy, từ founder Cal AI), thấy một app có traction (Boost App Social thấy Hashtag Expert), tải thử một app được nói là kiếm ~100k/tháng (Preycreen với One Sec), thread viral trên X (Stronger, habit tracker), danh sách ý tưởng tài trợ (Payout), top grossing theo ngách (Mal Baron của Prayer Lock khuyên bước một là tìm ngách có app trên 50k/tháng bằng Sensor Tower). Mỗi dòng ghi nguồn.
2. **[manual] Kiểm tiền của mẫu bằng nguồn thứ hai.** Doanh thu mẫu phải kiểm được ngoài lời tự khai: làm theo `VALIDATE.md` cổng 1.1 và `s1-revenue-spy`. Trong kho chỉ 5/28 case full dùng s11 nêu bằng chứng nhu cầu là doanh thu của sản phẩm tương tự; 15/28 không kể bằng chứng nhu cầu nào.
3. **[manual] Chọn biến thể và viết khác biệt một câu.** Hỏi lần lượt: mẫu đã bán ở thị trường/ngôn ngữ của mình chưa (B1); nhóm khách nào chưa được phục vụ bằng cơ chế này (C1); người dùng mẫu ghét gì (C2, dùng `s3-competitor-reviews` và `VALIDATE.md` cổng 2.2). Signaturely đi theo C2: điểm riêng là cái người ta ghét ở công ty lớn nhất.
4. **[manual] Gọi tên đường phân phối của mình** (≤15 phút). Ghi ai đưa sản phẩm tới khách, bằng kênh nào, không tốn tiền. Cal Buddy: lợi thế chỉ có khi khách nội địa chưa biết app gốc. Payout: founder chia cổ phần cho người lo mảng khác để mình lo phân phối. Không gọi được tên thì ghi rõ là rủi ro lớn nhất.
5. **[manual] Đếm số bản sao** đã có trong 6–12 tháng gần nhất (`VALIDATE.md` cổng 2.9). Trong kho có hai app chặn điện thoại tới khi cầu nguyện (Preycreen và Prayer Lock) cùng chạy; không đếm được bản sao nghĩa là chưa biết mình vào đông hay vắng.
6. **Ghi ứng viên** vào `journey/ideas/`: mẫu + nguồn, biến thể, khác biệt một câu, đường phân phối, số bản sao.

## Đầu ra
Mỗi ứng viên một dòng: mẫu + doanh thu kiểm ở đâu · biến thể (A/B1/B2/C1/C2) · khác biệt một câu · đường phân phối · số bản sao đã có · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng của từng tín hiệu nằm ở `VALIDATE.md` (cổng 1.1 tiền ngay cạnh, cổng 2.9 độ đông bản sao). Riêng công thức này: ứng viên chỉ vào chương VALIDATE khi có cả (a) mẫu có doanh thu kiểm được, (b) khác biệt một câu và (c) đường phân phối gọi được tên. Ba điều kiện này là đề xuất, chưa có số của kho.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 32 step trong 31 video |
| Case (video, case) có step này | 29, trong đó 28 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 2/32 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 16/28 |
| Case full không nêu existing_audience | 26/28 |
| Case full video không kể bằng chứng nhu cầu trước launch | 14/28 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 11.0 tháng (5.8–25.5), n=16 |
| Kênh scale trả tiền / thuần organic / không nêu | 13 / 14 / 1 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s11-copy-or-localize-proven.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Trong 28 case full: 15 ghi nguồn ý tưởng là chép/theo trend và 5 ghi là soi doanh thu để chọn. Theo nhóm vị trí ngách (case full): 16 là người trong cuộc, **5 outsider** (tự ghi là đứng ngoài: Glam Up, Copia, Oceans, Stoppr, DuckMath), 7 không nêu. Chỉ 2/32 step là lời khuyên chung chứ không phải việc một case đã làm (Mike và Benji; cả hai là founder nói về cách làm nói chung); phần còn lại là việc founder kể. Số tháng trung vị của từng biến thể quá nhỏ (n=1 đến 6) nên không đọc được; đừng so sánh các biến thể bằng tốc độ.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể (hoặc lời khuyên founder tự nói, ghi rõ ở cột "Dùng cho").

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| David Attias (founder) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-break` · 08:10 | "Fastest way to make some money right now is to do one-to-one copy of a very successful app." | founder khuyên: chép một-một một app đang thắng (Stoppr copy từng màn, đổi màu và nội dung sang ngách đường) |
| Pat Walls (host/expert) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-break` · 08:26 | "I think it's totally okay to copy an app, and actually, I think that's the right thing to do, especially when you're starting out." | lời khuyên của host: chép app là ổn, nhất là khi mới bắt đầu |
| Pat Walls (host/expert) · `2025-10-30_i-vibe-coded-a-12k-month-mobile-app-stoppr-break` · 01:22 | "It is something that I've been hearing about recently, taking kind of proven English or American apps and localizing them to different countries." | lời của host: xu hướng lấy app Anh/Mỹ đã chạy rồi bản địa hoá sang nước khác |
| Tomer (founder) · `2026-08-09_i-copied-a-huge-app-now-i-make-80k-month` · 02:34 | "I realized that it doesn't matter that the app already exists if no one knows about it in my local market." | founder kể (bản địa hoá): app đã có không quan trọng nếu thị trường nội địa chưa ai biết (Cal Buddy, Israel) |
| Tomer (founder) · `2026-08-09_i-copied-a-huge-app-now-i-make-80k-month` · 04:22 | "And if you're going to localize an app for a small market like Israel, the niche has to be huge." | founder kể (bản địa hoá): thị trường nhỏ thì ngách phải rộng; ngược với thu hẹp ngách |
| Mike (founder) · `2025-11-02_i-built-3-saas-apps-to-200k-mrr-heres-my-exact-playb` · 06:02 | "pick an idea that's been done before. New ideas are risky." | lời khuyên (không phải một case kể lại) của founder Mike: chọn ý tưởng đã có người làm vì ý tưởng mới rủi ro |
| Will Cannon (founder) · `2025-10-01_my-two-apps-made-30m` · 01:03 | "I took business models that already had product market fit and I added my own little twist to them." | founder kể (remix cách làm): lấy mô hình đã có product-market fit rồi thêm một điểm riêng (Signaturely) |
| Will Cannon (founder) · `2025-10-01_my-two-apps-made-30m` · 04:23 | "Our twist is what people dislike about the biggest companies in the space because those are the easiest customers to go after and acquire." | founder kể: điểm riêng là chỗ người dùng ghét ở công ty lớn nhất, vì đó là khách dễ lấy nhất |
| Mal Baron (founder) · `2026-01-18_i-built-a-20k-month-mobile-app-heres-my-entire-p` · 03:35 | "and I said, you know what, I can do a better job than them." | founder kể (làm tốt hơn): thấy app cầu nguyện chặn điện thoại đã có và tin mình làm tốt hơn (Prayer Lock) |
| Mal Baron (founder) · `2026-01-18_i-built-a-20k-month-mobile-app-heres-my-entire-p` · 11:59 | "Step four, do not touch your app. Obsess over distribution. I haven't touched my app in over 3 months now." | founder kể: sau khi ra app, bước còn lại là phân phối, không sửa app nữa |
| Joseph Choi (host/expert) · `2025-08-15_my-app-makes-600kyear-using-this-easy-growth-str` · 00:47:00 | "I think distribution is becoming more important than product" | lời của host: phân phối đang quan trọng hơn sản phẩm |
| Casper (founder) · `2026-03-15_the-stupid-simple-content-strategy-thats-making-` · 00:07:38 | "I'd rather partner with someone, give up some equity, and have them handle that whole side while I handle the whole distribution side." | founder kể: chọn chia cổ phần cho người lo mảng khác để mình lo phân phối (Payout) |
| Alex (founder) · `2026-04-26_copy-this-facebook-ads-strategy-itll-blow-up-you` · 00:38:07 | "Don't simply kill your soul copycatting stuff, cloning stuff because I see it many times these days" | bẫy: founder từng chép (Boost App Social) tự cảnh báo đừng chỉ làm nghề sao chép |
| Host (host/expert) · `2025-09-28_he-built-a-simple-120kyr-app-then-sold-it-for-mu` · 00:19:43 | "I feel like a lot of people like they see the big success and they just want to have the same thing" | bẫy (host): nhiều người thấy thành công lớn rồi muốn có đúng thứ đó |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Phản ví dụ nổi tiếng: chép app, đừng chép ngách.** Host Pat Walls (mốc 08:41 trong video của Stoppr) nói nên chép app nhưng không bê cả khách hàng của người ta; tóm tắt cuối video của ông nói David đã đổi ngách và đổi nhóm khách. Câu này đứng cạnh biến thể A trong kho: 6 founder chép nguyên mẫu cùng ngách vẫn lên kênh (Payout, Papermark, Boost App Social). Cả hai phía chỉ là mẫu từ kho người thắng; không có số người chép cùng ngách mà chết.
- **Khác biệt thường nằm ở brand và phân phối, nhưng kho không đo được điều này.** Kho không có cặp "cùng sản phẩm, khác phân phối" kiểm được; Preycreen (120k, tự khai theo năm) và Prayer Lock (21k/tháng, đo được) cùng cơ chế nhưng khác cơ sở tính, và Preycreen có founder đã bán nhiều sản phẩm trước. Cái kho có là lời nói: host nói phân phối đang quan trọng hơn sản phẩm, Mal Baron nói sau khi ra app thì không sửa app nữa mà chỉ lo phân phối.
- **Chỉ có một chân nhu cầu: "người khác đã kiếm được".** 15/28 case không kể bằng chứng nhu cầu; một số làm xong mới biết (GeoSports: không kiểm nhu cầu trước). Doanh thu của mẫu có thể là tự khai hoặc ước tính lệch nhiều lần (xem `VALIDATE.md` cổng 1.1).
- **Alex (Boost App Social) tự cảnh báo** đừng chỉ sống bằng sao chép (bảng). Sunflower: founder nói ban đầu cloned app nhưng chưa làm tốt hơn được.
- **Kho chỉ chứa người thắng.** 26 founder khác nhau (28 case full) dùng s11 và lên được kênh; số người chép mà thất bại không có trong kho.

## Quyết định
- **QUA** nếu có đủ (a)(b)(c) ở Ngưỡng qua và số bản sao ở bước 5 không áp đảo (ngưỡng "áp đảo" do `VALIDATE.md` cổng 2.9 quy định). Sang `VALIDATE.md` cổng 1 và 2.
- **DỪNG** nếu mẫu chỉ có doanh thu tự khai không kiểm được, hoặc khác biệt một câu chỉ là "đẹp hơn" mà không nói đẹp cho ai, hoặc không gọi được tên đường phân phối.
- **TEST THÊM** nếu thiếu một trong ba: trong 3 ngày (đề xuất, chưa có số của kho) kiểm tiền mẫu bằng nguồn thứ hai, hoặc đọc 100+ review của mẫu theo cổng 2.1–2.2.

## Cho solo founder bán global (từ VN)
- **Chép được:** quy trình 6 bước, làm hoàn toàn từ xa. C1 và C2 là hai biến thể đỡ nhất bằng số founder (7 và 10).
- **Rào cản thật:** (1) kho chỉ có một case bản địa hoá và đó là sang Israel, không phải sang thị trường trả cao, nên chưa có số cho "bản địa hoá app Mỹ sang Đức/Pháp/Nhật"; đó là suy luận của người viết, không phải của kho. (2) Chép sát từng màn và từng chữ (như Stoppr nói) có rủi ro bản quyền và điều khoản cửa hàng ứng dụng; kho không kể ai bị gỡ, nhưng cũng chỉ có người thắng. (3) Phân phối: nhiều case có co-founder, mạng lưới hoặc ngân sách quảng cáo; 13/28 có kênh trả tiền, mà ưu tiên của mình là organic. (4) Thu USD cần Stripe/pháp nhân hoặc store payout phù hợp.
- **KHÔNG nên làm** nếu mẫu chỉ có doanh thu tự khai, hoặc nếu bản sao đã đông và mình chỉ có "đẹp hơn" mà không có kênh organic riêng.
