import webbrowser
import sys

def open_urls(file_path, batch_size):
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