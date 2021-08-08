"""Program that simulate a command line calculator with the four basic operations (+, -, *, /)."""

import argparse
import operator
import sys


class WelcomeAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("Good morning :)")


def divide(first_number, second_number):
    """Takes two numbers, validates that the divisor isn't zero, returns the division of both numbers."""
    if second_number == 0:
        print("The divisor cannot be 0")
        sys.exit(1)

    return first_number / second_number


# I decided to use the operator module instead of writing 4 identical lambdas with different operator symbols.
OPERATIONS = {
    'add': operator.add,
    'subtract': operator.sub,
    'multiply': operator.mul,
    'divide': divide
}


def add_arguments(parser):
    """Given a parser, add all the arguments to it in order to configure it."""
    # Add arguments (welcome, operation and numbers)
    parser.add_argument('-w', '--welcome',
                        help="Use it if you wanna have a good morning before knowing the operation result!", nargs=0,
                        action=WelcomeAction)
    parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'])
    parser.add_argument('first_number', type=float)

    parser.add_argument('second_number', type=float)


def do_operation(parser):
    """Given a parser, take the parser args that the user provides, makes the operation, and prints the result."""
    args = parser.parse_args()
    operation = OPERATIONS.get(args.operation)

    print(operation(args.first_number, args.second_number))


def main():
    """Main function. It creates the Argument Parser and calls some functions in order to configure it."""
    # Init command line calculator parser

    parser = argparse.ArgumentParser(description="My command line calculator")
    add_arguments(parser)
    do_operation(parser)


if __name__ == "__main__":
    """Calls the main function."""
    main()
