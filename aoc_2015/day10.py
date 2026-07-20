from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


INPUT = '1113122113'

TEST_INPUT = '1'


def look_and_say(num: str) -> str:
    last = ''
    new = ''
    for c in num:
        if last and c not in last:
            new += f'{len(last)}{last[0]}'
            last = ''
        last += c
    if last:
        new += f'{len(last)}{last[0]}'
    return new


def solve(input_: str, count: int) -> int:
    s = input_
    for _ in range(count):
        s = look_and_say(s)
    return len(s)


if __name__ == '__main__':
    part1_args = [40]
    expected_1 = [(6, [TEST_INPUT, 5])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [50]
    expected_2 = [(6, [TEST_INPUT, 5])]  # [(<answer>, [<input>, *part1_args])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
