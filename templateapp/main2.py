import pandas as pd

# Path to the Excel file on your desktop
excel_file_path = r"/Users/kmundaray/Desktop/template test 1.xlsx"

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Path to save the CSV file
csv_file_path = r"/Users/kmundaray/Desktop/file.csv"

# Convert DataFrame to CSV and save it
df.to_csv(csv_file_path, index=False)

print("CSV file created successfully!")