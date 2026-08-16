import pandas as pd
import numpy as np

# Dataset
data = {
    "name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eva",
        "Bob"
    ],

    "age": [
        22,
        25,
        np.nan,
        30,
        150,
        25
    ],

    "salary": [
        50000,
        60000,
        55000,
        np.nan,
        65000,
        60000
    ],

    "department": [
        "CS",
        "cs",
        "Math",
        "Math",
        "CS",
        "cs"
    ]
}

df = pd.DataFrame(data)


# =========================
# Task 1 — Inspect
# =========================

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())


# =========================
# Task 2 — Find Duplicates
# =========================

print("\nDuplicate Rows:")
print(df.duplicated())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())


# =========================
# Task 3 — Investigate Age
# =========================

print("\nAge Column:")
print(df["age"])

print("\nAge Statistics:")
print(df["age"].describe())

# 150 is suspicious because it is much higher
# than the other ages.
# We will NOT change it yet.


# =========================
# Task 4 — Fix Department
# =========================

df["department"] = df["department"].replace({
    "cs": "CS"
})

print("\nDepartment After Cleaning:")
print(df["department"])


# =========================
# Task 5 — Handle Missing Salary
# =========================

mean_salary = df["salary"].mean()

print("\nMean Salary:")
print(mean_salary)

df["salary"] = df["salary"].fillna(mean_salary)


# =========================
# Task 6 — Remove Duplicate
# =========================

df = df.drop_duplicates()


# =========================
# Final DataFrame
# =========================

print("\nFinal DataFrame:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows After Cleaning:")
print(df.duplicated().sum())

print("\n========== FINAL VALIDATION ==========")

print("Shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDepartments:")
print(df["department"].unique())

print("\nAge statistics:")
print(df["age"].describe())