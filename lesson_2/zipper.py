"""
This program has the 'zipper' function. It receives two elements and returns a list of tuples.
Each tuple contains the i-th element from each of the argument sequences or iterables.
"""


def zipper(iterable1, iterable2):
    """
    Receives two elements and returns a list of tuples.
    Each tuple contains the i-th element from each of the argument sequences or iterables.
    The returned list’s length is equal to the length of the shorter argument the function receives.
    """
    min_len = min(len(iterable1), len(iterable2))
    list_of_tuples = []

    for i in range(0, min_len):
        list_of_tuples.append((iterable1[i], iterable2[i]))

    return list_of_tuples


def assert_with_message(actual, expected):
    assert actual == expected, f"The assertion expect {expected}, but has {actual}"


def zipper_two_lists_tests():
    """Tests zipper function passing two lists as parameters"""
    assert_with_message(zipper([1, 2, 3], ["hello", "mr.", "world"]), [(1, "hello"), (2, "mr."), (3, "world")])
    assert_with_message(zipper([], ["hello", "mr.", "world"]), [])
    assert_with_message(zipper([1, 2, 3], []), [])
    assert_with_message(zipper([], []), [])
    print("All tests with two lists as parameters passed!")


def zipper_two_tuples_tests():
    """Tests zipper function passing two tuples as parameters"""
    assert_with_message(zipper((1, 2, 3), ("hello", "mr.", "world")), [(1, "hello"), (2, "mr."), (3, "world")])
    assert_with_message(zipper((), ("hello", "mr.", "world")), [])
    assert_with_message(zipper((1, 2, 3), ()), [])
    assert_with_message(zipper((), ()), [])
    print("All tests with two tuples as parameters passed!")


def zipper_list_and_tuple_tests():
    """Tests zipper function passing a list and a tuple as parameters"""
    assert_with_message(zipper((1, 2, 3), ["hello", "mr.", "world"]), [(1, "hello"), (2, "mr."), (3, "world")])
    assert_with_message(zipper([1, 2, 3], ("hello", "mr.", "world")), [(1, "hello"), (2, "mr."), (3, "world")])
    assert_with_message(zipper([1, 2, 3], ()), [])
    assert_with_message(zipper([], ("hello", "mr.", "world")), [])
    assert_with_message(zipper([], ()), [])
    print("All tests with a list and a tuple as parameters passed!")


def main():
    """Tests the zipper function with different types inside the list"""
    zipper_two_lists_tests()
    zipper_two_tuples_tests()
    zipper_list_and_tuple_tests()


if __name__ == '__main__':
    main()
