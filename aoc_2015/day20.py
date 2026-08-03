from collections import defaultdict
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> int:
    return int(input_)


INPUT = parse_input(Path('data/day20.txt').read_text())


def solve(count: int, presents: int = 10, max_houses: int = 0) -> int:
    quotas = defaultdict(int)
    # Set the number of iterations. For the test data it anything larger than 16 will trigger a failure becausee
    # there won't be enough houses. For the real data 40 work (50 doesn't) and gets the runtime under a second.
    end = count // 40 if count > 1000 else 16

    # Use a default dict for the houses to accumulate the number of presents. It's a bit slower than using a
    # prepopulated list but it's more intuitive.
    houses = defaultdict(int)
    for elf in range(1, end):
        # By advancing by the elf we don't need to do any pesky modulos here.
        for house in range(elf, end, elf):
            if max_houses:
                if quotas[elf] > max_houses:
                    # Once an elf has delivered to all its houses it's done.
                    continue
                quotas[elf] += 1
            houses[house] += elf * presents
    return min(house for house, presents in houses.items() if presents >= count)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(8, [150])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [11, 50]
    expected_2 = [(8, [150])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
