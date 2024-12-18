import re
from collections import deque

from aoc_lib import GridBase, solve_problem

INPUT = open('data/day18.txt').read()

TEST_INPUT = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def search_for_first_obstacle(blocked, dropped, grid, size):
    """Binary search for the first obstacle that prevents exiting"""
    low = 0
    high = len(blocked)
    # Loop until the high and low catch up to one another.
    while low <= high:
        middle = (low + high) // 2
        if not grid.shortest_path((0, 0), (size - 1, size - 1), additional_obstacles={*blocked[:middle], *dropped}):
            # We're blocked so this is the lowest potential answer.
            high = middle - 1
        else:
            # We're not blocked so the answer has to be higher than this.
            low = middle + 1
    return blocked[high]


def solve(input_: str, fallen: int, size: int, find_blockage: bool = False) -> int | tuple[int, int]:
    blocked = deque()
    for line in input_.splitlines():
        blocked.append(tuple(map(int, re.findall(r'-?\d+', line))))
    # Get the group of points with obstacles that make up the start. Use a set for fast comparison in grid.shortest_path
    dropped = {blocked.popleft() for _ in range(fallen)}
    # Starting grid is all valid. We'll dynamically add the obstacles when we check it.
    grid = GridBase('\n'.join('.' * size for _ in range(size)))
    return (
        search_for_first_obstacle(list(blocked), dropped, grid, size)
        if find_blockage
        else grid.shortest_path((0, 0), (size - 1, size - 1), additional_obstacles=dropped)
    )


if __name__ == '__main__':
    part1_args = [1024, 71]
    expected_1 = [(22, [TEST_INPUT, 12, 7])]
    func_1 = solve

    part2_args = [1024, 71, True]
    expected_2 = [((6, 1), [TEST_INPUT, 12, 7, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
