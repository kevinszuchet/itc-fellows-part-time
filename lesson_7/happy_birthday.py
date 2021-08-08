"""
I want to wish my friends happy birthday, but I’m too lazy! I need your assistance, please...
I need to have a function called happy_birthday that returns a string with a happy birthday song.
"""
PHRASE = "Happy Birthday"
NAME_LINE = 2


def happy_birthday(name): return '\n'.join(
    map(lambda i: f"{PHRASE} {f'dear {name}' if i == NAME_LINE else 'to you'}", range(4)))


def happy_birthday_test():
    """Runs the test for the happy birthday function."""
    expected = 'Happy Birthday to you\nHappy Birthday to you\nHappy Birthday dear Dani\nHappy Birthday to you'
    assert happy_birthday("Dani") == expected


def main():
    """Main function that runs a test."""
    happy_birthday_test()
    print("--- All tests passed ---")

    print("\nHere it goes the song:")
    print(happy_birthday("Dani"))


if __name__ == '__main__':
    main()
