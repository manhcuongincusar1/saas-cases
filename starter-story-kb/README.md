# Starter Story — Knowledge Base cho Indie Hacking

Kho nghiên cứu case study từ kênh YouTube [Starter Story](https://www.youtube.com/@starterstory) — **180 video, 45,6 giờ, 45,7 triệu lượt xem** — được thu thập và phân tích để phục vụ đúng ba việc: **tìm ý tưởng · validate · go-to-market**.

---

## Bắt đầu từ đâu

| Anh đang ở đâu | Đọc gì trước |
|---|---|
| **Chưa có ý tưởng** | [`playbooks/01-tim-y-tuong.md`](playbooks/01-tim-y-tuong.md) → rồi [Tone Adapt](videos/2026-06-14_the-first-app-i-ever-built-makes-25k-month/case.md), [Profit AI](videos/2026-06-24_i-turned-this-spreadsheet-into-a-30k-month-micro-saa/case.md) |
| **Có ý tưởng, chưa biết đúng sai** | [`playbooks/02-validate.md`](playbooks/02-validate.md) → khung **VSC** ở [Flame](videos/2026-06-21_i-built-a-10k-month-app-with-this-one-system/case.md) |
| **Đã build mà không ai mua** | [72 app, $0 doanh thu](videos/2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/case.md) — đọc trước tiên |
| **Có sản phẩm, cần khách** | [`playbooks/03-go-to-market.md`](playbooks/03-go-to-market.md) → [Kleo](videos/2026-01-11_how-my-app-hit-60k-month-in-2-months/case.md), [Chart Detector](videos/2026-07-23_i-make-50k-per-month-working-5-hours-a-week/case.md) |
| **Muốn xem tất cả** | [`index.md`](index.md) — case đã phân tích · [`videos/README.md`](videos/README.md) — toàn bộ 180 video |

---

## Cấu trúc

```
starter-story-kb/
├── index.md              ← Bảng tra case đã phân tích: doanh thu, mô hình, kênh, độ sao chép
├── README.md             ← File này
├── build_index.py        ← Chạy lại sau khi thêm/sửa case: dựng lại index + videos/README + CSV
├── reorganize.py         ← Script gom dữ liệu vào từng thư mục video (đã chạy)
├── playbooks/            ← Đúc kết xuyên suốt nhiều case
├── data/cases.csv        ← Dữ liệu phẳng để query bằng DuckDB
├── _raw/meta/            ← Metadata JSON gốc (nguồn cho script)
│
└── videos/               ← MỘT VIDEO = MỘT THƯ MỤC
    ├── README.md                     ← Danh sách toàn bộ 180 video
    ├── 2026-08-30_the-insanely-.../  ← đặt tên theo ngày đăng + tiêu đề
    │   ├── README.md       ← Tóm tắt, link video, SỐ LIỆU BẮT ĐƯỢC, chapters, danh sách ảnh
    │   ├── case.md         ← Phân tích đầy đủ (chỉ ở video đã phân tích sâu)
    │   ├── transcript.md   ← Transcript gốc có timestamp
    │   ├── meta.json       ← Metadata gốc
    │   └── screenshots/    ← Ảnh 720p, tên theo timestamp + nội dung
    └── ... (180 thư mục)
```

**Mọi thứ của một video nằm cùng một chỗ** — không phải đi tìm ảnh ở thư mục này, transcript ở thư mục kia.

Với **163 video chưa phân tích sâu**, `README.md` trong thư mục vẫn có mục **"Số liệu bắt được từ transcript"** — các đoạn founder nhắc con số, kèm timestamp để tua thẳng tới đó trong video. Đủ để lướt nhanh và quyết định video nào đáng đào sâu.

---

## Cấu trúc một file case

Mỗi case có **frontmatter YAML** (để query) + phần phân tích. Các mục cố định:

1. **Con số** — doanh thu, chi phí, giá, chỉ số vận hành
2. **Sản phẩm giải quyết vấn đề gì**
3. **Ý tưởng đến từ đâu** ⭐
4. **Cách validate** ⭐
5. **Go-to-market** ⭐
6. **Mô hình kiếm tiền & giá**
7. **Tech stack & chi phí**
8. **Bài học & trích dẫn**
9. **Áp dụng cho tôi (indie hacker VN)** — sao chép được gì, rào cản thật, biến thể đáng thử

Phần 9 là phần tôi viết thêm, không có trong video: đánh giá thẳng thắn về **ARPU thấp ở VN, thanh toán quốc tế, rủi ro pháp lý, dòng tiền** — và khi nào **không nên** sao chép một mô hình.

**Hai trường để lọc nhanh:**
- `replicability_vn: 1-5` — mức độ sao chép được ở điều kiện Việt Nam
- `difficulty: 1-5` — độ khó thực thi

---

## Query bằng DuckDB

```bash
cd ~/Desktop/SAAS/starter-story-kb

# Case dễ sao chép nhất ở VN, sắp theo doanh thu
duckdb -c "SELECT product, revenue_usd_month, model, main_channel
           FROM read_csv('data/cases.csv')
           WHERE replicability_vn >= 4 AND difficulty <= 3
           ORDER BY revenue_usd_month DESC"

# Doanh thu trung bình theo mô hình kinh doanh
duckdb -c "SELECT model, count(*) n, round(avg(revenue_usd_month)) avg_rev
           FROM read_csv('data/cases.csv') GROUP BY model ORDER BY n DESC"

# Case vốn khởi đầu thấp
duckdb -c "SELECT product, revenue_usd_month, opex_usd_month, team_size
           FROM read_csv('data/cases.csv')
           WHERE opex_usd_month < 500 ORDER BY revenue_usd_month DESC"

# Tìm theo chủ đề
duckdb -c "SELECT product, tagline FROM read_csv('data/cases.csv')
           WHERE tags LIKE '%programmatic-seo%'"
```

Sau khi thêm hoặc sửa case: `python3 build_index.py` để dựng lại `index.md` và `data/cases.csv`.

---

## Cách kho này được xây

| Bước | Công cụ | Kết quả |
|---|---|---|
| Lấy danh sách video | `yt-dlp --flat-playlist` | 180 video |
| Tải transcript + metadata | `yt-dlp --write-auto-subs --sub-format json3` | 179 transcript, 180 meta |
| Chọn mốc chụp ảnh | Script Python chấm điểm theo **heatmap most-replayed** + **chapter** + **câu nhắc con số $** | ~9 mốc/video |
| Trích ảnh | `yt-dlp -f bv[height<=720]` + `ffmpeg -ss` | 1.622 ảnh |
| Gom về từng thư mục video | `reorganize.py` | 180 thư mục |
| Phân tích | Đọc transcript, viết `case.md` | 17/180 xong |

Một video (`hCvy-Rt7Naw`) không có auto-caption nên không có transcript.

---

## Lưu ý về nguồn

Đây là **tài liệu nghiên cứu cá nhân**. Các file `case.md` và `playbooks/` là **phân tích và đúc kết của riêng tôi**, có trích dẫn ngắn và dẫn nguồn tới video gốc — không phải bản sao nội dung. Transcript thô (`transcript.md` trong mỗi thư mục video) là dữ liệu nguồn để tra cứu.

Toàn bộ số liệu doanh thu đều theo lời founder kể trên video (thường có show dashboard). Trường `revenue_basis` trong mỗi case ghi rõ con số đó là **MRR, doanh thu tháng, hay tổng tích luỹ** — vì các founder dùng lẫn lộn ba khái niệm này.

**Thiên lệch cần nhớ khi đọc:** đây là kênh phỏng vấn **người thành công**. Không có case thất bại nào ngoài [Starter Story Challenge](videos/2026-08-22_he-built-100-apps-and-made-0-can-he-fix-it-in-30-day/case.md). Với mỗi founder $100K/tháng ở đây, có hàng nghìn người làm đúng như vậy mà không có kết quả. Hãy đọc để lấy **cơ chế**, đừng đọc để lấy **kỳ vọng**.
