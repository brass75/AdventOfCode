import functools
import re
from hashlib import md5
from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


def parse_input(input_: str) -> Any:
    return input_.strip()


INPUT = parse_input(Path('data/day4.txt').read_text())

TEST_INPUT = parse_input("""abcdef""")


@functools.cache
def checksum(content: str) -> str:
    """Calculate the MD5 checksum of a string"""
    return md5(content.encode('utf-8')).hexdigest()


def solve(input_: Any, zeroes: int = 5) -> int:
    n = 0
    while True:
        if re.match(r'0{' + str(zeroes) + r',}\d', checksum(f'{input_}{n}')):
            return n
        n += 1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(609043, [TEST_INPUT])]
    func_1 = solve

    part2_args = [6]
    expected_2 = [(609043, [TEST_INPUT])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
