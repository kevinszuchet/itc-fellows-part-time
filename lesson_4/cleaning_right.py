"""
Program with a one-line function that receives a list of messed up strings (yep, with coffee) and cleans the mess.
Then, returns a list with the new and clean strings.
"""


def cleaning_right(list_of_strings):
    """Receives a list of strings, clean the right mess, and returns the new and clean list."""
    return [string.rstrip('cofe') for string in list_of_strings]


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(cleaning_right(["hell", "hello", "hello worldcofofcfee"]), ["hell", "hell", "hello world"])
    assert_verbose(cleaning_right(["coffee"]), [""])
    assert_verbose(cleaning_right([" "]), [" "])
    assert_verbose(cleaning_right([""]), [""])
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
