from collections import deque

from aoc_lib import GridBase, get_adjacent, solve_problem

INPUT = open('data/day10.txt').read()

TEST_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

TEST_INPUT2 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01
"""

TEST_INPUT3 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""

TEST_INPUT4 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""


def get_trails(
    grid: GridBase, point: tuple[int, int], min_slope: int = 1, max_slope: int = 1, end_value: int = 9
) -> list:
    queue = deque([point])
    found = list()
    seen = set()
    while queue:
        curr = queue.popleft()
        seen.add(curr)
        val = grid[curr]
        for next_point in (get_adjacent(direction, curr) for direction in ['N', 'S', 'E', 'W']):
            if next_point not in grid or next_point in seen or grid[next_point] == '.':
                continue
            next_val = grid[next_point]
            if min_slope <= next_val - val <= max_slope:
                if next_val == end_value:
                    found.append(next_point)
                    continue
                queue.append(next_point)
    return found


def solve(input_: str, rating: bool = False) -> int:
    grid = GridBase(input_, func=lambda x: x if x == '.' else int(x))
    return sum(
        len(found if rating else set(found))
        for found in (get_trails(grid, point) for point, value in grid.items if value == 0)
    )


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4, [TEST_INPUT3]), (3, [TEST_INPUT2]), (36, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(13, [TEST_INPUT4, True]), (81, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
