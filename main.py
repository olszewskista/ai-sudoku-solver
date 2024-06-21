from load_sudoku import load_sudoku, get_user_sudoku
from ga import solve_ga
from pso import solve_pso
from pretty_print import pretty_print_solution, pretty_print_sudoku
from utils import get_missing_values
import time

sud_choice = int(input("1 - Sample sudoku\n2 - User's sudoku\n"))

if sud_choice == 1:
    sudoku, _ = load_sudoku('./half_mil_sudoku.csv')
    print(f"Sample sudoku loaded with {get_missing_values(sudoku)} missing values")
elif sud_choice == 2:
    sudoku = get_user_sudoku()
    print(f"User's sudoku loaded with {get_missing_values(sudoku)} missing values")
else:
    print("Wrong option")
    exit()

pretty_print_sudoku(sudoku)
tries = int(input("Enter number of tries:\n"))
choice = int(input("1 - GA (very good)\n2 - PSO (very bad)\n"))
plot = True if input("Draw plot? y/n\n") == 'y' else False

time_sum = 0
tries_passed = 0

if choice == 1:
    print("Solving sudoku using genetic algorithm...")
    for tr in range(1,tries+1):
        print(f"Starting try {tr}...")
        start = time.time()
        result, is_solved = solve_ga(sudoku, plot)
        diff = time.time() - start
        time_sum += diff
        tries_passed += 1
        solution, _, _ = result.best_solution()
        pretty_print_solution(solution, sudoku)
        if is_solved: print("Solved sudoku " + u'\u2191' + f" in {tr} tr{"ies" if tr > 1 else "y"}")
        else: print("Solving sudoku failed")
        if plot: result.plot_fitness()
        if is_solved: 
            break
elif choice == 2:
    print("Solving sudoku using particle swarm optimization...")
    for tr in range(1,tries+1):
        print(f"Starting try {tr}...")
        before = time.time()
        solve_pso(sudoku, plot)
        diff = time.time()  - before
        time_sum += diff
        tries_passed += 1
        print("Solving sudoku failed")
else:
    print("Wrong option")

print(f"Average execution time: {time_sum/tries_passed:.2f} seconds.")