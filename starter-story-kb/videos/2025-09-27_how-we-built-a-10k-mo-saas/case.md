---
id: 3eY71OS4MFw
slug: setter-ai-fake-landing-page-deposit
product: Setter AI
founder: Josef và Timo (Timo ở Bangkok)
tagline: Kiếm $500 từ một LANDING PAGE GIẢ với DEMO GIẢ trước khi viết dòng code nào — và chỉ 38 khách hàng tạo ra $10K MRR
revenue_usd_month: 10000
revenue_basis: đúng $10K tháng gần nhất; tháng 8 là tháng thấp điểm của B2B, đã có tháng cao hơn
model: b2b-high-ticket-saas
category: sales-automation
audience: B2B — ngành điện mặt trời, coach, dịch vụ tài chính; thay thế nhân viên sales
started: landing page dựng nhiều tháng trước khi bắt đầu kinh doanh; thanh toán đầu tiên tháng 2/2024
time_to_first_sale: 500 USD qua Stripe TRƯỚC khi có sản phẩm
time_to_scale: hơn một năm lên 10K MRR
team_size: 2
funding: bootstrapped; đã nộp YC 5 lần, được 1 lần phỏng vấn, chưa được nhận
main_channel: SEO — landing page giả xếp hạng Google, rồi free tools + bài so sánh + YouTube dài
tech_stack: [TypeScript, PostgreSQL, Render, Supabase, Puppeteer, OpenAI, Netlify, Cursor, Webflow, Plausible, Beehiiv, Calendly, Zapier, Ahrefs]
key_metrics:
  paying_customers: chỉ 38 — nhưng giá trị cao
  total_signups: khoảng 2.000 doanh nghiệp
  pricing: từ 50 USD tới 5.000 USD mỗi tháng
  first_validation: 500 USD đặt cọc hoàn lại 100%, tháng 2/2024
  margin: hơn 90% nếu không chạy quảng cáo, khoảng 80% khi có thuê freelancer
  biggest_cost: OpenAI API khoảng 250 USD/tháng
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=3eY71OS4MFw
published: 2025-09-27
views: 57383
---

# Setter AI — $500 doanh thu từ một trang web giả

> **Tóm tắt 30 giây:** Josef bỏ việc freelance và **mất trọn một năm xây mà không có traction nào**. Lần này hai người làm ngược: Timo dựng một **landing page giả** với **demo AI giả tạo bằng ElevenLabs**, đặt trên một **domain cũ đã được Google index**, và một nút đặt lịch. Trang đó xếp hạng Google. Một **công ty doanh thu tỉ đô** đặt lịch gọi. Họ thu **$500 đặt cọc qua Stripe trước khi viết dòng code nào**. Hôm nay: **$10K MRR từ đúng 38 khách hàng**.

![$50/tháng](screenshots/01_01m22s_usd-50.jpg)

## 1. Con số — và tỉ lệ đáng kinh ngạc

| Chỉ số | Giá trị |
|---|---|
| MRR | ~$10.000 |
| **Khách trả tiền** | **Chỉ 38** |
| Tổng đăng ký | ~2.000 doanh nghiệp |
| Giá | **$50 → $5.000/tháng** |
| Biên lợi nhuận | **90%+** (không quảng cáo) · ~80% khi thuê freelancer |
| Chi phí lớn nhất | OpenAI API ~$250/tháng |

> **38 khách hàng tạo ra $10.000/tháng** — trung bình **$263/khách/tháng**. Đối chiếu với [BulkMockup cần ~800 khách ở $15/tháng](../2026-02-11_how-i-built-a-12k-month-micro-saas/case.md) hay [Letterly cần 20.000 khách](../2025-11-24_how-he-makes-250k-per-month-from-a-simple-app-letter/case.md). Họ nói rõ lý do chọn hướng này: *"Chúng tôi tập trung nhiều hơn vào doanh nghiệp trả cao vì thấy **churn thấp hơn** với nhóm này."*

## 2. Landing page giả — chi tiết từng bước ⭐⭐⭐

![Landing page giả kiếm $500](screenshots/02_02m40s_ch-fake-landing-page-that-made-500.jpg)

Cấu trúc trang, đơn giản đến mức thô sơ:
- **Một tiêu đề H1 chứa từ khoá**
- **Video demo ở bên phải** — hoàn toàn giả, tạo bằng **ElevenLabs**
- **Một nút "Book demo"** trỏ tới link Calendly cá nhân
- *"Thật sự không có gì khác trên trang này."*

**Ba quyết định kỹ thuật làm nó chạy:**

1. **Dùng domain "ấm".** *"Một domain từ một doanh nghiệp khác tôi đã sở hữu và đã được Google index."* Domain mới toanh mất nhiều tháng để có uy tín; domain cũ thì không.

2. **Chọn từ khoá bằng Ahrefs.** *"Tôi lên Ahrefs, tìm từ khoá này, thấy nó có lượng tìm kiếm nhưng **không có độ khó**. Nên tôi đặt nó làm H1."* Từ khoá cụ thể: *cold call automation*.

3. **Ép Google index trong 24 giờ.** *"Một trong những yếu tố then chốt là **làm cho trang được index ngay lập tức**... Vào Google Search Console và **yêu cầu index trang đó**. Bằng cách đó bạn chắc chắn trang được index trong vòng 24 giờ."*

**Vì sao đây là cách validate rẻ nhất trong kho:** nó kiểm tra **cùng lúc ba giả thuyết** — (1) có người tìm kiếm vấn đề này không, (2) sản phẩm có hấp dẫn đủ để họ đặt lịch không, (3) họ có trả tiền không — mà **không cần xây gì cả**.

## 3. Deposit Framework — cách xin tiền cho thứ chưa tồn tại ⭐⭐⭐

![Framework validation](screenshots/04_05m00s_ch-10k-month-validation-framework.jpg)

**Bước 1 — Có một công việc.** ⭐
Đây là bước phản trực giác nhất trong cả kho:
> *"Điểm đau tốt nhất để tìm ý tưởng B2B **không phải là ngó quanh Reddit** — vì thẳng thắn mà nói, chủ doanh nghiệp không thật sự vào Reddit. **Cách tốt nhất là từng đi làm ở một doanh nghiệp.** Có một công việc thật ra là **lợi thế tuyệt đối** so với những indie hacker chưa bao giờ đi làm, vì họ không biết các quy trình diễn ra trong một doanh nghiệp."*

**Bước 2 — Dựng landing page** với nghiên cứu SEO cơ bản. Tìm từ khoá mà **người mua** sẽ gõ.

**Bước 3 — Gắn link Calendly.**
> *"Họ thấy mặt bạn trên cuộc gọi. Họ biết bạn là người thật. Họ tin bạn. Rồi bạn cố chốt họ ngay trên cuộc gọi và **quẹt thẻ của họ trong lúc đang gọi**."*

**Bước 4 — Deposit Framework.** ⭐⭐⭐
> *"**Đừng nói 'làm ơn trả tiền cho giải pháp chưa tồn tại của tôi'**, cũng đừng bắt họ trả hằng tháng cho thứ chưa có. Cách tốt hơn là **giao càng nhiều giá trị càng tốt và đưa ra một khoản đặt cọc hoàn lại 100%**. Ví dụ $500, một lần, và người mua có **toàn quyền truy cập sản phẩm khi nó ra mắt**. Bạn cũng có thể thêm chút cấp bách: 'khoản này giữ chỗ cho bạn trong đợt ra mắt đầu tiên'."*

Và:
> *"**Đi high ticket.** Nếu bạn đi hướng này và gọi điện với người mua, **đừng tính $20**. Hãy tính một con số nghiêm túc để bạn biết họ thật sự vào cuộc. **Không gì validate ý tưởng của bạn hơn việc ai đó quẹt thẻ.**"*

**Bước 5 — Cho nó thời gian ủ.** SEO cần thời gian, nhưng bù lại người tìm đến là người mua nghiêm túc.

### So sánh ba cách thu tiền trước trong kho

| Cách | Ai | Điều kiện phù hợp |
|---|---|---|
| **Đặt cọc hoàn lại 100%, high ticket** | Setter AI (case này) | B2B, giá cao, bán qua cuộc gọi |
| **Pre-sale license trọn đời, giá bậc thang** | [Gil / Subscribr](../2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-breakd/case.md) | Có sẵn danh sách email; B2C/B2B nhỏ |
| **Lifetime deal ngày ra mắt** | [Floga](../2026-03-29_my-app-made-120k-in-24-hours/case.md) | Sản phẩm đã xây xong, cần dòng tiền |

Điểm chung của cả ba: **tiền thật đổi lấy lời hứa**, và người bán chịu rủi ro thực thi thay vì rủi ro thị trường.

## 4. Khoảnh khắc biết đã validate

> *"Cách duy nhất để validate là **khi người mua quẹt thẻ**. Khi chúng tôi nhận khoản thanh toán Stripe $500 đầu tiên **trước khi có sản phẩm**, tôi biết cái này đã được validate. Đó là tháng 2/2024. Và tôi bất ngờ vì **có cả một công ty doanh thu tỉ đô đặt lịch gọi với tôi**. Với tôi đó là dấu hiệu rõ ràng: không ai khác đang làm việc này. Đây là cơ hội chưa được phục vụ."*

![$500](screenshots/03_04m12s_usd-500.jpg)

## 5. Tăng trưởng: nhân đôi vào đúng thứ đã validate ⭐⭐

> *"Chúng tôi đi thuần **inbound**. Chúng tôi quyết định nhân đôi vào cái đã hoạt động và cái đã validate ý tưởng — vì đó là nơi khách hàng đầu tiên đến — **và đó là SEO và nội dung**."*

Kết quả: trong **một tuần** sau khi ra website thật, họ lên trang một Google; giờ **xếp số 1 thế giới** cho từ khoá đó.

Ba chiến lược SEO:
1. **Công cụ miễn phí người ta tìm kiếm** — ví dụ "free sales script generator"
2. **Bài viết so sánh với công cụ lớn** — ví dụ "HubSpot alternatives"
3. **YouTube dạng dài** — *"và đây là cái rất bị đánh giá thấp"* ⭐

> *"**Hầu hết khách hàng chúng tôi chốt được đều đã xem ít nhất một video YouTube trước khi lên cuộc gọi.** Xem nội dung dạng dài về bản chất có ý định cao từ người xem, nhưng nó cũng **tạo ra niềm tin điên rồ** vào doanh nghiệp của bạn. Và nó là **công cụ tìm kiếm lớn thứ hai** sau Google."*

Điểm 1 và 2 trùng khớp với [playbook của SuperDemo](../2026-03-11_how-this-250k-month-saas-got-its-first-100-users-ste/case.md) — hai case B2B độc lập cùng dùng free tools và trang so sánh đối thủ.

![Chiến lược SEO](screenshots/07_08m49s_ch-seo-growth-strategy.jpg)

## 6. Lời khuyên cuối

> *"**Thu tiền sớm. Đừng sợ tính tiền**, vì việc tính tiền tạo ra sự cấp bách và cam kết — không chỉ từ bạn mà cả từ khách hàng. **Đi high ticket, nó làm đời bạn dễ hơn.** Bán cho người giàu, họ trả tốt hơn — như Hormozi hay nói."*

![Thu tiền sớm](screenshots/10_12m01s_ch-charge-early-on.jpg)

## 7. Áp dụng cho tôi (indie hacker VN)

**Đây là case tôi nên đọc trước khi xây bất cứ thứ gì:**

- **Landing page giả tốn gần như $0 và một buổi chiều.** Webflow/Framer + một demo dựng bằng AI + Calendly. Không có cách nào rẻ hơn để biết ý tưởng có đáng theo không.
- **Bước 1 ("có một công việc") biến công việc hiện tại của tôi thành tài sản**, không phải trở ngại. Đây là cùng luận điểm với [Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md): ngách tốt nhất nằm trong chính công việc bạn đang làm.
- **Mô hình 38 khách × $263 dễ đạt hơn 800 khách × $15** với người ở VN. Ít khách nghĩa là ít hỗ trợ, ít hạ tầng, ít rủi ro thanh toán vụn.
- **Timo sống ở Bangkok** — bán B2B cho khách phương Tây từ Đông Nam Á. Đây là bằng chứng gần nhất với hoàn cảnh của tôi trong kho.

**Rào cản thật:**

- **Mô hình này đòi BÁN HÀNG QUA CUỘC GỌI bằng tiếng Anh.** Đây là rào cản lớn nhất và không thể né. Toàn bộ deposit framework xoay quanh việc bạn ngồi trên Zoom, thuyết phục một chủ doanh nghiệp Mỹ, và xin thẻ của họ. Nếu tiếng Anh nói của tôi chưa đủ, hãy chọn [mô hình không cần gọi](../2026-02-11_how-i-built-a-12k-month-micro-saas/case.md) trước và quay lại đây sau.
- **"Domain ấm" nghĩa là bạn cần có sẵn một domain cũ đã index.** Nếu chưa có, hãy mua một domain và bắt đầu đăng nội dung ngay bây giờ — nó sẽ là tài sản cho thí nghiệm sau này.
- **Đặt cọc hoàn lại tạo nghĩa vụ pháp lý.** Bạn cầm $500 của một công ty và hứa giao hàng. Với người ở VN, hãy chuẩn bị hạ tầng thanh toán (Stripe qua pháp nhân phù hợp) **trước**, không phải sau.
- **Landing page giả có ranh giới đạo đức.** Họ trung thực về việc sản phẩm chưa tồn tại **trên cuộc gọi**, và cho hoàn tiền 100%. Đó là điều làm nó hợp lệ. **Đừng nhận tiền mà không nói rõ sản phẩm chưa có** — đó là lừa đảo, không phải validate.
- **Họ nộp YC 5 lần và chưa được nhận.** Chi tiết nhỏ nhưng đáng nhớ: đây không phải câu chuyện thành công dễ dàng, và $10K MRR sau hơn một năm là tăng trưởng chậm.

**Khi nào KHÔNG dùng mô hình này:** khi sản phẩm của bạn là B2C giá thấp. Deposit framework cần **giá đủ cao để bõ một cuộc gọi**. Với sản phẩm $10/tháng, chi phí một cuộc gọi bán hàng đã vượt giá trị khách hàng — dùng [pre-sale qua email list](../2025-12-02_how-i-built-it-30k-month-micro-saas-subscribr-breakd/case.md) thay thế.

## Nguồn

- Video: <https://www.youtube.com/watch?v=3eY71OS4MFw> (13:12, đăng 27/09/2025, 57.383 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
