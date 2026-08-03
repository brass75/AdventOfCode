from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> int:
    return int(input_)


INPUT = parse_input(Path('data/day20.txt').read_text())


def solve(count: int) -> int:
    houses = [0 for _ in range(count // 10)]
    for elf in range(1, count // 10):
        for house in range(elf, count // 10, elf):
            houses[house] += elf * 10
    return min(i for i, presents in enumerate(houses) if presents >= count)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(8, [150])]  # [(<answer>, [<input>, *part1_args])]
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
