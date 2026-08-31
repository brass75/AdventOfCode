import re
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[str]:
    return input_.splitlines()


INPUT = parse_input(Path('data/day7.txt').read_text())

TEST_INPUT = parse_input("""abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""")


BAD_PATTERN = re.compile(r'[\[][^]]*(([a-z])([a-z])(?<!\2)\3\2)')
FULL_PATTERN = re.compile(r'[^[]*(([a-z])([a-z])(?<!\2)\3\2)')


def solve(addresses: list[str]) -> int:
    return sum(map(bool, map(FULL_PATTERN.search, (a for a in addresses if not BAD_PATTERN.search(a)))))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
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
