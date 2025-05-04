# Dataset Analysis

## Overview

This assignment involves analyzing the famous **Iris dataset** using Python. The task was to load the dataset, perform basic data analysis, and visualize key features to draw insights about the differences between flower species.

## Contents

- `main.py`: The main Python script that loads the dataset, performs exploratory data analysis, and generates visualizations.
-  The images/ screenshots attached shows us the differences based on what their supposed to distinguish
- `line chart.png`: Line chart showing Sepal Length trend over time samples.
- `bar Chart_avg.png`: Bar chart showing average Petal Length by species.
- `histogram.png`: Histogram showing the distribution of Sepal Width.
- `scatter plot.png`: Scatter plot comparing Sepal Length vs Petal Length.

## Tasks Performed

1. **Data Loading and Exploration**
   - Loaded the Iris dataset using `sklearn.datasets`.
   - Checked data types and ensured there are no missing values.

2. **Basic Analysis**
   - Computed summary statistics using `.describe()`.
   - Grouped data by species and calculated the mean of each numeric feature.

3. **Visualizations**
   - **Line Chart**: Sepal Length vs Index
   - **Bar Chart**: Average Petal Length per Species
   - **Histogram**: Sepal Width Distribution
   - **Scatter Plot**: Sepal Length vs Petal Length with species color-coded

4. **Insight**
   - Species show clear differences in flower measurements.
   - Setosa generally has smaller petals and sepals compared to Virginica.
   - These measurements can be used to classify iris species accurately.
   - Setosa has the smallest petal length and width, while Virginica has the largest.
   - These differences can be useful for classification tasks.

## How to Run

1. Ensure you have Python installed (preferably 3.13 or later).
2. Install required packages if not already installed:
   ```bash
   pip install pandas seaborn matplotlib scikit-learn

3. Run the script `main.py`, the script will automatically open the graphs 
