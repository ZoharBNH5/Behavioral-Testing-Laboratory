import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Load data
data = loadmat('C1B_271124_new.mat')
grooming_start_stop = data.get('grooming_start_stop', None)

# Extract start and stop times
grooming_starts = grooming_start_stop[0]
grooming_stops = grooming_start_stop[1]

# Calculate durations
grooming_durations = grooming_stops - grooming_starts

# Plot grooming segments as horizontal bars
plt.figure(figsize=(10, 5))
for i in range(len(grooming_starts)):
    plt.barh("C1B", grooming_durations[i], left=grooming_starts[i],
             height=0.5, color='skyblue', edgecolor='black')

# Add labels and titles
plt.title('Grooming Segments for C1B', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Mouse Name', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
