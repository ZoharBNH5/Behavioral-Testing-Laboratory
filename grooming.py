import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.io import loadmat
import numpy as np
from scipy.stats import linregress


# Load grooming data from .mat files and their corresponding names
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

# Define the bin size (150 seconds) and total time range
bin_size = 150
time_bins = np.arange(0, 600 + bin_size, bin_size)  # Define the bins

# Prepare grooming data
grooming_data = {}
for name, file in data_files.items():
    data = loadmat(file)
    grooming_start_stop = data.get('grooming_start_stop', None)
    if grooming_start_stop is not None:
        starts = grooming_start_stop[0]
        stops = grooming_start_stop[1]
        intervals = list(zip(starts, stops))
        grooming_data[name] = intervals
    else:
        grooming_data[name] = []  # Add empty if no data found

# Initialize a list to count how many mice are grooming in each bin
grooming_mice_per_bin = np.zeros(len(time_bins) - 1)

# Loop through each mouse's grooming intervals
for mouse, intervals in grooming_data.items():
    # Create a set to track bins where this mouse was grooming
    grooming_bins = set()
    for start_time, end_time in intervals:
        for i in range(len(time_bins) - 1):
            bin_start, bin_end = time_bins[i], time_bins[i + 1]
            if start_time < bin_end and end_time > bin_start:  # Overlap with the bin
                # If the mouse is grooming in this bin, add the bin index to the set
                grooming_bins.add(i)

    # For each bin where this mouse groomed, increment the count
    for bin_index in grooming_bins:
        grooming_mice_per_bin[bin_index] += 1

# Create the figure
plt.figure(figsize=(10, 6))

# Loop through each mouse and plot grooming intervals
for i, (mouse, intervals) in enumerate(grooming_data.items(), start=1):
    for start_time, end_time in intervals:
        plt.gca().add_patch(patches.Rectangle(
            (start_time, i - 0.4),  # Bottom-left corner of the rectangle
            end_time - start_time,  # Width of the rectangle
            0.8,                    # Height of the rectangle
            facecolor=[0.5, 0.7, 0.9], edgecolor='none'
        ))

# Customize the plot
plt.ylim(0, len(grooming_data) + 1)
plt.xlim(0, 600)
plt.yticks(range(1, len(grooming_data) + 1), list(grooming_data.keys()))
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Mouse Name', fontsize=12)
plt.title('Grooming Activity Over Time for Each Mouse', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


# Calculate total grooming time for all mice in each bin
total_grooming_per_bin = np.zeros(len(time_bins) - 1)

for intervals in grooming_data.values():
    for start_time, end_time in intervals:
        # Find the bins where the grooming duration falls
        for i in range(len(time_bins) - 1):
            bin_start, bin_end = time_bins[i], time_bins[i + 1]
            if start_time < bin_end and end_time > bin_start:  # Overlap with the bin
                # Calculate the overlap duration
                overlap_start = max(start_time, bin_start)
                overlap_end = min(end_time, bin_end)
                total_grooming_per_bin[i] += (overlap_end - overlap_start)

print(f"Total grooming time in all mouses per bin: {total_grooming_per_bin}")
# Plot the histogram
plt.figure(figsize=(10, 6))
plt.bar(range(len(total_grooming_per_bin)), total_grooming_per_bin, width=0.8, color='skyblue', edgecolor='black')
plt.xticks(range(len(total_grooming_per_bin)), [f'{int(bin_start)}-{int(bin_start + bin_size)}' for bin_start in time_bins[:-1]])
plt.xlabel('Time Bins (seconds)', fontsize=12)
plt.ylabel('Total Grooming Duration (seconds)', fontsize=12)
plt.title('Total Grooming Duration Across All Mice by Time Bins', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Calculate the midpoints of the bins for plotting
bins_midpoints = [(time_bins[i] + time_bins[i + 1]) / 2 for i in range(len(time_bins) - 1)]


# Create the figure
plt.figure(figsize=(10, 6))

# Loop through each mouse and plot grooming intervals
for i, (mouse, intervals) in enumerate(grooming_data.items(), start=1):
    for start_time, end_time in intervals:
        plt.gca().add_patch(patches.Rectangle(
            (start_time, i - 0.4),  # Bottom-left corner of the rectangle
            end_time - start_time,  # Width of the rectangle
            0.8,                    # Height of the rectangle
            facecolor=[0.5, 0.7, 0.9], edgecolor='none'
        ))

# Change X-axis to bins
plt.xlim(0, 600)
bin_labels = [f"{int(start)}-{int(start + bin_size)}" for start in time_bins[:-1]]
plt.xticks(time_bins[:-1], labels=bin_labels, rotation=45, fontsize=10)

# Add number of mice grooming in each bin as text annotations
for bin_index, num_mice in enumerate(grooming_mice_per_bin):
    bin_start = time_bins[bin_index]
    bin_center = bin_start + bin_size / 2
    plt.text(bin_center, len(grooming_data) + 0.5, f"Number of mice: {int(num_mice)}", ha='center', fontsize=14, color='black')

# Customize the plot
plt.ylim(0, len(grooming_data) + 2)
plt.yticks(range(1, len(grooming_data) + 1), list(grooming_data.keys()))
plt.xlabel('Time Bins (seconds)', fontsize=12)
plt.ylabel('Mouse Name', fontsize=12)
plt.title('Grooming Activity Over Time for Each Mouse', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


