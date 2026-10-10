---
id: 2dfMUtHlQik
slug: gravl-ai-fitness-clone-paid-ads
product: Gravl (tên ban đầu Gains AI)
founder: Julian Gargicevich
tagline: Clone thẳng app fitness đang top nhưng sửa đúng một lỗi chí mạng của nó, rồi scale bằng quảng cáo bắt đầu từ dưới 50 USD/ngày
revenue_usd_month: 440000
revenue_basis: founder nói tháng gần nhất làm hơn 440K USD (nhắc hai lần trong video); tiêu đề Starter Story làm tròn xuống thành 400K/tháng. Tôi lấy 440K vì đó là con số founder tự nêu, và ghi rõ cả hai để bạn tự kiểm
model: mobile-app-subscription
category: health-fitness
audience: B2C — người tập gym muốn có giáo án tự sinh theo thiết bị, mục tiêu và thể trạng
started: ý tưởng từ khi startup cũ đang chết; ra mắt khoảng 2 năm trước thời điểm quay (cuối 2023)
time_to_first_sale: subscription đầu tiên đến trong 10 phút sau khi bật quảng cáo
time_to_scale: khoảng 2 năm từ lúc ra mắt tới 440K USD/tháng
team_size: 3 người trong năm đầu (Julian code, Matias và Aaron lo growth/ads), nay 13-14 người kể cả part-time và contractor
funding: bootstrapped
main_channel: quảng cáo trả tiền Meta + TikTok với sáng tạo UGC; cú hích đầu tiên đến từ một bài Reddit
tech_stack: [React Native, Expo, .NET, Next.js, React, Cursor, RevenueCat, Apple Health, Strava]
key_metrics:
  subscribers: hơn 70.000
  mvp_time: 2-3 tháng
  reddit_launch: hơn 300.000 impression, vài trăm like trong vài giờ đầu, vài nghìn user đầu tiên
  ad_spend_start: dưới 50 USD/ngày
  ad_cost_share: khoảng 1/3 doanh thu (chỉ tiền mua ad, chưa tính chi phí sản xuất)
  salaries: 50.000-80.000 USD/tháng
  apple_cut: 15% (founder tự nêu)
  revenuecat_cut: 1% doanh thu
  infra_cost: khoảng 1.000 USD/tháng
  mmp_cost: khoảng 1.000 USD/tháng
replicability_vn: 2
difficulty: 4
video_url: https://www.youtube.com/watch?v=2dfMUtHlQik
published: 2025-11-13
views: 249456
---

# Gravl — $440K/tháng từ việc clone một app fitness rồi sửa đúng chỗ nó sai

> **Tóm tắt 30 giây:** Julian là dev người Argentina sống ở Úc. Bạn anh cho xem **Fitbod** — app tập gym lớn nhất thị trường. Julian dùng thử, thấy UI/UX tuyệt nhưng **giáo án tập thì kỳ quặc, thậm chí nguy hiểm**. Anh không tìm ý tưởng mới: anh lấy nguyên UI/UX của Fitbod và gắn vào một **workout engine làm đàng hoàng**. MVP 2-3 tháng, đăng một bài kỹ thuật lên Reddit → 300.000 impression và vài nghìn user đầu tiên trong vài giờ. Hai năm sau: **hơn 70.000 subscriber, 440K USD tháng gần nhất**, đội 13-14 người, và **1/3 doanh thu đổ ngược vào quảng cáo**. Chi tiết đắt nhất: anh dịch app sang tiếng Tây Ban Nha rồi chạy ads ở Nam Mỹ — nơi CPI rẻ hơn Mỹ nhiều lần.

![$400K/tháng](screenshots/01_00m50s_usd-400-000.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | hơn **$440K** tháng gần nhất (tiêu đề video ghi $400K) |
| Subscriber | hơn 70.000 |
| Thời gian làm MVP | 2-3 tháng |
| Kênh đầu tiên | 1 bài Reddit → 300.000 impression, vài nghìn user |
| Ngân sách ads ban đầu | **dưới $50/ngày** |
| Chi phí ads hiện tại | ~1/3 doanh thu (~$146K/tháng nếu doanh thu $440K) |
| Lương | $50K-$80K/tháng |
| Apple | 15% (theo lời founder) |
| RevenueCat | 1% doanh thu |
| Hạ tầng + AI bills | ~$1K/tháng |
| MMP (đo lường ads) | ~$1K/tháng |
| Đội ngũ | 3 → 13-14 người |

**Tự tính biên lợi nhuận theo đúng số founder đưa** (doanh thu $440K):

| Khoản | Ước tính |
|---|---|
| Quảng cáo (1/3) | ~$147K |
| Apple 15% | ~$66K |
| Lương | $50K-$80K |
| RevenueCat 1% | ~$4,4K |
| MMP + hạ tầng | ~$2K |
| **Còn lại** | **~$140K-$170K/tháng** (biên ròng ~32-38%) |

**Cảnh báo về con số 15% của Apple.** App Store lấy **30%** năm đầu của mỗi subscriber, chỉ xuống 15% từ năm thứ hai trở đi (và Small Business Program 15% chỉ áp dụng khi dưới $1M/năm — Gravl đã vượt xa). Với một app đang **tăng trưởng bằng ads**, phần lớn subscriber là người mới → tỉ lệ thực tế nằm đâu đó **giữa 15% và 30%**, gần 30% hơn. Nếu bạn dựng mô hình tài chính theo case này, đừng dùng con số 15%.

**Ghi chú tên riêng (transcript là auto-caption, sai nhiều):** app tên **Gravl** (caption đọc thành "Gravel"); app anh clone là **Fitbod** (caption đọc "Fitbot"); tên cũ của Gravl là **Gains AI** (caption đọc "Games AI"); các app tracker anh nhắc là **Hevy** và **Strong**; "Straa" = **Strava**; "Capkart" = **CapCut**; "Revenue cut" = **RevenueCat**.

## 2. Nguồn gốc ý tưởng: đừng sáng tạo, hãy tìm chỗ đối thủ làm ẩu ⭐⭐⭐

Đây là phần giá trị nhất của video, và nó ngược hoàn toàn với bản năng của đa số builder.

Julian bắt đầu bằng cách **sai**: anh làm một workout tracker giống Hevy, giống Strong.

> *"Nhưng khi đang build, tôi nhận ra: ok, mình chẳng thêm giá trị gì cả. Nó chỉ là bản sao của cái họ đang làm."*

Rồi bạn anh cho xem Fitbod. Julian mê ngay vì Fitbod **giải quyết một việc khác hẳn**: nó tự đưa giáo án cho bạn tại chỗ, bạn không phải nghĩ gì. Nhưng khi dùng thật:

> *"Tôi để ý các bài tập nó đưa ra rất kỳ, đôi lúc còn hơi nguy hiểm. Càng dùng tôi càng thấy: wow, ok, mấy giáo án này thật sự tệ. Đó là thứ kích hoạt tôi. Rồi tôi nghĩ: **được rồi, chính là nó. Chúng ta cần build UI/UX của Fitbod với một workout engine tử tế.**"*

**Cơ chế vì sao cách này ăn tiền:**

1. **Fitbod đã tiêu hàng triệu đô để dạy thị trường** rằng "app tự sinh giáo án" là một loại sản phẩm đáng trả tiền. Julian không phải trả học phí đó.
2. **UI/UX là thứ đã được kiểm chứng** — copy nó là copy hàng nghìn giờ A/B test của người khác. Sao chép giao diện gần như không có rủi ro.
3. **Điểm yếu anh nhắm vào là điểm yếu người dùng CẢM NHẬN được** — giáo án dở là thứ ai tập gym vài tuần cũng thấy. Đây là khác biệt bán được, không phải khác biệt kỹ thuật chỉ mình founder thấy.
4. **Anh có unfair advantage thật:** bố anh sở hữu một trung tâm thể hình, anh lớn lên trong phòng gym. Kiến thức về progressive overload là thứ đội Fitbod thiếu, còn anh có sẵn.

> **Bài học chuyển giao được:** đừng hỏi *"ý tưởng mới nào chưa ai làm?"*. Hãy hỏi *"trong nhóm app đang kiếm tiền tốt, cái nào có một phần lõi làm ẩu mà tôi tình cờ hiểu rõ hơn họ?"*. Đây chính xác là luận điểm của [CalBuddy](../2026-08-09_i-copied-a-huge-app-now-i-make-80k-month/case.md) (copy Cal AI) và [Mike Hill](../2025-11-02_i-built-3-saas-apps-to-200k-mrr-heres-my-exact-playb/case.md) (*"chọn ý tưởng đã có người làm rồi — ý tưởng mới cần validate, ý tưởng cũ thì đã có sẵn câu trả lời"*).

Bối cảnh khiến case này càng đáng tin: startup trước của Julian (nền tảng influencer marketing cho game di động) **đang chết dần** và biến thành agency — thứ anh không hề muốn.

> *"Vì bọn tôi chuyển thành dạng agency, tôi có cả đống năng lượng lập trình không được dùng đến."*

Nhưng cái agency đó **dạy anh user acquisition, marketing và các con số thật của ngành app**. Đó là lý do anh biết app fitness kiếm được nhiều tiền trước cả khi viết dòng code đầu tiên. Đừng bỏ qua chi tiết này: **anh không đoán mò thị trường, anh đã từng chạy ads cho người khác.**

![Xây MVP](screenshots/03_04m13s_ch-building-the-mvp.jpg)

## 3. MVP: phần khó không phải app, mà là business logic ⭐⭐

MVP mất **2-3 tháng**, chia hai giai đoạn: trước Fitbod (làm tracker) và sau Fitbod (làm engine).

Phần khó nằm ở đúng chỗ ai cũng đánh giá thấp:

> *"Có rất nhiều business logic quanh việc build giáo án riêng cho từng người. Có quá nhiều thiết lập và tổ hợp — thiết bị bạn có, mục tiêu tuần, bạn đi gym bao lâu một lần, bạn có đều không, giới tính, cân nặng, tuổi. Có quá nhiều thứ phải cân. Đó chắc chắn là phần thách thức nhất."*

**Vì sao đây là tin tốt cho bạn:** trong thời AI viết code, phần "app" (màn hình, navigation, thanh toán) gần như miễn phí. Thứ còn lại tạo ra giá trị là **logic nghiệp vụ mà chỉ người trong nghề mới viết đúng**. Đó cũng là moat: một người vibe-code có thể clone giao diện Gravl trong một tuần, nhưng không clone được engine — vì anh ta không biết progressive overload là gì.

Đây là lời phản biện trực tiếp cho nỗi lo *"AI làm ai cũng build được, còn lợi thế gì?"*. Lợi thế dịch chuyển từ *code* sang *domain knowledge*.

## 4. 1.000 khách đầu tiên: một bài Reddit ⭐⭐⭐

Không phải Product Hunt, không phải build-in-public trên X. Một bài trên Reddit.

> *"Tôi ủng hộ Reddit như một kênh phân phối một cách cực đoan. Tôi đăng thread này về cách tôi build Gravl — hồi đó nó còn tên là Gains AI — và tôi chia sẻ các **thông số kỹ thuật** quanh nó."*

Kết quả: vài trăm like trong vài giờ đầu, **hơn 300.000 impression**, vài nghìn user đầu tiên.

**Cơ chế — và đây là chỗ đa số làm sai:**

- Anh **không đăng bài bán hàng**. Anh đăng **bài kỹ thuật về cách anh build**. Reddit trừng phạt quảng cáo và thưởng cho nội dung có chất.
- Đối tượng đọc là **developer**, không phải người tập gym. Nghe như sai target — nhưng Julian phát hiện điều bất ngờ:

> *"Họ là developer, họ thích công nghệ, và một số cũng thích đi gym — nhưng cảm thấy phòng gym hơi đáng sợ. Tôi thấy rất nhiều người trong số họ thật sự dùng app."*

Đây là bài học về **ICP ẩn**: dev + ngại phòng gym = đúng người cần một app bảo họ phải tập gì. Anh vô tình bắn trúng một phân khúc có nỗi đau gấp đôi.

- Lúc đó app **hoàn toàn miễn phí**. Cú đăng Reddit không mang về tiền — nó mang về **feedback về bug và feature request**, và đó mới là thứ anh cần:

> *"Rồi bọn tôi bắt đầu nhận được feedback về bug, về feature request, và bọn tôi nghĩ: ok, mình đang chạm vào cái gì đó. Đó là cú đẩy cuối cùng bọn tôi cần."*

**Cách đọc đúng bước này:** Reddit **không phải kênh scale**. Nó là **máy xác thực product-market fit**, dùng đúng một lần, miễn phí, và cho tín hiệu đủ mạnh để dám bật ví chạy ads. So sánh với [Gojiberry AI](../2026-01-25_how-i-used-reddit-to-build-a-34k-month-saas/case.md) — nơi Reddit được dùng như kênh chính lâu dài — thì Gravl dùng Reddit như một cú mồi lửa rồi chuyển hẳn sang paid.

![1.000 khách đầu tiên](screenshots/04_05m00s_ch-his-first-1-000-customers.jpg)

## 5. Playbook scale: paid ads, và 5 mẹo của Julian ⭐⭐⭐

> *"Với bọn tôi, kênh phân phối lớn hơn là quảng cáo trả tiền. Bọn tôi bật ads ngay khi thêm mô hình subscription. Tôi vẫn nhớ lần đầu chạy — bọn tôi có một subscription **trong 10 phút đầu** sau khi kích hoạt quảng cáo. Đó chắc là cảm giác phê nhất đời tôi."*

Và điểm mấu chốt mà ai cũng bỏ qua:

> *"Bọn tôi tiêu **dưới 50 đô một ngày** cho quảng cáo. Và đó là thứ hiệu quả với bọn tôi từ lúc bắt đầu **cho đến tận hôm nay**."*

Nghĩa là: mô hình được chứng minh ở quy mô $50/ngày trước, rồi mới nhân lên. Không ai bắt đầu bằng $5.000/ngày.

### Mẹo 1 — Validate TRƯỚC khi tiêu tiền quảng cáo

> *"Và khi tôi nói validate, không chỉ là sản phẩm chạy được, mà còn là **người ta sẵn sàng trả tiền cho nó**. Đó cũng là điều rất quan trọng."*

### Mẹo 2 — Dịch app và chạy ads ở thị trường quảng cáo rẻ ⭐⭐⭐

Đây là mẹo đáng giá nhất video, và là mẹo **áp dụng được ngay cho người Việt**.

> *"Đây là chỗ bọn tôi hơi may — tôi nói tiếng Tây Ban Nha, Matias cũng vậy. Nên hợp lý là dịch app sang tiếng Tây Ban Nha rồi chạy ads ở Nam Mỹ, nơi quảng cáo rẻ hơn. Ai cũng muốn kết thúc ở Mỹ, nhưng chạy ads ở đó đắt, cạnh tranh khủng khiếp."*

**Cơ chế:** CPI (cost per install) trên Meta là kết quả đấu giá. Ở Mỹ bạn đấu với Duolingo, Noom, Whoop, hàng nghìn app khác. Ở Nam Mỹ (hay Đông Nam Á) hồ đấu giá loãng hơn nhiều lần → CPI có thể rẻ hơn 3-10 lần. Đổi lại ARPU thấp hơn. Bài toán chỉ cần **LTV/CPI ở thị trường rẻ tốt hơn ở Mỹ** — và với app subscription giá thấp thì thường là có.

**Cái Julian có mà bạn cũng có:** một ngôn ngữ mà đối thủ Mỹ không buồn dịch sang. Với người Việt, đó là **tiếng Việt và các thị trường Đông Nam Á** — hoặc, chính xác hơn về mặt kinh tế, tiếng Việt là thị trường thử nghiệm rẻ để tinh chỉnh creative trước khi mang phiên bản tiếng Anh ra đấu ở Mỹ.

### Mẹo 3 — Bắt đầu nhỏ với người làm nội dung

> *"Bạn có thể trả cho influencer hoặc content creator thấp tới **50 đô** cho một mẩu nội dung. Bạn có thể dùng AI tool để tạo video. Bạn có thể dùng CapCut tự dựng. **Làm một cái quảng cáo không khó như bạn nghĩ. Cái khó là tạo ra khối lượng.**"*

Câu cuối là toàn bộ trò chơi paid ads: không phải tìm một quảng cáo thiên tài, mà là **sản xuất đủ nhiều để tìm ra cái thắng**.

### Mẹo 4 — UGC là vua

Phần lớn quảng cáo hiệu quả trên thị trường là nội dung kiểu người thật quay bằng điện thoại, không phải video sản xuất bóng bẩy.

### Mẹo 5 — Copy, copy và copy ⭐⭐

> *"Điều hay ở Meta Ads Library là **nó công khai toàn bộ**. Bạn vào dashboard của bất kỳ đối thủ nào và xem quảng cáo nào đang chạy tốt cho họ, họ đang đổ tiền vào đâu. Chẳng có bí quyết gì cả. Cứ copy cái đang hiệu quả với họ và bắt đầu như vậy."*

**Cụ thể hoá cho bạn:** vào `facebook.com/ads/library`, gõ tên đối thủ, lọc theo quốc gia. Quảng cáo **chạy lâu nhất** là quảng cáo đang có lãi — đó là dữ liệu chiến thắng của người khác, miễn phí. Đây là cùng một logic với việc Julian clone Fitbod: **để thị trường trả tiền cho việc thử nghiệm, còn bạn chỉ đọc kết quả.**

![Chiến lược marketing](screenshots/07_07m47s_usd-400-000.jpg)

## 6. Sản phẩm: onboarding dài, hard paywall, và support người thật ⭐⭐

Julian demo app, và ba chi tiết đáng chép lại:

**1. Onboarding hỏi rất nhiều — cố ý.** Tên, lý do dùng app, trình độ, one-rep max, mục tiêu, tần suất tập, kiểu split, nhóm cơ muốn tránh/tập trung, tập ở đâu. Nghe như ma sát, thực ra là **cam kết tăng dần**: mỗi câu trả lời làm người dùng đầu tư thêm vào phiên, và làm giáo án cuối cùng cảm giác "của riêng tôi".

**2. Hiển thị AI một cách lộ liễu — vì đó là bán hàng.**

> *"Bọn tôi dùng AI chỗ này chỗ kia. **Hãy chắc chắn bạn cho người dùng thấy đây là một app AI, vì đó là bán hàng.**"*

Có màn hình riêng chỉ để hiển thị "đang generate giáo án riêng cho bạn". Về kỹ thuật không cần thiết. Về chuyển đổi thì cần.

**3. Hard paywall trước khi đăng nhập lần đầu.**

> *"Hard paywall trước khi bạn đăng nhập lần đầu tiên. Kiểu, có bao nhiêu người thật sự trả tiền trước khi họ nhìn thấy sản phẩm? Và câu trả lời là: **rất nhiều**."*

Đây là điểm mâu thuẫn thẳng với trực giác freemium. Nó hoạt động vì onboarding dài đã làm hết việc bán hàng: đến màn hình trả tiền, người dùng đã thấy bản tóm tắt giáo án của **chính họ**. Bạn không bán một app, bạn bán thứ họ vừa cùng bạn tạo ra.

**4. Support chat 24/7 do người thật trả lời.**

> *"Bọn tôi có chat hỗ trợ 24/7 trong app, và sẽ có **một người thật trả lời, không phải AI**. Đó là thứ người dùng đánh giá rất cao."*

Trong một app quảng cáo bằng AI, phần chăm sóc lại cố tình **không** AI. Đây là lựa chọn về churn: người trả tiền hàng tháng rời đi vì thất vọng, không phải vì thiếu tính năng.

![Demo app](screenshots/08_09m43s_ch-how-the-app-works-full-walkthrough.jpg)

## 7. Tech stack

| Hạng mục | Công cụ |
|---|---|
| Mobile | **React Native + Expo** |
| Backend | **.NET** (phần lõi) |
| Dashboard nội bộ | Next.js + React |
| Thanh toán/subscription | RevenueCat (1% doanh thu) |
| Tích hợp | Apple Health, Strava (để tính recovery rate) |
| AI coding | Cursor |

Cách anh dùng AI coding đáng chú ý:

> *"Tôi dùng Cursor rất nhiều, nhưng tôi **rất cụ thể về việc động vào file nào**, và không để AI tự tung tự tác."*

Một codebase .NET có business logic phức tạp thì đây là cách duy nhất dùng AI mà không tự bắn vào chân.

![Chi phí và biên lợi nhuận](screenshots/10_12m22s_replay.jpg)

## 8. Lời khuyên cuối: biết khi nào bỏ cuộc

> *"**Hãy tự hào về thứ bạn build.** Ít nhất với tôi, động lực đến từ việc làm một thứ mình hứng thú thì không gì sánh được. Cày cuốc và làm không công luôn dễ hơn khi bạn yêu thứ mình đang làm."*

Nhưng phần sắc hơn nằm ở vế sau:

> *"Cũng phải biết **khi nào nên dừng** — khi bạn nhận ra: rồi, sản phẩm này không chạy. Trường hợp của bọn tôi là startup trước. Bọn tôi chắc đã kéo lê nó thêm cả một năm. Lẽ ra nên khai tử sớm hơn nhiều."*

**Hai câu này không mâu thuẫn — chúng bổ sung cho nhau.** Đam mê là nhiên liệu để chịu đựng giai đoạn 0 đồng; nhưng nó không được phép trở thành lý do giữ một thứ đã chết. Julian mất **một năm** vì nhầm hai thứ đó với nhau, và chính năm đó là học phí đã dạy anh cách chạy ads.

## 9. Cảnh báo thiên kiến nguồn

- Video có **hai lần bán hàng**: quảng cáo HubSpot (5:45-6:55) và quảng cáo **Starter Story Build** ở cuối. Kênh này đã được HubSpot mua lại và đang bán khoá học build app bằng AI — nên câu chuyện được kể theo hướng *"bạn cũng làm được"* nhiều hơn mức thực tế.
- **Sống sót có chọn lọc:** kênh chỉ phỏng vấn người thành công. Với mỗi Gravl có hàng trăm app fitness đốt hết tiền ads rồi chết. Chính Julian có một startup thất bại trước đó — chi tiết duy nhất trong video nhắc bạn điều này.
- Phần tài chính là **bản ghi bổ sung quay sau** ("async update from the future") vì họ quên hỏi. Các con số đều là **ước lượng miệng** ("I'd say a third is somehow accurate", "somewhere between 50 and 80K"), không có ảnh dashboard. Hãy coi đó là bậc thang độ lớn, không phải sổ sách.

## 10. Áp dụng cho tôi (indie hacker VN)

**Sao chép được gì — cụ thể:**

1. **Quy trình tìm ý tưởng, làm được ngay tuần này.** Mở App Store, lọc top grossing trong một ngành bạn **thật sự hiểu** (không phải ngành bạn thấy hot). Tải 5 app top. Dùng thật 2 tuần. Ghi lại **chỗ nào chúng làm ẩu mà bạn — với kiến thức nghề của mình — biết là sai**. Đó là danh sách ý tưởng của bạn.
2. **Đăng một bài kỹ thuật lên Reddit trước khi tiêu một đồng ads.** Nội dung: *cách tôi build cái này*, kèm chi tiết kỹ thuật thật. Mục tiêu không phải doanh thu — mà là xem có ai gửi bug report và feature request không. Không có = chưa có PMF, đừng bật ads.
3. **Meta Ads Library là mỏ vàng miễn phí.** Trước khi tự nghĩ creative, hãy chép cấu trúc của quảng cáo đối thủ đã chạy trên 3 tháng.
4. **Chiến thuật ngôn ngữ rẻ.** Julian dùng tiếng Tây Ban Nha + Nam Mỹ. Bạn có tiếng Việt + Đông Nam Á. Cùng logic: **tìm hồ đấu giá quảng cáo mà đối thủ Mỹ không thèm vào.**
5. **Onboarding dài + hard paywall.** Không cho dùng thử miễn phí trước paywall. Bù lại, làm onboarding đủ dài để người dùng tự tay tạo ra thứ họ sắp mua.
6. **Domain knowledge là moat, không phải code.** Nếu bạn không có lợi thế hiểu biết nào trong ngành bạn định làm, bạn đang cạnh tranh bằng tốc độ ship — và bạn sẽ thua người có cả hai.

**Rào cản thật — không tô hồng:**

- **Đây là mô hình cần vốn quảng cáo, không phải mô hình $0.** 1/3 doanh thu là ads. Ở giai đoạn đầu, tỉ lệ đó còn tệ hơn nhiều (bạn trả tiền học phí để tìm creative thắng). $50/ngày = ~38 triệu VNĐ/tháng đốt vào Meta trước khi biết có lãi hay không. Đây là khác biệt lớn nhất so với các case $0-ads trong kho như [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md) hay [Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md).
- **Dòng tiền âm 30-45 ngày với Apple.** Bạn trả tiền ads cho Meta **ngay hôm nay**, Apple trả tiền cho bạn **sau 30-45 ngày**. Ở quy mô $50/ngày thì chịu được; ở quy mô $5.000/ngày, bạn cần vốn lưu động cỡ $150K-$225K chỉ để lấp khoảng trống thời gian. Đây là lý do thật khiến nhiều app "có lãi trên giấy" vẫn chết.
- **Apple thực tế lấy 30%, không phải 15%.** Xem lại mục 1. Sai số này đủ để lật ngược một mô hình.
- **Thanh toán và pháp lý.** Để nhận tiền từ App Store bạn cần tài khoản Apple Developer + phương thức nhận tiền hợp lệ. RevenueCat và MMP đều tính phí bằng USD. Đây là chi phí cố định trước khi có đồng doanh thu đầu tiên.
- **Cần đội, không phải solo.** Julian code; **Matias và Aaron làm growth và ads toàn thời gian**. Đây không phải case một người. Nếu bạn định solo, bạn phải chọn: giỏi build *hoặc* giỏi mua traffic — và mô hình này thắng nhờ vế thứ hai.
- **Ngành fitness cực kỳ đông.** Fitbod, Hevy, Strong, Freeletics, Ladder... đều đang mua cùng một tập khán giả. CPI ngành này thuộc nhóm đắt nhất.
- **Rào cản tiếng Anh ở khâu support.** Chat 24/7 do người thật trả lời là lợi thế cạnh tranh của Gravl. Nếu bạn bán cho thị trường Mỹ, đó là chi phí nhân sự tiếng Anh thật.

**Khi nào KHÔNG dùng mô hình này:**

- Khi bạn **không có vốn chịu lỗ 3-6 tháng tiền ads**. Mô hình này thắng bằng tốc độ học của creative, mà tốc độ học mua bằng tiền. Không có vốn → chọn mô hình SEO/content như [Mike Hill](../2025-11-02_i-built-3-saas-apps-to-200k-mrr-heres-my-exact-playb/case.md) hoặc [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md).
- Khi sản phẩm của bạn là **B2B ACV thấp** — paid ads gần như không bao giờ hoàn vốn ở đó.
- Khi bạn **không có lợi thế hiểu biết** trong ngành. Julian thắng vì anh biết giáo án của Fitbod sai ở đâu. Nếu bạn clone mà không biết chỗ sửa, bạn chỉ là bản sao rẻ hơn — và bạn sẽ thua trong cuộc đua đốt tiền ads.
- Khi bạn **cần doanh thu trong 30 ngày**. Từ MVP đến $440K/tháng là **2 năm**, và năm đầu chỉ có 3 người ăn lương thấp.

## Nguồn

- Video: <https://www.youtube.com/watch?v=2dfMUtHlQik> (15:34, đăng 13/11/2025, 249.456 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
