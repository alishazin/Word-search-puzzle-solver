from source import PuzzleSolver

totalRow = int(input('Enter the Number of Row(s) : '))
totalCol = int(input('Enter the Number of Column(s) : '))

puzzle = []
for rowCount in range(totalRow):
    row = []
    for colCount in range(totalCol):
        element = input(f'Enter the element in row {rowCount + 1} and column {colCount + 1} : ')
        row.append(element)
    puzzle.append(row)

print(f'Puzzle: {puzzle}')

obj = PuzzleSolver(puzzle)

while True:
    wordToSearch = input("Enter the WORD to search For (Enter Nothing to Cancel) : ")
    if wordToSearch == '':
        break
    else:
        for rowOut, colOut, directionDetails in (obj.solvePuzzle(wordToSearch)):
            print(f'Row {rowOut}, Column {colOut}, Towards {obj.shortDetails[directionDetails]}')

print("Search Ended...")