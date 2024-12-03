from collections import Counter
from aoc_lib import solve_problem
import re

INPUT = open("data/day1.txt").read()

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_input(input_) -> tuple[list[int], list[int]]:
    line1, line2 = [], []
    for a, b in (re.findall(r"\d+", s) for s in input_.splitlines()):
        line1.append(int(a))
        line2.append(int(b))
    return line1, line2


def solve(input_: str) -> int:
    line1, line2 = parse_input(input_)
    return sum(abs(a - b) for a, b in zip(sorted(line1), sorted(line2)))


def solve2(input_: str) -> int:
    line1, line2 = parse_input(input_)
    counter = Counter(line2)
    return sum(x * counter.get(x, 0) for x in line1)


if __name__ == "__main__":
    part1_args = []
    expected_1 = [(11, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(31, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
