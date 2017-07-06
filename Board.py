from Piece import *

class Board:

    def __init__(self, boardLayout):
        self.boardLayout = boardLayout.split("\n")
        for x in range(0, len(self.boardLayout)):
            self.boardLayout[x] = list(self.boardLayout[x])

    def printBoard(self):
        for line in self.boardLayout: print "".join(line)

    def addPiece(self, piece):
        for y in range(0, len(self.boardLayout)):
            for x in range(0, len(self.boardLayout[y])):
                if self.boardLayout[y][x] == '#':
                    if self.insertPiece(piece, y, x):
                        return True
                    else:
                        return False



    def insertPiece(self, piece, y, x):
        if y+len(piece) > len(self.boardLayout):
            return False

        for a in range(0, len(self.boardLayout)):
            if piece[0][a] != ' ':
                n=a
                break
        
        for a in range(0, len(piece)):
            for b in range(0, len(piece[a])):
                if piece[a][b] != ' ':
                    if x-n+b > len(self.boardLayout[a+y]) or x-n+b < 0 or self.boardLayout[a+y][x-n+b] != '#':
                        #We failed the mission: piece cant be inserted here
                        self.deletePiece(piece)
                        return False
                    else:
                        #Continue inserting the piece.
                        self.boardLayout[a+y][x-n+b] = piece[a][b]
        
        return True

    def deletePiece(self, piece):
        for i in piece[0]:
            if i != ' ':
                symbol = i
                break
        for y in range(0, len(self.boardLayout)):
            for x in range(0, len(self.boardLayout[y])):
                if self.boardLayout[y][x] == symbol:
                    self.boardLayout[y][x] =  '#'