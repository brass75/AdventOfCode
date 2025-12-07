import math
import re
from collections.abc import Iterable

from aoc_lib import solve_problem

INPUT = open('data/day6.txt').read()

TEST_INPUT = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def do_the_math(op: str, nums: Iterable[int]) -> int:
    return math.prod(nums) if op == '*' else sum(nums)


def solve(input_: str, transform: bool = False) -> int:
    rows = input_.splitlines()
    raw_ops = rows.pop()
    operators = [c for c in raw_ops if c != ' ']
    if transform:
        operand_groups = [[]]
        for val in (''.join(map(str.strip, row)) for row in zip(*rows, strict=True)):
            if val:
                operand_groups[-1].append(int(val))
            else:
                operand_groups.append(list())
    else:
        matrix = [re.split(r'\s+', row.strip()) for row in rows]
        operand_groups = [[int(row[n].strip()) for row in matrix] for n in range(len(operators))]
    return sum(do_the_math(operator, operands) for operator, operands in zip(operators, operand_groups, strict=True))


def pattern_solve(input_: str) -> int:
    """Solution for part 2 using pattern matching to parse"""
    rows = input_.splitlines()
    raw_ops = rows.pop()
    ops = [c for c in raw_ops if c != ' ']
    col_lens = [
        len(group) - 1 for group in (m.group(0) for m in re.finditer(r'([+*]\s*?)(?:\s(?=[*+])|$)', raw_ops + ' '))
    ]
    pattern = ''.join(rf'([\d\s]{{{col_len}}})\s' for col_len in col_lens[:-1]) + rf'([\d\s]{{{col_lens[-1]}}})$'
    rows = [re.search(pattern, row).groups() for row in rows]
    problems = list()
    for idx in range(len(ops)):
        problems.append(list())
        for i in range(col_lens[idx]):
            curr = ''
            for row in rows:
                if (val := row[idx][i]) != ' ':
                    curr += val
            problems[-1].append(int(curr))
    return sum(do_the_math(op, problem) for op, problem in zip(ops, problems, strict=True))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4277556, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(3263827, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
