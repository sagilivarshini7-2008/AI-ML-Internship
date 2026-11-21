import pandas as pd

# 1. Creating a DataFrame
data = {
    "Name": ["Varshini", "Rahul", "Priya", "Arjun"],
    "Age": [18, 20, 19, 21],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

# 2. Display first rows
print("\nFirst two rows:")
print(df.head(2))

# 3. Display information
print("\nData information:")
print(df.info())

# 4. Statistical summary
print("\nStatistical summary:")
print(df.describe())

# 5. Select a column
print("\nStudent names:")
print(df["Name"])

# 6. Filter data
print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])

# 7. Calculate average
print("\nAverage marks:", df["Marks"].mean())

# 8. Add a new column
df["Result"] = ["Pass", "Pass", "Pass", "Pass"]

print("\nUpdated Data:")
print(df)