import unittest
from connect_four import GameStatusChecker, Board


class Examples:
    def __init__(self):
        self.vert_win_board = Board()
        self.vert_win_board.column_1 = [
            "0", "0", "X", "X", "X", "X"
        ]
        self.vert_win_board.column_2 = [
            "0", "0", "X", "O", "X", "X"
        ]


class TestGameStatusChecker(unittest.TestCase):
    def setUp(self):
        self.checker = GameStatusChecker()
        self.examples = Examples()

    def test_contains_four_consecutive_true(self):
        self.assertEqual(
            True,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.column_1
            )
        )

    def test_contains_four_consecutive_false(self):
        self.assertEqual(
            False,
            self.checker.has_four_consecutive(
                self.examples.vert_win_board.column_2
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