import pandas as pd

# Remove Rows
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")

newData = data["Calories"].mean()
data.fillna({"Calories":newData}, inplace = True)