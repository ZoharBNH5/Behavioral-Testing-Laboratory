import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.io import loadmat

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
