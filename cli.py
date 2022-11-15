from logic import TicTacToe


if __name__ == "__main__":
    game = TicTacToe()

    if game.is_against_human():
        game.play_with_human()
    else:
        game.play_with_computer()
