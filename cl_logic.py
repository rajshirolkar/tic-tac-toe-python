import random
import sys


class Board:
    def __init__(self) -> None:
        self._rows = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __str__(self) -> str:
        s = "-------\n"
        for row in self._rows:
            for cell in row:
                s = s + "|"
                if cell == None:
                    s = s + " "
                else:
                    s = s + cell
            s = s + "|\n-------\n"
        return s

    def get(self, x, y):
        return self._rows[x][y]

    def set(self, x, y, value):
        self._rows[x][y] = value

    def _check_win(self, win_char):
        board = self._rows
        if board[0][0] == board[0][1] == board[0][2] == win_char:
            return win_char
        elif board[1][0] == board[1][1] == board[1][2] == win_char:
            return win_char
        elif board[2][0] == board[2][1] == board[2][2] == win_char:
            return win_char
        elif board[0][0] == board[1][0] == board[2][0] == win_char:
            return win_char
        elif board[0][1] == board[1][1] == board[2][1] == win_char:
            return win_char
        elif board[0][2] == board[1][2] == board[2][2] == win_char:
            return win_char
        elif board[1][1] == board[2][2] == board[0][0] == win_char:
            return win_char
        elif board[0][2] == board[1][1] == board[2][0] == win_char:
            return win_char
        else:
            return None


class Game:
    def __init__(self, playerX, playerO) -> None:
        self._board = Board()
        self._playerX = playerX
        self._playerO = playerO
        self.current_player = self._playerX
        self.current_char = "X"

    def is_against_human(self):
        """Function to get the player's choice
        whether they want to play with human or bod
        """
        print("     Play against : ")
        print("     1. Human ")
        print("     2. Computer ")
        self.gtype = int(input("     ---> Choice : "))
        return True if self.gtype == 1 else False

    def switch_player(self):
        if self.current_player == self._playerX:
            self.current_player = self._playerO
            self.current_char = "O"
            return
        self.current_player = self._playerX
        self.current_char = "X"

    def run(self):
        move_number = 0
        while move_number < 9:
            print(f"Take a turn Player {self.current_char}!")
            self.current_player.get_move(self._board, self.current_char)
            if self._board._check_win(self.current_char):
                print(f"{self.current_char} WINS!!!!!")
                sys.exit("Game Ended")

            move_number += 1
            self.switch_player()

        print("Draw!")


class Human:
    def get_move(self, board, char):
        # Show the board to the user
        print(board)

        # Input a move from the player
        row = int(input("Enter the row number (0-2) : "))
        column = int(input("Enter the column number (0-2) : "))

        # Do not allow players to play the same square
        if board.get(row, column) != None:
            print("Please play the move in an empty square!")
            self.get_move(board, char)

        board.set(row, column, char)
        return board


class Bot:
    def get_move(self, board, char):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board.get(row, column) != None:
            self.get_move(board, char)
        else:
            board.set(row, column, char)
            return board
