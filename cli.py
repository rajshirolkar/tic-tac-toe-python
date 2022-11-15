from logic import (
    is_against_human,
    play_with_computer,
    play_with_human,
)


human_players = {True: "Player 1 (X)", False: "Player 2 (O)"}

computer_player = {True: "Player 1 (X)", False: "Computer (O)"}


if __name__ == "__main__":
    human_game = is_against_human()
    if human_game:
        play_with_human(human_players)
    else:
        play_with_computer()

# if __name__ == '__main__':
#     board = make_empty_board()
#     winner = None
#     turn = True
#     move_number = 0
#     while (move_number < 9 and winner == None):
#         print(f"Take a turn {human_players[turn]}!")

#         #Show the board to the user
#         for row in board:
#             print(*row)

#         #Input a move from the player
#         row = int(input("Enter the row number (0-2) : "))
#         column = int(input("Enter the column number (0-2) : "))

#         # Do not allow players to play the same square
#         if board[row][column] != None:
#             print("Please play the move in an empty square!")
#             continue

#         if turn:
#             board[row][column] = 'X'
#             winner = check_win(board, 'X')
#         else:
#             board[row][column] = 'O'
#             winner = check_win(board, 'O')

#         # Increment the number of moves played
#         move_number += 1
#         # Update who's turn it is
#         turn = not turn
