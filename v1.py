import pygad
import time
from colorama import Fore

print(Fore.CYAN + "dfdf" + Fore.RESET)

x = f"{Fore.CYAN} sdfsdfsd {Fore.RESET} dsfsdfdsf"

print(x)

sudoku = [
    [5, 0, 0, 0, 0, 0, 9, 3, 0],
    [1, 0, 0, 0, 2, 0, 0, 7, 0],
    [0, 7, 9, 0, 3, 1, 6, 8, 2],
    [6, 8, 5, 1, 0, 0, 7, 2, 0],
    [0, 0, 0, 9, 0, 7, 0, 0, 0],
    [0, 9, 3, 0, 0, 2, 1, 4, 6],
    [9, 2, 1, 3, 7, 0, 4, 6, 0],
    [0, 5, 0, 0, 9, 0, 0, 0, 3],
    [0, 4, 6, 0, 0, 0, 0, 0, 7]
]


gene_space = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pretty_print_solution(solution, draw = True):
    combined = combine(sudoku, solution)
    result = ''
    for i in range(len(combined)):
        new_row = '|'
        for j in range(len(combined[0])):
            _, row_repeats = row_len_uniq(combined, i)
            _, col_repeats = col_len_uniq(combined, j)
            _, square_repeats = square_len_uniq(combined, i % 3, j % 3)
            num = combined[i][j]
            if num in row_repeats or num in col_repeats or num in square_repeats:
                new_row += f'{Fore.RED}{str(combined[i][j])}{Fore.RESET}'
            else:
                new_row += f'{Fore.GREEN}{str(combined[i][j])}{Fore.RESET}'

            # if str(combined[i][j]) in new_row:
            # new_row += str(combined[i][j])
            if ((j+1) % 3) == 0:
                new_row += '|'
        if i % 3 == 0: result += '-' * len(new_row) + '\n'

        result += new_row + '\n'
    result += '-' * len(new_row) + '\n'
    print(result)


def combine(sudoku, solution):
    solution = list(solution)
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

def col_len_uniq(sudoku, num):
    seen = []
    repeated = []
    for i in range(len(sudoku)):
        seen.append(sudoku[i][num])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    return 9 - len(set(seen)), repeated


def row_len_uniq(sudoku, num):
    seen = []
    repeated = []
    for i in range(len(sudoku)):
        seen.append(sudoku[num][i])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    return 9 - len(set(seen)), repeated

def square_len_uniq(sudoku, x_start, y_start):
    seen = []
    repeated = []
    for x_cord in range(x_start, x_start+3):
        for y_cord in range(y_start, y_start+3):
            seen.append(sudoku[y_cord][x_cord])
    for x in seen:
        if seen.count(x) > 1: repeated.append(x)
    return 9 - len(set(seen)), repeated


def get_missing_values(sudoku):
    c = 0
    for a in sudoku:
        for b in a:
            if b == 0: c += 1
    return c


def fitness_func(ga_instance, solution, solution_idx):
    pass
    combined = combine(sudoku, solution)
    # print(square_len_uniq(combined, 3, 0))
    score = 0
    for i in range(len(sudoku)):
        score += 9 - (col_len_uniq(combined, i)[0] * 2)
    for i in range(len(sudoku)):
        score += 9 - (row_len_uniq(combined, i)[0] * 2)
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            score += 9 - (square_len_uniq(combined, x, y)[0] * 2)
    return score
    



fitness_func(2, [1 for x in range(41)], 2)

pretty_print_solution(['x' for x in range(41)])

# exit()

fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 50
num_genes = get_missing_values(sudoku)

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 25
num_generations = 1000
keep_parents = 5

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"


# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    # stop_criteria="saturate_300",
    # suppress_warnings=True,
)


# uruchomienie algorytmu
ga_instance.run()

ga_instance.plot_fitness()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print(
    "Fitness value of the best solution = {solution_fitness}".format(
        solution_fitness=solution_fitness
    )
)

print(solution)
pretty_print_solution([int(x) for x in solution])


# pretty_print_solution([0,0,2,0,0,3,0,0,2,2,0,0,0,2,2,1,2,2,0,2,2,2])

# fitness_func("", [0,0,2,0,0,3,0,0,2,2,0,0,0,2,2,1,2,2,0,2,2,2], "")

accuracy = 0

time_sum = 0


# for _ in range(10):
#     ga_instance = pygad.GA(
#         gene_space=gene_space,
#         num_generations=num_generations,
#         num_parents_mating=num_parents_mating,
#         fitness_func=fitness_function,
#         sol_per_pop=sol_per_pop,
#         num_genes=num_genes,
#         parent_selection_type=parent_selection_type,
#         keep_parents=keep_parents,
#         crossover_type=crossover_type,
#         mutation_type=mutation_type,
#         mutation_percent_genes=mutation_percent_genes,
#         # stop_criteria="saturate_300",
#         # suppress_warnings=True,
#     )
    
#     start = time.time()

#     ga_instance.run()

#     end = time.time()

#     solution, _, _ = ga_instance.best_solution()

#     time_sum += end - start
#     if pretty_print_solution(solution): accuracy += 1

# print("Accuracy:", accuracy/10 * 100, "%")
# print("Average time:", round(time_sum/10, 2), "s")