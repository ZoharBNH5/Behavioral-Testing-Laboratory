import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Define the file path
file_path = '271124.txt'

# Define the column names
columns = ['Date', 'Time', 'Speed', 'Zone #', 'Subject ID', 'Duration(sec)', 'End Speed', 'Message']

# Read the data into a DataFrame
data = pd.read_csv(file_path, sep='\t', names=columns, skiprows=1, engine='python')

# Create a dictionary to store the vectors for each animal
animal_vectors = {}

# Group the data by Subject ID and extract durations
grouped_data = data.groupby('Subject ID')

# Create vectors for each animal
for animal, group in grouped_data:
    durations = group['Duration(sec)'].head(5).tolist()  # Get the first 5 durations
    animal_vectors[animal] = durations

# Filter out the 4th trial for C2R
filtered_animal_vectors = {}
for animal, vector in animal_vectors.items():
    if len(vector) >= 5:
        if animal == "C2R":
            # Remove the 4th trial explicitly
            filtered_animal_vectors[animal] = [vector[0], vector[1], vector[2], vector[4]]
        else:
            filtered_animal_vectors[animal] = vector

# Plot the linear regression for each animal
plt.figure(figsize=(12, 8))
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown', 'pink']

for i, (animal, vector) in enumerate(filtered_animal_vectors.items()):
    trials = list(range(1, len(vector) + 1))

    # Perform linear regression
    slope, intercept, _, _, _ = linregress(trials, vector)
    regression_line = [slope * x + intercept for x in trials]

    # Plot the data points and regression line
    plt.plot(trials, vector, 'o-', label=f'{animal} (Data)', color=colors[i % len(colors)])
    plt.plot(trials, regression_line, '--', label=f'{animal} (Regression)', color=colors[i % len(colors)])

# Add plot details
plt.xlabel('Trial', fontsize=12)
plt.ylabel('Duration (sec)', fontsize=12)
plt.title('Linear Regression of Learning for Each Mouse', fontsize=14)
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
