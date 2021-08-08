# Part 1
def translate_day(day):
    """
    Translate day name from English to Hebrew
    :param day: day in English
    :return: day in Hebrew (with English letters)
    """
    translations = {
        "sunday": "Yom Rishon",
        "monday": "Yom Shenee",
        "tuesday": "Yom Shlishee",
        "wednesday": "Yom Revi'ee",
        "thursday": "Yom Chameeshee",
        "friday": "Yom Sheeshee",
        "saturday": "Yom Shabat",
    }
    return translations[day.lower()]


def part1_get_friday_day():
    return translate_day("Friday")


# Part 2
def part2_delete_list_members(lst):
    """
    Delete list members
    :param lst: list whose members need to be deleted
    :return: updated list
    """
    for i in range(len(lst) - 1, -1, -1):
        del lst[i]

    return lst


# Part 3
def part3_is_bird_in_list(lst):
    """
    Check if the word "bird" is in the list received
    :param lst: list to check
    :return: message to print that answers the question of whether the word "bird" is in the list
    """
    message = "I don't found a bird"
    if "bird" in lst:
        message = "I found a bird!"
    return message


# Part 4
def part4_get_str_mult_of_3(num):
    """
    Return a string of a's and b's that answers whether a number from 0 till given num are multiples of 3
    If a number is a multiple of 3, return 'a' for this number, and 'b' otherwise.
    :param num: Number up to which to check (not inclusive)
    :return: String of a's and b's, a's for all number from 0 till num that are multiples of 3, b otherwise
    """
    message = ""
    for number in range(num):
        # add 'a' if the number is a multiple of 3, otherwise add 'b'
        if (number % 3) == 0:
            message = message + "a"
        else:
            message = message + "b"
    return message


# --------------------------------------------------
# WARNING - DO NOT CHANGE CODE BELOW THIS LINE
# --------------------------------------------------


if __name__ == '__main__':
    # Part 1
    print(part1_get_friday_day())

    # Part 2
    my_lst = list(range(1, 10))
    print(part2_delete_list_members(my_lst))

    # Part 3
    list_without_bird = ["boy", "girl", "lady", "dog", "pie"]
    print(part3_is_bird_in_list(list_without_bird))

    # Part 4
    print(part4_get_str_mult_of_3(10))
