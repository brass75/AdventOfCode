import copy
from pathlib import Path

from aoc_lib import GridBase, solve_problem


def parse_input(input_: str) -> GridBase:
    return GridBase(input_)


INPUT = parse_input(Path('data/day18.txt').read_text())

TEST_INPUT = parse_input(""".#.#.#
...##.
#....#
..#...
#.#..#
####..""")

TEST_INPUT2 = parse_input("""##.#.#
...##.
#....#
..#...
#.#..#
####.#""")


def solve(grid: GridBase, steps: int, corners: bool = False) -> int:
    for _ in range(steps):
        new_grid: GridBase = copy.deepcopy(grid)
        for point, val in grid.items:
            if corners and point in grid.corners:
                continue
            all_adjacent: int = grid.all_adjacent(point, value='#')
            if val == '#':
                if all_adjacent not in [2, 3]:
                    new_grid.grid[point] = '.'
            elif all_adjacent == 3:
                new_grid.grid[point] = '#'
        grid: GridBase = new_grid

    return sum(v == '#' for v in grid.values)


if __name__ == '__main__':
    part1_args = [100]
    expected_1 = [(4, [TEST_INPUT, 4])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [100, True]
    expected_2 = [(17, [TEST_INPUT2, 5, True])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
