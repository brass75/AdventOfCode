from aoc_lib import DIRECTIONS, GridBase, get_adjacent, solve_problem

INPUT = open('data/day4.txt').read()

TEST_INPUT = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

MAX_ADJACENT = 4


def solve(input_: str, remove: bool = False) -> int:
    return find_movable(GridBase(input_), remove)


def find_movable(grid: GridBase, remove: bool) -> int:
    count = 0
    for spot, val in ((spot, val) for spot, val in grid.items if val == '@'):
        adj = 0
        for direction in DIRECTIONS:
            if (adj := adj + (grid.get(get_adjacent(direction, spot)) == '@')) >= MAX_ADJACENT:
                break
        else:
            count += 1
            if remove:
                grid.add_obstacle(spot, marker='.')
    return count + find_movable(grid, remove) if remove and count else count


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(13, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(43, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
