# Hướng dẫn chạy thực nghiệm Chương 3 (Gemini)

1. Cài thư viện: `pip install google-genai pymupdf matplotlib`
2. Lấy API key miễn phí tại https://aistudio.google.com/apikey
   - PowerShell: `$env:GEMINI_API_KEY="khóa_của_bạn"`
   - (tùy chọn) chọn mô hình: `$env:GEMINI_MODEL="gemini-..."` – mặc định `gemini-flash-latest`
3. Bỏ 9 file PDF chuẩn vào `de_thi/`, đặt tên đúng: D25-MH, D25-G1..G4, D26-G1..G4 (.pdf)
4. Với từng đề:
   - `python gemini_tn_thpt.py convert D25-G1` → tạo `data/D25-G1.json`
   - MỞ file JSON, đối chiếu với PDF (dấu, số mũ, cận, tọa độ, đơn vị, has_figure/page, topic), sửa lỗi, đổi `"verified": true`
   - `python gemini_tn_thpt.py template D25-G1` → điền đáp án chính thức vào `dap_an/D25-G1.json`
5. Giải: `python gemini_tn_thpt.py solve all` (bị ngắt thì chạy lại, câu đã xong sẽ được bỏ qua)
6. Chấm: `python gemini_tn_thpt.py score` → `ket_qua/ket_qua.md` có sẵn Bảng 3.14–3.22 khớp với báo cáo,
   cùng các hình fig_3_2 … fig_3_5 và Bảng C.1–C.9 cho Phụ lục C.
7. Mở `nhan_loi.csv`, điền mã lỗi E1–E9 cho các câu sai (đọc lời giải trong `ket_qua/chi_tiet_tung_cau.csv`, cột summary), chạy lại `score` để có Bảng 3.21, 3.22.

Ghi mã mô hình thật (dòng "Mô hình ghi nhận trong phản hồi" ở đầu ket_qua.md) và ngày chạy vào Bảng 3.3.
