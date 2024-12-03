examplegrid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

examplegrid1 = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 0],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
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
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

def main(grid):
    state = checkgame(grid)
    original_set = checkgrid(grid)
    while state == False:
        changecell(grid, original_set)
        state = checkgame(grid)
    print("Congratulations, you have won!")

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
    return {(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell != 0}

# function to show the board
def displayboard(grid):
    print("    1 2 3   4 5 6   7 8 9 ")
    print("  +-------+-------+-------+")
    for i, row in enumerate(grid):
        row_display = f"{i+1} | "
        for j, cell in enumerate(row):
            if j > 0 and j % 3 == 0:
                row_display += "| "
            row_display += f"{cell if cell != 0 else '.'} "
        row_display += "|"
        print(row_display)
        if i > 0 and (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")
    print("")

# function to interact with the board
def choosecell():
    while True:
        try:
            row = int(input("Enter the row (1-9): ")) - 1
            if not (0 <= row < 9):
                raise ValueError
            col = int(input("Enter the column (1-9): ")) - 1
            if not (0 <= col < 9):
                raise ValueError
            return row, col
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# function to change a cell
def changecell(grid, myset):
    displayboard(grid)
    while True:
        row, col = choosecell()
        if (row, col) in myset:
            print("This cell is part of the original puzzle, choose another one")
        else:
            break

    while True:
        try:
            choice = int(input("Please input a number (1-9): "))
            if not (1 <= choice <= 9):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 9.")
    
    grid[row][col] = choice
    print("Success")

    return grid

main(examplegrid1)