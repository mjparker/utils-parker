# pylint: disable=pointless-string-statement
import sys
import os
import pandas as pd

"""
Combine multiple CSV files into one. Assumes that all CSVs have the same columns.
Accepts a directory path as a command line argument.

Usage:
    python combine_csvs_directory.py <directory_path>
"""


# Check if the command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <directory_path>")
    sys.exit(1)

DIRECTORY_PATH = sys.argv[1]

# Get all files in the directory
all_files = os.listdir(DIRECTORY_PATH)

# Filter for CSV files
csv_files = [f for f in all_files if f.endswith(".csv")]

# Check if any CSV files are found
if not csv_files:
    print("No CSV files found in the provided directory.")
    sys.exit(1)

# Full paths of the CSV files
file_paths = [os.path.join(DIRECTORY_PATH, file) for file in csv_files]

# Read all CSV files into DataFrames and store in a list
dataframes = [pd.read_csv(file_path) for file_path in file_paths]

# Concatenate all DataFrames
combined_df = pd.concat(dataframes, ignore_index=True)

# Remove duplicates
no_duplicates_df = combined_df.drop_duplicates()

# Save the result to a new CSV file in the same directory
output_file = os.path.join(DIRECTORY_PATH, "combined_all_scis.csv")
no_duplicates_df.to_csv(output_file, index=False)

print(f"Combined CSV file saved to: {output_file}")
