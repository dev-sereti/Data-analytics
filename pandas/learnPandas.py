import pandas as pd

#Series (1D)
numberPlate = ["KCA203J","KDA253U","KBC678D"]

availablePlates = pd.Series(numberPlate)
print (availablePlates)

# dataset = {
#     'carModels': ["Ford","BMW","Ford"],
#     'numberPlate':["KCA203J","KDA253U","KBC678D"]
# }

# carData = pd.DataFrame(dataset)
# print(carData)