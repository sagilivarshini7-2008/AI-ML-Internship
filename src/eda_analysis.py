import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create student dataset
data = {
    "Name": ["Varshini", "Rahul", "Priya", "Arjun", "Sneha"],
    "Marks": [85, 90, 78, 95, 88],
    "Age": [18, 20, 19, 21, 18]
}

df = pd.DataFrame(data)

# 1. Display dataset
print("Student Dataset:")
print(df)

# 2. Basic information
print("\nDataset Information:")
print(df.info())

# 3. Statistical analysis
print("\nMean:")
print(df["Marks"].mean())

print("\nMedian:")
print(df["Marks"].median())

print("\nMode:")
print(df["Marks"].mode())

print("\nMinimum Marks:")
print(df["Marks"].min())

print("\nMaximum Marks:")
print(df["Marks"].max())

# 4. Bar chart
plt.figure(figsize=(7, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("student_marks.png")
plt.show()

# 5. Histogram
plt.figure(figsize=(7, 5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("marks_distribution.png")
plt.show()

# 6. Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[["Age", "Marks"]].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

print("\nEDA Completed Successfully!")