import webbrowser
import click


@click.command()
@click.argument("file_path")
@click.argument("batch_size", default=20, type=int, required=False)
def open_urls(file_path, batch_size):
    """
    Open URLs from a text file in batches using the default web browser.

    Arguments:
        file_path (str): The path to the text file containing URLs.
        batch_size (int): The number of URLs to open at once (optional, default=20).

    Usage: cli open-urls <file_path> <batch_size>

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
        batch_urls = urls[opened_urls : opened_urls + batch_size]

        for url in batch_urls:
            url = url.strip()
            webbrowser.open(url)

        opened_urls += len(batch_urls)

        if opened_urls < total_urls:
            input(f"Opened {opened_urls} URLs. Press Enter to open the next batch...")


if __name__ == "__main__":
    open_urls()
