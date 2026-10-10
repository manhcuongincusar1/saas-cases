---
id: TUN8Y8__QGU
slug: visualizee
product: Visualizee
founder: Piotr (kỹ sư phần mềm 20+ năm kinh nghiệm, Ba Lan, làm full-time song song)
tagline: AI render nhà/nội thất từ ảnh phác thảo trong vài giây — 2 năm dậm chân tại $100/tháng, 1 lần pivot UX + giá lên $9,2K MRR
revenue_usd_month: 9200
revenue_basis: MRR hiện tại theo lời founder ("our current MRR is 9.2"); cộng cả thu một lần thì "gần $10.000/tháng" — đây là con số dùng trong tiêu đề video
model: ai-saas-subscription
category: ai-rendering-tools cho kiến trúc sư / nhà thiết kế nội thất
audience: B2B/B2C — kiến trúc sư và nhà thiết kế nội thất cần render ảnh thật cho khách xem trước
started: ~2023 ("gần 3 năm trước" tính tới 09/2026)
time_to_first_sale: không nêu rõ — nhưng 2 năm đầu chỉ dừng ở ~$100-150/tháng
time_to_scale: 6 tháng sau khi pivot (đầu 2026) → từ $150/tháng lên $9,2K MRR — case về BỀN BỈ, không phải case tăng trưởng nhanh
team_size: 1 (solo, vẫn đi làm full-time technical lead song song)
funding: bootstrapped
main_channel: không phải trọng tâm video — sản phẩm tăng trưởng chủ yếu nhờ SEO (có dùng Ahrefs theo dõi) và cải thiện conversion trên landing page có sẵn, KHÔNG nêu chi tiết kênh acquisition
tech_stack: [Cursor, Claude Code, Fal AI, Ahrefs, MailerLite, Supabase, Vercel, Stripe, Next.js, PostHog, Google Analytics, Sentry]
key_metrics:
  mrr_usd: 9200
  active_customers: ~300
  daily_visitors: 300+
  daily_trials: 5-10
  trial_to_paid_pct: 25
replicability_vn: 3
difficulty: 3
video_url: https://www.youtube.com/watch?v=TUN8Y8__QGU
published: 2026-09-02
views: 54729
tags: [ai-tools, saas, product-pivot, ux-simplification, subscription-vs-one-time, persistence, solo-founder, side-project, architecture-tech]
---

# Visualizee — 2 năm dậm chân ở $100/tháng, rồi một lần đơn giản hoá UX đưa lên $9,2K MRR

> **Tóm tắt 30 giây:** Piotr là kỹ sư phần mềm 20 năm kinh nghiệm ở Ba Lan, làm full-time song song build side project. Visualizee — công cụ AI biến ảnh phác thảo nhà/nội thất thành ảnh render thật trong vài giây — ra mắt gần 3 năm trước nhưng **giậm chân tại ~$100-150/tháng suốt 2 năm**. 6 tháng trước khi lên sóng, anh làm ĐÚNG HAI thay đổi: (1) **bỏ hệ thống node phức tạp kiểu ComfyUI, thay bằng chatbot 1 bước** — upload ảnh, mô tả, nhận kết quả — và (2) **chuyển từ thu tiền một lần sang subscription hàng tháng ngay từ đầu phễu**. Kết quả: MRR hiện tại $9,2K, ~300 khách trả phí, 25% trial → paid. Bài học founder tự rút ra: "tôi đổ lỗi cho marketing suốt 2 năm, trong khi vấn đề thật là sản phẩm quá khó dùng."

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR hiện tại | **$9.200/tháng** |
| Cộng thu một lần | gần **$10.000/tháng** (số dùng ở tiêu đề video) |
| 2 năm đầu | chỉ **$100–150/tháng** |
| Thời gian pivot → hiệu quả rõ rệt | **6 tháng** |
| Khách trả phí | **~300** |
| Khách ghé landing page/ngày | **300+** |
| Trial mới/ngày | **5–10** |
| Tỷ lệ trial → paid | **25%** |
| Thời gian xây | ~**3 năm** tổng, founder solo, làm ngoài giờ |

**Dòng thời gian:**

```
~2023      Ý tưởng nảy ra khi AI tạo ảnh vừa bắt đầu nổi
+5 tháng   Build V1 — hệ thống node kiểu ComfyUI (ngoài giờ làm)
2023-2025  Launch, dậm chân ở $100-150/tháng suốt ~2 năm
~03/2026   PIVOT: gộp node phức tạp thành 1 chatbot ("Vizy") + đổi one-time -> subscription
09/2026    MRR $9,2K, ~300 khách, lên sóng Starter Story
```

---

## 2. Sản phẩm giải quyết vấn đề gì

Kiến trúc sư/nhà thiết kế nội thất cần **cho khách xem trước** nhà/phòng sẽ trông ra sao — vẽ render ảnh thật truyền thống tốn nhiều thời gian. Visualizee: upload ảnh phác thảo hoặc model → AI trả về ảnh (hoặc video) render thật trong vài giây, đổi được vật liệu/màu sắc/phong cách theo yêu cầu.

**Điểm mấu chốt không phải công nghệ AI** (ai cũng có thể gọi Fal AI) mà là **lớp trung gian giúp người không biết prompt engineering vẫn ra được kết quả đúng ý** — chatbot "Vizy" hỏi lại người dùng để hiểu rõ họ muốn gì rồi mới tự soạn prompt.

---

## 3. Ý tưởng đến từ đâu

Không phải nỗi đau cá nhân — Piotr **thấy tiềm năng công nghệ** (AI tạo ảnh mới nổi ~2023) và chủ động đi tìm một ngách cụ thể để áp dụng, thay vì làm "đồ chơi AI chung chung". Anh chọn kiến trúc/nội thất — một ngách có nhu cầu rõ ràng và lặp lại (mọi dự án đều cần bản render để trình khách).

> Khác hẳn phần lớn case trong kho: đây là **idea xuất phát từ công nghệ đi tìm vấn đề** (technology-first), không phải vấn đề đi tìm giải pháp. Founder tự nhận ra rủi ro này ngay từ đầu ("tôi không muốn tạo ra một món đồ chơi AI điển hình khác") nhưng phải mất 2 năm mới thực sự né được nó.

---

## 4. Cách validate — hay đúng hơn là BÀI HỌC VỀ KHÔNG VALIDATE ⭐

Đây là giá trị lớn nhất của case này: **founder không hề pivot ý tưởng, không đổi khách hàng mục tiêu — chỉ đổi CÁCH TRÌNH BÀY sản phẩm**, và nó lật ngược cả doanh nghiệp.

**2 năm sai lầm:** đổ lỗi tăng trưởng chậm cho marketing. Thực ra vấn đề nằm ở **ma sát sản phẩm** — hệ thống node phức tạp (kiểu ComfyUI) đòi hỏi người dùng tự nối các bước, tự viết prompt. Với kiến trúc sư/nhà thiết kế (không phải dân kỹ thuật), đây là rào cản chết người.

**Tín hiệu founder cuối cùng cũng nhìn ra:** nhận phản hồi trực tiếp *"cái này khó quá với chúng tôi"* — và thay vì tiếp tục thêm tính năng, anh **rút gọn** xuống một luồng duy nhất.

**Bài học nói thẳng trên video:**
> "Friction trong sản phẩm giết chết conversion. Suốt 2 năm tôi đổ lỗi cho marketing, nhưng vấn đề thật là sản phẩm quá khó dùng. Giải pháp là **xoá bỏ rào cản giữa người ghé thăm và thành công đầu tiên của họ**."

---

## 5. Go-to-market

Video **không đào sâu kênh tăng trưởng** cụ thể (không nói rõ chạy ads hay không, không có con số CAC). Có dùng Ahrefs (theo dõi SEO) và PostHog (theo dõi hành vi/thử nghiệm) — gợi ý tăng trưởng chủ yếu tới từ **organic/SEO + cải thiện landing page có sẵn**, không phải một chiến dịch distribution mới. Điểm mấu chốt tăng trưởng ở case này nằm ở **sản phẩm + giá**, không nằm ở kênh mới.

---

## 6. Mô hình kiếm tiền & giá ⭐

Bài học thứ hai, ngang giá trị với việc đơn giản hoá UX:

> **"Charge a subscription fee from day one. Subscriptions are what drives growth. Đừng sợ rằng sẽ không ai trả tiền — nếu sản phẩm sống được, họ sẽ trả."**

Trước pivot: thu tiền một lần (one-time payment) → **không tạo ra doanh thu định kỳ**, mỗi tháng lại về vạch xuất phát. Sau khi chuyển hẳn sang subscription hàng tháng (kèm 7 ngày dùng thử miễn phí), doanh thu mới thực sự **cộng dồn** thay vì reset liên tục.

Giá theo transcript (lưu ý: auto-caption có thể sai số cụ thể): sau 7 ngày trial, các gói trả phí theo tháng tuỳ mức độ sử dụng.

---

## 7. Tech stack & chi phí

| Hạng mục | Công cụ |
|---|---|
| Viết code | **Cursor**, gần đây chuyển sang **Claude Code** |
| Sinh ảnh/video AI | **Fal AI** (GPU-as-a-service) |
| SEO | **Ahrefs** |
| Email | **MailerLite** |
| Database / Auth / Storage | **Supabase** |
| Hosting | **Vercel** |
| Thanh toán | **Stripe** |
| Framework | **Next.js** |
| Product analytics | **PostHog** |
| Web analytics | **Google Analytics** |
| Theo dõi lỗi | **Sentry** |

Stack solo-founder điển hình 2026: managed toàn bộ, không server tự quản, một người vừa code vừa vận hành $9K MRR song song với công việc full-time.

---

## 8. Bài học & trích dẫn

**Về việc không bỏ cuộc:**
> "Đây là sản phẩm đầu tiên tôi ra mắt. Xoá nó khỏi Internet là điều rất khó với tôi." — lý do thật khiến anh không dừng lại, không phải chiến lược tính toán.

**Tín hiệu giữ niềm tin khi chưa có kết quả:** nhìn đối thủ trong ngách vẫn sống khỏe — "*họ thành công, vậy chắc chắn mô hình này hoạt động được, vấn đề là tôi làm sai chỗ nào.*"

**Lời khuyên cho bản thân trẻ hơn:**
> "Đừng cố xây sản phẩm mạnh nhất có thể — hãy xây sản phẩm ĐƠN GIẢN NHẤT mà khách hàng cần. Bỏ qua hệ thống node phức tạp, ra bản đơn giản có subscription ngay, và lắng nghe phản hồi người dùng."

**Góc nhìn host (Pat & Gus):** điều khiến case này khác biệt không phải kỹ thuật hay AI — mà là **đam mê với đúng vấn đề đủ lâu để không bỏ cuộc trước khi tìm ra bản pivot đúng**. "Willpower" thuần tuý khó bền; động lực đến từ việc thật sự quan tâm tới bài toán của khách hàng (kiến trúc sư/nhà thiết kế).

---

## 9. Áp dụng cho tôi (indie hacker VN)

**Sao chép được ngay:**
- ✅ Nếu sản phẩm có **quy trình nhiều bước / nhiều tham số**, thử hỏi: có thể gộp thành **một luồng chat đơn giản** (kiểu ChatGPT) không? Càng ít bước tới "thành công đầu tiên", conversion càng cao.
- ✅ **Subscription từ ngày đầu tiên**, không thu one-time — kể cả khi sợ chưa ai chịu trả định kỳ. Số liệu case này chứng minh: chuyển đổi mô hình giá quan trọng ngang chuyển đổi sản phẩm.
- ✅ Trước khi đổ lỗi cho marketing khi tăng trưởng chậm, tự hỏi: **có phải sản phẩm quá khó dùng?** Xem lại funnel: bao nhiêu % người vào landing page thực sự chạm được "thành công đầu tiên"?
- ✅ Nếu ý tưởng bắt đầu từ công nghệ (AI mới, tool mới) thay vì từ nỗi đau — hãy ép mình chọn **MỘT ngách cụ thể** ngay từ đầu, đừng làm "công cụ chung chung".

**Cơ hội cho thị trường VN:**
- Kiến trúc sư/thiết kế nội thất VN cũng cần trình bày phối cảnh cho khách nhanh, rẻ — ngách này có nhu cầu tương tự, ít người khai thác bằng AI ở VN.
- Mô hình "chatbot AI hộ trợ prompt cho dân không rành AI" áp dụng được cho rất nhiều ngách chuyên môn khác (thiết kế đồ hoạ, marketing content, luật...).

**Rào cản:**
- ⚠️ Chi phí GPU AI (Fal AI hoặc tương đương) tính theo lượt render — cần kiểm tra đơn vị kinh tế kỹ trước khi định giá subscription ở VN, nơi mức chi trả trung bình thấp hơn Mỹ.
- ⚠️ 2 năm gần như không doanh thu là cái giá thật — không phải ai cũng đủ nguồn lực (thời gian + tài chính) để trụ được lâu như vậy trong lúc vẫn đi làm full-time.

**Điều dễ hiểu sai:** Bài học ở đây KHÔNG phải "cứ kiên trì rồi sẽ thắng". Piotr trụ được 2 năm nhưng **kết quả chỉ tới sau khi anh thực sự thay đổi thứ gì đó** (UX + mô hình giá) — kiên trì mà không thay đổi cách làm chỉ là 2 năm dậm chân kéo dài thêm. Bài học đúng là: **giữ đủ lâu với đúng vấn đề để có cơ hội tìm ra thay đổi đúng, nhưng phải chủ động đi tìm thay đổi đó, không chỉ chờ đợi.**

---

## Nguồn

- Video: [I was stuck at $100 for 2 years until I made one change. Now my app makes $10K/month](https://www.youtube.com/watch?v=TUN8Y8__QGU) — Starter Story, 02/09/2026, 13:34, 55K views
- Transcript: [`transcript.md`](transcript.md) — lưu ý: transcript auto-caption của video này có một số đoạn dịch/nhận diện lỗi (VD "Steeply", "Busy", "4AI") do giọng nói không phải người bản ngữ; các con số quan trọng đã được đối chiếu với phần mô tả video gốc.
