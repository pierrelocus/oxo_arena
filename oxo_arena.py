# -*- coding: utf-8 -*-

import player1
import player2

from time import sleep

def has_winner(game):
    for index, line in enumerate(game):
        char = line[0]
        # Check horizontal lines
        if char != '.' and all([x==char for x in line]):
            return True
        char_heights = [game[i][index] for i in range(3)]
        # Check vertical lines
        if char != '.' and all([x==char for x in char_heights]):
            return True
    # Check diagonals
    char = game[0][0]
    if char != '.' and all([x == char for x in [game[j][j] for j in range(3)]]):
        return True
    char = game[0][2]
    if char != '.' and all([x == char for x in [game[j][2-j] for j in range(3)]]):
        return True
    return False

if __name__ == '__main__':
    run = True
    game = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    while run:
        for line in game:
            print(line)
        print("")
        print("")
        game = player1.turn(game, 'O')
        game = player2.turn(game, 'X')
        if has_winner(game):
            run = False
        if run:
            run = False
            for line in game:
                for cell in line:
                    if cell == '.':
                        run = True
        sleep(1)

