import click
from scripts.combine_csvs import combine_csvs
from scripts.format_slack_dm_history import format_slack_dm_history
from scripts.format_slack_channel_history import format_slack_channel_history


@click.group()
def cli():
    """Main command group."""
    pass


cli.add_command(combine_csvs, name="combine-csvs")
cli.add_command(format_slack_dm_history, name="format-slack-dm")
cli.add_command(format_slack_channel_history, name="format-slack-channel")

if __name__ == "__main__":
    cli()
