class Piece:

    pieceCount = 0

    def __init__(self, pieceLayout):
        self.pieceLayout = pieceLayout.split("\n")
        Piece.pieceCount += 1
        self.__deleteUselessSpaces__()

    def printPiece(self):
        for line in self.pieceLayout: print line

    def rotate(self):
        longestLine = 0
        for line in self.pieceLayout:
            if(longestLine < len(line)):
                longestLine = len(line)

        oldPieceLayout = self.pieceLayout
        self.pieceLayout = []

        for x in reversed(range(0, len(oldPieceLayout))):
            if not oldPieceLayout[x][0] == ' ':
                if (len(oldPieceLayout)-x)%2 == 0: skipLine=True
                else: skipLine=False
                break

        for x in reversed(range(-longestLine+1, len(oldPieceLayout))):
            if not skipLine:
                temp = ""
                z = x
                for y in range(0, len(oldPieceLayout)+(-1*x)):
                    if z>=0 and z<len(oldPieceLayout) and y<len(oldPieceLayout[z]):
                        temp += oldPieceLayout[z][y] +  " "
                    else: temp += "  "
                    z+=1

                self.pieceLayout.insert(0, temp)
                self.__addUselessSpaces__(3)
                skipLine = True
            else:
                skipLine = False
        self.__deleteUselessSpaces__()

    def mirror(self):
        oldPieceLayout = self.pieceLayout
        self.pieceLayout = []
        for x in range(0, len(oldPieceLayout)):
            self.pieceLayout.insert(0, oldPieceLayout[x])

    def __deleteUselessSpaces__(self):
        while self.pieceLayout[0].isspace(): self.pieceLayout.pop(0)
        while self.pieceLayout[-1].isspace(): self.pieceLayout.pop(-1)
        while True:
            for line in self.pieceLayout:
                if not (line[0] == ' '): return                
            temp = []
            for line in self.pieceLayout:
                temp.append(line[1:])
            self.pieceLayout = temp

    def __addUselessSpaces__(self, amount):
        for x in range(0, amount):
            temp = []
            for line in self.pieceLayout:
                temp.append(' ' + line)
            self.pieceLayout = temp