#!/usr/bin/env python3

import asyncclick as click

from scripts import combine_csvs
from scripts import combine_json_files
from scripts import format_slack_dm_history
from scripts import format_slack_channel_history
from scripts import open_urls


@click.group()
def utils():
    """Main command group."""
    pass


combine_csvs.setup_cmd(utils)
combine_json_files.setup_cmd(utils)
format_slack_dm_history.setup_cmd(utils)
format_slack_channel_history.setup_cmd(utils)
open_urls.setup_cmd(utils)

if __name__ == "__main__":
    utils()
