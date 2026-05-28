import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD DATA
# ==============================

# Lấy đường dẫn gốc của project TimeSeries
BASE_DIR = Path(__file__).resolve().parents[2]

# Tạo đường dẫn tới dataset
file_path = BASE_DIR / "common" / "datasets" / "AirPassengers.csv"

# Đọc file CSV
df = pd.read_csv(file_path)


# ==============================
# 2. KIỂM TRA DATA BAN ĐẦU
# ==============================

print("===== 5 dòng đầu tiên =====")
print(df.head())

print("\n===== Kích thước dữ liệu =====")
print(df.shape)

print("\n===== Tên các cột =====")
print(df.columns)

print("\n===== Kiểu dữ liệu =====")
print(df.dtypes)

print("\n===== Thông tin tổng quan =====")
print(df.info())


# ==============================
# 3. KIỂM TRA MISSING / NULL
# ==============================

print("\n===== Missing mỗi cột =====")
print(df.isnull().sum())

print("\n===== Tổng missing =====")
print(df.isnull().sum().sum())

print("\n===== Tỷ lệ missing (%) =====")
print(df.isnull().mean() * 100)


# ==============================
# 4. KIỂM TRA DUPLICATE
# ==============================

print("\n===== Duplicate rows =====")
print(df.duplicated().sum())


# ==============================
# 5. THỐNG KÊ MÔ TẢ
# ==============================

print("\n===== Describe =====")
print(df.describe())


# ==============================
# 6. CHUYỂN DATETIME
# ==============================

# Đổi tên cột cho dễ làm việc
# Nếu dataset của ông tên khác thì sửa lại

df.columns = ["ds", "y"]

# Chuyển cột thời gian
df["ds"] = pd.to_datetime(df["ds"])

print("\n===== Dtypes sau datetime =====")
print(df.dtypes)


# ==============================
# 7. SORT TIME
# ==============================

df = df.sort_values("ds")


# ==============================
# 8. ROLLING MEAN
# ==============================

# Rolling window = 3
df["rolling_3"] = df["y"].rolling(window=3).mean()

# Rolling window = 5
df["rolling_5"] = df["y"].rolling(window=5).mean()

# Rolling window = 7
df["rolling_7"] = df["y"].rolling(window=7).mean()


# ==============================
# 9. EXPONENTIAL MOVING AVERAGE
# ==============================

df["ema_7"] = df["y"].ewm(span=7).mean()


# ==============================
# 10. VISUALIZATION
# ==============================

plt.figure(figsize=(16, 7))

# Original data
plt.plot(
    df["ds"],
    df["y"],
    label="Original",
    alpha=0.4
)

# Rolling Mean 3
plt.plot(
    df["ds"],
    df["rolling_3"],
    label="Rolling Mean 3"
)

# Rolling Mean 5
plt.plot(
    df["ds"],
    df["rolling_5"],
    label="Rolling Mean 5"
)

# Rolling Mean 7
plt.plot(
    df["ds"],
    df["rolling_7"],
    label="Rolling Mean 7"
)

# EMA
plt.plot(
    df["ds"],
    df["ema_7"],
    label="EMA 7"
)

# Title
plt.title("Rolling Mean & EMA Comparison")

# Axis
plt.xlabel("Date")
plt.ylabel("Value")

# Grid
plt.grid(True)

# Legend
plt.legend()

# Show chart
plt.show()


# ==============================
# 11. NHẬN XÉT
# ==============================

print("""
===== NHẬN XÉT =====

1. Rolling Mean 3:
- Smooth nhẹ
- Giữ nhiều detail

2. Rolling Mean 5:
- Smooth vừa
- Trend rõ hơn

3. Rolling Mean 7:
- Smooth mạnh
- Noise giảm nhiều

4. EMA:
- Mượt
- Phản ứng nhanh với dữ liệu mới
""")

