"""
A newspaper system requires a very specific format for their headlines.In order to fulfil that requirement, this program
will have a function 'encode_title' that receives a string and a pad with and returns the title with the correct format.
"""


def encode_title(string, width):
    """Receives a string and a pad width, returns the encoded title."""
    title = string.title()
    return title.zfill(width)


def main():
    """
    Asks the reporter to provide the string to encode and the minimum length of it.Then, print out the encoded title.
    """
    string = input("Hi reporter, could you please provide us with the title you want to encode?. ")
    min_width = input("Thanks! What is the minimum length of the title?. ")
    while not min_width.isdigit():
        min_width = input("Please enter a valid length. ")
    title = encode_title(string, int(min_width))
    print(title)


if __name__ == '__main__':
    assert encode_title("aaaa", 4) == "Aaaa"
    assert encode_title("aaaa", 5) == "0Aaaa"
    assert encode_title("hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya'
    assert encode_title("000hello mY naME is iynigo Montoya", 40) == '000000000Hello My Name Is Iynigo Montoya'

    print('--- All tests passed ---')
    main()
