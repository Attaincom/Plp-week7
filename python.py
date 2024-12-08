import pandas as pd

# Load the dataset
df = pd.read_csv("bank.csv")

# Display the first few rows
df.head()

# Check data types
df.info()

# Check for missing values
df.isnull().sum()
# Summary statistics
df.describe()

# Grouping and aggregation
grouped_data = df.groupby("categorical_column")["numerical_column"].mean()
print(grouped_data)

import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Example: Trend over time
plt.figure(figsize=(10, 6))
plt.plot(df['date_column'], df['numerical_column'], marker='o')
plt.title("Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.show()


plt.figure(figsize=(8, 6))
sns.barplot(x="categorical_column", y="numerical_column", data=df)
plt.title("Average Value by Category")
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df["numerical_column"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Numerical Column")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x="numerical_column1", y="numerical_column2", hue="categorical_column", data=df)
plt.title("Relationship Between Two Numerical Columns")
plt.show()
