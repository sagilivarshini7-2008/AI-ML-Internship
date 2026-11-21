import os
import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Table, TableStyle, Image, PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER

# Project folders
os.makedirs("reports", exist_ok=True)

# Create PDF
pdf = SimpleDocTemplate(
    "reports/AI_ML_EDA_Report.pdf"
)

styles = getSampleStyleSheet()
story = []

# Title
title_style = styles["Title"]
title_style.alignment = TA_CENTER

story.append(Paragraph(
    "AI/ML INTERNSHIP - EDA REPORT",
    title_style
))
story.append(Spacer(1, 20))

story.append(Paragraph(
    "Task: AI/ML Development Environment Setup, "
    "Python Foundations and Data Exploration",
    styles["Normal"]
))
story.append(Spacer(1, 15))

# 1. Introduction
story.append(Paragraph("1. Introduction", styles["Heading1"]))
story.append(Paragraph(
    "This project focuses on Python programming, "
    "data cleaning, exploratory data analysis and "
    "basic machine learning using Python libraries.",
    styles["BodyText"]
))
story.append(Spacer(1, 15))

# 2. Tools
story.append(Paragraph("2. Tools and Technologies", styles["Heading1"]))
story.append(Paragraph(
    "Python, Pandas, NumPy, Matplotlib, Seaborn, "
    "Scikit-learn, Jupyter Notebook, Git and GitHub.",
    styles["BodyText"]
))
story.append(Spacer(1, 15))

# 3. Student Performance Analysis
story.append(Paragraph(
    "3. Student Performance Analysis",
    styles["Heading1"]
))

df = pd.read_csv("data/student_performance.csv")

df = df.drop_duplicates()

numeric_columns = df.select_dtypes(include="number").columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

df["Average_Marks"] = df[
    ["Math_Score", "Science_Score", "English_Score"]
].mean(axis=1)

story.append(Paragraph(
    f"Total students analysed: {len(df)}",
    styles["BodyText"]
))
story.append(Paragraph(
    f"Class average marks: {df['Average_Marks'].mean():.2f}",
    styles["BodyText"]
))
story.append(Paragraph(
    f"Highest average marks: {df['Average_Marks'].max():.2f}",
    styles["BodyText"]
))
story.append(Paragraph(
    f"Lowest average marks: {df['Average_Marks'].min():.2f}",
    styles["BodyText"]
))
story.append(Spacer(1, 12))

# Subject averages table
subject_avg = df[
    ["Math_Score", "Science_Score", "English_Score"]
].mean()

table_data = [["Subject", "Average Marks"]]

for subject, marks in subject_avg.items():
    table_data.append([subject, f"{marks:.2f}"])

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("PADDING", (0, 0), (-1, -1), 8)
]))

story.append(table)
story.append(Spacer(1, 15))

# 4. Student visualizations
story.append(Paragraph(
    "4. Student Performance Visualizations",
    styles["Heading1"]
))

student_images = [
    "images/student_average_performance.png",
    "images/subject_performance.png",
    "images/grade_distribution.png",
    "images/average_marks_histogram.png",
    "images/study_hours_scatter.png",
    "images/subject_scores_boxplot.png",
    "images/student_correlation_heatmap.png"
]

for image_path in student_images:
    if os.path.exists(image_path):
        story.append(Image(image_path, width=6*inch, height=3.5*inch))
        story.append(Spacer(1, 10))

# 5. Iris Dataset
story.append(PageBreak())
story.append(Paragraph(
    "5. Iris Dataset Analysis",
    styles["Heading1"]
))

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions) * 100

story.append(Paragraph(
    "The Iris dataset contains 150 flower records, "
    "3 flower species and 4 measurement features.",
    styles["BodyText"]
))
story.append(Spacer(1, 10))

story.append(Paragraph(
    f"Random Forest model accuracy: {accuracy:.2f}%",
    styles["BodyText"]
))
story.append(Spacer(1, 15))

# Iris visualizations
iris_images = [
    "images/iris_histogram.png",
    "images/iris_scatter_plot.png",
    "images/iris_boxplot.png",
    "images/iris_heatmap.png"
]

for image_path in iris_images:
    if os.path.exists(image_path):
        story.append(Image(image_path, width=6*inch, height=3.5*inch))
        story.append(Spacer(1, 10))

# 6. Conclusion
story.append(Paragraph("6. Conclusion", styles["Heading1"]))
story.append(Paragraph(
    "This internship task helped develop practical "
    "knowledge of Python, data handling, data cleaning, "
    "data visualization, exploratory data analysis and "
    "machine learning. The project also provided "
    "experience with Git and GitHub.",
    styles["BodyText"]
))

# Generate PDF
pdf.build(story)

print("PDF report generated successfully!")
print("Location: reports/AI_ML_EDA_Report.pdf")