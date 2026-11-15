# Kết quả thực nghiệm Gemini – 15/11/2026 21:15
Mô hình ghi nhận trong phản hồi: gemini-3.6-flash

## Bảng 3.14. Kết quả tổng hợp
| Chỉ số | Kết quả |
|---|---|
| Số câu đúng / tổng số câu | 18 / 22 |
| Tỷ lệ đúng trên tổng số câu (3.1) | 81,8 % |
| Số mệnh đề Đúng/Sai xác định đúng | 16 / 16 |
| Điểm trung bình (thang 10) | 8,75 |
| Điểm cao nhất (mã đề) | 8,75 (D25-MH) |
| Điểm thấp nhất (mã đề) | 8,75 (D25-MH) |
| Số phản hồi lỗi định dạng hoặc kỹ thuật (E8, E9) | 3 |

## Bảng 3.15. Tỷ lệ đúng theo dạng bài
| Dạng bài | Đơn vị | Tổng số | Số đúng | Tỷ lệ đúng (%) | Điểm TB/đề | Điểm tối đa/đề |
|---|---|---|---|---|---|---|
| Nhiều lựa chọn | câu | 12 | 9 | 75,0 | 2,25 | 3,0 |
| Đúng/Sai (trọn câu) | câu | 4 | 4 | 100,0 | 4,00 | 4,0 |
| Đúng/Sai (theo mệnh đề) | mệnh đề | 16 | 16 | 100,0 | – | – |
| Trả lời ngắn | câu | 6 | 5 | 83,3 | 2,50 | 3,0 |
| Tổng (theo câu) | câu | 22 | 18 | 81,8 | 8,75 | 10,0 |

## Bảng 3.17. Kết quả chi tiết theo từng đề
| Mã dữ liệu | Nhiều lựa chọn (/12) | Đ/S mệnh đề (/16) | Đ/S trọn câu (/4) | Trả lời ngắn (/6) | Tổng câu đúng (/22) | Tỷ lệ đúng (%) | Điểm (/10) |
|---|---|---|---|---|---|---|---|
| D25-MH | 9 | 16 | 4 | 5 | 18 | 81,8 | 8,75 |
| TB 2025 | 9,0 | 16,0 | 4,0 | 5,0 | 18,0 | 81,8 | 8,75 |
| TB 1 đề | 9,0 | 16,0 | 4,0 | 5,0 | 18,0 | 81,8 | 8,75 |

## Bảng 3.16. Phân bố số mệnh đề xác định đúng trong mỗi câu Đúng/Sai
| Số mệnh đề đúng k | Số câu | Tỷ lệ (%) | Điểm g(k) |
|---|---|---|---|
| 0 | 0 | 0,0 | 0,00 |
| 1 | 0 | 0,0 | 0,10 |
| 2 | 0 | 0,0 | 0,25 |
| 3 | 0 | 0,0 | 0,50 |
| 4 | 4 | 100,0 | 1,00 |

## Bảng 3.18. So sánh kết quả theo năm và loại đề
| Nhóm đề | Số đề | Số câu | Số câu đúng | Tỷ lệ đúng (%) | Điểm TB | Thấp nhất | Cao nhất |
|---|---|---|---|---|---|---|---|
| Đề minh họa 2025 | 1 | 22 | 18 | 81,8 | 8,75 | 8,75 | 8,75 |

## Bảng 3.19. Tỷ lệ đúng theo mạch kiến thức
| Mạch kiến thức | Số câu | Số đúng | Tỷ lệ đúng (%) |
|---|---|---|---|
| Đại số và Giải tích | 12 | 9 | 75,0 |
| Hình học và Đo lường | 7 | 6 | 85,7 |
| Thống kê và Xác suất | 3 | 3 | 100,0 |
| Tổng | 22 | 18 | 81,8 |
| Trong đó: câu có hình vẽ | 6 | 4 | 66,7 |
| Trong đó: câu không có hình vẽ | 16 | 14 | 87,5 |

## Bảng 3.20. Thời gian xử lý và tài nguyên sử dụng
| Chỉ số | Giá trị |
|---|---|
| Tổng số yêu cầu đã gửi | 22 |
| Số yêu cầu lỗi API (E9) | 0 |
| Thời gian phản hồi trung bình (giây/câu) | 22,2 |
| Thời gian phản hồi lớn nhất (giây) | 206,6 |
| Token đầu vào trung bình/câu | 603,7 |
| Token đầu ra trung bình/câu | 257,7 |
| Tổng thời gian chạy 1 đề (phút) | 8,1 |

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
| E8 | Đầu ra | 3 | 75,0 |
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
| E8 | 2 | 0 | 1 | 3 |
| E9 | 0 | 0 | 0 | 0 |
| Tổng | 3 | 0 | 1 | 4 |

## Bảng C.1. Kết quả chi tiết từng câu – đề D25-MH
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | D | – | Sai | 0,00 | E8 |
| I.3 | NLC | TK-XS |  | A | A | Đúng | 0,25 |  |
| I.4 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT | x | B | C | Sai | 0,00 |  |
| I.6 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.7 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| I.8 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | HH-ĐL | x | D | D | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT | x | C | – | Sai | 0,00 | E8 |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: S, c: Đ, d: S} | {a: Đ, b: S, c: Đ, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL | x | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL |  | 4,9 | 4,9 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT | x | 43 | 43 | Đúng | 0,50 |  |
| III.3 | TLN | HH-ĐL |  | 3 | – | Sai | 0,00 | E8 |
| III.4 | TLN | ĐS-GT | x | 3200 | 3200 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 333 | 333 | Đúng | 0,50 |  |
| III.6 | TLN | TK-XS |  | 0,08 | 0,08 | Đúng | 0,50 |  |

> Còn 1 câu sai chưa gán nhãn lỗi – điền vào nhan_loi.csv rồi chạy lại.