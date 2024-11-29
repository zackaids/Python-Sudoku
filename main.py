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

def main(grid):
    state = checkgame(grid)
    original_set = checkgrid(grid)
    while state == False:
        changecell(grid, original_set)

# function for win con
def checkgame(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
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