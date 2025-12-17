# import os
# print(os.getcwd())
import pandas as pd

data = pd.read_csv(
    r"C:\Users\Kelvin\Documents\Sereti\Data-analytics\pandas\sample_retail_transactions_dataset.csv",
    parse_dates=["order_date", "ship_date", "signup_date", "last_login"]
)
