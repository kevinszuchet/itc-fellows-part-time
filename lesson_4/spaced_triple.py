"""
Program with a one-line function that receives a string and returns another string with tripled words.
The spaces won't be tripled in the new string.
"""


def spaced_triple(str_to_triple):
    """Receives a string and, in one line, triple each word of it.
    Then, returns the new word tripled string."""
    return ' '.join(word * 3 for word in str_to_triple.split())


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(spaced_triple("hello"), "hellohellohello")
    assert_verbose(spaced_triple("hello world"), "hellohellohello worldworldworld")
    assert_verbose(spaced_triple(" "), "")
    assert_verbose(spaced_triple(""), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
