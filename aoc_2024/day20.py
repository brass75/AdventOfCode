from functools import partial
from multiprocessing import Pool

from aoc_lib import GridBase, solve_problem

INPUT = open('data/day20.txt').read()

TEST_INPUT = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def cheats(path: dict, radius: int, min_savings, point_steps) -> int:
    # Found is a dict to avoid duplications
    found = dict()
    point, steps = point_steps
    x, y = point
    for i in range(-1 * radius, radius + 1):
        for j in range(-1 * radius, radius + 1):
            if abs(i) + abs(j) <= radius:
                check = (x + i, y + j)
                if check in path and (
                    steps > (new_steps := path[check])
                    and (savings := steps - new_steps - abs(i) - abs(j)) >= min_savings
                ):
                    found[(point, check)] = savings
    # We only care about how many we found so just return that.
    return len(found)


def solve(input_: str, min_savings: int, max_cheat: int) -> int:
    grid = GridBase(input_)
    # We don't actually care about how many steps are needed for the shortest path - just what it is.
    _, path_list = grid.shortest_path(*grid.find_start_and_end(), steps=True, obstacle='#')
    path = {p: i for i, p in enumerate(path_list)}
    p_func = partial(cheats, path, max_cheat, min_savings)
    return sum(Pool(10).map(p_func, path.items()))


if __name__ == '__main__':
    part1_args = [100, 2]
    expected_1 = [(4, [TEST_INPUT, 36, 2])]
    func_1 = solve

    part2_args = [100, 20]
    expected_2 = [(29, [TEST_INPUT, 72, 20])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
