---
id: rCV-TVCnF6Q
slug: propgpt-rebuild-product-not-distribution
product: PropGPT
founder: Eyal Hazan và Yahli Hazan (sinh viên đại học, cùng họ)
tagline: Ngược với mọi case khác — họ có phân phối ngay từ ngày đầu nhưng sản phẩm sai, phải TẮT toàn bộ marketing 4 tháng để viết lại từ đầu
revenue_usd_month: 30000
revenue_basis: 30.000 USD/tháng tại thời điểm quay; đỉnh từng đạt 40K MRR trong mùa playoff NBA. Video tự mâu thuẫn — intro nói đạt 30K MRR trong 10 tuần, mô tả video nói vượt 10K MRR trong 1 tuần sau khi relaunch, còn founder kể là 2,5 tháng sau relaunch mới chạm đỉnh 40K. Tôi lấy 30K vì đó là con số hiện tại được cả hai founder xác nhận
model: mobile-app-subscription
category: sports-betting-analytics (phân tích kèo thể thao bằng machine learning)
audience: B2C — người cá cược thể thao ở Mỹ, chủ yếu đặt kèo player props
started: build v1 mất 5 tháng, launch giữa mùa NFL năm trước
time_to_first_sale: có doanh thu ngay khi launch nhưng mắc kẹt ở 1-2K MRR nhiều tháng
time_to_scale: 4 tháng viết lại + khoảng 2,5 tháng sau relaunch để chạm đỉnh 40K MRR
team_size: 2 co-founder
funding: bootstrapped
main_channel: influencer marketing trả phí (khoảng 10.000 USD/tháng) cộng với cơ hội viral organic
tech_stack: [React Native, TypeScript, Python, Neon, RevenueCat, Superwall, PostHog]
key_metrics:
  downloads: 40.000+
  paying_customers: 3.000+
  revenue_per_download: 3,30 USD
  conversion_to_trial: 48%
  peak_mrr: 40.000 USD
  peak_downloads_day: 2.000 lượt tải trong một ngày
  before_rebuild: 45% tải sang trial nhưng chỉ 13% trial sang trả tiền
  marketing_spend: khoảng 10.000 USD/tháng
  margin: khoảng 50%
  viral_video: video thứ 70 đạt 600.000 view, kéo MRR từ 8K lên 38K trong 3 ngày
replicability_vn: 2
difficulty: 4
video_url: https://www.youtube.com/watch?v=rCV-TVCnF6Q
published: 2025-11-18
views: 38114
---

# PropGPT — $30K/tháng sau khi tắt marketing 4 tháng để đập đi xây lại

> **Tóm tắt 30 giây:** Hầu hết founder có sản phẩm tốt nhưng không biết bán. Eyal và Yahli Hazan gặp đúng vấn đề **ngược lại**: influencer marketing chạy ngon từ ngày đầu, 20 lượt tải/ngày, **45% người tải chuyển sang trial** — nhưng chỉ **13% trial chịu trả tiền**, và họ kẹt ở $1-2K MRR suốt nhiều tháng. Chẩn đoán của họ: người dùng muốn **được đưa đáp án**, không muốn tự đi tra kèo. Họ **tắt sạch marketing, dành 4 tháng viết lại từ đầu**, relaunch ngày 15/4 ở mức $1.700 MRR — rồi bơm marketing trở lại đúng mùa playoff NBA, conversion sang trả tiền vọt lên **trên 50%**, đỉnh **40K MRR** và **2.000 lượt tải trong một ngày**. Hiện tại: $30K/tháng, 40.000 lượt tải, 3.000+ khách trả tiền.

![$30.000/tháng](screenshots/01_01m09s_usd-30-000.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| Doanh thu | ~$30.000/tháng |
| Đỉnh | 40K MRR (mùa playoff NBA) |
| Lượt tải | 40.000+ |
| Khách trả tiền | 3.000+ |
| Doanh thu / lượt tải | **$3,30** |
| Conversion sang trial | 48% |
| **Trước khi viết lại** | 45% sang trial, chỉ **13%** trial sang trả tiền |
| **Sau khi viết lại** | conversion sang trả tiền **trên 50%** |
| Ngày đỉnh | 2.000 lượt tải |
| Chi marketing | ~$10.000/tháng |
| Biên lợi nhuận | ~50% |

**Về mâu thuẫn số liệu trong video:** phần intro (do Pat Walls dựng) nói *"they hit $30,000 MRR in just 10 weeks"*, mô tả video nói *"hit over $10K MRR in one week"*, còn lời founder kể là relaunch 15/4 ở $1.700 MRR, tháng sau mới bơm marketing, và **2,5 tháng sau đó** mới chạm đỉnh 40K MRR. Ba con số này không mâu thuẫn nếu hiểu là ba cột mốc khác nhau, nhưng cách đóng gói của kênh khiến người xem tưởng mọi thứ xảy ra trong một tuần. **Mốc đáng tin nhất: 15/4 relaunch → khoảng 10 tuần sau chạm 40K MRR.**

Một lỗi nói nhầm nữa: founder nói video 600K view *"raised our ARR from around 8K to 38K in about 3 days"* — nhưng với đỉnh 40K MRR thì con số 8K và 38K gần như chắc chắn là **MRR chứ không phải ARR**.

## 2. Sản phẩm là gì

PropGPT là nền tảng phân tích cá cược thể thao. Một thuật toán machine learning quét **toàn bộ kèo mỗi ngày**, chấm điểm và đưa ra danh sách kèo đã phân tích sẵn. Người dùng có thể xem danh sách đó, hoặc nhập kèo của chính mình để hệ thống đánh giá.

Kỹ thuật: TypeScript cho app, **Python cho thuật toán ML** và cho hệ thống tự động lấy dữ liệu, một database rất lớn đặt trên **Neon**.

## 3. Chẩn đoán quan trọng nhất — hai con số phân biệt lỗi sản phẩm với lỗi marketing ⭐⭐⭐

Đây là phần giá trị nhất của case, và nó áp dụng được cho **mọi app subscription**, không riêng cá cược.

Trước khi viết lại, PropGPT có:

- **45%** người tải chuyển sang trial → rất cao
- **13%** trial chuyển sang trả tiền → rất thấp

Founder diễn giải chính xác:

> *"Everybody wanted what we were selling, but the product was [not good enough]."*

Và họ mô tả khoảnh khắc nhìn ra nó, vào ngày Super Bowl:

> *"We saw that a lot of people were converting to the trial, but then nobody was staying after. Like what does that really say about your users? What it means is that your users think this is a great idea. They think that this could add a lot of value to their life, but when it actually comes to using the app, it's not the experience they were hoping for."*

**Bảng chẩn đoán — tôi rút ra từ cơ chế này, dùng được cho app của bạn:**

| Tải → trial | Trial → trả tiền | Chẩn đoán | Việc phải làm |
|---|---|---|---|
| Cao | **Thấp** | **Lời hứa đúng, sản phẩm sai.** Marketing của bạn đang bán một thứ mà app không giao được | Viết lại sản phẩm. Đổ thêm tiền marketing chỉ làm bạn cháy nhanh hơn — đây chính là PropGPT |
| **Thấp** | Cao | Sản phẩm giao được giá trị, nhưng paywall/onboarding/thông điệp không bán được nó | Sửa phễu và cách diễn đạt, đừng động vào core |
| Thấp | Thấp | Sai đối tượng, hoặc vấn đề này không đủ đau | Đổi ngách. Đừng cố sửa |
| Cao | Cao | Đúng cả hai | Bơm tiền, càng nhanh càng tốt |

**Vì sao cơ chế này đáng tin:** hai tỉ lệ này đo hai thứ khác nhau. Tỉ lệ tải→trial đo **sức thuyết phục của lời hứa** (store listing, paywall, quảng cáo của influencer). Tỉ lệ trial→trả tiền đo **sản phẩm có giữ lời hứa đó không**. Khi bạn có một tỉ lệ cao và một tỉ lệ thấp, bạn biết chính xác nửa nào đang hỏng — và đó là thông tin đắt hơn bất kỳ khảo sát người dùng nào.

![Doanh thu ngày relaunch — $1.700 MRR](screenshots/04_04m20s_usd-1-700-m.jpg)

## 4. Họ đã đổi CÁI GÌ — một câu duy nhất đáng ghi lại ⭐⭐⭐

> *"We realized that what our customers actually wanted was just to be given the right answers to the test, and not necessarily go through the sportsbooks and input their bets and check for themselves if it was a good bet or not."*

Dịch sang nguyên tắc chung: **người dùng B2C muốn KẾT QUẢ, không muốn CÔNG CỤ.**

- Bản cũ là một **workspace**: bạn tự đi qua các nhà cái, tự nhập kèo, tự kiểm tra.
- Bản mới là một **câu trả lời**: đây là các kèo nên đánh hôm nay.

Đây là cùng một sai lầm mà rất nhiều app AI đang mắc: xây một giao diện chat, một bảng điều khiển, một bộ công cụ — trong khi người dùng chỉ muốn bấm một nút và nhận đáp án. Với B2B thì công cụ bán được, vì người mua có thời gian và có quy trình. Với B2C giải trí thì **mỗi bước thao tác bạn bắt người dùng làm là một phần trăm conversion bị mất**.

Chi phí của bài học này: **4 tháng, không marketing, không doanh thu tăng.**

> *"We shut down all marketing and spent 4 months completely rebuilding from scratch."*

Đây là quyết định khó nhất trong case và đáng nể nhất. Đa số founder ở vị trí đó sẽ tăng chi quảng cáo để cứu con số — vì tỉ lệ tải→trial 45% khiến mọi thứ trông như đang hoạt động.

![Cách build một sản phẩm tốt](screenshots/05_05m47s_ch-how-to-build-a-great-product.jpg)

## 5. Playbook 4 bước ⭐⭐

| Bước | Nội dung | Ghi chú của tôi |
|---|---|---|
| 1 | **Hiểu chính xác bạn build cho ai và nỗi đau của họ là gì** | Nghe sáo rỗng, nhưng ở đây nó cụ thể — họ tưởng khách muốn công cụ phân tích, thực ra khách muốn được cho đáp án |
| 2 | **Nghe số liệu.** *We became obsessed with the numbers* | Cặp 45% / 13% ở mục 3 chính là thứ này |
| 3 | **Ám ảnh với analytics.** Theo dõi từng màn hình onboarding để biết người dùng rơi ở đâu; theo dõi từng cú click feature để biết **value proposition thật** của app là gì, rồi đem chính cái đó đi làm marketing | Đây là bước tinh vi nhất: analytics không chỉ để sửa sản phẩm, mà để **tìm ra câu quảng cáo**. Feature được click nhiều nhất chính là câu headline của bạn |
| 4 | **Scale bằng influencer marketing** | *"Their followers engage deeply and convert faster when they see someone that they admire using your product"* |

Công cụ họ dùng để làm việc này: **PostHog** cho hành vi, **Superwall** cho paywall và A/B test màn hình bán hàng, **RevenueCat** cho subscription.

![Playbook app tốt](screenshots/06_07m01s_ch-great-app-playbook.jpg)

## 6. Phân phối — và con số ít người nhắc tới ⭐⭐

Giai đoạn đầu: chi vài nghìn đô cho influencer marketing → **~20 lượt tải/ngày**, chuyển thành 5-10 người dùng/ngày.

Giai đoạn sau, cú nổ:

> *"Probably our 70th video to ever come out hit 600,000 views, and that raised our [MRR] from around 8K to 38K in about 3 days."*

**Chú ý con số 70.** Đây là bằng chứng định lượng cho cùng một quy luật đã thấy ở [Coherence](../2025-11-20_our-mobile-app-made-85k-in-8-months/case.md): bạn không dự đoán được video nào nổ, bạn chỉ kiểm soát được **số lần thử**. 69 video trước đó không đổi đời gì cả. Nếu họ bỏ cuộc ở video thứ 50, sẽ không có case này.

**Nhưng — và đây là điều video không nói thẳng:**

- Chi marketing là **$10.000/tháng** trên doanh thu $30.000/tháng. Tức **1/3 doanh thu đi vào việc mua lượt tải**. Đây **không phải** mô hình organic flywheel; đây là mô hình mua traffic có biên tốt. Ngừng chi tiền, doanh thu sẽ giảm.
- Đỉnh 40K MRR trùng đúng **mùa playoff NBA**. Hiện tại $30K. Cá cược thể thao là ngành **mùa vụ khắc nghiệt**: mùa NFL, playoff NBA, rồi mùa hè gần như chết. Video không hề đề cập rủi ro mùa vụ, và tôi cho đó là thiếu sót lớn nhất của nó. Nếu bạn định làm mô hình gắn với lịch thi đấu, hãy mô hình hoá dòng tiền theo mùa trước khi cam kết.

## 7. Tech stack và chi phí

| Hạng mục | Công cụ / chi phí |
|---|---|
| App | **React Native**, chủ yếu **TypeScript** |
| Machine learning + tự động lấy dữ liệu | **Python** |
| Database | **Neon** — ~$10/tháng |
| Paywall / A/B test | **Superwall** — $0,20 mỗi conversion |
| Subscription | **RevenueCat** — ~1% doanh thu |
| Analytics hành vi | **PostHog** |
| Data API thể thao thời gian thực | ~$100/tháng |
| LLM | ~$20/tháng (*"the cost is constantly going down"*) |
| **Marketing** | **~$10.000/tháng** |
| Biên lợi nhuận | ~50% |

**Điểm đáng học về cấu trúc chi phí:** hạ tầng kỹ thuật của một app $30K/tháng chỉ tốn khoảng **$130/tháng**. Toàn bộ chi phí thật nằm ở **marketing**. Đây là hình dạng chi phí điển hình của app di động B2C hiện đại — và nó nói cho bạn biết kỹ năng nào thực sự quyết định thắng thua.

## 8. Mâu thuẫn với các case khác — và cách phân định ⭐⭐⭐

Câu chốt của Pat Walls ở cuối video là câu đáng giá nhất:

> *"Usually you get the product right, but you don't have the distribution figured out. For them, they had the distribution figured out, but they didn't get the product right."*

| Quan điểm | Ai | Đúng khi nào |
|---|---|---|
| **Phân phối là tất cả**, sản phẩm chỉ cần đủ dùng | Phần lớn case app viral trong kho | Sản phẩm giao giá trị ngay ở lần dùng đầu, và bạn bán gói one-time hoặc gói tuần |
| **Sản phẩm là tất cả** — có phân phối mà sản phẩm tệ thì càng chi càng chết | PropGPT (case này) | Bạn bán **subscription dài hạn**, tức là phải giữ chân người dùng qua nhiều chu kỳ thanh toán |
| **Content validate trước, sản phẩm sau** | [Coherence](../2025-11-20_our-mobile-app-made-85k-in-8-months/case.md), [GlowUp](../2025-12-17_my-mobile-app-made-800k-in-365-days/case.md) | Bạn chưa biết ngách nào đau nhất |

**Phân định bằng mô hình doanh thu của bạn:**

- Nếu bạn bán **gói tuần / one-time / trải nghiệm dùng một lần**, phân phối thật sự quan trọng hơn — người dùng trả tiền trước khi kịp thất vọng.
- Nếu bạn bán **subscription tháng hoặc năm với trial**, sản phẩm quan trọng hơn — vì trial là chỗ sự thật lộ ra, và PropGPT bị đúng cái bẫy đó.

Đó là lý do case này bổ sung chứ không phủ định các case khác. Nó chỉ ra rằng **câu hỏi đúng không phải sản phẩm hay phân phối, mà là bạn thu tiền ở thời điểm nào trong hành trình người dùng.**

## 9. Lời khuyên cuối của founder

> *"Have a co-founder who you will be able to lean on, and that will be able to lean on you when things get hard."*

> *"Be honest with yourself and scientific about whether what you're working on has enough demand. And if you prove it to yourself that it's worth the time investment, it will be an order of magnitude easier to prove it to others."*

Câu thứ hai đáng chú ý vì nó **giải thích lý do họ dám tắt marketing 4 tháng**: họ đã có bằng chứng cầu là thật (45% sang trial). Nếu tỉ lệ đó cũng thấp, quyết định viết lại sẽ là canh bạc mù. **Chỉ nên đập đi xây lại khi bạn đã có bằng chứng rằng người ta MUỐN thứ bạn hứa.**

![Lời khuyên và bài học](screenshots/09_09m39s_ch-advice-and-lessons.jpg)

## 10. Cảnh báo thiên kiến nguồn và cảnh báo pháp lý

**Thiên kiến nguồn:** video có **hai đoạn quảng cáo** trong 10 phút — deal Black Friday của Starter Story (2:19-2:56) và khoá học Starter Story Build (4:42-5:35). Đoạn Starter Story Build được cài ngay giữa cao trào câu chuyện, đúng chỗ người xem đang muốn biết họ đã sửa gì. Kênh đã được HubSpot mua lại và chỉ phỏng vấn người thành công.

**Cảnh báo về ngành:** chính mô tả video có dòng miễn trừ *"Nothing in this video constitutes gambling advice"* và số hotline **1-800-GAMBLER**. Đây không phải hình thức. PropGPT là sản phẩm phục vụ cá cược thể thao, và:

- **Ở Việt Nam, cá cược thể thao gần như bị cấm với công dân Việt Nam** (chỉ có một số thí điểm rất hẹp). Xây và vận hành sản phẩm phục vụ hoạt động này từ VN là rủi ro pháp lý thật, không phải rủi ro lý thuyết.
- **App Store và Google Play có chính sách rất khắt khe** với app liên quan cờ bạc: yêu cầu giấy phép, giới hạn theo quốc gia, kiểm duyệt riêng. Ngay cả app chỉ làm "phân tích" cũng thường xuyên bị vướng.
- **Cổng thanh toán** thường từ chối ngành này hoặc áp phí cao hơn.

Tôi vẫn đưa case này vào kho vì **bài học chẩn đoán ở mục 3 và 4 là tài sản thật và hoàn toàn tách rời khỏi ngành cá cược**. Hãy lấy phương pháp, đừng lấy ngách.

## 11. Áp dụng cho tôi (indie hacker VN)

### Sao chép được gì

1. **Dựng bảng chẩn đoán ở mục 3 vào dashboard của bạn ngay từ tuần đầu.** Hai tỉ lệ — tải→trial và trial→trả tiền — là bộ đôi rẻ nhất, nhanh nhất để biết bạn đang hỏng ở đâu. Không cần phỏng vấn ai.
2. **Câu hỏi tự vấn: sản phẩm của tôi là công cụ hay là đáp án?** Nếu người dùng phải làm 3 bước trước khi nhận giá trị, hãy thử phiên bản chỉ có 1 bước. Đây là bài học chuyển được sang gần như mọi app AI B2C.
3. **Dùng analytics để tìm câu quảng cáo, không chỉ để sửa bug.** Feature nào được click nhiều nhất chính là headline của bạn. Bước 3 trong playbook của họ là bước ít người làm nhất.
4. **PostHog + Superwall + RevenueCat là bộ ba rẻ và đủ.** Superwall cho phép bạn A/B test paywall mà không cần submit lại app — với thị trường ARPU thấp như VN, tối ưu paywall là đòn bẩy lớn nhất bạn có.
5. **Kỷ luật "70 video".** Ghi con số đó lên tường. Nếu bạn bỏ cuộc ở video thứ 20, bạn chưa thật sự thử.

### Rào cản thật

- **Ngách này gần như đóng với người VN** vì lý do pháp lý nêu ở mục 10. Đừng copy ngách, chỉ copy phương pháp.
- **$10.000/tháng chi marketing là rào cản vốn thật.** Đây không phải case bootstrapped $0 như [FollowBuddy](../2026-03-19_i-make-17k-month-with-one-strategy/case.md). Bạn cần vốn để chạy influencer marketing ở quy mô có ý nghĩa, và bạn phải chịu được **dòng tiền âm 30-45 ngày** vì Apple/Google trả tiền chậm trong khi influencer đòi trả trước.
- **4 tháng không doanh thu tăng là 4 tháng phải sống bằng gì đó.** Họ là sinh viên đại học, chi phí sinh hoạt gần bằng 0. Hãy trung thực về đường băng tài chính của bạn trước khi bắt chước quyết định này.
- **Influencer marketing bằng tiếng Anh cần khả năng đàm phán và brief bằng tiếng Anh.** Đây là rào cản ngôn ngữ thật, khác hẳn với việc chỉ cần chạy Meta ads.
- **Mùa vụ.** Nếu ngách của bạn gắn với lịch (thi cử, lễ tết, mùa giải), doanh thu sẽ dao động mạnh và bạn phải tính vốn lưu động theo mùa thấp nhất.
- **Rủi ro nền tảng ở mức rất cao** với bất kỳ app nào chạm tới cờ bạc, tài chính, hoặc sức khoẻ. Một lần đổi chính sách của Apple có thể xoá sổ doanh nghiệp.

### Khi nào KHÔNG dùng mô hình này

- **Khi bạn không có tiền để mua traffic.** Toàn bộ tăng trưởng của PropGPT được mua bằng $10K/tháng. Nếu vốn của bạn là $0, hãy đọc case dựa trên SEO hoặc organic content thay vì case này.
- **Khi bạn chưa có bằng chứng cầu.** Đừng bắt chước quyết định "tắt marketing 4 tháng để viết lại" nếu bạn chưa có một tỉ lệ nào đó cao bất thường chứng minh người ta muốn lời hứa của bạn. Không có bằng chứng đó, 4 tháng viết lại chỉ là 4 tháng trốn tránh việc bán hàng.
- **Khi bạn bán gói one-time hoặc gói tuần cho một trải nghiệm dùng một lần.** Lúc đó bài học ở đây bị đảo ngược — phân phối mới là thứ quyết định.
- **Khi ngách bị ràng buộc pháp lý mà bạn không kiểm soát được.** Cá cược, tài chính có tư vấn đầu tư, y tế có chẩn đoán. Chi phí compliance và rủi ro bị gỡ app sẽ ăn hết lợi thế tốc độ của một indie hacker.

## Nguồn

- Video: <https://www.youtube.com/watch?v=rCV-TVCnF6Q> (10:49, đăng 18/11/2025, 38.114 view)
- Founder trên X: <https://x.com/eyali__> và <https://x.com/YahliHazan>
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
