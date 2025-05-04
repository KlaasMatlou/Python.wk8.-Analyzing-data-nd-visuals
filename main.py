# Task 1 : Load and Explore the Dataset

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Error handling while loading dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame
    print("Dataset loaded succesfully")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display first few rows
print("first 5 rows:")
print(df.head())

# Check data types and missing values
print("Data Types:")
print(df.dtypes)

print("n\Missing Values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis

print("\nBasic Statistics:")
print(df.describe())

# Group by species and compute mean of numerical column for each group
grouped = df.groupby('target').mean()
print("\nMean values grouped by species (target):")
print(grouped)

# identify any partens or interesting findings
print("\nInsight:")
print("From the grouped data, you can see how each species differs in sepal and petal measurements.")


# Task 3: Data Visualization

#1. Line Chart showing trend over time
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label='Sepal Length')
plt.title('Line Chart: Sepal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()


# 2. Bar Chart- average petal length by species
plt.figure(figsize=(8, 5))
sns.barplot(x='target', y='petal length (cm)', data=df)
plt.title('Bar Chart: Average Petal Length by Species')
plt.xlabel('species')
plt.ylabel('Average petal length (cm)')
plt.show()

#3. Histogram of a numerical column
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal width (cm)'], kde=True, bins=20, color='blue')
plt.title('Histogram: Sepal Width Distribution')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('frequency')
plt.show()

#4. Scartter plot between sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='target', data=df, palette='Set1')
plt.title('Scatter Plot: Sepal Length vs Petal Length')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend(title='Species')
plt.show()

