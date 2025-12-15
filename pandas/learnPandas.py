# import os
# print(os.getcwd())
import pandas as pd

data = pd.read_csv(
    r"C:\Users\VF3535\Documents\Analytics\sample_retail_transactions_dataset.csv",
    parse_dates=["order_dates", "ship_date", "signup_date", "last_login"]
)

print(data.shape)

