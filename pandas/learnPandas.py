import pandas as pd

# #Series (1D)
# numberPlate = ["KCA203J","KDA253U","KBC678D"]

# availablePlates = pd.Series(numberPlate, index= ["1","2","3"])
# #print (availablePlates[2])


# #DataFrames (2D)
# dataset = {
#     'carModels': ["Ford","BMW","Ford"],
#     'plateNumbers':["KCA203J","KDA253U","KBC678D"]
# }
# carData = pd.DataFrame(dataset, index = ["1","2","3"])
# # print(carData)
# print(carData.loc[3])


#Load Files Into a DataFrame

data = pd.read_csv('data.csv')

# Read CSV Files
print(data.to_string)
