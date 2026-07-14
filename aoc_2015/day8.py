import re
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: bytes) -> list[bytes]:
    return [line.strip() for line in input_.strip().splitlines()]


# For this one we need bytes and not string to properly handle the parsed vs. unparsed length.
INPUT = parse_input(Path('data/day8.txt').read_bytes())

TEST_INPUT = parse_input(rb"""
""
"abc"
"aaa\"aaa"
"\x27"
""")


def solve(input_: list[bytes]) -> int:
    return sum(map(len, input_)) - sum(map(lambda line: len(eval(line)), input_))


def solve2(input_: list[bytes]) -> int:
    def line_sub(line: bytes):
        """Encode the string to have escaped \\ and ", return it enclosed in "" """
        return f'"{re.sub(r'(["\\])', r"\\\g<1>", line.decode())}"'

    return sum(map(len, map(line_sub, input_))) - sum(map(len, input_))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(12, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(19, [TEST_INPUT])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
