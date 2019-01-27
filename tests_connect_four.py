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
            "X"
        ]

        self.board2_vert_win = Board()
        self.board2_vert_win.cols = {
            1: ["O", "O", "X", "O", "X", "X", "X"],
            2: ["X", "O", "X", "X", "X", "X", "O"],  # Vertical win column
            3: ["O", "O", "X"],
            4: ["X"],
            5: ["O", "O", "X", "O", "X", "X", "X"],
            6: ["O", "O", "X", "O"],
            7: ["O", "O", "X", "O", "X", "X", "X"]
        }

        self.board3_no_win = Board()
        self.board3_no_win.cols = {
            1: ["O", "O", "X", "O", "X", "X", "X"],
            2: ["X", "O", "X", "O", "X", "X", "O"],
            3: ["O", "O", "X"],
            4: ["X"],
            5: ["O", "O", "X", "O", "X", "X", "X"],
            6: ["O", "O", "X", "O"],
            7: ["O", "O", "X", "O", "X", "X", "X"]
        }

        self.board4_horizontal_win = Board()
        self.board4_horizontal_win.cols = {
            1: ["O", "O", "X", "O", "X", "X", "X"],
            2: ["X", "O", "O", "O", "X", "X", "O"],
            3: ["O", "O"],
            4: ["O", "X", "O"],
            5: ["O", "O", "O", "X", "X"],
            6: ["X", "O", "O"],
            7: ["O", "O", "O", "O", "X", "X", "X"]
        }


class TestVerticalWinChecks(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_vertical_win_true(self):
        self.checker = GameChecker(self.examples.board2_vert_win)
        self.assertEqual(
            True,
            self.checker.is_vertical_win()
        )

    def test_is_vertical_win_false(self):
        self.checker = GameChecker(self.examples.board3_no_win)
        self.assertEqual(
            False,
            self.checker.is_vertical_win()
        )


class TestHorizontalWinChecks(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_horizontal_win_true(self):
        self.checker = GameChecker(self.examples.board4_horizontal_win)
        self.assertEqual(
            True,
            self.checker.is_horizontal_win()
        )

    def test_is_horizontal_win_false(self):
        self.checker = GameChecker(self.examples.board3_no_win)
        self.assertEqual(
            False,
            self.checker.is_horizontal_win()
        )

class TestContainsFourConsecutive(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()
        self.checker = GameChecker(self.examples.vert_win_board)

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