#!/usr/bin/python -tt
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

No need to submit tests, but make sure you try your code on numerous files and that it works.
"""

import random
import sys

NUMBER_OF_REQUIRED_ARGS = 2
FILE_NAME = 1
INITIAL_WORD_ARG = 2
NUMBER_OF_WORDS = 200
INITIAL_WORD = "the"


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    mimic = {}
    text = get_text(filename)
    words = text.split()
    for i, word in enumerate(words):
        if (i + 1) < len(words):
            next_word = words[i + 1]
            following_words = mimic.get(word, []) + [next_word]
            mimic.update({word: following_words})

    return mimic


def get_text(filename):
    """Given a filename, tries to read the text inside and returns it."""
    try:
        text_file = open(filename, 'r')
        text = text_file.read()
        text_file.close()
        return text
    except FileNotFoundError:
        print(f"The provided filename '{filename}' doesn't exist")
        sys.exit(1)


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    for i in range(NUMBER_OF_WORDS):
        if word:
            print(word, end=' ')
        following_words = mimic_dict.get(word, [''])
        word = random.choice(following_words)


def main():
    """ Provided main(), calls mimic_dict() and mimic() """
    if len(sys.argv) < NUMBER_OF_REQUIRED_ARGS:
        print("usage: ./mimic.py file-to-read [initial-word]")
        sys.exit(1)

    my_dict = mimic_dict(sys.argv[FILE_NAME])
    initial_word = sys.argv[INITIAL_WORD_ARG] if len(sys.argv) > NUMBER_OF_REQUIRED_ARGS else INITIAL_WORD
    print_mimic(my_dict, initial_word)


if __name__ == "__main__":
    main()
