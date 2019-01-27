from typing import Dict, Tuple, Sequence, List


class Play:
    def __init__(self):
        self.board = Board()








class Board:
    def __init__(self):
        self.cols = {
            1 : [],
            2 : [],
            3 : [],
            4 : [],
            5 : [],
            6 : [],
            7 : []
        }


class GameChecker(Board):
    def __init__(self):
        pass

    def is_vertical_win(self):
        # Check each column for 4 identical consecutive elements
        for k in self.cols.keys():
            if self.has_four_consecutive(self.cols[k]):
                return True
        else:
            return False

    def is_horizontal_win(self):
        pass

    def is_pos_wiagonal_win(self):
        pass

    def is_neg_diagonal_win(self):
        pass

    def is_draw(self):
        pass

    def has_four_consecutive(self, some_list: List) -> bool:
        # There are four possible combinations of 4 in a set of 7 elements
        for i in range(4):
            consecutive = some_list[i:i+4]
            if len(set(consecutive)) == 1:
                return True
        return False



class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token







