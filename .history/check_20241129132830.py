import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('C1B_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)
grooming_durations_C1B = grooming_start_stop[1] - grooming_start_stop[0]
print(f'duration : {grooming_durations_C1B}')

# Grooming data for multiple mice
grooming_data = [
    grooming_durations_C1B,       # Mouse 1
    [[100, 300], [120, 350]],     # Mouse 2
    [[200, 400], [250, 450]],     # Mouse 3
    [[50, 500], [100, 550]],      # Mouse 4
    [[0, 350], [30, 400]],        # Mouse 5
    [[120, 300], [160, 320]],     # Mouse 6
    [[240, 500], [280, 520]],     # Mouse 7
    [[30, 220, 450], [70, 250, 480]]  # Mouse 8
]

# Number of mice
num_mice = len(grooming_data)

# Create the figure
plt.figure(figsize=(10, 6))

# # Loop through each mouse and plot grooming intervals
# for i, intervals in enumerate(grooming_data, start=1):
#     for start_time, end_time in zip(intervals[0], intervals[1]):
#         plt.gca().add_patch(patches.Rectangle(
#             (start_time, i - 0.4),  # Bottom-left corner of the rectangle
#             end_time - start_time,  # Width of the rectangle
#             0.8,                    # Height of the rectangle
#             facecolor=[0.5, 0.7, 0.9], edgecolor='none'
#         ))

# # Customize the plot
# plt.ylim(0, num_mice + 1)
# plt.xlim(0, 600)
# plt.yticks(range(1, num_mice + 1), [f'Mouse {i}' for i in range(1, num_mice + 1)])
# plt.xlabel('Time (seconds)', fontsize=12)
# plt.ylabel('Mouse ID', fontsize=12)
# plt.title('Grooming Activity Over Time for Each Mouse', fontsize=14)
# plt.grid(axis='x', linestyle='--', alpha=0.7)

# plt.tight_layout()
# plt.show()
