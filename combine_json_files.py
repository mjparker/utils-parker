# pylint: disable=invalid-name
import json
import os
import argparse


def combine_json_files(files):
    combined_data = []

    for file in files:
        with open(file, "r", encoding="utf8") as f:
            data = json.load(f)
            combined_data.extend(data)

    return combined_data


def main():
    """
    Combine multiple JSON files into one file.
    Args:
        directory: Directory containing the JSON files to combine.
    """
    parser = argparse.ArgumentParser(description="Combine multiple JSON files into one.")
    parser.add_argument("directory", type=str, help="Directory containing the JSON files to combine.")
    args = parser.parse_args()

    # Get all JSON files in the specified directory
    json_files = [os.path.join(args.directory, f) for f in os.listdir(args.directory) if f.endswith(".json")]

    combined_data = combine_json_files(json_files)

    # Write the combined data to a new JSON file
    output_file = os.path.join(args.directory, "combined.json")
    with open(output_file, "w", encoding="utf8") as f:
        json.dump(combined_data, f, indent=4)

    print(f"Combined {len(json_files)} JSON files into 'combined.json'")


if __name__ == "__main__":
    main()
