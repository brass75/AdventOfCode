import heapq
from itertools import combinations

from shapely import Polygon

from aoc_lib import solve_problem

INPUT = open('data/day9.txt').read()

TEST_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def solve(input_: str, contains: bool = False) -> int:
    points = [tuple(map(int, line.split(','))) for line in input_.strip().splitlines()]
    rects = [
        ((abs(ax - bx) + 1) * (abs(ay - by) + 1), ax, ay, bx, by) for (ax, ay), (bx, by) in combinations(points, 2)
    ]
    heapq.heapify_max(rects)
    if not contains:
        return heapq.heappop(rects)[0]
    polygon = Polygon(points + [points[0]])
    while rects:
        area, ax, ay, bx, by = heapq.heappop_max(rects)
        if Polygon([(ax, ay), (ax, by), (bx, by), (bx, ay), (ax, ay)]).within(polygon):
            return area
    return 0


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(50, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(24, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
