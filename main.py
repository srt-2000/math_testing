# import libs and modules
import click

from src.calculator import NumCalculator
from src.fcalc import Fcalc


# create command's group
@click.group
def app_commands():
    pass

# simple calculator commands
#sum command
@click.command(help="Return the sum of two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' integer to sum",
    help="You have to enter integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' integer to sum",
    help="You have to enter integer value"
)

def sm(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} + {y} = {result.plus(x, y)}")

#difference command
@click.command(help="Return the difference of two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' first integer to diff",
    help="You have to enter first integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' second integer to diff",
    help="You have to enter second integer value"
)

def df(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} - {y} = {result.minus(x, y)}")

#mul command
@click.command(help="Return the mul result for two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' first integer to mul",
    help="You have to enter first integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' second integer to mul",
    help="You have to enter second integer value"
)

def ml(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} * {y} = {result.mult(x, y)}")

#divide command
@click.command(help="Return the divide result for two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' first integer to divide",
    help="You have to enter first integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' second integer to divide",
    help="You have to enter second integer value"
)

def dv(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} / {y} = {result.div(x, y)}")

#full divide command
@click.command(help="Return the FULL divide result for two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' first integer to divide",
    help="You have to enter first integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' second integer to divide",
    help="You have to enter second integer value"
)

def fdv(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} // {y} = {result.full_div(x, y)}")

#end divide command
@click.command(help="Return the END divide result for two integers")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' first integer to divide",
    help="You have to enter first integer value"
)
@click.option(
    "--y",
    type=int,
    prompt="Enter 'y' second integer to divide",
    help="You have to enter second integer value"
)

def edv(x, y):
    result = NumCalculator()
    click.echo(f"\nResult {x} % {y} = {result.end_div(x, y)}")

#factorial command
@click.command(help="Return the FACTORIAL for integer")
@click.option(
    "--x",
    type=int,
    prompt="Enter 'x' integer to find it's factorial",
    help="You have to enter integer value"
)

def fc(x):
    result = Fcalc()
    click.echo(f"\nFactorial of {x}  = {result.factor(x)}")


# adding commands into group
app_commands.add_command(sm)
app_commands.add_command(df)
app_commands.add_command(ml)
app_commands.add_command(dv)
app_commands.add_command(fdv)
app_commands.add_command(edv)
app_commands.add_command(fc)


if __name__ == '__main__':
    app_commands()