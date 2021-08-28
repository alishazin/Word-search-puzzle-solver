# Created By Ali Shazin
# Puzzle Solver

# return value :-
# [
#   [row, column, direction]
# ]

# direction(s):-
# "r" = right 
# "l" = left
# "b" = bottom
# "t" = top
# "br" = bottom right
# "bl" = bottom left
# "tr" = top right
# "tl" = top left

class PuzzleSolver:

    shortDetails = {
        'r': 'Right',
        'l': 'Left',
        'b': 'Bottom',
        't': 'Top',
        'br': 'Bottom Right',
        'bl': 'Bottom Left',
        'tr': 'Top Right',
        'tl': 'Top Left'
    }

    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.rowLimit = len(puzzle)
        self.colLimit = len(puzzle[0])

    def solvePuzzle(self, wordCheck):

        self.wordCheck = wordCheck

        colCount = 0
        rowCount = 0

        returnMessage = []

        for puzzleRow in self.puzzle:

            for rowElement in puzzleRow:

                if rowElement == self.wordCheck[0]:
                    rightCheck = self.checkRight(rowCount, colCount)
                    LeftCheck = self.checkLeft(rowCount, colCount)
                    bottomCheck = self.checkBottom(rowCount, colCount)
                    topCheck = self.checkTop(rowCount, colCount)
                    bottomRightCheck = self.checkBottomRight(rowCount, colCount)
                    bottomLeftCheck = self.checkBottomLeft(rowCount, colCount)
                    topRightCheck = self.checkTopRight(rowCount, colCount)
                    topLeftCheck = self.checkTopLeft(rowCount, colCount)

                    if rightCheck != None:
                        returnMessage.append(rightCheck)
                    if LeftCheck != None:
                        returnMessage.append(LeftCheck)
                    if bottomCheck != None:
                        returnMessage.append(bottomCheck)
                    if topCheck != None:
                        returnMessage.append(topCheck)
                    if bottomRightCheck != None:
                        returnMessage.append(bottomRightCheck)
                    if bottomLeftCheck != None:
                        returnMessage.append(bottomLeftCheck)
                    if topRightCheck != None:
                        returnMessage.append(topRightCheck)
                    if topLeftCheck != None:
                        returnMessage.append(topLeftCheck)

                if colCount < self.colLimit:
                    colCount += 1
                if colCount == self.colLimit:
                    colCount = 0
                    rowCount += 1

        return returnMessage

    def checkRight(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                wordResult += self.puzzle[rowCount][colCount]
                colCount += 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'r']
        else:
            return None

    def checkLeft(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                self.raiseErrorIfNegative(colCount)
                wordResult += self.puzzle[rowCount][colCount]
                colCount -= 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'l']
        else:
            return None

    def checkBottom(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                wordResult += self.puzzle[rowCount][colCount]
                rowCount += 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'b']
        else:
            return None
    
    def checkTop(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                self.raiseErrorIfNegative(rowCount)
                wordResult += self.puzzle[rowCount][colCount]
                rowCount -= 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 't']
        else:
            return None

    def checkBottomRight(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                wordResult += self.puzzle[rowCount][colCount]
                rowCount += 1
                colCount += 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'br']
        else:
            return None

    def checkBottomLeft(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                self.raiseErrorIfNegative(colCount)
                wordResult += self.puzzle[rowCount][colCount]
                rowCount += 1
                colCount -= 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'bl']
        else:
            return None

    def checkTopRight(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                self.raiseErrorIfNegative(rowCount)
                wordResult += self.puzzle[rowCount][colCount]
                rowCount -= 1
                colCount += 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'tr']
        else:
            return None

    def checkTopLeft(self, rowCount, colCount):
        startRowCount = rowCount
        startColCount = colCount
        wordResult = ''
        for i in range(len(self.wordCheck)):
            try:
                self.raiseErrorIfNegative(rowCount, colCount)
                wordResult += self.puzzle[rowCount][colCount]
                rowCount -= 1
                colCount -= 1
            except IndexError:
                wordResult = ''
                break
        if wordResult == self.wordCheck:
            return [startRowCount + 1, startColCount + 1, 'tl']
        else:
            return None

    def raiseErrorIfNegative(self, indexOne, indexTwo = 0):
        if indexOne < 0 or indexTwo < 0:
            raise IndexError