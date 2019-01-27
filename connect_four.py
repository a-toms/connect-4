from typing import Dict, Tuple, Sequence, List
import os
import time


class Game:
    def __init__(self):
        self.board = Board()
        self.game_checker = GameChecker(self.board)
        self.players = []

    def play(self):
        print("Welcome to Connect 4!")
        self.get_players_names()
        print("Let's play Connect 4!")
        self.wait(3)
        winning_player = self.run_loop_until_game_ends_and_get_winner()
        winning_player.show_winner_message()

    def get_players_names(self) -> None:
        name_1 = input("Please enter player 1's name:\t")
        self.add_player(name_1, "X")
        print(f"Thanks {name_1.title()}.")
        name_2 = input("Please enter player 2's name:\t")
        self.add_player(name_2, "O")
        print(f"Thanks {name_2.title()}.")

    def add_player(self, player_name, player_token) -> None:
        self.players.append(Player(player_name, player_token))

    def wait(self, seconds):
        while seconds > 0:
            print(seconds)
            time.sleep(1)
            seconds -= 1

    def run_loop_until_game_ends_and_get_winner(self):
        self.board.clear_screen()
        while True:
            for active_player in self.players:
                self.board.clear_screen()
                self.board.show()
                self.move(active_player)
                if self.game_checker.is_game_complete():
                    return active_player

    def move(self, active_player) -> None:
        col = self.get_column(active_player)
        self.place_token(col, active_player)

    def place_token(self, column, player) -> None:
        print(self.board.cols[column])
        self.board.cols[column].append(player.token)

    def get_column(self, active_player) -> int:
        column = int(input(
            f"{active_player.name.title()}, "
            f"please enter the column to place your piece.\t"
        ))
        if column not in (self.board.cols.keys()):
            "That column was not found. I will ask again."
            return self.move(active_player)
        if len(self.board.cols[column]) == 6:
            "That column is full. I will ask again"
            return self.move(active_player)
        return column + 1


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def show_winner_message(self):
        print(f"Congratulations! {self.name.title()} won the game!")

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

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def show(self) -> None:
        right_divider = " |"
        space = " "
        board_title = "--~--   Connect Four    --~--"
        board_line = "-----------------------------"
        row_numbers = "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
        print(board_title + "\n")
        for i in range(6, -1, -1):  # The column height is 6. Countdown from 6.
            row = "|"
            for k in self.cols.keys():
                try:
                    row += space + self.cols[k][i] + right_divider
                except IndexError:
                    row += space + space + right_divider
            print(row)
        print(board_line)
        print(row_numbers)


class GameChecker:
    def __init__(self, board):
        self.board = board

    def is_game_complete(self):
        return self.is_there_a_winner() and self.is_there_a_draw()

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

    def is_there_a_draw(self) -> bool:
        # Checks if there is a draw based on any win and if the board is full.
        if self.is_there_a_winner() is False:
            return sum(len(v) for v in self.board.cols.values()) == 42
        else:
            return False

    def has_four_consecutive(self, some_list: List) -> bool:
        # There are four possible combinations of 4 in a set of 7 elements
        for i in range(4):
            consecutive = some_list[i:i+4]
            if len(consecutive) == 4 and len(set(consecutive)) == 1:
                if None not in consecutive:
                    return True
        return False


if __name__ == '__main__':
    Game().play()




