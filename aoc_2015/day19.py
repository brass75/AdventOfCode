import heapq
from collections.abc import Iterator
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> tuple[tuple[tuple[str, str], ...], str]:
    params, start = input_.strip().split('\n\n')
    replacements: list[tuple[str, str]] = []
    for line in params.splitlines():
        if not line.strip():
            continue
        line = line.strip()
        atom, replacement = line.split(' => ')
        replacements.append((atom, replacement))

    return tuple(replacements), start


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


entry_cache = {}


def do_replacement(start: str, replacements: tuple[tuple[str, str], ...]) -> Iterator[str]:
    global entry_cache
    if cached := entry_cache.get((start, replacements)):
        yield from cached
        return

    entry_cache[(start, replacements)] = set()
    for i in range(len(start)):
        for atom, replacement in replacements:
            if start[i:].startswith(atom):
                possibility = f'{start[:i]}{replacement}{start[i + len(atom) :]}'
                if possibility in entry_cache[(start, replacements)] or entry_cache[(start, replacements)].add(
                    possibility
                ):
                    continue
                yield possibility


def solve(input_: tuple[tuple[tuple[str, str], ...], str]) -> int:
    replacements, start = input_
    possibilities: set[str] = set()
    possibilities.update(do_replacement(start, replacements))
    return len(possibilities)


def solve2(input_: tuple[tuple[tuple[str, str], ...], str]) -> int:
    replacements, end = input_
    start = 'e'
    q = [(0, start)]
    while q:
        count, curr = heapq.heappop(q)
        for next_molecule in do_replacement(curr, replacements):
            # print(f'{count = } {curr = } {next_molecule = } {end = }')
            if next_molecule == end:
                return count + 1
            if count and not end.startswith(next_molecule[:count]):
                continue
            q.append((count + 1, next_molecule))
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4, [TEST_INPUT]), (7, [TEST_INPUT2])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(3, [TEST_INPUT]), (6, [TEST_INPUT2])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
