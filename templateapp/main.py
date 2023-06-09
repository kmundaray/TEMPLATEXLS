import pandas as pd
import os

# Set the folder path where the .xls files are located on your desktop
folder_path = r"/Users/kmundaray/Desktop"

# Create an empty list to store the data from .xls files
data = []

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        data.append(df)

# Concatenate all the dataframes into a single dataframe
combined_data = pd.concat(data)

# Print the combined dataframe
#print(data)
print(combined_data)