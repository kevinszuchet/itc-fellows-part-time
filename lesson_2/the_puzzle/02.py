import json
from pprint import pprint

PUZZLE_PATH = '/Users/jkru/DATA/DEV/JK/Repos/ds_itc/01_exercises/03_lists_tuples_and_venv/ex4_the_puzzle/' \
              'mini2.txt'
AMOUNT_OF_COLUMNS = 3
AMOUNT_OF_ROWS = 3


class PuzzleSolver(dict):
    def __init__(self):
        super().__init__()
        self.board = self.create_board(AMOUNT_OF_ROWS, AMOUNT_OF_COLUMNS)
        self.pieces = self.map_pieces(PUZZLE_PATH)
        self.solve_board()

    @staticmethod
    def map_pieces(path):

        # READING THE SOURCE
        file = open(path)
        content = file.read()
        file.close()

        # LIST OF PIECES
        pieces = content.split(';')
        pieces_dict = dict()

        # MAPPING THE LIST OF PIECES TO A DICT
        for piece in pieces:
            piece_id, content = piece.split(',', 1)
            parsed_list = json.loads(content.strip())
            pieces_dict[piece_id.strip()] = {
                "id": piece_id.strip(),
                "original_pieces": [x for x in parsed_list],
                "final_pieces": [x for x in parsed_list],
                "rotations_performed": 0,
            }
        return dict(sorted(pieces_dict.items()))

    @staticmethod
    def rotate_piece(piece):
        piece['rotations_performed'] += 1
        piece['final_pieces'] = [piece['final_pieces'][-1]] + piece['final_pieces'][:-1]
        return piece

    @staticmethod
    def create_board(rows, cols):
        board = []
        for _ in range(rows):
            board.append([None] * cols)
        return board

    def __dict__(self):
        return {"pieces": self.pieces, "board": self.board}

    def __str__(self):
        return {"pieces": self.pieces, "board": self.board}

    def move_pointer(self, position):
        if len(position) != 2:
            raise ValueError('only coordinates expected')
        if position[0] == AMOUNT_OF_ROWS - 1 and position[1] == AMOUNT_OF_COLUMNS - 1:
            raise ValueError('LAST')
        if position[0] > AMOUNT_OF_ROWS - 1:
            raise ValueError("trying to access a row that doesn't exist")
        if position[1] > AMOUNT_OF_COLUMNS - 1:
            raise ValueError("trying to access a column that doesn't exist")
        copy = [x for x in position]
        copy[1] += 1
        try:
            _ = self.board[copy[0]][copy[1]]
        except IndexError:
            copy[0] += 1
            copy[1] = 0
        return copy

    def solve_board(self):
        used_ids = set()
        for r in range(AMOUNT_OF_ROWS):
            for c in range(AMOUNT_OF_COLUMNS):
                current_place = [r, c]
                # print(f"\nCurrent place {current_place}")
                values = {
                    "top": None,
                    "right": None,
                    "bottom": None,
                    "left": None,
                }

                # finding previous values
                if self.board[r][c - 1] and self.board[r][c - 1] is not None:
                    values['left'] = self.board[r][c - 1]['final_pieces'][1]
                if self.board[r - 1][c] and self.board[r - 1][c] is not None:
                    values['top'] = self.board[r - 1][c]['final_pieces'][2]

                # finding side board edges
                if c == 0:
                    values['left'] = 0
                elif c == AMOUNT_OF_COLUMNS - 1:
                    values['right'] = 0

                # finding top bottom board edges
                if r == 0:
                    values['top'] = 0
                elif r == AMOUNT_OF_ROWS - 1:
                    values['bottom'] = 0

                seeked_sequence = [values['top'], values['right'], values['bottom'], values['left']]

                # looking for a matching piece
                for key_id in self.pieces:
                    if key_id not in used_ids:
                        # print(
                        #     f"Checking piece id {key_id} "
                        #     f"Used ids: {used_ids}")
                        piece = self.pieces[key_id]
                        match = False
                        while piece['rotations_performed'] < 3 and not match:
                            inner_match = True
                            for idx in range(4):
                                if seeked_sequence[idx] is not None and seeked_sequence[idx] != \
                                        piece['final_pieces'][idx]:
                                    inner_match = False
                                    break
                            if not inner_match:
                                self.rotate_piece(piece)
                            else:
                                match = True
                        if match:
                            self.board[r][c] = piece
                            used_ids.add(key_id)
                            break
        # caca = self.create_board(AMOUNT_OF_ROWS, AMOUNT_OF_COLUMNS)
        # for r in range(AMOUNT_OF_ROWS):
        #     for c in range(AMOUNT_OF_COLUMNS):
        #         caca[r][c] = (self.board[r][c]['id'], self.board[r][c]['rotations_performed'])

        print('finished')
        print(self.board)


if __name__ == "__main__":
    puzzle = PuzzleSolver()

    # pprint(puzzle.__dict__())
    puzzle.rotate_piece(puzzle.pieces['1'])
