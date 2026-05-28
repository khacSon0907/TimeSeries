# 📊 Time Series Analysis & Forecasting

## Giới thiệu

Đây là tài liệu toàn diện về **Time Series Analysis** - một lĩnh vực quan trọng trong Data Science và Machine Learning. Tài liệu này bao gồm từ những khái niệm cơ bản đến các mô hình nâng cao for dự báo và phân tích dữ liệu chuỗi thời gian.

## 📚 Nội dung

### 1. **Nền tảng Time Series** (Foundation)
- Trend, seasonality, noise, cycle
- Stationarity, differencing
- Autocorrelation, PACF, ACF
- Train/test split cho dữ liệu thời gian
- Rolling forecast, walk-forward validation

### 2. **Mô hình truyền thống** (Traditional Models)
- Naive forecast
- Moving Average
- Exponential Smoothing
- ARIMA, SARIMA, SARIMAX
- Prophet
- VAR cho nhiều chuỗi thời gian

### 3. **Machine Learning cho Time Series**
- Feature engineering: lag features, rolling mean, date features
- XGBoost, LightGBM, CatBoost
- Random Forest, Linear Regression
- Multi-step forecasting
- Recursive vs direct forecasting

### 4. **Deep Learning**
- RNN, LSTM, GRU
- Temporal CNN
- Transformer cho time series
- N-BEATS, TFT, DeepAR
- Forecasting nhiều biến cùng lúc

### 5. **Đánh giá mô hình**
- MAE, RMSE, MAPE, SMAPE
- Backtesting
- Leakage trong time series
- Baseline comparison
- Confidence interval / prediction interval

### 6. **Ứng dụng thực tế**
- Dự báo doanh thu
- Dự báo nhu cầu hàng hóa
- Dự báo giá
- Dự báo traffic website
- Dự báo sản lượng
- Dự báo tài chính/crypto ở mức phân tích dữ liệu, không phải lời khuyên đầu tư

## 📁 Cấu trúc tài liệu

```
TimeSeries/
├── README.md (file này)
└── docs/
    ├── ReadmeDocs.md (Roadmap chi tiết)
    └── 01-foundation/ (Các khái niệm cơ bản)
        ├── 01-what-is-time-series.md
        ├── 02-trend.md
        ├── 03-seasonality.md
        ├── 04-noise.md
        └── 05-cyclical.md
```

## 🎯 Đối tượng

Tài liệu này dành cho:
- Sinh viên Data Science
- Data Analysts
- Machine Learning Engineers
- Bất kỳ ai muốn học về Time Series Analysis

## 🚀 Cách sử dụng

1. Bắt đầu với phần **Nền tảng** (`01-foundation/`) để hiểu các khái niệm cơ bản
2. Tiếp tục với các mô hình truyền thống
3. Nâng cao với Machine Learning và Deep Learning
4. Học về các metrics đánh giá
5. Áp dụng vào các ứng dụng thực tế

## 📖 Tài liệu tham khảo

- [ReadmeDocs.md](./docs/ReadmeDocs.md) - Roadmap chi tiết
- [01-Foundation](./docs/01-foundation/) - Khái niệm cơ bản

## 💡 Ghi chú

- Tất cả ví dụ đều dựa trên dữ liệu thực tế
- Mỗi khái niệm đều có ví dụ minh họa cụ thể
- Tài liệu được viết bằng tiếng Việt để dễ hiểu

---

**Cập nhật lần cuối**: May 28, 2026

