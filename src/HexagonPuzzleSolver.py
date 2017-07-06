#!/usr/bin/python

from Piece import *
from Board import *
from Solver import *
import sys

### Parameter parsing ###
verbose = False
findAll = False
boardUrl = "board.txt"
piecesUrl = "pieces.txt"
for n in range(1, len(sys.argv)):
    if sys.argv[n] == "--verbose" or sys.argv[n] == "-v": verbose = True
    elif sys.argv[n] == "--findAll" or sys.argv[n] == "-a": findAll = True
    else:
        print "Unknown argument:", sys.argv[n]
        sys.exit()

### File reading ###
# Board reading #
boardf = open(boardUrl, 'r')
boardString = ''
for line in boardf:
    boardString += line
board = Board(boardString)
pieces = []

# Pieces reading #
piecesf = open(piecesUrl, 'r')
pieceString = ''
for line in piecesf:
    if line.isspace():
        if not (pieceString.isspace()):
            pieceString = pieceString[:-1]  #Last newline is useless
            pieces.append(Piece(pieceString))
        pieceString = ''
    else:
        pieceString += line

### The Magic ###
result = Solver(pieces, board, verbose, findAll).solve()
print "Execution complete, found", result, "results."