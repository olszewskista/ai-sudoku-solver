import pyswarms as ps
import numpy as np
from utils import (
    get_missing_values,
    combine,
    col_numof_missing_and_repeated,
    row_numof_missing_and_repeated,
    square_numof_missing_and_repeated,
)
from load_sudoku import load_sudoku
from pyswarms.utils.plotters import plot_cost_history
from pretty_print import pretty_print_sudoku, pretty_print_solution
import matplotlib.pyplot as plt

sudoku, _ = load_sudoku("./sudoku.csv")
pretty_print_sudoku(sudoku)


def optimize_fn(solutions):
    result = []
    for solution in solutions:
        combined = combine(sudoku, [int(x * 10) for x in solution])
        score = 0
        for i in range(len(combined)):
            score += 9 - (col_numof_missing_and_repeated(combined, i)[0])
        for i in range(len(combined)):
            score += 9 - (row_numof_missing_and_repeated(combined, i)[0])
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                score += 9 - (square_numof_missing_and_repeated(combined, x, y)[0])
        result.append(-score)
    return result


# options = {"c1": 0.5, "c2": 0.3, "w": 0.9}
options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 3, 'p': 2}
x_min = np.full(get_missing_values(sudoku), 0.1)
x_max = np.full(get_missing_values(sudoku), 0.9)
# print(get_missing_values(sudoku))
# print(x_min)
# print(x_max)
my_bounds = (x_min, x_max)

optimizer = ps.single.LocalBestPSO(
    n_particles=100, dimensions=get_missing_values(sudoku), options=options, bounds=my_bounds,
)



res = optimizer.optimize(optimize_fn, iters=5000)


pretty_print_solution([int(x * 10) for x in res[1]], sudoku)


plot_cost_history(optimizer.cost_history)

plt.show()
