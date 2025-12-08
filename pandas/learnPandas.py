import pandas as pd

#Series (1D)
numberPlate = ["KCA203J","KDA253U","KBC678D"]

availablePlates = pd.Series(numberPlate, index= ["1","2","3"])
print (availablePlates[2])

# dataset = {
#     'carModels': ["Ford","BMW","Ford"],
#     'plateNumber':["KCA203J","KDA253U","KBC678D"]
# }

# carData = pd.DataFrame(dataset)
# print(carData)