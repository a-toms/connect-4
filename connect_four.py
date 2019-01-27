from typing import Dict, Tuple, Sequence, List


class Play:
    def __init__(self):
        self.board = Board()





class GameStatusChecker:
    def __init__(self):
        pass

    def is_vertical_win(self):
        pass

    def is_horizontal_win(self):
        pass

    def is_pos_wiagonal_win(self):
        pass

    def is_neg_diagonal_win(self):
        pass

    def is_draw(self):
        pass

    def has_four_consecutive(self, some_list: List) -> bool:
        # There are three possible combinations of 4 in a set of 6 elements
        for i in range(3):
            consecutive = some_list[i:i+4]
            print(consecutive)
            print(set(consecutive))
            if len(set(consecutive)) == 1:

                return True
        return False





class Board:
    def __init__(self):
        self.column_1 = []
        self.column_2 = []
        self.column_3 = []
        self.column_4 = []
        self.column_5 = []
        self.column_6 = []
        self.column_7 = []


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token







