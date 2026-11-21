from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. LOAD IRIS DATASET
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

# 2. DISPLAY DATASET
print("FIRST 5 ROWS:")
print(df.head())

print("\nDATASET SHAPE:")
print(df.shape)

print("\nCOLUMN NAMES:")
print(df.columns)

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nFLOWER SPECIES:")
print(iris.target_names)

# 3. STATISTICAL SUMMARY
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# 4. SPECIES DISTRIBUTION
print("\nSPECIES DISTRIBUTION:")
print(df["species"].value_counts())

# 5. DATA VISUALIZATION
sns.set_theme(style="whitegrid")

# Histogram
df[iris.feature_names].hist(figsize=(10, 8))
plt.suptitle("Iris Feature Distribution")
plt.tight_layout()
plt.savefig("images/iris_histogram.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="species"
)
plt.title("Iris Sepal and Petal Length")
plt.savefig("images/iris_scatter_plot.png")
plt.show()

# Box Plot
plt.figure(figsize=(9, 5))
sns.boxplot(data=df[iris.feature_names])
plt.title("Iris Features Box Plot")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("images/iris_boxplot.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    df[iris.feature_names].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Iris Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/iris_heatmap.png")
plt.show()

# 6. MACHINE LEARNING MODEL
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL ACCURACY:", accuracy * 100, "%")

print("\nCLASSIFICATION REPORT:")
print(classification_report(
    y_test,
    y_pred,
    target_names=iris.target_names
))

# 7. SAVE MODEL
joblib.dump(model, "models/iris_model.pkl")

print("\nModel saved successfully!")

# 8. INSIGHTS
print("\nIRIS DATASET INSIGHTS:")
print("1. The dataset contains 150 flower records.")
print("2. There are 3 different flower species.")
print("3. Each flower has 4 measurement features.")
print("4. Petal measurements help distinguish flower species.")
print("5. Random Forest model was trained successfully.")