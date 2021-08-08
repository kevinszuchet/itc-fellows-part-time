"""
This program asks the user to provide a list of numbers, then it prints out the product of all of them.
"""


def numbers_multiplier(numbers):
    """Takes a list of numbers delimited by space, returns the product of all the numbers."""
    total = 1
    for number in numbers.split(' '):
        total *= int(number)
    return total


def main():
    """Asks the user to provide a list of numbers delimited by spaces. Then, print out the product of the numbers."""
    numbers = input("Hi, which numbers do you want to multiply? Please enter theme leaving a space between each one. ")
    product_of_the_numbers = numbers_multiplier(numbers)
    print(product_of_the_numbers)


if __name__ == '__main__':
    assert numbers_multiplier("1 2 3") == 6
    assert numbers_multiplier("0 500 12 5") == 0
    assert numbers_multiplier("12 4 5") == 240
    assert numbers_multiplier("5") == 5

    print('--- All tests passed ---')
    main()
