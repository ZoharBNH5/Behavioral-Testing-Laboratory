import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

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

# Print the vectors for each animal
for animal, vector in animal_vectors.items():
    print(f"{animal}: {vector}")

# Calculate the learning metric for each animal
learning_results = {}

for animal, vector in animal_vectors.items():
    # Ensure the vector has at least 5 values
    if len(vector) >= 5:
        # Convert strings to integers
        vector = list(map(int, vector))
        if animal == "C2R":
            numerator = vector[3] + vector[5]  # Use 3rd + 5th trial for C2R
        else:
            numerator = vector[3] + vector[4]  # Use 4th + 5th trial for other animals
        denominator = vector[0] + vector[1]  # 1st + 2nd trial

        if denominator > 0:  # Avoid division by zero
            learning_metric = numerator / denominator
            learning_results[animal] = "Learning" if learning_metric > 1 else "No Learning"
        else:
            learning_results[animal] = "Undefined (Denominator = 0)"
    else:
        learning_results[animal] = "Insufficient Data"

# Print the learning results
print("\nLearning Results:")
for animal, result in learning_results.items():
    print(f"{animal}: {result}")

# Calculate the slopes for each animal
learning_slopes = {}

for animal, vector in animal_vectors.items():
    if len(vector) >= 5:  # Ensure there are enough trials
        trials = list(range(1, len(vector) + 1))
        if animal == "C2R":
            # Ignore 4th trial for C2R
            filtered_trials = [1, 2, 3, 5]
            filtered_durations = [vector[0], vector[1], vector[2], vector[4]]
        else:
            filtered_trials = trials
            filtered_durations = vector

        slope, _, _, _, _ = linregress(filtered_trials, filtered_durations)
        learning_slopes[animal] = slope

# Plot learning slopes for each animal
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown', 'pink']
plt.figure(figsize=(10, 6))

for i, (animal, slope) in enumerate(learning_slopes.items()):
    plt.bar(animal, slope, color=colors[i % len(colors)], edgecolor='black')

# Add labels and title
plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Add a line at slope=0
plt.xlabel('Mouse ID', fontsize=12)
plt.ylabel('Slope of Performance (Learning Trend)', fontsize=12)
plt.title('Learning Slopes for Each Mouse', fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()
plt.show()
