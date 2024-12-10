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

# Calculate the learning metric for each animal
learning_results = {}
learning_slopes = {}

for animal, vector in animal_vectors.items():
    if len(vector) >= 5:  # Ensure there are enough trials
        # Convert strings to integers
        vector = list(map(int, vector))
        if animal == "C2R":
            numerator = vector[2] + vector[4]  # Use 3rd + 5th trial for C2R
        else:
            numerator = vector[4] + vector[3]  # Use 5th + 4th trial for other animals
        denominator = vector[0] + vector[1]  # 1st + 2nd trial

        if denominator > 0:  # Avoid division by zero
            learning_metric = numerator / denominator
            learning_results[animal] = "Learning" if learning_metric > 1 else "No Learning"
        else:
            learning_results[animal] = "Undefined (Denominator = 0)"
    else:
        learning_results[animal] = "Insufficient Data"

    # Calculate the slope for each animal
    trials = list(range(1, len(vector) + 1))
    if animal == "C2R":
        filtered_trials = [1, 2, 3, 5]
        filtered_durations = [vector[0], vector[1], vector[2], vector[4]]
    else:
        filtered_trials = trials
        filtered_durations = vector

    slope, intercept, _, _, _ = linregress(filtered_trials, filtered_durations)
    learning_slopes[animal] = slope

# Print the learning results
print("\nLearning Results:")
for animal, result in learning_results.items():
    print(f"{animal}: {result}")

# Print the slopes
print("\nLearning Slopes:")
for animal, slope in learning_slopes.items():
    print(f"{animal}: Slope = {slope}")

# Plot the linear regression for each animal
plt.figure(figsize=(12, 8))
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown', 'pink']

for i, (animal, vector) in enumerate(animal_vectors.items()):
    if len(vector) >= 5:
        trials = list(range(1, len(vector) + 1))
        if animal == "C2R":
            filtered_trials = [1, 2, 3, 5]
            filtered_durations = [vector[0], vector[1], vector[2], vector[4]]
        else:
            filtered_trials = trials
            filtered_durations = vector

        slope, intercept, _, _, _ = linregress(filtered_trials, filtered_durations)
        regression_line = [slope * x + intercept for x in filtered_trials]

        plt.plot(filtered_trials, filtered_durations, 'o-', label=f'{animal} (Data)', color=colors[i % len(colors)])
        plt.plot(filtered_trials, regression_line, '--', label=f'{animal} (Regression)', color=colors[i % len(colors)])

# Add plot details
plt.xlabel('Trial', fontsize=12)
plt.ylabel('Duration (sec)', fontsize=12)
plt.title('Linear Regression of Learning for Each Mouse', fontsize=14)
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()
plt.show()
