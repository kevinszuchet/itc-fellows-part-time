whitespace_symbols = [' ', '\n', '\r', '\t']


def remove_whitespace(s):
    while s[0] in whitespace_symbols:
        s = s[1:]
    while s[-1] in whitespace_symbols:
        s = s[:-1]
    return s


def remove_whitespace_revised(s):
    s_whitespace_symbols = ''.join(whitespace_symbols)
    return s.strip(s_whitespace_symbols)


my_string = """




                    hi hi
Write a function remove_whitespace that removes extra whitespace (spaces, new line, tab) from the beginning and end of a string. You should implement the functionality on your own and not use system functions.
After you’ve done that, find a system function that does this for you, and write a new function remove_whitespace_revised that uses the new function you’ve found. Submit both versions to hive.

        the end of the excercise
    
"""
my_string_l_r_stripped = remove_whitespace(my_string)
print("My string without whitespaces:")
print("------------------------------")
print(my_string_l_r_stripped)
print("Lengths: original {}, stripped {}".format(len(my_string), len(my_string_l_r_stripped)))

print("******************************")

my_string_l_r_stripped_revised = remove_whitespace_revised(my_string)
print("My string without whitespaces revised:")
print("------------------------------")
print(my_string_l_r_stripped_revised)
print("Lengths: original {}, stripped {}".format(len(my_string), len(my_string_l_r_stripped_revised)))

print("******************************")
print("The stripped strings are equal between them: ", my_string_l_r_stripped == my_string_l_r_stripped_revised)
