---
id: 7vz6b_Ohdl0
slug: chartdb-open-source-devtool
product: ChartDB
founder: Jonathan Fishner
tagline: Công cụ trực quan hoá cơ sở dữ liệu, mã nguồn mở — miễn phí cho developer, thu tiền ở bản cloud; 21.000 sao GitHub
revenue_usd_month: 9400
revenue_basis: gần $9.400 MRR sau 16 tháng kể từ khi mở mã nguồn
model: open-source-cloud-upsell
category: developer-tools
audience: B2B/B2D — developer cần xem sơ đồ quan hệ (ERD) của database
started: mở mã nguồn 16 tháng trước thời điểm quay
time_to_first_sale: không thu tiền lúc đầu — chỉ bắt đầu bán khi người dùng đòi tính năng cộng tác
time_to_scale: 16 tháng lên ~$9,4K MRR
team_size: không nêu (có co-founder)
funding: bootstrapped
main_channel: Hacker News (Show HN lên trang chủ) → GitHub → Reddit self-hosted
tech_stack: [React, Vite, Node.js, Tailwind, React Flow, AWS, Stripe, Resend, Framer, ChartMogul, Ahrefs, Claude Code]
key_metrics:
  github_stars: hơn 21.000
  developers_reached: 250.000 trong một năm
  build_time_before_launch: 3 tuần
  monthly_costs: AWS 600 USD · Claude Code 200 USD · công cụ compliance 500 USD · analytics 25 USD · Framer 30 USD
  launch_result: hàng nghìn engineer trong đúng một ngày từ một bài Show HN
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=7vz6b_Ohdl0
published: 2026-02-25
views: 68896
---

# ChartDB — $9K MRR từ một công cụ nhỏ cho developer

> **Tóm tắt 30 giây:** Jonathan thất bại với ý tưởng đầu (database client tích hợp AI) vì nó đòi credentials, đòi cài đặt, và anh **không có uy tín để xin những thứ đó**. Anh xoay sang thứ đơn giản hơn nhiều: lấy database, biến thành sơ đồ. Mở mã nguồn, đăng **một bài Show HN** sau 3 tuần code, lên trang chủ Hacker News, **hàng nghìn engineer đổ về trong một ngày**. 16 tháng sau: **21.000 sao GitHub, 250.000 developer, ~$9.400 MRR** từ bản cloud.

> **Lưu ý về tên:** phụ đề tự động của YouTube đọc sai tên sản phẩm thành "Chartbrew"/"Charted Be". Tên đúng là **ChartDB** (xác nhận qua mô tả video và tiêu đề chương).

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR | ~$9.400 |
| Sao GitHub | Hơn **21.000** |
| Developer đã dùng | 250.000 trong một năm |
| Thời gian code trước khi ra mắt | **3 tuần** |
| Thời gian từ mở mã tới hiện tại | 16 tháng |

**Mô hình:** lõi mã nguồn mở, self-hosted, cài trên máy → miễn phí. Bản **cloud có trả phí** là nơi kiếm tiền. Developer tìm thấy qua GitHub, dùng miễn phí, và khi quy trình làm việc trở nên nghiêm túc hơn thì họ chuyển sang gói trả tiền.

![ChartDB là gì](screenshots/02_01m47s_ch-what-is-chartdb.jpg)

## 2. Ý tưởng đầu tiên thất bại — và vì sao ⭐⭐⭐

Đây là phần dạy nhiều nhất trong video.

Ý tưởng ban đầu: **database client có tích hợp AI**. Nó chết, và lý do rất cụ thể:

> *"Sản phẩm đó cần cấp quyền, họ cần credentials để kết nối vào database của bạn để chạy tất cả những truy vấn đó, và bạn cần cài gì đó lên máy. **Và không có uy tín và niềm tin từ các kỹ sư**, chúng tôi nói: thôi, khó quá."*

Anh chuyển sang: *"lấy database của bạn và biến nó thành một sơ đồ. Đơn giản vậy thôi."*

**Hai điều khiến phiên bản thứ hai chạy được:**

1. **Trực quan hơn nhiều** — người ta thấy giá trị ngay lập tức, *"tạo hiệu ứng wow tốt hơn"*.
2. **Giảm ma sát** — *"bạn không cần cấp bất kỳ quyền truy cập nào và bạn không cần cài phần mềm nào lên máy"*.

> **Nguyên tắc rút ra:** với sản phẩm cho developer, **ma sát tin cậy quan trọng hơn tính năng**. Người mới không có uy tín để đòi credentials. Hãy thiết kế sản phẩm sao cho nó chứng minh giá trị **trước khi** đòi hỏi bất cứ điều gì.

Gus bình luận rất đúng ở cuối video:

> *"Ý tưởng anh ấy có trước công cụ dev là cái AI wrapper cho SQL mà không chạy. Buồn cười là tôi thấy rất nhiều developer cố xây ý tưởng đó. Điều đó không có nghĩa nó nhất thiết là ý tưởng tệ. **Việc xây cái không chạy đó là cần thiết** rồi họ mới pivot."*

![Cách tìm ý tưởng dev tool](screenshots/03_02m37s_ch-how-to-find-developer-tool-ideas.jpg)

## 3. Bài Hacker News đổi đời ⭐⭐⭐

- Code **3 tuần** rồi quyết định ra mắt.
- Chuẩn bị, chọn ngày, đăng dưới dạng **Show HN**.
- Lên **trang chủ** → *"hàng nghìn kỹ sư đổ về sản phẩm trong cùng một ngày"*.

Pat nhận xét đúng mức, không thổi phồng:

> *"Một bài đăng trên một nền tảng có thể bắn doanh nghiệp của bạn lên. Nó sẽ không làm bạn thành triệu phú sau một đêm, nhưng **nó có thể là một thứ duy nhất thay đổi cuộc đời bạn**."*

**Vì sao bài đó chạy — theo lời Jonathan:**

1. **Developer trân trọng mã nguồn mở** vì họ có thể thử nghiệm mà *"không cần đăng ký và những thứ họ không thích"*.
2. **Phải có một wedge độc đáo** — *"nếu bạn đưa ra thứ gì đó độc đáo mà họ chưa từng thấy... họ sẽ thể hiện sự trân trọng bằng upvote, và những upvote đó đưa bạn lên trang chủ."*

![Vì sao bài Hacker News hiệu quả](screenshots/05_05m03s_ch-why-the-hacker-news-post-worked.jpg)

## 4. Playbook công cụ dev — 5 bước ⭐⭐⭐

![Playbook dev tools](screenshots/07_06m48s_ch-developer-tools-playbook.jpg)

**Bước 1 — Là người dùng; lý tưởng nhất là xây cho chính mình.**
Nếu là cho chính bạn, bạn thấy giá trị ngay và bạn thật sự hiểu cách làm vì bạn có kinh nghiệm trong lĩnh vực đó.

**Bước 2 — Thiết kế cho RÀNG BUỘC, không phải cho lý tưởng.** ⭐
> *"Mỗi persona đều có ràng buộc riêng. Ví dụ, developer **rất thích công cụ self-hosted** mà họ có thể thử và kiểm tra trên môi trường local, thay vì phải đi qua bất kỳ bức tường đăng ký nào."*

Vì thế ChartDB: **không đăng ký, không cuộc gọi bán hàng, không cần cung cấp credentials**.

Đây là bước có giá trị nhất và ít người làm. Hầu hết người mới thiết kế cho *khách hàng lý tưởng trong tưởng tượng*; Jonathan thiết kế quanh **những thứ khách hàng thật sự từ chối làm**.

**Bước 3 — Bắt đầu từ một wedge, không phải từ tầm nhìn đầy đủ.**
Làm thứ người ta thấy giá trị ngay lập tức, rồi tiến hoá dựa trên phản hồi, qua các vòng lặp nhỏ.

**Bước 4 — Để CÁCH DÙNG dẫn đường cho việc thu tiền.** ⭐⭐
> *"Ban đầu chúng tôi hoàn toàn không thu tiền. Rồi người ta bắt đầu hỏi về làm việc cùng nhóm của họ, và khi đó chúng tôi cần cung cấp cộng tác thời gian thực phức tạp hơn, và chúng tôi hiểu ra có thứ gì đó rất phức tạp cần hỗ trợ. **Đó có lẽ là chỗ chúng tôi bắt đầu thu tiền.**"*

Và câu chốt:

> ***"Việc kiếm tiền không nên là một phỏng đoán, mà nên là phản ứng với hành vi [của người dùng]."***

Đây là quan điểm khác hẳn [Marc Lou "ship kèm nút mua ngay"](../2026-04-26_how-i-work-77k-month-solopreneur/case.md) và [Packager "thu tiền sớm dù giá thấp"](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md). **Điều kiện phân định:** khi sản phẩm của bạn là **mã nguồn mở dành cho developer**, thu tiền sớm giết mất kênh phân phối — vì kênh phân phối *chính là* sự miễn phí. Với sản phẩm đóng bán cho doanh nghiệp, thu tiền sớm là tín hiệu xác thực. Đừng áp dụng chéo.

**Bước 5 — Marketing ở nơi ICP đã sống.**
> *"Phân phối phải cảm thấy tự nhiên. Chúng tôi không đi tìm cách phát minh kênh mới nào cả, chúng tôi xuất hiện ở nơi developer vốn đã ở."*

Cụ thể: **GitHub, Hacker News, các subreddit về self-hosted**, và việc các đội nội bộ tự chia sẻ với nhau.

**Kết luận của anh:**
> *"Chọn một persona và **loại bỏ ma sát một cách quyết liệt** hết mức có thể, và **ám ảnh với một giá trị cốt lõi duy nhất** cho tới khi bạn thật sự thấy sự chấp nhận và nó cảm thấy dễ dàng."*

## 5. Tech stack và chi phí thật ⭐

Đây là một trong số ít case công bố chi phí vận hành chi tiết:

| Hạng mục | Công cụ | Chi phí/tháng |
|---|---|---|
| Frontend | React + Vite + Tailwind + **React Flow** (canvas) | — |
| Backend | Node.js | — |
| Hosting | AWS | **$600** |
| AI coding | Claude Code (gói max) | **$200** |
| Compliance (SOC 2) | công cụ trust | **$500** |
| AI assistant | ChatGPT + API | ~$70 |
| Email giao dịch | Resend | — |
| Analytics | Better Analytics | $25 |
| Website marketing | Framer | $30 |
| Doanh thu | ChartMogul | miễn phí |
| Thanh toán | Stripe | phí giao dịch |
| SEO | Ahrefs | — |

> **Con số đáng chú ý:** $500/tháng cho **compliance** — vì *"khách hàng lớn bắt đầu xuất hiện và hỏi về SOC 2"*. Ở mức $9,4K MRR, đó là hơn 5% doanh thu chỉ để trả lời câu hỏi bảo mật. Đây là chi phí ẩn của việc bán B2B mà hầu hết case khác không nói ra — xem thêm ở [Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md) và [Late](../2026-03-04_zero-to-40k-month-with-one-marketing-channel-no-soci/case.md).

Tổng chi phí cố định ~$1.400/tháng trên $9.400 doanh thu → biên gộp vẫn tốt, nhưng không phải "gần như bằng 0" như nhiều người tưởng về SaaS.

## 6. Lời khuyên cuối

> *"Tôi sẽ nói với chính mình rằng hãy **chọn một giá trị cốt lõi và bảo vệ nó một cách quyết liệt**. Mọi thứ bắt đầu chạy khi chúng tôi nhân đôi vào nó — khi chúng tôi tập trung hoàn toàn vào việc làm cho **trực quan hoá database trở nên hiển nhiên**, và bỏ qua mọi thứ khác."*

Pat mở rộng: *"Có rất nhiều developer muốn xây mọi thứ — nó phải là SaaS, nó phải có tất cả các thành phần. Nhưng bạn có thể bắt đầu với một wedge và làm một việc thật tốt."*

![$10.000](screenshots/10_13m51s_usd-10-000.jpg)

## 7. Vì sao mô hình open source hoạt động — góc nhìn của người ngoài

Gus không phải developer, và câu hỏi của anh chính là câu hỏi bạn cần trả lời nếu định sao chép:

> *"Tại sao người ta lại trả tiền cho thứ họ có thể tải miễn phí?"*

Câu trả lời anh tự rút ra: *"Developer trong trường hợp này là **cửa vào** dẫn tới những người sẽ trả tiền."*

Pat bổ sung yếu tố quy mô: *"Công cụ dev khổng lồ vì chúng **miễn phí để tải, miễn phí để thử**. Anh ấy làm đúng như vậy rồi gắn phần kiếm tiền vào phía sau. **Việc này không tốn đồng nào để làm.**"*

**Cơ chế đầy đủ:** mã nguồn mở → phân phối miễn phí và tin cậy → cá nhân dùng free → khi đưa vào **đội nhóm** thì phát sinh nhu cầu phức tạp (cộng tác, hosting, bảo mật) → tổ chức trả tiền. Người dùng và người trả tiền **không phải cùng một người**.

## 8. Cảnh báo thiên kiến nguồn ⚠️

**Mâu thuẫn số liệu ngay trong chính video — và nó nằm trên màn hình.** Jonathan nói hai con số: *"khoảng 9.000 MRR"* (`01:20`) và *"chúng tôi vừa vượt gần 9.400"* (`02:23`). Nhưng ở `13:46`, khi tổng kết với producer, Pat nói *"một business kiếm **$10.000 một tháng**"* — và đội biên tập **dập luôn dòng chữ `$10,000` lên màn hình** (xem [ảnh `10_13m51s_usd-10-000.jpg`](screenshots/10_13m51s_usd-10-000.jpg)). Con số bị làm tròn lên **6%** so với lời founder, ngay trong cùng một video, và cái đọng lại trong đầu người xem là con số to hơn. Tiêu đề thì lại dùng "$9K". **Ba con số khác nhau cho một sự thật.**

**Không có ảnh chụp dashboard doanh thu trong bộ tư liệu.** Ở `02:08-02:23` anh có chia sẻ màn hình GitHub (21.000 sao) và analytics (250.000 developer) — phần này kiểm chứng được. Nhưng **con số $9.400 chỉ được nói bằng lời**, và không khung hình nào trong 10 ảnh chụp của case giữ lại được bảng doanh thu. Sao GitHub là thứ ai cũng xem được; MRR thì không. **Hãy đọc $9.400 như lời tự khai.**

**Quảng cáo chèn giữa — và nó là quảng cáo trá hình.** `05:45-06:33` Pat cắt ngang để tặng *"business idea template miễn phí — hướng dẫn 7 phương pháp đã được kiểm chứng để tìm vấn đề thật"*. Anh giới thiệu nó như sản phẩm của chính mình (*"đó là lý do tôi tạo ra..."*), nhưng link trong mô tả là **`clickhubspot.com/swt` — tức đây là lead magnet của HubSpot**, một tài trợ được đóng gói thành quà tặng. Nội dung của nó (*"tìm 21 vấn đề trong đời sống hằng ngày"*) **mâu thuẫn với chính câu chuyện đang kể**: ChartDB không đến từ việc liệt kê vấn đề, nó đến từ **một sản phẩm đầu tiên thất bại rồi xoay trục**. Thêm `00:46` gài mồi và `15:03-15:25` chào bán **Starter Story Build**.

**Bối cảnh bị làm mờ:**
- **Đây không phải case solo.** Jonathan tự giới thiệu là *"**co-founder**"* và dùng "chúng tôi" xuyên suốt. **Quy mô đội ngũ không bao giờ được nêu** — điều này quan trọng vì nó quyết định $9,4K MRR là thu nhập đủ sống hay là ngân sách chia cho nhiều người.
- **Anh là developer chuyên nghiệp**, xây cho chính giới của mình. Toàn bộ lợi thế phân phối (biết Hacker News hoạt động ra sao, viết được Show HN, đọc được tín hiệu từ subreddit self-hosted) đến từ việc **anh là ICP**.
- **Sản phẩm đầu tiên thất bại trước đó** — nghĩa là có một quãng thời gian và nguồn tiền nuôi giai đoạn đó, không được nhắc tới.
- **Bài Show HN được "chuẩn bị"** (*"chúng tôi chuẩn bị một chút rồi chọn ngày"*) nhưng **chuẩn bị cái gì thì không nói** — đây đúng là phần quyết định giữa lên trang chủ và chìm nghỉm.

**Thiếu số liệu quan trọng:**
- **Không có giá, không có số khách trả tiền.** Với $9.400 MRR, đây có thể là 30 khách doanh nghiệp hay 900 khách cá nhân — hai mô hình kinh doanh hoàn toàn khác nhau.
- **Không có tỉ lệ chuyển đổi** từ 250.000 developer dùng miễn phí sang bản cloud trả tiền. Đây là con số then chốt của toàn bộ mô hình open-source, và nó bị bỏ trống.
- **Không có churn, không có CAC.**
- **Chi phí gần như ăn hết biên lợi nhuận, nhưng không ai làm phép cộng.** Các khoản anh tự nêu: AWS $600 + Claude Code $200 + compliance $500 + ChatGPT/API ~$70 + analytics $25 + Framer $30, **chưa tính** Resend, Crisp, Ahrefs và phí Stripe — tức **trên $1.500/tháng** trước khi trả lương cho bất kỳ ai. Ở $9.400 MRR, đó là hơn 16% doanh thu chỉ riêng hạ tầng.

## 9. Áp dụng cho tôi (indie hacker VN)

**Điểm mạnh của mô hình này với người Việt:**

- **Mã nguồn mở xoá bỏ vấn đề uy tín.** Đây là điều quan trọng nhất. Rào cản lớn nhất khi tôi bán ra quốc tế là *"anh là ai mà tôi phải tin?"* — với open source, người ta **không cần tin tôi**, họ đọc code. Jonathan thất bại ở ý tưởng đầu vì thiếu uy tín, và mã nguồn mở chính là cách anh giải quyết nó.
- **Hacker News không quan tâm bạn ở đâu.** Show HN được đánh giá bằng sản phẩm, không bằng hộ chiếu.
- **Ba tuần code, một bài đăng.** Chi phí thử nghiệm cực thấp.
- **GitHub stars là tài sản có thật** — nó vừa là marketing, vừa là bằng chứng năng lực cho mọi việc sau này.

**Rào cản thật:**

- **Bạn phải là developer giỏi thật.** Không có đường tắt no-code ở đây, khác hẳn [Packager chạy trên Bubble](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md). Người đọc code của bạn là developer.
- **Doanh thu đến chậm và không chắc chắn.** 16 tháng để đạt $9,4K với 250.000 người dùng — **tỉ lệ chuyển đổi cực thấp**. Đây không phải mô hình để thay lương nhanh.
- **Chi phí cố định $1.400/tháng** phải trả trước khi có doanh thu tương xứng. AWS $600 là con số thật.
- **Bạn gánh nghĩa vụ bảo trì mã nguồn mở** — issue, PR, câu hỏi — mà phần lớn đến từ người **không bao giờ trả tiền**.
- **Hacker News chỉ bắn một lần.** Nếu bài Show HN chìm, bạn không có kênh dự phòng. Jonathan may mắn trúng ngay lần đầu; anh không nói về các lần trượt.

**Cách tôi sẽ giảm rủi ro:** dùng open source như **kênh phân phối cho một sản phẩm có đường kiếm tiền rõ ràng ngay từ đầu** (bản cloud, bản team), chứ không mở mã rồi mới nghĩ cách thu tiền. Jonathan làm ngược lại và mất một năm — anh có điều kiện để chờ, tôi thì không.

**Khi nào KHÔNG dùng mô hình này:** khi khách hàng của bạn **không phải developer**. Toàn bộ cơ chế dựa vào việc người dùng biết đọc code, tự host được, và tụ tập ở GitHub/HN. Với khách hàng thường, mã nguồn mở không mang lại niềm tin nào cả — nó chỉ là chữ vô nghĩa.

## Nguồn

- Video: <https://www.youtube.com/watch?v=7vz6b_Ohdl0> (15:29, đăng 25/02/2026, 68.896 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
