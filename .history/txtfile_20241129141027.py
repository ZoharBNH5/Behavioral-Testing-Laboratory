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
