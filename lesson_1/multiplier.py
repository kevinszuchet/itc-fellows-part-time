"""
This is a program that implements a multiplier function. It takes a string input and multiply each and every character.
Also, it has a main function that ask the user for an input to apply the multiplier function defined above.
"""


def multiplier(string_to_multiply):
    """Receives a string, returns its multiplied version."""
    multiplied_string = ""
    for character in string_to_multiply:
        multiplied_string += character * 2
    return multiplied_string


def main():
    """Asks the user to provide a string to multiply and print out its multiplied version."""
    string_to_multiply = input("Hi, which string do you want to multiply? ")
    multiplied_string = multiplier(string_to_multiply)
    print(multiplied_string)


if __name__ == '__main__':
    assert multiplier("a") == "aa"
    assert multiplier("ab") == "aabb"
    assert multiplier("hello world") == "hheelllloo  wwoorrlldd"

    print('--- All tests passed ---')
    main()
