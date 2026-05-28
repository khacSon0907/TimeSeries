# 2. Trend - Xu hướng dài hạn

## Định nghĩa

**Trend** là hướng đi chung của dữ liệu theo thời gian, có thể là tăng, giảm hoặc ổn định. Đây là thành phần chính trong phân tích Time Series, thể hiện chiều hướng tổng thể của dữ liệu qua các thời kỳ dài.

## Ví dụ thực tế

### Doanh thu tăng dần
Doanh thu hàng tháng của một cửa hàng trực tuyến: từ 100 triệu (tháng 1) → 150 triệu (tháng 6) → 200 triệu (tháng 12)

### Số lượng người dùng giảm
Một trang web cũ có số lượng người dùng hoạt động giảm dần qua các quý.

### Giá cộng hòa ổn định
Giá điện không thay đổi nhiều trong 2-3 năm.

## Các dạng Trend phổ biến

| Dạng Trend | Ý nghĩa | Ví dụ |
|-----------|---------|-------|
| **Upward trend** | Tăng dần | Doanh thu, lượt truy cập website |
| **Downward trend** | Giảm dần | Số khách hàng cũ, chi phí hoạt động |
| **Flat trend** | Gần như không đổi | Giá sản phẩm, lượng hàng tồn kho |

## Cách nhận biết Trend

1. **Nhìn biểu đồ**: Đường hẳn hẳn đi lên / đi xuống / nằm ngang
2. **Tính Linear Regression**: Nếu hệ số dốc dương → uptrend, âm → downtrend
3. **Moving Average**: So sánh dữ liệu thực với đường MA để thấy xu hướng

## Tại sao cần biết Trend?

- **Dự báo**: Nếu biết trend, dễ dự báo giá trị tương lai
- **Phát hiện vấn đề**: Downtrend có thể cảnh báo vấn đề kinh doanh
- **Lên kế hoạch**: Uptrend giúp doanh nghiệp lên kế hoạch phát triển 
