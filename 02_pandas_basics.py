import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'David', 'Charlie', 'Eva'],
    'age': [22, 25, 30, 21, 28],
    'scores': [85, 98, 78, 95, 88],
    "department": ["CS", "CS", "Math", "Math", "CS"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

print('-' * 50)

# Shape of the DataFrame
print(df.shape)

print('-' * 50)

# Column names
print(df.columns)

print('-' * 50)

# First 3 rows
print(df.head(3))

print('-' * 50)

# Students with scores greater than 85
print(df[df['scores'] > 85])

print('-' * 50)

# Students younger than 25
print(df[df['age'] < 25])

print('-' * 50)

# Students younger than 25 AND with scores greater than 80
filtered_students = df[(df['age'] < 25) & (df['scores'] > 80)]

print(filtered_students)

print('-' * 50)

# Total number of students
number_of_students = len(df)

# Total score
total_score = df['scores'].sum()

# Minimum score
min_score = df['scores'].min()

# Maximum score
max_score = df['scores'].max()

# Average / Mean score
mean_score = df['scores'].mean()

print("Number of students:", number_of_students)
print("Total score:", total_score)
print("Minimum score:", min_score)
print("Maximum score:", max_score)
print("Average score:", mean_score)

print('-' * 50)
grouped_scores = df.groupby('department')['scores'].mean()
print(grouped_scores)
print('-'*50)


# Exercise 1: Average score per department
average_score = df.groupby('department')['scores'].mean()
print("Average score per department:")
print(average_score)

# Exercise 2: Maximum score per department
max_score = df.groupby('department')['scores'].max()
print("\nMaximum score per department:")
print(max_score)

# Exercise 3: Minimum score per department
min_score = df.groupby('department')['scores'].min()
print("\nMinimum score per department:")
print(min_score)