#!/usr/bin/env python3
"""
Convert CSV file to Excel format
Usage: python3 format_csvs_to_excel.py input.csv
Output will be saved as input.xlsx in the same directory
"""

import sys
import os
import pandas as pd
from pathlib import Path


def convert_csv_to_excel(csv_path):
    """Convert a CSV file to Excel format"""
    try:
        # Convert to absolute path to handle any directory issues
        csv_path = os.path.abspath(csv_path)

        # Read the CSV file
        df = pd.read_csv(csv_path)

        # Create output path (same directory, same name but .xlsx extension)
        csv_file = Path(csv_path)
        output_path = csv_file.parent / f"{csv_file.stem}.xlsx"

        # Write to Excel
        df.to_excel(output_path, index=False, engine="openpyxl")

        print(f"Successfully converted {csv_path} to {output_path}")
        return str(output_path)

    except FileNotFoundError:
        print(f"Error: CSV file '{csv_path}' not found")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: CSV file '{csv_path}' is empty")
        sys.exit(1)
    except Exception as e:
        print(f"Error converting CSV to Excel: {str(e)}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 format_csvs_to_excel.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]

    if not os.path.exists(csv_file):
        print(f"Error: File '{csv_file}' does not exist")
        sys.exit(1)

    if not csv_file.lower().endswith(".csv"):
        print(f"Error: File '{csv_file}' is not a CSV file")
        sys.exit(1)

    convert_csv_to_excel(csv_file)


if __name__ == "__main__":
    main()
