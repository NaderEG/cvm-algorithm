import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file_path = 'data_stream_analysis_B4.csv'  # Replace with the actual file path
df = pd.read_csv(csv_file_path)

# Extract relevant columns
buffer_size = df['Buffer Size']
lowest_attempt = df['Lowest Attempt']
highest_attempt = df['Highest Attempt']
num_distinct_elements = df['Num Distinct Elements']
med_of_10 = df['Med of 10']

# Plot the data
plt.plot(buffer_size, lowest_attempt, label='Lowest Attempt')
plt.plot(buffer_size, highest_attempt, label='Highest Attempt')
plt.plot(buffer_size, num_distinct_elements, label='Num Distinct Elements')
plt.plot(buffer_size, med_of_10, label='Med of 10')

# Set labels and title
plt.xlabel('Buffer Size')
plt.ylabel('Prediction')
plt.title('Prediction with Multiple Metrics')

# Add a legend
plt.legend()

# Save the plot as an image file with the same name as the CSV file but add "_variance" to the end
output_file_path = csv_file_path.replace('.csv', '_variance.png')
plt.savefig(output_file_path)

# Show the plot
plt.show()