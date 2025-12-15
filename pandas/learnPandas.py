import pandas as pd

data = pd.read_csv("sample_retail_transactions_dataset.csv", 
parse_dates= ["order_dates","ship_date","signup_date","last_login"]
)

