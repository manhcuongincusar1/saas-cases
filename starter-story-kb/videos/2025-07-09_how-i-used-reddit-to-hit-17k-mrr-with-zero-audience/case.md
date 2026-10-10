---
id: BaWUPamqWlA
slug: appalchemy-reddit-volume-playbook
product: AppAlchemy
founder: Diego Roshardt
tagline: Một bài Reddit hay được nhân bản lên hàng chục subreddit — 1 triệu lượt tiếp cận, 0 đồng quảng cáo, founder có đúng 70 follower trên X
revenue_usd_month: 17000
revenue_basis: founder nói around 17K per month sau 4 tháng, tiêu đề video ghi 17K MRR. KHÔNG có ảnh dashboard Stripe nào trong video — chỉ có lời founder. Con số chi phí anh tự nêu lại không khớp với biên lợi nhuận anh tự nêu, xem mục 1
model: micro-saas-subscription
category: ai-design-tools
audience: B2B/B2C — indie hacker và người làm sản phẩm cần thiết kế giao diện app di động mà không muốn thuê designer
started: khoảng tháng 3/2025 (founder nói bắt đầu 4 tháng trước, video đăng 09/07/2025)
time_to_first_sale: dưới 1 tháng — MVP mất 2 tuần rồi marketing Reddit ngay lập tức
time_to_scale: 4 tháng từ 0 lên khoảng 17.000 USD/tháng
team_size: 1
funding: bootstrapped
main_channel: Reddit organic — một bài viết tốt nhân bản lên nhiều subreddit, 2-3 lần/tuần
tech_stack: [Cursor, Next.js, React, Firebase, Chakra UI, Ant Design, Vercel]
key_metrics:
  paying_customers: hơn 1.000
  signups: khoảng 20.000, gần như toàn bộ từ Reddit
  traffic: khoảng 20.000 lượt truy cập/tháng
  reddit_reach: hơn 1.000.000 lượt tiếp cận
  ad_spend: 0
  ai_api_cost: khoảng 2.500 USD/tháng
  gross_margin: khoảng 70% theo lời founder
  arpu_suy_ra: khoảng 17 USD/tháng/khách
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=BaWUPamqWlA
published: 2025-07-09
views: 277469
---

# AppAlchemy — $17K/tháng từ Reddit, với 70 follower trên X

> **Tóm tắt 30 giây:** Diego Roshardt trả cho một designer trên Upwork hàng trăm đô để thiết kế app di động, và mỗi lần sửa vặt lại phải trả thêm. Anh dựng công cụ AI làm đúng việc đó — **MVP trong 2 tuần** — rồi đem đi marketing trên Reddit ngay. Sau **4 tháng**: hơn **1.000 khách trả tiền**, ~20.000 signup, hơn **1 triệu lượt tiếp cận** và **$0 tiền quảng cáo**. Anh có **70 follower trên X**, không YouTube, không TikTok. Cơ chế duy nhất: viết MỘT bài Reddit cho giá trị trước rồi cắm link sản phẩm ở giữa bài, sau đó **nhân bản bài đó lên hàng chục subreddit**.

![$0 chi phí marketing](screenshots/01_01m08s_usd-0.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$17K/tháng (MRR), sau 4 tháng |
| Khách trả tiền | hơn 1.000 |
| Signup | ~20.000, gần như 100% từ Reddit |
| Traffic | ~20.000 lượt/tháng |
| Lượt tiếp cận Reddit | hơn 1.000.000 |
| Chi quảng cáo | **$0** |
| Chi phí AI API | ~$2.500/tháng |
| Cursor | $20/tháng |
| Vercel hosting | ~$40/tháng |
| Biên lợi nhuận (founder nói) | ~70% |
| Follower trên X lúc quay | dưới 100 (lúc cold DM là 70) |

**ARPU suy ra:** $17.000 / 1.000+ khách ≈ **$17/khách/tháng**. Đây là mức giá SaaS rẻ, phù hợp tệp indie hacker/freelancer.

### ⚠️ Chỗ số liệu KHÔNG khớp

Cộng đúng những chi phí founder tự liệt kê: $2.500 (AI API) + $40 (Vercel) + $20 (Cursor) = **$2.560**. Trên doanh thu $17.000, biên phải là **~85%**, không phải 70% như anh nói. Khoảng trống ~$2.500/tháng không được giải thích. Ba khả năng:

1. Phí Stripe + hoàn tiền + thuế (thường ngốn 5-10% doanh thu, tức ~$1.000-1.700) — hợp lý nhất.
2. Chi phí AI API thật cao hơn con số $2.5K anh đọc ra.
3. Anh nói biên 70% theo cảm tính, không tính sổ.

**Không có ảnh dashboard doanh thu nào trong toàn bộ video.** Với một case chỉ 4 tháng tuổi và toàn bộ số liệu đến từ lời kể, hãy coi $17K là con số tham khảo chứ không phải bằng chứng.

### Kiểm tra chéo các tỉ lệ (những cái này thì hợp lý)

- 20.000 signup / hơn 1.000 khách trả tiền = **free-to-paid ~5%** — bình thường với sản phẩm có bản miễn phí rộng rãi.
- 1.000.000 lượt tiếp cận Reddit → ~80.000 lượt truy cập trong 4 tháng = **CTR ~8%**. Cao, nhưng Reddit organic đúng ngách thì có thể.

![Con số của AppAlchemy](screenshots/04_04m19s_ch-numbers-behind-appalchemy.jpg)

## 2. Ý tưởng đến từ hoá đơn của chính mình ⭐⭐

Không có framework tìm ý tưởng gì cao siêu. Đúng một chuỗi sự kiện:

1. Diego muốn tự làm một app di động.
2. Anh thuê designer trên Upwork, trả **hàng trăm đô** cho một bản thiết kế tạm được.
3. Mỗi lần muốn **sửa một chi tiết nhỏ**, anh phải trả thêm tiền.
4. Anh nghĩ: nếu dựng được công cụ AI quanh việc này, mình tiết kiệm cho người khác rất nhiều thời gian và tiền.

Sản phẩm được mô tả gọn trong một câu bán hàng cực tốt:

> *"App của tôi tên là **AppAlchemy** và nó cho phép bạn dựng thiết kế app di động rất nhanh bằng AI. **Nó giống Cursor, nhưng cho việc thiết kế app di động**."*

**Cơ chế đằng sau câu đó:** khi thị trường vừa có một sản phẩm ai cũng hiểu (Cursor), công thức `X nhưng cho Y` tiết kiệm cho bạn toàn bộ chi phí giáo dục thị trường. Đây là lý do câu này chạy tốt trên Reddit — người đọc hiểu ngay trong 2 giây.

**Về việc "xác thực ý tưởng":** Diego thẳng thắn nói anh gần như **không validate gì cả**. Đó là vấn đề anh tự gặp, nên anh tin là có thật, xây MVP đơn giản nhất trong 2 tuần rồi đem lên Reddit luôn.

![Cách xác thực ý tưởng](screenshots/02_02m07s_ch-how-to-validate-an-idea.jpg)

## 3. Reddit Marketing Playbook — 5 bước ⭐⭐⭐

Đây là phần đáng tiền nhất của video (chiếm gần 5 phút, từ phút 5:26 đến 10:12).

### Bước 1 — Trở thành người dùng Reddit thật trước đã

Nếu bạn chưa dùng Reddit, bắt đầu dùng **hàng ngày**. Hai mục đích:

- **Học nền tảng:** thấy loại bài nào ăn khách.
- **Warm-up tài khoản:** *"bất kỳ bài nào đến từ tài khoản mới tạo đều sẽ bị Reddit tự động lọc bỏ."*

Đây là chi tiết mà 90% người Việt bỏ qua rồi kết luận "Reddit không hiệu quả". Bài của bạn không bị người ta chê — nó **không bao giờ được hiển thị**.

### Bước 2 — Dựng danh sách subreddit (cần VOLUME)

> *"Cái này rất quan trọng vì bạn **cần volume** thì chiến thuật này mới chạy. Càng nhiều càng tốt, và bạn có thể đi cả rộng lẫn hẹp."*

**Mẹo hay nhất trong toàn bộ video** — dùng công cụ Reddit Ads mà **không tốn một xu quảng cáo**:

1. Vào trang Reddit Ads, tạo một campaign mới.
2. Vào mục **targeting → communities**.
3. Gõ từ khoá liên quan sản phẩm (ví dụ của anh: `no code`).
4. Reddit trả về hàng loạt cộng đồng liên quan — thêm vào là nó **gợi ý tiếp**, cứ thế mà đào.
5. Không cần chạy ads, không cần nạp tiền. Chỉ lấy danh sách rồi thoát.

Đây là công cụ nghiên cứu subreddit miễn phí, chính chủ, tốt hơn mọi công cụ bên thứ ba.

### Bước 3 — Viết MỘT bài organic thật tốt

Xem chi tiết ở mục 4 bên dưới.

### Bước 4 — Đem chính bài đó đăng lên NHIỀU subreddit

Đây là chỗ chiến thuật này khác hẳn mọi lời khuyên Reddit thông thường.

> *"Volume ở đây cực kỳ quan trọng vì nó tăng cơ hội một trong các bài của bạn lên được trang chủ Reddit — và cái đó cho bạn cực nhiều traffic."*

Và phép tính đáy — phần quan trọng hơn:

> *"Kể cả điều đó không xảy ra, giả sử bạn đăng lên 10 subreddit khác nhau và mỗi bài trung bình được khoảng 10.000 view. Vậy là tổng cộng đã 100.000 view rồi, cũng đã rất tốt. Nên vẫn đáng làm."*

**Cơ chế:** đây là bài toán xổ số có kỳ vọng dương. Bạn không đặt cược vào một bài viral; bạn mua nhiều vé bằng cùng một lần viết. Chi phí biên của vé thứ hai gần bằng 0.

### Bước 5 — Lặp lại và thử nghiệm

- Thử các **dạng bài** khác nhau: video, case study, dạng khác — xem cái nào ăn trong ngách của mình.
- **Nhịp an toàn: 2-3 bài/tuần.** *"Tôi nghĩ nhiều hơn thế thì khả năng cao bạn bị ban."*

![Reddit Marketing Playbook](screenshots/05_05m38s_ch-reddit-marketing-playbook.jpg)

## 4. Giải phẫu bài "ăn" và bài "chết" ⭐⭐⭐

Diego mở cả bài của anh và bài của người khác lên so sánh trực tiếp.

### Cấu trúc bài ăn khách (bài thật của anh cho AppAlchemy)

| Vị trí | Làm gì | Vì sao |
|---|---|---|
| **Tiêu đề** | Câu giật sự chú ý, **không nhắc tên sản phẩm** | Nhắc sản phẩm ngay tiêu đề = tự dán nhãn quảng cáo, người ta lướt qua |
| **Mở bài** | Vẫn **chưa** nhắc sản phẩm — cho giá trị thật trong ngách trước | Đổi giá trị lấy sự chú ý trước khi xin gì |
| **Giữa bài** | **Cắm link trực tiếp** sản phẩm | *"Nếu bạn link thẳng sản phẩm, bạn sẽ được nhiều traffic về website hơn hẳn so với chỉ nhắc tên nó"* |
| **Nội dung** | Trong bài cụ thể này anh làm **case study về một app di động rất thành công** — tìm thấy trên Twitter, tóm tắt lại | Nội dung có thể đi mượn. Điều quan trọng là nó hữu ích thật |

### Mẹo lách luật subreddit khắt khe ⭐⭐⭐

Đây là chi tiết tinh vi nhất và gần như không ai nói ra:

> *"Với những subreddit khắt khe hơn không cho link sản phẩm, tôi khuyên bạn **link thêm một sản phẩm khác bên cạnh sản phẩm của mình** — cắm một sản phẩm bổ trợ. Ví dụ của tôi là công cụ thiết kế, nên Cursor bổ trợ rất tốt vì nó dành cho lập trình. Tôi thường cắm nó ngay sau sản phẩm mình, và như vậy **khả năng bị ban hoặc bị gỡ bài vì tự quảng cáo thấp hơn hẳn**."*

**Cơ chế tâm lý:** một link = quảng cáo. Hai link, trong đó có một link không phải của bạn = danh sách gợi ý. Mod và người đọc đọc nó như nội dung biên tập, không phải rao vặt. Chi phí gần như bằng 0.

### Bài chết trông thế nào

Diego mở một bài thất bại của founder khác:

- Nhắc tên sản phẩm **ngay trong tiêu đề**
- Vào bài là nói ngay về sản phẩm, liệt kê hết tính năng
- Còn link cả Discord vào

> *"Như bạn thấy từ lượng tương tác, cái này không ăn gì cả, **vì người ta không quan tâm**. Họ muốn nhận giá trị trước. Họ muốn đọc cái gì đó thú vị đã — rồi nếu sản phẩm của bạn liên quan tới cái đó thì được, bạn cắm vào và họ có thể sẽ quan tâm."*

![Ví dụ bài Reddit](screenshots/06_08m25s_replay.jpg)

## 5. Mâu thuẫn: BỐN trường phái Reddit trong kho này ⭐⭐⭐

Đây là mục quan trọng nhất để bạn không sao chép sai. Reddit không có một playbook — nó có ít nhất bốn, và chúng **mâu thuẫn trực tiếp** với nhau.

| Trường phái | Ai | Cách làm | Đúng khi nào |
|---|---|---|---|
| **Volume / phân phối** | Diego (case này) | 1 bài giá trị nhân bản lên 10+ subreddit, **có link sản phẩm giữa bài**, 2-3 lần/tuần | Sản phẩm phục vụ ngách rộng, có nhiều subreddit lớn; bạn chấp nhận rủi ro bị ban và sẵn sàng đổi tài khoản |
| **Kể chuyện / uy tín** | [Romàn Czerny — Gojiberry AI](../2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/case.md) | Post về **chính việc mình đang làm**, KHÔNG gắn link sản phẩm | Ngách hẹp, mod soi kỹ, bạn cần uy tín dài hạn và bán giá cao ($99/tháng trở lên) |
| **Chỉ để xác thực** | Lukas Hermann — Stagetimer (video 25/06/2025 cùng kênh) | **Đúng một bài, một subreddit siêu ngách**, xin feedback, website **chưa có giá** | Bạn chưa có gì để bán và cần biết vấn đề có thật không |
| **Beta miễn phí** | [Tom — Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md) | Ra mắt beta **miễn phí** trên Reddit để gom người dùng, sau đó mới thu $25/tháng | Sản phẩm B2B chán, tệp người dùng chuyên nghiệp tập trung ở 1-2 subreddit |

**Cách phân định — dựa trên 3 biến số:**

1. **Giá bán.** ARPU $17 (Diego) bắt buộc phải chơi volume — bạn cần hàng nghìn khách, không thể chăm từng người. ARPU $99 (Gojiberry) thì một mối quan hệ đáng giá hơn 100 lượt click, nên chơi uy tín.
2. **Độ rộng của ngách.** Diego bán cho "người làm app" — có hàng chục subreddit. Lukas bán cho "người làm video production" — anh nói *"tôi mất khá lâu mới tìm được một subreddit. Chúng rất ẩn, rất nhỏ, rất ngách"*. Ngách chỉ có 1 subreddit thì **không có** trò volume; đăng lần thứ hai là bị mod ghi sổ.
3. **Bạn đang ở giai đoạn nào.** Chưa có sản phẩm = chế độ Lukas (hỏi, không bán). Có sản phẩm rồi = chế độ Diego hoặc Romàn.

**Cảnh báo về rủi ro Diego không nói ra:** đăng cùng một nội dung lên hàng chục subreddit **chính xác là mẫu hành vi mà bộ lọc spam của Reddit được thiết kế để bắt**. Anh giảm rủi ro bằng ba cách (warm-up tài khoản, giới hạn 2-3 bài/tuần, cắm thêm link sản phẩm thứ hai) nhưng không loại bỏ được. Nếu toàn bộ 20.000 signup của bạn đến từ Reddit và tài khoản bị khoá, doanh nghiệp bạn mất kênh phân phối duy nhất trong một đêm. Hãy coi Reddit là **tiền thuê nhà**, không phải tài sản — và dùng doanh thu đó mua thứ bạn sở hữu (email list, SEO, thương hiệu).

## 6. Build nhanh bằng AI — hai mẹo ngược đời ⭐⭐

Diego xây MVP trong **2 tuần**. Hai nguyên tắc anh dùng, cả hai đều đi ngược thói quen của dev:

**1. Cố tình dùng thư viện CŨ, đừng dùng cái mới nhất.**

> *"Tôi **không** dùng những thư viện hay framework mới nhất, vì AI **luôn giỏi hơn nhiều** với những thư viện được dùng phổ biến nhất trên web."*

**Cơ chế:** chất lượng code AI sinh ra tỉ lệ thuận với lượng dữ liệu huấn luyện. Framework ra mắt tháng trước = AI bịa API. Framework 5 năm tuổi có 100.000 câu hỏi StackOverflow = AI viết gần như không sai. Bạn đang tối ưu **tốc độ ship**, không phải độ sành điệu của stack.

**2. Dùng thư viện component UI có sẵn.**

> *"Tôi dùng rất nhiều thư viện component UI như **Chakra UI** hoặc **Ant Design**. Cái này cho phép prototype nhanh hơn nhiều và cũng làm website đẹp hơn."*

*(Ghi chú ASR: phụ đề tự động ghi "Antesign" — đối chiếu ngữ cảnh thì đây là **Ant Design**.)*

## 7. Tech stack và chi phí

| Hạng mục | Công cụ | Chi phí |
|---|---|---|
| IDE / build | **Cursor** | $20/tháng |
| Framework | **Next.js + React** | — |
| Auth + Database | **Firebase** | — |
| Hosting | **Vercel** | ~$40/tháng |
| UI | Chakra UI, Ant Design | — |
| **AI API backends** | không nêu tên nhà cung cấp | **~$2.500/tháng** |

Điểm đáng chú ý: **83% chi phí biến đổi của doanh nghiệp này là tiền AI API.** Đó là đặc điểm của mọi AI wrapper — chi phí phục vụ tăng tuyến tính theo lượng dùng, khác hẳn SaaS truyền thống. Nếu bạn định làm mô hình này với giá $17/tháng, hãy tính kỹ: bạn có ~$2,5 chi phí AI trên mỗi khách/tháng ở mức hiện tại. Một khách dùng nặng có thể ăn hết lãi của mười khách nhẹ. **Rate limit và gói theo credit là bắt buộc, không phải tuỳ chọn.**

## 8. Ba bài học founder tự rút ra

**1. Giải vấn đề trong thị trường ĐANG LỚN.**

> *"Ví dụ tôi có thể đưa ra là xây một công cụ SaaS cho **chủ báo giấy** — báo giấy đang suy tàn. Hoặc bạn xây công cụ cho **vibe coding** — thứ chỉ trong vài tháng gần đây đã bùng nổ và sẽ còn tiếp tục lớn."*

Đây là lời khuyên đúng nhưng có mặt trái ít người nói: thị trường đang lớn cũng là thị trường **đông đối thủ nhất và vòng đời sản phẩm ngắn nhất**. Công cụ thiết kế app bằng AI năm 2025 có hàng chục đối thủ; đến 2026 nhiều khả năng Figma hoặc chính Cursor nuốt luôn tính năng này.

**2. Marketing quan trọng ngay từ đầu, không phải sau khi hoàn thiện sản phẩm.**

> *"Ngay từ lúc bắt đầu, bạn nên dành **rất nhiều thời gian cho marketing** thay vì thêm tính năng chẳng ai yêu cầu."*

**3. Tốc độ là lợi thế lớn nhất của solo founder.** Hãy tận dụng nó bất cứ khi nào có thể.

Lời khuyên cuối cho chính mình ngày trước:

> *"Bây giờ là thời điểm tốt nhất để build. Nếu bạn có ý tưởng, **đưa một MVP đơn giản ra ngoài kia và bắt đầu marketing càng sớm càng tốt**."*

![Bắt đầu ngay](screenshots/08_12m05s_ch-start-now.jpg)

## 9. Cảnh báo thiên kiến nguồn

Case này cần đọc với mức hoài nghi cao hơn trung bình trong kho:

- **Không có bằng chứng số liệu nào.** Không dashboard Stripe, không ảnh doanh thu. Toàn bộ con số đến từ lời kể của founder qua một cold DM.
- **Chi phí không khớp biên lợi nhuận** (mục 1).
- **Video mới 4 tháng tuổi tính từ lúc sản phẩm ra đời.** Chưa ai biết churn thế nào. Với AI wrapper giá $17 bán cho indie hacker — tệp khách hàng nổi tiếng là churn cao — con số $17K MRR sau 4 tháng có thể không tồn tại sau 12 tháng.
- **Kênh Starter Story đã được HubSpot mua lại và bán khoá học Starter Story Build.** Video này có **hai** đoạn bán hàng: một quảng cáo 10Web dài hơn một phút (chiếm nguyên chương "Build a professional website with one prompt" — đây **không** phải nội dung của Diego), và một đoạn chốt bán Starter Story Build ở cuối. Câu chuyện "founder vô danh, 70 follower, 4 tháng, $17K" chính là quảng cáo hoàn hảo cho một khoá học dạy build app bằng AI trong 2 tuần. Điều đó không có nghĩa là nó giả — nhưng nó giải thích vì sao case này được chọn lên sóng.
- **Kênh chỉ phỏng vấn người thành công.** Với mỗi Diego, có hàng nghìn người đăng bài Reddit đúng công thức này và bị gỡ bài, bị ban, hoặc không ai đọc.

## 10. Áp dụng cho tôi (indie hacker VN)

### Sao chép được gì — cụ thể, làm được tuần này

1. **Lấy danh sách subreddit miễn phí bằng Reddit Ads.** Tạo campaign nháp → targeting → communities → gõ từ khoá ngách của bạn → chép danh sách → thoát, không nạp tiền. 30 phút cho ra 30-50 subreddit.
2. **Warm-up tài khoản Reddit NGAY HÔM NAY.** Đây là bước có độ trễ dài nhất (2-4 tuần) nên phải bắt đầu trước khi có sản phẩm. Comment thật, vote thật, tham gia thật. Đừng để đến lúc có sản phẩm mới tạo account.
3. **Viết một bài theo đúng khung 4 lớp:** tiêu đề giật (không có tên sản phẩm) → giá trị thật trong ngách → link sản phẩm giữa bài → link một sản phẩm bổ trợ ngay sau đó.
4. **Áp dụng mẹo "cắm sản phẩm thứ hai".** Đây là chi tiết đáng giá nhất và tốn 0 đồng.
5. **Dùng stack cũ + thư viện component có sẵn** để rút thời gian build. Next.js + Firebase + Chakra/Ant/shadcn là tổ hợp AI viết gần như không sai.
6. **Đặt công thức định vị `X nhưng cho Y`** với X là sản phẩm ai cũng biết.

### Rào cản thật — không tô hồng

- **Reddit rất khắc nghiệt với người dùng mới ngoài Mỹ.** Tài khoản mới + IP Việt Nam + VPN = tỉ lệ bị shadowban cao. Nhiều subreddit có ngưỡng karma tối thiểu (thường 50-100 comment karma) và ngưỡng tuổi tài khoản (30-90 ngày). Bạn cần **1-3 tháng warm-up trước khi được đăng bài ở đâu có ý nghĩa**. Đây là chi phí thật, tính bằng thời gian.
- **Rào cản tiếng Anh cao hơn ở đây so với mọi kênh khác.** Reddit là nơi người ta đọc kỹ và ngửi thấy văn AI từ dòng đầu. Một bài SEO tiếng Anh dở vẫn có thể lên hạng Google; một bài Reddit tiếng Anh dở thì bị downvote thẳng. Nếu bạn định dùng ChatGPT viết hộ toàn bộ, khả năng cao thất bại — dùng nó để sửa ngữ pháp thì được.
- **Rủi ro nền tảng ở mức tối đa.** 100% signup đến từ một kênh mà bạn không sở hữu và có thể bị khoá không cần lý do. Xem lại phần cảnh báo ở mục 5.
- **Chi phí AI API tính bằng USD, cần thẻ quốc tế.** ~$2.500/tháng ở quy mô của Diego. Ở quy mô của bạn khi mới bắt đầu thì nhỏ, nhưng nó tăng **trước** doanh thu — vì người dùng free đốt tiền của bạn trước khi có ai trả tiền. Chuẩn bị đệm tiền mặt và bật rate limit ngay từ ngày đầu.
- **ARPU $17/tháng nghĩa là bạn cần 1.000 khách** để có $17K. Với thị trường VN thì con số này gần như bất khả thi ở mức giá đó — mô hình này **chỉ có nghĩa nếu bạn bán cho khách quốc tế bằng tiếng Anh**.
- **Không có audience là điểm mạnh của case này, nhưng nó cũng có nghĩa là bạn không có gì để rơi trở lại.** Diego không có email list, không có kênh. Nếu Reddit tắt, anh về 0.

### Khi nào KHÔNG dùng mô hình này

- **Khi ngách của bạn chỉ có 1-2 subreddit.** Trò volume của Diego cần ít nhất 10 subreddit đủ lớn. Ngách siêu hẹp (như Stagetimer, như Packager) thì phải chuyển sang chế độ "một bài để xác thực" hoặc "beta miễn phí", và kênh chính phải là **Google SEO đáy phễu**, không phải Reddit.
- **Khi bạn bán giá cao ($99+/tháng, B2B, có sale cycle).** Traffic hàng loạt từ Reddit chuyển đổi kém ở mức giá đó. Xem [Gojiberry AI](../2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/case.md) — dù kênh là Reddit, cỗ máy chốt thật lại là cold email và LinkedIn outreach.
- **Khi bạn cần một tài sản dài hạn.** Reddit không tích luỹ. Bài đăng chết sau 48 giờ. So sánh với [SEO đáy phễu + Google Ads của Late](../2026-03-04_zero-to-40k-month-with-one-marketing-channel-no-soci/case.md) hoặc [YouTube search của FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md) — cả hai kênh đó cho tài sản còn kéo traffic sau nhiều tháng.
- **Khi sản phẩm của bạn giải một vấn đề người ta chưa biết mình có.** Reddit organic chỉ ăn khi có sẵn một cộng đồng đang bàn về vấn đề đó.

## Nguồn

- Video: <https://www.youtube.com/watch?v=BaWUPamqWlA> (13:16, đăng 09/07/2025, 277.469 view)
- Founder trên X: `@DiegoRoshardt`
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
