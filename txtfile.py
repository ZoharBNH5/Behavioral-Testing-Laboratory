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
    animal_vectors[animal.strip()] = durations  # Ensure no extra spaces

# Filter animal_vectors and remove the 4th trial for C2R
filtered_animal_vectors = {}
for animal, vector in animal_vectors.items():
    if len(vector) >= 5:
        if animal == "C2R":
            # Exclude the 4th trial without renumbering the rest
            filtered_animal_vectors[animal] = [vector[i] for i in [0, 1, 2, 4]]  # Skip index 3 (4th trial)
        else:
            filtered_animal_vectors[animal] = vector

# Plot the data for all animals in a single graph without linear regression
plt.figure(figsize=(12, 8))

# Create individual plots for each animal
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown', 'black']

for i, (animal, vector) in enumerate(filtered_animal_vectors.items(), start=1):
    # plt.figure(figsize=(8, 6))

    # Recompute trial numbers but skip the 4th trial only for C2R
    if animal == "C2R":
        trials = [1, 2, 3, 5]  # Explicitly define trials for C2R
    else:
        trials = list(range(1, len(vector) + 1))

    # Plot the data points
    plt.plot(trials, vector, 'o-', label=animal, color=colors[i % len(colors)])


# Add plot details
plt.xticks(range(1, max([len(vector) for vector in filtered_animal_vectors.values()]) + 1))
plt.xlabel('Trial', fontsize=12)
plt.ylabel('Duration (sec)', fontsize=12)
plt.title('Learning Progression for All Animals', fontsize=14)
plt.grid(alpha=0.5)
plt.legend(title='Animal ID', fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()

import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Initialize dictionary to store trial data across all animals
trial_sums = {}
trial_counts = {}

# Iterate over all animals and compute the sum and count of durations for each trial
for animal, vector in filtered_animal_vectors.items():
    if animal == "C2R":
        trials = [1, 2, 3, 5]  # Skip the 4th trial for C2R
    else:
        trials = list(range(1, len(vector) + 1))

    for trial, duration in zip(trials, vector):
        if trial not in trial_sums:
            trial_sums[trial] = 0
            trial_counts[trial] = 0
        trial_sums[trial] += duration
        trial_counts[trial] += 1 if animal != "C2R" or trial != 4 else 0

# Calculate the average duration per trial (ignore C2R's 4th trial)
average_durations = {trial: trial_sums[trial] / (trial_counts[trial] if trial != 4 else 7) for trial in sorted(trial_sums.keys())}

# Prepare data for plotting
trials = sorted(average_durations.keys())
averages = [average_durations[trial] for trial in trials]

# Perform linear regression on the averages
slope, intercept, r_value, p_value, std_err = linregress(trials, averages)
regression_line = [slope * x + intercept for x in trials]

# Plot the averages with the regression line
plt.figure(figsize=(10, 6))
plt.plot(trials, averages, 'o-', label='Average Durations', color='blue')
plt.plot(trials, regression_line, '--', label=f'Regression Line (R²={r_value**2:.2f}\n pValue={p_value:.2f})', color='red')

# Customize the plot
plt.xlabel('Trial', fontsize=12)
plt.ylabel('Average Duration For All Mice(sec)', fontsize=12)
plt.title('Average Learning Progression Across All Mice', fontsize=14)
plt.xticks(trials)  # Show only the trial numbers on the x-axis
plt.grid(alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.show()

# Print regression summary
var = {
    "Slope": slope,
    "Intercept": intercept,
    "R-squared": r_value ** 2,
    "P-value": p_value,
    "Standard Error": std_err
}

print(f"Values for linear regression for the average learning progression graph:")
for key, value in var.items():
    print(f"{key}: {round(value, 5)}")


