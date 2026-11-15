# Hướng dẫn chạy thực nghiệm Chương 3 (Gemini)

## Chuẩn bị (1 lần)
1. `pip install google-genai pymupdf matplotlib`
2. Đặt API key (lấy tại https://aistudio.google.com/apikey):
   - PowerShell: `$env:GEMINI_API_KEY="khóa_của_bạn"`
   - (tùy chọn) đổi mô hình: `$env:GEMINI_MODEL="gemini-..."`

## Chạy TỪNG ĐỀ (khuyên dùng)
```
python gemini_tn_thpt.py run D25-MH
```
- Giải 22 câu của đúng 1 đề rồi chấm luôn. Kết quả nằm ở `ket_qua/D25-MH/ket_qua.md`
  (Bảng C.x cho Phụ lục C và các bảng 3.14–3.22 của riêng đề đó). Màn hình in sẵn dòng tóm tắt:
  số câu đúng / tỷ lệ / điểm.
- Bị lỗi hay ngắt giữa chừng: chạy lại **đúng lệnh đó**. Các câu đã có kết quả sẽ được bỏ qua.
- Muốn chấm lại một đề đã giải, không gọi Gemini: `python gemini_tn_thpt.py score D25-MH`

Thứ tự 9 đề: D25-MH, D25-G1, D25-G2, D25-G3, D25-G4, D26-G1, D26-G2, D26-G3, D26-G4

## Tổng hợp sau khi chạy xong các đề
```
python gemini_tn_thpt.py score
```
→ `ket_qua/TONG_HOP/ket_qua.md`: Bảng 3.14–3.22 cho Chương 3 cùng Hình 3.2–3.5 (file png).
Chưa chạy đủ 9 đề thì bảng tổng hợp chỉ tính các đề đã có.

## Nhãn lỗi (Bảng 3.21, 3.22)
Mở `nhan_loi.csv` và điền cột `ma_loi` (E1–E7) cho các câu sai. Lời giải của Gemini nằm ở cột
`summary` trong `ket_qua/.../chi_tiet_tung_cau.csv`. Điền xong thì chạy lại `score`.
E8/E9 được gán tự động.

Ghi mã mô hình thật (dòng "Mô hình ghi nhận trong phản hồi" ở đầu ket_qua.md) và ngày chạy vào Bảng 3.3.
