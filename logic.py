def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def get_winner(board):
    return None

def other_player(player):
    return 'O'

def check_win(board, win_char):
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