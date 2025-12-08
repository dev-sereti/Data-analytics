import pandas as pd

# Remove Rows
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")
cleanData = data.dropna()
print(cleanData.to_string)