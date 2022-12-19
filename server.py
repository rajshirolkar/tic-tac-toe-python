from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session
from flask_cors import CORS
from tempfile import mkdtemp
import random


app = Flask(__name__)
CORS(app)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app = Flask(__name__)
app.secret_key = "super secret key"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/game")
def game():
    print('in')
    if not "board" in session:
        session["board"] = [[None, None, None],
                            [None, None, None],
                            [None, None, None]]
        session["turn"] = "Player X"
        session["char"] = "X"
    ans = check_win(session["board"], session["char"])
    if (ans[0] == True):
        return render_template("finish.html", ans="{} Player is Won!".format(ans[1]))
    elif (ans[0] == False and ans[1] == "Draw"):
        return render_template("finish.html", ans="Its a Draw!")
    else:
        return render_template("game.html", game=session["board"], turn=session["turn"])


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["char"]
    if session["turn"] == "Player X":
        session["char"] = "O"
        session["turn"] = "Player O"
    else:
        session["char"] = "X"
        session["turn"] = "Player X"
    return redirect(url_for("game"))


@app.route("/clear")
def clear():
    session["board"] = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
    session["turn"] = "Player X"
    session["char"] = "X"
    return redirect(url_for("game"))


# [x,y] for x iff game is finished with winner and y = "Draw" if the game is draw, else, the winner (["Player X","Y"])
def check_win(board, win_char):
    print('inside checkwin')
    if board[0][0] == board[0][1] == board[0][2] == win_char:
        return [True, win_char]
    elif board[1][0] == board[1][1] == board[1][2] == win_char:
        return [True, win_char]
    elif board[2][0] == board[2][1] == board[2][2] == win_char:
        return [True, win_char]
    elif board[0][0] == board[1][0] == board[2][0] == win_char:
        return [True, win_char]
    elif board[0][1] == board[1][1] == board[2][1] == win_char:
        return [True, win_char]
    elif board[0][2] == board[1][2] == board[2][2] == win_char:
        return [True, win_char]
    elif board[1][1] == board[2][2] == board[0][0] == win_char:
        return [True, win_char]
    elif board[0][2] == board[1][1] == board[2][0] == win_char:
        return [True, win_char]
    else:
        for i in range(3):
            for j in range(3):
                if (board[i][j] == None):
                    # Its Return somthing, never mind[1].
                    return [False, win_char]

    # Its Draw!
    return [False, "Draw"]


def bot_move(board, char):
    row = random.randint(0, 2)
    column = random.randint(0, 2)
    if board[row][column] != None:
        bot_move(board, char)
    else:
        board[row][column] = char
        print(board)
    return (row, column)


@app.route("/help")
def help():
    # ans = minimax(session["board"], session["turn"])
    row, column = bot_move(session["board"], session["char"])
    return redirect(url_for('play', row=row, col=column))
    # if ans[1] is not None:
    #     return redirect(url_for('play', row=ans[1][0], col=ans[1][1]))


def minimax(board, turn):
    ans = CheckWinner(board)
    if (ans[0] == True and ans[1] == "Player X"):
        return (1, None)
    elif (ans[0] == True and ans[1] == "Player O"):
        return (-1, None)
    elif (ans[0] == False and ans[1] == "Draw"):
        return (0, None)
    else:  # Next Step of Recursion
        moves = []
        for i in range(3):
            for j in range(3):
                if (board[i][j] == None):
                    moves.append((i, j))
        # All Moves that avaliabe are now at moves
        if turn == "Player X":
            value = -2
            for i, j in moves:
                board[i][j] = "Player X"
                result = minimax(board, "Player O")[0]
                if (value < result):
                    value = result
                    step = (i, j)
                board[i][j] = None
        elif turn == "Player O":  # turn is "Player O"
            value = 2
            for i, j in moves:
                board[i][j] = "Player O"
                result = minimax(board, "Player X")[0]
                if (value > result):
                    value = result
                    step = (i, j)
                board[i][j] = None
        return (value, step)


if __name__ == '__main__':
    app.debug = True
    app.run()
