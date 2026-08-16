import numpy as np 

#data representaion is home/house : area | bedrooms | bathrooms
X = np.array([
    [1000, 2, 1],
    [1500, 3, 2],
    [2000, 4, 2],
    [2500, 5, 3],
    [3000, 6, 4]
])

weights = np.array([200, 50000, 30000])
bias = 10000

dataset_shape = X.shape

mins = X.min(axis=0)
maxs = X.max(axis=0)

X_scaled = (X - mins) / (maxs - mins)

print(dataset_shape,mins,maxs)
print()
print(X_scaled)
print()
prediction = X @ weights
print(prediction)
print()
prediction_with_bias = X @ weights + bias
print(prediction_with_bias)

