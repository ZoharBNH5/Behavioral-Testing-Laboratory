import scipy.io

# Load the MATLAB file
file_path = '/mnt/data/C1B_271124_new.mat'
data = scipy.io.loadmat(file_path)

# Extract relevant data
crossing_times = data.get('crossing_times', None)
periphery_times = data.get('periphery_times', None)

# Ensure data is available
if crossing_times is not None and periphery_times is not None:
    # Flatten arrays for processing
    crossing_times = crossing_times.flatten()
    periphery_times = periphery_times.flatten()

    # Calculate total crossings and peripheral crossings
    total_crossings = len(crossing_times)
    peripheral_crossings = len(periphery_times)

    # Calculate Thigmotaxis
    thigmotaxis = (peripheral_crossings / total_crossings) * 100 if total_crossings > 0 else 0

    thigmotaxis
else:
    "Relevant data not found in the provided file."
