from src.data_loader import load_data
from src.preprocessing import clean_data
from src.feature_engineering import create_features
from src.model import train_model
from src.forecast import forecast
from src.inventory import calculate_inventory

import pandas as pd

# Step 1: Load data
df = load_data()

# Step 2: Clean data
df = clean_data(df)

# Step 3: Feature engineering
df = create_features(df)

# Step 4: Train model
model = train_model(df)

# Step 5: Forecast
df = forecast(model, df)

# Step 6: Calculate inventory (IMPORTANT LINE)
inventory = calculate_inventory(df)

# Step 7: Save outputs
df.to_csv("outputs/forecast.csv", index=False)
pd.DataFrame([inventory]).to_csv("outputs/inventory_recommendations.csv", index=False)

# Step 8: Print nicely
print("\n📦 INVENTORY RECOMMENDATION")
print("="*40)
print(f"Average Daily Demand : {inventory['mean_demand']} units")
print(f"Safety Stock         : {inventory['safety_stock']} units")
print(f"Reorder Point        : {inventory['reorder_point']} units")

# Optional (if you added order quantity)
if "order_quantity" in inventory:
    print(f"Order Quantity       : {inventory['order_quantity']} units")

print("="*40)