from itertools import combinations
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[int]:
    return [int(line.strip()) for line in input_.strip().splitlines()]


INPUT = parse_input(Path('data/day17.txt').read_text())

TEST_INPUT = parse_input("""20
15
10
5
5
""")


def solve(containers: list[int], liters: int, fewest: bool = False) -> int:
    count = 0
    for r in range(1, len(containers) + 1):
        if (count := count + sum(sum(combo) == liters for combo in combinations(containers, r=r))) and fewest:
            return count
    return count


if __name__ == '__main__':
    part1_args = [150]
    # [(<answer>, [<input>, *part1_args])]
    expected_1 = [(4, [TEST_INPUT, 25])]
    func_1 = solve

    part2_args = [150, True]
    # [<answer>, [(<input>, *part2_args)]]
    expected_2 = [(3, [TEST_INPUT, 25, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
