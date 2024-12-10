import numpy as np
from scipy.io import loadmat
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Define the data_files dictionary
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

# Initialize a dictionary to store thigmotaxis values for all mice
all_thigmotaxis = {mouse: [] for mouse in data_files.keys()}
colors = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray']

bin_edges = np.arange(0, 600 + 150, 150)  # Bins of 2 minutes (150 seconds)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Midpoints for plotting

plt.figure(figsize=(12, 8))
# Iterate over all mice and calculate thigmotaxis per bin
for i, (mouse, file) in enumerate(data_files.items()):
    try:
        # Load the data file
        data = loadmat(file)

        # Extract necessary data
        crossing_times = data.get('crossing_times', None)
        periphery_times = data.get('periphery_times', None)

        if crossing_times is not None and periphery_times is not None:
            # Flatten arrays for processing
            crossing_times = crossing_times.flatten()
            periphery_times = periphery_times.flatten()

            # Calculate thigmotaxis per bin for the current mouse
            thigmotaxis_values = []
            for start, end in zip(bin_edges[:-1], bin_edges[1:]):
                crossings_in_bin = (crossing_times >= start) & (crossing_times < end)
                periphery_in_bin = (periphery_times >= start) & (periphery_times < end)

                total_crossings = np.sum(crossings_in_bin)
                peripheral_crossings = np.sum(periphery_in_bin)

                # Calculate Thigmotaxis for the bin
                thigmotaxis = (peripheral_crossings / total_crossings) * 100 if total_crossings > 0 else 0
                thigmotaxis_values.append(thigmotaxis)

            all_thigmotaxis[mouse] = thigmotaxis_values

            # Plot individual thigmotaxis lines
            # plt.figure(1)
            color = colors[i % len(colors)]
            plt.plot(bin_centers, thigmotaxis_values, marker='o', label=mouse, color=color)
        else:
            print(f"Missing data for mouse {mouse}: crossing_times or periphery_times not found.")
    except FileNotFoundError:
        print(f"File not found for mouse {mouse}: {file}")

# Add labels and legend
plt.title('Thigmotaxis Over Time for All Mice', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Thigmotaxis (%)', fontsize=14)
plt.xticks(bin_centers, labels=[f'{int(edge)}-{int(edge+150)}' for edge in bin_edges[:-1]])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend(title='Mouse ID and Regressions', fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Combine thigmotaxis values across all mice for each bin
average_thigmotaxis_per_bin = np.mean(
    [values for values in all_thigmotaxis.values() if values], axis=0
)

# Calculate Standard Deviation (SD) for each bin across all mice
std_dev_thigmotaxis_per_bin = np.std(
    [values for values in all_thigmotaxis.values() if values], axis=0
)

# Calculate the Coefficient of Variation (CV) for each bin
cv_thigmotaxis_per_bin = (std_dev_thigmotaxis_per_bin / average_thigmotaxis_per_bin) * 100

# Plotting the combined results with SD as error bars
plt.figure(figsize=(12, 8))
plt.bar(
    bin_centers,
    average_thigmotaxis_per_bin,
    width=110,
    color='lightgreen',
    edgecolor='black',
    label='Average Thigmotaxis (%)',
    yerr=std_dev_thigmotaxis_per_bin,  # Adding SD as error bars
    capsize=5,
    ecolor='black',
    error_kw={'elinewidth': 1.5}
)

# Add CV values as annotations
for i, cv in enumerate(cv_thigmotaxis_per_bin):
    plt.text(bin_centers[i], average_thigmotaxis_per_bin[i] + std_dev_thigmotaxis_per_bin[i] + 2,
             f"CV={cv:.1f}%",
             ha='center',
             fontsize=10,
             color='blue')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), fontsize=12)  # Centering the label
plt.title('Average Thigmotaxis Over Time (All Mice) with SD', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Average Thigmotaxis (%)', fontsize=12)
plt.xticks(bin_centers, labels=[f'{int(edge)}-{int(edge + 150)}' for edge in bin_edges[:-1]])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Print results
print(f"Average Thigmotaxis per bin: {average_thigmotaxis_per_bin}")
print(f"Standard Deviation per bin: {std_dev_thigmotaxis_per_bin}")

# Adding individual deviations for each mouse from the average
deviations = {
    mouse: np.array(values) - average_thigmotaxis_per_bin
    for mouse, values in all_thigmotaxis.items()
    if values
}

# Display deviations for each mouse
for mouse, deviation in deviations.items():
    print(f"{mouse} deviations: {deviation}")

