# import os
# print(os.getcwd())
import pandas as pd

import pandas as pd

data = pd.read_csv(
    r"C:\Users\VF3535\Documents\Analytics\pandas\sample_retail_transactions_dataset.csv",
    parse_dates=["order_date", "ship_date", "signup_date", "last_login"]
)

# print(data.shape)
# print(data.dtypes)

# print (data.head (20))

remove_data_duplicates = data.drop_duplicates ()
#Drop duplicated orders
data_orders = data.drop_duplicates(subset=["order_id"])


# Handle missing ages: fill with median by gender
data_orders["customer_age"] = data_orders.groupby("gender")["customer_age"].transform(lambda s:s.fillna(s.median))