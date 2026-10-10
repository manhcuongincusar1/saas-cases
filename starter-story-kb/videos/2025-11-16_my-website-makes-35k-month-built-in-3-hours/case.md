---
id: LWPN-PAhtLA
slug: cursor-directory-open-source-directory
product: Cursor Directory (cursor.directory)
founder: Pontus Abrahamsson và Victor (co-founder của Midday)
tagline: Directory mã nguồn mở về cursor rules — build 3 tiếng, biên lãi gộp 99,8%, bảo trì 3 tiếng MỖI THÁNG vì cộng đồng tự đóng góp nội dung qua GitHub
revenue_usd_month: 34000
revenue_basis: founder nói 35K trong hook, Pat Walls và ảnh dashboard đều ghi 34.000 USD. Tôi lấy 34.000 vì có ảnh dashboard xác nhận; con số 35K nhiều khả năng là làm tròn lên
model: directory-ads-listings (bán job ads và vị trí featured, không phải subscription)
category: developer-tools / directory
audience: B2C-dev — lập trình viên dùng Cursor tìm rules và MCP; bên trả tiền là công ty tuyển dụng và công ty dev tool
started: ý tưởng nảy ra trên chuyến bay 3 tiếng sang Pháp; build ngay khi hạ cánh
time_to_first_sale: không nêu; viral ngay tuần đầu
time_to_scale: dưới 1 tuần để có traffic lớn — nhưng đứng trên 2 năm build in public trước đó
team_size: 2 (đều đang làm toàn thời gian cho startup chính là Midday)
funding: bootstrapped
main_channel: X (build in public, khoảng 1 triệu impression trên một post), Hacker News trang nhất, YouTuber đưa tin lại
tech_stack: [Next.js, TypeScript, shadcn/ui, Resend, OpenPanel, Vercel, Polar, Cursor, Notion, GitHub]
key_metrics:
  registered_users: 49.000
  unique_visitors: 2.200.000 kể từ khi launch
  gross_margin: 99,8%
  operating_cost: 500-525 USD/tháng
  build_time: 3 tiếng cho bản đầu tiên
  maintenance: 3 tiếng/tháng
  launch_impressions: khoảng 1 triệu trên một post X
replicability_vn: 3
difficulty: 3
video_url: https://www.youtube.com/watch?v=LWPN-PAhtLA
published: 2025-11-16
views: 91055
---

# Cursor Directory — $34K/tháng từ một website build trong 3 tiếng, bảo trì 3 tiếng mỗi tháng

> **Tóm tắt 30 giây:** Pontus Abrahamsson chán trên chuyến bay 3 tiếng sang Pháp, xem mấy video về Cursor và nhận ra **không có chỗ nào tập hợp cursor rules lại một nơi**. Vừa hạ cánh anh gọi cho co-founder Victor. Victor mở Figma, Pontus mở Next.js với một file JSON hard-code — **nửa tiếng sau đã có bản chạy được trên Vercel**, ba tiếng sau là website hoàn chỉnh. Giờ nó có **2,2 triệu lượt khách, 49.000 người đăng ký, $34.000/tháng, biên lãi gộp 99,8%** và họ chỉ đụng vào nó **3 tiếng mỗi tháng** — vì directory là **mã nguồn mở**, cộng đồng tự merge rules qua GitHub. Nhưng "3 tiếng" là con số gây hiểu lầm nhất trong video: cú launch chỉ nổ được nhờ **2 năm build in public** trước đó.

![$34.000/tháng](screenshots/01_00m53s_usd-34-000.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$34.000/tháng (founder nói 35K, dashboard ghi 34K) |
| Người đăng ký | 49.000 |
| Lượt khách unique | 2.200.000 kể từ khi launch |
| **Biên lãi gộp** | **99,8%** |
| Chi phí vận hành | ~$500-525/tháng |
| Thời gian build bản đầu | **3 tiếng** |
| Thời gian bảo trì | **3 tiếng/tháng** |
| Impression khi launch | ~1 triệu trên một post X |

**Hai điểm không nhất quán nhỏ trong video:**

1. Founder mở đầu bằng *"we built it in a weekend"* rồi sau đó nói *"we built the site completely in three hours"*. Hiểu đúng: **3 tiếng cho bản đầu chạy được, cuối tuần đó tiếp tục iterate.**
2. Chi phí vận hành lúc đầu nói *"just under 500 bucks"*, cuối video nói *"all in all 525 bucks a month"*. Chênh lệch không đáng kể.

## 2. Nguồn gốc ý tưởng — nhận diện khoảng trống, không phải sáng tạo ý tưởng ⭐⭐

> *"The whole idea came up when I actually took the flight down to move to France. It's a three-hour flight and I downloaded a lot of videos to look on tech heavy stuff... I discovered this common pattern about rules. So it was kind of mind-blowing for me that there were no place to find these rules in one specific place. You could Google and find some obscure gist on GitHub or some forums, but no real clear answer to finding these rules in one place."*

Phân tích cơ chế: đây **không phải** một ý tưởng sáng tạo. Đó là việc phát hiện ra một thứ **đang tồn tại rải rác** mà **chưa ai gom lại**. Ba điều kiện được thoả mãn cùng lúc:

1. **Thứ cần gom đang phân mảnh** — nằm rải trong gist GitHub, forum, video YouTube.
2. **Có một lượng người đang tăng rất nhanh đi tìm nó** — Cursor lúc đó đang bùng nổ.
3. **Nguồn nội dung miễn phí** — rules là thứ cộng đồng tự viết và sẵn sàng chia sẻ.

Điều kiện thứ 3 là điều kiện giết chết hầu hết directory khác, và tôi tách nó ra thành một mục riêng ở dưới.

![Cách Pontus tìm ra ý tưởng](screenshots/03_03m25s_ch-how-pontus-found-the-idea.jpg)

## 3. Cơ chế thật khiến case này hoạt động — chi phí nội dung bằng 0 ⭐⭐⭐

Ai cũng bị hút vào con số "3 tiếng". Con số đáng giá hơn nhiều là **3 tiếng mỗi THÁNG**.

> *"Of course it's open source. All the rules are merged on in GitHub. So the maintenance cost is like 3 hours per month and then we continue building our main startup."*

**Vì sao đây mới là bí quyết:** một directory không chết vì khó build. Nó chết vì **nội dung bị mốc**. Bạn phải liên tục thêm mục mới, kiểm tra link hỏng, cập nhật thông tin — và đó là công việc thủ công vô tận không ai trả tiền cho bạn. Đó là lý do 90% directory bị bỏ hoang sau 6 tháng.

Pontus giải quyết bằng cách **biến nội dung thành mã nguồn mở**. Người dùng đóng góp rule mới bằng cách gửi pull request lên GitHub. Kết quả:

- Chi phí sản xuất nội dung: **0**
- Chi phí kiểm duyệt: gần như bằng 0 (merge PR)
- Nội dung tự tươi mới theo tốc độ của cộng đồng, không theo tốc độ của founder
- Tạo thêm **hào bảo vệ**: người đã đóng góp có động cơ quay lại và giới thiệu

Đây cũng là lý do biên lãi gộp đạt **99,8%** — không có COGS, không có đội vận hành, không có nội dung phải mua.

**Đây là điều bạn phải copy.** Nếu bạn định làm directory, câu hỏi đầu tiên không phải "tôi build thế nào" mà là: **ai sẽ cập nhật nội dung này thay tôi, và vì sao họ chịu làm?** Nếu không trả lời được, đừng làm.

So sánh trong kho: [Postiz](../2026-01-28_how-i-built-it-17k-month-open-source-saas/case.md) dùng mã nguồn mở làm **kênh phân phối**; Cursor Directory dùng mã nguồn mở làm **dây chuyền sản xuất nội dung**. Hai công dụng khác nhau của cùng một chiến lược.

## 4. Build MVP — 30 phút để có thứ bấm được ⭐⭐

> *"In just a matter of minutes, he spun up Figma and started to design while I started initial project with Next.js and I created a hard-coded JSON file with some rules that I found online. And in a matter of like half an hour we had something up in Vercel ready to click around on."*

Ba chi tiết kỹ thuật đáng học:

1. **File JSON hard-code, không database.** Bản đầu tiên không có backend, không có CMS. Nội dung nằm thẳng trong repo. Đây cũng chính là thứ về sau cho phép mở mã nguồn — vì nội dung *là* code.
2. **Deploy lên Vercel trong 30 phút** để có thứ *bấm được* trước khi hoàn thiện. Có thứ bấm được sớm là cách duy nhất để hai người đồng bộ ý tưởng nhanh.
3. **Mua domain cursor.directory ngay** — anh nói đó là *"a really really good domain"*. Domain khớp chính xác từ khoá là tài sản SEO miễn phí.

Anh cũng thẳng thắn về lý do họ nhanh được đến vậy:

> *"Victor and I have been working together for several years. We already know our DNA in terms of design and code. So that helped a lot of course."*

Và về hệ thống thiết kế: *"We already have a design system. We already have components that we can reuse from our previous startups."* **3 tiếng đó được xây trên nhiều năm tích luỹ component và ăn ý.**

![Build MVP](screenshots/04_04m02s_ch-building-the-mvp.jpg)

## 5. Launch — và phần video không nói thẳng ⭐⭐⭐

Cách họ launch:

- Đăng lên **X** khi ra mắt → **~1 triệu impression** trên một post, và họ đăng nhiều post
- Lên **trang nhất Hacker News**
- **Nhiều YouTuber** đưa cursor.directory vào video của họ

> *"We're building in public on X. We share everything we do all the way to the code, right? We are fully open source. So I think we had like 1 million impressions on one of the posts... We have a developer following from the beginning."*

**Đây là chỗ tôi phải nói thẳng, vì video không nói:** cụm *"we have a developer following from the beginning"* đi lướt qua trong nửa giây, nhưng nó là **biến số quyết định toàn bộ kết quả**. Pontus và Victor đã dành **hai năm build in public** cho Midday trước đó. Cái mà anh gọi là launch trong 3 tiếng thực chất là **rút tiền từ một tài khoản uy tín đã gửi tiết kiệm suốt 2 năm**.

Nếu bạn build đúng directory đó, đúng thời điểm đó, với 40 follower, nó sẽ không nổ.

**Nhưng đừng rút ra kết luận sai.** Kết luận đúng không phải "tôi không làm được vì không có audience". Kết luận đúng là: **trong mô hình này, audience là điều kiện tiên quyết, nên hãy bắt đầu xây nó TRƯỚC — song song với công việc chính**, đúng như họ đã làm. Đây cũng chính là điểm mà [Ben của FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md) phản bác gay gắt trong một case khác: anh gọi suy nghĩ "anh làm được vì đã có kênh" là niềm tin tự giới hạn, vì anh xây kênh bằng đúng những việc anh đang chỉ. Cả hai đều đúng — chỉ khác ở **thời gian**. Ben mất nhiều năm xây kênh YouTube; Pontus mất 2 năm build in public. Không ai có được nó miễn phí.

**Nếu bạn KHÔNG có audience**, con đường thay thế cho directory là **SEO** thay vì launch nổ: domain khớp từ khoá, nội dung có cấu trúc, và kiên nhẫn 6-12 tháng. Chậm hơn nhiều, nhưng không cần ai biết bạn là ai. Đây là con đường của [AngelMatch và InvestorHunt](../2026-08-23_i-make-32k-month-from-3-simple-boring-websites/case.md) và của [DuckMath](../2026-03-01_i-make-15k-month-from-one-website/case.md).

![Chiến lược launch](screenshots/06_05m39s_ch-pontus-launch-strategy.jpg)

## 6. Kiếm tiền thế nào — không phải subscription ⭐⭐⭐

Đây là mục mà nhiều người xem bỏ qua nhưng lại là mô hình kinh doanh thật:

| Nguồn thu | Cơ chế |
|---|---|
| **Job ads** | Công ty trả tiền để đăng tin tuyển dụng, hiển thị trong một số tháng |
| **Featured listings** | MCP và các mục khác trả tiền để được đưa lên vị trí nổi bật |
| Cộng đồng | Đăng ký tài khoản, đăng nội dung riêng, vote — **miễn phí**, dùng để nuôi traffic và nội dung |

**Cơ chế kinh tế:** Cursor Directory không bán phần mềm. Nó bán **sự chú ý của một nhóm người rất cụ thể và rất đắt giá — lập trình viên đang dùng công cụ AI**. Người trả tiền không phải người dùng, mà là **công ty muốn tiếp cận người dùng đó**.

Đây là lý do biên lãi 99,8% khả thi: bạn không bán thứ gì có chi phí biến đổi. Bạn bán vị trí trên một trang web.

**Điều kiện để mô hình này chạy:** khán giả của bạn phải là nhóm mà **ai đó sẵn sàng trả tiền để tiếp cận**. Developer, marketer, chủ doanh nghiệp, nhà đầu tư — có. Học sinh, người xem giải trí chung chung — gần như không (họ phải chuyển sang AdSense với eCPM thấp hơn nhiều lần).

**Con sóng thứ hai — MCP:** đây là chi tiết chiến lược hay nhất trong video.

> *"Some months after, MCPs came along and that were also a thing that made Cursor Directory really really fly. So that was the second way where we saw a huge adoption of the site, because we created this MCP searchable way to find and extend your Cursor experience."*

Khi MCP xuất hiện, họ **không xây sản phẩm mới**. Họ thêm một danh mục vào directory sẵn có và bắt trọn làn sóng thứ hai. Một directory đã có traffic là **bệ phóng để bắt mọi làn sóng tiếp theo trong cùng hệ sinh thái** — chi phí gần bằng 0, lợi ích cộng dồn.

Họ cũng thêm tính năng **upload package.json để sinh cursor rules riêng cho dự án của bạn** — biến directory tĩnh thành công cụ có tương tác, tăng lý do quay lại.

## 7. Thiết kế là lợi thế cạnh tranh trong thời AI ⭐⭐

Pat Walls nhận xét rằng thiết kế của cursor.directory chính là lý do nó được chia sẻ nhiều. Pontus trả lời:

> *"Design is more important than ever, especially in this fast-paced AI generated website world that we started to live in. Design will actually be the thing that puts you apart from the competitors, right? Because it's easy to create a website today, but all of them usually look the same."*

**Cơ chế đằng sau:** khi AI hạ chi phí build về gần 0, **build không còn là hào bảo vệ**. Thứ còn lại là những gì AI làm ra đồng loạt giống nhau — và thiết kế có gu là một trong số đó. Với sản phẩm phụ thuộc vào việc được **chia sẻ** (như directory), thiết kế không phải trang trí, nó là **cơ chế phân phối**: người ta screenshot và post lên X những thứ đẹp, không post những thứ trông như template.

Công thức của anh cho người mới:

- **Keep it simple.** Những thứ nhỏ mới là thứ khó nhất.
- **Tìm những website bạn thực sự thích, lấy từng mảnh, học từ đó.**
- **Tìm ra tonality và góc nhìn bạn tin là đúng** — đó mới là lợi thế, không phải hiệu ứng.
- Theo dõi designer giỏi trên X, cộng đồng đó rất lớn.

![Thiết kế với AI](screenshots/07_06m45s_ch-designing-with-ai.jpg)

## 8. Directory năm 2025 đã chết chưa?

Pat hỏi thẳng vì đây là quan niệm phổ biến. Pontus:

> *"Directories still are incredibly successful in 2025, especially if you build something for the right audience... Cursor Directory solves a timeless problem — you need to find something that you're interested in. And in this new AI world where we live in, like Cursor, people are starting to look through how to do things and find the right answers. That's where directories really really shine. It's a collection of things that a bigger audience are interested in at the same time. And if you can catch that wave, if you can own it, then it's super powerful."*

**Phân tích trung thực của tôi:** câu trả lời này đúng nhưng chưa đủ. Directory không chết, nhưng **loại directory sống được đã thu hẹp lại rất nhiều**. Điều kiện để một directory năm nay còn ăn được:

| Điều kiện | Cursor Directory có? |
|---|---|
| Gắn với một **công nghệ đang bùng nổ**, nơi thông tin còn hỗn loạn | Có — Cursor và MCP |
| Nội dung do **cộng đồng đóng góp**, không phải founder cày tay | Có — mã nguồn mở |
| Khán giả là nhóm mà **có người sẵn sàng trả tiền để tiếp cận** | Có — developer |
| Có **kênh phân phối sẵn** để nổ ngày launch, hoặc chấp nhận đi đường SEO dài | Có — 2 năm X following |

Thiếu bất kỳ điều nào trong bốn điều trên, xác suất thành công tụt rất mạnh. Một directory "top 50 công cụ AI" chung chung năm nay: thiếu cả 4.

**Rủi ro cấu trúc mà video không nói:** đây là **tài sản phái sinh trên tăng trưởng của một nền tảng khác**. Doanh thu của Cursor Directory phụ thuộc vào việc Cursor tiếp tục lớn và tiếp tục **không tự làm cái này**. Nếu Cursor ra registry rules chính chủ, hoặc nếu lập trình viên chuyển sang công cụ khác, giá trị của directory bốc hơi. Tên miền cursor.directory — vốn là tài sản SEO tuyệt vời — cũng chính là **xiềng xích**: nó không di chuyển sang hệ sinh thái khác được. Hãy đối xử với dòng tiền này như **tiền thuê**, không phải tài sản.

## 9. Tech stack — triết lý no servers, no friction

| Hạng mục | Công cụ |
|---|---|
| Framework | **Next.js**, toàn bộ **TypeScript** |
| UI components | **shadcn/ui** (ASR nghe thành *shing components*) |
| Email | **Resend** |
| Analytics | **OpenPanel** (ASR nghe thành *open paniful*) |
| Hosting | **Vercel**, nối thẳng với GitHub |
| Thanh toán | **Polar** — merchant of record, họ chọn vì là công ty châu Âu |
| IDE | **Cursor** |
| Quản lý sản phẩm | **Notion** |
| Version control | **GitHub** |
| **Tổng chi phí** | **$525/tháng**, biên lãi gộp **99,8%** |

> *"You should stick with something that you know and already use every day... Every tool we choose has the same philosophy: no servers, no friction, just focus on building and shipping fast."*

Hai điểm đáng chú ý cho người VN:

- **Polar là merchant of record**, nghĩa là họ đứng ra chịu trách nhiệm thuế VAT/sales tax thay bạn. Với người bán từ VN cho khách quốc tế, merchant of record (Polar, Paddle, Lemon Squeezy) giải quyết đúng bài toán khó nhất là thuế xuyên biên giới. Đây là chi tiết đáng giá hơn cả stack còn lại.
- **Không dùng công cụ mới để tỏ ra hiện đại.** Họ dùng lại đúng thứ đã dùng hằng ngày ở Midday. Đó là lý do 3 tiếng là con số khả thi.

## 10. Lời khuyên cuối

> *"Start. It sounds simple, but here's the thing. When you start building and when you commit to something, you eventually get dialed in. **You create your own luck by constantly finding ways to move forward, shipping, sharing, and iterate.** One thing will lead to another and there's really no such thing as failure."*

Anh cũng mô tả nhịp làm việc thật của họ, và đây là chi tiết dễ bỏ qua nhất:

> *"I have this main startup that we focus on day in and day out... Usually once a week or twice a week, we find these things that you can really do really really fast, but we hold off. But in this case, we didn't."*

**Nghĩa là:** mỗi tuần họ nhìn thấy 1-2 cơ hội kiểu này và **thường bỏ qua**. Cursor Directory là cái họ tình cờ không bỏ qua. Đây là lập luận mạnh cho việc **thỉnh thoảng cứ làm cái nhỏ**: tỉ lệ trúng thấp, nhưng chi phí một lần thử chỉ là 3 tiếng, còn phần thưởng thì không giới hạn trên.

## 11. Cảnh báo thiên kiến nguồn

Video 14 phút này có **hai đoạn quảng cáo dài** cho chính Starter Story: VIP list Black Friday (1:09-2:02) và khoá học Starter Story Build (8:03-9:04), cộng thêm một lần nữa ở cuối. Gần **2 phút rưỡi trên 14 phút** là bán hàng. Đây là video có tỉ lệ quảng cáo cao nhất trong ba case tôi viết cùng đợt.

Thông điệp được đóng gói — *"built in 3 hours"* — là thông điệp bán khoá học AI coding, và nó **cố ý làm mờ** phần khó thật của câu chuyện: 2 năm build audience, một design system tích luỹ nhiều năm, và một cặp co-founder đã ăn ý sau nhiều năm. Hãy đọc case này với sự tỉnh táo đó.

Kênh Starter Story đã được HubSpot mua lại và chỉ phỏng vấn người thành công.

## 12. Áp dụng cho tôi (indie hacker VN)

### Sao chép được gì

1. **Đây là mô hình có rào cản kỹ thuật thấp nhất trong kho.** Next.js, một file JSON, Vercel. Bạn dựng được bản đầu trong một buổi tối.
2. **Quy tắc vàng: chỉ làm directory nếu bạn trả lời được ai sẽ cập nhật nội dung thay bạn.** Cách của Pontus là mã nguồn mở. Các cách khác: cho phép người dùng tự submit (có kiểm duyệt), scrape hợp pháp một nguồn công khai, hoặc trả tiền cho mục được liệt kê. Không có cơ chế nào trong số đó thì directory của bạn sẽ chết trong 6 tháng.
3. **Săn hệ sinh thái đang bùng nổ và còn hỗn loạn.** Năm nay có nhiều: MCP servers, sub-agent, skills, các công cụ AI mới ra hằng tuần. Điều kiện là **thông tin đang phân mảnh** và **có người tăng nhanh đi tìm nó**.
4. **Mua domain khớp từ khoá.** cursor.directory là món hời SEO. Với thị trường VN, các domain khớp từ khoá tiếng Việt còn rất trống.
5. **Mô hình doanh thu job ads + featured listing đáng học riêng.** Không cần xây hệ thống subscription, không cần lo churn. Bạn bán vị trí. Nhưng nó chỉ chạy nếu khán giả của bạn là nhóm có người muốn mua sự chú ý.
6. **Dùng merchant of record (Polar, Paddle, Lemon Squeezy) ngay từ đầu** nếu bán cho khách quốc tế. Đây là cách gọn nhất để không vướng thuế xuyên biên giới.

### Rào cản thật

- **Audience là điều kiện tiên quyết bị giấu trong tiêu đề.** Không có nó, bạn phải đi đường SEO 6-12 tháng và chấp nhận không có cú nổ nào. Hãy lập kế hoạch cho đường dài đó thay vì mong một cú viral.
- **Hacker News và X là sân chơi tiếng Anh, và rất khó đoán.** Lên trang nhất HN không mua được và không lặp lại theo ý muốn. Đừng đưa nó vào kế hoạch tài chính.
- **Rủi ro nền tảng ở mức rất cao.** Bạn đang xây trên tăng trưởng của một công ty khác, với một domain không di chuyển được. Nếu Cursor ra registry chính chủ, doanh nghiệp này teo lại. Hãy coi doanh thu là tiền thuê.
- **Cửa sổ thời gian rất hẹp.** Giá trị nằm ở chỗ họ là người ĐẦU TIÊN gom cursor rules. Người thứ hai làm y hệt không có gì. Nghĩa là bạn phải **thường trực dò sóng**, và ra tay trong vài ngày chứ không vài tháng.
- **Bán quảng cáo và job ads đòi hỏi bán hàng B2B bằng tiếng Anh.** Bạn phải liên hệ công ty, báo giá, xuất hoá đơn. Đây là rào cản ngôn ngữ và quy trình thật, khác hẳn việc thu subscription tự động.
- **Thiết kế là lợi thế của họ, và có thể là điểm yếu của bạn.** Họ có một designer co-founder và một design system sẵn. Nếu bạn không mạnh về thiết kế, cơ chế "được chia sẻ vì đẹp" sẽ không kích hoạt.
- **Vốn cần có gần bằng 0** — đây là điểm sáng thật. $525/tháng, và ở quy mô nhỏ thì gần như miễn phí.

### Khi nào KHÔNG dùng mô hình này

- **Khi khán giả của bạn không phải nhóm ai đó muốn trả tiền để tiếp cận.** Nếu bạn chỉ có thể kiếm tiền bằng AdSense, hãy đọc [DuckMath](../2026-03-01_i-make-15k-month-from-one-website/case.md) thay vì case này — kinh tế học hoàn toàn khác.
- **Khi bạn phải tự sản xuất và tự cập nhật nội dung.** Đó không phải directory, đó là một công việc toàn thời gian lương thấp.
- **Khi hệ sinh thái đã ổn định.** Directory ăn được khi thông tin còn hỗn loạn. Khi thị trường đã có câu trả lời rõ ràng, không ai cần bạn gom lại nữa.
- **Khi bạn cần một tài sản bền để bán lại.** Directory phái sinh trên một nền tảng khác rất khó định giá cao, vì người mua nhìn ngay ra rủi ro tập trung.
- **Khi bạn cần doanh thu trong 30 ngày mà không có audience.** Không có kênh phân phối sẵn thì directory là trò chơi dài hạn, không phải nguồn tiền nhanh.

## Nguồn

- Video: <https://www.youtube.com/watch?v=LWPN-PAhtLA> (14:26, đăng 16/11/2025, 91.055 view)
- Sản phẩm: <https://cursor.directory>
- Founder trên X: <https://x.com/pontusab>
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
