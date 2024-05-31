# utils.parker

Various scripts and utilities that I frequently use.

## Setup

1. `cd` to root directory
2. run `./setup`
3. activate your virtualenv
4. run a commmand like so: `utils format-slack-channel "filename.txt" "Speaker 1 Name" "Speaker 2 Name"

## Adding Commands

1. Create a new command file under the `scripts` folder.
2. Register the new command in `src/cli.py`. View `cli.py` to see how to do that - it's very simple and repeatable.
