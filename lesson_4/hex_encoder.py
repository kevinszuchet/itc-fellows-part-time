"""Program with a one-line function that receives a string and returns it Hex-encoded."""


def hex_encode(string):
    """Receives a string, returns a hex encoded string."""
    return ''.join([hex(ord(char)).replace('0x', '') for char in string])


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(hex_encode("hello world"), "68656c6c6f20776f726c64")
    assert_verbose(hex_encode(""), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
