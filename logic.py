import random
import sys
import pandas as pd
import uuid


class Database:
    def __init__(self) -> None:
        self.path = "game_data.csv"
        try:
            with open("game_data.csv"):
                self.games = pd.read_csv(self.path, index_col=0)
        except FileNotFoundError:
            self.games = pd.DataFrame(
                columns=[
                    "game_id",
                    "playerX",
                    "playerO",
                    "winner",
                    "winner_char",
                    "move1",
                    "move2",
                    "move3",
                    "move4",
                    "move5",
                    "move6",
                    "move7",
                    "move8",
                    "move9",
                ]
            )

    # Create a new game
    def insert_game(self, game_id, playerX, playerO):
        self.games = self.games.append(
            {"game_id": game_id, "playerX": playerX, "playerO": playerO},
            ignore_index=True,
        )
        self.save()

    # Insert a move into a game
    def insert_move(self, game_id, move_number, coordinates):
        game = self.games[self.games["game_id"] == game_id]
        if len(game) == 0:
            return False
        move_column = "move" + str(move_number)
        self.games.loc[self.games["game_id"] ==
                       game_id, move_column] = coordinates
        self.save()
        return True

    # Update the winner of a game
    def update_winner(self, game_id, winner, win_char):
        game = self.games[self.games["game_id"] == game_id]
        if len(game) == 0:
            return False
        self.games.loc[self.games["game_id"] == game_id, "winner"] = winner
        self.games.loc[self.games["game_id"] ==
                       game_id, "winner_char"] = win_char
        self.save()
        return True

    # Get all games in the database
    def get_all_games(self):
        return self.games

    # Get a specific game by game_id
    def get_game_by_id(self, game_id):
        return self.games[self.games["game_id"] == game_id]

    def get_stats(self):
        games = self.games
        total_games = len(games)
        if total_games == 0:
            return {
                "total_games": 0,
                "human_wins": 0,
                "bot_wins": 0,
                "win_percentages": {"human": 0, "bot": 0},
            }
        human_wins = len(games[games["winner"] == "Human"])
        bot_wins = len(games[games["winner"] == "Bot"])
        human_win_percentage = human_wins / total_games * 100
        bot_win_percentage = bot_wins / total_games * 100
        return {
            "total_games": total_games,
            "human_wins": human_wins,
            "bot_wins": bot_wins,
            "win_percentages": {
                "human": human_win_percentage,
                "bot": bot_win_percentage,
            },
        }

    def get_most_common_first_move(self):
        games = self.games
        if len(games) == 0:
            return None
        first_moves = games["move1"]
        first_move_counts = first_moves.value_counts()
        if len(first_move_counts) == 0:
            return None
        most_common_first_move = first_move_counts.index[0]
        return most_common_first_move

    def get_least_common_first_move(self):
        games = self.games
        if len(games) == 0:
            return None
        first_moves = games["move1"]
        first_move_counts = first_moves.value_counts()
        if len(first_move_counts) == 0:
            return None
        least_common_first_move = first_move_counts.index[len(
            first_move_counts) - 1]
        return least_common_first_move

    # Save the DataFrame to the CSV file
    def save(self):
        self.games.to_csv(self.path)


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
        self.db = Database()
        self.game_id = uuid.uuid4().hex
        self.db.insert_game(
            self.game_id, self._playerX.type, self._playerO.type)

    def switch_player(self):
        if self.current_player == self._playerX:
            self.current_player = self._playerO
            self.current_char = "O"
            return
        self.current_player = self._playerX
        self.current_char = "X"

    def run(self):
        move_number = 1
        while move_number <= 9:
            print(f"Take a turn Player {self.current_char}!")
            row, column = self.current_player.get_move(
                self._board, self.current_char)
            coordinates = str(row) + '-' + str(column)
            self.db.insert_move(self.game_id, move_number, coordinates)
            if self._board._check_win(self.current_char):
                print(f"{self.current_char} WINS!!!!!")
                self.db.update_winner(
                    self.game_id, self.current_player.type, self.current_char)
                print(self.db.get_stats())
                print('Most common first move : ',
                      self.db.get_most_common_first_move())
                print('Least common first move : ',
                      self.db.get_least_common_first_move())
                # self.db.save()
                sys.exit("Game Ended")

            move_number += 1
            self.switch_player()

        print("Draw!")
        self.db.update_winner(self.game_id, "Draw", "NONE")
        print(self.db.get_stats())
        # self.db.save()


class Human:
    def __init__(self) -> None:
        self.type = "Human"

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
        return (row, column)


class Bot:
    def __init__(self) -> None:
        self.type = "Bot"

    def get_move(self, board, char):
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board.get(row, column) != None:
            self.get_move(board, char)
        else:
            board.set(row, column, char)
            print(board)
        return (row, column)
