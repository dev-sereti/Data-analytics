import pandas as pd

# Load data
data = pd.read_csv( r"C:\Users\Kelvin\Documents\Sereti\Data-analytics\pandas\Datasets\Retail Transactions.csv")
print(data.head(10))
#Parse dates
date_cols = ["signup_date","last_login","order_date","ship_date"]
