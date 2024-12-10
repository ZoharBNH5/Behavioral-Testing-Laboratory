# Redefine and rerun the provided code snippet
import numpy as np
import pandas as pd
from scipy.io import loadmat
from scipy.stats import pearsonr

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
    animal_vectors[animal.strip()] = durations  # Ensure no extra spaces

mean_durations = {}
# Filter animal_vectors and remove the 4th trial for C2R
filtered_animal_vectors = {}
for animal, vector in animal_vectors.items():

    if len(vector) >= 5:
        if animal == "C2R":
            # Exclude the 4th trial without renumbering the rest
            filtered_animal_vectors[animal] = [vector[i] for i in [0, 1, 2, 4]]  # Skip index 3 (4th trial)
        else:
            filtered_animal_vectors[animal] = vector
        mean_duration = np.mean(vector)  # Calculate the mean for the current animal
        mean_durations[animal] = {"mean_duration": mean_duration}

print(f"Mean durations per animal: {mean_durations}")

data_files = {
    'C1B': 'C1B_271124_new.mat',
    'C2B': 'C2B_271124_new.mat',
    'C1G': 'C1G_241124_new.mat',
    'C2G': 'C2G_271124_new.mat',
    'C1R': 'C1R_271124_new.mat',
    'C2R': 'C2R_271124_new.mat',
    'C1W': 'C1W_241124_new.mat',
    'C2W': 'C2W_271124_new.mat'
}

for animal, file in data_files.items():
    mat_data = loadmat(file)
    crossing_times = mat_data.get('crossing_times', None)
    if crossing_times is not None:
        crossing_times = crossing_times.flatten()  # Convert to a flat list
    else:
        crossing_times = []
    if animal in mean_durations:
        mean_durations[animal]["number_of_crossings"] = len(crossing_times)

# Print the final dictionary
print("Animal Data (Mean Duration and Crossing Times):")
print(mean_durations)

# Prepare data for the scatter plot
x_values = []  # Number of crossings
y_values = []  # Mean durations
colors = []    # Colors for different mice
labels = []    # Mouse labels

# Assign a unique color to each mouse
color_map = {
    'C1B': 'red', 'C2B': 'blue', 'C1G': 'green', 'C2G': 'orange',
    'C1R': 'purple', 'C2R': 'brown', 'C1W': 'pink', 'C2W': 'cyan'
}

for animal, data in mean_durations.items():
    if isinstance(data, dict):  # Ensure it's a dictionary
        x_values.append(data.get("number_of_crossings", 0))  # Default to 0 if key is missing
        y_values.append(data.get("mean_duration", 0))  # Default to 0 if key is missing
        colors.append(color_map.get(animal, 'black'))  # Default to black if mouse is not in color_map
        labels.append(animal)

# Calculate Pearson correlation
correlation, p_value = pearsonr(x_values, y_values)

# Create the scatter plot
plt.figure(figsize=(10, 6))
for i in range(len(x_values)):
    plt.scatter(x_values[i], y_values[i], color=colors[i], label=labels[i], s=100)  # s=100 for larger dots

# Add labels and title
plt.xlabel("Number of Crossings", fontsize=12)
plt.ylabel("Mean Duration (sec)", fontsize=12)
plt.title("Number of Crossings vs Mean Duration", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Adjust plot to make space for text
plt.subplots_adjust(top=0.85)  # Reduce the space for the graph to add text above

# Add Pearson correlation details outside the plot area
text = f"Pearson Correlation Coefficient: {correlation:.2f}\nP-value: {p_value:.4f}"
plt.gcf().text(
    0.5, 0.92, text, fontsize=12, ha='center',
    bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)
)

# Ensure unique labels in the legend
handles, unique_labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(unique_labels, handles))
plt.legend(by_label.values(), by_label.keys(), title="Mouse", fontsize=10, title_fontsize=12)

# Show the plot
plt.show()

# Ensure all entries in mean_durations are dictionaries
mean_durations = {
    animal: data if isinstance(data, dict) else {"mean_duration": data, "number_of_crossings": 0}
    for animal, data in mean_durations.items()
}

# Extract x (number of crossings) and y (mean duration) values
x_values = [data["number_of_crossings"] for data in mean_durations.values()]
y_values = [data["mean_duration"] for data in mean_durations.values()]

# Calculate Pearson correlation
correlation, p_value = pearsonr(x_values, y_values)

# Display the results
print(f"Pearson Correlation Coefficient: {correlation:.2f}")
print(f"P-value: {p_value:.4f}")