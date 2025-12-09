import pandas as pd

data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")

data['Date'] = pd.to_datetime(data['Date'], format='mixed')

print(data.corr(numeric_only=True))
