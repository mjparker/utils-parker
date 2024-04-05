import webbrowser
import sys

def open_urls(file_path, batch_size):
    """
    This script opens URLs from a text file in batches using the default web browser.

    Usage:
        python script.py <file_path> [batch_size]

    Arguments:
        file_path (str): The path to the text file containing URLs (required).
        batch_size (int): The number of URLs to open at once (optional, default=20).

    Example:
        python script.py urls.txt 15

    Note:
        - The text file should contain one URL per line.
        - The script will open the URLs in batches and wait for user input before opening the next batch.
        - If the batch_size is not provided, the default is 20.
    """
    with open(file_path, "r") as file:
        urls = file.readlines()

    total_urls = len(urls)
    opened_urls = 0

    while opened_urls < total_urls:
        batch_urls = urls[opened_urls:opened_urls + batch_size]

        for url in batch_urls:
            url = url.strip()
            webbrowser.open(url)

        opened_urls += len(batch_urls)

        if opened_urls < total_urls:
            input(f"Opened {opened_urls} URLs. Press Enter to open the next batch...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the file path as a command line argument.")
        sys.exit(1)

    file_path = sys.argv[1]
    batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 20

    open_urls(file_path, batch_size)