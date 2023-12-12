import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path = 'data_stream_analysis_A6.csv'
data = pd.read_csv(file_path)

# Extract the columns for Buffer Size and Accuracy
buffer_size = data.iloc[:30, 0]
accuracy = data.iloc[:30, 5]

# Plotting
plt.plot(buffer_size, accuracy, marker='o', color='blue', label='Buffer Size vs Accuracy', linestyle='-')
plt.title('Buffer Size vs Accuracy')
plt.xlabel('Buffer Size')
plt.ylabel('Accuracy')
plt.legend()

plt.grid(True)
save_path = file_path.replace('.csv', '_v2.png')
plt.savefig(save_path)
plt.show()