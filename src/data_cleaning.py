import pandas as pd
import numpy as np

# Creating a dataset with missing values
data = {
    "Name": ["Varshini", "Rahul", "Priya", "Arjun", "Rahul"],
    "Age": [18, 20, np.nan, 21, 20],
    "Marks": [85, 90, 78, np.nan, 90]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 1. Find missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter Filling Missing Values:")
print(df)

# 3. Find duplicate records
print("\nDuplicate Records:")
print(df.duplicated())

# 4. Remove duplicate records
df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df)

# 5. Display cleaned dataset
print("\nFinal Cleaned Dataset:")
print(df)