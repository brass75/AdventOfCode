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
    """
    Get the solution.

    :param input_: The challenge data
    :param remove: Flag to indicate whether or not we need to move the rolls (part 2) or not (part 1)
    :return: The number of movable rolls
    """
    return find_movable(GridBase(input_), remove)


def find_movable(grid: GridBase, remove: bool) -> int:
    """
    Find all the movable rolls in the grid. If we need to remove them, do so.

    :param grid: The grid with the rolls.
    :param remove: Boolean to indicate whether we need to remove and run recursively.
    :return: The number of movable rolls.
    """
    count = 0
    for spot, val in ((spot, val) for spot, val in grid.items if val == '@'):
        adj = 0
        for direction in DIRECTIONS:
            if (adj := adj + (grid.get(get_adjacent(direction, spot)) == '@')) >= MAX_ADJACENT:
                # Once we have more than 4 we don't need to look at any more. This one can't be moved.
                break
        else:
            # We checked all the adjacent tiles and less than 4 are occupied so it can be moved.
            count += 1
            if remove:
                # If we need to remove them we can just do it in place. It will lower the number of iterations.
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
