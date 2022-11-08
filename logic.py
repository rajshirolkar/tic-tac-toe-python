def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]

def check_win(board, win_char):
    """ Checks if the board is winning for the character passed
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