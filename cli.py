from logic import Game, Human, Bot


if __name__ == "__main__":

    print("     Play against : ")
    print("     1. Human ")
    print("     2. Computer ")
    choice = int(input("     ---> Choice : "))
    if choice <= 1:
        game = Game(Human(), Human())
    else:
        game = Game(Human(), Bot())

    game.run()
