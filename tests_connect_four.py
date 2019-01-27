import unittest
from connect_four import GameChecker, Board, Game


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
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "X", "X", "X", "X"],  # Vertical win column
            2: ["O", "O", "X"],
            3: ["X"],
            4: ["O", "O", "X", "O", "X", "X"],
            5: ["O", "O", "X", "O"],
            6: ["O", "O", "X", "O", "X", "X"]
        }

        self.board3_no_win_or_draw = Board()
        self.board3_no_win_or_draw.cols = {
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "X", "O", "X", "X"],
            2: ["O", "O", "X"],
            3: ["X"],
            4: ["O", "O", "X", "O", "X", "X"],
            5: ["O", "O", "X", "O"],
            6: ["O", "O", "X", "O", "X", "X"]
        }

        self.board4_horizontal_win = Board()
        self.board4_horizontal_win.cols = {
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "O", "O", "X", "X"],
            2: ["O", "O"],
            3: ["O", "X", "O"],
            4: ["O", "O", "O", "X", "X"],
            5: ["X", "O", "O"],
            6: ["O", "O", "O", "O", "X", "X"]
        }

        self.board5_positive_diagonal_win = Board()
        self.board5_positive_diagonal_win.cols = {
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "O", "O", "X", "X"],
            2: ["O", "O", "O"],
            3: ["O", "X", "O"],  # Winning chain at [0]
            4: ["O", "O", "O", "X", "X"], # Winning chain at [1]
            5: ["X", "X", "O"], # Winning chain at [2]
            6: ["O", "O", "X", "O", "X", "X"] # Winning chain at [3]
        }

        self.board6_negative_diagonal_win = Board()
        self.board6_negative_diagonal_win.cols = {
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "O", "O", "X", "X"],
            2: ["O", "O", "O"],
            3: ["O", "X", "O"],  # Winning chain at [0]
            4: ["O", "O", "O", "X", "X"],  # Winning chain at [1]
            5: ["X", "X", "O"],  # Winning chain at [2]
            6: ["O", "O", "X", "O", "X", "X"]  # Winning chain at [3]
        }

        self.board7_draw = Board()
        self.board7_draw.cols = {
            0: ["O", "O", "X", "O", "X", "X"],
            1: ["X", "O", "O", "O", "X", "X"],
            2: ["O", "O", "O", "X", "X", "O"],
            3: ["O", "X", "X", "X", "O", "X"],
            4: ["O", "O", "O", "X", "O", "X"],
            5: ["O", "O", "X", "O", "X", "X"],
            6: ["O", "O", "X", "O", "X", "X"]
        }


class TestPlaceToken(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.game.add_player("Hzu", "X")

    def test_place_token(self):
        self.assertEqual(
            [],
            self.game.board.cols[0]
        )
        self.game.place_token(0, self.game.players[0])
        self.assertEqual(
            ["X"],
            self.game.board.cols[0]
        )

class TestIsGameComplete(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def is_game_complete_true_win(self):
        self.checker = GameChecker(self.examples.board2_vert_win)
        self.assertEqual(
            True,
            self.is_game_complete_true()
        )

    def is_game_complete_true_draw(self):
        self.checker = GameChecker(self.examples.board7_draw)
        self.assertEqual(
            True,
            self.is_game_complete_true()
        )

    def is_game_complete_false(self):
        self.checker = GameChecker(self.examples.board3_no_win_or_draw)
        self.assertEqual(
            False,
            self.is_game_complete_true()
        )


class TestIsThereAWinner(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_there_a_winner_true(self):
        self.checker = GameChecker(self.examples.board2_vert_win)
        self.assertEqual(
            True,
            self.checker.is_there_a_winner()
        )

    def test_is_there_a_winner_false(self):
        self.checker = GameChecker(self.examples.board7_draw)
        self.assertEqual(
            False,
            self.checker.is_there_a_winner()
        )


class TestDraw(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_draw_true(self):
        self.checker = GameChecker(self.examples.board7_draw)
        self.assertEqual(
            True,
            self.checker.is_there_a_draw()
        )

    def test_is_draw_false(self):
        self.checker = GameChecker(self.examples.board2_vert_win)
        self.assertEqual(
            False,
            self.checker.is_there_a_draw()
        )


class TestPositiveDiagonalWinChecks(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_positive_diagonal_win_true(self):
        self.checker = GameChecker(self.examples.board5_positive_diagonal_win)
        self.assertEqual(
            True,
            self.checker.is_positive_diagonal_win()
        )

    def test_is_positive_diagonal_win_false(self):
        self.checker = GameChecker(self.examples.board3_no_win_or_draw)
        self.assertEqual(
            False,
            self.checker.is_positive_diagonal_win()
        )


class TestNegativeDiagonalWinChecks(unittest.TestCase):
    def setUp(self):
        self.examples = Examples()

    def test_is_positive_diagonal_win_true(self):
        self.checker = GameChecker(self.examples.board6_negative_diagonal_win)
        self.assertEqual(
            True,
            self.checker.is_negative_diagonal_win()
        )

    def test_is_negative_diagonal_win_false(self):
        self.checker = GameChecker(self.examples.board3_no_win_or_draw)
        self.assertEqual(
            False,
            self.checker.is_negative_diagonal_win()
        )



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
        self.checker = GameChecker(self.examples.board3_no_win_or_draw)
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
        self.checker = GameChecker(self.examples.board3_no_win_or_draw)
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