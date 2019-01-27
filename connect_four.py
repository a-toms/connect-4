from typing import Dict, Tuple, Sequence, List


class Play:
    def __init__(self):
        self.board = Board()








class Board:
    def __init__(self):
        self.cols = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: []
        }


class GameChecker:
    def __init__(self, board):
        self.board = board


    def is_there_a_winner(self):
        for win_check in (
                self.is_vertical_win(),
                self.is_horizontal_win(),
                self.is_negative_diagonal_win(),
                self.is_positive_diagonal_win()
        ):
            if win_check:
                return True
            else:
                return False

    def is_vertical_win(self) -> bool:
        # Check each column for 4 identical consecutive elements.
        for k in self.board.cols.keys():
            if self.has_four_consecutive(self.board.cols[k]):
                return True
        else:
            return False

    def is_horizontal_win(self) -> bool:
        # Build each row. Check each row for 4 identical consecutive elements.
        for i in range(6):  # The column height is 6
            row = []

            for k in self.board.cols.keys():
                try:
                    row.append(self.board.cols[k][i])
                except IndexError:
                    row.append(None)
            if self.has_four_consecutive(row):
                return True
        else:
            return False

    def is_positive_diagonal_win(self) -> bool:
        starting_indices = ((0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0))
        for x, y in starting_indices:
            # Build diagonal
            diagonal = []
            for i in range(6):  # The maximum diagonal length is 6 for the board.
                try:
                    diagonal.append(self.board.cols[x + i][y + i])
                except (IndexError, KeyError):  # Excepts when the diagonal exceeds the board's dimensions.
                    diagonal.append(None)
            if self.has_four_consecutive(diagonal):
                return True
        else:
            return False

    def is_negative_diagonal_win(self) -> bool:
        starting_indices = ((0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5))
        for x, y in starting_indices:
            # Build diagonal
            diagonal = []
            for i in range(6):  # The maximum diagonal length is 6 for the board.
                try:
                    diagonal.append(self.board.cols[x + i][y - i])
                except (IndexError, KeyError):  # Excepts when the diagonal exceeds the board's dimensions.
                    diagonal.append(None)
            if self.has_four_consecutive(diagonal):
                return True
        else:
            return False

    def is_draw(self) -> bool:
        if self.is_there_a_winner() is False:
            print(sum(len(v) for v in self.board.cols.values()))
            return sum(len(v) for v in self.board.cols.values()) == 42


    def has_four_consecutive(self, some_list: List) -> bool:
        # There are four possible combinations of 4 in a set of 7 elements
        for i in range(4):
            consecutive = some_list[i:i+4]
            if len(consecutive) == 4 and len(set(consecutive)) == 1:
                return True
        return False



class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token







