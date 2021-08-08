import json


def map_pieces(path):
    file = open(path)
    content = file.read()
    file.close()
    pieces = content.split(';')
    pieces_dict = dict()
    for puzzle in pieces:
        idx, content = puzzle.split(',', 1)
        parsed_list = json.loads(content.strip())
        pieces_dict[idx.strip()] = {
            "pieces": parsed_list,
            "rotations performed": 0,
            "position": {"x": None, "y": None}
        }
    return pieces_dict


def create_board(rows, cols):
    board = []
    for _ in range(rows):
        board.append([None] * cols)
    return board


def find_corners(pieces_dict, board):
    x_len = len(board[0])
    y_len = len(board)

    for piece in pieces_dict:
        if pieces_dict[piece]['top'] == 0 and pieces_dict[piece]['left'] == 0:
            board[0][0] = piece
            pieces_dict[piece]['position'] = {"x": 0, "y": 0}
            print(f'eureka {piece}', 1)
        elif pieces_dict[piece]['top'] == 0 and pieces_dict[piece]['right'] == 0:
            board[0][x_len - 1] = piece
            pieces_dict[piece]['position'] = {"x": x_len - 1, "y": 0}
            print(f'eureka {piece}', 2)
        elif pieces_dict[piece]['bottom'] == 0 and pieces_dict[piece]['left'] == 0:
            board[y_len - 1][0] = piece
            pieces_dict[piece]['position'] = {"x": 0, "y": y_len - 1}
            print(f'eureka {piece}', 3)

        elif pieces_dict[piece]['bottom'] == 0 and pieces_dict[piece]['right'] == 0:
            board[y_len - 1][x_len - 1] = piece
            pieces_dict[piece]['position'] = {"x": x_len - 1, "y": y_len - 1}
            print(f'eureka {piece}', 4)

    return pieces_dict, board


def solve_puzzle(pieces_dict, board):
    pieces, new_board = find_corners(pieces_dict, board)
    print(new_board)


def main():
    path = '/Users/jkru/DATA/DEV/JK/Repos/ds_itc/01_exercises/03_lists_tuples_and_venv/ex4_the_puzzle/ex4 - puzzle.txt'
    mapped_pieces = map_pieces(path)
    board = create_board(10, 10)
    solve_puzzle(mapped_pieces, board)


if __name__ == "__main__":
    main()
