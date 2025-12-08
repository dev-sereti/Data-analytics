import pandas as pd

#Python dictionary
dataset = {
    'carModels': ["Ford","BMW","Ford"],
    'numberPlate':["KCA203J","KDA253U","KBC678D"]
}

carData = pd.DataFrame(dataset)
print(carData)