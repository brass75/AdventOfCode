from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input_.splitlines()]


INPUT = parse_input(Path('data/day3.txt').read_text())

TEST_INPUT = parse_input(
    """
 4  5  6
10 20 30
10 10 10
""".strip()
)


def is_valid(triangle: list[int]) -> bool:
    sides = sorted(triangle)
    return sides[2] < sides[0] + sides[1]


def solve(triangles: list[list[int]]) -> int:
    return sum(map(is_valid, triangles))


def solve2(numbers: list[list[int]]) -> int:
    count = 0
    for idx in range(0, len(numbers), 3):
        for _ in range(3):
            count += is_valid([numbers[idx + jdx].pop() for jdx in range(3)])
    return count


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(1, [TEST_INPUT])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
