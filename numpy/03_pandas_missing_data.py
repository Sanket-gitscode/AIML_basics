import numpy as np
import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [22, np.nan, 25, 30, np.nan],
    "salary": [50000, 60000, np.nan, 70000, 65000]
}

df = pd.DataFrame(data)

# Exercise 1
print(df)

# Exercise 2
print(df.isnull().sum())

# Exercise 3
mean_age = df["age"].mean()
print("Mean age:", mean_age)

# Exercise 4
df["age"] = df["age"].fillna(mean_age)

# Exercise 5
median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)

# Exercise 6
print(df.isnull().sum())

print(df)