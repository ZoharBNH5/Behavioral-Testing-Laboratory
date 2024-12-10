import pandas as pd

# Define the file path
file_path = '271124.txt'

# Define the column names
columns = ['Date', 'Time', 'Speed', 'Zone #', 'Subject ID', 'Duration(sec)', 'End Speed', 'Message']

# Read the data into a DataFrame
data = pd.read_csv(file_path, sep='\t', names=columns, skiprows=1, engine='python')

# Create a dictionary to store the vectors for each animal
animal_vectors = {}

# Group the data by Subject ID and extract durations
grouped_data = data.groupby('Subject ID')

# Create vectors for each animal
for animal, group in grouped_data:
    durations = group['Duration(sec)'].head(5).tolist()  # Get the first 5 durations
    animal_vectors[animal] = durations

# Print the vectors for each animal
for animal, vector in animal_vectors.items():
    print(f"{animal}: {vector}")
# Calculate the learning metric for each animal
learning_results = {}

for animal, vector in animal_vectors.items():
    # Ensure the vector has at least 5 values
    if len(vector) >= 5:
        # Convert strings to integers
        vector = list(map(int, vector))
        if animal =="C2R":
            numerator = vector[2] + vector[4] #4th trail failed
        else:
            numerator = vector[4] + vector[3]  # 5th + 4th trial
        denominator = vector[0] + vector[1]  # 1st + 2nd trial
        
        if denominator > 0:  # Avoid division by zero
            learning_metric = numerator / denominator
            learning_results[animal] = "Learning" if learning_metric > 1 else "No Learning"
        else:
            learning_results[animal] = "Undefined (Denominator = 0)"
    else:
        learning_results[animal] = "Insufficient Data"

# Print the learning results
for animal, result in learning_results.items():
    print(f"{animal}: {result}")


from scipy.stats import linregress

learning_slopes = {}

for animal, vector in animal_vectors.items():
    if len(vector) >= 5:  # Ensure there are enough trials
        trials = list(range(1, len(vector) + 1))
        slope, _, _, _, _ = linregress(trials, vector)
        learning_slopes[animal] = slope
        print(f"{animal}: Slope = {slope}, Learning = {'Yes' if slope > 0 else 'No'}")
