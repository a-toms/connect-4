import unittest
from connect_four import GameChecker, Board


class Examples:
    def __init__(self):
        self.vert_win_board = Board()
        self.vert_win_board.column_1 = [
            "O", "O", "X", "X", "X", "X"
        ]
        self.vert_win_board.column_2 = [
            "O", "O", "X", "O", "X", "X"
        ]
        self.vert_win_board.row_1 = [
            "O", "O", "O", "O", "X", "X", "X"
        ]
        self.vert_win_board.row_2 = [
            "O", "O", "X", "O", "X", "X", "X"
        ]


class TestGameStatusChecker(unittest.TestCase):
    def setUp(self):
        self.checker = GameChecker()
        self.examples = Examples()

    def test_contains_four_consecutive_true_column(self):
        self.assertEqual(
            True,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.column_1
            )
        )

    def test_contains_four_consecutive_false_column(self):
        self.assertEqual(
            False,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.column_2
            )
        )

    def test_contains_four_consecutive_true_row(self):
        self.assertEqual(
            True,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.row_1
            )
        )
    def test_contains_four_consecutive_false_row(self):
        self.assertEqual(
            False,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.row_2
            )
        )


    def test_is_vertical_win(self):
        pass

    def test_is_horizontal_win(self):
        pass

    def test_is_pos_diagonal_win(self):
        pass

    def test_is_neg_diagonal_win(self):
        pass