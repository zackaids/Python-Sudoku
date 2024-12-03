import random

# solver
def solveboard(grid):
    n = 9

    def isvalid(row, col, num):
        # Check row and column
        for i in range(n):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        # Check subgrid
        subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve(row, col):
        if row == n:
            return True
        if col == n:
            return solve(row + 1, 0)
        if grid[row][col] == 0:
            for i in range(1, 10):
                if isvalid(row, col, i):
                    grid[row][col] = i
                    if solve(row, col + 1):
                        return True
                    grid[row][col] = 0
            return False
        return solve(row, col + 1)

    if solve(0, 0):
        return grid
    else:
        return "No Solution"

def readrandomdata(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

    data = random.choice(lines).strip()

    grid = [[int(data[i * 9 + j]) for j in range(9)] for i in range(9)]
    return grid

def getgrids(filepath):
    unsolvedgrid = readrandomdata(filepath)
    tempgrid = unsolvedgrid
    solvedgrid = solveboard(tempgrid)
    return unsolvedgrid, solvedgrid


# filepath = "sudoku_boards_unsolved.txt"

# unsolvedgrid = readrandomdata(filepath)
# print("Unsolved Sudoku Grid:")
# displaygrid(unsolvedgrid)

# start_time = time.time()
# solvedgrid = solveboard([row[:] for row in unsolvedgrid])
# end_time = time.time()
# elapsed_time = end_time - start_time

# print("Solved Sudoku Grid:")
# displaygrid(solvedgrid)
# print("It took", elapsed_time, "seconds to solve this board")