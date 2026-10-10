---
id: 3X4VneEHvig
slug: savewise-reddit-facebook-groups
product: Savewise
founder: Avneesh
tagline: Product Hunt + Hacker News cho traffic nhưng bounce 95% — thứ thật sự chạy là 3,5 tháng nằm vùng trong subreddit rồi mới xin mod cho đăng bài
revenue_usd_month: 25000
revenue_basis: founder nói ~25.000 USD doanh thu/tháng lúc quay — nhưng KHÔNG phải MRR thuần, 97% đến từ gói lifetime mua đứt nên đây là dòng tiền phụ thuộc khách mới hàng tháng
model: micro-saas-lifetime-deal
category: fintech-consumer — credit card points và cashback
audience: B2C — người Mỹ săn điểm thẻ tín dụng, airline miles, cashback Rakuten/Amex
started: khoảng giữa 2024 (suy ra từ mốc 15 tháng trước lúc quay)
time_to_first_sale: không nêu
time_to_scale: 15 tháng từ lúc bắt đầu tới 25K USD/tháng
team_size: 1 (solopreneur)
funding: bootstrapped, 0 USD quảng cáo
main_channel: Reddit + Facebook Groups — nằm vùng trước, đăng bài sau
tech_stack: [Next.js, Vercel, Azure, Retool, Clerk, v0, PostHog, Google Analytics, ChatGPT, Cursor, Copilot]
key_metrics:
  paying_customers: 1.500
  users: hàng chục nghìn
  lifetime_share_of_revenue: 97%
  bounce_rate_product_hunt_hn: 95-96%
  influencer_outreach: 300-400 email/DM gửi đi, 1 hồi âm
  one_facebook_post: 1.500+ lượt truy cập website
  lurk_time_before_posting: 3,5 tháng trong subreddit chính
  ad_spend: 0
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=3X4VneEHvig
published: 2025-08-09
views: 160796
---

# Savewise — $25K/tháng từ Reddit và Facebook Groups, $0 quảng cáo

> **Tóm tắt 30 giây:** Avneesh (cựu nhân viên Microsoft, Instagram, Foursquare, Dropbox) build Savewise — công cụ tự động ghép ưu đãi cashback và điểm thẻ tín dụng cho thứ bạn sắp mua. Anh đăng Product Hunt, Hacker News, Indie Hackers: **traffic nhiều nhưng bounce rate 95-96%, không ai ở lại**. Gửi 300-400 email cho influencer: **đúng 1 người trả lời**. Thứ thật sự hiệu quả là điều ngược lại hoàn toàn — **nằm vùng 3,5 tháng** trong một subreddit, mỗi tuần chỉ comment trong thread Q&A, build đúng những gì thành viên yêu cầu, rồi **nhắn xin phép moderator** mới đăng bài top-level. Bài đó đưa anh từ vài nghìn lên hàng chục nghìn user. 15 tháng, $25K/tháng, $0 quảng cáo. Cú twist về mô hình giá: **97% doanh thu đến từ gói lifetime**, không phải subscription.

![$25.000/tháng](screenshots/01_01m23s_usd-25-000.jpg)

## 0. Đính chính tên riêng và cảnh báo nguồn

**Transcript là auto-caption và sai nặng tên riêng.** Đối chiếu với `meta.json`:

| ASR đọc thành | Tên đúng |
|---|---|
| "OV niche", "Anish", "Ovnish", "Omnesh", "Ovniche" | **Avneesh** (X: `@avneeshk91`) |
| "Save Wise", "Save West", "Safe Wise", "Save Lives" | **Savewise** |
| "Rakitin", "Rakutin" | **Rakuten** (trang cashback Mỹ) |
| "F5bot" | **F5Bot** (f5bot.com — đúng) |

**Cảnh báo thiên kiến nguồn:** video có **hai chèn quảng cáo** cho khoá học Starter Story Build (phút 7:55 và phút 14:00), chiếm gần 1/7 thời lượng. Kênh chỉ phỏng vấn người đã thành công — bạn không thấy hàng nghìn người làm đúng playbook này mà thất bại. Chi tiết nhỏ cho thấy khâu sản xuất khá cẩu thả: link trong mô tả video này gắn `utm_campaign=abhishek` — copy nhầm từ [case YouForm](../2025-08-02_i-copied-a-100m-saas-undercut-their-prices-and-hit-1/case.md) đăng trước đó một tuần. Hãy đọc con số với thái độ đó.

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$25.000/tháng |
| Trong đó gói lifetime | **97%** |
| Khách trả tiền | ~1.500 |
| Người dùng | hàng chục nghìn |
| Thời gian tới mốc này | 15 tháng |
| Chi quảng cáo | **$0** |
| Team | 1 người |
| Bounce rate từ Product Hunt / HN / Indie Hackers | 95-96% |
| Outreach influencer | 300-400 tin nhắn → **1 hồi âm** |
| Một bài Facebook | 1.500+ lượt truy cập |

**Suy luận của tôi (không phải con số founder nói):** 1.500 khách trả tiền tích luỹ trong ~15 tháng ≈ 100 khách mới/tháng. Để ra $25K/tháng thì giá gói lifetime rơi vào khoảng **$200-250**. Founder không xác nhận con số này — tôi ghi ra vì nó quyết định toàn bộ phần phân tích rủi ro bên dưới.

## 2. Cái bẫy "launch platform" — thứ hầu hết indie hacker VN đang mắc ⭐⭐⭐

Đây là phần đắt nhất của video và nó đi ngược trực giác của gần như mọi người mới.

Avneesh làm đúng những gì Twitter dạy:

1. Đăng **Product Hunt** ✗
2. Đăng **Hacker News** ✗
3. Đăng **Indie Hackers** ✗

> *"I actually got tons of traffic and then quickly realized that **none of those people stuck**. I think the bounce rate was like **95, 96%**. I got none of the feedback that I was actually looking for."*

Rồi anh chuyển sang influencer outreach: **300-400 email và tin nhắn, nhận về đúng 1 hồi âm**.

> *"**Nobody who has an audience or influence cares about a product that is not ready** is still looking for feedback."*

**Cơ chế vì sao thất bại — và đây mới là phần quan trọng:** Product Hunt, Hacker News, Indie Hackers là nơi tập trung **người XÂY sản phẩm**, không phải **người DÙNG sản phẩm**. Họ vào xem vì tò mò nghề nghiệp, chấm điểm kỹ thuật, rồi đi. Họ không có vấn đề mà sản phẩm bạn giải.

Cú xoay của Avneesh gói gọn trong một câu:

> *"Focus on subreddits that were more related to **using products** rather than **building products** — unlike the Indie Hackers and the SaaS subreddits. And focus on the Facebook groups where people organized around **travel and credit card points**."*

Savewise giải bài toán của **người săn điểm thẻ tín dụng**, nên khách của anh nằm ở r/churning, r/creditcards, các group du lịch — không nằm ở r/SaaS.

![Đi tìm khách hàng](screenshots/03_03m44s_ch-the-2-platforms-that-worked.jpg)

**Bài test 10 giây cho bạn:** viết ra tên 3 cộng đồng bạn định đăng bài. Nếu cả 3 đều là nơi lập trình viên tụ tập mà sản phẩm bạn không bán cho lập trình viên → bạn đang lặp lại sai lầm 15 tháng đầu của Avneesh.

## 3. Playbook 5 bước chiếm Reddit và Facebook Groups ⭐⭐⭐

![Playbook 5 bước](screenshots/04_04m19s_ch-5-step-marketing-playbook.jpg)

### Bước 1 — Brainstorm 5-15 từ khoá, rồi dùng Map of Reddit để lan ra

Liệt kê từ khoá, sở thích, đặc điểm nhân khẩu của người **sẽ dùng** sản phẩm. Rồi dùng công cụ **Map of Reddit**: nhập vào một subreddit (ví dụ `credit cards`), nó quét toàn bộ Reddit và **vẽ bản đồ trực quan** các cộng đồng liên quan gần hoặc xa.

> *"It almost allowed me to **traverse from one community to several different related communities** where I could find more and more of these potential target users."*

Đây là cách phá thế bí "tôi chỉ biết mỗi 2-3 subreddit".

### Bước 2 — Vào rồi ĐỪNG đăng gì cả (bước quan trọng nhất)

> *"The second, perhaps **most important step**, is when you join these Reddit and Facebook groups, **do not initially post** in those groups."*

Quan sát hai thứ:
- Người ta đang **nói về cái gì**
- Người ta **nói như thế nào** (giọng điệu, từ ngữ, cái gì bị ghét)

Mục tiêu không phải thu thập insight sản phẩm. Mục tiêu là **tìm cách bước vào cuộc trò chuyện** thay vì nhảy vào quảng cáo — vì quảng cáo thẳng thì "simply not going to work".

### Bước 3 — Mỗi cộng đồng một mục tiêu, và bắt đầu từ COMMENT

Với từng cộng đồng, hỏi: nếu tôi có được sự chú ý của nhóm này, tôi thật sự muốn gì? (hiểu họ đang dùng sản phẩm nào? họ đau ở đâu? hay chỉ muốn họ thử sản phẩm?) Mục tiêu quyết định bạn đăng cái gì và đăng kiểu gì.

> *"**Starting in the comments** before you actually do a top-level post. Starting in the comments is a **very low-risk way** of figuring out is this type of stuff you're saying actually resonating with the community."*

**Cơ chế:** comment bị chìm thì không mất gì. Bài top-level bị downvote hoặc bị mod xoá thì tài khoản bạn dính dớp, và ở một số subreddit là ban vĩnh viễn. Comment là **môi trường thử nghiệm rẻ**; top-level post là **canh bạc một lần**. Đừng đánh bạc khi chưa biết luật.

### Bước 4 — Cảnh báo từ khoá bằng F5Bot

Dựng alert trên **F5Bot**: mỗi khi ai đó trên Reddit nhắc tới từ khoá của bạn, F5Bot gửi email real-time. Avneesh đọc nguyên bài đó và tìm cơ hội: lấy feedback, hoặc hiểu thêm nhu cầu.

**Vì sao real-time quan trọng:** trên Reddit, comment đến trong 1-2 giờ đầu mới có cơ hội lên top. Trả lời sau 2 ngày là nói vào hư không.

### Bước 5 — Hữu ích trước, bán sau

> *"There are so many people out there looking for advice, looking for opinions from people who are **not necessarily experts, but just know a little bit more than them**. Once I figured out a way to just organically and naturally be helpful... that then **earned me the right** to also mention my product."*

Câu "not necessarily experts, but just know a little bit more than them" là câu tháo gỡ tâm lý quan trọng nhất video: **bạn không cần là chuyên gia**, chỉ cần biết nhiều hơn người đang hỏi một chút.

## 4. Case Facebook — một câu SQL đổi lấy 1.500 khách ⭐⭐⭐

![1.500 khách từ một bài đăng](screenshots/07_08m47s_ch-getting-1500-visitors-from-one-post.jpg)

Chuỗi hành động, sao chép được nguyên xi:

1. Search Facebook theo từ khoá liên quan sản phẩm → tìm ra group **"Rakuten Stacks — How to double dip with Rakuten"**.
2. Nhận ra: **hàng nghìn người trong group đang LÀM THỦ CÔNG** đúng việc mà sản phẩm anh làm bằng **một câu query**.
3. Viết **một câu SQL** lấy từ database Savewise → xuất ra bảng danh sách: cửa hàng, ưu đãi Rakuten, ưu đãi American Express.
4. Đăng **link tới bảng tính** (không phải link sản phẩm) trong group.
5. Người mở bảng tính thấy đúng thứ họ cần — **và thấy link website nguồn dữ liệu ở trong bảng**.

Kết quả: **1.500+ lượt truy cập website từ một bài đăng.**

**Vì sao cơ chế này hiệu quả (và vì sao nó không phải "hack"):**

- Thứ được đăng là **kết quả**, không phải quảng cáo. Không mod nào xoá một bảng dữ liệu miễn phí hữu ích.
- Bảng tính là **định dạng bản địa** của group đó — họ vốn đã trao đổi nhau bằng spreadsheet. Anh nói đúng ngôn ngữ của cộng đồng.
- Link sản phẩm nằm **bên trong** giá trị, không nằm trước nó. Người click là người đã tiêu thụ giá trị rồi.
- Nó biến **lợi thế kỹ thuật thành nội dung**: thứ anh mất 30 giây (một câu SQL), họ mất hàng giờ mỗi tuần. Đó chính là định nghĩa của demo giá trị.

**Bản dịch cho bạn:** bạn có database gì mà cộng đồng nào đó đang làm thủ công? Xuất nó ra Google Sheet, đăng miễn phí, nhét link nguồn vào trong. Đây là chiến thuật rẻ nhất trong toàn bộ kho case này.

## 5. Case Reddit — 3,5 tháng nằm vùng và một tin nhắn cho moderator ⭐⭐⭐

Đây là phần mà 99% người sẽ không đủ kiên nhẫn làm — và chính vì thế nó còn hiệu quả.

| Giai đoạn | Việc làm |
|---|---|
| Vài tuần đầu | Chỉ **theo dõi**, không đăng gì |
| Hàng tuần, suốt ~3,5 tháng | Vào **weekly Q&A thread**, comment link website, xin feedback |
| Song song | **Build đúng những tính năng thành viên nói ra** |
| Sau 3,5 tháng | **Nhắn riêng cho moderator xin phép** đăng bài top-level |
| Được đồng ý | Đăng → *"it blew up"* |

> *"After about three and a half months, I had built out **all of the core functionality that members of the community were just straight up telling me about**. And at that point, **I messaged the moderator back and said, hey, are you still okay with me doing a top-level post?** They said yes."*

> *"**This was the post that took me from single thousands of users to tens of thousands of users.**"*

![Con số](screenshots/09_11m15s_usd-25-000.jpg)

**Ba cơ chế đang chạy cùng lúc — nếu bỏ một cái là hỏng:**

1. **Weekly Q&A thread là cửa hợp pháp.** Hầu hết subreddit lớn cấm self-promotion ở top-level nhưng **mở một thread định kỳ cho phép**. Đây là kẽ hở được cộng đồng chính thức thừa nhận. Việc đầu tiên khi vào một subreddit mới: đọc rule, tìm thread định kỳ đó.
2. **3,5 tháng build theo yêu cầu = sản phẩm khi lên sóng đã đúng nhu cầu.** Bài đăng "blew up" không phải vì copywriting hay. Nó nổ vì đến thời điểm đó, sản phẩm đã có **đúng những gì chính họ đòi**. Marketing chỉ là bước cuối; 3,5 tháng kia mới là công việc thật.
3. **Xin phép mod là bước đảo chiều quan hệ quyền lực.** Thay vì lén lút đăng rồi bị xoá, anh biến mod thành người bảo trợ. Chi phí: một tin nhắn. Lợi ích: bài không bị xoá, và có khi còn được ghim.

**So sánh với các case khác trong kho:**

| Cách tiếp cận cộng đồng | Ai | Đúng khi nào |
|---|---|---|
| Nằm vùng 3,5 tháng, xin phép mod, đăng 1 bài | Avneesh (case này) | Cộng đồng đã tồn tại, đông, và có luật chặt. Bạn là người ngoài. |
| Dùng Reddit làm kênh chính, quy mô lớn hơn | [Gojiberry AI](../2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/case.md) | So sánh trực tiếp — cùng kênh, khác cách vận hành |
| **Tự dựng** cộng đồng Discord của mình | [Algrow](../2026-01-14_i-built-a-14k-month-saas-using-discord/case.md) | Bạn muốn sở hữu kênh, chấp nhận đổi bằng thời gian nuôi cộng đồng |
| Đi vào cộng đồng khách hàng của **đối thủ** | [Lancer](../2026-03-08_i-built-a-10k-month-saas-using-other-peoples-custome/case.md) | Đối thủ đã gom sẵn đúng ICP cho bạn |

## 6. Mô hình giá — "người tiêu dùng ghét subscription" ⭐⭐

Đây là con số gây tranh cãi nhất video:

> *"What's most fascinating is that I learned **consumers hate subscriptions**. I initially launched a subscription product and **the day that I launched**, I had several emails from members who wanted to buy the pro product asking for a **lifetime membership**, where they were willing to pay for **two-plus years worth** of the pro membership all upfront. That is now about **97% of the revenue** — people choosing the lifetime plan over a monthly or yearly subscription plan."*

**Phân tích tỉnh táo — vì sao 97% lifetime KHÔNG hẳn là tin vui:**

- **"$25K/tháng" ở đây không phải MRR.** Nó là doanh thu tiền mặt tháng đó, mà 97% là bán đứt. Nếu tháng sau không có khách mới, doanh thu tụt về ~$750 (phần subscription còn lại). Đây là mô hình **chạy trên guồng quay**, không phải tài sản tích luỹ.
- **Định giá lifetime = bán tương lai với giá quá khứ.** Khách trả "2+ năm" để dùng vĩnh viễn. Nếu khách trung bình ở lại 4 năm, bạn vừa bán lỗ 50%. Với sản phẩm có chi phí biến đổi (Azure, xử lý dữ liệu liên tục), lifetime user là **nợ phải trả suốt đời**.
- **Nhưng nó đúng trong bối cảnh của anh:** ICP của Savewise là **người săn ưu đãi chuyên nghiệp** — nhóm người có bản năng nghề nghiệp là né phí định kỳ và tối ưu chi phí. Bán subscription cho dân churning giống như bán giá niêm yết cho người đi chợ chuyên nghiệp.

> **Điều kiện phân định:** lifetime deal hợp lý khi (a) chi phí biến đổi/user gần bằng 0, (b) ICP của bạn có tâm lý ghét phí định kỳ, (c) bạn cần tiền mặt sớm để tự nuôi. Nó **sai** khi sản phẩm ngốn compute mỗi lần dùng — xem [Neural Frames](../2025-07-30_my-ai-app-makes-100k-month/case.md), nơi $45K/tháng chảy thẳng vào GPU: bán lifetime ở đó là tự sát.

Case dùng lifetime deal ở quy mô khác để đối chiếu: [Floga](../2026-03-29_my-app-made-120k-in-24-hours/case.md).

## 7. Tech stack

| Hạng mục | Công cụ | Ghi chú |
|---|---|---|
| Frontend | **Next.js** | |
| Hosting web | **Vercel** | |
| Data / DB | **Azure** | Toàn bộ xử lý dữ liệu và kiến trúc DB |
| Admin nội bộ | **Retool** | Cách nhanh để thao tác trên khối dữ liệu lớn |
| Auth | **Clerk** | Đăng nhập Google, Apple |
| Design/UI | **v0** | *"perhaps the biggest unlock for me in the last 6 months"* — trước đó phải thiết kế trong Figma |
| Analytics | **PostHog** + Google Analytics | |
| Coding | ChatGPT, Copilot, Cursor | |

Điểm đáng chú ý: **v0 thay thế Figma**, không thay thế lập trình viên. Avneesh là dân kỹ thuật (từng làm Microsoft, Instagram, Dropbox); thứ anh thiếu là **kỹ năng thiết kế**, và đó chính là chỗ AI tạo đòn bẩy lớn nhất cho anh.

## 8. Lời khuyên cuối — hiểu khách hàng để MARKETING, không phải để BUILD ⭐⭐

> *"Something that I always thought was true was that understanding your target customer was really important **for the specific features that you built**. And that's still true. But my realization is that understanding your target customer is **even more useful for the marketing part** — figuring out **where do my target customers hang out on the internet**. It has been way more impactful for that."*

Đây là câu tổng kết cả case: 15 tháng của anh không phải cuộc chiến sản phẩm, mà là cuộc chiến **định vị nơi ở của khách**. Anh đã có sản phẩm chạy được từ sớm (nó giải chính vấn đề của anh); anh chỉ không biết khách ngồi đâu.

## 9. Áp dụng cho tôi (indie hacker VN)

### Sao chép được gì

- **Toàn bộ playbook 5 bước dùng được ngay, chi phí $0.** Không cần vốn quảng cáo, không cần lên hình, không cần giọng nói hay.
- **Chiến thuật "bảng tính đổi traffic" là món rẻ nhất trong kho này.** Tìm một group Facebook Việt đang làm thủ công thứ bạn có thể query. Xuất Google Sheet miễn phí, để link nguồn trong sheet. Việt Nam có vô số group kiểu này: săn vé máy bay rẻ, mã giảm giá Shopee/Lazada, so sánh lãi suất, tra cứu học phí, giá vật liệu xây dựng.
- **Quy trình xin phép mod dùng được cho group Facebook Việt** — nơi admin thậm chí còn khắt khe hơn mod Reddit, và cũng dễ tiếp cận hơn (nhắn Messenger).
- **Đừng lãng phí lượt launch đầu tiên vào Product Hunt.** Con số 95-96% bounce là bằng chứng cứng. Chỉ launch PH khi khách của bạn **chính là** dân làm sản phẩm.
- **Dùng v0 để bù kỹ năng thiết kế** nếu bạn là dev không biết design — đây là điểm đòn bẩy AI rõ ràng nhất trong case.

### Rào cản thật

- **Ngách này KHÔNG bê nguyên về Việt Nam được.** Savewise sống nhờ hệ sinh thái Mỹ: Rakuten, American Express Offers, văn hoá "churning" thẻ tín dụng. Việt Nam không có tầng ưu đãi chồng lớp đó. Bạn sao chép được **playbook phân phối**, không sao chép được **sản phẩm**.
- **Nếu nhắm thị trường Mỹ thì rào tiếng Anh là thật và nặng.** Playbook này đòi bạn **comment hàng tuần suốt 3,5 tháng** với giọng điệu bản địa trong một cộng đồng dân sành sỏi. Reddit ngửi ra người ngoài rất nhanh. Đây là rào cản cao hơn nhiều so với việc chỉ dịch landing page.
- **Chi phí thời gian bị giấu kín.** 3,5 tháng nằm vùng + 15 tháng tới $25K = khoảng thời gian không doanh thu rất dài. Nếu bạn cần tiền trong 90 ngày, đây không phải kênh của bạn.
- **Rủi ro nền tảng.** Một lần bị mod ban là mất trắng cộng đồng đó, không kháng cáo được. Đừng dồn 100% phân phối vào một subreddit.
- **Mô hình lifetime giấu rủi ro dòng tiền.** Nếu bạn bắt chước và bán lifetime, hãy tính trước: chi phí phục vụ một user trong 5 năm là bao nhiêu? Với sản phẩm gọi API AI mỗi lần dùng, lifetime là bẫy chết người.
- **ARPU ~$200-250/lần mua là mức giá cho ví Mỹ.** Bán cùng sản phẩm cho người Việt, con số này phải chia 5-10 lần → số khách cần có tăng tương ứng. Nếu định làm mô hình này, nhắm quốc tế ngay từ ngày đầu hoặc chọn ngách B2B trong nước có ngân sách.

### Khi nào KHÔNG dùng mô hình này

- **Khi vấn đề bạn giải chưa có cộng đồng tồn tại.** Playbook này hoàn toàn ký sinh vào các cộng đồng có sẵn. Không có subreddit/group nào tụ quanh vấn đề của bạn → không có gì để nằm vùng. Lúc đó bạn cần SEO ([FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md)) hoặc quảng cáo trả tiền.
- **Khi bạn bán B2B giá cao.** Reddit và Facebook Group hầu như không phải nơi người ra quyết định mua phần mềm $500/tháng lui tới. Xem [Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md) cho hướng B2B ngách.
- **Khi bạn không chịu nổi việc bị lơ trong 3 tháng.** Playbook này thất bại 100% nếu làm nửa vời — comment 2 tuần rồi bỏ thì không tạo được uy tín gì, và bài top-level sẽ chìm.

## Nguồn

- Video: <https://www.youtube.com/watch?v=3X4VneEHvig> (14:35, đăng 09/08/2025, 160.796 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
- Founder trên X: `@avneeshk91`
- Công cụ nhắc tới: Map of Reddit, F5Bot (f5bot.com)
