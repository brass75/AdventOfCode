import re
from collections.abc import Iterable
from math import prod

from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day6.txt').read()

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def do_the_math(op: str, nums: Iterable[int]) -> int:
    if op == '*':
        return prod(nums)
    else:
        return sum(nums)


def solve(input_: str) -> int:
    matrix = [re.split(r'\s+', line.strip()) for line in input_.strip().splitlines()]
    operators = matrix.pop()
    return sum(do_the_math(operators[n], map(int, (row[n].strip() for row in matrix))) for n in range(len(operators)))

def solve2(input_: str) -> int:
    rows = input_.splitlines()
    ops = (c for c in rows.pop() if c != ' ')
    problems = [[]]
    for val in (''.join(map(str.strip, row)) for row in zip(*rows, strict=True)):
        if val:
            problems[-1].append(int(val))
        else:
            problems.append(list())
    return sum(do_the_math(op, problem) for op, problem in zip(ops, problems, strict=True))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4277556, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(3263827, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
