from random import randint
def turn(game, symbol):
    # My symbol is symbol, the enemy is the opposite (so if I'm "X" he's "O")
    # I check in the matrix if he could win and block him
    # Else I try to get my symbol on the same line to win
    while 1:
        x = randint(0,2)
        y = randint(0,2)
        if game[x][y] == '.':
            game[x][y] = symbol
            return game
