# Kết quả thực nghiệm Gemini – 15/11/2026 22:02
Mô hình ghi nhận trong phản hồi: gemini-3.6-flash

## Bảng 3.14. Kết quả tổng hợp
| Chỉ số | Kết quả |
|---|---|
| Số câu đúng / tổng số câu | 16 / 22 |
| Tỷ lệ đúng trên tổng số câu (3.1) | 72,7 % |
| Số mệnh đề Đúng/Sai xác định đúng | 16 / 16 |
| Điểm trung bình (thang 10) | 7,50 |
| Điểm cao nhất (mã đề) | 7,50 (D26-G4) |
| Điểm thấp nhất (mã đề) | 7,50 (D26-G4) |
| Số phản hồi lỗi định dạng hoặc kỹ thuật (E8, E9) | 5 |

## Bảng 3.15. Tỷ lệ đúng theo dạng bài
| Dạng bài | Đơn vị | Tổng số | Số đúng | Tỷ lệ đúng (%) | Điểm TB/đề | Điểm tối đa/đề |
|---|---|---|---|---|---|---|
| Nhiều lựa chọn | câu | 12 | 10 | 83,3 | 2,50 | 3,0 |
| Đúng/Sai (trọn câu) | câu | 4 | 4 | 100,0 | 4,00 | 4,0 |
| Đúng/Sai (theo mệnh đề) | mệnh đề | 16 | 16 | 100,0 | – | – |
| Trả lời ngắn | câu | 6 | 2 | 33,3 | 1,00 | 3,0 |
| Tổng (theo câu) | câu | 22 | 16 | 72,7 | 7,50 | 10,0 |

## Bảng 3.17. Kết quả chi tiết theo từng đề
| Mã dữ liệu | Nhiều lựa chọn (/12) | Đ/S mệnh đề (/16) | Đ/S trọn câu (/4) | Trả lời ngắn (/6) | Tổng câu đúng (/22) | Tỷ lệ đúng (%) | Điểm (/10) |
|---|---|---|---|---|---|---|---|
| D26-G4 | 10 | 16 | 4 | 2 | 16 | 72,7 | 7,50 |
| TB 2026 | 10,0 | 16,0 | 4,0 | 2,0 | 16,0 | 72,7 | 7,50 |
| TB 1 đề | 10,0 | 16,0 | 4,0 | 2,0 | 16,0 | 72,7 | 7,50 |

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
| Đề gốc 2026 | 1 | 22 | 16 | 72,7 | 7,50 | 7,50 | 7,50 |

## Bảng 3.19. Tỷ lệ đúng theo mạch kiến thức
| Mạch kiến thức | Số câu | Số đúng | Tỷ lệ đúng (%) |
|---|---|---|---|
| Đại số và Giải tích | 14 | 10 | 71,4 |
| Hình học và Đo lường | 4 | 3 | 75,0 |
| Thống kê và Xác suất | 4 | 3 | 75,0 |
| Tổng | 22 | 16 | 72,7 |
| Trong đó: câu có hình vẽ | 5 | 1 | 20,0 |
| Trong đó: câu không có hình vẽ | 17 | 15 | 88,2 |

## Bảng 3.20. Thời gian xử lý và tài nguyên sử dụng
| Chỉ số | Giá trị |
|---|---|
| Tổng số yêu cầu đã gửi | 22 |
| Số yêu cầu lỗi API (E9) | 0 |
| Thời gian phản hồi trung bình (giây/câu) | 18,3 |
| Thời gian phản hồi lớn nhất (giây) | 127,0 |
| Token đầu vào trung bình/câu | 557,5 |
| Token đầu ra trung bình/câu | 252,6 |
| Tổng thời gian chạy 1 đề (phút) | 6,7 |

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
| E8 | Đầu ra | 5 | 83,3 |
| E9 | Kỹ thuật | 0 | 0,0 |
|  | Tổng | 6 | 100 |

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
| E8 | 2 | 0 | 3 | 5 |
| E9 | 0 | 0 | 0 | 0 |
| Tổng | 2 | 0 | 4 | 6 |

## Bảng C.9. Kết quả chi tiết từng câu – đề D26-G4
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT | x | C | – | Sai | 0,00 | E8 |
| I.5 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.6 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | A | – | Sai | 0,00 | E8 |
| I.8 | NLC | TK-XS |  | D | D | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.10 | NLC | TK-XS |  | A | A | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.12 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| II.1 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: Đ} | {a: Đ, b: Đ, c: S, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: Đ, d: S} | {a: Đ, b: Đ, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL |  | 17,1 | – | Sai | 0,00 | E8 |
| III.2 | TLN | ĐS-GT | x | 6,19 | 5,91 | Sai | 0,00 |  |
| III.3 | TLN | ĐS-GT | x | 3456 | – | Sai | 0,00 | E8 |
| III.4 | TLN | TK-XS | x | 2656 | – | Sai | 0,00 | E8 |
| III.5 | TLN | ĐS-GT |  | 3980 | 3980 | Đúng | 0,50 |  |
| III.6 | TLN | ĐS-GT |  | 1350 | 1350 | Đúng | 0,50 |  |

> Còn 1 câu sai chưa gán nhãn lỗi – điền vào nhan_loi.csv rồi chạy lại.