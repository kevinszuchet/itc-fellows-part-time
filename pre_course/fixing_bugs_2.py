"""
General instructions:
The errors you will see now may not be as instant as the ones in the previous exercise.
Check your answers before submitting them.
Make sure you only FIX the bugs in the current program. You do not need to write a new
program, nor add lines of code.
"""


# Part 1
def part1_list_to_zeros(lst):
    """
    Return list after changing all values to 0's.
    Hint: read more about looping through lists.
    :param lst: List to change values in
    :return: List after changing values to zeros.
    """
    for i in range(len(lst)):
        lst[i] = 0
    return lst


# Part 2
def part2_print_10j_i_10_times():
    """
    Print 10 "j"s followed by an "i", 10 times
    """
    lst = []
    for i in ["i"] * 10:
        for j in ["j"] * 10:
            lst.append(j)
        lst.append(i)
    print(lst)


# Part 3
"""
    You had 4 exams, and your average score is Failed.
    Now, you had new exams and you want to see if your average improved.
    You want to make sure you did not Fail anymore (Fail is < 60 on average).
    What is wrong with this code? Fix it    
"""


def part3_retry_until_pass():
    """
    Starts from a failing grade (average 55) and gets new scores until pass (>= 60).
    """
    n_tests = 4
    tot_grade = 220
    while round(tot_grade / float(n_tests), 1) < 60:
        grade_str = input("What is the new grade that you got?")
        # What do happen with the grades greater than 100?
        while not grade_str.isdigit():
            grade_str = input("You did not submit a number. What is your new grade")
        grade_int = int(grade_str)
        n_tests += 1
        tot_grade += grade_int
        print("Your new average score is: ", round(tot_grade / float(n_tests), 1))
        if round(tot_grade / float(n_tests), 1) < 60:
            print("You still Failed")
    print("You Passed!")


# Part 4
"""
Run the following code, that will ask you for the current time (hour), and how long you want to
stay, and tell you when you will leave. After you've seen how it works, run it again, and when
asked for what time is it, just press OK (Enter). What happened? Fix it.
"""


def part4_plan_my_day():
    """
    Asks for current time and how long you want to wait, and suggests the time to leave
    :return:
    """
    # I took 0 as the default value for each inputs trying not to add more lines to the code.
    # If I could add some code, I would validate that both inputs were digits like in part 3
    curr_t_str = input("What time is it now (hour)?")
    curr_t_int = int(curr_t_str or 0)

    wait_t_str = input("How long do you want to wait (hours)")
    wait_t_int = int(wait_t_str or 0)

    final_t_int = (curr_t_int + wait_t_int) % 24
    print("You will leave at: ", final_t_int)


# --------------------------------------------------
# WARNING - DO NOT CHANGE CODE BELOW THIS LINE
# --------------------------------------------------


if __name__ == '__main__':
    # Part 1
    my_lst = [1, 2, 3, 4, 4, 5, 9, 8, 7, 9]
    print(part1_list_to_zeros(my_lst))

    # Part 2
    part2_print_10j_i_10_times()

    # Part 3
    part3_retry_until_pass()

    # Part 4
    part4_plan_my_day()
