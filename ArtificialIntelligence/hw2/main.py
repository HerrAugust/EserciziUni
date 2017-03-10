#CHECKERS game Minmax implementation
#for this implementation MACHINE -> WHITE ('w'); HUMAN -> BLACK ('k')

__author__ = 'giodegas'

import GameModels as G
import Heuristics as H

def printMatrix(board):
    print "____________________________"
    for r in range(0,len(board)):
        row = ""
        for c in range(0,len(board[0])):
            row += board[r][c] + " "
        print row
        print "____________________________"

def game():
    board = [
        [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
        ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
        [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['k', ' ', 'k', ' ', 'k', ' ', 'k', ' '], # human frontier
        [' ', 'k', ' ', 'k', ' ', 'k', ' ', 'k'],
        ['k', ' ', 'k', ' ', 'k', ' ', 'k', ' ']
    ]

    LEVEL = 5
    heuristic = H.CheckerHeuristic()
    rep =  G.CheckerRepresentation(board)
    rep.setCurrentPlayer('w')
    curState = G.CheckerState(heuristic, rep)

    while True:
        turn = 'w' # machine
        states = curState.neighbors(turn)# find possible moves from here (1 level deeper)
        for j in states:
            b = j.getRepresentation().getBoard()
            printMatrix(b)
        mx = -9999
        ix = None # best state
        for s in states:
            h = heuristic.Hl(game, s, LEVEL, turn) # for each move, calculate heuristic value
            if h > mx: # find best heuristic value (MAX one) and remember the corresponding state
                mx = h
                ix = s
        print "Chosen MAX state:"
        print ix
        # generate a move in function of ix
        curState = ix
        curState.printMatrix()

        # check if final break WHITE wins!
        if curState.solution() == 'machine':
            print "You lose"
            return

        turn = 'k' #human
        curState.setCurrentPlayer(turn)
        movePossible = False
        while movePossible == False:
            r = input('Position of move start. row: ')
            c = input('Position of move start. column: ')
            re = input('Position of move end. row: ')
            ce = input('Position of move end. column: ')
            # is it feasible?
            movePossible = curState.isAdmissible(r,c,re,ce)


        curState = curState.makeMove(r,c, re,ce)
        # check if final break BLACK wins!
        if curState.solution() == 'human':
            print "You win"
            return

#Main
game()