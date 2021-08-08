def build_matrix(rows, cols):
    matrix = []
    for i in range(0, rows):
        matrix.append([])
        for j in range(0, cols):
            value = (i + 1) * (j + 1)
            matrix[i].append(value)
    return matrix


# A simple, tiny, custom pretty print for my matrix
# For now, it works only with spaces instead of tabs
def pretty_print_matrix(matrix):
    for row in matrix:
        print('|', end=' ')
        numbers_spaces_count = 0
        for col in row:
            numbers_spaces_count += len(str(col))
            print(col, end=' | ')
        print()
        # Num. of chars in each col + 1 more pipe than cols + 2 spaces per col
        # 3 * Num. of cols + 1 (the extra pipe)
        cols_count = len(row)
        dash_count = (3 * cols_count) + 1 + numbers_spaces_count
        print('-' * dash_count)


# my_matrix = build_matrix(3, 3)
# pretty_print_matrix(my_matrix)
