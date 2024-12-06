from aoc_lib import InLoop, WalkingGrid, solve_problem
from multiprocessing import Pool

INPUT = open('data/day6.txt').read()

TEST_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""


def causes_loop(data: tuple[WalkingGrid, tuple[int, int]]) -> bool:
    grid, point = data
    try:
        grid.walk(point)
    except InLoop:
        return True
    return False

def solve(input_: str, with_obstructions: bool = False) -> int:
    grid = WalkingGrid(input_, '^', obstacle='#')
    if not with_obstructions:
        return len(grid.path)
    pool = Pool(10)
    return sum(pool.map(causes_loop, ((grid, point) for point in grid.path)))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(41, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(6, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
