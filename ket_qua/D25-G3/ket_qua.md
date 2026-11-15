# Kết quả thực nghiệm Gemini – 15/11/2026 21:53
Mô hình ghi nhận trong phản hồi: gemini-3.6-flash

## Bảng 3.14. Kết quả tổng hợp
| Chỉ số | Kết quả |
|---|---|
| Số câu đúng / tổng số câu | 18 / 22 |
| Tỷ lệ đúng trên tổng số câu (3.1) | 81,8 % |
| Số mệnh đề Đúng/Sai xác định đúng | 12 / 16 |
| Điểm trung bình (thang 10) | 7,75 |
| Điểm cao nhất (mã đề) | 7,75 (D25-G3) |
| Điểm thấp nhất (mã đề) | 7,75 (D25-G3) |
| Số phản hồi lỗi định dạng hoặc kỹ thuật (E8, E9) | 4 |

## Bảng 3.15. Tỷ lệ đúng theo dạng bài
| Dạng bài | Đơn vị | Tổng số | Số đúng | Tỷ lệ đúng (%) | Điểm TB/đề | Điểm tối đa/đề |
|---|---|---|---|---|---|---|
| Nhiều lựa chọn | câu | 12 | 11 | 91,7 | 2,75 | 3,0 |
| Đúng/Sai (trọn câu) | câu | 4 | 3 | 75,0 | 3,00 | 4,0 |
| Đúng/Sai (theo mệnh đề) | mệnh đề | 16 | 12 | 75,0 | – | – |
| Trả lời ngắn | câu | 6 | 4 | 66,7 | 2,00 | 3,0 |
| Tổng (theo câu) | câu | 22 | 18 | 81,8 | 7,75 | 10,0 |

## Bảng 3.17. Kết quả chi tiết theo từng đề
| Mã dữ liệu | Nhiều lựa chọn (/12) | Đ/S mệnh đề (/16) | Đ/S trọn câu (/4) | Trả lời ngắn (/6) | Tổng câu đúng (/22) | Tỷ lệ đúng (%) | Điểm (/10) |
|---|---|---|---|---|---|---|---|
| D25-G3 | 11 | 12 | 3 | 4 | 18 | 81,8 | 7,75 |
| TB 2025 | 11,0 | 12,0 | 3,0 | 4,0 | 18,0 | 81,8 | 7,75 |
| TB 1 đề | 11,0 | 12,0 | 3,0 | 4,0 | 18,0 | 81,8 | 7,75 |

## Bảng 3.16. Phân bố số mệnh đề xác định đúng trong mỗi câu Đúng/Sai
| Số mệnh đề đúng k | Số câu | Tỷ lệ (%) | Điểm g(k) |
|---|---|---|---|
| 0 | 1 | 25,0 | 0,00 |
| 1 | 0 | 0,0 | 0,10 |
| 2 | 0 | 0,0 | 0,25 |
| 3 | 0 | 0,0 | 0,50 |
| 4 | 3 | 75,0 | 1,00 |

## Bảng 3.18. So sánh kết quả theo năm và loại đề
| Nhóm đề | Số đề | Số câu | Số câu đúng | Tỷ lệ đúng (%) | Điểm TB | Thấp nhất | Cao nhất |
|---|---|---|---|---|---|---|---|
| Đề gốc 2025 | 1 | 22 | 18 | 81,8 | 7,75 | 7,75 | 7,75 |

## Bảng 3.19. Tỷ lệ đúng theo mạch kiến thức
| Mạch kiến thức | Số câu | Số đúng | Tỷ lệ đúng (%) |
|---|---|---|---|
| Đại số và Giải tích | 10 | 8 | 80,0 |
| Hình học và Đo lường | 8 | 7 | 87,5 |
| Thống kê và Xác suất | 4 | 3 | 75,0 |
| Tổng | 22 | 18 | 81,8 |
| Trong đó: câu có hình vẽ | 5 | 4 | 80,0 |
| Trong đó: câu không có hình vẽ | 17 | 14 | 82,4 |

## Bảng 3.20. Thời gian xử lý và tài nguyên sử dụng
| Chỉ số | Giá trị |
|---|---|
| Tổng số yêu cầu đã gửi | 22 |
| Số yêu cầu lỗi API (E9) | 0 |
| Thời gian phản hồi trung bình (giây/câu) | 12,6 |
| Thời gian phản hồi lớn nhất (giây) | 49,0 |
| Token đầu vào trung bình/câu | 558,0 |
| Token đầu ra trung bình/câu | 270,9 |
| Tổng thời gian chạy 1 đề (phút) | 4,6 |

## Bảng 3.21. Phân bố nhóm lỗi chính trong các câu trả lời sai
| Mã | Nhóm lỗi | Số câu | Tỷ lệ trên tổng câu sai (%) |
|---|---|---|---|
| E1 | Đọc dữ kiện | 0 | 0,0 |
| E2 | Đọc hình | 0 | 0,0 |
| E3 | Mô hình hóa | 0 | 0,0 |
| E4 | Kiến thức | 0 | 0,0 |
| E5 | Suy luận | 0 | 0,0 |
| E6 | Tính toán | 0 | 0,0 |
| E7 | Kết luận | 0 | 0,0 |
| E8 | Đầu ra | 4 | 100,0 |
| E9 | Kỹ thuật | 0 | 0,0 |
|  | Tổng | 4 | 100 |

## Bảng 3.22. Phân bố nhóm lỗi theo dạng bài
| Mã lỗi | Nhiều lựa chọn | Đúng/Sai | Trả lời ngắn | Tổng |
|---|---|---|---|---|
| E1 | 0 | 0 | 0 | 0 |
| E2 | 0 | 0 | 0 | 0 |
| E3 | 0 | 0 | 0 | 0 |
| E4 | 0 | 0 | 0 | 0 |
| E5 | 0 | 0 | 0 | 0 |
| E6 | 0 | 0 | 0 | 0 |
| E7 | 0 | 0 | 0 | 0 |
| E8 | 1 | 1 | 2 | 4 |
| E9 | 0 | 0 | 0 | 0 |
| Tổng | 1 | 1 | 2 | 4 |

## Bảng C.4. Kết quả chi tiết từng câu – đề D25-G3
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT |  | B | – | Sai | 0,00 | E8 |
| I.5 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.6 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.7 | NLC | TK-XS |  | B | B | Đúng | 0,25 |  |
| I.8 | NLC | HH-ĐL |  | D | D | Đúng | 0,25 |  |
| I.9 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT | x | D | D | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: S, d: Đ} | – | 0/4 | 0,00 | E8 |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: S, d: S} | {a: Đ, b: S, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | ĐS-GT |  | 1808 | 1808 | Đúng | 0,50 |  |
| III.2 | TLN | TK-XS |  | 2016 | 2016 | Đúng | 0,50 |  |
| III.3 | TLN | TK-XS | x | 3780 | – | Sai | 0,00 | E8 |
| III.4 | TLN | HH-ĐL |  | 2,08 | – | Sai | 0,00 | E8 |
| III.5 | TLN | ĐS-GT |  | 2150 | 2150 | Đúng | 0,50 |  |
| III.6 | TLN | HH-ĐL | x | 95,3 | 95,3 | Đúng | 0,50 |  |