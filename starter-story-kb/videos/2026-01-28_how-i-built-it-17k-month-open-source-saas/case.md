---
id: RPM4ImzcIFc
slug: postiz-open-source-distribution
product: Postiz
founder: Nevo (Nevo David)
tagline: Mã nguồn mở là KÊNH PHÂN PHỐI chứ không phải mô hình kiếm tiền — 25.000 sao GitHub, 5 triệu lượt tải, nhưng chỉ 472 người trả tiền và churn 19%
revenue_usd_month: 17000
revenue_basis: founder nói 17K MRR và mở dashboard; khớp với 472 subscriber (ARPU ~36 USD/tháng). Không có mâu thuẫn số trong video này. Đây là ảnh chụp tháng 01/2026 — 6 tháng sau cùng kênh quay lại và Postiz đã lên 143K MRR nhờ một chuyện khác hẳn
model: open-source-cloud-upsell
category: social-media-tools
audience: B2B/B2D — developer tự host, solo builder, marketer, agency lên lịch đăng mạng xã hội
started: khoảng 2024, sau 2 năm làm ở một công ty open source và 1 năm tư vấn open source
time_to_first_sale: không nêu
time_to_scale: vài năm để đạt 25.000 sao GitHub và 17K MRR
team_size: nhỏ, không nêu rõ (bản phỏng vấn sau nêu 3 người)
funding: bootstrapped
main_channel: mã nguồn mở — GitHub trending, Hacker News Show HN, r/selfhosted, Lemmy, dev.to/Medium/HackerNoon qua Google Discover
tech_stack: [Next.js, Railway, Vercel, Cloudflare R2, Resend, dub.co, Plausible, OpenAI, fal.ai, beehiiv, Cursor, WebStorm, Semrush, Ahrefs, Discord, Sentry, GitHub Actions, Docker]
key_metrics:
  mrr: 17.000 USD
  subscribers: 472
  arpu: khoảng 36 USD/tháng (tự tính 17.000 / 472)
  churn: 19%/tháng — founder tự nhận là rất cao và đang cố hạ
  trials: 3.830 trial kể từ tháng 08/2025
  trial_to_paid: 21%
  github_stars: hơn 25.000
  downloads: 5.000.000 lượt
  platforms_supported: 25 nền tảng mạng xã hội
  gross_margin: khoảng 80%
  biggest_cost: 600 USD/tháng cho dịch vụ convert video sang đúng tỉ lệ từng nền tảng
replicability_vn: 3
difficulty: 4
video_url: https://www.youtube.com/watch?v=RPM4ImzcIFc
published: 2026-01-28
views: 35875
tags: [open-source, github, hacker-news, reddit, self-hosted, distribution, social-media-tools, churn, devtools, seo]
---

# Postiz — $17K/tháng và toàn bộ playbook marketing bằng mã nguồn mở

> **Tóm tắt 30 giây:** Nevo build Postiz — công cụ lên lịch đăng lên 25 nền tảng mạng xã hội, một thị trường có **hàng nghìn đối thủ**. Vũ khí khác biệt duy nhất của anh là **mở mã nguồn**: 25.000 sao GitHub, **5 triệu lượt tải**, và anh chia sẻ nguyên văn playbook 5 bước để lọt vào GitHub trending. Nhưng con số thật đáng đọc lại nằm ở chỗ khác: **17K MRR chỉ đến từ 472 người trả tiền, với churn 19%/tháng**. Nói cách khác, mã nguồn mở cho anh *phân phối miễn phí* chứ **không** cho anh *khách hàng trung thành* — và 6 tháng sau, thứ đưa Postiz lên $143K không phải open source.

![$17K/tháng](screenshots/02_01m54s_usd-17k.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR | **$17.000** |
| Người trả tiền | **472** |
| ARPU (tự tính) | ~$36/tháng |
| Churn | **19%/tháng** — founder tự nhận là rất cao |
| Trial từ 08/2025 | 3.830 |
| Trial → trả tiền | 21% |
| Sao GitHub | hơn 25.000 |
| Lượt tải | 5.000.000 |
| Nền tảng hỗ trợ | 25 (nhiều nhất thị trường) |
| Biên lợi nhuận gộp | ~80% |

**Phép tính mà video không làm — nhưng bạn nên làm:**

- Churn 19%/tháng → vòng đời khách trung bình ≈ 1 / 0,19 ≈ **5,3 tháng** → **LTV ≈ $190**.
- 3.830 trial trong ~5 tháng ≈ 766 trial/tháng × 21% ≈ **160 khách mới/tháng**.
- Nhưng 472 khách × 19% ≈ **90 khách mất/tháng**.
- Ròng: **+70 khách/tháng ≈ +$2.5K MRR/tháng**, và tốc độ mất khách tăng theo quy mô.

Đây là hình ảnh của một doanh nghiệp **có phân phối tốt nhưng giữ chân kém**. Giữ nguyên đà này, Postiz sẽ đụng trần quanh $30-40K MRR khi số khách mất bằng số khách vào. Ghi nhớ điều này — mục 7 sẽ cho biết chuyện gì thực sự xảy ra sau đó.

![Chỉ số kinh doanh](screenshots/03_02m59s_metric.jpg)

## 2. Vì sao mở mã nguồn lại là cơ hội — cơ chế thật ⭐⭐⭐

Lập luận của Nevo bắt đầu từ một quan sát về năm 2026:

> *"Hôm nay ai cũng có thể build gần như bất cứ thứ gì. Và đó chính là lý do đây nên là năm của open source so với những năm trước — bởi vì **cái gì bạn build được thì người khác cũng build được**. Vậy tại sao không mở mã nguồn?"*

Postiz là công cụ lên lịch mạng xã hội — *"nếu bạn tìm 'social media scheduling tool', có hàng nghìn cái"*. Mở mã nguồn là cách anh **thoát khỏi biển đỏ** bằng một trục mà đối thủ SaaS đóng không dám đi.

Điểm quan trọng nhất, và cũng là điểm nhiều người hiểu sai:

> *"Developer **không phải chân dung khách hàng mua**, và họ gần như chắc chắn sẽ không trả tiền cho bạn. Đừng cố nghĩ cách cầu kỳ để bắt họ trả tiền. Bạn chỉ cần làm docs thật tốt. Hãy coi đây như **free tier của SaaS mà bạn không tốn một đồng chi phí vận hành** — vì họ tự deploy trên máy họ."*

**Vậy developer trả lại cho bạn thứ gì?** Nevo liệt kê 7 thứ:

1. **Xây brand.** Họ nói về bạn với người khác.
2. **Truyền miệng vào doanh nghiệp.** Developer đang làm ở công ty mà bộ phận marketing đang tìm giải pháp → *"À, tôi biết cái này."*
3. **UGC trên mạng xã hội.** *"Ngày nào tôi search 'Postiz' cũng thấy có developer đang đi bán Postiz hộ tôi."*
4. **Contribution.** Không hẳn làm bạn code nhanh hơn, nhưng cho **feedback và bug report cực nhanh**, và họ trở thành advocate.
5. **SEO miễn phí.** Người ta tự viết blog post *how to use Postiz*, tự viết review.
6. **Listing directory.** Rất nhiều thư mục open source có **domain authority cao** — backlink chất lượng miễn phí.
7. **Uy tín với người không phải developer.** Khách vào GitHub thấy có commit vài ngày trước → biết sản phẩm còn sống.

Và nơi tiền lớn thật sự nằm:

> *"Thứ nhiều người làm và **thường là chỗ tiền lớn nhất trong open source** — đó là **self-hosting enterprise support**. Hãy tưởng tượng tôi làm công cụ lên lịch mạng xã hội nhưng đang làm việc với một doanh nghiệp lớn — họ sẽ **không bao giờ** để dữ liệu ra ngoài. Họ sẽ muốn self-host, nhưng họ cũng cần support."*

**Về nỗi sợ bị copy** — Nevo phản bác thẳng:

> *"Đừng sợ ai đó copy sản phẩm của bạn, vì hôm nay thứ duy nhất thắng cuộc thường là **brand**. Tôi thấy rất nhiều người copy Postiz, self-host ở đâu đó thành một giải pháp khác hẳn để cạnh tranh với tôi. Tôi kiểu 'ôi tôi căng thẳng quá'. Rồi một hai tuần sau kiểm tra lại, họ đã bỏ dự án. **Không có cách nào bạn là brand cả** — bạn mới là người tạo ra giải pháp open source đó. Ai cạnh tranh với bạn cũng sẽ luôn chậm hơn bạn một bước."*

Pat Walls chốt lại đúng bản chất: *"Trong một thế giới mà AI viết được mọi đoạn code và bản thân nó cũng đang tham chiếu code open source để viết — **giá trị của code còn lại bao nhiêu?** Không nhiều. Nó nằm ở brand."*

![Vì sao open source là cơ hội](screenshots/06_06m34s_ch-why-open-source-is-a-great-opportunity.jpg)

## 3. Playbook mã nguồn mở — nguyên văn 5 bước ⭐⭐⭐

Đây là phần đáng giá nhất video. Nevo từng **tư vấn riêng mảng này suốt một năm** cho nhiều công ty — anh nói đây là toàn bộ quy trình anh vẫn chạy hàng tuần.

### Giai đoạn 0 — Chuẩn bị (làm trước khi launch)

| Việc | Chi tiết |
|---|---|
| **GitHub = landing page** | *"GitHub của bạn TRỞ THÀNH landing page. Hãy đối xử với nó y như website chính, thậm chí tốt hơn."* Vào repo Postiz mà xem cách anh viết. |
| **Định vị bằng một câu** | Nếu đã có đối thủ, cách nhanh nhất là viết thẳng: **open-source alternative to X**. Câu đó cho người đọc context nhanh nhất. |
| **Chọn license** | 3 lựa chọn chính: **MIT · Apache 2 · AGPL-3**. Cân nhắc kỹ. (AGPL-3 là loại buộc bên dùng làm SaaS phải mở mã — hàng rào chống copy thương mại.) |
| **Tạo sẵn issue** | Developer vào repo **không biết nên làm gì**. Tạo sẵn issue cho từng tính năng bạn muốn có → họ chỉ cần nói *"assign tôi issue này"*. Nhanh hơn nhiều so với để họ tự nghĩ. |
| **Mở Discord** | *"Vào Discord của Postiz và copy y hệt danh sách channel như tôi."* |
| **Docs deploy** | Cực kỳ quan trọng. *"Nếu họ không biết deploy, họ sẽ churn. Họ sẽ không clone repo. Bạn sẽ không trending."* |
| **Docker** | *"Tốt hơn nhiều nếu bạn có Docker — deploy dễ hơn rất rất nhiều."* |

### Bước 1 — Chuẩn bị tài khoản TRƯỚC 2 tuần

- **Hacker News**: đăng ký trước ~2 tuần.
- **Reddit**: đăng ký trước và **cày karma**. *"Không có karma thì gần như mọi bài của bạn sẽ bị lọc."*
- **Lemmy** (ASR đọc là *Lei/Lemie*): Reddit self-hosted, ít người biết. *"Họ không giỏi cái gì khác ngoài open source — nhưng với open source thì họ điên rồ. Mỗi lần tôi post lên Lemmy đều được ít nhất 100 upvote."*
- **dev.to · Medium · HackerNoon**.

### Bước 2 — Viết bài lên dev.to / Medium / HackerNoon

Nội dung: *how I built X* hoặc *tôi vừa launch dự án open source này*. Sau đó viết thêm **listicle** kiểu *top 10 open source project bạn nên xem năm 2026*.

**Cơ chế thật ít ai nói:**

> *"Có thứ gọi là **Google Discover feed**. Nếu bạn xem các bài của tôi trên dev.to, Medium, HackerNoon — **đây là nguồn traffic chính của tất cả chúng**. Nên phải đầu tư vào **tiêu đề và ảnh bìa**, y như khi bạn làm YouTube, vì người ta chỉ nhìn thấy cái feed Discover đó."*

Nghĩa là bạn đang **mượn hai thứ** của các nền tảng này: domain authority cho SEO, và **tư cách được Google Discover phân phối** — thứ mà một blog mới toanh của bạn không bao giờ có.

### Bước 3 — Hacker News

Tạo post mới, tiêu đề **`Show HN: <tên dự án>`**, và link tới **GitHub repo, KHÔNG phải website chính**.

> *"Họ rất kén thứ họ cho lên. Không có gì đảm bảo bạn lên được. Nhưng **Hacker News yêu dự án open source**. Nếu bạn đưa dự án open source vào, xác suất lên main feed rất rất cao — và khi đó bạn có thể kỳ vọng gần **10.000 view**."*

Đây đúng là kênh đã đưa [ChartDB](../2026-02-25_i-built-a-niche-app-to-9k-mrr/case.md) từ 0 lên hàng nghìn engineer **trong đúng một ngày**. Hai case độc lập, cùng một cửa.

### Bước 4 — Reddit r/selfhosted

Đây là **kẽ hở cấu trúc đáng giá nhất trong bài**:

> *"Nếu bạn KHÔNG open source mà đi post dự án lên Reddit, bạn sẽ bị lọc hoặc bị ban vì tự quảng cáo bị cấm. Nhưng cái hay của open source là: nếu bạn có thứ mã nguồn mở và bạn vào **r/selfhosted**, **người ta đang chờ bạn post** và tự quảng cáo cho chính mình. Không chỉ vậy — **mỗi lần bạn có phiên bản mới, họ lại muốn xem lại**, lần này qua lần khác."*

Quy tắc post:
- **Xin sao** (ask for a star) một cách thẳng thắn.
- **Cực kỳ khiêm tốn, xuống đất.** Làm như build in public.
- Dùng **"I", không dùng "we"**.
- Post lại **mỗi tháng**, mỗi lần một release mới với danh sách tính năng.
- Cross-post: r/webdev, r/programming. Nếu ở mảng AI: **r/LocalLLaMA, r/AI_Agents, r/LangChain**.

### Bước 5 — Dồn mọi thứ bạn đang có

X, LinkedIn, newsletter — **tất cả trỏ về GitHub**, không phải website.

### Quy tắc bao trùm — và đây là lý do playbook hoạt động ⭐⭐⭐

> *"Đảm bảo cả 5 bước này diễn ra **TRONG CÙNG MỘT TUẦN**. Cực kỳ quan trọng. Để bạn lọt vào main trending feed."*

**Vì sao?** GitHub trending không xếp hạng theo **tổng số sao**, mà theo **tốc độ tăng sao trong một khoảng ngắn**. 5.000 sao rải đều một năm = không bao giờ trending. 500 sao trong một tuần = trending. Đây là lý do bạn phải **nén toàn bộ traffic vào một cửa sổ thời gian**, thay vì post lai rai cho "an toàn".

Và khi đã lên trending, hiệu ứng tự nhân: *"bạn sẽ thấy số sao bay lên rất nhanh, rất nhiều người vào Discord, và nhiều issue, pull request, fork hơn hẳn."*

![Playbook open source](screenshots/07_10m43s_ch-open-source-playbook.jpg)

## 4. Sản phẩm và mô hình giá

Postiz chạy **SaaS thuần** với 4 gói: Standard, Team, Pro, Ultimate — càng lên cao càng nhiều channel và nhiều tính năng.

> *"Chúng tôi muốn người ta dùng gói Standard, nhưng cũng muốn upsell lên gói cao hơn **dựa trên tính năng chứ không chỉ dựa trên số channel**."*

**Điểm khác biệt so với đa số công ty open source:** *"Với chúng tôi **không có khác biệt nào giữa bản open source và bản cloud**. Bạn self-host được toàn bộ Postiz. Chúng tôi để rất nhiều docs hướng dẫn."*

Cái giá phải trả cho sự hào phóng đó chính là **churn 19%**. Nếu bản miễn phí bằng bản trả tiền, thứ duy nhất bạn bán là **sự tiện lợi** — và tiện lợi thì dễ bỏ. Đây là đánh đổi trực tiếp, không phải chi tiết vụn.

Demo sản phẩm: kết nối 25 channel, viết một post rồi **tuỳ biến riêng cho từng nền tảng**, lịch dạng calendar, AI tools (tạo ảnh, video, bold text), và **public API** — *"nhiều người dùng lắm, và vì chúng tôi open source nên developer thích dùng chúng tôi hơn các giải pháp đóng"*, cắm thẳng vào n8n hoặc workflow tự động.

## 5. Tech stack và chi phí thật ⭐⭐

Đây là một trong những bảng chi phí minh bạch nhất trong kho.

| Hạng mục | Công cụ | Chi phí |
|---|---|---|
| Backend + web marketing | **Railway** | không nêu |
| App Next.js | **Vercel** (chỉ host Next.js, không dùng Vercel API) | không nêu |
| SEO | **Semrush** | không nêu |
| SEO dashboard | **Ahrefs** (chỉ mua gói dashboard, không mua full) | **$20/tháng** |
| Email giao dịch | **Resend** | không nêu |
| Lưu trữ file | **Cloudflare R2** | không nêu |
| Short link + affiliate | **dub.co** | không nêu |
| Analytics | **Plausible** | không nêu |
| AI ảnh và text | **OpenAI**, **fal.ai** (+ một dịch vụ ASR đọc không rõ, có thể là kie.ai) | *chi phí lớn nhất* |
| Convert video | dịch vụ transcoding (ASR đọc *translated* — nhiều khả năng là **Transloadit**) | **$600/tháng** |
| SEO content | **Outrank** (ASR đọc *Outrrench*) — 1 bài SEO mỗi ngày | không nêu |
| AI coding | **Cursor** | **$20/tháng** (*"tôi không phải người dùng nặng"*) |
| IDE | **WebStorm** | không nêu |
| Newsletter | **beehiiv** (dùng headless) | không nêu |
| Support khách | **Discord** | **$0** |
| Copilot, Sentry, GitHub Actions | | **$0 — miễn phí cho open source** |

**Biên lợi nhuận gộp ~80%.**

Hai chi tiết đáng ăn cắp ngay:

1. **$600/tháng cho convert video** là chi phí lớn bất ngờ, và lý do rất thật: *"Tôi muốn MỌI post đều đăng được, không muốn có lỗi nào. Nghĩa là tôi phải convert video sang đúng kích thước của nền tảng sắp đăng. Không làm thì nó fail."* Đây là loại chi phí mà người mới **luôn quên** khi định giá sản phẩm đa nền tảng.
2. **Open source làm giảm chi phí vận hành thật**: Copilot, Sentry, GitHub Actions đều miễn phí cho repo mở. Cộng thêm support chạy trên Discord = $0. Đó là một phần lý do biên 80%.

![Ahrefs $20](screenshots/09_19m35s_usd-20.jpg)

## 6. Lời khuyên cuối — và mâu thuẫn với phần còn lại của kho ⭐⭐

> *"Lời khuyên lớn nhất của tôi hơi gây tranh cãi. Tôi nghĩ bạn **nên học rất nhiều trước khi build** — nhưng cũng đừng rơi vào analysis paralysis. Tôi thất bại ở rất nhiều startup lúc đầu, rồi tôi dừng lại và nói 'ok, đọc sách đi'. Đọc **Traction** về marketing, đọc **$100M Offers** của Alex Hormozi, đọc **Russell Brunson** về lead generation. Sau đó tôi bắt đầu ra quyết định thông minh hơn. Hãy dành **nửa thời gian học, nửa thời gian tạo ra thứ gì đó**."*

Anh còn cảnh báo một sai lầm cụ thể:

> *"Rất nhiều người chưa từng nghe gì về cái gì cả và cứ thế lao vào **B2C — thứ thường khó hơn nhiều với người không giỏi phân phối**. Rồi họ cày một năm, đóng cửa, rồi mới nói lẽ ra tôi nên làm B2B."*

**Mâu thuẫn thẳng với các case khác trong kho:**

| Quan điểm | Ai | Đúng khi nào |
|---|---|---|
| Học nhiều trước rồi mới build | Nevo (case này) | Bạn đã thất bại nhiều lần, hoặc đang chọn giữa các thị trường lớn cần cam kết dài |
| Cứ ship, gắn nút mua ngay | [Marc Lou](../2026-04-26_how-i-work-77k-month-solopreneur/case.md) | Sản phẩm build dưới 1 tuần — chi phí sai rẻ hơn chi phí học |
| Validate trước khi viết dòng code nào | [Once](../2026-05-10_i-built-a-20k-month-app-in-83-days/case.md) | Sản phẩm build trên 1 tháng |

**Cách hoà giải:** Nevo không nói ngược Marc Lou về *tốc độ ship*, anh nói về **tốc độ chọn thị trường**. Cái anh học từ sách là *positioning, offer, lead gen* — những thứ quyết định **bạn build cho ai**, không phải *bạn build nhanh chậm thế nào*. Với indie hacker VN, phân định thực tế: **chọn thị trường thì học kỹ, chọn tính năng thì ship nhanh.**

## 7. Điều video này KHÔNG nói — nhưng kho này biết ⭐⭐⭐

Đây là giá trị lớn nhất của việc có cả hai video trong cùng một kho.

Tháng 01/2026 (video này): Postiz **$17K MRR, churn 19%**, playbook open source đẹp đẽ.
Tháng 07/2026 ([video sau](../2026-07-30_how-postiz-went-from-17k-to-143k-month-in-4-months/case.md)): Postiz **$143K MRR**, churn xuống **13,7%**.

**Cái gì đã thay đổi?** KHÔNG phải open source. Nevo **pivot sang agentic** — biến Postiz thành thứ mà AI agent (Claude, ChatGPT, OpenClaw) gọi thay cho người dùng bấm tay, rồi cưỡi một bài viral trên X đạt 7,2 triệu view.

**Bài học rút ra — và nó khá phũ:**

- **Open source đưa anh tới $17K rồi đứng lại.** Nó giải bài toán *biết đến* rất tốt, giải bài toán *giữ chân* rất tệ (19% churn). Nếu bạn định copy playbook mục 3, hãy copy nó như một **chiến lược ra mắt**, không phải chiến lược tăng trưởng.
- **Nhưng open source là ĐIỀU KIỆN CẦN cho cú nhảy sau đó.** Chính vì Postiz có API công khai, có docs, có repo mở mà một người dùng ngẫu nhiên mới tự động hoá được nó bằng agent và viết bài viral. Bạn không tính trước được cú đó — bạn chỉ **tạo bề mặt để nó xảy ra**.
- **Đọc case nào cũng nên hỏi: 6 tháng sau con số này còn đúng không?** Kênh Starter Story quay founder ở đúng một lát cắt. Ở lát cắt tháng 01, câu chuyện là *open source thắng*. Sự thật đầy đủ hơn là *open source dựng sân, trend AI ghi bàn*.

![Cộng đồng open source ngách](screenshots/08_16m19s_ch-niche-open-source-communities.jpg)

## 8. Cảnh báo thiên kiến nguồn

Video này có **mật độ quảng cáo cao bất thường** — hãy tách bạch khi đọc:

- **Sponsor là Delve** (nền tảng compliance SOC 2 / ISO 27001). Đoạn dẫn vào quảng cáo được **may khéo vào chính câu chuyện**: *"cộng đồng open source yêu minh bạch, họ sẽ quay bạn về bảo mật và compliance, họ có thể hỏi bạn về SOC 2..."*. Đó là **kịch bản bán hàng, không phải phát hiện từ founder**. Nevo không hề nói anh cần SOC 2 để bán Postiz, cũng không nói anh dùng Delve.
- **Hai lần chèn Starter Story Build** (bootcamp trả phí) và **niche communities playbook** (lead magnet). Cả hai đều ở vị trí đắc địa nhất video.
- Kênh chỉ phỏng vấn người thành công. Không có video về 100 dự án open source có 300 sao và $0 doanh thu — mà đó mới là phân phối xác suất thật.

**Số liệu thì đáng tin**: Nevo mở dashboard, và anh **tự nêu churn 19%** — không ai bịa ra con số làm mình xấu đi. Đây là dấu hiệu founder trung thực.

## 9. Áp dụng cho tôi (indie hacker VN)

**Sao chép được gì — cụ thể:**

1. **Cửa r/selfhosted là thật và gần như miễn phí.** Đây là subreddit hiếm hoi mà **tự quảng cáo chính là nội dung được mong đợi**, miễn là bạn thật sự mở mã. Không cần tiếng Anh hoàn hảo — chỉ cần README rõ ràng và một bản Docker chạy được. Ba case độc lập trong kho (Postiz, [ChartDB](../2026-02-25_i-built-a-niche-app-to-9k-mrr/case.md), [Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md)) đều đi qua cửa Reddit này.
2. **Nén launch vào một tuần.** Đây là chi tiết kỹ thuật quan trọng nhất bài. Chuẩn bị tài khoản HN/Reddit/Lemmy **trước 2 tuần**, cày karma, rồi bắn tất cả trong 7 ngày.
3. **Viết bài trên dev.to / Medium / HackerNoon để mượn Google Discover.** Với người Việt, đây là kênh dễ hơn viết blog riêng nhiều lần — bạn không cần domain authority, chỉ cần **tiêu đề + ảnh bìa tốt**.
4. **Tạo sẵn issue "good first issue"** ngay ngày đầu. Chi phí 30 phút, đổi lại contributor thật.
5. **Bắt chước cấu trúc chi phí**: Discord thay vì Intercom ($0), Sentry/Copilot/GitHub Actions miễn phí cho repo mở, Ahrefs chỉ mua gói dashboard $20 thay vì full $129.

**Rào cản thật — không tô hồng:**

- **Churn 19%/tháng là án tử với ARPU thấp.** Với ARPU $36 thì LTV chỉ $190 — vẫn sống được vì kênh miễn phí. Nếu bạn định làm bản Việt hoá với giá 99K-199K/tháng (~$4-8), LTV rơi xuống **$20-40**. Ở mức đó **không kênh trả phí nào có lãi**, và bạn buộc phải sống 100% bằng kênh miễn phí — tức là bạn không có phương án B.
- **Open source nghĩa là bạn phải support bằng tiếng Anh, công khai, mãi mãi.** GitHub issue và Discord không có giờ hành chính. Đây là **chi phí ẩn lớn nhất** và nó không giảm khi doanh thu tăng. Nevo trước đó đã bỏ nghề tư vấn vì *"làm quá nhiều meeting và nói chuyện với quá nhiều người làm tôi phát hoảng"* — rồi anh chọn một mô hình mà cộng đồng nói chuyện với anh cả ngày.
- **Bạn cho không bản đầy đủ.** Postiz không giữ tính năng nào cho riêng bản cloud. Đó là lý do khách rời dễ dàng. Nếu bạn định copy, **hãy quyết định từ ngày đầu** đâu là ranh giới open-core (thường là SSO, phân quyền, audit log, multi-tenant).
- **Chi phí compliance khi lên enterprise.** Nevo nói tiền lớn nằm ở enterprise self-host support — nhưng doanh nghiệp lớn sẽ đòi SOC 2/ISO 27001. Theo case [ChartDB](../2026-02-25_i-built-a-niche-app-to-9k-mrr/case.md) trong kho: **~$500/tháng chỉ riêng tool compliance**, chưa tính audit. Từ VN, việc ký hợp đồng enterprise Mỹ còn vướng pháp nhân, hợp đồng, và múi giờ.
- **Rủi ro nền tảng ở tầng API.** Postiz sống nhờ API của 25 mạng xã hội. Mỗi lần X, LinkedIn hay Instagram siết API là một lần sản phẩm hụt tính năng. Chi phí bảo trì loại này **tăng tuyến tính theo số nền tảng** — 25 nền tảng là 25 nguồn hỏng.

**Khi nào KHÔNG dùng mô hình này:**

- **Khi khách hàng của bạn không phải developer.** Toàn bộ động cơ phân phối chạy bằng developer — GitHub, HN, r/selfhosted, dev.to. Nếu bạn bán cho chủ shop, giáo viên, nhân viên sale, mở mã nguồn cho bạn **con số 0 về phân phối** mà vẫn tốn toàn bộ chi phí support và mất hết lợi thế sản phẩm.
- **Khi giá trị cốt lõi nằm ở dữ liệu hoặc mạng lưới, không ở code.** Mở mã một sản phẩm mà giá trị là dataset độc quyền thì bạn chẳng cho đi gì — nhưng cũng chẳng ai quan tâm để star.
- **Khi bạn cần doanh thu trong 90 ngày.** Postiz mất vài năm để có 25.000 sao. Cửa HN/Reddit cho bạn một đợt traffic, không cho bạn dòng tiền đều. Cần tiền nhanh thì xem [Late](../2026-03-04_zero-to-40k-month-with-one-marketing-channel-no-soci/case.md) (Google Ads đáy phễu) hoặc [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md).
- **Khi bạn một mình và không chịu nổi phản hồi công khai.** Repo mở = mọi lỗi của bạn hiện ra trước hàng nghìn người, bằng tiếng Anh.

![Nhiều dịch vụ miễn phí cho open source](screenshots/10_20m23s_usd-0.jpg)

## Nguồn

- Video: <https://www.youtube.com/watch?v=RPM4ImzcIFc> (22:52, đăng 28/01/2026, 35.875 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
- Sản phẩm: <https://postiz.com/> · Founder: <https://x.com/wickedguro>
- **Đọc tiếp phần 2 của chính case này:** [Postiz — $17K → $143K trong 4 tháng](../2026-07-30_how-postiz-went-from-17k-to-143k-month-in-4-months/case.md)
- *Lưu ý ASR: phụ đề tự động đọc sai tên sản phẩm thành Posties/Postis/Opus. Tên đúng là **Postiz** (theo mô tả video). Lemmy bị đọc thành Lei/Lemie, HackerNoon thành Hackeron/Hackernon, dev.to thành Devo2, Plausible thành Flossible, Cursor thành Corser, beehiiv thành Beehive, Semrush thành Simrush. Hai tên tôi KHÔNG chắc chắn và đã ghi rõ trong bảng tech stack: dịch vụ transcoding $600/tháng và công cụ SEO Outrank.*
