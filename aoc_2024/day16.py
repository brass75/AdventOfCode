from heapq import heappop, heappush
from typing import Any

from aoc_lib import get_adjacent, GridBase, solve_problem

RIGHT_TURN_SCORE = 1001

INPUT = open('data/day16.txt').read()

TEST_INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

TEST_INPUT2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

POINT_MAPPING = {
    'E': {
        'N': RIGHT_TURN_SCORE,
        'S': RIGHT_TURN_SCORE,
        'E': 1,
    },
    'W': {
        'N': RIGHT_TURN_SCORE,
        'S': RIGHT_TURN_SCORE,
        'W': 1,
    },
    'N': {
        'E': RIGHT_TURN_SCORE,
        'W': RIGHT_TURN_SCORE,
        'N': 1,
    },
    'S': {
        'E': RIGHT_TURN_SCORE,
        'W': RIGHT_TURN_SCORE,
        'S': 1,
    },
}


def fewest_points(grid: GridBase, start: tuple[int, int], end: tuple[int, int], direction: str) -> int:
    q = [(0, start, direction)]
    seen = set()
    scores = set()
    while q:
        score, curr, direction = heappop(q)
        if curr == end:
            scores.add(score)
        if (curr, direction) in seen:
            continue
        seen.add((curr, direction))
        for dir_options, differential in POINT_MAPPING[direction].items():
            if (next_point := get_adjacent(dir_options, curr)) and next_point in grid and grid[next_point] != '#':
                heappush(q, (score + differential, next_point, dir_options))
    return min(scores)


def find_start_and_end(grid: GridBase) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None
    for k, v in grid.items:
        if v == 'S':
            start = k
        elif v == 'E':
            end = k
        if start and end:
            return start, end



def solve(input_: str) -> int:
    grid = GridBase(input_)
    start, end = find_start_and_end(grid)
    return fewest_points(grid, start, end, 'E')


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(7036, [TEST_INPUT]), (11048, [TEST_INPUT2])]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
