# 4. Noise — Nhiễu / Biến động ngẫu nhiên

## Định nghĩa

**Noise** (nhiễu) là phần biến động bất thường, ngẫu nhiên, khó dự đoán và không tuân theo quy luật nhất định. Đây là thành phần "rác" khiến dữ liệu trở nên phức tạp.

## Ví dụ thực tế

### Trời mưa
Một ngày quán cà phê bán ít hơn bình thường vì trời mưa rất to.

### Sự cố hệ thống
Website bị lỗi nên lượt truy cập giảm đột ngột.

### Sự kiện bất ngờ
- Một influencer nhắc đến sản phẩm nên doanh thu tăng bất ngờ
- Có sự kiện bất thường làm giá cổ phiếu nhảy mạnh
- Một ngày shipper đình công nên đơn hàng giảm

## Đặc điểm của Noise

| Đặc điểm | Chi tiết |
|---------|----------|
| **Ngẫu nhiên** | Không tuân theo quy luật nhất định, không lặp lại |
| **Khó dự đoán** | Không biết trước nó sẽ xảy ra khi nào hoặc quy mô bao nhiêu |
| **Không có chu kỳ** | Không lặp lại theo thời gian |
| **Do sự kiện ngoài dự kiến** | Thường do những yếu tố bên ngoài gây ra |

## Cách nhận biết Noise

1. **Biểu đồ thời gian**: Có các "spike" bất thường, biến động không theo mô hình
2. **Phần dư (Residuals)**: Sau khi loại bỏ trend và seasonality, phần còn lại là noise
3. **Thống kê**: Noise có giá trị trung bình ≈ 0 và phương sai không đổi

## Cách xử lý Noise

### 1. Làm mịn dữ liệu (Smoothing)
- Moving Average
- Exponential Smoothing
- Hạ thấp vang tần cao (Low-pass filter)

### 2. Loại bỏ outliers
- Xác định giá trị bất thường (quá cao/quá thấp)
- Thay thế bằng giá trị hợp lý hoặc loại bỏ

### 3. Chấp nhận noise
- Sử dụng mô hình có khả năng xử lý noise tốt (ví dụ: ARIMA với error term)
- Tăng kích thước training data để noise bị "average out"

## Tại sao cần xử lý Noise?

- **Dự báo chính xác hơn**: Loại bỏ bias từ những biến động ngẫu nhiên
- **Tìm ra quy luật thực sự**: Focus vào trend và seasonality thực sự
- **Giảm overfitting**: Mô hình không học theo noise mà học theo quy luật chung
