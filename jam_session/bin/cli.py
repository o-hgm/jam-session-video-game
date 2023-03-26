import click
from jam_session.bin.game import start_game

@click.command()
def cli():
    start_game()


def main():
    cli()