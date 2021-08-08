"""
Program with a one-line function that receives a list of numbers and a list of divisors.
It returns all the numbers that at least are divisible by one divisor.
"""


def dividable(numbers, divisors):
    """
    Receives a list of numbers and a list of divisors.
    Returns all the numbers that at least are divisible by one divisor.
    """
    return [number for number in numbers if [number % divisor == 0 for divisor in divisors].count(True) > 0]


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(dividable([3, 6, 9, 12], [3]), [3, 6, 9, 12])
    assert_verbose(dividable([3, 6, 9, 13], [3, 13]), [3, 6, 9, 13])
    assert_verbose(dividable([1, 2, 3, 4, 5, 6], [2, 3]), [2, 3, 4, 6])
    assert_verbose(dividable([], []), [])
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
