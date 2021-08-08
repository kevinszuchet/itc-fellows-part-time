"""
Program with a one-line function that receives a list of numbers and a divisor.
It returns if all the numbers of the list are divisible (without reminder) by the divisor.
"""


def dividable(numbers, divisor):
    """
    Receives a list of numbers and a divisor.
    Returns if all the numbers of the list are divisible (without reminder) by the divisor.
    """
    return len([number for number in numbers if number % divisor == 0]) == len(numbers)


def main():
    """Main function for run tests."""
    assert dividable([3, 6, 9, 12], 3)
    assert not dividable([3, 6, 9, 13], 3)
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
