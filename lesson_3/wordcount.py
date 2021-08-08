#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##   instructions were changed to deal with proper handling of punctuation
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in alphabetical order. Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. Remember to deal with punctuation. For example:
Alice     Alice:     "Alice      Alice,    Alice"   are all the same word   >>>> alice

BUT - In words like  Alice's   or   they're, the apostrophe is part of the word
so don't split them into into    Alice + s    or   they  +  re

3. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

4. Please use functions to prevent writing duplicate code.

In addition to  print_words(filename) and print_top(filename) functions,
you must write additional functions that read a file, build a word/count dict
and so on.

5. Make sure to write and submit tests for as much of your code as possible.
It's OK not to test 100% of your code
(it's OK not to test input from command line and actually reading files),
but try to reach a high percentage of testing of the rest of the code.
"""

import sys

# constants used for main()
REQUIRED_NUM_OF_ARGS = 3
ARG_OPTION = 1
ARG_FILE_NAME = 2
RANKING_TOP_LIMIT = 20


def print_words(filename):
    """Given a filename, counts how often each word appears in the text, and prints each word with the count."""
    count_words_and_print(filename)


def print_top(filename):
    """Given a filename, prints the top RANKING_TOP_LIMIT most common words sorted by the number of occurrences of each word."""
    count_words_and_print(filename, key=lambda item: item[1], reverse=True, limit=RANKING_TOP_LIMIT)


def count_words_and_print(filename, **kwargs):
    """
    Given a filename and a fn which knows how to count and sort the words,
    prints:
    word1 count1
    word2 count2
    ...
    """
    try:
        text_file = open(filename, 'r')
        words_with_count = words_with_count_dict(text_file)
        print_words_with_count(words_with_count, **kwargs)
        text_file.close()
    except FileNotFoundError:
        print(f"The provided filename '{filename}' doesn't exist")



def words_with_count_dict(text_file):
    """Given the text file, counts the number of words, and returns the dictionary {..., word: count, ...}"""
    words_with_count = {}
    for line in text_file:
        count_words_in_line(line, words_with_count)
    return words_with_count


def count_words_in_line(line, words_with_count):
    """Takes the entire line, counts the number of words in it, and updates the dictionary."""
    # Split the line by space, strip all the -- at the end of each word, split the words by --
    words = [word for split_word in line.split() for word in split_word.rstrip("--").split("--")]
    for word in words:
        chars_to_replace = ['"', ',', '.', '?', '!', ';', ':', '{', '[', '(', ')', ']', '}', '`', '_']
        word = word.lower().rstrip("'")
        for char in chars_to_replace:
            word = word.replace(char, "")
        count_value = words_with_count.get(word, 0)
        words_with_count.update({f"{word}": count_value + 1})


def print_words_with_count(words_with_count, limit=None, **kwargs):
    """
    Takes the words with count dictionary and prints:
    word1 count1
    word2 count2
    """
    sorted_words = sorted(words_with_count.items(), **kwargs)
    printable_words_with_count = sorted_words[:limit] if limit else sorted_words
    for word, count in printable_words_with_count:
        print(f"{word} {count}")


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    get user input - file name and which option --count or --topcount
    read text file, count and sort words
    """

    if len(sys.argv) != REQUIRED_NUM_OF_ARGS:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[ARG_OPTION]
    filename = sys.argv[ARG_FILE_NAME]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


def count_words_in_line_tests():
    """Tests of the count_words_in_line function"""
    actual = {}
    expected = {"i'm": 1, 'afraid': 1, 'i': 4, 'am': 1, 'sir': 1, 'said': 1, 'alice': 1, "can't": 1, 'remember': 1,
                'things': 1, 'as': 1, 'used': 1, 'and': 1, "don't": 1, 'keep': 1, 'the': 1, 'same': 1, 'size': 1,
                'for': 1, 'ten': 1, 'minutes': 1, 'together': 1}
    count_words_in_line("`I'm afraid I am, sir,' said Alice; `I can't remember things as I used--and I don't keep the "
                        "same size for ten minutes together!'", actual)
    assert actual == expected
    print("--- All count_words_in_line tests passed ---")


def count_words_in_line_tests():
    """Tests of the count_words_in_line function"""
    actual = {}
    expected = {"i'm": 1, 'afraid': 1, 'i': 4, 'am': 1, 'sir': 1, 'said': 1, 'alice': 1, "can't": 1, 'remember': 1,
                'things': 1, 'as': 1, 'used': 1, 'and': 1, "don't": 1, 'keep': 1, 'the': 1, 'same': 1, 'size': 1,
                'for': 1, 'ten': 1, 'minutes': 1, 'together': 1}
    count_words_in_line("`I'm afraid I am, sir,' said Alice; `I can't remember things as I used--and I don't keep the "
                        "same size for ten minutes together!'", actual)
    assert actual == expected
    print("--- All count_words_in_line tests passed ---")


if __name__ == "__main__":
    count_words_in_line_tests()
    print("--- All tests passed ---")
    # What else I could test?
    main()
