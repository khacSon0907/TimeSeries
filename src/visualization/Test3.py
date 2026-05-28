import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose



# 1. LOAD DATA
# ==============================

# Lấy đường dẫn gốc của project TimeSeries
BASE_DIR = Path(__file__).resolve().parents[2]

# Tạo đường dẫn tới dataset
file_path = BASE_DIR / "common" / "datasets" / "ustreas.csv"

# Đọc file CSV
df = pd.read_csv(file_path)

result = seasonal_decompose(
    df["y"],
    model="additive",
    period=30
)

result.plot()
plt.show()