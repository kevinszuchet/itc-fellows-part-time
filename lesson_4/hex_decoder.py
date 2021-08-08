"""Program with a one-line function that receives a Hex-encoded string and returns it decoded."""

CHUNK_SIZE = 2


def hex_decode(hex_encoded_string):
    """Receives a hex-encoded string, returns it decoded."""
    return ''.join([chr(int("0x" + hex_encoded_string[i:i + CHUNK_SIZE], 16)) for i in range(0, len(hex_encoded_string), CHUNK_SIZE)])


def assert_verbose(actual, expected):
    """
    Given the expected and actual values o the assertion, check if both are equal,
    and prints an error message if the assertion fails.
    """
    assert expected == actual, f"Expected value: {expected}. But actual value is {actual}"


def main():
    """Main function for run tests."""
    assert_verbose(hex_decode("68656c6c6f20776f726c64"), "hello world")
    assert_verbose(hex_decode(""), "")
    print("--- All tests passed ---")


if __name__ == '__main__':
    main()
