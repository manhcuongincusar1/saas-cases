---
id: 88BbTpbWVpY
slug: yadaphone-skype-shutdown-timing
product: Yadaphone (yadaphone.com)
founder: Denis Yurchak
tagline: Microsoft khai tử Skype, một dev tự học người Nga ở Áo build bản thay thế trong một cuối tuần — và đi xin các bài blog đang xếp hạng thay chữ Skype bằng tên app mình
revenue_usd_month: 14000
revenue_basis: founder nói trong video là 14.000 USD/tháng; dashboard cho thấy tháng 6 (tháng gần nhất) là 13.300 USD; phần mô tả video của kênh lại ghi 15K MRR. Tôi lấy 14.000 vì đó là con số founder tự nói và khớp tiêu đề, đồng thời ghi rõ số dashboard thấp hơn
model: micro-saas-payg-credits
category: voip-telecom
audience: B2C và B2B — người đi du lịch, expat, và doanh nghiệp phải gọi quốc tế nhiều
started: tháng 3/2025, vài ngày sau khi Microsoft công bố đóng Skype
time_to_first_sale: vài phút sau bài đăng Reddit đầu tiên
time_to_scale: 7 tháng từ 0 lên 14.000 USD/tháng
team_size: 1 (solo founder, hỗ trợ khách hàng tự động hoá bằng công cụ tự build)
funding: bootstrapped
main_channel: Reddit lúc ra mắt, sau đó SEO và xin thay tên trong các bài blog đang xếp hạng cho từ khoá Skype alternative
tech_stack: [Next.js, Cursor, Vercel, Stripe, Twilio, Ahrefs]
key_metrics:
  registered_users: 10.000 sau 7 tháng
  paying_customers: 4.500 khách cá nhân trả tiền
  enterprise_clients: 20 khách doanh nghiệp
  biggest_enterprise_deal: khoảng 1.000 USD/tháng từ một khách duy nhất
  month_1_revenue: 4.000 USD
  month_3_revenue: 10.800 USD
  month_6_revenue: 13.300 USD
  calls_september: 27.000 cuộc gọi trong một tháng
  cogs_twilio: khoảng 35% doanh thu tháng
  first_week_users: 150
  twitter_followers_before_launch: 60
replicability_vn: 3
difficulty: 3
video_url: https://www.youtube.com/watch?v=88BbTpbWVpY
published: 2025-10-16
views: 92066
---

# Yadaphone — $14K/tháng nhờ đứng đúng chỗ khi một công ty $1B sập tiệm

> **Tóm tắt 30 giây:** Tháng 3/2025 Microsoft tuyên bố đóng Skype. Denis Yurchak — một nhà ngoại giao được đào tạo bài bản, **không có nền tảng kỹ thuật**, tự học code trong 2 tháng — nhìn thấy tweet của Pieter Levels kêu gọi ai đó làm bản thay thế Skype và tự hỏi *"why not me?"*. Anh build prototype trong **một cuối tuần**, đăng Reddit, **có đơn hàng đầu tiên sau vài phút** (bị ban sub ngay sau đó). 7 tháng sau: **10.000 người đăng ký, 4.500 khách trả tiền, 20 khách doanh nghiệp, $14K/tháng**. Chiêu hay nhất không phải build mà là: anh đi tìm **tác giả các bài blog đang xếp hạng cho từ khoá Skype alternative** và xin họ thay chữ Skype bằng Yadaphone — thừa hưởng domain authority mà anh không đời nào tự xây được.

![$4.000 tháng đầu tiên](screenshots/01_01m23s_usd-4-000.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu hiện tại | **$14.000/tháng** (dashboard tháng gần nhất: $13.300) |
| Tháng 1 | $4.000 |
| Tháng 3 | $10.800 |
| Tháng 6 | $13.300 |
| Người đăng ký | 10.000 sau 7 tháng |
| Khách cá nhân trả tiền | 4.500 |
| Khách doanh nghiệp | 20 (deal lớn nhất ~$1.000/tháng) |
| Cuộc gọi tháng 9 | 27.000 |
| Chi phí Twilio | **~35% doanh thu** |
| Người ra mắt | 1 (solo) |
| Follower Twitter trước khi launch | 60 |

**Ba con số doanh thu vênh nhau — nói thẳng ra:**

| Nguồn | Con số |
|---|---|
| Founder nói trong video | $14.000/tháng |
| Dashboard tháng 6 (gần nhất) | $13.300 |
| Mô tả video do kênh viết | $15K MRR |

Tôi dùng **$14.000**. Lý do: đó là con số founder tự đọc ra, khớp tiêu đề, và nằm giữa hai con số kia. Con số $15K trong mô tả là do kênh viết chứ founder không nói — Starter Story có xu hướng làm tròn lên. Lưu ý thêm: **$13.300 là doanh thu, không phải lợi nhuận** — Twilio đã ăn ~35%.

![Gọi quốc tế 10 phút có thể tốn $50-100](screenshots/02_02m11s_usd-50.jpg)

## 2. Sản phẩm giải quyết gì

Gọi quốc tế **thật** (số điện thoại thật, không phải messenger) vẫn cực đắt: một cuộc 10 phút có thể tốn **$50-100** tuỳ nước và nhà mạng. Yadaphone dùng VoIP để gọi tới bất kỳ số di động hoặc cố định nào **ngay trong trình duyệt**, tính bằng cent.

Vì sao vẫn còn nhu cầu trong thời đại WhatsApp: Denis nói rất chính xác về ICP của mình —

> *"Tôi đi lại nhiều. Về mặt cơ quan chính phủ, ngân hàng, doanh nghiệp, cơ quan di trú — **họ không có trên các app nhắn tin**. Cách duy nhất để gọi họ là gọi điện thật. Và làm việc đó khi ở nước ngoài thì đắt kinh khủng."*

**Điểm khác biệt về mô hình giá — đây mới là thứ đáng học:**

| Đối thủ (cũ) | Yadaphone |
|---|---|
| Subscription ~$30/tháng trở lên | **Pay-as-you-go**, nạp credit |
| B2B phải mua seat cho từng nhân viên | Doanh nghiệp mua một cục credit, **cả tổ chức dùng chung số dư** |
| Hết tháng vẫn trả tiền dù không gọi | Hết credit thì nạp thêm, không gọi thì không mất |

Cơ chế vì sao thắng: nhu cầu gọi quốc tế **không đều** — có tháng gọi 20 cuộc, có tháng không gọi cuộc nào. Bắt khách trả subscription cố định cho một nhu cầu bất định là ma sát tâm lý lớn nhất trong ngành này. Denis xoá đúng ma sát đó. Với B2B, việc **bỏ mô hình per-seat** còn quan trọng hơn: công ty 50 người mà chỉ 6 người hay gọi quốc tế thì per-seat là vô lý.

## 3. Nền tảng founder: nhà ngoại giao tự học code trong 2 tháng ⭐⭐

> *"Tôi hoàn toàn không có nền tảng kỹ thuật. Thực ra tôi được đào tạo làm nhà ngoại giao. Tôi từng học ngành ngoại giao ở Nga. Rồi tôi chuyển sang Áo... **tôi tự học code trong hai tháng**, chủ yếu bằng sách và khoá học."*

Sau đó anh đi làm ở một công ty, nhận ra không hợp, chuyển sang freelance để nuôi thân và **luôn có một project phụ đang chạy**.

> *"Những project đầu tiên của tôi xấu tệ. Chúng không có người dùng. Rồi từ từ, với mỗi project, tôi học được thứ này thứ kia. Design của tôi khá lên. Code của tôi đáng tin hơn. Cuối cùng tất cả **chồng lên nhau thành bộ kỹ năng** cho phép tôi build được Yadaphone."*

**Đọc case này đúng cách:** tiêu đề nói "build trong một cuối tuần", nhưng cái cuối tuần đó chỉ khả thi vì **nhiều năm làm project thất bại trước đó**. Đây là mẫu lặp lại trong gần như mọi case thành công của kho này: cái "overnight success" luôn là lần rút thẻ thứ N, không phải thứ nhất. Khác biệt duy nhất là lần thứ N rơi đúng vào lúc thị trường mở cửa.

![Không có nền tảng kỹ thuật](screenshots/03_03m21s_ch-non-technical-background.jpg)

## 4. Cơ chế thật của case này: timing arbitrage ⭐⭐⭐

Đây là phần đắt nhất và cũng là phần dễ bị hiểu sai nhất.

**Chuỗi sự kiện:**

1. Denis là khách trung thành của Skype để gọi cơ quan hành chính khi đi nước ngoài.
2. Tháng 3/2025, Microsoft công bố **đóng Skype**.
3. **Pieter Levels tweet** rằng anh và bạn bè cũng dùng Skype, bực vì Microsoft đóng nó, và **công khai kêu gọi ai đó làm bản thay thế**.
4. Denis: *"Tôi nghĩ, **why not me?** Hoá ra tôi không phải người duy nhất dùng Skype để gọi quốc tế — điều mà tôi không biết."*
5. Build prototype trong một cuối tuần. Đăng Reddit và X. **Có đơn hàng đầu tiên sau vài phút.**

Khi Pat hỏi "anh làm đúng cái gì mà lần này khác các app trước", Denis trả lời câu đáng chép ra dán tường:

> *"Điều then chốt về ý tưởng này là **nó không phải một ý tưởng gì cả. Nó là một thị trường đã được xác thực** — xác thực lần đầu bằng cái tweet của Pieter Levels, rồi bằng chính những đơn hàng tôi nhận được từ bài Reddit."*

**Vì sao cơ chế này hiệu quả (và khi nào hết hiệu quả):**

Khi một công ty tỷ đô đóng cửa một sản phẩm, ba thứ xảy ra cùng lúc trong một cửa sổ vài tháng:

| Thứ được mở ra | Ý nghĩa với bạn |
|---|---|
| **Cầu tồn dư có sẵn** | Hàng triệu người đang dùng buộc phải tìm cái khác — bạn không phải tạo nhu cầu, chỉ phải xuất hiện |
| **Từ khoá mới bùng nổ** | Skype alternative, Skype replacement... đi từ 0 lên rất cao, chưa ai chiếm |
| **Virality miễn phí** | Mọi bài viết dính tới tin lớn đó đều được lan truyền, kể cả bài của người 60 follower |

Nhưng cửa sổ này **đóng lại**. Sau 6-12 tháng, cầu tồn dư đã phân bổ xong về tay ai đó, từ khoá đã có người xếp hạng. Nghĩa là mô hình này **không lặp lại theo lịch** — bạn phải ở tư thế sẵn sàng và chờ. Đó chính là lý do phần "nhiều năm project thất bại" ở mục 3 quan trọng: **nó là chi phí duy trì tư thế sẵn sàng**.

![Cái tweet trị giá $100K](screenshots/04_04m20s_ch-the-100k-tweet.jpg)

## 5. Chiến thuật Reddit: bị ban vẫn có tiền ⭐⭐⭐

Denis không có audience. **60 follower Twitter suốt nhiều năm.** Nhưng anh biết Reddit.

> *"Điều hay về Reddit là bạn có thể lấy được **hàng triệu impression mà không cần một follower nào cả**. Tôi từng ra mắt sản phẩm trên đó, từng bị block rất nhiều, nhưng tôi biết cách viết, biết nhắm sub nào, dùng giọng điệu nào."*

Trình tự thật, kể cả phần xấu:

1. Bài đầu tiên: **chỉ là ảnh chụp màn hình tính năng lõi** — giao diện quay số sạch, đơn giản — cộng vài câu về sản phẩm.
2. Đăng vào các sub về **du lịch**, vì anh nghĩ đó là ICP.
3. **Bị ban rất nhanh.** *"Rất nản."*
4. Nhưng trước khi bị ban, bài kịp đủ thời gian để người ta thấy. **Đơn hàng đầu tiên đến vài phút sau bài Reddit đầu tiên.**
5. Chuyển sang các sub về **entrepreneur** — nơi *"bạn được phép khoe project, tự quảng bá, và **đăng link mà không bị block**"*.
6. Tuần đầu tiên: **150 người dùng**.

**Bài học vận hành, không phải bài học truyền cảm hứng:**

- Sub đúng ICP (r/travel) thường là sub **cấm quảng cáo gắt nhất**. Sub cho phép quảng bá (r/entrepreneur, r/SideProject) lại **không phải ICP** — người ở đó là founder khác, không phải khách hàng. Denis dùng cả hai với hai mục đích khác nhau: sub ICP để **lấy đơn hàng đầu tiên và xác thực**, sub founder để **lấy volume bền vững**.
- Bị ban không phải thất bại nếu bài đã kịp chạy. Chi phí của việc bị ban là một tài khoản; giá trị là tín hiệu xác thực.
- **Ảnh chụp tính năng lõi > mô tả dài.** Denis nói chính giao diện sạch làm bài nổi bật.

So sánh với [Gojiberry AI dùng Reddit lên $34K/tháng](../2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/case.md) — cùng kênh nhưng Gojiberry chơi dài hạn còn Denis chơi cửa sổ tin tức. Điều kiện phân định: **nếu bạn có một sự kiện tin tức đang nóng, Reddit trả tiền ngay; nếu không, Reddit đòi bạn phải xây uy tín trong sub trước hàng tháng trời.**

![Lấy người dùng chỉ sau một đêm](screenshots/06_06m42s_ch-how-to-get-users-overnight.jpg)

## 6. Playbook 5 bước của Denis ⭐⭐⭐

Khi được hỏi "nếu làm lại từ đầu hôm nay":

### Bước 1 — Tìm thị trường mà đối thủ là khủng long

> *"Bước đầu tiên là **tìm một thị trường nơi đối thủ của bạn là khủng long**. Họ cổ lỗ và chậm chạp. Yadaphone không phải app duy nhất trên thị trường gọi quốc tế. Tôi có đối thủ và họ đã ở đó **20, có khi 30 năm**. Nhưng những công ty kiểu đó rất chậm thay đổi và thích nghi. Những thị trường đó **có nhu cầu đã được xác thực**, và bạn có thể làm usability với design tốt hơn họ rất nhanh."*

Đây là dạng ngách hay nhất cho indie hacker: **cầu đã có, đối thủ không thể chết nhưng cũng không thể chạy nhanh**. Khác hẳn ngách AI nơi mỗi tuần có 50 đối thủ mới. Cùng logic với [Packager — SaaS chán nhất internet, $60K/tháng](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md) và [Savvy Nomad](../2026-05-21_i-make-1-7m-year-in-the-most-boring-niche-imaginable/case.md).

### Bước 2 — Build MVP thật nhanh rồi đăng khắp nơi

MVP không cần hoàn hảo. Nhưng Denis nêu ba điều kiện cứng:

- **Design và usability phải ăn được** — vì đó là toàn bộ lợi thế so với khủng long.
- **Tính năng lõi phải chạy ngon.** Với Yadaphone, tính năng lõi chỉ là: gọi được một cuộc ra ngoài từ app.
- **Phải có một câu chuyện kể được.** Câu chuyện của Denis: *"một kỹ sư đơn độc đứng lên thế chỗ một công ty khổng lồ."*

> *"Điều này đặc biệt quan trọng với Reddit vì người ta ở đó cuộn rất nhanh và họ sẽ bỏ qua thứ không thú vị với họ."*

### Bước 3 — Khi ông lớn rút lui, đi cướp backlink của xác chết ⭐⭐⭐

Đây là chiêu hay nhất trong toàn bộ case, và tôi chưa thấy ai khác trong kho này làm:

> *"Khi một đối thủ lớn rời đi, **vẫn còn rất nhiều bài viết nhắc tới họ**. Và đó là cơ hội tuyệt vời để xếp hạng cho những từ khoá mà bạn sẽ không bao giờ có cơ hội nếu không có website domain authority cao."*

Quy trình cụ thể:

1. Liệt kê từ khoá muốn xếp hạng — ví dụ *Skype alternative*.
2. Tìm các **bài blog đang xếp hạng** cho từ khoá đó.
3. Tìm **tác giả** của những bài đó — qua X, LinkedIn, hoặc email.
4. Viết thẳng cho họ, hỏi có thể **nhắc tới Yadaphone** không.
5. Kết quả: *"Họ hoặc đồng ý thêm công cụ của tôi vào bài, **hoặc thay hẳn Skype bằng Yadaphone**."*

> *"Điều này thấy như điên rồ vì **Yadaphone thay thế một thương hiệu khổng lồ đã có tên tuổi**, và rõ ràng nó kéo rất nhiều traffic về website của tôi."*

**Vì sao chiêu này hiệu quả — cơ chế:** một bài blog đang xếp hạng cho *Skype alternative* mà vẫn liệt kê Skype thì **bài đó đã lỗi thời** và tác giả biết điều đó. Bạn không xin xỏ; bạn **đang giúp họ cập nhật nội dung để giữ thứ hạng**. Động cơ của hai bên trùng nhau — đó là lý do tỷ lệ đồng ý cao bất thường so với cold outreach xin backlink thông thường.

**Khi nào hết hiệu quả:** cửa sổ chỉ mở khi có một cái tên lớn vừa chết. Sau 12-18 tháng, các bài đó đã được cập nhật bằng tên khác. Nếu bạn đang đọc case này và tìm một cái tên vừa bị khai tử — đó chính là bài tập.

### Bước 4 — Nhắn tin cho từng khách trả tiền, suốt 6 tháng

> *"Tôi từng **nhắn tin cho từng khách hàng trả tiền một** suốt 6 tháng để xin feedback. Tôi chỉ nói: **Chào, tôi là Denis, founder của Yadaphone. Tôi rất muốn biết bạn nghĩ gì về app và trải nghiệm của bạn tới giờ thế nào.**"*

Hai lợi ích anh nêu, và cái thứ hai ít người nói ra:

1. Biết được **phân khúc người dùng nào** app phục vụ tốt nhất. (Chính từ đây anh phát hiện mảng B2B.)
2. **Bắt review xấu trước khi nó thành review công khai** — bạn có cơ hội xử lý trải nghiệm tệ trước khi người ta đi đánh giá 1 sao.

Anh cũng thẳng thắn: *"Việc này tốn thời gian và bạn không phải lúc nào cũng đủ năng lượng cho nó."*

### Bước 5 — Làm bản B2B càng sớm càng tốt ⭐⭐⭐

> *"Enterprise **cheque to hơn và churn thấp hơn nhiều**."*

Câu chuyện đằng sau vui và rất thật:

> *"Tôi tạo ra gói enterprise **hoàn toàn do tai nạn**. Một anh nhắn tôi lúc nửa đêm hỏi Yadaphone có gói enterprise cho tổ chức của anh ta không. Tôi nói: **Tất nhiên là có.** Và tiết lộ bí mật: **chúng tôi không có.** Tôi code gói enterprise trong trạng thái hoảng loạn suốt đêm đó, vì sáng hôm sau tôi phải demo trực tiếp cho khách. Nhân tiện, anh ta **vẫn là khách của Yadaphone, trả khoảng $1.000 mỗi tháng**."*

Đối chiếu số học: **1 khách enterprise = $1.000/tháng**. Trong khi đó 4.500 khách cá nhân + 20 enterprise tạo ra $14K/tháng. Nếu một khách enterprise là $1.000 thì 20 khách enterprise có thể chiếm phần rất lớn doanh thu — video không tách bạch, nhưng cấu trúc này nói lên điều gì đó quan trọng: **app B2C có thể là kênh tìm khách B2B**.

![Playbook của Denis](screenshots/08_08m51s_ch-denis-successful-app-playbook.jpg)

## 7. Kinh tế đơn vị: 35% doanh thu chảy về Twilio ⭐⭐

Đây là phần Starter Story lướt qua nhưng bạn **không được lướt qua**:

> *"Chi phí chính của tôi là **Twilio**, thứ xử lý các cuộc gọi, và tôi trả họ **khoảng 35% thu nhập hàng tháng**."*

| So sánh | SaaS phần mềm thuần | Yadaphone |
|---|---|---|
| Gross margin điển hình | 85-95% | **~65%** trước mọi chi phí khác |
| COGS biến động theo doanh thu | Gần như không | **Tuyến tính** — càng nhiều cuộc gọi càng nhiều tiền cho Twilio |
| Rủi ro nhà cung cấp | Thấp | **Cao** — Twilio đổi giá là biên lợi nhuận đổi theo |

Nghĩa là $14.000/tháng doanh thu thực chất chỉ còn **~$9.100 gross profit**, chưa trừ Stripe (~3%), Vercel, Ahrefs, Cursor. Đây vẫn là con số rất tốt cho một người, nhưng **đừng đọc $14K như $14K của một SaaS thuần**.

**Rủi ro nghiêm trọng chưa được nhắc trong video:** ngành VoIP quốc tế có yêu cầu pháp lý (KYC, chống gian lận cước, quy định viễn thông từng nước) và nạn **toll fraud** — kẻ xấu chiếm tài khoản để gọi tới các số premium, hoá đơn Twilio nổ trong vài giờ. Một founder solo đang chạy mô hình nạp credit là mục tiêu điển hình. Video không đề cập chuyện này chút nào.

![Một khách enterprise trả $1.000/tháng](screenshots/09_11m45s_usd-1-000.jpg)

## 8. Tech stack và cách solo mà vẫn sống

| Hạng mục | Công cụ |
|---|---|
| Framework | **Next.js** (trước đó anh dùng React/JS/HTML/CSS thuần) |
| Code + viết copy | **Cursor** |
| Hosting | Vercel |
| Thanh toán | Stripe |
| Hạ tầng gọi | **Twilio** (~35% doanh thu) |
| SEO / keyword | Ahrefs |

Denis thừa nhận về AI coding: *"Tôi dùng Cursor và LLM nhưng **nó không phải lúc nào cũng đẹp**. Tôi phải sửa nhiều thứ và chỉnh tay khá nhiều ở phần design."* — Một câu trung thực hiếm gặp trên kênh này, nơi mọi thứ thường được kể như AI làm hết.

**Cách anh giữ được trạng thái solo:**

> *"Với AI thì rất dễ tự build giải pháp riêng. Tôi tự build **hệ thống xử lý yêu cầu hỗ trợ và admin panel** bằng Cursor. Tôi bắt được phần lớn yêu cầu hỗ trợ từ sớm nên có thể điều tiết luồng công việc. Tôi hiệu quả với support và **nhờ đó đủ sức ở lại làm solo founder**."*

Đây là mẫu hình đáng chú ý: **AI không dùng để build sản phẩm, mà để build công cụ nội bộ giữ cho headcount = 1**. Cùng ý với [Fastlane](../2026-08-30_the-insanely-obvious-secret-behind-this-69k-month-sa/case.md) và [Once](../2026-05-10_i-built-a-20k-month-app-in-83-days/case.md).

## 9. Lời khuyên cuối: SEO từ ngày 1 — và cái bug $-nhiều-tháng ⭐⭐

> *"Tôi khuyên làm SEO **từ ngày đầu tiên** và phải rất kiên nhẫn. Tôi nghĩ SEO là **phép thuật thuần tuý với hầu hết developer** vì nó không tự nhiên với chúng ta. Chúng ta quen với vòng phản hồi nhanh — bạn đổi một thứ trong editor, vài giây sau thấy thay đổi trên localhost. Với SEO thì không. Thay đổi mất **hàng tuần, có khi hàng tháng**, nhưng nó trả lại rất đáng."*

Rồi anh kể cái bug đáng giá:

> *"Đối thủ của tôi bắt đầu xếp hạng tốt hơn cho chính những từ khoá tôi nhắm, **dù tôi là người đầu tiên trên thị trường**. Tôi soi lại SEO, chat rất nhiều với ChatGPT về nó, và hoá ra đó là **một chi tiết nhỏ ngu ngốc: sitemap của tôi không có tiền tố www**, và Google đơn giản là bỏ qua toàn bộ các trang tôi muốn xếp hạng."*

**Đây là bài học đắt nhất về mặt kỹ thuật trong case:** anh có lợi thế first-mover, có backlink cướp được từ Skype, và vẫn thua vì một dòng cấu hình. Hãy đi kiểm tra `sitemap.xml`, `robots.txt` và canonical domain của bạn hôm nay.

**Mâu thuẫn nội bộ trong chính case này — và cách hoà giải:** Denis có đơn hàng **trong vài phút** nhờ Reddit, nhưng lời khuyên cuối cùng của anh lại là **SEO, kênh chậm nhất**. Không mâu thuẫn nếu hiểu đúng vai trò:

| Kênh | Vai trò | Thời gian có kết quả |
|---|---|---|
| Reddit + X lúc launch | **Xác thực** và tiền mặt ngay | Vài phút tới vài ngày |
| Cướp mention trong bài blog cũ | **Bơm authority** khi cửa sổ tin tức còn mở | Vài tuần |
| SEO | **Nền doanh thu** khi cửa sổ đã đóng | Vài tháng |

Nếu chỉ chạy Reddit, doanh thu chết khi tin tức nguội. Nếu chỉ chạy SEO, bạn chết đói trong 6 tháng đầu. Case này thắng vì chạy cả ba **theo đúng thứ tự**.

![Xây app trong một cuối tuần](screenshots/05_05m20s_ch-building-the-app-in-a-weekend.jpg)

## 10. Cảnh báo thiên kiến nguồn

- Video này **quảng cáo Starter Story Build khá lộ liễu** — chèn giữa video, ngay sau đoạn "anh build trong một cuối tuần", và lặp lại ở cuối. Câu chuyển tiếp *"đây chính xác là những gì chúng tôi làm trong Starter Story Build"* gắn thành công của Denis với khoá học của kênh, dù Denis **không hề dùng khoá đó** và anh tự học code trong 2 tháng bằng sách trước khi có AI coding.
- Kênh chỉ phỏng vấn người thành công. **Không ai đếm được bao nhiêu người cũng thấy tweet của Pieter Levels, cũng build bản thay thế Skype, và không ai mua.** Cái tweet đó được hàng trăm nghìn người đọc.
- Con số $15K MRR trong mô tả video **không được founder xác nhận trong video**.

## 11. Áp dụng cho tôi (indie hacker VN)

**Sao chép được gì — cụ thể:**

1. **Lập danh sách theo dõi các sản phẩm sắp bị khai tử.** Google Graveyard, thông báo sunset của Microsoft/Google/Meta/Atlassian, các thông báo "end of life" trên changelog. Đây là **nguồn ý tưởng có sẵn cầu**, không phải ý tưởng bạn phải tự nghĩ ra. Đặt alert cho cụm *is shutting down*, *end of life*, *sunset*.
2. **Chiêu cướp mention áp dụng được ngay, không cần sản phẩm sắp chết nào cả.** Tìm bài blog "top 10 công cụ X" đang xếp hạng, xem bài nào **còn liệt kê sản phẩm đã chết hoặc đã đổi giá**, viết cho tác giả. Bạn đang giúp họ, không xin họ. Tỷ lệ hồi đáp cao hơn cold outreach thường rất nhiều.
3. **Hai loại subreddit, hai mục đích.** Sub ICP để xác thực (chấp nhận bị ban), sub founder để chạy volume.
4. **Nhắn từng khách trả tiền trong 3-6 tháng đầu.** Đây là cách rẻ nhất để phát hiện mảng B2B ẩn trong app B2C của bạn.
5. **Nói có với deal enterprise trước, code sau.** Denis code cả đêm cho một demo sáng hôm sau và có khách $1.000/tháng. Rủi ro thấp hơn bạn nghĩ nếu deal đủ lớn.
6. **Kiểm tra sitemap và canonical domain hôm nay.**

**Rào cản thật — không tô hồng:**

- **Đây không phải mô hình phần mềm thuần.** 35% doanh thu chảy về Twilio. Nếu bạn định làm VoIP/SMS/telecom, hãy dựng bảng tính unit economics **trước** khi viết dòng code đầu tiên, và mô hình cả kịch bản Twilio tăng giá.
- **Toll fraud là rủi ro có thể xoá sổ bạn.** Mô hình nạp credit + gọi quốc tế là mục tiêu ưa thích của gian lận cước. Bạn cần rate limit, KYC, chặn dải số premium, và một hạn mức chi tiêu cứng trên Twilio ngay từ ngày đầu. Video **không nói gì về chuyện này** — đó là lỗ hổng lớn nhất của case.
- **Rào cản pháp lý viễn thông ở VN.** Cung cấp dịch vụ gọi thoại quốc tế cho người dùng tại Việt Nam đụng vào quy định về dịch vụ viễn thông. Nếu làm mô hình này, **nhắm khách quốc tế và đặt pháp nhân ngoài VN** — đừng bán cho thị trường trong nước.
- **Rào cản tiếng Anh ở mức trung bình-cao.** Toàn bộ chiêu bước 3 là **cold email cho biên tập viên blog tiếng Anh**. Email dở sẽ bị bỏ qua. Đây là kỹ năng viết, không phải kỹ năng code.
- **Cửa sổ timing không thể lên lịch.** Bạn không quyết định được khi nào Microsoft giết một sản phẩm. Chiến lược thực tế là: **có sẵn kỹ năng ship trong một cuối tuần**, rồi chờ. Nghĩa là bạn cần một nguồn thu khác trong lúc chờ — Denis freelance.
- **Vốn cần có: rất thấp.** Đây là điểm sáng. Vercel, Stripe, Cursor, Ahrefs — dưới $200/tháng. Twilio trả sau theo usage. Không cần quảng cáo.

**Khi nào KHÔNG dùng mô hình này:**

- Khi **không có sự kiện tin tức nào** đang mở cửa sổ. Chạy playbook này trong một thị trường yên ả nghĩa là bạn chỉ là app thứ 200 trong ngách, không có cầu tồn dư, không có từ khoá trống, không có story để kể trên Reddit. Khi đó hãy dùng mô hình chậm mà chắc như [FollowBuddy YouTube search](../2026-03-19_i-make-17k-month-with-one-strategy/case.md) hoặc [BulkMockup](../2026-02-11_how-i-built-a-12k-month-micro-saas/case.md).
- Khi bạn **chưa từng ship xong một sản phẩm nào**. Cuối tuần của Denis dựa trên nhiều năm project chết. Nếu đây là app đầu tiên của bạn, một cửa sổ timing sẽ đóng trước khi bạn kịp deploy.
- Khi sản phẩm có **COGS biến động cao mà bạn không kiểm soát giá bán** — telecom, inference AI, vận chuyển. Ở quy mô nhỏ bạn không có đòn bẩy đàm phán với nhà cung cấp, và mọi tăng trưởng đều kéo theo chi phí tăng tuyến tính.

## Nguồn

- Video: <https://www.youtube.com/watch?v=88BbTpbWVpY> (14:24, đăng 16/10/2025, 92.066 view)
- Sản phẩm: <https://www.yadaphone.com>
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)

*Ghi chú về phụ đề tự động: ASR đọc tên sản phẩm thành Yaphone / Yataphone / Yodafone / Yafone và tên founder thành Dennis. Tên đúng theo mô tả video là **Yadaphone** (yadaphone.com) và **Denis Yurchak**. ASR cũng đọc Next.js thành Nex.js, Cursor thành Corser, Pieter Levels thành Peter Levelvels.*
