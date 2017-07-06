from Piece import *
from Board import *

class Solver:

    def __init__(self, pieceArray, board, verbose, findAll):
        self.pieceArray = pieceArray
        self.board = board
        self.verbose = verbose
        self.findAll = findAll

    def solve(self):
        return self.__recursive__(0)

    def __recursive__(self, result):
        if self.verbose: self.board.printBoard()
        if(len(self.pieceArray) == 0):
            self.board.printBoard()
            print ""
            return result+1
        for n in range(len(self.pieceArray)):
            for i in range(12):
                if i == 6: self.pieceArray[n].mirror()
                self.pieceArray[n].rotate()
                if self.board.addPiece(self.pieceArray[n].pieceLayout):
                    temp = self.pieceArray[:]
                    del temp[n]
                    result = Solver(temp, self.board, self.verbose, self.findAll).__recursive__(result)
                    if not self.findAll and result > 0: return result
                    self.board.deletePiece(self.pieceArray[n].pieceLayout)
        return result