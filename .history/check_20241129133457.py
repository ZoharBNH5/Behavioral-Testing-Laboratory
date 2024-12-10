import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.io import loadmat

# Load grooming data from .mat files
data_files = [
    'C1B_271124_new.mat',
    'C2B_271124_new.mat',
    'C1G_241124_new.mat',
    'C2G_271124_new.mat',
    'C1R_271124_new.mat',
    'C2R_271124_new.mat',
    'C1W_241124_new.mat',
    'C2W_271124_new.mat'
]

# Prepare grooming data
grooming_data = []
for file in data_files:
    data = loadmat(file)
    grooming_start_stop = data.get('grooming_start_stop', None)
    if grooming_start_stop is not None:
        starts = grooming_start_stop[0]
        stops = grooming_start_stop[1]
        intervals = list(zip(starts, stops))
        grooming_data.append(intervals)
    else:
        grooming_data.append([])  # Add empty if no data found

# Number of mice
num_mice = len(grooming_data)

# Create the figure
plt.figure(figsize=(10, 6))

# Loop through each mouse and plot grooming intervals
for i, intervals in enumerate(grooming_data, start=1):
    for start_time, end_time in intervals:
        plt.gca().add_patch(patches.Rectangle(
            (start_time, i - 0.4),  # Bottom-left corner of the rectangle
            end_time - start_time,  # Width of the rectangle
            0.8,                    # Height of the rectangle
            facecolor=[0.5, 0.7, 0.9], edgecolor='none'
        ))

# Customize the plot
plt.ylim(0, num_mice + 1)
plt.xlim(0, 600)
plt.yticks(range(1, num_mice + 1), [f'Mouse {i}' for i in range(1, num_mice + 1)])
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Mouse ID', fontsize=12)
plt.title('Grooming Activity Over Time for Each Mouse', fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
