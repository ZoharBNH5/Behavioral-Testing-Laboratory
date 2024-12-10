import pandas as pd

# Define the file path
file_path = '271124.txt'

# Define the column names
columns = ['Date', 'Time', 'Speed', 'Zone #', 'Subject ID', 'Duration(sec)', 'End Speed', 'Message']

# Read the data into a DataFrame
data = pd.read_csv(file_path, sep='\t', names=columns, skiprows=1, engine='python')

# Display the DataFrame
print(data)
