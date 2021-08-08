""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names

Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Additional basic list exercises """


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    """
    Given a list of numbers, it takes only the non equal adjacent numbers, adds them to a new list,
    and returns the new list.
    """
    non_equal_adjacent_nums = []
    for i, num in enumerate(nums):
          if i == 0 or num != non_equal_adjacent_nums[-1]:
            non_equal_adjacent_nums.append(num)
    return non_equal_adjacent_nums


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
#
# NOTE - DO NOT use return sorted(sorted1 + sorted2) - that's too easy :-)
#
def linear_merge(sorted1, sorted2):
    """Takes 2 sorted lists, merges both list in sorted order, and returns the new list."""
    sorted_list = []
    while sorted1 and sorted2:
        # Takes an element out of the list which contains the smallest one, appends to the new sorted list
        if sorted1[0] < sorted2[0]:
            sorted_list.append(sorted1.pop(0))
        else:
            sorted_list.append(sorted2.pop(0))

    # Add what's left at the end of the new sorted list
    sorted_list += sorted1
    sorted_list += sorted2

    return sorted_list


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """
    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print("\nremove_adjacent")
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print("\nlinear_merge")
    test(linear_merge(["aa", "xx", "zz"], ["bb", "cc"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "xx"], ["bb", "cc", "zz"]), ["aa", "bb", "cc", "xx", "zz"])
    test(linear_merge(["aa", "aa"], ["aa", "bb", "bb"]), ["aa", "aa", "aa", "bb", "bb"])


# WARNING: DO NOT CHANGE OR DELETE THE FOLLOWING CODE:
if __name__ == "__main__":
    main()
