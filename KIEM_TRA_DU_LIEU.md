# Nhật ký kiểm tra và sửa dữ liệu (15/11/2026)

Đối chiếu 9 file JSON đề và 9 file đáp án với PDF đề, với bảng đáp án chính thức năm 2025 và 2026
(mã đề 0101–0104 ứng với G1–G4) và với ảnh đáp án đề tham khảo 2025. Toàn bộ câu Phần II và
Phần III được giải lại để kiểm tra đáp án có khớp với nội dung đề trong JSON hay không.

## Đã sửa
- D25-G1 II.2 b: «$k = -\frac{\ln 2}{6}$» → «$k = \frac{\ln 2}{6}$»
- D25-G1 II.3 b: «\frac{z}{\sqrt{2}}» → «\frac{z}{2}»
- D25-G1 II.3 c: «\beta = 2$» → «$\beta = 2$»
- D25-G1 II.3: «trong đó \beta là» → «trong đó $\beta$ là»
- D25-G2 II.4 b: «\frac{z}{\sqrt{2}}» → «\frac{z}{2}»
- D25-G2 II.4 c: «\beta = 3$» → «$\beta = 3$»
- D25-G2 II.4: «trong đó \beta là» → «trong đó $\beta$ là»
- D25-G3 II.4 c: «\beta = 2$» → «$\beta = 2$»
- D25-G3 II.4: «trong đó \beta là» → «trong đó $\beta$ là»
- D25-G4 II.2 c: «\beta = 3$» → «$\beta = 3$»
- D25-G4 II.2: «trong đó \beta là» → «trong đó $\beta$ là»
- dap_an D25-G1 I.1: A → C
- D26-G2 II.4 b: «z = 3 \end{cases}» → «z = 0 \end{cases}»
- D26-G4 II.4 b: «z = 3 \end{cases}» → «z = 0 \end{cases}»
- D26-G4 III.6: «\text{Thứ Bảy} & 50 & 20 & 20» → «\text{Thứ Bảy} & 50 & 30 & 20»
- D26-G3 II.1 c: «là 100 mét» → «là 50 mét»
- D26-G3 III.5: «$R(x) = 90x$» → «$R(x) = 60x$»
- D26-G3 III.6: «đến hàng phần mười» → «đến hàng phần trăm»
- dap_an D26-G2 II.4 b: → Sai
- dap_an D26-G4 II.4 b: → Sai
- dap_an D26-G3 II.1 c: → Đúng
- data D26-G1..G4: verified false → true
## Lý do
- Đề 2025 (D25-G1, D25-G2): lúc chuyển PDF sang JSON, Gemini chép sai đề (dấu của k; z/2 bị chép
  thành z/√2). Đã đối chiếu với ảnh trong PDF gốc.
- Đáp án D25-G1 câu I.1 phải là C (bảng chính thức mã 0101; BA + A'C' = BA + AC = BC).
- PDF đề 2026 mã 0102–0104 là bản gõ lại (Loigiaihay), có lỗi gõ khiến nội dung đề mâu thuẫn với
  đáp án chính thức của Bộ. Ví dụ: với R(x) = 90x thì đáp số không phải 1990; với bí xanh 20 kg thì
  đáp số không phải 1350. Đã sửa đề cho khớp với đáp án chính thức.
- Lỗi $ không đóng quanh \beta: sửa để LaTeX hiển thị đúng.
- D26-G1..G4 đổi `verified` thành true; nếu không, lệnh solve sẽ bỏ qua các đề này.
