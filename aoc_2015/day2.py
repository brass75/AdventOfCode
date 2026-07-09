import re
from itertools import combinations
from math import prod
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[tuple[int, int, int]]:
    return [tuple(map(int, line.groups())) for line in re.finditer(r'(\d+)x(\d+)x(\d+)', input_)]


INPUT = parse_input(Path('data/day2.txt').read_text())

TEST_INPUT = parse_input("""2x3x4
1x1x10""")


def solve(boxes: list[tuple[int, int, int]]) -> int:
    return sum(
        sum(2 * area for area in areas) + min(areas)
        for box in boxes
        if (areas := [x * y for x, y in combinations(box, 2)])
    )


def solve2(boxes: list[tuple[int, int, int]]) -> int:
    return sum(prod(box) + 2 * min(sum(face) for face in combinations(box, 2)) for box in boxes)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(101, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(48, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
