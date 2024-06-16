import pygad
from load_sudoku import load_sudoku
from pretty_print import pretty_print_solution, pretty_print_sudoku
from utils import (
    col_numof_missing_and_repeated,
    square_numof_missing_and_repeated,
    row_numof_missing_and_repeated,
    get_missing_values,
    combine,
)

sudoku, sudoku_solution = load_sudoku("./sudoku.csv")
pretty_print_sudoku(sudoku)
print("Missing values:", get_missing_values(sudoku))

# ile chromsomów w populacji
sol_per_pop = 100

# ile genow ma chromosom
num_genes = get_missing_values(sudoku)

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
num_parents_mating = 10

# ile pokolen
num_generations = 1000

# ilu rodzicow zachowac (kilka procent)
keep_parents = 2

# jaki typ selekcji rodzicow?
# sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "two_points"

# typ mutacji
mutation_type = "random"
# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_percent_genes = 1

# possible genes
gene_space = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fitness_func(ga_instance, solution, solution_idx):
    combined = combine(sudoku, solution)
    score = 0
    for i in range(len(sudoku)):
        score += 9 - (col_numof_missing_and_repeated(combined, i)[0])
    for i in range(len(sudoku)):
        score += 9 - (row_numof_missing_and_repeated(combined, i)[0])
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            score += 9 - (square_numof_missing_and_repeated(combined, x, y)[0])

    return score

fitness_function = fitness_func

for _ in range(10):
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
        # stop_criteria="reach_243",
        suppress_warnings=True,
    )

    ga_instance.run()
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print(solution_fitness)
    pretty_print_solution([int(x) for x in solution], sudoku)
    if solution_fitness == 243:
        break

ga_instance.plot_fitness()

# podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
# solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print(
    "Fitness value of the best solution = {solution_fitness}".format(
        solution_fitness=solution_fitness
    )
)