# utils.parker

Various scripts and utilities that I frequently use.

## Setup

1. `cd` to root directory
2. run `./setup`
3. activate your virtualenv
4. run `pip install .`
5. run a commmand like so: `cli format-slack-channel "filename.txt" "Speaker 1 Name" "Speaker 2 Name"

## Adding Commands

1. Create a new command file under the `scripts` folder.
2. Register the new command in `src/cli.py`. View `cli.py` to see how to do that - it's very simple and repeatable.
3. Open a terminal, `cd` to the `util.parker` directory, activate your virtualenv, and run  `pip install --editable .`
4. You may then call your command by running `utils command-name <arg1> <arg2> ...`
