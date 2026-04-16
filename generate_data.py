import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=365)

data = pd.DataFrame({
    "date": dates,
    "qty_sold": np.random.poisson(lam=50, size=365)
})

# Add simple seasonality
data["qty_sold"] = data["qty_sold"] + (data.index % 7) * 5

# Save file
data.to_csv("data/raw/retail_data.csv", index=False)

print("✅ Dataset created successfully!")