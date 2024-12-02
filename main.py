# import libs and modules
import click

from src.calculator import NumCalculator
from src.fcalc import Fcalc


# create command's group
@click.group
def app_commands():
    pass


# simple calculator commands
@click.command(help="Return the sum of two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter the integer to sum",
    help="You have to enter integers values"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter the integer to sum",
    help="You have to enter integers values"
)

def sm(x, y):
    summa = NumCalculator()
    click.echo(f"\nThe sum {x} and {y} is {summa.plus(x, y)}.")

# adding commands into group
app_commands.add_command(sm)

if __name__ == '__main__':
    app_commands()