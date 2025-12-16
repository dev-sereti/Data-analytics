# Copy and View in Numpy
import numpy as np

data = np.array([1,1,1,2,3,3,4,4,8,])
newData = data.copy()

#Make changes to original array
data[4] = 23

print(data)
print(newData)