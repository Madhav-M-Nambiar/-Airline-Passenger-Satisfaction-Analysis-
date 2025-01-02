import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (assuming the dataset is a CSV file)
df = pd.read_csv(r"C:\Users\m8494\Downloads\Airline Feedback.csv")

# Filter data for high and low satisfaction
high_satisfaction = df[df['Satisfaction'] > 4]
low_satisfaction = df[df['Satisfaction'] < 4]

# List of factors to analyze
factors1 = ['Inflight_Service', 'Seat_Comfort', 'Cleanliness', 'Food_Quality']

mean_values = high_satisfaction[factors1].mean()
# Calculate the average rating for each factor for high and low satisfaction
plt.figure(figsize=(10, 6))
mean_values.plot(kind='bar', color='green')
plt.title('Satisfaction level (Mean of Factors)')
plt.ylabel('Mean Value')
plt.xlabel('Factors')
plt.show()

factors = ['Departure_Delays', 'Arrival_Delays']

# Calculate the mean values for each factor in low satisfaction group
mean_values = low_satisfaction[factors].mean()

# Plot the mean values for each factor for dissatisfied passengers (Satisfaction < 4)
plt.figure(figsize=(10, 6))
mean_values.plot(kind='bar', color='red')
plt.title('Common Causes of Complaints (Mean of Factors)')
plt.ylabel('Mean Value')
plt.xlabel('Factors')
plt.show()

# A. Age vs Satisfaction (Scatter Plot)
plt.figure(figsize=(8, 6))
plt.scatter(df['Age'], df['Satisfaction'], alpha=0.5, color='green')
plt.title('Age vs Satisfaction')
plt.xlabel('Age')
plt.ylabel('Satisfaction')
plt.show()

# Group by gender and calculate the mean satisfaction
gender_satisfaction = df.groupby('Gender')['Satisfaction'].mean()

# Plot the average satisfaction by gender
plt.figure(figsize=(8, 6))
gender_satisfaction.plot(kind='bar', color=['blue', 'orange'])
plt.title('Average Satisfaction by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Satisfaction')
plt.xticks(rotation=0)
plt.show()
