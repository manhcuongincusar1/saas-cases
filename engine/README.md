# engine — cookbook tìm ý tưởng $1k MRR trong 1 tháng

> **Giai đoạn hiện tại: CHƯNG CẤT video của 2 kênh thành cookbook. Chưa tìm ý tưởng.** Phần "Giao thức cho agent" bên dưới là thiết kế cho giai đoạn sau, chưa chạy cho tới khi tôi bảo.
> Bản nháp, cập nhật 16/11/2026. Cho AI agent **hoặc** cho tôi: mở `COOKBOOK.md`, chọn công thức theo tình huống, chạy, ra quyết định.
> Công thức được chưng cất từ Superwall + Starter Story (câu trích nguyên văn có mốc giây ở `evidence/`), không viết từ kiến thức chung.
> Nơi nào chưa có case thì ghi rõ "chưa có case kiểm chứng".

## Bốn thư mục, bốn việc

```
engine/            CÁCH LÀM — cookbook + công thức + công cụ (thư mục này)
kb/                BẰNG CHỨNG — video đã phân tích, câu trích nguyên văn (kb/videos/…), check.py kiểm
journey/           CỦA TÔI — bản đồ hành trình (MAP.md), ứng viên và ý tưởng (ideas/)
VALIDATE.md        4 cổng + thang tín hiệu 0–8 (engine không viết lại ngưỡng, chỉ trỏ về đây)
```

## Giao thức cho agent

Đầu vào: một câu mục tiêu, mặc định là "ý tưởng sản phẩm $1k MRR, solo, bán global (US/UK/CA/AU/EU), founder ở VN" (kho không có số đo trực tiếp cho "trong 1 tháng"; xem `COOKBOOK.md`) cộng với một **ngách hoặc cụm từ gợi ý** nếu có.

1. Đọc `COOKBOOK.md`. Chọn **2–3 chiến lược** hợp điều kiện (xem cột "hợp khi" và "thời gian").
2. Với mỗi chiến lược, mở các công thức trong `recipes/` và **chạy phần có nhãn `auto`**: chạy hết, đừng dừng chờ.
3. Gom mọi bước có nhãn `manual` thành **một danh sách duy nhất** (mỗi mục: link hoặc câu tìm kiếm ghi sẵn, đếm cái gì, mẫu để dán kết quả lại, ≤15 phút) rồi **hỏi tôi một lần**.
4. Mỗi ứng viên tìm được: tạo một file trong `journey/ideas/` từ `_TEMPLATE.md`, `status: inbox`, kèm link bằng chứng và `demand_signal.level` (thang 0–8 của `VALIDATE.md`).
5. Cuối mỗi công thức, ghi **một trong ba quyết định**: `QUA` · `DỪNG` · `TEST THÊM` (test gì, tới ngày nào).
6. Có danh sách ứng viên thì trình tôi. **Không sang cổng 3 (build/chi tiền/đăng ra ngoài) khi tôi chưa duyệt.**

Những việc agent **không** tự làm: tiêu tiền, đăng bài ra ngoài, tạo tài khoản, xoá thật, bắt đầu build. Gom thành danh sách cho tôi duyệt.

## Nhãn của công thức

| Nhãn | Nghĩa |
|---|---|
| `auto` | agent chạy được bằng script/API công khai |
| `chrome` | agent chạy được qua Chrome (claude-in-chrome) nhưng chậm hơn, có thể bị chặn vùng |
| `manual` | tôi phải tự mở (Reddit chặn agent; TikTok khoá theo vùng khi mở từ VN) |
| bằng chứng `corpus` | có founder/host trong Superwall + Starter Story đã làm, câu trích ở `evidence/` |
| bằng chứng `external` | lấy từ tài liệu công cụ/tra cứu web, **chưa có case kiểm chứng** trong kho |
| bằng chứng `none` | mới là ý tưởng, chưa có nguồn |

## Hiện trạng (cập nhật 16/11/2026)

Giai đoạn vẫn là **chưng cất, chưa tìm ý tưởng**. Đã xong:

1. 210 video (Starter Story + Superwall 2025+, cộng một video ngoài hai kênh) trong `kb/videos/`; DB sinh ra `kb/data/kb.duckdb` (`python3 -I kb/scripts/build.py`; đừng sửa tay).
2. **3 chương, 29 công thức** trong `recipes/` (12 tìm ý tưởng, 4 validate, 13 grow), mỗi chương có trang "Thực tế" ở `chapters/` (FIND, VALIDATE, GROW). Trang đầu để đọc là `COOKBOOK.md`.
3. Mỗi công thức có bảng số tự sinh từ DB (`python3 -I engine/scripts/build_recipe.py <id>`; câu truy vấn lưu cạnh công thức: `recipes/<id>.sql`, `.extra.sql`) và bảng câu trích nguyên văn (sinh từ `evidence/<id>.picks.yaml`). Kiểm: `python3 -I engine/scripts/check_recipes.py`.
4. Một chiến thuật thành công thức khi có **≥3 founder độc lập** làm; ít hơn thì ở `kb/frameworks/candidates.md` hoặc ghi nhãn "mỏng". Không viết `s6-upwork-demand` (chưa có founder nào xác nhận).

Ba điều đọc kèm mọi con số: kho chỉ chứa người thắng; "không nêu" không có nghĩa "không có"; kho không đo mốc $1k MRR (xem `COOKBOOK.md`, mục "Đọc trước").

Công cụ trong `tools/` (`topgrossing.py`, `kw.py`, `autofill.py`, `reviews.py`) và lần chạy thử ở `journey/runs/2026-11-15-1k-search/` thuộc giai đoạn tìm ý tưởng, **tạm gác** cho tới khi user cho phép.
