import os
import pandas as pd
import click


@click.command()
@click.argument("directory_path")
def combine_csvs(directory_path):
    """
    Combine multiple CSV files into one. Assumes that all CSVs have the same columns.
    Accepts a directory path as an argument.

    Usage: cli combine-csvs <directory_path>
    """

    # Get all files in the directory
    all_files = os.listdir(directory_path)

    # Filter for CSV files
    csv_files = [f for f in all_files if f.endswith(".csv")]

    # Check if any CSV files are found
    if not csv_files:
        click.echo("No CSV files found in the provided directory.")
        raise click.Abort()

    # Full paths of the CSV files
    file_paths = [os.path.join(directory_path, file) for file in csv_files]

    # Read all CSV files into DataFrames and store in a list
    dataframes = [pd.read_csv(file_path) for file_path in file_paths]

    # Concatenate all DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Remove duplicates
    no_duplicates_df = combined_df.drop_duplicates()

    # Save the result to a new CSV file in the same directory
    output_file = os.path.join(directory_path, "combined_all_csvs.csv")
    no_duplicates_df.to_csv(output_file, index=False)

    click.echo(f"Combined CSV file saved to: {output_file}")


if __name__ == "__main__":
    combine_csvs()
