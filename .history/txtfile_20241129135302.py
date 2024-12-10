import pandas as pd
from scipy.io import loadmat

# Load the text file into a DataFrame
file_path = loadmat('C2R_271124_new.mat')
columns = ['Date', 'Time', 'Speed', 'Zone #', 'Subject ID', 'Duration(sec)', 'End Speed', 'Message']

# Read the data into a DataFrame
data = pd.read_csv(file_path, sep='\t', names=columns, skiprows=1, engine='python')

# Display the DataFrame to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Grooming Data Table", dataframe=data)
