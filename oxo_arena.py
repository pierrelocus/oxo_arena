# -*- coding: utf-8 -*-

import player1
import player2

from time import sleep

def flatten(game):
    m = []
    for row in game:
        for cell in row:
            m.append(cell)
    return m

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
        if not any([cell == '.' for cell in flatten(game)]):
            for line in game:
                print(line)
            break
        game = player2.turn(game, 'X')
        run = any([cell == '.' for cell in flatten(game)])
        if has_winner(game):
            run = False
            for line in game:
                print(line)

