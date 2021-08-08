"""
We’ve been writing code that will be presented at the Lambada Championships. The problem is, we’ve written quite a
few functions that we’re no longer allowed to use. The organizer of the championship’s name is def, and def decided
that the use of the word ‘def’ so often in the code is insulting, as it makes him look like a programmer rather than a
dancer.

Artistic spirit...

Since the name of the organizer’s wife is list, and their son’s name is join, we’re not allowed to use list
comprehensions or join either. Go figure.

With those restrictions, the program implements div_and_mod, non_negative, double_digits.
"""

from functools import reduce

# Receives two integers – a,b and returns the result of a//b and a%b.
div_and_mod = lambda a, b: (a // b, a % b)

# Receives one integer – a. If a is negative, returns zero. Otherwise, returns a.
non_negative = lambda a: max(a, 0)

# Receives one integer – a, and returns it with each digit doubled.
double_digits = lambda a: int(reduce(lambda doubled, char: doubled + (char * 2), str(a), ""))


def main():
    """Main function that runs some tests."""
    assert div_and_mod(5, 2) == (2, 1)
    assert non_negative(5) == 5
    assert non_negative(-5) == 0
    assert double_digits(542) == 554422
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
