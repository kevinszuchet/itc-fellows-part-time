def print_pattern():
    rows = 5
    for i in range(0, rows + 1):
        print(' '.join(['*'] * i))

    for i in range(rows - 1, 0, -1):
        print(' '.join(['*'] * i))


# print_pattern()
