import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('C1B_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C1B = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C1B: {grooming_durations_C1B}')

data = loadmat('C2B_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C2B = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C2B: {grooming_durations_C2B}')

data = loadmat('C1G_241124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C1G = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C1G: {grooming_durations_C1G}')

data = loadmat('C2G_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C2G = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C2G: {grooming_durations_C2G}')
data = loadmat('C2G_271124_new.mat')

data = loadmat('C1R_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C1R = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C1R: {grooming_durations_C1R}')
data = loadmat('C2G_271124_new.mat')

data = loadmat('C2R_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C2R = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C2R: {grooming_durations_C2R}')

data = loadmat('C1W_241124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C1W = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C1W: {grooming_durations_C1W}')

data = loadmat('C2W_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C2W = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration C2W: {grooming_durations_C2W}')

# Grooming data for multiple mice
grooming_data = [
    grooming_durations_C1B,       # Mouse 1
    grooming_durations_C2B,     # Mouse 2
    grooming_durations_C1G,     # Mouse 3
    grooming_durations_C2G,      # Mouse 4
    grooming_durations_C1R,        # Mouse 5
    grooming_durations_C2R,     # Mouse 6
    grooming_durations_C1W,     # Mouse 7
    grooming_durations_C2W  # Mouse 8
]

# Number of mice
num_mice = len(grooming_data)

# Create the figure
plt.figure(figsize=(10, 6))

# Loop through each mouse and plot grooming intervals
for i, intervals in enumerate(grooming_data, start=1):
    for start_time, end_time in zip(intervals[0], intervals[1]):
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
