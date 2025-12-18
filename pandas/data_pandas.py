import pandas as pd

path = r"C:\Users\Kelvin\Documents\Sereti\Data-analytics\pandas\Datasets\Retail Transactions.csv"

# Parse dates
date_cols = ["signup_date", "last_login", "order_date", "ship_date"]

# Load data (only once)
data = pd.read_csv(path, parse_dates=date_cols)

print(data.head())

# Shape, columns, dtypes
print(data.shape)
print(data.columns)
print(data.dtypes)

#null values
nulls = data.isna().sum().sort_values(ascending=False)
print(f"\nNulls:\n{nulls}")

# Cardinalities for key identifiers
data["transaction_id"].nunique(), data["order_id"].nunique(), data["customer_id"].nunique()

#Date Ranges
date_ranges = data["order_date"].min(), data["order_date"].max()
date_ranges = data["ship_date"].min(), data["ship_date"].max()

#Numeric Ranges
num_cols = ["customer_age","quantity","unit_price","discount_rate","shipping_cost","satisfaction_score","loyalty_points","delivery_days"]

# Coerce numerics
to_numeric = ["customer_age","latitude","longitude","quantity","unit_price","discount_rate",
              "shipping_cost","satisfaction_score","loyalty_points","delivery_days"]

for non_numeric in to_numeric:
    data[non_numeric] = pd.to_numeric(data[non_numeric], errors="coerce")

