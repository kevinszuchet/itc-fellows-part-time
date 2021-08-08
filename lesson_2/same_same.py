"""
This program has the 'samesame' function. It receives a list, sums all of its members, and returns that sum.
"""


def samesame(elements):
    """Takes a list, returns the sum of all the members inside it or None if the list is empty"""
    if len(elements) == 0:
        return None

    sum_of_elements = elements[0]
    for elem in elements[1:]:
        sum_of_elements += elem

    return sum_of_elements


def assert_with_message(actual, expected):
    assert actual == expected, f"The assertion expect {expected}, but has {actual}"


def samesame_empty_list_tests():
    """Tests samesame function passing an empty list as a parameter"""
    assert samesame([]) is None
    print("All tests with empty list as parameter passed!")


def samesame_strings_tests():
    """Tests samesame function passing strings or a list of strings as a parameter"""
    assert_with_message(samesame(["Hello", "World", "!"]), "HelloWorld!")
    assert_with_message(samesame("Hello World!"), "Hello World!")
    print("All tests with strings or a list of strings as parameter passed!")


def samesame_numbers_tests():
    """Tests samesame function passing a list of numbers as a parameter"""
    assert_with_message(samesame([1, 2, 3, 4, 5]), 15)
    assert_with_message(samesame([1, 1.5, 3, 4.5, 5]), 15.0)
    assert_with_message(samesame([1.0, 2.0, 3.0, 4.0, 5.0]), 15.0)
    print("All tests with a list of numbers as parameter passed!")


def samesame_lists_tests():
    """Tests samesame function passing a list of lists as a parameter"""
    assert_with_message(samesame([[1, 2], [3, 4, 5]]), [1, 2, 3, 4, 5])
    assert_with_message(samesame([[1, 2], []]), [1, 2])
    assert_with_message(samesame([[], []]), [])
    print("All tests with a list of lists as parameter passed!")


def samesame_tuples_tests():
    """Tests samesame function passing a list of tuples as a parameter"""
    assert_with_message(samesame([(1, 2), (3, 4)]), (1, 2, 3, 4))
    assert_with_message(samesame([(1, 2), ()]), (1, 2))
    assert_with_message(samesame([(), (3, 4)]), (3, 4))
    assert_with_message(samesame([(), ()]), ())
    print("All tests with a list of tuples as parameter passed!")


def main():
    """Tests the samesame function with different types inside the list"""
    samesame_empty_list_tests()
    samesame_strings_tests()
    samesame_numbers_tests()
    samesame_lists_tests()
    samesame_tuples_tests()


if __name__ == '__main__':
    main()
