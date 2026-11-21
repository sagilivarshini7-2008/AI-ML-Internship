import pandas as pd

# Load student dataset
df = pd.read_csv("data/student_performance.csv")

# Display project title
print("=" * 50)
print("       STUDENT PERFORMANCE DATA EXPLORER")
print("=" * 50)

# Display first five records
print("\n1. STUDENT DATA")
print(df.head())

# Dataset information
print("\n2. DATASET INFORMATION")
print("Total Students:", df.shape[0])
print("Total Columns:", df.shape[1])

# Column details
print("\n3. COLUMN NAMES")
print(df.columns.tolist())

# Check missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# Statistical summary
print("\n5. STATISTICAL SUMMARY")
print(df.describe())

print("\nDataset loaded successfully!")

# 6. DATA CLEANING

print("\n6. DATA CLEANING")

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with column averages
numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

print("Data cleaning completed!")
print("Remaining missing values:", df.isnull().sum().sum())

# 7. PERFORMANCE CALCULATION

df["Average_Marks"] = df[
    ["Math_Score", "Science_Score", "English_Score"]
].mean(axis=1)

# Assign grades
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

df["Grade"] = df["Average_Marks"].apply(calculate_grade)

print("\n7. STUDENT PERFORMANCE")
print(df[["Name", "Average_Marks", "Grade"]])

# 8. PERFORMANCE ANALYSIS

print("\n" + "=" * 50)
print("           PERFORMANCE ANALYSIS")
print("=" * 50)

# Overall class average
class_average = df["Average_Marks"].mean()
print("\nClass Average:", round(class_average, 2))

# Top-performing student
top_student = df.loc[df["Average_Marks"].idxmax()]
print("\nTop Performer:", top_student["Name"])
print("Average Marks:", round(top_student["Average_Marks"], 2))

# Lowest-performing student
low_student = df.loc[df["Average_Marks"].idxmin()]
print("\nLowest Performer:", low_student["Name"])
print("Average Marks:", round(low_student["Average_Marks"], 2))

# Subject-wise average
print("\nSubject-wise Average Marks:")
print(df[["Math_Score", "Science_Score", "English_Score"]].mean())

# Grade distribution
print("\nGrade Distribution:")
print(df["Grade"].value_counts().sort_index())

# 9. DATA VISUALIZATION

import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# 1. Student Average Marks
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="Name", y="Average_Marks")
plt.title("Student Average Performance")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/student_average_performance.png")
plt.show()

# 2. Subject-wise Performance
subject_averages = df[
    ["Math_Score", "Science_Score", "English_Score"]
].mean()

plt.figure(figsize=(8, 5))
subject_averages.plot(kind="bar")
plt.title("Subject-wise Average Performance")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("images/subject_performance.png")
plt.show()

# 3. Grade Distribution
plt.figure(figsize=(7, 5))
df["Grade"].value_counts().sort_index().plot(kind="pie", autopct="%1.1f%%")
plt.title("Student Grade Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/grade_distribution.png")
plt.show()

print("\nAll visualizations created successfully!")

# 10. EXPORT FINAL RESULTS

# Save cleaned dataset with calculated performance
df.to_csv("reports/student_performance_report.csv", index=False)

print("\n" + "=" * 50)
print("PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 50)

print("Total Students Analysed:", len(df))
print("Class Average:", round(df["Average_Marks"].mean(), 2))
print("Report saved in reports folder.")

# 11. HISTOGRAM

plt.figure(figsize=(8, 5))
plt.hist(df["Average_Marks"], bins=5)
plt.title("Average Marks Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.savefig("images/average_marks_histogram.png")
plt.show()

# 12. SCATTER PLOT

plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Average_Marks"])
plt.title("Study Hours vs Average Marks")
plt.xlabel("Study Hours")
plt.ylabel("Average Marks")
plt.savefig("images/study_hours_scatter.png")
plt.show()

# 13. BOX PLOT

plt.figure(figsize=(8, 5))
sns.boxplot(data=df[["Math_Score", "Science_Score", "English_Score"]])
plt.title("Subject Scores Box Plot")
plt.savefig("images/subject_scores_boxplot.png")
plt.show()

# 14. CORRELATION HEATMAP

plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Student Performance Correlation")
plt.savefig("images/student_correlation_heatmap.png")
plt.show()

print("All additional graphs created successfully!")