import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Linear Relationship")

plt.show()

import matplotlib.pyplot as plt

age = [22, 25, 30, 35, 40]
salary = [45000, 52000, 65000, 72000, 85000]

plt.scatter(age, salary)

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()