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

    return solve(0, 0)

if solveboard(examplegrid):
    for row in examplegrid:
        print(row)
else:
    print("No Solution")
   
print(examplegrid)
print("helele ")



    # def backtrack(grid):
    #     for row in range(9):
    #         for col in range(9):
    #             if grid[row][col] == "0":
    #                 for num in "123456789":
    #                     if isvalid(grid, row, col, num):
    #                         grid[row][col] = num

    #                         if backtrack(grid):
    #                             return True
    #                         grid[row][col] = "0"
    #                 return False
    #     return True
    
    # return backtrack(grid)