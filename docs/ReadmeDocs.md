# Time Series Analysis & Forecasting - Roadmap Chi Tiết

## 1. Nền tảng Time Series

### Khái niệm cơ bản
- [What is Time Series?](./01-foundation/01-what-is-time-series.md) - Giới thiệu, định nghĩa và phân loại
- [Trend - Xu hướng dài hạn](./01-foundation/02-trend.md) - Trend types, cách nhận biết, ứng dụng
- [Seasonality - Tính mùa vụ](./01-foundation/03-seasonality.md) - Chu kỳ cố định, ví dụ thực tế
- [Noise - Nhiễu ngẫu nhiên](./01-foundation/04-noise.md) - Biến động bất thường, xử lý noise
- [Cycle - Chu kỳ dài hạn](./01-foundation/05-cyclical.md) - Chu kỳ không cố định, vs Seasonality

### Phân tích nâng cao
- Stationarity, differencing
- Autocorrelation, PACF, ACF
- Train/test split cho dữ liệu thời gian
- Rolling forecast, walk-forward validation

## 2. Mô hình truyền thống

### Mô hình đơn giản
- Naive forecast
- Moving Average
- Exponential Smoothing

### Mô hình phức tạp
- ARIMA, SARIMA, SARIMAX
- Prophet
- VAR cho nhiều chuỗi thời gian

## 3. Machine Learning cho Time Series

### Feature Engineering
- Lag features (t-1, t-2, ..., t-n)
- Rolling mean / rolling std
- Date features (day of week, day of month, v.v.)
- Trend và Seasonality components

### Mô hình ML phổ biến
- XGBoost, LightGBM, CatBoost
- Random Forest, Linear Regression
- Multi-step forecasting
- Recursive vs direct forecasting

## 4. Deep Learning

### Các kiến trúc AI
- RNN, LSTM, GRU
- Temporal CNN, 1D Convolution
- Transformer cho time series
- N-BEATS, TFT, DeepAR

### Ứng dụng
- Forecasting nhiều biến cùng lúc (Multivariate)
- Sequence-to-sequence models
- Attention mechanisms

## 5. Đánh giá mô hình

### Metrics đánh giá
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)
- SMAPE (Symmetric MAPE)

### Validation methods
- Backtesting
- Walk-forward validation
- Leakage trong time series
- Baseline comparison
- Confidence interval / prediction interval

## 6. Ứng dụng thực tế

### Dự báo kinh tế
- Dự báo doanh thu
- Dự báo nhu cầu hàng hóa
- Dự báo giá

### Dự báo kỹ thuật
- Dự báo traffic website
- Dự báo sản lượng
- Dự báo tài chính/crypto ở mức phân tích dữ liệu, không phải lời khuyên đầu tư

---

## 📚 Cách học tài liệu này

1. **Tuần 1**: Đọc kỹ phần Nền tảng (Foundation)
2. **Tuần 2-3**: Học các mô hình truyền thống
3. **Tuần 4-5**: Học Machine Learning
4. **Tuần 6-7**: Học Deep Learning
5. **Tuần 8**: Ôn tập và áp dụng vào dự án thực tế

## 🔗 Tài liệu tham khảo

- [README.md](../README.md) - Giới thiệu project
