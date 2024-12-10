from scipy.stats import ttest_ind
from scipy.io import loadmat
import numpy as np


# Define data file dictionaries
data_files_24 = {
    'C1B': 'C1B_271124_new.mat',
    'C2B': 'C2B_271124_new.mat',
    'C1G': 'C1G_241124_new.mat',
    'C2G': 'C2G_271124_new.mat',
    'C1R': 'C1R_271124_new.mat',
    'C2R': 'C2R_271124_new.mat',
    'C1W': 'C1W_241124_new.mat',
    'C2W': 'C2W_271124_new.mat'
}

data_files_22 = {
    'C2B11': '111222_C2_blue.mat',
    'C2G11': '111222_C2_green.mat',
    'C2B16': '161122_C2_blue.mat',
    'C2R16': '161122_C2_red.mat',
    'C2W16': '161122_C2_white.mat',
    'C1B20': '201122_C1_blue.mat',
    'C1W20': '201122_C1_white.mat',
    'C2B23': '231122_C2_blue.mat',
    'C2G23': '231122_C2_green.mat'
}


# Function to extract crossing times and calculate the total number of crossings per mouse
def get_total_crossings(data_files):
    total_crossings = []
    for mouse, file in data_files.items():
        try:
            # Load data from the .mat file
            data = loadmat(file)
            crossing_times = data.get('crossing_times', None)
            if crossing_times is not None:
                # Count total crossings
                total_crossings.append(len(crossing_times.flatten()))
            else:
                print(f"Missing 'crossing_times' for {mouse}.")
        except FileNotFoundError:
            print(f"File not found for {mouse}: {file}")
    return total_crossings


# Extract total crossings for 2024 and 2022 groups
total_crossings_2024 = get_total_crossings(data_files_24)
total_crossings_2022 = get_total_crossings(data_files_22)

# Calculate mean and standard deviation for each group
mean_2024 = np.mean(total_crossings_2024)
std_2024 = np.std(total_crossings_2024, ddof=1)  # ddof=1 for sample standard deviation

mean_2022 = np.mean(total_crossings_2022)
std_2022 = np.std(total_crossings_2022, ddof=1)  # ddof=1 for sample standard deviation
# Perform independent t-test
t_stat, p_value = ttest_ind(total_crossings_2024, total_crossings_2022, equal_var=False)

# Calculate variance for each group
var_2024 = np.var(total_crossings_2024, ddof=1)  # ddof=1 for sample variance
var_2022 = np.var(total_crossings_2022, ddof=1)  # ddof=1 for sample variance

# Display variance results
print(f"2024 Group: Variance = {var_2024:.2f}")
print(f"2022 Group: Variance = {var_2022:.2f}")

# Display results
print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.4f}")
print(f"2024 Total Crossings: {total_crossings_2024}")
print(f"2022 Total Crossings: {total_crossings_2022}")
print(f"2024 Group: Mean = {mean_2024:.2f}, Standard Deviation = {std_2024:.2f}")
print(f"2022 Group: Mean = {mean_2022:.2f}, Standard Deviation = {std_2022:.2f}")
