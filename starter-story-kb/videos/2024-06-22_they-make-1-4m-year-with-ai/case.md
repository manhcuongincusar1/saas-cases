---
id: b5JhfGHafZA
slug: castmagic-appsumo-lifetime-deal-launch
product: Castmagic (castmagic.io) — biến audio/video thành nội dung bằng AI
founder: Ramon Berrios, Blaine Bolus và Justin (ba đồng sáng lập)
tagline: Ba founder từng gọi vốn VC hàng chục triệu quay lưng với VC, build sản phẩm trong 2 tuần bằng Elixir và dùng một lifetime deal trên AppSumo để mua 10.000 user cùng thương hiệu
revenue_usd_month: 120000
revenue_basis: founder nói north of 120,000 in MRR tại thời điểm quay (tháng 6/2024). Video có mâu thuẫn về thời gian đạt mốc — mô tả và lời Pat nói 9 tháng, còn founder nói we started about 10 months ago. Không có ảnh dashboard, chỉ có overlay chữ do biên tập thêm
model: b2b-saas-plg — subscription theo tháng có cap usage
category: ai-content-tools — repurpose nội dung từ podcast, video, audio
audience: B2B/B2C — podcaster, creator, marketer và đội nội dung cần biến audio thành show notes, bài đăng, newsletter
started: khoảng tháng 8-9/2023
time_to_first_sale: ngay khi ra mắt cùng AppSumo, 2 tuần sau khi bắt đầu code
time_to_scale: 9-10 tháng lên hơn 120.000 USD MRR
team_size: 3 co-founder cộng contractor theo từng mảng; marketing chỉ có một người
funding: bootstrapped — cả ba đều có quá khứ VC nhưng lần này không gọi vốn
main_channel: lifetime deal trên AppSumo để khởi động, sau đó là mạng lưới creator và affiliate trả theo CPM
tech_stack: [Elixir, Phoenix LiveView, Webflow, Notion, LLM API, dịch vụ transcription]
key_metrics:
  mrr: hơn 120.000 USD
  growth: hơn 20% tháng trên tháng
  net_churn: một chữ số
  marketing_spend_cap: luôn dưới 20% doanh thu
  appsumo_launch: khoảng 350.000 USD doanh thu và khoảng 10.000 user
  build_time: 2 tuần cho phiên bản đầu
  marketing_team: 1 người
replicability_vn: 3
difficulty: 3
video_url: https://www.youtube.com/watch?v=b5JhfGHafZA
published: 2024-06-22
views: 134078
---

# Castmagic — $120K MRR trong 9 tháng, và bài toán thật của một lifetime deal

> **Tóm tắt 30 giây:** Blaine dẫn một podcast và ghét việc viết show notes. Khi AI nổi lên, cả nhóm nhận ra máy làm được việc đó. Họ **viết sản phẩm trong 2 tuần bằng Elixir** để kịp một khung giờ ra mắt mà AppSumo đề nghị, rồi bán **lifetime deal**: khoảng **$350.000 doanh thu và ~10.000 user chỉ trong vài ngày**. Chín-mười tháng sau họ ở mốc **hơn $120.000 MRR**, tăng **trên 20% mỗi tháng**, **net churn một chữ số**, và giữ **chi phí marketing luôn dưới 20% doanh thu**. Điều thú vị nhất: cả ba founder đều đã từng ở trong hệ VC (một công ty của Ramon gọi hơn **$80 triệu**) và lần này họ chủ động không gọi một đồng nào.

![Ứng dụng AI](screenshots/01_01m16s_ch-the-ai-app.jpg)

## 1. Con số

| Chỉ số | Giá trị |
|---|---|
| MRR (tháng 6/2024) | hơn **$120.000** (≈ $1,44M/năm) |
| Thời gian đạt mốc | **9–10 tháng** *(video tự mâu thuẫn — xem dưới)* |
| Tăng trưởng | **hơn 20% tháng/tháng** |
| Net churn | **một chữ số** |
| Trần chi phí marketing | **dưới 20% doanh thu** — nguyên tắc cứng |
| Cú ra mắt AppSumo | ~**$350.000** doanh thu, ~**10.000 user** |
| Thời gian build bản đầu | **2 tuần** |
| Đội marketing | **1 người** (Ramon) + contractor theo mảng |
| Vốn ngoài | **$0** |

**Mâu thuẫn trong video:** mô tả và lời dẫn của Pat nói **9 tháng** (*"you guys grew zero to 120k MRR in 9 months"*), còn Ramon nói *"we started Castmagic about 10 months ago and today we're north of 120,000 in MRR"* và intro nói *"scaled it to six figures in MRR in just 10 months"*. Chênh lệch không đáng kể; tôi ghi **9–10 tháng** và không chọn một con số. Cũng cần lưu ý: **không có ảnh chụp dashboard nào** — mọi con số là lời kể, các số trên màn hình là overlay do biên tập thêm.

![Chỉ số](screenshots/04_03m49s_metric.jpg)

## 2. Nguồn gốc ý tưởng: làm một việc khác đủ lâu để va vào vấn đề ⭐⭐⭐

Blaine đồng dẫn **DTC Pod** cùng Ramon. Vấn đề của anh rất hẹp:

> *"Tôi để ý vấn đề này, mà lúc đó trong đầu tôi chỉ là: **làm sao viết show notes cho podcast**? Tôi không thể giao nó cho một VA ngẫu nhiên vốn không hiểu ngữ cảnh của người tôi vừa nói chuyện cùng. Đó là cảm hứng ban đầu — rồi khi thấy AI nổi lên, chúng tôi nghĩ: khoan đã, **AI có thể làm được việc này**."*

Bài học Ramon rút ra là câu đáng nhớ nhất của mục này:

> *"Bài học thật cho bất kỳ founder nào là: chỉ cần **làm một việc gì đó** và đặt mình vào tình huống liên tục phải làm — bạn sẽ **khai quật ra những vấn đề đáng giải quyết**, và có thể những vấn đề đó có hàm ý lớn hơn nhiều so với bạn nghĩ ban đầu."*

**Cơ chế:** đây không phải "tìm ý tưởng", mà là **tạo bề mặt va chạm với vấn đề**. Bạn không thể brainstorm ra "show notes cho podcast" trên giấy — bạn phải làm podcast 50 tập rồi mới thấy nó nhức. Điều này giải thích vì sao các case tốt nhất trong kho đều đến từ người **đang sống trong một quy trình** chứ không phải người ngồi tìm ý tưởng: [Thomas với Microsoft Intune](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md), [Profit AI từ một bảng tính](../2026-06-24_i-turned-this-spreadsheet-into-a-30k-month-micro-saa/case.md).

**Ngược lại — cảnh báo cho người VN:** hàm ý của điều này là bạn cần một "việc gì đó" đang làm đủ nghiêm túc. Nếu bạn đang tìm ý tưởng SaaS mà không có nghề nào, không cộng đồng nào, không quy trình nào lặp lại hằng ngày, bạn thiếu đúng nguyên liệu đầu vào của case này.

Về việc **AI nào thì đáng làm**, Ramon nêu một bộ lọc dùng được:

> *"Nếu bạn **nhúng được mình vào một workflow sẵn có** và **loại bỏ triệt để ma sát** của rào cản để làm một việc như sản xuất podcast — đó là những công cụ thật sự cất cánh. Đây là nhu cầu thật, không phải **vitamin — nó là painkiller**."*

![Tìm ra ý tưởng](screenshots/02_02m11s_ch-finding-the-idea.jpg)

## 3. AppSumo lifetime deal: phân tích thật cái đánh đổi ⭐⭐⭐

Đây là phần quan trọng nhất của case, và cũng là phần video kể một chiều nhất — nên tôi sẽ bóc cả hai mặt.

**Chuyện đã xảy ra:** khi nhóm bắt đầu nghĩ về phân phối, họ nói chuyện với đội AppSumo.

> *"Chúng tôi đang nói chuyện với team ở AppSumo và họ bảo: bọn tôi có cơ hội này, các anh có sẵn sàng ra mắt **sau 2 tuần nữa** không? Và chúng tôi nghĩ: ồ, 2 tuần cơ à — nhưng đây là cơ hội rất tốt để có phân phối và bắt đầu tăng trưởng."*

⇒ Deadline 2 tuần **tạo ra** sản phẩm. Không có lời mời đó, không có Castmagic phiên bản đầu.

**Kết quả:**

> *"AppSumo là một bệ phóng tuyệt vời để chúng tôi thiết lập một thương hiệu vững. Chúng tôi ra mắt với họ và tôi nghĩ đó là **một trong những launch thành công nhất từ trước tới nay trên AppSumo** — khoảng **$350.000 doanh thu**, mang lại cho chúng tôi khoảng **10.000 user**."*

**Họ tự nêu phản biện, rồi trả lời:**

> *"Chúng tôi chào **lifetime deal**, tức là khách hàng có quyền truy cập sản phẩm và dịch vụ của chúng tôi **mãi mãi**. Với người theo mô hình subscription thì họ sẽ nói: đời nào tôi làm thế khi có thể thu tiền định kỳ? Nhưng **chúng tôi cần xây thương hiệu, cần xây nền móng, và chúng tôi cần phản hồi**."*

### Bóc tách con số — phần video không làm

**Mặt được:**
- ~$350.000 tiền mặt ngay lập tức, không pha loãng cổ phần. So với việc gọi seed để có ngần đó tiền, đây là **vốn rẻ nhất trên đời**.
- ~10.000 người dùng thật đang dùng sản phẩm 2 tuần tuổi ⇒ **lượng phản hồi khổng lồ nén trong vài tuần**.
- Bằng chứng xã hội và thương hiệu — thứ mà một AI wrapper mới sinh không có cách nào khác để có.

**Mặt mất mà bạn phải tính:**
1. **AppSumo ăn phần rất lớn.** Con số "$350.000 revenue generated" trong video **không nói rõ là gross hay net về tay founder**. Trên thực tế AppSumo giữ một tỷ lệ đáng kể của mỗi deal. Nếu $350K là doanh thu gộp của deal, số tiền thực nhận thấp hơn nhiều. Video không làm rõ điểm này — hãy giả định số về tay founder nhỏ hơn con số bạn nghe.
2. **Đây là AI app — COGS không bằng không.** Đây là điểm mấu chốt và cũng là chỗ khác biệt lớn nhất so với lifetime deal của một phần mềm thuần. Mỗi lần một user LTD chạy transcription và gọi LLM, Castmagic **trả tiền thật**, mãi mãi, cho một khách đã trả tiền một lần duy nhất. 10.000 user LTD là một **khoản nợ chi phí biến đổi vĩnh viễn** trên bảng cân đối.
3. **Cách họ giảm thiểu — và đây là chi tiết đáng học nhất:** họ định giá subscription **có cap usage**, và:

> *"Chúng tôi **luôn phân tích số tiền đang chi cho LLM và transcription**, đảm bảo có đủ biên để biện minh cho đầu ra mà chúng tôi giao cho khách. Và đến giờ vẫn giữ được cân bằng."*

**Rút gọn thành quy tắc:** *lifetime deal cho sản phẩm AI chỉ an toàn khi bạn có usage cap.* Không có cap, một cú LTD thành công là một cách phá sản chậm. Đây là thứ tôi khuyên bạn ghi lại nếu định làm AppSumo với app AI.

4. **Nhóm khách LTD lệch khỏi ICP.** Người mua trên AppSumo là dân săn deal, không phải khách doanh nghiệp trả $99/tháng. Phản hồi từ họ có giá trị nhưng **thiên lệch** — họ nhạy giá cực đoan và không đại diện cho tệp khách trả tiền định kỳ.

**So sánh trong kho:** cùng họ "một cú nổ ra mắt" với [Floga kiếm $120K trong 24 giờ](../2026-03-29_my-app-made-120k-in-24-hours/case.md) và [SuperGrow kiếm $65K trong 3 ngày](../2025-09-10_how-i-made-65k-in-3-days/case.md). Điểm chung: một cú nổ ban đầu **không phải doanh thu, nó là ngân sách marketing tự tài trợ**. Điểm khác: Castmagic đổi lấy một nghĩa vụ phục vụ vĩnh viễn.

![Ra mắt một AI app](screenshots/03_02m54s_ch-launching-an-ai-app.jpg)

## 4. Cỗ máy creator/affiliate — playbook cụ thể nhất video ⭐⭐⭐

Sau AppSumo, kênh tăng trưởng chính là mạng lưới creator. Ramon mô tả rất cụ thể, đây gần như là một quy trình có thể chép nguyên:

> *"Thứ nữa hiệu quả rất tốt với chúng tôi là **creator**. Chúng tôi bắt đầu tạo động lực cho người ta làm nội dung trên mạng xã hội — một số người chúng tôi trả tiền, một số người chúng tôi tiếp cận để làm affiliate. Và một trong những cách tốt nhất là **scrape Instagram, scrape các nền tảng, tìm những công ty ở ngành liền kề, tra các hashtag đó, rồi build volume**. Khi đã có volume và có phản hồi, giờ **bạn có đòn bẩy để đàm phán giá**, rồi bắt đầu **trả theo CPM**, rồi quyết định ai đáng tài trợ, và tạo đủ volume để **kiểm tra xem đây có phải kênh khả thi cho mình hay không**."*

**Tách ra thành 6 bước:**

1. **Scrape** Instagram/các nền tảng theo hashtag của ngách và **ngành liền kề** (không chỉ ngách của bạn).
2. **Gửi số lượng lớn** — chấp nhận tỷ lệ phản hồi thấp.
3. **Xây volume phản hồi trước khi đàm phán** — đây là bước tạo đòn bẩy.
4. **Đàm phán giá dựa trên volume đó** (bạn có lựa chọn, nên có quyền mặc cả).
5. **Trả theo CPM** thay vì phí cố định ⇒ chi phí gắn với lượt xem thật.
6. **Đo rồi mới scale** — quyết định ai đáng tài trợ và kênh này có khả thi không.

**Vì sao bước 3 mới là mấu chốt** (Ramon nói lướt qua): nếu bạn chỉ tiếp cận 5 creator, bạn ở thế yếu và phải nhận giá họ đưa. Nếu bạn có 200 phản hồi, bạn có **thị trường** và giá rơi xuống. Đòn bẩy đàm phán trong influencer marketing là **hàm số của volume outreach**, không phải của kỹ năng thương lượng. Đây là insight thực dụng và ít ai nói.

**Và mẹo về ngành liền kề** cũng đáng nhớ: khách của Castmagic là podcaster, nhưng hashtag "podcast" thì cạnh tranh và đắt. Creator ở ngành liền kề (marketing, content, productivity, agency) có cùng khán giả với chi phí thấp hơn.

**Cảnh báo pháp lý cho người VN:** scrape Instagram vi phạm điều khoản dịch vụ của Meta và có thể khiến tài khoản bị khoá. Ramon nói ra rất thoải mái vì đó là chuẩn mực ở thị trường Mỹ, nhưng nó là rủi ro thật.

## 5. Marketing một người: nghiên cứu đối thủ + hệ thống hoá ⭐⭐

Pat hỏi làm sao vận hành marketing cho một business $120K MRR với **một người**. Hai câu trả lời:

**(1) Nghiên cứu ngược con đường của công ty tương tự:**

> *"Thứ mà người ta không làm đủ là **nghiên cứu**. Bạn thật sự có thể ngồi vẽ ra: **công ty này giống chúng tôi, phục vụ đúng tệp khách của chúng tôi — họ đã có phân phối bằng cách nào?** Trong trường hợp của tôi, tôi quay lại tìm những doanh nghiệp thật sự đã tăng trưởng bằng affiliate, rồi hỏi: làm sao tôi dựng một hệ thống ở đây?"*

**Đây là bước mà đa số bỏ qua và nó gần như miễn phí.** Thay vì tự nghĩ kênh nào hợp, hãy tìm 3–5 công ty đã bán cho **đúng tệp khách của bạn** và truy ngược kênh của họ (backlink, affiliate page, sponsor trên podcast/YouTube, ad library của Meta). Kênh nào chạy được cho họ là ứng viên tốt cho bạn — vì tệp khách quyết định kênh, không phải sản phẩm.

**(2) Biến việc lặp lại thành hệ thống — ví dụ cụ thể:**

> *"Ví dụ hữu hình: tôi thấy mình cứ qua lại với một loạt creator về việc **nghĩ ý tưởng nội dung**, và tôi nghĩ **cái này sẽ không scale được**. Nên tôi tạo hẳn **một tài liệu Notion đầy các concept** — giờ tôi không phải lên call với họ để brainstorm nội dung nữa. Nên rốt cuộc **tất cả quy về hệ thống**."*

**Cơ chế:** một người làm marketing cho $120K MRR chỉ khả thi nếu mỗi cuộc trao đổi lặp lại được thay bằng một tài liệu. Bài test rất đơn giản: *việc này tôi đã giải thích lần thứ ba chưa?* Nếu rồi, viết ra.

![Mẹo marketing khi làm một mình](screenshots/05_04m55s_ch-solo-marketing-hacks.jpg)

## 6. Tech stack: chọn Elixir để build 2 tuần ⭐⭐

> *"Tôi không thể nhấn mạnh đủ việc bạn phải **chấp nhận build một sản phẩm không hoàn hảo**. Một lựa chọn hơi phi truyền thống với nhiều người: tôi build cái này bằng **Elixir**. Nó rất ổn định, là ngôn ngữ scale rất tốt, và vì Elixir có công cụ tên là **Phoenix** và **LiveView**, bạn thật sự có thể build **toàn bộ front end và back end trong cùng một ngôn ngữ**."*

> *"Còn landing page thì chúng tôi làm bằng **Webflow** — dùng template là trông ổn ngay, nhờ đó cả đội dev dành toàn bộ thời gian cho **phần quan trọng nhất với người dùng, là sản phẩm**."*

| Hạng mục | Công cụ | Lý do |
|---|---|---|
| Toàn bộ app | **Elixir + Phoenix LiveView** | một ngôn ngữ cho cả FE và BE ⇒ không mất thời gian ghép API |
| Landing page | **Webflow** + template | tách hoàn toàn khỏi codebase, không tốn giờ dev |
| Xử lý nội dung | LLM API + dịch vụ transcription | chi phí biến đổi, được theo dõi sát |
| Vận hành creator | Notion | thay thế các cuộc gọi lặp lại |

**Bài học có thể mang đi ngay, kể cả nếu bạn không dùng Elixir:** hai quyết định giúp họ ra mắt trong 2 tuần đều là quyết định **loại bỏ việc**, không phải quyết định về công nghệ hay ho:
1. Chọn stack không phải viết hai lớp riêng (FE/BE) và không phải thiết kế API giữa chúng.
2. **Tách landing page ra khỏi codebase**, dùng template no-code. Đây là mẹo bị đánh giá thấp — rất nhiều dev đốt cả tuần làm marketing site trong Next.js trong khi Webflow/Framer xong trong một buổi chiều.

![Chiến lược giá](screenshots/07_07m00s_ch-pricing-strategy.jpg)

## 7. Định giá: thú nhận trung thực nhất video ⭐⭐

> *"Chúng tôi bán subscription theo tháng **có cap usage**. Buồn cười là **chúng tôi chỉ ném ra vài con số muốn thử và thấy nó chạy**."*

Không có mô hình định giá tinh vi nào. Nhưng phần thứ hai mới là phần nghiêm túc:

> *"Chúng tôi **luôn phân tích số tiền đang chi cho LLM và transcription**, đảm bảo có đủ biên để biện minh cho đầu ra mà chúng tôi giao, và đến nay giữ được cân bằng để **cả khách hàng lẫn chúng tôi cùng thắng**."*

**Đây là điều then chốt cho bất kỳ ai làm app AI:** giá khởi điểm cứ đoán cũng được, nhưng **biên gộp thì phải theo dõi liên tục**. Khác với SaaS thuần (COGS gần bằng 0, biên ~90%), app AI có COGS trôi theo hành vi user. Một khách dùng nhiều gấp 50 lần khách trung bình có thể ăn hết lợi nhuận của cả nhóm. **Usage cap là cơ chế bảo vệ, không phải chiêu bán hàng.**

So sánh: đây chính là điểm khác biệt cấu trúc giữa app AI và [SaaS thuần như Packager](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md), và là lý do bạn không thể chép nguyên bảng giá của SaaS thường sang app AI.

## 8. Vì sao Castmagic sống khi hàng nghìn AI app chết ⭐⭐⭐

Ramon đưa ba lý do, và cả ba đều kiểm chứng được trong chính video:

> *"Lý do chính tôi nghĩ Castmagic thắng là ba điều. **Một, chúng tôi giải quyết vấn đề của chính mình. Hai, chúng tôi xây thương hiệu bằng cách hợp tác với đúng creator. Ba, chúng tôi build và tiếp tục đầu tư vào sản phẩm để nâng chất lượng đầu ra.** Với một sản phẩm AI, cái quyết định không chỉ là nền tảng chạy thế nào, mà là **chất lượng đầu ra tôi nhận được là gì, và họ có đi tắt ở back end không** — rõ ràng là chúng tôi không."*

**Lý do thứ ba là lý do ít ai nói và đáng suy nghĩ nhất.** Với AI wrapper, cạnh tranh không diễn ra ở tính năng — ai cũng gọi cùng một model. Nó diễn ra ở **chất lượng đầu ra**: prompt engineering, chia nhỏ ngữ cảnh, hậu xử lý, chọn model theo tác vụ, và **chịu trả tiền cho model đắt hơn khi cần**. "Đi tắt ở back end" chính là dùng model rẻ hơn để tăng biên — người dùng cảm nhận được, và họ churn.

**Vậy hào của một AI wrapper là gì?** Ramon trả lời câu "nếu ChatGPT ra model mới và thay thế sản phẩm của anh thì sao":

> *"Chúng tôi đang giải quyết **vấn đề workflow** của mình, và luôn có cách tiếp tục tối ưu quy trình đó — đó không phải việc kinh doanh của ChatGPT. **ChatGPT ở đó để cung cấp hạ tầng. Họ có một feature, không phải một product.** Họ giải quyết một điểm đau nhỏ. Họ không giải quyết **cả một giải pháp mà chỉ một platform phủ workflow từ A đến Z mới giải được**."*

**Đánh giá thẳng thắn về lập luận này:** nó đúng một nửa và cần đọc thận trọng. Đúng ở chỗ: một workflow hoàn chỉnh (upload → transcribe → sinh nhiều định dạng đầu ra → chỉnh sửa → xuất bản) có nhiều điểm ma sát mà một chat interface không giải quyết được, và mỗi điểm là một lý do trả tiền. Nhưng lập luận này đã được **mọi** founder AI wrapper nói kể từ 2023, và trong hai năm sau video này, các nhà cung cấp model liên tục nuốt các workflow lân cận (upload file, xử lý dài, output có cấu trúc, agent, connector). **Hào thật của Castmagic không nằm ở lập luận này mà nằm ở hai thứ khác trong video:** thương hiệu và mạng lưới creator (khó sao chép) và net churn một chữ số (đã nhúng vào quy trình làm việc hằng tuần của khách).

**Với người VN:** đừng dùng lập luận "ChatGPT chỉ là feature" để tự trấn an. Hãy hỏi câu cụ thể hơn: *nếu OpenAI ra tính năng này native tháng sau, khách của tôi có còn lý do ở lại không?* Nếu câu trả lời chỉ là "vì UI của tôi đẹp hơn", bạn không có hào.

![ChatGPT có thay thế bạn không](screenshots/08_08m20s_ch-will-you-get-replaced-by-chatgpt.jpg)

## 9. Nguyên tắc tài chính: marketing luôn dưới 20% doanh thu ⭐⭐⭐

> *"Net churn ở mức **một chữ số** — điều đó quay lại giá trị của việc **giải quyết một vấn đề đang tồn tại chứ không tạo ra một thứ mới lạ**. Chúng tôi có hơn $120.000 MRR, đang tăng trưởng **hơn 20% tháng trên tháng**. Và tôi nghĩ một điều then chốt: **chúng tôi không chi quá 20% doanh thu cho marketing. Marketing luôn phải dưới 20%.** Lý do là vì **chúng tôi muốn kiếm tiền, chúng tôi muốn có lãi.**"*

**Đây là điểm đối lập trực tiếp và rất đáng đặt cạnh nhau trong kho:**

| | Castmagic | [ListKit](../2024-07-22_i-built-a-1m-saas-in-87-days/case.md) |
|---|---|---|
| MRR | $120K | $200K |
| Chi phí vận hành | marketing < 20% doanh thu, đội 3 người | $150–175K/tháng, đội 40 người |
| Ước tính biên | cao, có lãi rõ ràng | khoảng 12–25% |
| Kênh chính | creator/affiliate trả theo CPM | cold email + paid ads |
| Triết lý | tăng trưởng trong giới hạn lợi nhuận | mua tăng trưởng bằng ads và nhân sự |

**Cả hai đều "thành công" theo tiêu đề video, nhưng hai founder về nhà với số tiền rất khác nhau.** Điều kiện phân định: nếu kênh của bạn có **hiệu ứng tích luỹ** (nội dung creator sống mãi, SEO, affiliate) thì trần 20% khả thi và bạn nên áp. Nếu kênh của bạn **tắt tiền là tắt khách** (paid ads thuần), bạn buộc phải chi cao hơn để giữ tốc độ — và bạn đang mua tăng trưởng bằng lợi nhuận. Đây là lựa chọn chiến lược, không phải chuyện giỏi hay dở.

**Với indie hacker VN, quy tắc 20% là quy tắc đúng để bắt đầu**, vì bạn không có vốn để chịu lỗ trong lúc chờ LTV trả về.

![Hơn $120.000 MRR](screenshots/10_12m44s_usd-120-000-m.jpg)

## 10. Quá khứ VC và lý do lần này họ không gọi vốn ⭐⭐

Ramon tự nhận: *"Tôi sẽ làm poster boy chống VC."*

Lý lịch của anh:
- Công ty đầu tiên: từ seed tới Series C, **gọi hơn $80 triệu**.
- Công ty thứ hai: **Omnipanel**, được CRV rót, **seed $2,5 triệu**.
- **Trend.io** — *"tôi cố gọi vốn cho business đó gần 4 năm."*

> *"Lần này cảm giác rất khác. Cảm giác như **toàn bộ thời gian lẽ ra dành để nói chuyện với VC và giải thích tầm nhìn rộng lớn của sản phẩm, chúng tôi dành để nói chuyện với khách hàng và build thứ vớ vẩn cho chính mình mà rồi chính mình dùng.**"*

> *"**Đừng đi tìm sự xác nhận ở nơi khác.** Hãy build thứ khách hàng muốn, thứ họ sẵn sàng trả tiền, và thứ giải quyết vấn đề cho chính bạn."*

Và câu sắc nhất, về bản chất của việc gọi vốn:

> *"Nỗ lực để thật sự **giỏi việc gọi vốn — đó là một bộ kỹ năng riêng biệt**. Nếu bạn không giỏi việc xây dựng doanh nghiệp và tạo ra doanh thu, mà bạn lại chọn đi giỏi việc gọi vốn, thì **bạn đang làm ngược toàn bộ mọi thứ**."*

Anh vẫn để cửa mở: *"Rồi nếu bạn muốn nhận VC để tăng tốc, đó là tuỳ bạn."*

**Vì sao lời khuyên này đáng tin hơn bình thường:** nó không đến từ người chưa bao giờ gọi được vốn. Nó đến từ người đã gọi $80M+ và vẫn chọn con đường khác. Đây là kiểu bằng chứng khó bác bỏ nhất.

**Với người VN, điểm này còn quan trọng hơn:** hệ VC ở VN nhỏ và ưu tiên các mô hình local scale được, chứ hiếm khi rót cho micro-SaaS bán quốc tế. Bootstrapped không phải lựa chọn triết lý mà gần như là mặc định. Câu của Ramon là lời trấn an có căn cứ: **thời gian bạn không dùng để gọi vốn là thời gian bạn dùng để nói chuyện với khách hàng.**

## 11. Vận hành đội 3 người phân tán

- **Địa lý:** Ramon ở Fort Lauderdale, Blaine ở Miami, Justin ở Austin.
- **Nhịp:** phần lớn công việc **async** trong tuần.
- **Đồng bộ:** *"mỗi quý chúng tôi gặp nhau **ít nhất một tuần** để họp về tất cả những việc quan trọng."*
- **Standup:** **thứ Hai 30 phút** và **thứ Sáu 30 phút**. *"Chúng tôi thật sự cố chặn lịch để không bị kẹt trong các cuộc gọi cả ngày, mà tập trung vào **shipping**."*

> *"Không quan trọng bạn ở đâu, văn phòng ở đâu — hãy **tìm một nhóm người giỏi ở bất cứ đâu trên thế giới**, và đảm bảo là các bạn cũng gặp nhau để thật sự đồng bộ về những thứ cần xảy ra trong doanh nghiệp."*

**Về việc chọn co-founder,** Blaine nói một câu rất thẳng:

> *"Rất nhiều co-founder, nhất là lần đầu, hợp tác với người khác **vì tiện lợi cá nhân hoặc vì cần thiết, chứ không phải vì thật sự cùng chí hướng**. Thứ hai cực kỳ quan trọng là **kỹ năng bổ trợ nhau để mỗi người ở làn của mình** — một đội không giẫm lên chân nhau là điều rất lớn."*

Justin bổ sung: *"Chúng tôi rất **thành thật về thứ mình đang build** — không ngại nói: này, cái này chưa tốt như nó có thể tốt."*

Đây là **cùng bài học với đội co-founder của [ListKit](../2024-07-22_i-built-a-1m-saas-in-87-days/case.md)** — kỹ năng bổ trợ, không chồng lấn. Hai case độc lập, cùng kết luận: yếu tố quyết định của đội co-founder là **không giẫm chân**, không phải tình bạn.

![Ba founder](screenshots/06_06m13s_replay.jpg)

## 12. Cảnh báo thiên kiến nguồn ⚠️

1. **Không có bằng chứng số liệu.** Không có ảnh Stripe/dashboard trong toàn bộ video. Mọi con số — $120K MRR, 20% MoM, net churn một chữ số, $350K AppSumo — đều là lời kể. Các số trên màn hình là overlay biên tập.
2. **Con số AppSumo mập mờ.** "$350.000 in revenue generated" không nói rõ gross hay net về tay founder. Marketplace giữ một tỷ lệ đáng kể.
3. **Chi phí của lifetime deal bị lướt qua hoàn toàn.** 10.000 user LTD trên một sản phẩm có COGS theo token là một khoản nghĩa vụ vĩnh viễn. Video chỉ nói về mặt được.
4. **Mâu thuẫn 9 tháng so với 10 tháng** giữa mô tả, lời dẫn và lời founder.
5. **Chỉ phỏng vấn người thắng.** Cùng thời kỳ đó có hàng nghìn AI app cho podcast ra đời và chết. Không có mẫu đối chứng. Câu "vì sao chúng tôi thắng" của Ramon là **giải thích hậu nghiệm** — mỗi lý do anh nêu cũng đúng với nhiều sản phẩm đã thất bại.
6. **Starter Story đã được HubSpot mua lại và bán khoá học (Starter Story Build).** Video 13 phút có hai đoạn quảng cáo lead magnet, và Pat kết bằng lời mời tham gia Starter Story.
7. **Tên sản phẩm bị ASR đọc sai nghiêm trọng** — "C magic", "Cass magic", "CM magic". Tên đúng lấy từ mô tả video: **Castmagic**. Họ của Justin không được nêu trong video nên tôi không ghi.

## 13. Áp dụng cho tôi (indie hacker VN)

**Sao chép được gì:**

- **Bộ lọc ý tưởng "painkiller trong một workflow sẵn có"** — không phải "AI làm được gì hay ho", mà "khâu nào trong một quy trình tôi đang làm hằng tuần đang tốn cả tiếng đồng hồ".
- **Deadline ép ra sản phẩm.** Họ có 2 tuần vì AppSumo đưa ngày. Bạn có thể tự tạo áp lực tương đương: chốt ngày ra mắt trên Product Hunt/AppSumo trước khi viết dòng code đầu.
- **Tách landing page khỏi codebase** — Webflow/Framer với template. Tiết kiệm hàng chục giờ dev, áp dụng được cho mọi dự án.
- **Quy trình creator/affiliate 6 bước** (mục 4) là thứ chép nguyên được, và trả theo CPM là mô hình chi phí an toàn cho người ít vốn.
- **Nghiên cứu ngược kênh phân phối của đối thủ** — miễn phí, làm được trong một buổi tối, và là bước đầu tiên nên làm trước khi chọn kênh.
- **Trần chi phí marketing 20% doanh thu** như một nguyên tắc cứng khi bootstrapped.
- **Usage cap bắt buộc cho mọi sản phẩm có COGS theo token.** Đây là điều quan trọng nhất về mặt kỹ thuật tài chính trong case này.
- **Mô hình async + gặp mặt theo quý + 2 standup 30 phút/tuần** cho đội phân tán.

**Rào cản thật:**

- **AppSumo không mở cửa cho tất cả.** Castmagic được **mời** vì mạng lưới sẵn có của ba founder trong hệ sinh thái startup Mỹ. Quy trình nộp hồ sơ công khai thì cạnh tranh gay gắt, yêu cầu sản phẩm hoàn thiện, hỗ trợ tiếng Anh, và tuân thủ các điều khoản hoàn tiền của marketplace. Đừng lập kế hoạch tài chính dựa trên "sẽ có cú AppSumo".
- **Lifetime deal là con dao hai lưỡi cực kỳ sắc với app AI.** 10.000 user dùng vĩnh viễn trên chi phí LLM là rủi ro sống còn nếu bạn không có cap và không có đội theo dõi biên gộp hằng tuần. Với vốn mỏng của một indie hacker VN, một cú LTD sai thiết kế có thể giết dự án.
- **COGS theo token + tỷ giá.** Bạn thu USD nhưng cũng trả USD cho OpenAI/Anthropic/transcription — điều này thực ra tốt (tự nhiên hedge). Vấn đề là **biên gộp thấp hơn SaaS thường rất nhiều**, nên đừng dùng các benchmark biên 90% để lập kế hoạch.
- **Cạnh tranh trong ngách repurpose nội dung đã cực kỳ đông** so với thời điểm video (giữa 2024). Cửa "làm show notes bằng AI" gần như đã đóng.
- **Rủi ro nhà cung cấp model.** Giá và chính sách của OpenAI/Anthropic thay đổi, và họ có thể ra tính năng nuốt sản phẩm của bạn. Đây là rủi ro nền tảng ở tầng sâu hơn cả App Store.
- **Kênh creator đòi giao tiếp tiếng Anh liên tục** — đàm phán giá, brief nội dung, theo dõi kết quả. Không phải kênh im lặng như SEO.
- **Scrape Instagram vi phạm ToS** và có thể mất tài khoản.

**Khi nào KHÔNG dùng mô hình này:**

- **Khi bạn không kiểm soát được chi phí biến đổi.** Nếu sản phẩm của bạn có COGS theo usage mà bạn chưa biết cách đặt cap, đừng chào lifetime deal, đừng chào gói unlimited, và đừng ra mắt trên marketplace săn deal.
- **Khi bạn cần một hào bền.** AI wrapper cho một tác vụ đơn lẻ là mô hình có tuổi thọ ngắn. Nếu bạn muốn thứ chạy 5 năm, hãy nhìn [SaaS B2B ngách chán](../2026-03-15_i-make-60k-month-from-the-most-boring-saas-on-the-in/case.md) — churn thấp vì gắn với quy trình doanh nghiệp, không vì chất lượng prompt.
- **Khi bạn làm một mình và không có mạng lưới.** Case này có 3 founder full-time, một lời mời AppSumo từ quan hệ sẵn có, và một podcast làm nguồn ý tưởng lẫn kênh. Bản một người sẽ chậm hơn nhiều lần.
- **Khi bạn muốn tăng trưởng nhanh bằng vốn.** Họ chọn ngược lại một cách có ý thức, và đó là lý do họ có lãi.

**Case liên quan trong kho:** [Jenni AI — playbook AI SaaS $10M](../2025-03-18_the-10m-ai-saas-playbook/case.md) · [Magai — AI app $100K/tháng](../2025-10-11_i-built-a-100k-month-ai-app/case.md) · [Neural Frames](../2025-07-30_my-ai-app-makes-100k-month/case.md) · [Floga — $120K trong 24 giờ từ một cú ra mắt](../2026-03-29_my-app-made-120k-in-24-hours/case.md) · [SuperGrow — $65K trong 3 ngày](../2025-09-10_how-i-made-65k-in-3-days/case.md) · [ListKit — đối cực về cấu trúc chi phí](../2024-07-22_i-built-a-1m-saas-in-87-days/case.md)

## Nguồn

- Video: <https://www.youtube.com/watch?v=b5JhfGHafZA> (13:40, đăng 22/06/2024, 134.078 view)
- [Transcript đầy đủ](transcript.md) · [Ảnh chụp](screenshots/)
- **Lưu ý ASR:** phụ đề đọc "Castmagic" thành "C magic", "Cass magic", "CM magic"; "MRR" thành "Mr"; "Omnipanel" thành "Omni panel"; "trend.io" thành "trend. iio"; "ChatGPT" thành "Chad GPT". Tên đúng lấy từ mô tả video và handle Twitter của founder.
