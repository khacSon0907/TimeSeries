# 3. Seasonality — Tính mùa vụ

## Định nghĩa

**Seasonality** là kiểu dao động lặp lại theo một chu kỳ cố định. Các biến động này xảy ra một cách đều đặn trong những khoảng thời gian nhất định.

## Chu kỳ Seasonality phổ biến

- **Hàng ngày**: Người dùng online cao vào buổi tối, thấp vào sáng sớm
- **Hàng tuần**: Doanh số bán lẻ cao vào cuối tuần
- **Hàng tháng**: Lượng điện tiêu thụ cao vào hè (do dùng máy lạnh)
- **Hàng quý**: Doanh thu công ty có chu kỳ quý (Q1, Q2, Q3, Q4)
- **Hàng năm**: Doanh số bán hàng cao vào Tết, Noel, cuối năm

## Ví dụ thực tế

### E-commerce
- Doanh số online tăng cao vào các ngày lễ (Tết, Noel, 8/3, 20/11, v.v.)
- Thậm chí có "peaks" nhỏ vào cuối tháng khi nhân viên được lương

### Điện nước
- Mùa hè: tiêu thụ điện tăng (dùng máy lạnh)
- Mùa đông: tiêu thụ nước nóng tăng

### Vận tải
- Thứ 6 tối: tắc đường do mọi người về quê
- Thứ 2 sáng: tắc đường do mọi người về công ty

## Đặc điểm của Seasonality

| Đặc điểm | Chi tiết |
|---------|----------|
| **Chu kỳ cố định** | Tính lặp lại xảy ra ở những khoảng thời gian đều đặn |
| **Theo lịch** | Thường liên quan đến lịch (ngày, tuần, tháng, năm) |
| **Dự đoán được** | Vì lặp lại nên dễ dự báo hơn so với noise |
| **Nhất quán** | Các chu kỳ khác nhau có cùng hình dáng/biên độ tương tự |

## Cách nhận biết Seasonality

1. **Biểu đồ thời gian**: Mô hình lặp lại rõ ràng mỗi chu kỳ
2. **ACF plot**: Có spike định kỳ ở lag = chu kỳ
3. **Phân tích thông kê**: So sánh cùng khoảng thời gian năm trước/năm nay

## Tại sao cần tìm Seasonality?

- **Dự báo tốt hơn**: Biết được mô hình lặp lại không phải kỳ vọng bất ngờ
- **Loại bỏ seasonality**: Để focus vào các yếu tố khác (trend, noise)
- **Kế hoạch hóa**: Biết mùa cao điểm/mùa mở để chuẩn bị hàng hóa, nhân lực
