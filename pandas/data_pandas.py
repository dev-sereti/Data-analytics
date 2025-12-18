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
nulls = data.isna().sum().sort(ascending = False)


# Cardinalities for key identifiers
df["transaction_id"].nunique(), df["order_id"].nunique(), df["customer_id"].nunique()