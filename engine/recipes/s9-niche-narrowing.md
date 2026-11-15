---
id: s9-niche-narrowing
strategy: S9
title: "Thu hẹp ngách, hoặc mở sang nhóm khách kề của thứ đã chạy"
label: manual                  # liệt kê nhóm con, đọc App Store/review, ước cỡ bằng tay
time: "2 giờ cho một ngách rộng; mở sang kề: 1 giờ"
cost: "$0"
evidence: corpus
signal_level_when_pass: 3      # QUA đòi có sản phẩm trả tiền kiểm được trong nhóm con hoặc nhóm kề: mức 3 của thang (VALIDATE.md); nhu cầu của khách mình chưa kiểm
tools: []
status: draft
---

## Dùng khi
Mình đã nghiêng về một ngách rộng (fitness, hẹn hò, học tập, AI) nhưng quá đông, hoặc đã có một sản phẩm chạy và muốn một bước tiếp theo. Nếu cái chọn là một sản phẩm cụ thể để chép hoặc remix thì dùng `s11-copy-or-localize-proven`; nếu cái chọn là một thay đổi mới thì dùng `s12-timing-shift`.

## Đầu vào
Hoặc một ngách rộng mình muốn vào (nhánh T), hoặc một sản phẩm đang có người dùng/doanh thu (nhánh M).

## Hai nhánh (phân loại tay của người viết theo mô tả step; câu truy vấn ở `engine/recipes/s9-niche-narrowing.extra.sql`)
| Nhánh | Là gì | Số founder (case) | Ví dụ trong kho |
|---|---|---|---|
| T. Thu hẹp, chọn khe hẹp | vào một nhóm con, một kịch bản, hoặc một nhóm khách mà đối thủ lớn bỏ qua | 13 (13) | Wrestle AI (người dùng cứ hỏi có làm cho đấu vật không), 3AK, Coconote, Packager, Visualizee, Pep AI, Flame, Local Rank, Boot.dev, Attention Design, Hero Analytics, Alia, Bro |
| M. Mở sang kề của thứ đã chạy | cùng khách khác sản phẩm, hoặc cùng sản phẩm khác nhóm khách | 5 (7, gồm 2 case chỉ được nhắc) | Sprout (rời beauty sang sinh viên), SiteGPT (từ khách của Feather), MagicSlides (Sheets sang Slides sang Forms), Task Magic với Mail Lead và LeadQuest, Scanemon |

## Các bước
1. **[manual] Liệt kê nhóm con** (≤15 phút): với ngách rộng, viết 3 cách cắt (theo nghề, theo giai đoạn đời, theo một kịch bản cụ thể). Founder trong kho cắt kiểu này: Pep AI chọn peptide khi app cho GLP đã có; Flame chọn giai đoạn sau khi đã yêu khi thị trường hẹn hò đã đông; Visualizee chọn kiến trúc sư và nhà thiết kế nội thất thay vì một món AI chung; Boot.dev chọn học back-end khi học online đẩy người ta sang front-end; Bro chọn nhắn tin làm kịch bản đầu tiên.
2. **[manual] Tìm khe có bằng chứng nhìn thấy** (≤15 phút). Coconote thấy App Store gần như không có app AI học cho sinh viên trong khi các note-taker nhắm chuyên gia; Packager bỏ khách mà đối thủ lớn đang chạy theo để chọn doanh nghiệp nhỏ. Việc làm: mở App Store/Google/Product Hunt, tìm nhóm con, ghi 3 sản phẩm gần nhất và nhóm khách của từng cái (dùng `s3-competitor-reviews` nếu cần).
3. **[manual] Hỏi người dùng đã có** (nhánh M hoặc khi đã có chút người dùng). Wrestle AI ra đời vì người dùng của Fight AI hỏi nhiều lần. Nếu chưa có người dùng thì thay bằng `s4-tiktok-comment-mining` hoặc `s3-reddit-pain-mining` để thấy ai hỏi nhóm con.
4. **[manual] Kiểm tiền ngay cạnh và cỡ ngách.** Có sản phẩm trả tiền trong nhóm con hoặc nhóm kề không, doanh thu kiểm ở đâu (`VALIDATE.md` cổng 1.1)? Ngách có vừa cỡ không (`VALIDATE.md` cổng 1.5)? Hero Analytics chọn bán cho agency vì mỗi agency mang theo 10–30 brand: đó là cách nâng cỡ khi ngách hẹp.
5. **[manual] Gọi tên đường organic tới nhóm hẹp.** 3AK đặt app vào nơi người điền kinh đã có ảnh hưởng; Local Rank nói ngách hẹp giúp được nhìn như người dẫn đầu. Không gọi được tên đường tới họ thì ghi là rủi ro.
6. **[manual] Nhánh M: chọn bước kề có khách chung.** SiteGPT lấy khách đã có của Feather; Sprout đổi sang nhóm có sức mua cao hơn; MagicSlides đi tiếp theo nền tảng đã có (Sheets, Slides, Forms). Việc làm: liệt kê 3 nhóm kề, mỗi nhóm ghi "khách của mình có hỏi chưa".
7. **Ghi ứng viên** vào `journey/ideas/`: nhóm con, khe nhìn thấy, tiền kiểm ở đâu, cỡ ngách, đường organic.

## Đầu ra
Mỗi ứng viên một dòng: nhóm con (và ngách rộng cha) · khe + link bằng chứng · sản phẩm trả tiền kiểm được · ước cỡ ngách · đường organic · mức tín hiệu 0–8.

## Ngưỡng qua
Ngưỡng của từng tín hiệu nằm ở `VALIDATE.md` (cổng 1.1, 1.3, 1.5). Riêng công thức này: ứng viên vào chương VALIDATE khi có cả (a) khe gọi tên bằng bằng chứng nhìn thấy, (b) ít nhất một sản phẩm trả tiền kiểm được ở nhóm con hoặc nhóm kề, (c) qua cổng 1.5 về cỡ. Ba điều kiện này là đề xuất, chưa có số của kho.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 30 step trong 24 video |
| Case (video, case) có step này | 20, trong đó 18 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 9/30 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 10/18 |
| Case full không nêu existing_audience | 15/18 |
| Case full video không kể bằng chứng nhu cầu trước launch | 13/18 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 12.0 tháng (7.0–27.5), n=11 |
| Kênh scale trả tiền / thuần organic / không nêu | 3 / 11 / 4 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/s9-niche-narrowing.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Trong 18 case full: 6 ghi nguồn ý tưởng là thu hẹp ngách và 6 là mở sang ngách kề; 8 là người trong cuộc, **3 outsider** (tự ghi là đứng ngoài: SiteGPT, Pep AI, Flame), 7 không nêu. 7/18 từng nêu thất bại trước đó. **9/30 step không gắn case nào**: Canyon (4), Steve Young (1), Steph France (1) là expert, và 3 step từ video founder nói về cách làm nói chung (Adrian, Lots, Florin Pop). Con số founder thật sự làm là 13 (nhánh T) và 5 (nhánh M).

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Phần lớn câu nói về ngách siêu hẹp trong bảng là của expert.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Christian hoặc Braylin (founder) · `2026-06-28_how-we-built-this-20k-month-ai-app` · 04:57 | "What we did is we found a niche that not a lot of people were in." | founder kể (3AK, app điền kinh): chọn một ngách ít người đang làm |
| Pat Walls (host/expert) · `2026-06-28_how-we-built-this-20k-month-ai-app` · 08:05 | "If you have any specialty in anything, whether it's tennis, pickleball, whatever you can build a niche app like you guys built." | lời khuyên của host: có chuyên môn ở môn nào thì làm app ngách cho môn đó |
| Thomas (founder) · `2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-th` · 06:00 | "Step three is to avoid competing with the masses." | founder kể (Packager): bước ba trong quy trình của anh là tránh cạnh tranh với số đông; anh bỏ khách triệu thiết bị để chọn doanh nghiệp nhỏ |
| Zach (founder) · `2026-06-10_i-built-a-1m-saas-in-a-hidden-niche` · 05:28 | "Each of the agencies have 10, 20, 30 brands as customers. And so in effect, I'm getting 30 brands onto the platform by going through one agency." | founder kể (Hero Analytics): bán cho agency để một khách mang theo 10-30 brand |
| Pat Walls (host/expert) · `2026-06-10_i-built-a-1m-saas-in-a-hidden-niche` · 12:58 | "focus on unsexy niches, especially if you're doing something in B2B like this." | lời khuyên của host: làm ngách ít hấp dẫn, nhất là B2B |
| Jacky (founder) · `2026-03-22_i-make-250k-month-from-13-businesses-after-losin` · 06:33 | "Narrow is better. People will see you as like a thought leader." | founder kể (Local Rank): ngách hẹp giúp được nhìn như người dẫn đầu |
| Shaan Arora (founder) · `2025-08-27_how-i-built-a-4m-business-simple-strategy` · 03:19 | "We realized that we're actually not an education tool. We're not a loyalty tool. We're a pop-up tool." | founder kể (Alia): bỏ định vị cũ, chỉ làm một việc là pop-up |
| Roger Chen (founder) · `2025-12-06_how-i-built-the-1-app-on-the-app-store-twice` · 00:03:56 | "we still need to find a wedge like a concrete wedge like a concrete scenario in people's lives." | founder kể (Bro): tầm nhìn quá rộng, cần một kịch bản cụ thể làm điểm vào |
| Canyon (host/expert) · `2026-09-27_grow-app-23x-faster` · 00:00:00 | "It was look for markets that look too small for most people to bother with." | lời khuyên của expert Canyon: tìm thị trường trông quá nhỏ với đa số |
| Canyon (host/expert) · `2026-09-27_grow-app-23x-faster` · 00:22:19 | "Like it's these niches that are super super narrow where you're speaking to a really specific audience." | lời khuyên của expert Canyon: ngách siêu hẹp, nói đúng một nhóm |
| Steve Young (host/expert) · `2026-07-19_beginners-guide-to-buying-selling-apps-2026` · 00:07:34 | "It's like my ASO strategy is to focus on keywords that nobody is going after not that ones that are everybody is going after." | lời khuyên của expert Steve Young: ASO nhắm từ khoá mà không ai nhắm, không phải từ khoá ai cũng nhắm |
| Steve Young (host/expert) · `2026-07-19_beginners-guide-to-buying-selling-apps-2026` · 00:11:53 | "So you try to find these painkiller keywords that people are more likely to pay." | lời khuyên của expert Steve Young: tìm từ khoá giảm đau mà người ta dễ trả tiền |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Công thức này có 9/30 step chỉ là lời host/expert, không phải việc founder đã làm.** Phần "ngách siêu hẹp, thị trường trông quá nhỏ, từ khoá không ai nhắm" chủ yếu đến từ expert Canyon và Steve Young trong video về cách tăng trưởng và mua bán app, không từ founder kể sản phẩm của mình. Phần founder làm (13 + 5 case) thiên về chọn khe và đổi nhóm khách; chỉ một vài founder (Local Rank, 3AK) nói thẳng rằng ngách hẹp có lợi.
- **Hẹp quá thì không đủ lớn.** Đừng áp lời expert nguyên xi: `VALIDATE.md` cổng 1.5 nói ngách siêu hẹp thường kẹt quanh mức thấp. Trong kho, app đầu của Runafy (cho người mắc chứng tiểu không được) kiếm khoảng 5–10k USD; founder tự kể lý do gồm ngách quá hẹp, marketing khó, không có đam mê và build nhiều tháng trước khi validate (không chỉ do ngách). Sau đó anh chuyển sang app chạy bộ ranked (nằm ở `s11`). Đây là một ca thất bại tự kể; phần còn lại của kho chỉ là người thắng.
- **Từ khoá trống chưa chắc là cơ hội.** Lời Steve Young về từ khoá không ai nhắm đối lập với cổng 1.3 của `VALIDATE.md` (top 3 có 0–1 review có thể nghĩa là chưa ai kiếm được tiền). Kho không có số nào cho thấy cách nào đúng.
- **Nhánh M cần có thứ đã chạy.** 4 trong 5 founder nhánh M mở từ sản phẩm hoặc khách của chính họ (Sprout, SiteGPT, MagicSlides, Task Magic); Scanemon mở từ app của người khác (CardStock), tức là sang `s11`. Solo chưa có gì thì chủ yếu dùng nhánh T.
- **Kho chỉ chứa người thắng.** 18 case full dùng s9 và lên được kênh; số người thu hẹp ngách mà vẫn không ra đơn vắng mặt. "Không nêu" ≠ "không có": 7/18 không nêu vị trí ngách.

## Quyết định
- **QUA** nếu có đủ (a)(b)(c) ở Ngưỡng qua. Sang `VALIDATE.md` cổng 1 và 2.
- **DỪNG** nếu nhóm con không có sản phẩm trả tiền kiểm được ở đâu cả (kể cả nhóm kề), hoặc ước cỡ không qua cổng 1.5.
- **TEST THÊM** nếu thiếu đúng một điều kiện: trong 3 ngày (đề xuất, chưa có số của kho) tìm sản phẩm trả tiền ở nhóm con hoặc đọc 100+ review của đối thủ gần nhất (cổng 2.1).

## Cho solo founder bán global (từ VN)
- **Chép được:** bước 1–5 của nhánh T, làm từ xa bằng App Store, review, TikTok comment. Chọn khe theo nhóm khách mà đối thủ lớn bỏ qua (Coconote, Packager) hợp với solo hơn là thu hẹp theo sở thích.
- **Rào cản thật:** nhiều case nhánh T là người trong cuộc (8/18 ghi insider, ví dụ 3AK, Packager, Hero Analytics) nên biết nhóm con ở đâu; mình có thể không biết. Cách bù: dùng bước 3 qua comment/Reddit thay cho kinh nghiệm riêng. Ngách hẹp cũng làm trần doanh thu thấp, nên cổng 1.5 nghiêm.
- **KHÔNG nên làm** nếu không tìm được sản phẩm trả tiền nào ở nhóm con và nhóm kề (không có bằng chứng tiền), hoặc nếu nhóm con chỉ tiếp cận được bằng quảng cáo trả tiền trong khi ưu tiên của mình là organic.
