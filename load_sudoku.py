import pandas as pd

# sudoku = [
#     [5, 0, 0, 0, 0, 0, 9, 3, 0],
#     [1, 0, 0, 0, 2, 0, 0, 7, 0],
#     [0, 7, 9, 0, 3, 1, 6, 8, 2],
#     [6, 8, 5, 1, 0, 0, 7, 2, 0],
#     [0, 0, 0, 9, 0, 7, 0, 0, 0],
#     [0, 9, 3, 0, 0, 2, 1, 4, 6],
#     [9, 2, 1, 3, 7, 0, 4, 6, 0],
#     [0, 5, 0, 0, 9, 0, 0, 0, 3],
#     [0, 4, 6, 0, 0, 0, 0, 0, 7],
# ]

def load_sudoku(file):

    sudoku_sample = pd.read_csv(file).sample().values[0]

    sudoku_string, solution_string = sudoku_sample[0], sudoku_sample[1]

    sudoku = []
    sudoku_solution = []
    row = []
    row_solution = []

    for num1, num2 in zip(sudoku_string, solution_string):
        if len(row) == 9:
            sudoku.append(row)
            sudoku_solution.append(row_solution)
            row = [int(num1)]
            row_solution = [int(num2)]
        else:
            row.append(int(num1))
            row_solution.append(int(num2))
    sudoku.append(row)
    sudoku_solution.append(row_solution)


    return sudoku, sudoku_solution
