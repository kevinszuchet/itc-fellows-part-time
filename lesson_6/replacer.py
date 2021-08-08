import sys

NUM_REPLACEMENTS = 0
# Replacement rule (index, string to replace, char to replace with)
INDEX = 0
STR_TO_REPLACE = 1
CHAR_TO_REPLACE_WITH = 2


def replacer(*args):
    """
    Replace a character at a given index in a string with a different single character.
    It can handle multiple strings at the same time.
    """
    validate_user_input(*args)
    return replaced_strings(*args)


def replaced_strings(replacement_rules):
    replaced_strings = []

    for i in range(NUM_REPLACEMENTS + 1, len(replacement_rules), 3):
        replaced_string = replace_single(replacement_rules[i:i + 3])
        replaced_strings.append(replaced_string)

    print(replaced_strings)
    return replaced_strings


def validate_user_input(args):
    """Given the input of the user, checks that the structure of the arguments is valid."""
    if len(args) == 1:
        raise ValueError("Missing at least one replacement rule after the number of replacements.")

    num_of_replacements = args[NUM_REPLACEMENTS]
    if not num_of_replacements.isdigit():
        raise ValueError("The number of replacements has to be a positive integer.")

    number_of_rules_of_replacement = len(args[NUM_REPLACEMENTS + 1:])

    if number_of_rules_of_replacement % 3 != 0:
        raise SyntaxError("Any of the replacement rules has an invalid number of arguments.")
    elif (number_of_rules_of_replacement / 3) != int(num_of_replacements):
        raise ValueError(
            "The number of rules of replacement isn't the same as the number or replacements in the argument.")


def replace_single(replacement_rule):
    """Given a replacement rule, replaces a letter in a string."""
    index, string_to_replace, char_to_replace_with = deconstruct_replacement_rule(replacement_rule)
    validate_single(index, string_to_replace, char_to_replace_with)
    index = int(index)
    return string_to_replace[:index] + char_to_replace_with + string_to_replace[index + 1:]


def validate_single(index, string_to_replace, char_to_replace_with):
    """Given all the members of the rule, checks they are valid."""
    if not index.isdigit():
        # I decided to accept only positive integers as indexes
        raise ValueError(f"The index of the rule {index, string_to_replace, char_to_replace_with} has to be a number.")

    if int(index) >= len(string_to_replace):
        raise ValueError(
            f"The index of the rule number {index, string_to_replace, char_to_replace_with} is gte than the length of the string to replace.")


def deconstruct_replacement_rule(replacement_rule):
    """Given the replacement rule, takes the value of each member of it, and returns those values."""
    return replacement_rule[INDEX], replacement_rule[STR_TO_REPLACE], replacement_rule[CHAR_TO_REPLACE_WITH]


# WARNING: DO NOT CHANGE CODE BELOW THIS LINE


HELP_STRING = """Welcome to the replacer!
Replacer knows to replace a character at a given index in a string with a different single character.
It knows to do so for multiple strings.
It prints a the strings after replacement.

Usage:
"ex2-replacer.py --help" - display this message 
"ex2-replacer.py num_replacements [index1 str1 char_to_replace_with1 [index2 str2 char_to_replace_with2]...]"

Examples:
"ex2-replacer.py 0" - do not do any replacements.  Will print "" - empty string
"ex2-replacer.py 1 0 boat g" - will print "goat"
"ex2-replacer.py 2 0 boat g 2 boat o" - will print "goat boot"  
"""

NUM_ARGS_NO_ARGS = 1
NUM_ARGS_HELP = 2


def main():
    if len(sys.argv) == NUM_ARGS_HELP and sys.argv[1] == '--help':
        print(HELP_STRING)
        return
    elif len(sys.argv) == NUM_ARGS_NO_ARGS:
        print(f'ERROR: No arguments were given.\nFor proper usage:\n{HELP_STRING}', )
        return

    try:
        result = replacer(sys.argv[1:])
    except Exception as ex:
        print(f'ERROR: Invalid input: {ex}\nFor proper usage:\n{HELP_STRING}', )
    else:
        print(f'SUCCESS: Result of replacing the letters is:\n', ' '.join(result))


if __name__ == '__main__':
    main()
