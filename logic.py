import random


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def print_board(board):
    for row in board:
        print(*row)


def check_win(board, win_char):
    """Checks if the board is winning for the character passed
    Args:
        board (List[int][int])
        win_char (str): Check if the character won or not
    Returns:
        List[str]: Modified board
    """
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


def is_against_human():
    print("Play against : ")
    print("1. Human ")
    print("2. Computer ")
    gtype = int(input("Choice : "))
    return True if gtype == 1 else False


def get_computer_move(board):
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    if board[row][column] != None:
        get_computer_move(board)
    else:
        board[row][column] = "O"
        return board


def play_with_human(players):
    board = make_empty_board()
    winner = None
    turn = True
    move_number = 0
    while move_number < 9 and winner == None:
        print(f"Take a turn {players[turn]}!")

        # Show the board to the user
        print_board(board)

        # Input a move from the player
        row = int(input("Enter the row number (0-2) : "))
        column = int(input("Enter the column number (0-2) : "))

        # Do not allow players to play the same square
        if board[row][column] != None:
            print("Please play the move in an empty square!")
            continue

        if turn:
            board[row][column] = "X"
            winner = check_win(board, "X")
        else:
            board[row][column] = "O"
            winner = check_win(board, "O")

        # Increment the number of moves played
        move_number += 1
        # Update who's turn it is
        turn = not turn

    if winner == None:
        print("Draw")
    else:
        print(f"{players[not turn]} is the winner!! ")


def play_with_computer():
    board = make_empty_board()
    move_number = 0
    while move_number < 9:
        print(f"--------Take a turn Player!-----------")

        # Show the board to the user
        print_board(board)

        # Input a move from the player
        row = int(input("Enter the row number (0-2) : "))
        column = int(input("Enter the column number (0-2) : "))

        # Do not allow players to play the same square
        if board[row][column] != None:
            print("Please play the move in an empty square!")
            continue

        board[row][column] = "X"
        if check_win(board, "X"):
            print("****Congratulations You Win!****")
            return

        get_computer_move(board)

        if check_win(board, "X"):
            print("You lost! Better luck next time. :( ")
            return

        # Increment the number of moves played
        move_number += 2
