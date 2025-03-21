def solve_sudoku(board, depth=0):
    def find_empty(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # row, col
        return None  # No empty cells, puzzle solved

    def is_valid(board, num, pos):
        # Check row
        for i in range(9):
            if board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(9):
            if board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        return True

    empty = find_empty(board)
    if not empty:
        print(f"{'  ' * depth}Solution found!")
        return True  # Puzzle solved
    else:
        row, col = empty
        print(f"{'  ' * depth}Trying cell ({row}, {col})")

        for num in range(1, 10):
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                print(f"{'  ' * depth}  Placed {num} at ({row}, {col})")
                if solve_sudoku(board, depth + 1):  # Recursive call
                    return True
                board[row][col] = 0  # Backtrack
                print(f"{'  ' * depth}  Backtracking from ({row}, {col})")
        print(f"{'  ' * depth}No valid number for ({row}, {col})")
        return False  # Trigger backtracking

# Fully solvable Sudoku puzzle
sudoku_grid = [
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [9, 6, 5, 3, 2, 7, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 4, 6, 8, 2, 7, 1],
    [4, 7, 2, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 5],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 9, 6, 8, 2, 3],
    [2, 3, 9, 8, 4, 1, 5, 6, 7]
]

# Remove some numbers to make it a proper puzzle
sudoku_grid[0][1] = 0
sudoku_grid[1][3] = 0
sudoku_grid[2][5] = 0
sudoku_grid[3][6] = 0
sudoku_grid[4][4] = 0
sudoku_grid[5][7] = 0
sudoku_grid[6][2] = 0
sudoku_grid[7][8] = 0
sudoku_grid[8][0] = 0

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku:")
    for row in sudoku_grid:
        print(row)
else:
    print("No solution exists.")