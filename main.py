examplegrid = [
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [7, 8, 0, 4, 0, 0, 0, 2, 0],
    [0, 0, 2, 6, 0, 1, 0, 7, 8],
    [6, 1, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 7, 5, 4, 0, 0, 6, 1],
    [0, 0, 1, 7, 5, 0, 9, 3, 0],
    [0, 7, 0, 3, 0, 0, 0, 1, 0],
    [0, 4, 0, 2, 0, 6, 0, 0, 7],
    [0, 2, 0, 0, 0, 7, 4, 0, 0],
]

won_grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

def main(grid):
    state = checkgame(grid)
    original_set = checkgrid(grid)
    while state == False:
        changecell(grid, original_set)
    print("congrats, you won")

# function for win con
def checkgame(grid):
    def isvalid(group):
        return sorted(group) == list(range(1, 10))

    for row in grid:
        if not isvalid(row):
            return False
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not isvalid(column):
            return False
    for boxrow in range(0, 9, 3):
        for boxcol in range(0, 9, 3):
            subgrid = [
                grid[row][col]
                for row in range(boxrow, boxrow + 3)
                for col in range(boxcol, boxcol + 3)
            ]
            if not isvalid(subgrid):
                return False
    return True

# function to check if valid
def checkgrid(grid):
    myset = set()
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell != 0:
                myset.add((i, j))
    return myset

# function to show the board
def displayboard(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
        

# function to interact with the board
def choosecell():
    print("Enter the row: ")
    row = int(input()) - 1
    print("Enter the column: ")
    col = int(input()) - 1
    return row, col

def changecell(grid, myset):

    displayboard(grid)
    row, col = choosecell()

    if (row, col) in myset:
        print("This cell is part of the og, choose another one")
        changecell(myset)
    else:
        print("please input")
        choice = int(input())
        grid[row][col] = choice
        print("success")

    return grid
    
main(examplegrid)