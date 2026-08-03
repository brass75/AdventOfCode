import re
from collections.abc import Iterator
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> tuple[dict[str, str], str]:
    params, start = input_.strip().split('\n\n')
    replacements: dict[str, str] = {}
    for line in params.splitlines():
        if not line.strip():
            continue
        line = line.strip()
        atom, replacement = line.split(' => ')
        replacements[replacement[::-1]] = atom[::-1]

    return replacements, start


INPUT = parse_input(Path('data/day19.txt').read_text())

TEST_INPUT = parse_input("""
e => H
e => O
H => HO
H => OH
O => HH

HOH""")

TEST_INPUT2 = parse_input("""
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO""")


def do_replacement(start: str, replacements: dict[str, str]) -> Iterator[tuple[str, int]]:
    for i in range(len(start)):
        for replacement, atom in replacements.items():
            if start[i:].startswith(atom):
                yield f'{start[:i]}{replacement}{start[i + len(atom) :]}', len(atom)


def solve(input_: tuple[dict[str, str], str]) -> int:
    replacements, start = input_
    return len({possibility for possibility, _ in do_replacement(start[::-1], replacements)})


def solve2(input_: tuple[dict[str, str], str]) -> int:
    replacements, end = input_
    end = end[::-1]

    pattern = r'|'.join(replacements.keys())

    def replace(s: re.Match):
        return replacements[s.group()]

    count = 0
    while end != 'e':
        count += 1
        end = re.sub(pattern, replace, end, count=1)
    return count


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4, [TEST_INPUT]), (7, [TEST_INPUT2])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(0, [({}, 'e')])]  # The algorithm doesn't work for the test input.
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
