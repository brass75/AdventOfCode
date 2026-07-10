from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


def parse_input(input_: str) -> Any:
    return input_


INPUT = parse_input(Path('data/day***.txt').read_text())

TEST_INPUT = parse_input("""""")


def solve(input_: Any) -> int:
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = []  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = []  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
