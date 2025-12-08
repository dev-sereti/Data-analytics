import pandas as pd

# Remove Rows
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")
data.dropna(inplace=True)
print(data.to_string)

#Replace Empty Values

data.fillna(130, inplace=True)