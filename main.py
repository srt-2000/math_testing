# import libs and modules
import click

from src.calculator import NumCalculator
from src.fcalc import Fcalc

# create command's group
@click.group
def app_commands():
    pass

# # binary search algorithm command
# @click.command(help="binary search algorithm")
# @click.option(
#     "--mx",
#     type=int,
#     prompt="Hello!"
#            "\nI'm the binary search algorithm"
#            "\nI'll find the index of item you want very fast"
#            "\n\nEnter the maximum number of sorted array",
#     help="You have to enter max value of list"
# )
# @click.option(
#     "--find",
#     type=int,
#     prompt="Enter the digit we want to find",
#     help="You have to enter the value what index you want to find"
# )
# def bs(mx, find):
#     my_list = [n for n in range(1, mx + 1)]
#     click.echo(f"\nWe have a  sorted list from 0 to {mx}")
#     position = PositionFinder()
#     click.echo(f"\nFIND!!!\n{position.bin_search(my_list, find)} is position of {find}")
#
# # adding commands into group
# app_commands.add_command(bf)
# app_commands.add_command(bs)

if __name__ == '__main__':
    app_commands()