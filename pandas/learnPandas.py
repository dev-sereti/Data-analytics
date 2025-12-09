import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\VF3535\Documents\Analytics\pandas\data.csv")

# parse Date robustly
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# set Date as index so time series plots look correct
data = data.set_index('Date')

# plot
ax = data['Calories'].plot(title='Calories over time', xlabel='Date', ylabel='Calories')

# show the plot window
plt.show()
