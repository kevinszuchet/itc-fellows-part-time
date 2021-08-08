"""
Program with a one-line function that receives a list of digits.
It returns a string, where each digit appears i times, starting from one instead of zero.
"""


def ordered_digits(digits):
    """
    Receives a list of digits.
    Returns a string, where each digit appears i times, starting from one instead of zero.
    """
    return ''.join([str(digit) * (i + 1) for i, digit in enumerate(digits)])


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(ordered_digits([2, 5, 1, 9, 2]), "255111999922222")
    assert_verbose(ordered_digits([1, 2, 3]), "122333")
    assert_verbose(ordered_digits([]), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
