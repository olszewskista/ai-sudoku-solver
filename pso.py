import pyswarms as ps
import numpy as np
from utils import (
    get_missing_values,
    combine,
    col_numof_missing_and_repeated,
    row_numof_missing_and_repeated,
    square_numof_missing_and_repeated,
)
from pyswarms.utils.plotters import plot_cost_history
from pretty_print import pretty_print_solution
import matplotlib.pyplot as plt



def solve_pso(sudoku, plot = False):
    def optimize_fn(solutions):
        result = []
        for solution in solutions:
            combined = combine(sudoku, [round(x) for x in solution])
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


    options = {"c1": 0.5, "c2": 0.3, "w": 0.9}
    # options = {"c1": 0.3, "c2": 0.5, "w": 0.8}
    # options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 3, 'p': 2}
    x_min = np.full(get_missing_values(sudoku), 0.51)
    x_max = np.full(get_missing_values(sudoku), 9.49)
    my_bounds = (x_min, x_max)
    optimizer = ps.single.GlobalBestPSO(
        n_particles=100, dimensions=get_missing_values(sudoku), options=options, bounds=my_bounds,
    )

    res = optimizer.optimize(optimize_fn, iters=1000)
    print(res[0])

    pretty_print_solution([round(x) for x in res[1]], sudoku)

    if plot: 
        plot_cost_history(optimizer.cost_history)
        plt.show()
