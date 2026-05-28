import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD DATA
# ==============================

# Lấy đường dẫn gốc của project TimeSeries
BASE_DIR = Path(__file__).resolve().parents[2]

# Tạo đường dẫn tới file AirPassengers.csv
file_path = BASE_DIR / "common" / "datasets" / "AirPassengers.csv"

# Đọc file CSV vào DataFrame
df = pd.read_csv(file_path)


# ==============================
# 2. KIỂM TRA DATA BAN ĐẦU
# ==============================

# Xem 5 dòng đầu tiên
print("===== 5 dòng đầu tiên =====")
print(df.head())

# Xem số dòng và số cột
print("\n===== Kích thước dữ liệu =====")
print(df.shape)

# Xem tên các cột
print("\n===== Tên các cột =====")
print(df.columns)

# Xem kiểu dữ liệu của từng cột
print("\n===== Kiểu dữ liệu =====")
print(df.dtypes)

# Xem thông tin tổng quan:
# số dòng, số cột, kiểu dữ liệu, số giá trị non-null
print("\n===== Thông tin tổng quan =====")
print(df.info())


# ==============================
# 3. KIỂM TRA MISSING / NULL
# ==============================

# Kiểm tra mỗi cột có bao nhiêu giá trị bị thiếu
print("\n===== Số lượng missing/null mỗi cột =====")
print(df.isnull().sum())

# Kiểm tra tổng số giá trị missing trong toàn bộ dataset
print("\n===== Tổng số missing/null toàn bộ data =====")
print(df.isnull().sum().sum())

# Kiểm tra tỷ lệ missing theo phần trăm
print("\n===== Tỷ lệ missing/null theo phần trăm =====")
print(df.isnull().mean() * 100)


# ==============================
# 4. KIỂM TRA DỮ LIỆU TRÙNG LẶP
# ==============================

# Đếm số dòng bị trùng hoàn toàn
print("\n===== Số dòng duplicate =====")
print(df.duplicated().sum())


# ==============================
# 5. KIỂM TRA THỐNG KÊ CƠ BẢN
# ==============================

# Xem thống kê với cột số:
# count, mean, std, min, max...
print("\n===== Thống kê mô tả =====")
print(df.describe())


# ==============================
# 6. CHUYỂN CỘT NGÀY SANG DATETIME
# ==============================

# Với dataset này:
# ds = cột thời gian
# y  = số lượng hành khách
df["ds"] = pd.to_datetime(df["ds"])

# Kiểm tra lại kiểu dữ liệu sau khi chuyển
print("\n===== Kiểu dữ liệu sau khi chuyển ds sang datetime =====")
print(df.dtypes)


# ==============================
# 7. SẮP XẾP DỮ LIỆU THEO THỜI GIAN
# ==============================

# Time series nên được sắp xếp theo thời gian từ cũ đến mới
df = df.sort_values("ds")


# ==============================
# 8. VẼ LINE CHART
# ==============================

plt.figure(figsize=(12, 5))

# Trục X là thời gian ds
# Trục Y là giá trị y
plt.plot(df["ds"], df["y"])

plt.title("Air Passengers Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Passengers")
plt.grid(True)
plt.show()