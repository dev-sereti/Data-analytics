import pandas as pd
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")
print(data.columns)
# Convert date column to datetime
# data['date'] = pd.to_datetime(data['date'])
# Pandas - Data Correlations
# data.corr()