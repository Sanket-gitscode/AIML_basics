import numpy as np 

X = np.array([
    [1000, 2, 1],
    [1500, 3, 2],
    [2000, 4, 2],
    [2500, 5, 3]
])


print(X.min(axis=0))
print(X.max(axis=0))


mins = (X.min(axis=0))
maxs =(X.max(axis=0))


X_scaled = (X - mins ) / (maxs - mins)

print(X_scaled)

print("X:", X.shape)
print("mins:", mins.shape)
print("maxs:", maxs.shape)
print("X_scaled:", X_scaled.shape)