import click
from scripts.yourscript import cli as yourscript_cli
from scripts.format_slack_dm_history import main as format_slack_dm_cli
from scripts.format_slack_channel_history import main as format_slack_channel_cli


@click.group()
def cli():
    """Main command group."""
    pass


cli.add_command(yourscript_cli, name="yourscript")
cli.add_command(format_slack_dm_cli, name="format-slack-dm")
cli.add_command(format_slack_channel_cli, name="format-slack-channel")

if __name__ == "__main__":
    cli()
