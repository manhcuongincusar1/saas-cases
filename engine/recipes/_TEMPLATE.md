---
id: s2-aso-keyword-gap          # <chiến-lược>-<tên-ngắn>, trùng tên tactic trong kb/vocab.yaml nếu có
strategy: S2                    # S1…S15 hoặc G1…G14, xem COOKBOOK.md
title: "Tên công thức"
label: auto                     # auto | chrome | manual (nhãn nặng nhất của cả công thức)
time: "≤1 giờ"                  # thời gian chạy một lượt
cost: "$0"
evidence: corpus                # corpus | external | none
signal_level_when_pass: 3       # phải KHỚP điều kiện QUA bên dưới; công thức grow ghi "—"
tools: []
status: draft                   # draft | tested | proven
---

> (Nếu bằng chứng founder mỏng hoặc chủ yếu từ host/expert: ghi một dòng nhãn ở đây.)

## Dùng khi
Một câu: tình huống nào thì chạy công thức này, tình huống nào thì chọn công thức khác.

## Đầu vào

## Các bước
Phần lõi (Dùng khi + Các bước + Quyết định) gọn khoảng một trang. Mỗi bước ghi nhãn `[auto]`, `[chrome]` hoặc `[manual]`; bước manual có link/câu tìm ghi sẵn, đếm cái gì, mẫu để dán (≤15 phút). Gắn với việc founder trong kho thật sự làm (tên founder/sản phẩm).
1. [manual] …

## Đầu ra
Mỗi ứng viên một dòng: ý tưởng · khách trả tiền · bằng chứng (link) · mức tín hiệu 0–8 · ghi chú. Tạo file ở `journey/ideas/` từ `_TEMPLATE.md`. (Công thức grow: "cách đo thành công".)

## Ngưỡng qua
Con số cụ thể. Ngưỡng nằm trong `VALIDATE.md` thì chỉ trỏ về. Ngưỡng không lấy từ kho: ghi "đề xuất, chưa có số của kho" ngay trong dòng.

## Thực tế của công thức này (từ kho; không phải "validate thì nhanh hơn")
Một đến ba câu diễn giải số (nói rõ phần "chỉ host" nếu đáng kể). Bảng số do `engine/scripts/build_recipe.py <id>` sinh từ `kb/data/kb.duckdb`:

<!-- stats:start -->
<!-- stats:end -->

## Bằng chứng từ kho
Câu **của host/expert** là lời khuyên; câu **của founder** là việc họ kể. Danh sách chọn ở `engine/evidence/<id>.picks.yaml` ({v: 6 ký tự đầu video_id, ts, use, who?}); bảng này tự sinh nguyên văn. Mỗi dòng phải đỡ trực tiếp một bước hoặc một bẫy; không câu cụt.

<!-- evidence:start -->
<!-- evidence:end -->

## Bẫy và phản ví dụ
Ít nhất một ví dụ thật. Nhắc "kho chỉ chứa người thắng" và số case; nếu chủ yếu host/expert thì nói thẳng ở đầu mục.

## Quyết định
**QUA** nếu … · **DỪNG** nếu … · **TEST THÊM** nếu …: test gì, tới ngày nào.

## Cho solo founder bán global (từ VN)
Chép được gì · rào cản thật (phân phối, cạnh tranh, kỹ năng, vốn, thanh toán/pháp nhân) · khi nào KHÔNG nên làm. Chỉ nhắc bối cảnh VN khi là rào cản/lợi thế thật.
