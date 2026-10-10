---
id: T5zMsTw8GWQ
slug: momego-hyperlocal-aso
product: Momego
founder: John McEvoy
tagline: App bắt xe buýt phủ 160+ thành phố — 5,2 triệu lượt tải với $0 quảng cáo, nhờ nhét đúng tiếng lóng giao thông của từng thành phố vào metadata App Store
revenue_usd_month: 30000
revenue_basis: founder tự nêu ~$30.000 MRR, gần như toàn bộ từ subscription; không có ảnh dashboard trong video nên đây là con số tự khai
model: mobile-app-subscription
category: transit-navigation
audience: B2C — người đi xe buýt/tàu điện ở các đô thị Âu Mỹ
started: 2017 (app lên store)
time_to_first_sale: không nêu; 2 năm đầu kiếm tiền bằng banner ads chứ chưa bán subscription
time_to_scale: ~8 năm từ 2017 tới $30K/tháng; bước nhảy $8K → $30K diễn ra trong 2021 sau khi A/B test paywall
team_size: 1
funding: bootstrapped
main_channel: App Store Optimization (ASO) siêu địa phương, $0 ads
tech_stack: [Laravel, PHP, Flutter, Xamarin, Adobe Creative Suite, Lottie, After Effects, Appfigures, RevenueCat, Mixpanel, Cloudflare, ChatGPT]
opex_usd_month: 3610
key_metrics:
  downloads: 5,2 triệu (từ 2017)
  mau: 400.000
  ratings: ~75.000
  cities: hơn 160
  paywall_conversion: 0,5% → 8% sau ~10 thí nghiệm trong 2-3 tháng
  ad_revenue_peak: ~8.000 USD/tháng trước khi COVID xoá sạch
  servers: ~20 dedicated server, ~2.500 USD/tháng
  map_api_cost: ~1.000 USD/tháng
replicability_vn: 4
difficulty: 3
video_url: https://www.youtube.com/watch?v=T5zMsTw8GWQ
published: 2025-10-23
views: 86209
tags: [mobile-app, aso, app-store-search, localization, keyword-first, paywall-optimization, ab-testing, reverse-trial, revenuecat, mixpanel, solo-founder, bootstrapped, pull-channel, pandemic-pivot]
---

# Momego — $30K/tháng từ app bắt xe buýt, 5,2 triệu lượt tải, $0 quảng cáo

> **Tóm tắt 30 giây:** John McEvoy là dân thiết kế đồ hoạ ở Scotland, tự học code vì muốn uống hết ly cà phê sáng thay vì đứng chờ xe buýt 20 phút dưới mưa. App **Momego** của anh giờ phủ **hơn 160 thành phố**, **5,2 triệu lượt tải**, **400.000 người dùng/tháng**, **$30K MRR** — một mình làm, **$0 tiền quảng cáo**. Toàn bộ tăng trưởng đến từ một việc buồn tẻ: tìm ra người New York gọi tàu điện là **MTA subway** còn người Chicago gọi là **CTA L train**, rồi nhét đúng từ đó vào title và keyword. Nhưng cú nhảy tiền thật lại đến từ chỗ khác: **A/B test paywall đưa tỉ lệ chuyển đổi từ 0,5% lên 8%**.

![$30.000/tháng](screenshots/01_00m36s_usd-30-000.jpg)

---

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$30.000 MRR, gần như toàn bộ là subscription |
| Lượt tải | 5,2 triệu (từ 2017) |
| Người dùng hoạt động | 400.000/tháng |
| Đánh giá | ~75.000 |
| Thành phố phủ sóng | hơn 160 |
| Đội ngũ | 1 người |
| Chi quảng cáo | **$0** |
| Chi phí vận hành | ~$3.610/tháng (server $2.500 + API bản đồ $1.000 + Cloudflare $90 + ChatGPT $20) |
| Tỉ lệ chuyển đổi paywall | 0,5% → **8%** |

**Lưu ý về số liệu:** video **không có ảnh chụp dashboard doanh thu** — con số $30K là founder tự khai. Ngoài ra $3.610 chi phí hạ tầng chưa tính **hoa hồng 15-30% của Apple/Google** vốn bị trừ thẳng trước khi tiền về. Margin thực tế thấp hơn con số 88% mà phép trừ đơn giản gợi ra.

![Số liệu Momego](screenshots/02_01m19s_ch-numbers-behind-momego.jpg)

**Cảnh báo tên riêng:** phụ đề tự động đọc tên app thành *Mumigo* và tên founder thành *John Makavoy*. Tên đúng theo mô tả video là **Momego** / **John McEvoy**. Mô tả video cũng dẫn link `travelwhiz.app` chứ không phải momego — nhiều khả năng app đã đổi thương hiệu hoặc đây là sản phẩm thứ hai của anh; video không giải thích, tôi ghi lại để bạn tự kiểm tra.

---

## 2. Nguồn gốc ý tưởng: Uber cho tôi xem taxi trên bản đồ, sao xe buýt thì không? ⭐⭐

John lúc đó **đang làm cho một hãng xe buýt ở Edinburgh**. Uber vừa ra mắt.

> *"Được nhìn thấy chiếc taxi bò trên bản đồ tiến về phía mình là một cảm giác thật đã. Và tôi muốn có đúng trải nghiệm đó khi chờ xe buýt. Tôi muốn một thứ cho phép mình uống nốt ly cà phê buổi sáng thay vì đứng ở trạm xe buýt 10-20 phút dưới mưa."*

Cơ chế đáng học ở đây không phải "giải vấn đề của chính mình" (ai cũng nói câu đó) mà là **chuyển giao trải nghiệm giữa hai ngành**: một trải nghiệm đã được chứng minh ở ngành A (Uber, gọi xe) được bê nguyên sang ngành B (giao thông công cộng) nơi chưa ai làm. Bạn không cần phát minh cảm giác mới — bạn chỉ cần tìm ngành chưa có nó.

Và John có một lợi thế mà anh không nhấn mạnh nhưng rất quan trọng: **anh làm việc trong ngành xe buýt**. Anh biết dữ liệu ở đâu, ai kiểm soát nó, nó tệ đến mức nào.

![Ý tưởng Momego](screenshots/03_02m13s_ch-idea-for-momego.jpg)

---

## 3. Playbook ASO siêu địa phương — 3 bước ⭐⭐⭐

Đây là phần giá trị nhất của video và là thứ ít người trong kho này làm được ở mức chuyên sâu như vậy.

### Bước 1 — Từ khoá theo địa danh, và phải là từ dân bản địa thật sự dùng

Bắt đầu đơn giản: nhét từ khoá gắn địa danh (`New York subway`, `Chicago train`) vào **title, subtitle và keyword list**. App bắt đầu xuất hiện trong tìm kiếm.

Nhưng tăng trưởng chỉ thật sự nổ khi anh làm nghiên cứu sâu hơn một tầng:

> *"Mỗi thành phố dùng thuật ngữ khác nhau. Ví dụ ở New York người ta nói **MTA subway**. Ở Chicago là **CTA L train**. Khi tôi bắt đầu thêm loại từ khoá này, lượt tải tăng lên đáng kể."*

**Cơ chế:** người dùng không gõ từ chung chung (`bus app`) — họ gõ **đúng tên mà cộng đồng họ dùng**. Từ chung chung thì cạnh tranh khủng khiếp; tiếng lóng địa phương thì gần như trống. Một app phủ 160 thành phố có nghĩa là **160 từ khoá long-tail riêng biệt**, mỗi cái dễ chiếm top, cộng lại thành 5,2 triệu lượt tải.

Song song, anh **thay ảnh chụp màn hình theo từng địa phương** — mỗi localization có bộ screenshot riêng, để người mở trang app ở Chicago thấy ngay tàu Chicago. Đây là phần nhiều người bỏ qua: ASO không chỉ là được hiển thị, mà là **được click sau khi hiển thị**.

### Bước 2 — Mẹo localization ăn ké chỉ số ⭐⭐⭐

Đây là chi tiết kỹ thuật đáng giá nhất video, và nó gần như là một lỗ hổng trong cách Apple xếp hạng:

> *"Nếu bạn thêm keyword vào phần localization **Mexican Spanish**, chính những từ khoá đó sẽ được index cho App Store Mỹ và **có trọng số ngang với localization tiếng Anh Mỹ bản địa**."*

Nói cách khác: App Store Mỹ index nhiều localization cùng lúc. Một app chỉ có một trường keyword 100 ký tự cho tiếng Anh Mỹ — nhưng nếu bạn mở thêm các localization được index chung vào cùng storefront, bạn **nhân đôi, nhân ba số ký tự keyword** mà mình sở hữu. Với một app phủ 160 thành phố, đây chính là thứ cho phép nhồi hết `MTA`, `CTA`, `BART`, `TfL`... mà không phải chọn.

⚠️ **Đây là mẹo nền tảng, không phải quy luật vật lý.** Apple đã đổi cách index localization nhiều lần. Trước khi xây chiến lược lên nó, hãy tự test lại trên chính app của bạn.

### Bước 3 — Tìm thêm từ khoá bằng chính thanh tìm kiếm App Store

Hai lựa chọn:
- **Apple Search Ads** — chạy thử vài keyword một lúc để xem cái nào chuyển đổi (tốn tiền nhưng cho dữ liệu thật).
- **Miễn phí:** gõ vài ký tự đầu vào ô tìm kiếm App Store, đọc danh sách gợi ý.

> *"Hầu hết mọi người khi bắt đầu gõ sẽ thấy danh sách hiện ra và bấm vào **mục thứ nhất hoặc thứ hai**. Nhìn vào các danh sách đó, tôi xác định được đâu là từ khoá có tác động lớn nhất mà người ta đang tìm."*

Và điểm mấu chốt:

> *"Điều tuyệt nhất là vì chúng rất cụ thể nên chúng **không có độ phổ biến lớn**. Nhắm đúng những từ khoá đó, đúng chỗ, đúng lúc, bạn có thể lọt top 5 khá dễ dàng."*

Đây là **cùng một logic với YouTube Search của [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md)**: chọn theo *ý định*, không chọn theo *lượng tìm*. Từ khoá ít người tìm nhưng đúng người thì thắng cả từ khoá triệu view.

### Bước 4 (được gọi là "bước ba" trong video) — Xin đánh giá vào đúng khoảnh khắc vàng

Vào top 10 rồi, muốn lên số 1 thì cần **ratings chảy vào liên tục**.

> *"Bạn cần có những **khoảnh khắc vàng** để xin đánh giá. Ở đây có thể là lúc người dùng chạm vào một trạm và thấy xe buýt hoặc tàu đang chạy trực tiếp trên bản đồ. Bạn thật sự nhìn thấy nó di chuyển. Đó là khoảnh khắc tuyệt vời để xin đánh giá — lúc khách hàng có nhiều khả năng phản hồi tích cực nhất."*

**Cơ chế:** đừng xin rating theo lịch (sau 3 lần mở app). Hãy xin **ngay sau khi sản phẩm vừa làm người dùng ngạc nhiên**. Với Momego đó là giây phút cục xe buýt nhúc nhích trên bản đồ. Với app của bạn, hãy đi tìm cái giây đó và gắn prompt vào đúng đó.

75.000 đánh giá là kết quả của việc này — và ratings lại đẩy ranking, đẩy tải, đẩy ratings. Vòng lặp tự nuôi.

![Cách lấy hàng triệu người dùng miễn phí](screenshots/06_04m54s_ch-how-to-get-millions-of-users-for-free.jpg)

---

## 4. Cú nhảy tiền thật KHÔNG đến từ ASO ⭐⭐⭐

Đây là điểm dễ bị đọc sai nhất của case. Tiêu đề video nói về ASO. Nhưng đọc kỹ dòng thời gian:

| Giai đoạn | Việc xảy ra | Doanh thu |
|---|---|---|
| 2017-2019 | Lượt tải tăng đều nhờ ASO, kiếm tiền bằng **banner ads** | ~$8.000/tháng |
| 2020 (COVID) | Không ai đi xe buýt → **doanh thu quảng cáo biến mất** | sụp |
| 08/2020 | Xây lại app quanh **subscription**, thêm tính năng premium, đẩy gói năm | phục hồi dần trong ~1 năm |
| 2021 | **A/B test paywall** — ~10 thí nghiệm trong 2-3 tháng | $8K → **$30K+** |

> *"Chỉ bằng cách tối ưu onboarding và paywall, tôi tăng tỉ lệ chuyển đổi từ **0,5% lên tận 8%**. Và đột nhiên tăng trưởng bùng nổ, từ khoảng 8K/tháng lên hơn 30.000 đô."*

**Rút ra:** ASO mang **lưu lượng**. Paywall biến lưu lượng thành **tiền**. John đã có 5 triệu lượt tải trước khi kiếm được $30K — nghĩa là suốt nhiều năm anh **đã ngồi trên toàn bộ lưu lượng cần thiết mà chỉ thu về $8K** vì phần chuyển đổi chưa được động tới.

Nếu bạn đang có app với lượng tải kha khá mà doanh thu bèo, **vấn đề của bạn gần như chắc chắn không phải marketing**.

⚠️ **Ghi rõ một chỗ chưa khớp:** conversion tăng 16 lần (0,5% → 8%) nhưng doanh thu chỉ tăng ~3,75 lần ($8K → $30K). Hai con số này không phải cùng một cơ số — $8K là **doanh thu quảng cáo thời trước COVID**, còn $30K là **doanh thu subscription sau này**. Video không tách bạch, nên đừng dùng phép nhân 16x để dự phóng cho app của bạn.

![$8.000/tháng thời banner ads](screenshots/07_08m43s_usd-8-000.jpg)

---

## 5. Giải phẫu paywall thắng cuộc ⭐⭐⭐

John demo trực tiếp. Đây là bản thiết kế đáng chép lại:

**1. Onboarding cực ngắn — và có lý do rất cụ thể:**

> *"Hầu hết người tải và cài app đều đang làm việc đó **ở trạm xe buýt hoặc nhà ga**. Nên không có thời gian cho onboarding 20 màn hình."*

Đây là điểm phân định quan trọng với [Prayer Lock](../2026-01-18_i-built-a-20k-month-mobile-app-heres-my-entire-playb/case.md), nơi onboarding **dài 12 câu hỏi** lại là thứ làm tăng chuyển đổi.

| Chọn onboarding dài | Chọn onboarding ngắn |
|---|---|
| Người dùng đang ở nhà, rảnh, đang tìm hiểu bản thân (app tâm linh, sức khoẻ, thói quen) | Người dùng đang **đứng giữa đường và cần câu trả lời ngay** (giao thông, tra cứu, tiện ích) |
| Mỗi câu trả lời là một **cam kết nhỏ** làm họ khó bỏ đi ở paywall | Mỗi màn hình thừa là một cơ hội để họ **đóng app và bỏ lỡ chuyến xe** |

**Quy tắc phân định: bối cảnh vật lý lúc cài app quyết định độ dài onboarding.** Không có câu trả lời chung.

**2. Chuỗi màn hình của Momego:**
- Xin **quyền vị trí ngay** (permission quan trọng nhất, xin sớm khi ý định còn cao)
- Vài màn hình giới thiệu giá trị — không chỉ bắt xe buýt mà cả các tính năng thêm → *"chuẩn bị tinh thần cho paywall sắp tới"*
- **Social proof:** dòng chữ *"join millions, saving time"*
- **Paywall 3 lựa chọn:** dùng thử 7 ngày cho gói năm / gói tuần (cam kết thấp) / **gói lifetime cho người ghét subscription**

**3. Cú unlock lớn nhất — reverse trial ⭐⭐⭐**

> *"Sau rất nhiều thí nghiệm, thứ tôi thấy là một unlock thật sự nằm ở **những người bấm nút đóng**. App khởi động một reverse trial. Nếu tôi đóng ngay bây giờ, nó nói **enjoy a week of pro on us**. Và giờ bạn có 7 ngày dùng thử toàn bộ tính năng Pro, bắt đầu mà không cần trả tiền, không cần cam kết gì cả."*

**Cơ chế vì sao nó ăn tiền:** paywall truyền thống coi nút X là điểm kết thúc. Reverse trial coi nó là **điểm bắt đầu của một cuộc thương lượng thứ hai**. Người vừa từ chối trả tiền vẫn có thể đồng ý *nhận miễn phí* — và sau 7 ngày dùng bản Pro trong đời thật (nhận thông báo tàu trễ, được gợi ý tuyến thay thế), họ đã có **chi phí chuyển đổi tâm lý** để mà trả tiền. Bạn đổi 0% (họ đã đóng paywall) lấy một xác suất khác 0.

Điều kiện để reverse trial ăn: **giá trị sản phẩm phải cảm nhận được trong đúng cửa sổ dùng thử**. Momego đạt điều đó vì người ta bắt xe buýt mỗi ngày. Một app dùng mỗi tháng một lần thì 7 ngày là vô nghĩa.

![Paywall và reverse trial](screenshots/09_10m45s_replay.jpg)

---

## 6. Sản phẩm thật ra làm gì

Ba tầng, tăng dần độ khó sao chép:

1. **Bản đồ + trạm.** Chạm vào một trạm, xem giờ khởi hành. Chỗ này ai cũng làm được.
2. **Khoảnh khắc kỳ diệu.** Chạm vào một chuyến → **thấy chiếc xe buýt đang di chuyển trên bản đồ**. Đây là điểm bán hàng và cũng là nơi xin đánh giá.
3. **Trip Assist (hào bảo vệ thật sự).** Bấm "go" → server chạy **machine learning theo dõi chặng đường phía trước**. Nếu có tàu/xe trễ hoặc bạn sắp lỡ chuyến nối, server biết trước, gửi thông báo và **đề xuất tuyến thay thế**.

> *"Đó mới là điều kỳ diệu thật sự của app."*

Tầng 3 là lý do app này không bị một người vibe-code trong cuối tuần đè bẹp: nó cần **dữ liệu thời gian thực của 160 thành phố, 20 dedicated server, và mô hình dự báo**. Chi phí hạ tầng $3.500/tháng vừa là gánh nặng vừa là **rào cản gia nhập**.

---

## 7. Tech stack và chi phí

| Hạng mục | Công cụ | Chi phí |
|---|---|---|
| Backend | **Laravel / PHP** — *"tôi chọn đồ cũ và chán"* | — |
| App (bản đầu, 2017) | **Xamarin** với C#/.NET (thứ anh quen từ web) | — |
| App (bản viết lại) | **Flutter** — hợp với bản đồ và sliding panel, viết lại trong 2-3 tháng | — |
| Đồ hoạ / UI | Adobe Creative Suite | — |
| Animation | After Effects → xuất ra **Lottie** để nhúng vào app | — |
| Nghiên cứu ASO | **Appfigures** | — |
| Quản lý subscription | **RevenueCat** | — |
| Analytics theo sự kiện | **Mixpanel** — *"unlock lớn nhất với tôi"* | — |
| Load balancer địa lý | Cloudflare | ~$90/tháng |
| AI | ChatGPT — *"dùng cho gần như mọi thứ"* | ~$20/tháng |
| **Server** | ~20 dedicated server | **~$2.500/tháng** |
| **API bên thứ ba** | chủ yếu bản đồ | **~$1.000/tháng** |

⚠️ Transcript chỗ này lộn xộn: nó nói *"viết lại app bằng native Swift trên iOS"* rồi ngay câu sau lại nói *"vì cách app hoạt động với bản đồ và sliding panel nên Flutter hoàn hảo"*. Đọc kỹ ngữ cảnh, tôi hiểu là **anh cân nhắc Swift rồi chọn Flutter** — nhưng đây là chỗ phụ đề tự động không đáng tin, đừng dùng làm căn cứ chọn stack.

![$90 Cloudflare](screenshots/10_12m23s_usd-90.jpg)

---

## 8. Lời khuyên cuối — hai điều

**1. Giải vấn đề của chính mình, nhưng vì một lý do rất cụ thể:**

> *"Bạn cần giải một vấn đề mà bạn có, vì khi bạn làm việc đêm và cuối tuần, bạn **liên tục đâm vào tường**. Bạn cần một thứ giữ cho mình đi tiếp. Giải vấn đề của chính mình có lẽ là cách tốt nhất để vượt qua mỗi lần bị chặn."*

Chú ý anh không nói "vì bạn hiểu khách hàng". Anh nói vì **động lực**. Đây là lập luận về **sức bền**, không phải về nghiên cứu thị trường — và với một dự án kéo dài 8 năm thì đó mới là biến số quyết định.

**2. Bỏ vanity metrics, chuyển sang analytics theo sự kiện:**

> *"Trong hai năm đầu, tôi dựa vào các **vanity metrics** như monthly active users. Thứ đó không thật sự tạo ra khác biệt. Chỉ khi tôi chuyển sang analytics theo sự kiện thì tăng trưởng mới thật sự xảy ra."*

Cụ thể: MAU không cho bạn biết **phải sửa gì**. Event analytics + A/B test paywall thì có. Đây chính là cây cầu dẫn tới cú nhảy 0,5% → 8% ở mục 4.

![Điều đưa Momego lên $30K](screenshots/05_04m19s_ch-what-grew-momego-to-30k-month.jpg)

---

## 9. Cảnh báo thiên kiến nguồn

- Video có **hai đoạn quảng cáo lộ liễu**: doola (dịch vụ lập LLC, có mã giảm giá) và **Starter Story Build** (khoá học của chính kênh). Đoạn Pat Walls nói *"ngày nay bạn có thể làm tất cả những thứ đó bằng AI trong ba ngày"* — nói về một app cần 20 server và ML dự báo trễ chuyến — là **lời bán khoá học, không phải nhận định kỹ thuật**.
- Không có ảnh dashboard doanh thu. Mọi con số tài chính đều là tự khai.
- Case này mất **8 năm**. Kênh trình bày nó cạnh những case 83 ngày. Đừng để cách đóng gói làm bạn nhầm về thời gian thực tế.

---

## 10. Áp dụng cho tôi (indie hacker VN)

### Sao chép được gì

- ✅ **Chiến lược "một app, N từ khoá địa phương".** Đây là cấu trúc quan trọng nhất: chọn một bài toán mà **mỗi địa phương có một tên gọi riêng**, rồi biến mỗi địa phương thành một cửa vào tìm kiếm. Không chỉ giao thông — bãi đỗ xe, lịch cúp điện, giá chợ, lịch thi, thủ tục hành chính từng tỉnh, tra cứu phạt nguội... đều có tính chất này.
- ✅ **Nghiên cứu tiếng lóng bản địa trước khi viết title.** Người Hà Nội và người Sài Gòn gọi cùng một thứ bằng hai từ khác nhau. Đó là hai từ khoá, không phải một.
- ✅ **Gợi ý tự động của App Store là công cụ research miễn phí.** Gõ 2-3 ký tự, đọc danh sách. Không cần trả tiền cho tool nào để bắt đầu.
- ✅ **Bộ screenshot riêng cho từng localization.** Rẻ, ít người làm, ảnh hưởng trực tiếp tới tỉ lệ click.
- ✅ **Reverse trial trên nút đóng paywall.** Đây là thứ bạn triển khai được **trong một buổi chiều** với RevenueCat và có thể là ROI cao nhất trong toàn bộ case.
- ✅ **Xin rating tại khoảnh khắc vàng**, không xin theo lịch.
- ✅ **Chuyển từ MAU sang event analytics trước khi làm bất cứ việc marketing nào.**

### Rào cản thật

- 🔴 **Chi phí hạ tầng $3.500/tháng là rào cản vốn nghiêm trọng.** Đây không phải app chạy trên Supabase free tier. Bạn cần doanh thu tương đối trước khi mở rộng số thành phố, mà doanh thu lại đến sau khi có thành phố → **bài toán con gà quả trứng có mùi tiền thật**. Cách vào an toàn cho người Việt: **bắt đầu bằng đúng một thành phố** và một nguồn dữ liệu, đẩy lên hoà vốn rồi mới thêm thành phố thứ hai.
- 🔴 **Dữ liệu giao thông công cộng ở VN không sẵn như ở châu Âu.** Momego sống nhờ các cơ quan giao thông Anh/Mỹ **công bố dữ liệu real-time theo chuẩn mở** (GTFS-RT). Ở VN, dữ liệu này rời rạc, không chuẩn hoá, nhiều nơi không có. **Nếu bạn định sao chép đúng ngành này, hãy kiểm tra nguồn dữ liệu TRƯỚC, đừng viết một dòng code nào trước khi biết dữ liệu ở đâu.**
- 🔴 **ARPU nội địa thấp.** Gói năm kiểu Âu Mỹ ($20-40/năm) không bán được cho phần lớn người dùng VN. Hoặc bạn nhắm thị trường nước ngoài ngay từ đầu (ASO không cần bạn nói tiếng Anh giỏi — chỉ cần viết đúng keyword), hoặc bạn thiết kế mô hình giá thấp hơn nhiều và cần lượng user lớn hơn nhiều.
- 🔴 **Dòng tiền âm 30-45 ngày với Apple** cộng hoa hồng 15-30%. Với chi phí server cố định $2.500/tháng, đây là rủi ro thanh khoản thật, không phải lý thuyết.
- 🔴 **Mẹo localization có thể đã bị Apple vá.** Video đăng 10/2025 nhưng mô tả chiến thuật kéo dài từ 2017. Hãy tự test, đừng tin.
- 🔴 **Thời gian.** 8 năm. Nếu bạn cần tiền trong 6 tháng, mô hình này sai.

### Khi nào KHÔNG dùng mô hình này

- ❌ **Khi sản phẩm của bạn không có biến thể theo địa phương.** Toàn bộ lợi thế ASO của Momego đến từ việc 160 thành phố = 160 từ khoá riêng. Một app ghi chú thì chỉ có một từ khoá `notes` và bạn đang đấu với Notion. Hãy dùng cách của [Journable](../2026-03-25_i-built-a-100k-month-android-app/case.md) (Google Ads trên Android) hoặc [CalBuddy](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) (bản địa hoá ngôn ngữ + ads CPM rẻ).
- ❌ **Khi người dùng không mở app hằng ngày.** Reverse trial 7 ngày và vòng lặp rating đều dựa trên tần suất sử dụng cao. App dùng theo mùa hoặc theo sự kiện thì cả hai cơ chế đều gãy.
- ❌ **Khi bạn không chịu nổi chi phí cố định.** ASO là kênh **pull, chi phí gần 0** — nhưng sản phẩm này thì không. Nếu muốn kênh pull *và* chi phí thấp, xem [danh mục 28 app của Max](../2025-12-11_i-make-10k-month-from-28-apps/case.md), nơi mỗi app là một tiện ích nhẹ không cần hạ tầng.
- ❌ **Khi bạn cần doanh thu tăng đột biến.** Đây là đường tăng trưởng phẳng và chậm — ngược hoàn toàn với [GlowUp](../2025-12-17_my-mobile-app-made-800k-in-365-days/case.md) (viral, răng cưa). Chọn theo nhu cầu dòng tiền của bạn, không theo con số cuối cùng.

---

## Nguồn

- Video: <https://www.youtube.com/watch?v=T5zMsTw8GWQ> (14:50, đăng 23/10/2025, 86.209 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
