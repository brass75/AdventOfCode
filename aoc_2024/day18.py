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


def get_grid(dropped: set[tuple[int, int]], size: int) -> GridBase:
    s = ''
    for y in range(size):
        for x in range(size):
            s += '#' if (x, y) in dropped else '.'
        s += '\n'
    grid = GridBase(s)
    return grid


def solve(input_: str, fallen: int, size: int, find_blockage: bool = False) -> int | tuple[int, int]:
    blocked = deque()
    for line in input_.splitlines():
        blocked.append(tuple(map(int, re.findall(r'-?\d+', line))))
    dropped = {blocked.popleft() for _ in range(fallen)}
    grid = get_grid(dropped, size)
    if not find_blockage:
        return grid.shortest_path((0, 0), (size - 1, size - 1), '#')
    while blocked:
        obstacle = blocked.popleft()
        grid.add_obstacle(obstacle)
        if not grid.shortest_path((0, 0), (size - 1, size - 1), '#'):
            return obstacle


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
