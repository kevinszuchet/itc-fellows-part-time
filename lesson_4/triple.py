"""
Program with a one-line function that receives a string, and returns another string with tripled characters.
"""


def triple(str_to_triple):
    """Receives a string and, in one line, triple each character of it. Then, returns the new tripled string."""
    return ''.join([char * 3 for char in str_to_triple])


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(triple("hello"), "hhheeellllllooo")
    assert_verbose(triple("kevin szuchet"), "kkkeeevvviiinnn   ssszzzuuuccchhheeettt")
    assert_verbose(triple(" "), "   ")
    assert_verbose(triple(""), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
