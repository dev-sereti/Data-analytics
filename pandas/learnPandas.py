import pandas as pd

# Remove Rows
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")

#Mean
newData = data["Calories"].mean()
data.fillna({"Calories":newData}, inplace = True)

#Median
newData = data["Calories"].median()
data.fillna({"Calories":newData}, inplace = True)
