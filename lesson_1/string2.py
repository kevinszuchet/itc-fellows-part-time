""" This program has been adapted for use by GVAHIM
       - the main revisions regard pep8 compliance and use of variable names
Copyright 2010 Google Inc.
Licensed under the Apache License, Version 2.0
http://www.apache.org/licenses/LICENSE-2.0

Google's Python Class
http://code.google.com/edu/languages/google-python-class/

Additional basic string exercises  """


# E. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(my_inputs):
    """
    Takes a string. If the length is at least 3, returns the string + 'ing' unless the word already contains the 'íng'.
    In that case, it returns the string + 'ly'.
    If the string length is less than 3, returns the string unchanged.
    """
    if len(my_inputs) >= 3:
        return my_inputs + "ing" if my_inputs[-3:] != "ing" else my_inputs + "ly"

    return my_inputs


# F. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(my_input):
    """Takes a string, changes 'not bad' for 'good', and returns the new string."""
    bad_appearance = my_input.find("bad")
    not_appearance = my_input.find("not")
    if not_appearance < bad_appearance:
        # The text before 'not' + the word 'good' + the rest of the text after 'bad'
        return my_input[:not_appearance] + "good" + my_input[bad_appearance + 3:]
    return my_input


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, input1 and input2, return a string of the form
#  input1-front + input2-front + input1-back + input2-back
def front_back(input1, input2):
    """
    Takes two inputs. Cuts each one in the middle. Returns a new string with the first half of both inputs
    and then the last half of both inputs.
    """
    front_1, back_1 = input_halves(input1)
    front_2, back_2 = input_halves(input2)
    return front_1 + front_2 + back_1 + back_2


def input_halves(input):
    """Takes an input, returns the front and the back of it considering the front_back instructions."""
    count = len(input)
    middle = count // 2 if count % 2 == 0 else (count // 2) + 1
    return input[:middle], input[middle:]


# WARNING: Do not change this function!!!
def test(got, expected):
    """ simple test() function used in main() to print
        what each function returns vs. what it's supposed to return. """

    if got == expected:
        prefix = " OK "
    else:
        prefix = "  X "
    print("%s got: %s expected: %s" % (prefix, repr(got), repr(expected)))


# WARNING: Do not change this function!!!
def main():
    """ main() calls the above functions with interesting inputs,
        using test() to check if each result is correct or not. """

    print("\nverbing")
    test(verbing("hail"), "hailing")
    test(verbing("swiming"), "swimingly")
    test(verbing("do"), "do")

    print("\nnot_bad")
    test(not_bad("This movie is not so bad"), "This movie is good")
    test(not_bad("This dinner is not that bad!"), "This dinner is good!")
    test(not_bad("This tea is not hot"), "This tea is not hot")
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print("\nfront_back")
    test(front_back("abcd", "xy"), "abxcdy")
    test(front_back("abcde", "xyz"), "abcxydez")
    test(front_back("Kitten", "Donut"), "KitDontenut")


# WARNING: Do not change this function!!!
if __name__ == "__main__":
    main()
