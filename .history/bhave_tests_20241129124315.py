import numpy as np
import scipy.io


import matplotlib.pyplot as plt
from scipy.io import loadmat
import matplotlib.pyplot



# load data from file
data = loadmat('C1B_271124_new.mat')

print(data.keys())
# Extract grooming start-stop data
grooming_start_stop = data.get('grooming_start_stop', None)
crossing_times = data.get('crossing_times', None)
periphery_times = data.get('periphery times', None)

if crossing_times is not None and periphery_times is not None and grooming_start_stop is not None:
    # Flatten arrays for processing
    crossing_times = crossing_times.flatten()
    periphery_times = periphery_times.flatten()
    grooming_start_stop = grooming_start_stop.T  # Transpose grooming data for easier handling

# Define bins (2-minute intervals over 10 minutes)
    bin_edges = np.arange(0, 600 + 120, 120)  # Bins of 2 minutes (120 seconds)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Midpoints for plotting

# Calculate Thigmotaxis per bin
    thigmotaxis_values = []
    for start, end in zip(bin_edges[:-1], bin_edges[1:]):
        # Filter crossing and peripheral crossing within the current bin
        crossings_in_bin = (crossing_times >= start) & (crossing_times < end)
        periphery_in_bin = (periphery_times >= start) & (periphery_times < end)
        
        total_crossings = np.sum(crossings_in_bin)
        peripheral_crossings = np.sum(periphery_in_bin)
        
        # Calculate Thigmotaxis for the bin
        thigmotaxis = (peripheral_crossings / total_crossings) * 100 if total_crossings > 0 else 0
        thigmotaxis_values.append(thigmotaxis)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.bar(bin_centers, thigmotaxis_values, width=110, color='skyblue', edgecolor='black', label='Thigmotaxis (%)')
    plt.title('Thigmotaxis Over Time (2-minute bins)', fontsize=14)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Thigmotaxis (%)', fontsize=12)
    plt.xticks(bin_centers, labels=[f'{int(edge/60)}-{int((edge+120)/60)}' for edge in bin_edges[:-1]])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()
else:
    print("Required data (crossing_times, periphery_times, or grooming_start_stop) not found in the provided file.")