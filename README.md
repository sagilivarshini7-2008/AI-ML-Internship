AI/ML Internship – Task 1

Student Performance Data Explorer

Project Overview

The Student Performance Data Explorer is a Python-based data analysis project developed as part of the AI/ML internship. It focuses on analysing student academic performance using Python programming, data processing, statistical analysis, machine learning and visualization techniques.

Objectives

- Understand Python fundamentals.
- Perform numerical operations using NumPy.
- Analyse datasets using Pandas.
- Clean and preprocess data.
- Perform Exploratory Data Analysis (EDA).
- Create meaningful data visualizations.
- Train a machine learning model using the Iris dataset.
- Analyse student academic performance.
- Calculate average marks and assign grades.
- Identify top and lowest-performing students.
- Compare subject-wise performance.

Technologies Used

- Python 3.12
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- Git and GitHub
- VS Code

Project Structure

AI-ML-Internship/
│
├── data/
│   └── student_performance.csv
│
├── src/
│   ├── test_setup.py
│   ├── python_fundamentals.py
│   ├── numpy_basics.py
│   ├── pandas_basics.py
│   ├── data_cleaning.py
│   ├── eda_analysis.py
│   ├── iris_dataset.py
│   ├── student_performance.py
│   └── generate_report.py
│
├── images/
│   ├── Student performance graphs (7 PNG files)
│   └── Iris dataset graphs (4 PNG files)
│
├── reports/
│   ├── student_performance_report.csv
│   └── AI_ML_EDA_Report.pdf
│
├── notebooks/
│   └── task1.ipynb
│
├── models/
│   └── iris_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore

Tasks Completed

1. Python Environment Setup
2. Python Fundamentals
3. NumPy Basics
4. Pandas Basics
5. Data Cleaning
6. Exploratory Data Analysis (EDA)
7. Data Visualization
8. Iris Dataset – Machine Learning Classification
9. Student Performance Data Explorer
10. Jupyter Notebook Documentation
11. GitHub Repository Management

Iris Dataset – Machine Learning

- Loaded and analysed the Iris dataset.
- Split the dataset into training and testing data.
- Trained a Random Forest Classifier.
- Evaluated the model using accuracy and classification report.
- Saved the trained model as "iris_model.pkl".

Model Accuracy: 100% on the test split used in this experiment.

Student Performance Data Explorer

The project analyses student marks across Mathematics, Science and English.

It performs the following operations:

- Reads student data from a CSV file.
- Calculates average marks.
- Assigns grades based on student performance.
- Identifies top and lowest-performing students.
- Calculates class and subject-wise averages.
- Generates performance visualizations.
- Exports the analysed results into a CSV report.

Project Outputs

- Student performance analysis.
- Class average and subject-wise averages.
- Student grades.
- Performance visualizations.
- Exported CSV report.
- Trained Iris machine learning model.

How to Run

1. Clone the repository

git clone https://github.com/sagilivarshini7-2008/AI-ML-Internship.git

2. Open the project folder

cd AI-ML-Internship

3. Install the required libraries

pip install -r requirements.txt

4. Run the Student Performance project

python src/student_performance.py

5. Run the Iris Dataset project

python src/iris_dataset.py

Conclusion

This internship project provided practical experience in Python programming, data manipulation, data cleaning, exploratory data analysis, visualization and machine learning.

It demonstrates how Python and machine learning techniques can be used to analyse datasets and generate meaningful insights.

Author

Sagili Varshini

GitHub: https://github.com/sagilivarshini7-2008
- AI/ML EDA PDF Report.

## AI/ML Project Lifecycle

```mermaid
flowchart TD
A[Problem Definition] --> B[Data Collection]
B --> C[Data Cleaning]
C --> D[Exploratory Data Analysis]
D --> E[Model Development]
E --> F[Model Evaluation]
F --> G[Model Deployment]
G --> H[Monitoring and Improvement]

[17:39, 21/11/2026] +91 93980 23619: ## EDA Workflow

```mermaid
flowchart TD
A[Load Dataset] --> B[Understand Data]
B --> C[Check Missing Values]
C --> D[Clean Data]
D --> E[Statistical Analysis]
E --> F[Create Visualizations]
F --> G[Find Insights]
G --> H[Prepare Report]

 ## Git and GitHub Workflow

```mermaid
flowchart TD
A[Create Project] --> B[Write Code]
B --> C[Git Add]
C --> D[Git Commit]
D --> E[Git Push]
E --> F[GitHub Repository]


 ## Project Folder Structure

```mermaid
flowchart TD
A[AI-ML-Internship] --> B[data]
A --> C[src]
A --> D[images]
A --> E[reports]
A --> F[notebooks]
A --> G[models]
A --> H[requirements.txt]
A --> I[README.md]