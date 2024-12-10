import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('C1B_271124_new.mat')
# Grooming start and stop data for a single mouse
grooming_start_stop = data.get('grooming_start_stop', None)

# Calculate grooming durations
grooming_durations = grooming_start_stop[1] - grooming_start_stop[0]

# Mouse name for Y-axis
mouse_name = 'C1B'

# Plotting grooming durations as horizontal bars
plt.figure(figsize=(10, 3))
plt.barh(mouse_name, np.sum(grooming_durations), color='skyblue', edgecolor='black')

# Add labels and titles
plt.title('Total Grooming Duration per Mouse', fontsize=14)
plt.xlabel('Duration (seconds)', fontsize=12)
plt.ylabel('Mouse Name', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
