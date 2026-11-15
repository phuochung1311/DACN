# Kết quả thực nghiệm Gemini – 15/11/2026 15:33
Mô hình ghi nhận trong phản hồi: gemini-3.6-flash

## Bảng 3.14. Kết quả tổng hợp
| Chỉ số | Kết quả |
|---|---|
| Số câu đúng / tổng số câu | 196 / 198 |
| Tỷ lệ đúng trên tổng số câu (3.1) | 99,0 % |
| Số mệnh đề Đúng/Sai xác định đúng | 144 / 144 |
| Điểm trung bình (thang 10) | 9,92 |
| Điểm cao nhất (mã đề) | 10,00 (D25-G1) |
| Điểm thấp nhất (mã đề) | 9,50 (D26-G4) |
| Số phản hồi lỗi định dạng hoặc kỹ thuật (E8, E9) | 0 |

## Bảng 3.15. Tỷ lệ đúng theo dạng bài
| Dạng bài | Đơn vị | Tổng số | Số đúng | Tỷ lệ đúng (%) | Điểm TB/đề | Điểm tối đa/đề |
|---|---|---|---|---|---|---|
| Nhiều lựa chọn | câu | 108 | 107 | 99,1 | 2,97 | 3,0 |
| Đúng/Sai (trọn câu) | câu | 36 | 36 | 100,0 | 4,00 | 4,0 |
| Đúng/Sai (theo mệnh đề) | mệnh đề | 144 | 144 | 100,0 | – | – |
| Trả lời ngắn | câu | 54 | 53 | 98,1 | 2,94 | 3,0 |
| Tổng (theo câu) | câu | 198 | 196 | 99,0 | 9,92 | 10,0 |

## Bảng 3.17. Kết quả chi tiết theo từng đề
| Mã dữ liệu | Nhiều lựa chọn (/12) | Đ/S mệnh đề (/16) | Đ/S trọn câu (/4) | Trả lời ngắn (/6) | Tổng câu đúng (/22) | Tỷ lệ đúng (%) | Điểm (/10) |
|---|---|---|---|---|---|---|---|
| D25-MH | 11 | 16 | 4 | 6 | 21 | 95,5 | 9,75 |
| D25-G1 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D25-G2 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D25-G3 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D25-G4 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D26-G1 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D26-G2 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D26-G3 | 12 | 16 | 4 | 6 | 22 | 100,0 | 10,00 |
| D26-G4 | 12 | 16 | 4 | 5 | 21 | 95,5 | 9,50 |
| TB 2025 | 11,8 | 16,0 | 4,0 | 6,0 | 21,8 | 99,1 | 9,95 |
| TB 2026 | 12,0 | 16,0 | 4,0 | 5,8 | 21,8 | 98,9 | 9,88 |
| TB 9 đề | 11,9 | 16,0 | 4,0 | 5,9 | 21,8 | 99,0 | 9,92 |

## Bảng 3.16. Phân bố số mệnh đề xác định đúng trong mỗi câu Đúng/Sai
| Số mệnh đề đúng k | Số câu | Tỷ lệ (%) | Điểm g(k) |
|---|---|---|---|
| 0 | 0 | 0,0 | 0,00 |
| 1 | 0 | 0,0 | 0,10 |
| 2 | 0 | 0,0 | 0,25 |
| 3 | 0 | 0,0 | 0,50 |
| 4 | 36 | 100,0 | 1,00 |

## Bảng 3.18. So sánh kết quả theo năm và loại đề
| Nhóm đề | Số đề | Số câu | Số câu đúng | Tỷ lệ đúng (%) | Điểm TB | Thấp nhất | Cao nhất |
|---|---|---|---|---|---|---|---|
| Đề minh họa 2025 | 1 | 22 | 21 | 95,5 | 9,75 | 9,75 | 9,75 |
| Đề gốc 2025 | 4 | 88 | 88 | 100,0 | 10,00 | 10,00 | 10,00 |
| Đề gốc 2026 | 4 | 88 | 87 | 98,9 | 9,88 | 9,50 | 10,00 |

## Bảng 3.19. Tỷ lệ đúng theo mạch kiến thức
| Mạch kiến thức | Số câu | Số đúng | Tỷ lệ đúng (%) |
|---|---|---|---|
| Đại số và Giải tích | 109 | 107 | 98,2 |
| Hình học và Đo lường | 55 | 55 | 100,0 |
| Thống kê và Xác suất | 34 | 34 | 100,0 |
| Tổng | 198 | 196 | 99,0 |
| Trong đó: câu có hình vẽ | 47 | 45 | 95,7 |
| Trong đó: câu không có hình vẽ | 151 | 151 | 100,0 |

## Bảng 3.20. Thời gian xử lý và tài nguyên sử dụng
| Chỉ số | Giá trị |
|---|---|
| Tổng số yêu cầu đã gửi | 198 |
| Số yêu cầu lỗi API (E9) | 0 |
| Thời gian phản hồi trung bình (giây/câu) | 14,5 |
| Thời gian phản hồi lớn nhất (giây) | 206,6 |
| Token đầu vào trung bình/câu | 567,1 |
| Token đầu ra trung bình/câu | 260,9 |
| Tổng thời gian chạy 9 đề (phút) | 47,9 |

## Bảng 3.21. Phân bố nhóm lỗi chính trong các câu trả lời sai
| Mã | Nhóm lỗi | Số câu | Tỷ lệ trên tổng câu sai (%) |
|---|---|---|---|
| E1 | Đọc dữ kiện | 0 | 0,0 |
| E2 | Đọc hình | 2 | 100,0 |
| E3 | Mô hình hóa | 0 | 0,0 |
| E4 | Kiến thức | 0 | 0,0 |
| E5 | Suy luận | 0 | 0,0 |
| E6 | Tính toán | 0 | 0,0 |
| E7 | Kết luận | 0 | 0,0 |
| E8 | Đầu ra | 0 | 0,0 |
| E9 | Kỹ thuật | 0 | 0,0 |
|  | Tổng | 2 | 100 |

## Bảng 3.22. Phân bố nhóm lỗi theo dạng bài
| Mã lỗi | Nhiều lựa chọn | Đúng/Sai | Trả lời ngắn | Tổng |
|---|---|---|---|---|
| E1 | 0 | 0 | 0 | 0 |
| E2 | 1 | 0 | 1 | 2 |
| E3 | 0 | 0 | 0 | 0 |
| E4 | 0 | 0 | 0 | 0 |
| E5 | 0 | 0 | 0 | 0 |
| E6 | 0 | 0 | 0 | 0 |
| E7 | 0 | 0 | 0 | 0 |
| E8 | 0 | 0 | 0 | 0 |
| E9 | 0 | 0 | 0 | 0 |
| Tổng | 1 | 0 | 1 | 2 |

## Bảng C.1. Kết quả chi tiết từng câu – đề D25-MH
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.3 | NLC | TK-XS |  | A | A | Đúng | 0,25 |  |
| I.4 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT | x | B | C | Sai | 0,00 | E2 |
| I.6 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.7 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| I.8 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | HH-ĐL | x | D | D | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT | x | C | C | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: S, c: Đ, d: S} | {a: Đ, b: S, c: Đ, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL | x | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL |  | 4,9 | 4,9 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT | x | 43 | 43 | Đúng | 0,50 |  |
| III.3 | TLN | HH-ĐL |  | 3 | 3 | Đúng | 0,50 |  |
| III.4 | TLN | ĐS-GT | x | 3200 | 3200 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 333 | 333 | Đúng | 0,50 |  |
| III.6 | TLN | TK-XS |  | 0,08 | 0,08 | Đúng | 0,50 |  |

## Bảng C.2. Kết quả chi tiết từng câu – đề D25-G1
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | HH-ĐL | x | C | C | Đúng | 0,25 |  |
| I.2 | NLC | HH-ĐL | x | C | C | Đúng | 0,25 |  |
| I.3 | NLC | TK-XS |  | C | C | Đúng | 0,25 |  |
| I.4 | NLC | HH-ĐL |  | D | D | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.6 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.8 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.9 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT | x | B | B | Đúng | 0,25 |  |
| I.12 | NLC | HH-ĐL |  | D | D | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: S, d: S} | {a: Đ, b: S, c: S, d: S} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: Đ, d: S} | {a: Đ, b: S, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: Đ, d: S} | {a: Đ, b: S, c: Đ, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: Đ} | {a: Đ, b: Đ, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | TK-XS | x | 1260 | 1260 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT |  | 1536 | 1536 | Đúng | 0,50 |  |
| III.3 | TLN | ĐS-GT |  | 2650 | 2650 | Đúng | 0,50 |  |
| III.4 | TLN | HH-ĐL |  | 1,04 | 1,04 | Đúng | 0,50 |  |
| III.5 | TLN | TK-XS |  | 1008 | 1008 | Đúng | 0,50 |  |
| III.6 | TLN | HH-ĐL | x | 96,5 | 96,5 | Đúng | 0,50 |  |

## Bảng C.3. Kết quả chi tiết từng câu – đề D25-G2
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.2 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT | x | B | B | Đúng | 0,25 |  |
| I.6 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.7 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.8 | NLC | TK-XS | x | B | B | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.10 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | HH-ĐL | x | B | B | Đúng | 0,25 |  |
| I.12 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | TK-XS |  | {a: Đ, b: S, c: S, d: S} | {a: Đ, b: S, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL | x | 95,9 | 95,9 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT |  | 1092 | 1092 | Đúng | 0,50 |  |
| III.3 | TLN | TK-XS | x | 2520 | 2520 | Đúng | 0,50 |  |
| III.4 | TLN | ĐS-GT |  | 2975 | 2975 | Đúng | 0,50 |  |
| III.5 | TLN | TK-XS |  | 2352 | 2352 | Đúng | 0,50 |  |
| III.6 | TLN | HH-ĐL |  | 0,85 | 0,85 | Đúng | 0,50 |  |

## Bảng C.4. Kết quả chi tiết từng câu – đề D25-G3
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.6 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.7 | NLC | TK-XS |  | B | B | Đúng | 0,25 |  |
| I.8 | NLC | HH-ĐL |  | D | D | Đúng | 0,25 |  |
| I.9 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT | x | D | D | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: S, d: S} | {a: Đ, b: S, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | ĐS-GT |  | 1808 | 1808 | Đúng | 0,50 |  |
| III.2 | TLN | TK-XS |  | 2016 | 2016 | Đúng | 0,50 |  |
| III.3 | TLN | TK-XS | x | 3780 | 3780 | Đúng | 0,50 |  |
| III.4 | TLN | HH-ĐL |  | 2,08 | 2,08 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 2150 | 2150 | Đúng | 0,50 |  |
| III.6 | TLN | HH-ĐL | x | 95,3 | 95,3 | Đúng | 0,50 |  |

## Bảng C.5. Kết quả chi tiết từng câu – đề D25-G4
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.3 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.4 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.5 | NLC | HH-ĐL | x | C | C | Đúng | 0,25 |  |
| I.6 | NLC | TK-XS |  | B | B | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.8 | NLC | ĐS-GT | x | D | D | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.10 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.11 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: Đ, d: S} | {a: Đ, b: S, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: S, c: S, d: S} | {a: Đ, b: S, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| III.1 | TLN | ĐS-GT |  | 3528 | 3528 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT |  | 3150 | 3150 | Đúng | 0,50 |  |
| III.3 | TLN | TK-XS | x | 5040 | 5040 | Đúng | 0,50 |  |
| III.4 | TLN | HH-ĐL |  | 2,55 | 2,55 | Đúng | 0,50 |  |
| III.5 | TLN | HH-ĐL | x | 94,7 | 94,7 | Đúng | 0,50 |  |
| III.6 | TLN | ĐS-GT |  | 1347 | 1347 | Đúng | 0,50 |  |

## Bảng C.6. Kết quả chi tiết từng câu – đề D26-G1
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.5 | NLC | HH-ĐL |  | A | A | Đúng | 0,25 |  |
| I.6 | NLC | TK-XS |  | D | D | Đúng | 0,25 |  |
| I.7 | NLC | HH-ĐL | x | B | B | Đúng | 0,25 |  |
| I.8 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT | x | A | A | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.12 | NLC | TK-XS |  | A | A | Đúng | 0,25 |  |
| II.1 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: Đ, d: S} | {a: Đ, b: Đ, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL |  | 7,35 | 7,35 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT | x | 1152 | 1152 | Đúng | 0,50 |  |
| III.3 | TLN | ĐS-GT | x | 5,91 | 5,91 | Đúng | 0,50 |  |
| III.4 | TLN | TK-XS | x | 1856 | 1856 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 1275 | 1275 | Đúng | 0,50 |  |
| III.6 | TLN | ĐS-GT |  | 1990 | 1990 | Đúng | 0,50 |  |

## Bảng C.7. Kết quả chi tiết từng câu – đề D26-G2
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | HH-ĐL | x | D | D | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.3 | NLC | HH-ĐL |  | D | D | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.6 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.8 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.9 | NLC | TK-XS |  | C | C | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.11 | NLC | TK-XS |  | C | C | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT | x | D | D | Đúng | 0,25 |  |
| II.1 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: Đ, d: S} | {a: Đ, b: Đ, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: Đ} | {a: Đ, b: Đ, c: S, d: Đ} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | ĐS-GT | x | 6,19 | 6,19 | Đúng | 0,50 |  |
| III.2 | TLN | HH-ĐL |  | 17,1 | 17,1 | Đúng | 0,50 |  |
| III.3 | TLN | ĐS-GT | x | 3456 | 3456 | Đúng | 0,50 |  |
| III.4 | TLN | ĐS-GT |  | 3980 | 3980 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 1350 | 1350 | Đúng | 0,50 |  |
| III.6 | TLN | TK-XS | x | 2656 | 2656 | Đúng | 0,50 |  |

## Bảng C.8. Kết quả chi tiết từng câu – đề D26-G3
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.2 | NLC | HH-ĐL | x | B | B | Đúng | 0,25 |  |
| I.3 | NLC | TK-XS |  | C | C | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT | x | C | C | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.6 | NLC | TK-XS |  | C | C | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.8 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.9 | NLC | HH-ĐL |  | C | C | Đúng | 0,25 |  |
| I.10 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.12 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| II.1 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: Đ, d: Đ} | {a: Đ, b: S, c: Đ, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: Đ, d: S} | {a: Đ, b: Đ, c: Đ, d: S} | Đúng | 1,00 |  |
| III.1 | TLN | TK-XS | x | 1856 | 1856 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT |  | 1275 | 1275 | Đúng | 0,50 |  |
| III.3 | TLN | ĐS-GT | x | 5,91 | 5,91 | Đúng | 0,50 |  |
| III.4 | TLN | ĐS-GT | x | 1152 | 1152 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 1990 | 1990 | Đúng | 0,50 |  |
| III.6 | TLN | HH-ĐL |  | 7,35 | 7,35 | Đúng | 0,50 |  |

## Bảng C.9. Kết quả chi tiết từng câu – đề D26-G4
| Câu | Dạng | Mạch | Hình | Đáp án chính thức | Trả lời của Gemini | Kết quả | Điểm | Mã lỗi |
|---|---|---|---|---|---|---|---|---|
| I.1 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.2 | NLC | ĐS-GT |  | C | C | Đúng | 0,25 |  |
| I.3 | NLC | ĐS-GT |  | D | D | Đúng | 0,25 |  |
| I.4 | NLC | ĐS-GT | x | C | C | Đúng | 0,25 |  |
| I.5 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.6 | NLC | HH-ĐL | x | A | A | Đúng | 0,25 |  |
| I.7 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.8 | NLC | TK-XS |  | D | D | Đúng | 0,25 |  |
| I.9 | NLC | ĐS-GT |  | B | B | Đúng | 0,25 |  |
| I.10 | NLC | TK-XS |  | A | A | Đúng | 0,25 |  |
| I.11 | NLC | ĐS-GT |  | A | A | Đúng | 0,25 |  |
| I.12 | NLC | HH-ĐL |  | B | B | Đúng | 0,25 |  |
| II.1 | Đ/S | TK-XS |  | {a: Đ, b: Đ, c: S, d: Đ} | {a: Đ, b: Đ, c: S, d: Đ} | Đúng | 1,00 |  |
| II.2 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: Đ, d: S} | {a: Đ, b: Đ, c: Đ, d: S} | Đúng | 1,00 |  |
| II.3 | Đ/S | ĐS-GT |  | {a: Đ, b: Đ, c: S, d: S} | {a: Đ, b: Đ, c: S, d: S} | Đúng | 1,00 |  |
| II.4 | Đ/S | HH-ĐL |  | {a: Đ, b: S, c: S, d: Đ} | {a: Đ, b: S, c: S, d: Đ} | Đúng | 1,00 |  |
| III.1 | TLN | HH-ĐL |  | 17,1 | 17,1 | Đúng | 0,50 |  |
| III.2 | TLN | ĐS-GT | x | 6,19 | 5,91 | Sai | 0,00 | E2 |
| III.3 | TLN | ĐS-GT | x | 3456 | 3456 | Đúng | 0,50 |  |
| III.4 | TLN | TK-XS | x | 2656 | 2656 | Đúng | 0,50 |  |
| III.5 | TLN | ĐS-GT |  | 3980 | 3980 | Đúng | 0,50 |  |
| III.6 | TLN | ĐS-GT |  | 1350 | 1350 | Đúng | 0,50 |  |