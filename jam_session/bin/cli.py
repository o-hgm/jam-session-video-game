import click
from jam_session.game import start_game

@click.command()
def cli():
    start_game()


def main():
    cli()