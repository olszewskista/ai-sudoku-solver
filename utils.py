def get_missing_values(sudoku):
    c = 0
    for a in sudoku:
        for b in a:
            if b == 0:
                c += 1
    return c

def trim_number(a, b):
    result = 0
    while result + b <= a:
        result += b
    return result

def combine(sudoku, solution):
    solution = [int(x) for x in solution]
    # print(solution)
    combined = []
    for row in sudoku:
        new_row = []
        for cell in row:
            if cell == 0:
                new_row.append(solution.pop(0))
            else:
                new_row.append(cell)
        combined.append(new_row)
    return combined

def col_numof_missing_and_repeated(sudoku, num):
    seen = []
    repeated = []
    for i in range(len(sudoku)):
        seen.append(sudoku[i][num])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    return 9 - len(set(seen)), repeated


def row_numof_missing_and_repeated(sudoku, num):
    seen = []
    repeated = []
    for i in range(len(sudoku)):
        seen.append(sudoku[num][i])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    return 9 - len(set(seen)), repeated

def square_numof_missing_and_repeated(sudoku, x_start, y_start):
    # print(x_start, y_start)
    seen = []
    repeated = []
    for x_cord in range(x_start, x_start+3):
        for y_cord in range(y_start, y_start+3):
            seen.append(sudoku[y_cord][x_cord])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    # print(x_start, y_start, seen)
    return 9 - len(set(seen)), repeated