from utils import (
    col_numof_missing_and_repeated,
    combine,
    row_numof_missing_and_repeated,
    square_numof_missing_and_repeated,
    trim_number,
)
from colorama import Fore

def pretty_print_solution(solution, sudoku):
    combined = combine(sudoku, solution)
    result = "\u250c" + ("\u2500" * 7 + "\u252C") * 2 + "\u2500" * 7 + "\u2510" + "\n"
    for i in range(len(combined)):
        new_row = "\u2502 "
        for j in range(len(combined[0])):
            _, row_repeats = row_numof_missing_and_repeated(combined, i)
            _, col_repeats = col_numof_missing_and_repeated(combined, j)
            _, square_repeats = square_numof_missing_and_repeated(
                combined, trim_number(i, 3), trim_number(i, 3)
            )
            num = combined[i][j]
            if num in row_repeats or num in col_repeats or num in square_repeats:
                new_row += f"{Fore.RED}{str(combined[i][j])} {Fore.RESET}"
            else:
                new_row += f"{Fore.GREEN}{str(combined[i][j])} {Fore.RESET}"

            if ((j + 1) % 3) == 0:
                new_row += "\u2502 "
        if i % 3 == 0 and i != 0:
            result += (
                "\u251C"
                + ("\u2500" * 7 + "\u253C") * 2
                + "\u2500" * 7
                + "\u2524"
                + "\n"
            )

        result += new_row + "\n"
    result += "\u2514" + ("\u2500" * 7 + "\u2534") * 2 + "\u2500" * 7 + "\u2518"
    print(result)


def pretty_print_sudoku(sudoku):
    combined = sudoku
    result = "\u250c" + ("\u2500" * 7 + "\u252C") * 2 + "\u2500" * 7 + "\u2510" + "\n"
    for i in range(len(combined)):
        new_row = "\u2502 "
        for j in range(len(combined[0])):
            _, row_repeats = row_numof_missing_and_repeated(combined, i)
            _, col_repeats = col_numof_missing_and_repeated(combined, j)
            _, square_repeats = square_numof_missing_and_repeated(
                combined, trim_number(i, 3), trim_number(i, 3)
            )
            num = combined[i][j]
            if num in row_repeats or num in col_repeats or num in square_repeats:
                new_row += f"{Fore.RED}{str(combined[i][j])} {Fore.RESET}"
            else:
                new_row += f"{Fore.GREEN}{str(combined[i][j])} {Fore.RESET}"

            if ((j + 1) % 3) == 0:
                new_row += "\u2502 "
        if i % 3 == 0 and i != 0:
            result += (
                "\u251C"
                + ("\u2500" * 7 + "\u253C") * 2
                + "\u2500" * 7
                + "\u2524"
                + "\n"
            )

        result += new_row + "\n"
    result += "\u2514" + ("\u2500" * 7 + "\u2534") * 2 + "\u2500" * 7 + "\u2518"
    print(result)
