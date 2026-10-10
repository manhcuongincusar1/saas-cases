---
id: hYW9YDwHE20
slug: rabbitholes-ai-lifetime-deal-byok
product: Rabbitholes AI
founder: Praneeth Pike
tagline: Bỏ subscription, chuyển sang one-time purchase + bring-your-own-keys + app desktop — chi phí vận hành gần bằng 0 và thu $80K trong 6 tháng
revenue_usd_month: 13333
revenue_basis: video chỉ nêu 80.000 USD gross trong 6 tháng (lợi nhuận ~75.000 USD sau hoàn tiền). Con số tháng ở đây là trung bình 80.000 chia 6 — KHÔNG phải MRR. Đây là doanh thu one-time, không tái diễn, nên tháng nào cũng phải bán mới có
model: desktop-app-lifetime-deal
category: ai-productivity-tools
audience: B2C — power user AI (người trả tiền cho nhiều model cùng lúc)
started: nghỉ việc 250.000 USD/năm vào 2024; bản đầu ra mắt sau ~3 tháng build
time_to_first_sale: bản subscription đầu tiên gần như không ra tiền; tiền thật đến ngay sau khi đổi sang one-time purchase
time_to_scale: 6 tháng kể từ lúc pivot để đạt 80.000 USD tích luỹ
team_size: 1 (solo founder)
funding: bootstrapped
main_channel: landing page nhắm đúng ICP + trả lời chủ đề AI trên Twitter/X
tech_stack: [Cursor, Next.js, Electron, React, TypeScript, Vercel AI SDK, Cloudflare, Vercel]
key_metrics:
  gross_revenue: 80.000 USD trong 6 tháng
  profit: ~75.000 USD sau hoàn tiền
  paying_users: 1.200
  lifetime_share: 60% mua lifetime, 40% mua one-time có gia hạn năm để nhận update
  unique_visitors: 38.000 lượt khách duy nhất từ đầu tới nay
  price_ladder: 29 USD dưới 100 khách → 49 USD sau đó → dự kiến tăng tiếp và thêm gói recurring
  monthly_cost: ~250 USD/tháng (50 USD Vercel + 200 USD Cursor)
replicability_vn: 5
difficulty: 2
video_url: https://www.youtube.com/watch?v=hYW9YDwHE20
published: 2025-10-08
views: 51373
---

# Rabbitholes AI — $80K trong 6 tháng sau khi giết chết mô hình subscription

> **Tóm tắt 30 giây:** Praneeth Pike bỏ công việc lương **$250.000/năm**, build 3 tháng, ra mắt web app AI theo mô hình freemium + subscription — và **gần như không ai trả tiền**. Anh đổi đúng **một thứ**: bán **one-time purchase** thay vì subscription. Để làm được điều đó anh phải đẩy toàn bộ chi phí sang người dùng — **bring your own keys** (khách tự trả tiền AI) và **đóng gói thành app desktop Electron** (khách tự chạy trên máy mình, không tốn server). Kết quả: **$80.000 trong 6 tháng**, ~$75.000 lợi nhuận, **1.200 khách trả tiền**, chi phí vận hành **~$250/tháng**.

![Rabbitholes AI](screenshots/01_00m57s_replay.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu gross | **$80.000 trong 6 tháng** |
| Lợi nhuận | ~$75.000 (sau hoàn tiền và chi phí) |
| Khách trả tiền | 1.200 |
| Cơ cấu | 60% lifetime · 40% one-time có gia hạn năm để nhận update |
| Khách duy nhất vào site | 38.000 |
| Bậc giá | $29 (dưới 100 khách) → $49 → dự kiến tăng tiếp |
| Chi phí vận hành | **~$250/tháng** ($50 Vercel + $200 Cursor) |
| Chi phí AI | **$0** — khách tự trả bằng API key của họ |
| Chi phí server chạy app | **$0** — chạy trên máy khách |
| Team | 1 người |

**Lưu ý về số liệu:** video **không nêu MRR**. $80K là **tích luỹ 6 tháng** của một mô hình bán đứt. Trường `revenue_usd_month` trong frontmatter là phép chia trung bình để so sánh được với các case khác trong kho — đừng đọc nó như MRR. Với LTD, doanh thu **không tự lặp lại**: tháng nào ngừng bán là tháng đó về gần 0.

**Lưu ý về tên sản phẩm:** phần mô tả video và link chính thức là **rabbitholes.ai**. Trong transcript, founder nói *"I built an app called Canvas Mode, which was formerly known as Rabbit Holes AI"* — tức sản phẩm có thể đã/đang được đổi tên thành **Canvas Mode**. Tôi giữ tên **Rabbitholes AI** vì đó là tên trong mô tả chính thức, nhưng bạn nên kiểm tra lại nếu tra cứu sau này.

## 2. Sản phẩm: ChatGPT nhưng dạng canvas, không phải dòng chat thẳng

Vấn đề Praneeth tự gặp: anh học một chủ đề mới bằng cách mở song song ChatGPT + Claude + Perplexity, mỗi cái mạnh một mảng:

- **Claude** — code
- **GPT** — kiến trúc, tư duy tầng cao
- **Perplexity** — thông tin thời gian thực

Anh thấy mình *"phân tán qua cả đống tab khác nhau"*. Cộng thêm một vấn đề kỹ thuật: chat tuyến tính càng dài thì model càng **quên/lạc mạch**.

Giải pháp: canvas. Khi cuộc hội thoại đi tới chỗ thú vị và bạn muốn rẽ nhánh, bạn **tạo một node mới** thay vì làm bẩn mạch chat cũ.

> *"Rabbit Holes AI được xây cho power AI user để lấy được nhiều hơn từ AI, khác với các app hội thoại tuyến tính."*

![Ý tưởng cho Rabbitholes AI](screenshots/02_01m58s_ch-idea-for-rabbitholes-ai.jpg)

## 3. Vì sao subscription THẤT BẠI — chẩn đoán rất chính xác ⭐⭐⭐

Praneeth mặc định làm theo cách ai cũng làm: web app + free trial vài câu hỏi + trả tiền theo tháng. Không ra tiền. Anh nêu **hai lý do**, và cả hai đều là bài học chung:

**Lý do 1 — Không có personal brand thì subscription không có nhiên liệu.**

> *"Tôi không có personal brand lớn, cố làm cái trò build in public, nói trên Twitter, đăng mọi nơi có thể. Tôi nhận được vài sự quan tâm, nhưng chưa bao giờ biến thành đô-la thật."*

**Lý do 2 — ICP của anh đã BÃO HOÀ subscription.** Đây là insight sắc nhất video:

> *"Tôi đã quyết định ICP của mình là power AI user. Mà tại thời điểm đó, ICP của tôi đã ngập trong cả đống subscription họ đang trả cho các model AI."*

**Cơ chế:** người dùng có một "ngân sách subscription tinh thần" hữu hạn. Power user AI năm 2025 đã trả ChatGPT Plus + Claude Pro + Perplexity + Cursor = $80-100/tháng. Một app thứ tư đòi $10-20/tháng không cạnh tranh với **giá trị của bạn**, nó cạnh tranh với **sự mệt mỏi vì subscription**. Còn $49 trả một lần thì rơi vào một ngăn não khác — ngăn "mua công cụ", cùng ngăn với mua chuột hay bàn phím.

![Mô hình giá đã thất bại](screenshots/03_02m40s_ch-the-pricing-model-that-failed.jpg)

## 4. Cú pivot — và chuỗi logic bắt buộc đằng sau nó ⭐⭐⭐

Đây là phần đáng học nhất. Praneeth **không chỉ đổi giá** — đổi giá kéo theo hai quyết định kiến trúc bắt buộc:

1. **Muốn bán one-time** → không được phép gánh chi phí AI định kỳ
   → **Bring your own keys**: khách dán API key của chính họ vào.
2. **Muốn bán one-time** → cũng không được phép gánh chi phí server
   → **Đóng thành app desktop (Electron)**: chạy trên máy khách, dùng CPU và điện của khách.

> *"Nếu tôi build một lần rồi bán nhiều lần, tôi phải đẩy cả chi phí server sang người dùng nữa. Và cách dễ nhất là dùng luôn máy tính của người dùng."*
>
> *"Cái này cho phép tôi **ship rồi quên luôn chi phí kinh doanh** — tất cả chạy trên máy người dùng. Họ trả tiền AI."*

**Đây là quy tắc tổng quát:** *mô hình doanh thu quyết định kiến trúc.* Bán đứt mà vẫn ôm chi phí biến đổi định kỳ thì mỗi khách bạn bán là một khoản nợ dài hạn. Ai đã bán lifetime deal cho một sản phẩm ngốn token đều biết cảm giác đó.

**Hiệu ứng phụ Praneeth không lường trước — và nó quan trọng không kém tiền:**

> *"Ngay khi tôi đổi, rất nhiều người bắt đầu trả tiền. Họ **nghiêm túc hơn hẳn khi cho feedback**. Cảm giác rất khác — người ta không chỉ nghiêm túc hơn mà còn sẵn lòng giúp, họ tin vào sản phẩm giai đoạn đầu này."*

**Cơ chế:** người trả $49 một lần đã **cam kết** vào sản phẩm; người dùng free trial thì chưa. Bạn không mua doanh thu, bạn mua **một nhóm người thật sự muốn sản phẩm này tồn tại**. Với solo founder, đó là thứ hiếm hơn tiền.

![Cú pivot 80K](screenshots/04_03m47s_ch-the-80k-pivot.jpg)

## 5. Khung định giá LTD — bậc thang theo số khách ⭐⭐

Praneeth **không** đặt giá một lần rồi thôi. Anh dùng số khách làm nấc thang:

| Mốc | Giá | Ý nghĩa |
|---|---|---|
| Dưới 100 khách | **$29** | Giá rẻ để kiểm chứng thị trường có muốn không |
| Trên 100 khách | **$49** | Tín hiệu thị trường đã có, tăng giá |
| ~1.200 khách (hiện tại) | Sắp tăng tiếp + chuyển dần sang **recurring** | Đã có PMF, giờ mới nghĩ tới doanh thu lặp lại |

> *"Mức chào ban đầu thấp hơn nhiều, và những người mua sớm được deal tốt hơn hẳn. Và nó cũng cho tôi feedback rằng **thị trường đang muốn mua thứ như thế này**."*

**Vì sao cách này khôn:** giá $29 lúc đầu không phải để kiếm tiền, nó là **thiết bị đo**. Nếu 100 người không chịu bỏ $29 thì $49 hay $99 đều vô nghĩa. Còn với người mua sớm, việc giá tăng dần biến họ thành người "mua hời" — họ có động lực khoe và giới thiệu.

![$29](screenshots/06_07m17s_usd-29.jpg)

## 6. Luận điểm gây tranh cãi — và đường phân định ⭐⭐⭐

Praneeth phát biểu rất mạnh:

> *"Tôi sẽ **không** khuyên bắt đầu bằng subscription model nếu bạn đang bootstrap."*
>
> *"Tôi nghĩ **mọi doanh nghiệp bootstrap đều nên làm LTD**. Kiểu freemium của VC sẽ không chạy với mô hình bootstrap. Có vốn mạo hiểm nghĩa là bạn được phép **hoãn việc đi tìm sự thật** — bạn có thể trì hoãn product-market fit, ngồi hy vọng người ta sẽ lên tàu. Doanh nghiệp bootstrap không có sự xa xỉ đó."*

**Đây là câu đắt nhất video.** Diễn giải cơ chế: freemium + subscription là mô hình **trả lời chậm**. Bạn phải nuôi người dùng free nhiều tháng mới biết họ có trả tiền không. Đó là mô hình dành cho người có tiền để **mua thời gian**. Bootstrapper không mua được thời gian, nên cần mô hình cho **câu trả lời có/không trong tuần này**.

**Nhưng phát biểu này va thẳng vào phần lớn kho case:**

| Quan điểm | Ai nói | Đúng khi nào |
|---|---|---|
| Bootstrap thì đừng bắt đầu bằng subscription — làm LTD trước | **Praneeth (case này)** | ICP đã bão hoà subscription; chi phí biến đổi có thể đẩy sang khách (BYOK/desktop); sản phẩm là **công cụ**, không phải dịch vụ chạy liên tục |
| Subscription là mặc định, LTD chỉ để tạo cú hích | [Floga](../2026-03-29_my-app-made-120k-in-24-hours/case.md) — bán lifetime deal ra $120K trong 24 giờ | Bạn đã có traffic/audience sẵn để bắn một phát lớn |
| One-time purchase là mô hình chính từ đầu | [LaunchFast](../2026-01-04_how-i-built-my-first-saas-without-an-audience-25k-mo/case.md) — boilerplate bán đứt | Sản phẩm là thứ mua một lần dùng mãi, không có chi phí chạy |
| Subscription thuần, ARPU thấp, cần khối lượng | [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md), phần lớn app mobile trong kho | Có kênh phân phối ổn định để liên tục nạp khách mới |

**Đường phân định tôi rút ra:** hãy hỏi **chi phí biên của một khách hàng thêm là bao nhiêu?**
- Gần $0 (app chạy máy khách, BYOK, phần mềm tải về) → LTD an toàn, Praneeth đúng.
- Có chi phí AI/server thật theo từng lần dùng → LTD là **bán nợ cho tương lai**. Đừng làm, hoặc chỉ làm giới hạn số lượng.

Và lưu ý bản thân Praneeth cũng đang **chuyển dần sang recurring** khi đã tới 1.200 khách. Nghĩa là ngay trong chính case này, LTD được dùng như **bệ phóng để tìm PMF**, không phải mô hình cuối cùng.

![$80.000](screenshots/05_04m45s_usd-80-000.jpg)

## 7. Tăng trưởng: landing page nhắm đúng ICP > mọi mẹo marketing ⭐⭐

Khi được hỏi về growth, câu trả lời đầu tiên của Praneeth **không phải kênh** mà là **trang đích**:

> *"Điều đầu tiên tôi vẫn muốn mọi người làm là **làm cho đúng cái landing page**. Để làm đúng nó, tôi nghĩ điều tôi làm đúng lần này là **xác định đúng ICP**. Với tôi đó là power AI user. Nên toàn bộ copy trên landing page được may đo cho power AI user. **Tôi gọi thẳng tên họ ở H1**, và gọi tên họ ở nhiều chỗ khác trên website."*

Kênh thứ hai — Twitter/X, nhưng theo cách rất cụ thể:

> *"Tôi trả lời vào các cuộc trò chuyện liên quan tới tương tác với AI và kỷ nguyên AI mới. Và **không phải kiểu nói thẳng về sản phẩm** — không phải 'mua sản phẩm của tôi đi' hay 'tôi đang build cái này cái kia' — mà chỉ **gợi ý tới thứ liên quan tới sản phẩm**."*

Đây là kênh yếu nhất của case: 38.000 khách duy nhất tổng cộng là con số **rất nhỏ**. Ước tính tỉ lệ chuyển đổi thô 1.200/38.000 ≈ **3,2%** — cao bất thường cho traffic lạnh, gợi ý traffic của anh **rất đúng đối tượng** (đến từ các cuộc thảo luận AI, không phải quảng cáo rải thảm).

![Chiến lược tăng trưởng](screenshots/07_08m00s_ch-growth-strategy-for-rabbitholes-ai.jpg)

## 8. Tech stack và cấu trúc chi phí — con số đẹp nhất case ⭐⭐

| Hạng mục | Công cụ |
|---|---|
| Code | **Cursor** (~$200/tháng) |
| Landing page | Next.js, host trên Vercel (~$50/tháng) |
| App | **Electron** + React + TypeScript |
| Tích hợp AI | **Vercel AI SDK** |
| Hosting phụ | Cloudflare |

Về AI SDK, anh nói đây là **chất xúc tác lớn**:

> *"Nó cho tôi một lớp trừu tượng tuyệt vời, tôi chỉ cần tập trung vào front-end và gần như không phải lo gì về việc tích hợp với nhiều nhà cung cấp AI khác nhau."*

**Cấu trúc chi phí là thứ đáng nhìn nhất:**

> *"Gần như không tốn gì. Tôi chỉ phải trả tiền host landing page, và tôi gần như đưa được về 0, nhưng vì tôi là dân Next.js hư hỏng nên tôi host trên Vercel với vài thứ màu mè, tốn khoảng **$50/tháng**. Và tôi có subscription Cursor khoảng **$200/tháng**. Nhưng đó là thứ tôi chỉ phải chi vì **tôi phải tiếp tục làm tính năng mới, không phải để duy trì sản phẩm hiện có**."*

Câu cuối là điểm mấu chốt: **chi phí duy trì gần bằng 0, chi phí còn lại là chi phí phát triển tự nguyện**. Nếu Praneeth ngừng làm việc hôm nay, sản phẩm vẫn chạy và không ngốn tiền. Rất ít mô hình SaaS có được tính chất này.

![$50/tháng](screenshots/10_10m42s_usd-50.jpg)

## 9. Lời khuyên cuối — cái bẫy "làm để gây ấn tượng với đồng nghiệp"

> *"Tôi đã thử build sản phẩm suốt 6-7 năm qua, và phần lớn 5 năm gần nhất tôi vận hành như một [người thợ giỏi nghề]. Là một entrepreneur, mục tiêu của bạn là **tìm ra product-market fit càng sớm càng tốt** và xây thứ làm cuộc sống người ta tốt hơn. Nhưng thứ tôi đã làm là **cố gây ấn tượng với đồng nghiệp của mình** — đó hoàn toàn không phải tư duy tôi cần có."*

*(Cụm trong ngoặc vuông là chỗ auto-caption nghe không rõ — bản ASR ghi "a skills man". Ý của anh rõ ràng: anh làm sản phẩm để khoe kỹ năng với dân trong nghề, không phải để giải quyết vấn đề của khách hàng.)*

Đây là bệnh phổ biến của dev giỏi: chọn bài toán **thú vị về mặt kỹ thuật** thay vì bài toán **có người trả tiền**. Praneeth mất 5 năm mới thoát ra.

![Số liệu kinh doanh](screenshots/08_09m00s_ch-numbers-behind-rabbitholes-ai.jpg)

## 10. Cảnh báo thiên kiến nguồn

- Video này có **quảng cáo Starter Story Build khá nặng** — chèn giữa video ở phút 6:10 và lặp lại ở cuối, với UTM riêng cho case này (`utm_campaign=praneeth`). Kênh đang bán khoá học "build app bằng AI", nên các case chứng minh *"một người có thể build sản phẩm nhanh bằng AI"* được ưu tiên lên sóng.
- Kênh **chỉ phỏng vấn người thành công**. Số lượng người làm LTD rồi chết vì không bán được tiếp không xuất hiện ở đây.
- $80K trong 6 tháng cho một người từng có lương $250K/năm là **chưa hoà vốn cơ hội**. Video không nói ra điều này. Nếu bạn nghỉ việc lương cao để làm cái này, bảng cân đối thật của bạn tính tới giờ vẫn **âm**.
- Con số "gross $80K, profit $75K" **không trừ lương founder** — đó là chuẩn chung của kho này, nhưng cần nhớ.

## 11. Áp dụng cho tôi (indie hacker VN)

**Sao chép được gì — case này thuộc nhóm dễ áp dụng nhất trong kho:**

1. **Test bằng one-time purchase trước, luôn.** Đặt giá $19-29 cho 100 khách đầu. Nếu 100 người không chịu trả một lần duy nhất, đừng mơ họ trả hàng tháng. Đây là **bài kiểm tra rẻ nhất** để biết có PMF hay không.
2. **BYOK là vũ khí cho người thiếu vốn.** Nếu sản phẩm của bạn có AI, hãy cho khách dán API key của họ. Bạn xoá sạch rủi ro lớn nhất của indie hacker Việt: **một khách dùng quá tay là bay hết lợi nhuận của 20 khách khác**, trong khi bạn không có tiền dự phòng.
3. **Đóng app desktop để xoá chi phí server.** Electron/Tauri chạy trên máy khách. Không server = không cần thẻ tín dụng quốc tế hạn mức cao, không lo hoá đơn AWS bất ngờ, không lo scale.
4. **Bậc thang giá theo mốc khách hàng.** $29 → $49 → $99. Người mua sớm được lời, bạn có cớ để truyền thông mỗi lần tăng giá.
5. **Viết H1 gọi thẳng tên ICP.** Không phải "AI chat tốt hơn" mà "Dành cho người dùng đang mở 5 tab AI cùng lúc".
6. **Chọn thị trường mà ICP đã có thẻ tín dụng quốc tế** — power user AI là ví dụ hoàn hảo. Họ đã trả ChatGPT, họ trả bạn được.

**Rào cản thật, không tô hồng:**

- **LTD không phải doanh thu, nó là dòng tiền.** $80K của Praneeth **không lặp lại**. Tháng nào không bán được thì tháng đó gần như $0. Đây là lý do anh đang phải quay lại recurring. Đừng nhìn con số $80K rồi tưởng mình có business ổn định — bạn đang có một **chiến dịch bán hàng**, chưa phải một **doanh nghiệp**.
- **Bán lifetime là hứa hỗ trợ vĩnh viễn.** 1.200 khách lifetime nghĩa là 1.200 người có quyền đòi support, đòi tương thích với model AI mới, đòi fix bug — mãi mãi, không thêm đồng nào. Với solo founder Việt phải cân bằng công việc chính, đây là **nợ vận hành** dễ bị đánh giá thấp.
- **BYOK giết mất một phần lớn thị trường.** Ai không biết lấy API key OpenAI thì không mua được. Bạn đang tự giới hạn vào tệp kỹ thuật, cũng chính là tệp **khó tính nhất và ít chịu trả tiền nhất**. Ở VN tệp này còn nhỏ hơn nữa.
- **Thanh toán quốc tế.** Để bán $49 cho khách Mỹ/EU bạn cần Paddle/Lemon Squeezy/Stripe qua công ty nước ngoài. Chi phí lập và duy trì công ty (Wyoming LLC hoặc tương đương) khoảng **$300-800/năm**, cộng thời gian làm thuế. Đây là chi phí ẩn không xuất hiện trong con số "$250/tháng" của Praneeth.
- **Rào cản tiếng Anh nằm ở landing page**, không phải ở code. Toàn bộ tăng trưởng của anh dựa vào **copy H1 gọi tên ICP** và **trả lời tự nhiên trong các cuộc thảo luận AI trên X**. Cả hai đều đòi tiếng Anh tự nhiên. Đây là nút thắt thật với người Việt — đầu tư vào chỗ này trước khi đầu tư vào tính năng.
- **Chi phí Cursor $200/tháng** ≈ 5 triệu đồng — với indie hacker VN đây là khoản thật, không phải làm tròn.
- **Rủi ro sản phẩm bị nuốt.** Đây là wrapper quanh các model AI. Nếu OpenAI hoặc Anthropic ra giao diện canvas gốc, giá trị lõi biến mất. Cùng loại rủi ro nền tảng với các case wrapper khác trong kho.

**Khi nào KHÔNG dùng mô hình này:**

- Khi sản phẩm **có chi phí biến đổi thật mỗi lần dùng** mà bạn không đẩy sang khách được (chạy model trên server của bạn, gửi SMS, lưu trữ lớn, gọi API bên thứ ba có phí). LTD lúc đó là bán một khoản lỗ dài hạn.
- Khi sản phẩm là **dịch vụ chạy liên tục** (giám sát, đồng bộ, tự động hoá nền, đăng bài theo lịch). Người ta trả subscription cho thứ **làm việc cho họ hàng ngày** — bán đứt là tự bắn vào chân.
- Khi bạn **cần MRR để gọi vốn hoặc để bán công ty**. Người mua định giá theo bội số ARR; doanh thu one-time gần như không được tính.
- Khi ICP của bạn **chưa bão hoà subscription**. Lý do LTD thắng ở đây rất đặc thù — power user AI đã trả quá nhiều subscription rồi. Nếu bạn bán cho nha sĩ hay chủ quán cà phê, họ không có "subscription fatigue" và subscription vẫn là mô hình tốt hơn.

## Nguồn

- Video: <https://www.youtube.com/watch?v=hYW9YDwHE20> (12:38, đăng 08/10/2025, 51.373 view)
- Sản phẩm: <https://www.rabbitholes.ai/> · Founder: <https://x.com/praneethpike>
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
