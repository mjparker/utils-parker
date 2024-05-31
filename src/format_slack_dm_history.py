import re
import os
import asyncclick as click


def parse_chat_history(file_path, speakers):
    with open(file_path, "r") as file:
        lines = file.readlines()

    chat_history = []
    current_speaker = None
    current_messages = []

    for line in lines:
        line = line.strip()
        if line in speakers:
            if current_speaker:
                chat_history.append((current_speaker, current_messages))
            current_speaker = line
            current_messages = []
        elif re.match(r"^\d{2}:\d{2}", line):
            time_message = line.split(" ", 1)
            if len(time_message) == 2:
                time, message = time_message
                current_messages.append((time, message))
            else:
                current_messages.append((time_message[0], ""))
        elif current_messages and line:
            current_messages[-1] = (
                current_messages[-1][0],
                current_messages[-1][1] + " " + line,
            )

    if current_speaker:
        chat_history.append((current_speaker, current_messages))

    return chat_history


def format_chat_history(chat_history):
    formatted_history = []

    for speaker, messages in chat_history:
        formatted_history.append(speaker)
        for time, message in messages:
            formatted_history.append(f"{time} - {message}")
        formatted_history.append("")

    return "\n".join(formatted_history)


def save_formatted_history(formatted_history, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(formatted_history)


@click.command()
@click.argument("input_file")
@click.argument("speakers", nargs=-1)
def main(input_file, speakers):
    """Process chat history from an input file and format it."""
    output_file_path = f"{os.path.splitext(input_file)[0]}_formatted.txt"

    chat_history = parse_chat_history(input_file, speakers)
    formatted_history = format_chat_history(chat_history)
    save_formatted_history(formatted_history, output_file_path)

    print(f"Formatted chat history saved to {output_file_path}")


if __name__ == "__main__":
    main()
