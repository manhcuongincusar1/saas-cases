---
id: g9J_-5w9Nrs
slug: habit-tracker-paid-ads-playbook
product: Habit tracker iOS (founder không tiết lộ tên app)
founder: Frederick James — software developer ở London, 5 năm làm big tech, build app sau một lần "health scare" và chia sẻ hành trình trên X
tagline: App habit tracker "không có gì đặc biệt" lên ~$10K/tháng chỉ nhờ paid ads (Apple Ads rồi TikTok Ads) — cái đáng học là playbook mua traffic, không phải app
revenue_usd_month: 10000
revenue_basis: Founder nói app "peaked at about 13k per month" và "hovering around 10k right now". Dashboard trong video cho MRR khoảng $8.000, doanh thu 30 ngày gần nhất khoảng $11.000, 90 ngày khoảng $25.000, ARR đỉnh "just under 100k". Chọn $10.000 theo lời founder nói; đây là doanh thu gộp trước chi phí ads và phí Apple, không phải lợi nhuận. Tiêu đề "$10K/Month in 88 Days" khớp với lời nói, nhưng mô tả video nói "over $10,000" trong khi MRR thật trên dashboard thấp hơn
model: mobile-app-subscription
category: health & fitness — habit tracker iOS
audience: B2C — người dùng iPhone trả subscription trong app
started: khoảng 3 tháng trước thời điểm quay (~07/2026), build lúc đi nghỉ
time_to_first_sale: không nêu
time_to_scale: 88 ngày tới mức đỉnh ~$13K/tháng; từ $5K lên $10K chỉ trong khoảng 1 tuần sau khi bật TikTok Ads goal-based
team_size: 1 (solo)
funding: bootstrapped
main_channel: paid ads — Apple Ads (search, từ khoá đối thủ) rồi TikTok Ads
tech_stack: [Figma, GPT image, ChatGPT coding agent, Cloudflare R2, Cloudflare D1, Cloudflare Workers, AppsFlyer, RevenueCat, Apple Ads, TikTok Ads]
key_metrics:
  peak_revenue_usd_month: 13000
  mrr_usd: 8000
  revenue_last_30d_usd: 11000
  revenue_last_90d_usd: 25000
  download_to_paid_pct: 7
  refund_rate_pct: 0.7
  tiktok_daily_spend_peak_usd: 1000
  paid_ads_margin_pct: 30
difficulty: 3
video_url: https://www.youtube.com/watch?v=g9J_-5w9Nrs
published: 2026-10-25
views: 50679
tags: [mobile-app, paid-ads, solo-founder, ai-coding, clone-idea, copy-and-improve, ship-fast, subscription, niche-app, build-in-public]
---

# Habit tracker iOS — app "chán" lên $10K/tháng, thắng nhờ playbook mua quảng cáo

> **Tóm tắt 30 giây:** Frederick James, dev ở London, thấy một bài breakdown onboarding của một app habit tracker trên X, nhận ra mình có thể làm bản "design cao cấp hơn + thêm vài tính năng hiển nhiên", rồi build trong kỳ nghỉ. App không được đặt tên trong video (founder và host đều nói app "không có gì đặc biệt"). Doanh thu đỉnh khoảng $13K/tháng, hiện "hovering around 10k" — dashboard cho MRR khoảng $8K, 30 ngày gần nhất khoảng $11K. Phần đáng học là kênh: 0 → ~$5K nhờ Apple Ads (chỉ bid đúng từ khoá tên đối thủ, tắt search match), rồi $5K → ~$10K trong khoảng một tuần nhờ TikTok Ads — remake 5 format video đã viral sẵn, mỗi bài ~$50, sau đó bật goal-based budget với target CPA để TikTok tự đẩy spend từ ~$200 lên ~$1.000/ngày. Chính founder thừa nhận biên lợi nhuận chỉ khoảng 30% và vài tuần đầu không có lãi.

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu đỉnh (founder nói) | **~$13.000/tháng** |
| Mức hiện tại (founder nói) | **~$10.000/tháng** ("hovering around 10k") |
| MRR trên dashboard | **~$8.000** |
| Doanh thu 30 ngày gần nhất | **~$11.000** |
| Doanh thu 90 ngày | **~$25.000** |
| ARR đỉnh | **"just under 100k"** |
| Download → trả tiền | **7%** |
| Tỷ lệ refund | **0,7%** |
| TikTok Ads spend/ngày | từ **~$200** lên **~$1.000** |
| Biên lợi nhuận khi chỉ chạy paid ads | **~30%** (founder ước lượng) |
| Thời gian tới đỉnh | **88 ngày** (theo tiêu đề; founder nói "launched about 3 months ago") |
| Nhân sự | **1 (solo)** |

[01:22](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=82s) là đoạn show dashboard.

**Về độ tin cậy của con số:** "$10K/tháng" là lời nói; thứ nhìn thấy trên màn hình thấp hơn một chút (MRR ~$8K). Đây là doanh thu gộp — chưa trừ ad spend, chưa trừ 15% Apple, chưa trừ VAT. Với biên ~30% (founder tự nói ở [13:13](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=793s)), lãi ròng thực tế chỉ cỡ vài nghìn USD/tháng, và video không đưa số lãi cụ thể. Ngoài ra "peak 13K" gồm cả giai đoạn tăng tốc spend rất mạnh nên chưa chắc bền. Bảng thống kê 30 ngày bị ASR ghi lệch tên nguồn, nên không chắc đó là dashboard của chính app hay trang tổng hợp bên thứ ba.

---

## 2. Sản phẩm giải quyết vấn đề gì

Một app habit tracker trong ngách health & fitness. Founder mô tả: "not really anything special", giá trị cốt lõi là **thiết kế premium, UI thật đẹp** ([02:13](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=133s)). Không có luận điểm "giải quyết nỗi đau mới" — đây là danh mục cực kỳ bão hoà, và chính host cũng nhấn mạnh "there's a million of those".

Điều video cố ý cho thấy: **ngách và sản phẩm gần như không quan trọng bằng khả năng mua traffic có lãi**. Mô tả video nói thẳng "He believes the specific app barely matters… what actually moves the needle is the repeatable marketing playbook". Đây là lập trường của founder, cũng là thứ khiến case vừa hữu ích (cơ chế tái dùng được) vừa cần dè chừng (khó biết có bao nhiêu phần là do chọn đúng category health & fitness, nơi người dùng quen trả subscription).

Video không nêu tên app, không show màn hình app, nên không đánh giá được "premium design" thực chất ra sao.

---

## 3. Ý tưởng đến từ đâu

Không phải scratch-your-own-itch. Founder kể ([03:19](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=199s)): thấy một bài breakdown onboarding của một app trên X (dạng bài khá phổ biến), nhận ra có thể "make it my own angle" và thêm vài tính năng hiển nhiên còn thiếu. Anh chốt: "I knew I could take this app, make the design premium, add a couple of features, and it would likely sell itself."

Bối cảnh cá nhân: 5 năm làm big tech ở London, chán nhịp 9-5, một lần health scare năm ngoái khiến anh "go all in" và build in public trên X. Chọn health & fitness vì đó là ngách mà người dùng sẵn sàng trả tiền cho app — founder chỉ nói gọn "I just thought it would probably make money", không đưa dữ liệu nào.

Đây là mẫu **copy-and-improve** thuần: lấy một app đã có traction, làm bản đẹp hơn. Video không nói app gốc là app nào hay ngoại hình bản sao khác bản gốc bao nhiêu.

---

## 4. Cách validate

Video **không nói** có validate trước khi build hay không (không có landing page test, không phỏng vấn user). Cách "validate" thực chất là dùng bằng chứng gián tiếp — app gốc có người bàn trên X, ngách health & fitness vốn có tiền — rồi để thị trường trả lời bằng ads.

Tín hiệu validation thật nằm ở sau khi launch, và nó là **tín hiệu tài chính từ ads chứ không phải tín hiệu sản phẩm**:
- Tỷ lệ download → trả tiền 7% ("pretty good for the niche that I'm in") và refund 0,7%.
- Apple Ads có spend và chuyển đổi được, nên chạy tiếp.
- Với TikTok: không kỳ vọng có lãi ngay; chấp nhận lỗ để thuật toán học đối tượng (xem mục 5).

Founder còn khuyên: nếu lần đầu chạy paid ads, có thể mất tới ~$1.000 mà chưa thấy lợi nhuận ([12:56](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=776s)).

---

## 5. Go-to-market ⭐ — phần giá trị nhất của case này

Cả case xoay quanh paid ads. Hai giai đoạn, hai nền tảng.

### Giai đoạn 1 — 0 → ~$5K/tháng: Apple Ads ([07:27](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=447s))

Playbook founder liệt kê, theo thứ tự:

1. **Trang App Store phải thật tốt.** Screenshot có thể làm bằng AI, hoặc thuê designer "50, 100 bucks". Đây là creative của chiến dịch search, vì đó là thứ người dùng thấy khi tìm.
2. **Dựng tracking/attribution** — "a few lines of code" trong app và vài click ở RevenueCat.
3. **Tạo campaign**: **tắt search match, chỉ dùng exact keyword, và keyword là tên các đối thủ lớn** (ví dụ khi người ta gõ Duolingo thì quảng cáo app của bạn hiện ra).
4. Bid theo mức Apple đề xuất (recommended max bid), chờ ít nhất ~2 ngày. Nếu không spend, nghĩa là có người bid cao hơn, phải tăng bid.
5. **Mỗi sáng**: export dữ liệu từ RevenueCat và Apple, ghép lại, đưa cho coding agent để tìm keyword/campaign tốt nhất.

Apple Ads cho $100 credit lúc đầu nên rào cản vốn thấp ở giai đoạn này.

### Giai đoạn 2 — $5K → ~$10K/tháng: TikTok Ads, "hockey stick trong khoảng một tuần" ([09:23](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=563s))

- **Creative**: tìm các video đã viral organically trong ngách và remake lại. Chạy **5 format, mỗi format 1 bài, tổng 5 ads**, mỗi bài ~$50 ad spend. (Transcript ghi "I just called in my niche" — nhiều khả năng là ASR của một động từ kiểu "scoured"; ý chắc chắn là lấy video viral làm nguồn.)
- **Chấp nhận lỗ ban đầu để đào tạo account**: "it's more important that your account understands what users it needs to target". Nếu quá lỗ thì dừng ad đó, còn lại giữ chạy.
- **Công thức P&L sơ bộ** ([10:46](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=646s)): lấy realized LTV trừ CPA, trừ 15% Apple (khuyên đăng ký Small Business Program kẻo trả dư — con số chênh phí trong transcript bị ASR ghi lệch), trừ 1% revenue cap (đúng theo lời founder), trừ VAT. Bán trực tiếp cho Mỹ thì không có VAT; subscriber từ EU thì nhiều khả năng mất khoảng 20% (founder nói "likely"). Khuyến nghị: nhắm tới có lãi ngay trên giao dịch đầu tiên.
- **Kỷ luật hằng ngày**: sáng ngày nào cũng đọc báo cáo TikTok Ads. Tăng budget **không quá 20% mỗi vài ngày** — founder nhấn mạnh rất mạnh việc này.
- **Điểm bẻ lái ([11:34](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=694s))**: chuyển sang **goal-based budget increase với target CPA** — nói với TikTok "tôi muốn khách với giá X", rồi TikTok tự điều chỉnh spend. Campaign đang ~$200/ngày bỗng lên ~$1K/ngày, và đó là giai đoạn từ $5K lên ~$10K trong khoảng một tuần.

### Ý kiến của founder về lựa chọn kênh ([13:29](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=809s))

Trả tiền cho marketing bằng thời gian hoặc bằng tiền. Paid ads là "all the way with the money"; influencer/UGC ở giữa (phải quản lý người); founder-led content là đầu kia (tự quay mỗi ngày). Anh cũng cảnh báo **chỉ sống bằng paid ads là không tối ưu**: biên mỏng, khó bán lại app nếu kênh duy nhất là mua user, và rủi ro tập trung — ví dụ TikTok khoá account thì mất cả kênh. Nên kết hợp nhiều kênh về lâu dài.

### Điều video không nói

CPA, ROAS, LTV cụ thể không được nêu bằng số. Không rõ vì sao 5 format cụ thể thắng. Không rõ tỷ trọng subscriber là annual hay weekly — và điều này quyết định MRR thật so với doanh thu cash.

---

## 6. Mô hình kiếm tiền & giá

Subscription trong app, quản lý paywall qua RevenueCat với remote paywall. Video **không nêu mức giá** hay cấu trúc plan (tuần/tháng/năm), cũng không nói app có free tier hay hard paywall. Founder chỉ nói giai đoạn 3 là **A/B test paywall, giá và các tuỳ chọn giá** sau khi app live ([05:46](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=346s)), và khuyên ít nhất thử paywall.

Cấu trúc chi phí biến đổi mà founder nêu: 15% Apple và khuyên đăng ký Small Business Program (đoạn nói về mức phí chênh bị ASR ghi lệch nên không chắc con số), 1% revenue cap, VAT khi bán cho EU, và ad spend. Kết quả: biên khoảng 30% khi chỉ chạy paid ads.

---

## 7. Tech stack & chi phí

| Hạng mục | Công cụ |
|---|---|
| Thiết kế UI mock, wireframe, ảnh App Store | **Figma** (+ GPT image để hoàn thiện) |
| Asset ảnh trong app | Pinterest làm nguồn, chỉnh bằng **GPT image** (founder nói "free với subscription OpenAI") |
| Coding agent | **ChatGPT** (~$100/tháng theo lời founder); thêm gói Claude Pro để thử model mới |
| Backend | **Cloudflare** — R2 (lưu asset, free), D1 (database), Workers (compute) |
| MMP / attribution | **AppsFlyer** (free tới 12.000 installs) |
| Monetization, remote paywall, tracking | **RevenueCat** |
| Font | Mua một font license, **$300 một lần** dùng cho app, website và subtitle video |

Quy trình build founder mô tả ([04:21](https://www.youtube.com/watch?v=g9J_-5w9Nrs&t=261s)): mock UI trong Figma trước (wireframe giúp agent "one shot" tốt hơn), vẽ ERD và sơ đồ hạ tầng, làm sẵn screenshot App Store MVP, rồi đưa toàn bộ mock cho coding agent dựng flow và UI. Phiên bản/tên model (ví dụ "Opus 5.5", "GPT image 2.5") là đúng như lời founder nói trong transcript, chưa kiểm chứng.

Chi phí lớn nhất không nằm ở stack mà ở **ad spend**, và video không cho tổng số tiền đã đốt.

---

## 8. Bài học & trích dẫn

- **Ngách "chán" vẫn kiếm được nếu bạn có kênh mua traffic có lãi.** Nhưng đó là mua traffic bằng vốn, biên ~30%.
- **Tiêu chí kiểm soát rủi ro**: tăng budget tối đa 20% mỗi vài ngày, hoặc chuyển sang target-CPA để nền tảng tự scale; luôn xem báo cáo mỗi sáng.
- **Đừng phụ thuộc một kênh**: chính founder nói rủi ro bị ban account.
- **Build in public là đòn bẩy phân phối của bản thân founder** — host nói đây là cách anh tìm thấy Frederick, và nó là "springboard" cho app kế tiếp.

> **"I knew I could take this app, make the design premium, add a couple of features, and it would likely sell itself."**

> **"In the beginning, it's more important that your account understands what users it needs to target."**

> **"Paid ads take a lot of money upfront. I was not profitable for the first like couple of weeks."**

> **"I think that success really is just failure on a long enough timeline."**

**Góc nhìn tỉnh táo:** đây là kênh phỏng vấn người thành công nên có survivorship bias. App không có tên nên không ai kiểm chứng được. Không biết app bị khoá/hạ spend ra sao sau đỉnh $13K (từ $13K xuống ~$10K, MRR $8K). Và video quảng bá "iOS apps database" của kênh ở giữa và cuối video, nên thông điệp "idea nào cũng làm được" có động cơ thương mại đi kèm.

---

## 9. Áp dụng cho tôi (indie hacker ở VN, bán global)

**Sao chép được gì:**
- Quy trình **Apple Ads exact-match theo tên đối thủ**: tắt search match, bid theo mức đề xuất, mỗi sáng xuất dữ liệu RevenueCat + Apple đưa cho agent phân tích. Vốn khởi đầu thấp nhờ $100 credit.
- Quy trình **TikTok Ads 5 format × ~$50**: lấy video đã viral trong ngách, remake, để dữ liệu chọn winner, rồi chuyển sang target-CPA để nền tảng scale.
- **Công thức P&L trước khi scale** (LTV trừ CPA, trừ 15% Apple, trừ revenue cap, trừ VAT) và kỷ luật không tăng budget quá 20% mỗi vài ngày.
- **Quy trình build bằng AI**: Figma mock → ERD/infra → agent dựng; backend Cloudflare gọn, gần như không tốn tiền ban đầu.
- **Copy-and-improve từ bài breakdown onboarding trên X**: biến một format content đang phổ biến thành nguồn ý tưởng.

**Rào cản thật:**
- **Vốn và chịu lỗ**: founder nói có thể mất khoảng $1.000 chưa thấy lãi, và vài tuần đầu không có lợi nhuận. Nếu không đủ tiền để chịu lỗ, đừng bắt đầu bằng paid ads.
- **Biên mỏng ~30% và phụ thuộc nền tảng**: một lần TikTok khoá account hoặc CPA tăng là hết lãi; founder tự nói không nên sống chỉ bằng paid ads.
- **Cạnh tranh**: habit tracker thuộc loại cực kỳ bão hoà; bid theo tên đối thủ sẽ gặp chính các đối thủ đó bid cao hơn. Video không nói app khác biệt thế nào ngoài "design đẹp".
- **Thanh toán/pháp nhân**: bán subscription iOS đi qua Apple nên Apple lo thu tiền và thuế bán hàng; phần bạn cần lo là nhận payout về tài khoản ngân hàng quốc tế và khai thuế bên mình. Đây là nhận định của người viết, không có trong video.
- **Kỹ năng**: cần biết đọc số liệu CPA/LTV và làm creative video quảng cáo; biết code không đủ.

**Biến thể đáng thử ở thị trường trả cao:**
- **Cùng playbook ads, ngách có ARPU cao hơn habit tracker**: ví dụ app dành cho nhóm có chi tiêu cao (tập luyện cho người tập nghiêm túc, sleep/recovery, quản lý tài chính cá nhân) bán ở Mỹ/UK/Canada/Úc với gói năm ở mức khoảng $30–70 (ước tính của người viết). Lý do có cửa: CPA ở Mỹ cao nhưng LTV cũng cao hơn; founder khuyên bán trực tiếp cho Mỹ vì không dính VAT.
- **Chỉ làm giai đoạn Apple Ads exact-match trước** (vốn nhỏ, $100 credit), dùng keyword tên đối thủ; chỉ lên TikTok khi đã chứng minh CPA dưới LTV. Lý do có cửa: kiểm tra unit economics bằng ngân sách nhỏ trước khi gom vốn lớn.
- **Kết hợp paid + build in public** như host gợi ý: dùng X để xây thương hiệu cá nhân và pipeline ý tưởng, ads để lấy user. Lý do có cửa: giảm rủi ro một kênh.

**Khi nào KHÔNG nên làm:**
- Khi bạn không có vốn chịu lỗ vài trăm tới ~$1.000 và vài tuần chưa có lãi.
- Khi app không có hook gì ngoài "đẹp hơn" và ngách đã có đối thủ spend rất mạnh trên cùng keyword.
- Khi mục tiêu là tài sản bán lại hay lợi nhuận ổn định: founder tự nói app chỉ sống bằng paid ads thì khó bán.
- Khi bạn không thể ngồi xem số liệu ads hằng ngày; mô hình này cần kỷ luật theo dõi mỗi sáng.

---

## Nguồn

- Video: [I Built a $10K/Month App in 88 Days](https://www.youtube.com/watch?v=g9J_-5w9Nrs) — Starter Story, 25/10/2026, 18:45, 50,7K views
- Transcript: [`transcript.md`](transcript.md)
