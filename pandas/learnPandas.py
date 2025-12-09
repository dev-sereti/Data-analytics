import pandas as pd
data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")


#Removing duplicates
print(data.duplicated())