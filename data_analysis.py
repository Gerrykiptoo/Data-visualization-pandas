import pandas as pd
import matplotlib.pyplot as plt

# Load data
students = pd.read_csv('students.csv')

# Show first 5 rows
print("First 5 rows:")
print(students.head())

# Create plots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Bar chart (only numeric columns)
numeric_cols = students.select_dtypes(include=['int64','float64']).columns
students.groupby('Grade_Level')[numeric_cols].mean().plot(kind='bar', ax=axs[0, 0])
axs[0, 0].set_title('Average Scores by Grade')

# Plot 2: Histogram
students['Math_Score'].plot.hist(ax=axs[0, 1], bins=5, edgecolor='black')
axs[0, 1].set_title('Math Scores Distribution')

# Plot 3: Scatter plot
students.plot.scatter(x='Math_Score', y='Science_Score', ax=axs[1, 0], color='green')
axs[1, 0].set_title('Math vs Science Scores')

# Plot 4: Box plot
students[numeric_cols].boxplot(ax=axs[1, 1])
axs[1, 1].set_title('Score Distribution')

# Save and show
plt.tight_layout()
plt.savefig('analysis_results.png')
plt.show()