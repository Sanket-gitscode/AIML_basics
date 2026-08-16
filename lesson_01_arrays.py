import numpy as np 
 
#X.shape = (number_of_samples, number_of_features)
# 4 → samples 
# # 2 → features


#ndim #Tells you how many dimensions array has 

#vectorization   - perform a single operation on all array at once 


import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(X.shape)
print(X.ndim)

print(X[0, 0])
print(X[1, 2])
print(X[0, :])
print(X[:, 1])

prices = np.array([100, 200, 300, 400])
prices =(prices * 1.10)
print(prices)

X = np.array([
    [1000, 2],
    [1500, 3],
    [2000, 4],
    [2500, 5]
])

X[:, 0] = X[:, 0] * 1.10

print(X)


a = np.array([10, 20, 30])
b = np.array([
    [10],
    [20],
    [30]
])

print(a.shape)
print(b.shape)

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers + 10)