import itertools
from functools import cache
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[int]:
    return list(map(int, input_.splitlines()))


INPUT = parse_input(Path('data/day24.txt').read_text())

TEST_INPUT = [*range(1, 6), *range(7, 12)]


@cache
def entanglements(group: tuple[int, ...]) -> int:
    entanglement: int = group[0]
    for n in group[1:]:
        entanglement *= n
    return entanglement


def solve(packages: list[int], compartments: int = 3) -> int:
    all_combinations: set[tuple[int, ...]] = set()
    expected = sum(packages) // compartments
    seen: set[tuple[int, ...]] = set()
    if expected in packages:
        return expected
    for r in range(2, len(packages)):
        for combo in itertools.combinations(packages, r=r):
            combo = tuple(sorted(combo))
            if sum(combo) != expected or combo in seen or seen.add(combo):
                continue
            rest = [package for package in packages if packages not in combo]
            for r1 in range(r, len(rest)):
                for combo2 in itertools.combinations(rest, r=r1):
                    combo2 = tuple(combo2)
                    if sum(combo2) != expected:
                        continue
                    all_combinations.add(combo)
                    if r == r1:
                        seen.add(combo2)
                        all_combinations.add(combo2)
                    break
                else:
                    continue
                break
        if not all_combinations:
            continue
        if len(all_combinations) == 1:
            return entanglements(all_combinations.pop())
        return min(map(entanglements, all_combinations))
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(99, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [4]
    expected_2 = [(44, [TEST_INPUT, 4])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
