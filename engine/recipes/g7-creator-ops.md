---
id: g7-creator-ops
strategy: G7
title: "Làm việc với người để tạo và phân phối nội dung (creator, UGC, clipper, agency, influencer): tuyển, chọn, duyệt, trả, quản, giữ, và quyết định có thuê hay không"
label: manual                  # nhắn tin, phỏng vấn, chốt giá, duyệt video bằng tay; agent chỉ giúp lập danh sách và bảng chi
time: "1 ngày dựng danh sách, brief và mẫu tin; 14–30 ngày chạy một nhóm thử 3–5 creator (đề xuất, chưa có số của kho)"
cost: "$500–3.000 cho tháng đầu một nhóm thử (tính lại từ số founder nêu, xem mục dự toán; không phải số của kho)"
evidence: corpus
signal_level_when_pass: —      # grow không chuyển ứng viên lên thang 0–8; kết quả là "cách đo thành công" (xem mục Đầu ra)
tools: []
status: draft
---

> **Đây là công thức TỐN TIỀN và tốn công quản người; người dùng chọn organic, nên nó là tuỳ chọn và chỉ làm sau khi tự mình đã có một format organic thắng** (xem Điều kiện trước). Bằng chứng gồm cả founder lẫn host/expert: 38/223 step là lời host, và nhiều người trong số đó (Sideshift, Noise, agency UGC, v.v.) đang bán đúng dịch vụ này, xem mục Bẫy.

## Dùng khi
Đã có một format organic do chính mình đăng và đo được người trả tiền, nhưng mình không thể đăng đủ nhiều video/tài khoản một mình, nên muốn trả người làm lại đúng format đó. Nếu chưa có format thắng, quay về `g3-organic-content-formats`; nếu chỉ trả tiền cho nền tảng quảng cáo, dùng `g6-paid-ads`; nếu là vòng mời bạn trong sản phẩm, `g10-referral-viral-loop`.

## Điều kiện trước (đọc trước khi chi đồng nào)
Thứ tự founder nói trong kho: tự làm trước, thuê sau. Jay (Nomad Table) chỉ bắt đầu thuê creator sau khi chính anh đã làm viral được; Gleam tự làm nội dung để biết thế nào là tốt rồi mới thuê agency hoặc growth operator; Stronger không dùng agency để tìm format, chỉ dùng khi đã có format thắng; ở Pingo, ba tháng đầu hai founder chủ yếu tự làm video, chỉ thử một hai influencer, tới 20k MRR; Glam Up tự warm up 3 tài khoản rồi thuê dần lên khoảng 30–40 creator; Social Wizard tự đăng để tìm format rồi mới giao cho creator (6 case full, câu truy vấn: `engine/recipes/g7-creator-ops.extra.sql`, mục 7, đọc tay từng step). Host Joseph Choi nói thêm: cần format thắng trước khi thêm creator, và chỉ chi thêm khi video của creator kéo được người trả tiền (lời host; bảng bằng chứng). Ngược lại, 7 case full kể điều không thành khi thuê quá sớm hoặc sai người: NaturalWrite, Savewise (300–400 tin nhắn cho influencer, 1 hồi âm), Abmax (UGC trả tiền trước khi có format thắng, margin 5–10%, founder tự nhận là sai lầm lớn), Prayer Lock, Massive, Push Scroll, và Symmetry (thử influencer không hiệu quả rồi chuyển sang UGC). Điều kiện này không có số ngưỡng trong kho; "đã có format thắng" của người này là "người trả tiền thật", của người khác chỉ là "view".

## Đầu vào
Một sản phẩm đã có đường từ video tới tiền đo được (paywall, mã giảm giá, UTM), một hoặc nhiều video organic của chính mình đã có số, một khoản tiền thử mình chấp nhận mất, và thời gian nhắn tin và duyệt video mỗi ngày.

## Các bước
1. **[manual] Kiểm điều kiện trước:** ≥1 format organic do chính mình đăng đã mang người trả tiền. Chưa có thì dừng.
2. **[manual] Chọn mô hình: creator nhỏ làm lại format của mình, không phải influencer lớn.** Host Joseph Choi nói hai dấu hiệu chiến lược sẽ flop là thuê influencer lớn trả nhiều tiền và copy trend chỉ để lấy view. Wrestle AI giữ khoảng 10 creator và không mở tới 100; Coconote giữ 10–12 người part-time; Pingo khoảng 100 creator rồi cắt 30–50 người.
3. **[chrome] Lập danh sách 30 creator (số 30 là đề xuất, chưa có số của kho).** Jenni AI xem thẳng video của họ, không xem follower; Studyfetch chọn theo engagement (bình luận, lưu) chứ không theo view hay follower; Boot.dev hỏi chính khách hiện có họ xem và nghe ai (founder nói đây là cách hiệu quả nhất của họ).
4. **[manual] Nhắn tin ngắn, chữ thường, kèm bằng chứng.** Jenni AI viết giọng casual kèm một bằng chứng về sản phẩm và creator đã làm được; Wrestle AI và Locked mở đầu bằng "paid promo?" để nói ngay là có trả tiền, và Locked mời gọi điện chứ không đàm phán trong tin nhắn; Jenny AI báo kỳ vọng hơn 50% không trả lời và theo dõi lại sau vài ngày.
5. **[manual] Phỏng vấn 15 phút và cho một video thử trả tiền.** Sprout phỏng vấn mỗi creator khoảng 15 phút để xem có nghiêm túc không; Halo AI cho mỗi người làm 5 video trong khoảng 5 ngày, $20 một video ($100 một creator), không đặt ngưỡng view tối thiểu mà đánh giá sự đều đặn, giao tiếp và cảm giác viral; Pep AI bắt đầu hợp đồng thử 1 tháng (4 bài, 4 story, link trong bio) khoảng $200 cho creator ~5.000 view mỗi bài.
6. **[manual] Gửi brief một trang, video mẫu và hook; gửi hợp đồng và duyệt bài trước khi đăng.** Noise đưa sẵn ý tưởng, kịch bản, slide và caption để creator chỉ việc đăng; Boost App Social gửi creator tài liệu A4 gợi ý hook và trigger; Locked yêu cầu app xuất hiện trong 15 giây đầu và duyệt bài trước khi đăng.
7. **[manual] Chốt một kiểu trả giá** (mục con B): phí cố định theo video, CPM có sàn view, hoặc retainer cộng thưởng. Locked tính CPM từ RPM của chính app (2–3 USD) rồi chỉ chốt ở CPM thấp hơn mức đó.
8. **[manual] Chạy nhóm thử 3–5 creator trong 14–30 ngày (cỡ nhóm và thời gian là đề xuất, chưa có số của kho; Host Sideshift nói mất 2–3 tuần mới có format thắng, Prayer Lock mất 14 ngày mới có một video ~20K view).** Ghi từng creator vào một bảng (ngày đăng, view, người trả tiền). Pingo theo dõi phễu bằng CRM; Halo AI cho mỗi creator một kênh Discord riêng.
9. **[manual] Đọc kết quả bằng người trả tiền, không bằng view; cắt đáy, giữ nhóm giữa và đỉnh.** Pingo: nhóm 20–30% tốt nhất tạo gần hết view, phần đáy là chi tiêu chết (bảng bằng chứng).
10. **[manual] Nhân format thắng, giữ nhóm nhỏ.** Chỉ cân nhắc thuê người quản lý khi có hơn 10 creator (host SuUJgm nói retainer $2–4k/tháng cho người quản lý đầu tiên, số của người bán nền tảng).

## Các mục con (nhóm theo từ khoá trên step; các nhóm chồng lấn; số là case full)
Trong 223 step, nhóm theo từ khoá trên mô tả, ghi chú, chi phí và ngưỡng của step: A (tìm, lọc, tiếp cận, tuyển) 65 step, 33 case full; B (trả tiền và cấu trúc deal) 124 step, 54 case full; C (brief, duyệt, đào tạo, quản, giữ) 72 step, 30 case full; D (nhân bản format đã thắng, quy mô) 67 step, 31 case full; E (thuê hay không, thất bại, agency, tự làm, đối tác) 40 step, 27 case full. Một step có thể nằm trong nhiều nhóm; câu truy vấn: `engine/recipes/g7-creator-ops.extra.sql`, mục 3.

### A. Tìm, lọc, tiếp cận, tuyển (33 case full)
- **Nguồn creator:** DM Instagram/TikTok (Wrestle AI 100 DM mỗi ngày; Locked cao điểm 500 DM mỗi ngày với giới hạn khoảng 100 DM mỗi tài khoản mỗi ngày; Push Scroll khoảng 2.000 DM chốt 5–6 influencer); email hàng loạt (Boost App Social dùng 1.000 Gmail, mỗi cái khoảng 10 email/ngày, ~100 USD trả trước mỗi creator, founder tự nhận hơi black hat và vài creator nhận tiền rồi bỏ đi); form nhận đơn (Halo AI đăng nhóm Facebook và Reddit nhận khoảng 500–600 hồ sơ; Photogenic nhận ~600 ứng viên qua Sideshift và chọn 1); chợ creator hoặc sinh viên (Handshake, Sideshift, Upwork ở Arvow); giới thiệu (Coconote).
- **Cách lọc:** chất lượng nội dung hơn số follower (Bloom qua agency Pebble; Studyfetch); người từng có một video viral (Pingo, micro dưới 10k follower; Gleam; Photogenic); ba tiêu chí biểu cảm, khung hình đầu, hướng ngoại và kể chuyện giỏi (Jenni AI); trần view, không phải trung bình: có ít nhất một hai video hàng triệu view và kiểm tra video tài trợ có flop không (Jenny AI).
- **Số founder nêu cho nhóm này:** Jenni AI từ 0 lên 150 creator và 75M view trong khoảng 3 tháng (tuyển 80 creator trong tháng đầu, mục tiêu đặt trước); Savewise 300–400 tin nhắn cho influencer lúc sản phẩm còn thô chỉ được 1 hồi âm; Cal AI (do Alfie, nhân viên marketing, kể) dùng khoảng 25 trợ lý, mỗi người ~100 lời mời mỗi ngày, đã liên hệ ~220.000 creator, quy mô ngoài tầm solo.
- **Quyết định mục con:** làm tay 30 creator trong 1–2 ngày trước khi nghĩ tới trợ lý hay công cụ (Pingo mới chuyển sang VA sau khi founder đã tự làm). Ngưỡng 30 là đề xuất, chưa có số của kho.

### B. Trả tiền và cấu trúc deal (54 case full)
Đếm theo từ khoá trong 68 case full: phí cố định theo video hoặc bài 17 case; CPM 15; equity hoặc chia sở hữu 7; affiliate hoặc hoa hồng 7; thử trước (video test, gói thử, trả trước) 5; retainer 4; chia doanh thu hoặc lợi nhuận 4; sàn view hoặc minimum view clause 4 (thô, chồng lấn; câu truy vấn mục 4).

**Số tiền do founder nêu** (một case, một con số; tự khai, không có dashboard):

| Kiểu trả | Case | Số founder nêu |
|---|---|---|
| Phí cố định theo video | Flame | $1 cho video 60 giây (UGC Đông Âu và Nga trên chợ freelance) |
| Phí cố định theo video | Social Wizard | khoảng $120 cho một video, video đạt 2 triệu view |
| Phí cố định theo video | Methods | $40 cho video đầu tiên của mỗi người dùng mới |
| Phí cố định theo video | Career Hound | không quá $20 mỗi video |
| Phí cố định + CPM theo mốc | Sprout | 10–30 USD mỗi bài, cộng CPM giảm dần (10k view khoảng 40 USD, 1 triệu view khoảng 800 USD) |
| Phí cố định + CPM theo mốc | Gleam | $10–25 mỗi video cộng thưởng CPM |
| Retainer + CPM theo mốc | Bloom | retainer $500–1.000/tháng cộng CPM $2–4 ở mốc 10k, 50k, 100k view; từ 100k view khoảng $1.000 mỗi video |
| Trả theo view qua nền tảng | Cardstock | khoảng $2.600 cho hơn 7.000 bài một tháng, CPM ~$1–2 (nền tảng giữ một nửa) |
| CPM nhắm tới | Copia | khoảng $1 CPM, creator 50k–250k follower |
| Trả trước + bảo đảm view | Wrestle AI | 20–50% trả trước cho 4–5 video, CPM $2–5, bảo đảm 100K view |
| Sàn view | Cal AI | sàn 800.000 view khi creator tự nhận ~1 triệu |
| Minimum view clause | Locked | $500 cho tối thiểu 500.000 view; +$500 nếu đạt 1 triệu view; CPM $1–2 |
| Flat nhiều video | Push Scroll | khoảng $800 cho 4 video mỗi deal; nhiều video chỉ 200–500 download |
| Gói thử | Pep AI | $200/tháng, creator ~5.000 view mỗi bài |
| Trả theo bài của influencer | Postiz | 60–350 USD mỗi bài |
| Bài tài trợ của trang lớn | Chatbase | khoảng 4.000 USD một bài (ước lượng của founder) |
| Influencer trả theo hợp đồng | Brawler | khoảng $4.500 cho 3 video, thu lại ~75% |
| Rev share | Calbuddy | chia doanh thu; sau khi đã có ~20K/tháng đàm phán tốt hơn, tránh chia 50/50 từ đầu |
| Chia gần nửa doanh thu | Symmetry | gần 50% doanh thu cho creator để họ ở lại lâu dài |
| Equity | Fitted | $20/video trước, sau đó rev share, rồi equity khi đóng góp nhiều hơn |
| Affiliate trọn đời | Lancer | 30% trọn đời nếu coach chốt và onboard khách; 20% nếu chỉ giới thiệu |
| Lương nội bộ | Jenny AI | ~$2.000/tháng cộng thưởng cho UGC trong nhà; influencer làm UGC $3.000–5.000/tháng |
| Vay vốn | Halo AI | $100.000 vay cá nhân dồn vào trả creator sau khi một video cho ROI 6x |

Số **do host hoặc người bán nền tảng nêu** (không gộp với số founder): DcDOgW (podcast Superwall) $30–40 mỗi video bậc thấp và $80–100 bậc cao, thưởng thêm $500–1.000 khi video nổ; Canyon (Sideshift) mô hình lai $15–20 mỗi video kèm retainer cơ bản (câu ở bảng); Nick Lawton (Sideshift) retainer ~600 USD và CPM 1–2 USD; Drew Levin (Sideshift) retainer khoảng $800/tháng cho 60 video; SuUJgm khoảng $15 mỗi video ở LATAM so với $25 ở Mỹ.

- **Hai điểm hay lặp:** (1) tính giá từ giá trị mỗi lượt tải của mình (Locked: CPM thấp hơn RPM; Noise: tự báo ~$0,30/install, chưa kiểm chứng); (2) retainer nhỏ cho giai đoạn đầu vì chỉ CPM thì creator bỏ cuộc (Bloom).
- **Quyết định mục con:** bắt đầu bằng gói thử giá cố định rẻ ($100–200 mỗi creator như Halo AI, Pep AI), chưa ký retainer. Ngưỡng này là đề xuất, chưa có số của kho.

### C. Brief, duyệt, đào tạo, quản, giữ (30 case full)
- **Đào tạo và duyệt:** Glam Up và Sprout làm khoá học riêng cho creator (module video, quiz cuối mỗi module, Typeform nối CRM; người học đăng viral sau khoảng 2 tuần); Jenni AI nói một creator chưa từng làm UGC mất 25 video mới vượt 10k view; Sideshift (host) khuyên duyệt từng video giai đoạn đầu bằng checklist ánh sáng, nhịp nói, hook; warm-up tài khoản 3–5 ngày (Sideshift host; Push Scroll 3–4 ngày).
- **Quản đội:** Nomad Table tự quản 60–70 creator qua nhóm WhatsApp và nhắn riêng; Coconote giữ 10–12 creator part-time và một content coach cho mỗi 12 creator; Pingo coi danh mục creator như VC (top 20–30% tạo gần hết view, cắt đáy); Halo AI tự động gửi video viral cho toàn bộ creator trong Discord để quay lại cùng ngày.
- **Giữ người:** Gleam giữ bằng quan hệ chứ không bằng giá (nhóm chat khi còn ít, Discord khi mở rộng) và trả theo đợt sau mỗi 10 video để giữ cam kết; Nomad Table tính view bài cũ thêm khoảng 3 tháng trước khi trả, mỗi tháng một lần; Bro lúc đỉnh có khoảng 50 creator rồi nhiều người ngừng đăng, còn 10–20.
- **Quyết định mục con:** nếu một creator không đăng đủ lịch sau 2 tuần thì cắt và thay người (đề xuất, chưa có số của kho).

### D. Nhân bản format đã thắng, quy mô (31 case full)
Social Wizard giao cho micro-streamer ngách khác làm lại đúng format; Bloom 5–10 tài khoản có sẵn follower mỗi tài khoản khoảng 2 bài/ngày, bài viral thì nhân ra khoảng 20 tài khoản; Jenny AI khoảng 5 tài khoản, tổng ~15 video mỗi ngày làm lại video viral; Payout điều phối 5 creator đăng cùng một ngày: doanh thu ngày đó $9.700 và app lên top ngành tài chính trên App Store; Symmetry đăng gần 80.000 video qua hơn 500 tài khoản trong một năm (gần 8 tỷ lượt xem). Host Sideshift đề xuất chia 90% creator đăng format thắng, 10% thử format mới. Một lưu ý của host trong video Cal AI: 2.000+ influencer không có nghĩa hàng nghìn creator 0 follower cho cùng kết quả.
- **Quyết định mục con:** sau khi một format thắng, nhân bằng cách đưa đúng video mẫu cho 3–5 creator (đề xuất, chưa có số của kho); không mở rộng tới trăm người khi chưa đo được người trả tiền.

### E. Thuê hay không: tự làm, agency, đối tác (27 case full)
- **Tự làm hay thuê agency:** host Joseph Choi (người bán cộng đồng có phí) nói ở mức $0/tháng không nên thuê agency, và kể một founder đốt 30.000 USD/tháng cho agency có case study tốt nhưng không đồng bộ động lực rồi thất bại (lời host kể lại, không có tên). Stronger chỉ dùng agency để scale khi đã có format thắng.
- **Đối tác thay vì trả tiền:** Wrestle AI có đồng sáng lập là influencer đấu vật; Payout làm cùng một influencer và Casper nói muốn chia equity cho người làm phần nội dung để mình giữ phần phân phối; Abmax chia equity cho một influencer thể hình lớn để có content và ads gần như không mất tiền trả creator (sau đó cắt mọi deal UGC và influencer, dồn tiền vào Meta Ads); Influencer Game Company chia 50% quyền sở hữu game cho influencer. Các câu này là lời của người bán mô hình hoặc kể lại; bằng chứng về kết quả thắng/thua dài hạn không có.
- **Thuê một người nội bộ:** Cardstock thuê một người quen làm TikTok; Jenny AI trả ~$2.000/tháng cho UGC trong nhà.

## Dự toán thô (tính lại từ số founder nêu; không phải số của kho)
| Kịch bản tháng đầu | Cách tính | Ghi chú |
|---|---|---|
| 5 creator, mỗi người 5 video thử | 5 × ($20 × 5 video = $100) = $500 | $100 mỗi creator là số của Halo AI; nhân 5 là suy ra |
| 3 creator theo retainer + CPM | 3 × ($500–1.000) = $1.500–3.000, chưa kể CPM $2–4 theo mốc | retainer là số của Bloom; nhân 3 là suy ra |
| Gói thử một creator ~5.000 view mỗi bài | $200/tháng (Pep AI) | số của một case |
| Một deal CPM có sàn | $800 ứng với sàn 400.000–800.000 view (Locked) | số của một case |
| Số do người bán nền tảng nêu | $2.000–4.000 cho đợt 30–60 video tháng đầu (Nick Lawton, Sideshift) | số của bên bán, coi là trần tham khảo |
| Lời khuyên founder | vài nghìn USD nếu thuê hơn 1–2 creator (Gleam) | một founder |

Mục tiêu của khoản này là trả lời "creator làm lại format của mình có kéo được người trả tiền không", không phải để có doanh thu. Tổng gợi ý $500–3.000 cho tháng đầu một nhóm 3–5 creator là suy ra, **đề xuất, chưa có số của kho**.

## Đầu ra
Cách đo thành công (grow không chuyển ứng viên lên thang 0–8): bảng "creator theo tháng": mỗi dòng một creator gồm ngày tuyển, kiểu trả, tổng chi, số video đăng, view, số lượt dùng thử, số người trả tiền, giữ hay cắt. Đây là đầu vào của `g8-funnel-measurement`.

## Ngưỡng qua
Không lấy từ kho. Đề xuất, chưa có số của kho: sau 30 ngày với nhóm thử, ≥1 video của creator kéo được người trả tiền (không chỉ view) và tổng chi mỗi người trả tiền thấp hơn giá trị khách; chỉ trỏ: nếu mục tiêu là xác nhận có người trả tiền, quay về `VALIDATE.md` (cổng 1–4, thang 0–8) chứ không dùng bảng này.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
<!-- stats:start -->
| Số đếm | Giá trị |
|---|---|
| Step mang tactic này | 223 step trong 90 video |
| Case (video, case) có step này | 88, trong đó 68 case full (founder kể kỹ) |
| Step không gắn case cụ thể (phần lớn là host/expert mô tả; có thể gồm lời founder nói chung) | 38/223 |
| Nhóm "giống user": case full không nêu cả audience, vốn, network, thành công trước | 42/68 |
| Case full không nêu existing_audience | 61/68 |
| Case full video không kể bằng chứng nhu cầu trước launch | 38/68 |
| Tháng tới mức doanh thu hiện tại (trung vị, p25–p75) | 9.0 tháng (4.8–24.0), n=40 |
| Kênh scale trả tiền / thuần organic / không nêu | 37 / 31 / 0 |

*"Không nêu" ≠ "không có". Một founder kể hai sản phẩm đếm là 2 case. Câu truy vấn: `engine/recipes/g7-creator-ops.sql` (chạy lại bằng `engine/scripts/recipe_stats.py`).*
<!-- stats:end -->
Theo `community_insider` trong 68 case full: 36 là người trong cuộc, 11 ghi rõ **outsider** (không phải người trong cuộc), 21 không nêu; đừng gộp 11 và 21. Step phân bố 200 ở chặng grow, 22 ở launch, 1 ở scale; 83 step từ video 2025, 140 từ video 2026. Theo kênh video: podcast Superwall 139 step (47 video, 29 step chỉ host), Starter Story 79 step (42 video, 9 chỉ host), Starter Story Build 5 step (1 video). Cột "kênh scale trả tiền" ở trên tính cả `influencer_paid`, nên với công thức này nó không nói trả tiền có hơn organic hay không. Chỉ 38/223 step là lời host, nhưng 33 step (18 trong số đó chỉ host) nằm ở 8 video mà bias nêu công ty bán nền tảng hoặc dịch vụ creator, UGC hay phân phối (Sideshift, Noise, Pebble, Clover, EVO Marketing); video Arcads (kênh jason-lee, có tài trợ Arcads) không có step g7 nào trong kho, nên bias của Arcads không ảnh hưởng đến công thức này.

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Các dòng của người bán nền tảng creator (Sideshift) và nhân viên marketing đang tuyển người được gắn nhãn trong cột cuối.

<!-- evidence:start -->
| Ai · video · mốc | Nguyên văn | Dùng cho |
|---|---|---|
| Jay (Nomad Table) (founder) · `2026-02-23_copy-this-ugc-strategy-itll-make-your-app-go-vir` · 00:53:52 | "once I can go viral myself, then I can hire creators because if I just hire them now, like there's no point" | founder kể: chỉ thuê creator sau khi chính mình làm viral được; thuê sớm hơn thì không có ý nghĩa (điều kiện trước của công thức) |
| Joseph Choi (host/expert) · `2026-10-11_start-1m-app-from-scratch` · 00:07:03 | "The important thing is to have a winning format before you bring on more creators because that way you've got all the tested information at hand." | lời khuyên của host (video là kịch bản giả định): cần format thắng trước khi thêm creator, để có sẵn thông tin đã kiểm |
| Joseph Choi (host/expert) · `2026-10-11_start-1m-app-from-scratch` · 00:07:41 | "However, if one creator is getting a lot of views, but I'm not getting any paying users, there's no point in spending money there." | lời khuyên của host: chỉ chi thêm cho creator khi video của họ kéo được người trả tiền; nhiều view mà không có người trả tiền thì không đáng |
| Morrie (Pingo) (founder) · `2026-04-19_how-i-built-a-500kmo-ai-app-so-you-can-just-copy` · 00:19:01 | "And that for the first 3 months, we had like one or two actual influencers we tried, but it was mainly just Michael and I making videos till like 20k MRR, just the two of us." | founder kể: ba tháng đầu chỉ thử một hai influencer, chủ yếu hai founder tự làm video tới 20k MRR |
| Joseph Choi (host/expert) · `2026-09-23_1000-hours-profitable-apps` · 00:14:12 | "Cuz if you're at $0 a month, you shouldn't be hiring an agency." | lời khuyên của host (người bán cộng đồng có phí): ở mức doanh thu $0 không nên thuê agency |
| Evan (Locked) (founder) · `2026-04-01_im-14-and-i-built-a-14k-month-app` · 04:10 | "I realized my RPM was around 2 to 3 dollars, so I knew I had to close creators at a CPM lower than that." | founder kể: tính ngưỡng CPM từ RPM của chính app (2–3 USD) rồi chỉ chốt creator ở CPM thấp hơn mức đó |
| George (Wrestle AI) (founder) · `2026-10-12_ex-wrestler-41k-ai-apps` · 00:28:58 | "We never scaled crazy hard on Wrestle AI. We never had 100 creators. We always had roughly 10." | founder kể: giữ khoảng 10 creator, không bao giờ mở tới 100 |
| Morrie (Pingo) (founder) · `2026-04-19_how-i-built-a-500kmo-ai-app-so-you-can-just-copy` · 00:24:44 | "The top 20-30% of creators are doing most of the views. The bottom percent are doing none of them and they're kind of dead spend." | founder kể: nhóm 20–30% creator tốt nhất tạo gần hết view, phần đáy là chi tiêu chết nên cắt |
| Canyon (Sideshift) (host/expert) · `2025-07-17_the-secret-behind-weirdly-viral-apps` · 00:14:01 | "We kind of recommend like a hybrid model. So $15 to $20 per video with a base retainer is is pretty common." | lời khuyên của người bán nền tảng creator (có động cơ bán hàng): mô hình lai $15–20 mỗi video kèm retainer cơ bản là phổ biến |
| Alfie Dickens (Cal AI) (host/expert) · `2026-08-25_marketing-genius-cal-ai` · 00:46:54 | "now even creators that get like 5,000 views every video or 10,000 views every video already have an agent." | bẫy (nhân viên marketing, không phải founder): creator 5.000–10.000 view mỗi video cũng đã có người đại diện, nên giá và đường tiếp cận tăng |
| David Park (Jenny AI) (founder) · `2025-03-18_the-10m-ai-saas-playbook` · 26:56 | "the good news is that you only need one amazing influencer to make up for all the losses of the previous 10 influencer Partnerships" | founder kể: chỉ cần một influencer xuất sắc là bù được lỗ của mười đợt hợp tác trước |
| Kieran (StudyFetch) (host/expert) · `2026-05-24_the-exact-system-to-go-from-0-10m-with-your-app` · 00:01:03 | "UGC is becoming less and less effective because audiences are starting to understand that the videos that they're watching are straight-up ads." | bẫy (marketing đang tuyển người): UGC kém hiệu quả dần vì khán giả nhận ra đó là quảng cáo |
| Casper (Payout) (founder) · `2026-03-15_the-stupid-simple-content-strategy-thats-making-` · 00:07:38 | "I'd rather partner with someone, give up some equity, and have them handle that whole side while I handle the whole distribution side." | founder kể: chọn chia equity cho đối tác làm phần nội dung, mình giữ phần phân phối (Casper bán mô hình này nên có động cơ) |
| Nikita (NaturalWrite) (founder) · `2025-09-06_our-simple-app-made-100k-in-90-days` · 10:21 | "Try find out what works and only then start thinking about uh delegate or hiring" | founder kể: tìm ra cái gì chạy được rồi mới nghĩ tới giao việc hay thuê người (NaturalWrite từng thuê influencer và thất bại) |
<!-- evidence:end -->

## Bẫy và phản ví dụ
- **Kho chỉ chứa người thắng.** 68 case full dùng g7 và đủ thành công để lên kênh; 37 trong số đó có kênh trả tiền ở giai đoạn scale (cột này tính cả `influencer_paid`). Người thuê creator rồi mất tiền không có mặt, trừ những người kể lại điều không thành (7 case full ở mục Điều kiện trước).
- **Influencer trả tiền có thể không ra kết quả.** NaturalWrite thử thuê influencer làm video: ít view, gần như không chuyển đổi (câu của Nikita ở bảng nói tìm ra cái chạy được rồi mới giao việc). Massive trả retainer hàng tháng và nói thất bại vì ít chuyển đổi; Push Scroll chốt 5–6 influencer theo deal flat 4 video nhưng nhiều video chỉ 200–500 download.
- **Creator giỏi nhanh được đại diện và giá tăng.** Alfie (Cal AI, nhân viên marketing) nói creator 5.000–10.000 view mỗi video cũng đã có người đại diện (câu ở bảng); theo anh, tin nhắn đầu xin gọi điện thường bị bỏ qua và gọi điện tăng khoảng 10 lần cơ hội ký deal tốt, tức đường tới creator có đại diện khác hẳn DM tới creator nhỏ.
- **Creator nhỏ làm việc không đều.** Bro lúc đỉnh ~50 creator rồi còn 10–20; Boost App Social có vài creator nhận trả trước rồi bỏ đi; Jenni AI nói một creator chưa làm UGC mất 25 video mới vượt 10k view.
- **UGC có thể kém hiệu quả dần.** Kieran (StudyFetch, marketing đang tuyển người) nói khán giả bắt đầu hiểu video họ xem là quảng cáo; Cal AI (Alfie) nói UGC rẻ view hơn nhưng có thể chuyển đổi thấp vì thiếu độ tin của influencer nổi tiếng. Nick Lawton nói UGC do AI tạo tốt cho view ảo và dở cho chuyển đổi, nhưng ông là đồng sáng lập một nền tảng bán creator UGC.
- **Bias người bán.** Sideshift (Canyon, Nick Lawton, Drew Levin, 4 video: `_a4ch3`, `qnDdab`, `F2dVvz`, `SuUJgm`) bán nền tảng creator UGC: mọi khuyến nghị của họ dẫn tới thuê nhiều creator có trả phí; mô hình lai $15–20 mỗi video kèm retainer là mức giá "phổ biến" theo lời người bán, và việc các brand lớn có CPM dưới 90 cent là lời của Drew Levin, không kiểm chứng. Nick Weber (Noise) quảng bá nền tảng của chính mình, nên $0,30 mỗi lượt cài là số tự báo. Podcast Superwall (139/223 step) do công ty bán paywall tài trợ và host bán cộng đồng Consumer Club: nhiều app chi tiền thì họ có lợi. Casper (Payout) là creator bán mô hình chia equity cho creator. Step của host Starter Story (ví dụ nền tảng `make ugc.ai`, `creator.io`) là tên công cụ, không có số.
- **Tự thuê một đội ở ngoài tầm solo.** Cal AI: đội ~25 trợ lý và ~220.000 creator được liên hệ; Symmetry: gần 80.000 video và hơn 500 tài khoản. Hai ví dụ này nói về quy mô người thắng lớn nhất, không phải bước đầu của solo.

## Quyết định
- **QUA** (mở rộng nhóm creator) nếu sau 30 ngày với nhóm thử, ≥1 video của creator kéo được người trả tiền và CPM thực thấp hơn RPM của app (cách Locked tính; ngưỡng đề xuất, chưa có số của kho). Khi mở rộng, thêm từng 3–5 creator một lần và giữ nhóm nhỏ (Wrestle AI ~10, Coconote 10–12).
- **DỪNG** nếu chưa có format organic thắng ở bước 1, hoặc sau 30 ngày chi hết ngân sách thử mà 0 video của creator mang người trả tiền (đề xuất, chưa có số của kho): quay về `g3-organic-content-formats` và đăng thêm bằng chính mình. Đừng thêm tiền để "học".
- **TEST THÊM** nếu creator đăng đều nhưng view thấp: đổi hook hoặc brief (không đổi giá), thử ngách khác (Jenni AI xem creator ở ngách làm đẹp, lifestyle), chạy lại 14 ngày với 3 creator mới.

## Cho solo founder bán global (từ VN)
- **Chép được:** bước 3–9 làm từ xa bằng DM và email. Creator ở nước khác có sẵn: nhóm UGC Đông Âu ($1 mỗi video ở Flame) hay LATAM rẻ hơn Mỹ ($15 so với $25 theo host Sideshift) cho thấy giá linh hoạt, nhưng creator phải nói được ngôn ngữ và văn hoá khách (Halo AI sàng người ở Mỹ hoặc dùng VPN Mỹ; Pingo thử creator người học ngôn ngữ).
- **Rào cản thật:** (1) vốn: $500–3.000 tháng đầu là một phần lớn runway; (2) thanh toán: trả creator ở Mỹ/EU qua PayPal, Wise hoặc nền tảng, và nếu thu USD ngoài store: Stripe thường không mở cho pháp nhân VN (`VALIDATE.md`, mục rào cản VN): dùng merchant-of-record (Polar, Lemon Squeezy, Paddle...) và kiểm điều kiện nhận seller ở VN trước khi chọn; App Store/Play thì đã thu hộ; (3) quản người nhiều múi giờ, creator Mỹ thường làm việc theo giờ Mỹ; (4) tiếng Anh bản xứ cho brief và đàm phán (Locked và Wrestle AI mời gọi điện chốt deal); (5) tài khoản TikTok và Instagram dùng để warm-up cần giữ sạch; (6) mục tiêu mặc định của người dùng là organic, nên đây chỉ là bước sau khi tự có format thắng.
- **KHÔNG nên làm** nếu chưa có format organic thắng đo bằng người trả tiền; nếu vốn chỉ vài trăm USD (tự đăng thêm video bằng chính mình, như Pingo ba tháng đầu); nếu chưa đo được từ video tới người trả tiền; nếu khách không xem video ngắn; hoặc nếu mình không có thời gian trả lời và duyệt mỗi ngày (Sideshift host: tuyển creator là việc tốn giờ nhất trong chương trình).
