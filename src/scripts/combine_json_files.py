import json
import os
import click


def combine_json(files):
    combined_data = []

    for file in files:
        with open(file, "r", encoding="utf8") as f:
            data = json.load(f)
            combined_data.extend(data)

    return combined_data


@click.command()
@click.argument("directory_path")
def combine_json_files(directory_path):
    """
    Combine multiple JSON files into one file.

    Usage: cli combine-json-files <directory_path>
    """

    # Get all JSON files in the specified directory
    json_files = [
        os.path.join(directory_path, f)
        for f in os.listdir(directory_path)
        if f.endswith(".json")
    ]

    # Check if any JSON files are found
    if not json_files:
        click.echo("No JSON files found in the provided directory.")
        raise click.Abort()

    combined_data = combine_json(json_files)

    # Write the combined data to a new JSON file
    output_file = os.path.join(directory_path, "combined.json")
    with open(output_file, "w", encoding="utf8") as f:
        json.dump(combined_data, f, indent=4)

    click.echo(f"Combined {len(json_files)} JSON files into 'combined.json'")


if __name__ == "__main__":
    combine_json_files()
