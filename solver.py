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


solution = solveboard(examplegrid)
if solution != "No Solution":
    for row in solution:
        print(row)
else:
    print(solution)

print(solution)