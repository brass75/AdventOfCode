from functools import cache

from aoc_lib import solve_problem

MULT = 252533
DIV = 33554393
START = 20151125


def solve(col: int, row: int) -> int:
    n = START
    row_start = 2
    calc = cache(lambda x: (x * MULT) % DIV)
    while True:
        i = row_start
        for j in range(1, row_start + 1):
            n = calc(n)
            if j == col and i == row:
                return n
            i -= 1
        row_start += 1


if __name__ == '__main__':
    part1_args = [3_029, 2_947]
    expected_1 = [(10600672, [5, 4])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = []  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, *part2_args)
