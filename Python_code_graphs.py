import pandas as pd
import matplotlib.pyplot as plt

file_path_csv = '/Users/terezasaskova/Desktop/python/sleep vs training.csv'
data_csv = pd.read_csv(file_path_csv)

#correct delimiter
data_csv = pd.read_csv(file_path_csv, delimiter=';')

# Display the first few rows - understand its structure
data_csv.head()

# Clean the TSS column - replacing commas with dots and converting to float
data_csv['TSS'] = data_csv['TSS'].str.replace(',', '.').astype(float)


# Convert the 'Date' column to datetime
data_csv['Date'] = pd.to_datetime(data_csv['Date'], format='%d-%m-%Y')

# Set the 'Date' column as the index
data_csv.set_index('Date', inplace=True)

# Plot Sleep performance (TSS over time)
plt.figure(figsize=(14, 7))

# Plot Sleep performance
plt.plot(data_csv.index, data_csv['Sleep performance %'], label='Sleep Performance %', marker='o')
# Plot TSS
plt.plot(data_csv.index, data_csv['TSS'], label='TSS', marker='x')

plt.title('Sleep Performance and TSS Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show plot
plt.show()

import matplotlib.pyplot as plt

# Reload the data
data_csv = pd.read_csv('/Users/terezasaskova/Desktop/python/sleep vs training.csv', delimiter=';')

# Convert the 'Date' column to datetime
data_csv['Date'] = pd.to_datetime(data_csv['Date'], format='%d-%m-%Y')

# Set the 'Date' column as the index
data_csv.set_index('Date', inplace=True)

# Clean the TSS column by replacing commas with dots and converting to float
data_csv['TSS'] = data_csv['TSS'].str.replace(',', '.').astype(float)

# Scatter plot showing the relationship between Sleep Performance % and TSS
plt.figure(figsize=(10, 6))
plt.scatter(data_csv['Sleep performance %'], data_csv['TSS'], c='blue', alpha=0.5)
plt.title('Relationship between Sleep Performance % and TSS')
plt.xlabel('Sleep Performance %')
plt.ylabel('TSS')
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()

# Bar plot comparing TSS across different WorkoutTypes
plt.figure(figsize=(12, 6))
data_csv.groupby('WorkoutType')['TSS'].mean().sort_values().plot(kind='bar', color='skyblue')
plt.title('Average TSS by Workout Type')
plt.xlabel('Workout Type')
plt.ylabel('Average TSS')
plt.grid(axis='y')
plt.tight_layout()

# Show plot
plt.show()

import pandas as pd

# Reload the data
data_csv = pd.read_csv('/Users/terezasaskova/Desktop/python/sleep vs training.csv', delimiter=';')

# Convert the 'Date' column to datetime
data_csv['Date'] = pd.to_datetime(data_csv['Date'], format='%d-%m-%Y')

# Set the 'Date' column as the index
data_csv.set_index('Date', inplace=True)

# Clean the TSS column by replacing commas with dots and converting to float
data_csv['TSS'] = data_csv['TSS'].str.replace(',', '.').astype(float)

# Calculate the correlation matrix for the sleep metrics
sleep_metrics = data_csv[['sleep', 'Sleep performance %', 'Deep (SWS) duration (min)', 'TSS']]

#sleep column to duration in minutes
sleep_metrics['sleep'] = pd.to_timedelta(data_csv['sleep']).dt.total_seconds() / 60

#the correlation matrix
df= correlation_matrix = sleep_metrics.corr()
df

import seaborn as sns
import matplotlib.pyplot as plt

# Plot a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
