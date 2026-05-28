What is Time Series?

Time Series là dữ liệu được lưu dưới dạng thời gian.

**Ví dụ:**
- Doanh thu hàng ngày
- Nhiệt độ hàng giờ
- Giá cổ phiếu hàng phút

## Đặc điểm chính của Time Series

### 1. Sắp xếp theo thứ tự thời gian
Dữ liệu được sắp xếp đúng thứ tự thời gian, mỗi điểm dữ liệu có một timestamp nhất định.

### 2. Có xu hướng, mùa vụ và nhiễu
Time Series có thể chứa:
- **Trend**: Xu hướng dài hạn (tăng, giảm, hoặc ổn định)
- **Seasonality**: Tính mùa vụ lặp lại theo chu kỳ cố định
- **Noise**: Nhiễu ngẫu nhiên khó dự đoán

### 3. Tính dừng (Stationarity)
- **Stationary**: Dữ liệu ổn định, không có trend, giá trị trung bình/phương sai không đổi
- **Non-stationary**: Dữ liệu có trend hoặc biến động không ổn định

### 4. Tự tương quan (Autocorrelation)
Giữa các giá trị trong chuỗi có mối quan hệ tương quan với nhau. Giá trị hiện tại có thể phụ thuộc vào giá trị quá khứ.

### 5. Dự báo
Time Series thường được sử dụng để dự báo giá trị tương lai dựa trên dữ liệu quá khứ.

## Phân loại Time Series

### Theo số lượng biến
- **Univariate**: Một biến (1 chuỗi dữ liệu)
- **Multivariate**: Nhiều biến (nhiều chuỗi dữ liệu liên quan)

### Theo khoảng thời gian
- **Regular**: Khoảng thời gian đều đặn (hàng ngày, hàng giờ, v.v.)
- **Irregular**: Khoảng thời gian không đều (có thể chênh lệch)
