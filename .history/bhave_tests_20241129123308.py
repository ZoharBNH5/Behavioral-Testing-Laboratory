import numpy
import matplotlib.pyplot as plt
from scipy.io import loadmat



# load data from file
data = loadmat('C1B_271124_new.mat')

# Extract relevant data
crossing_times = data.get('crossing_times', None)
time_step = 120  # Time resolution in seconds
total_time = 600  # Total time in seconds

# Calculate frequency from crossing times
if crossing_times is not None:
    # Flatten the crossing times array
    crossing_times = crossing_times.flatten()
    
    # Calculate frequencies
    time_bins = np.arange(0, total_time + time_step, time_step)
    frequencies, _ = np.histogram(crossing_times, bins=time_bins)
    
    # Time values for plotting (midpoints of bins)
    time_values = (time_bins[:-1] + time_bins[1:]) / 2

    # Plotting the frequency over time
    plt.figure(figsize=(10, 6))
    plt.plot(time_values, frequencies, marker='o', linestyle='-', label='Frequency')
    plt.title('Frequency Over Time')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.legend()
    plt.show()
else:
    print("The 'crossing_times' variable is not found in the provided file.")