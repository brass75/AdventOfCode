from pathlib import Path

from aoc_lib import solve_problem
from aoc_lib.grid import get_adjacent


def parse_input(input_: str) -> str:
    return input_


INPUT = parse_input(Path('data/day3.txt').read_text())

TEST_INPUT = parse_input("""^v^v^v^v^v""")


def get_next_house(instruction: str, house: tuple[int, int]) -> tuple[int, int]:
    """
    Get the coordinates of the next house.

    :param instruction: The direction to go.
    :param house: The coordinates of the current house.
    :return: The coordinates of the next house.
    """
    match instruction:
        case '^':
            return get_adjacent('N', house)
        case 'v':
            return get_adjacent('S', house)
        case '<':
            return get_adjacent('W', house)
        case '>':
            return get_adjacent('E', house)
    return house


def solve(input_: str) -> int:
    house: tuple[int, int] = 0, 0
    visited: set[tuple[int, int]] = {house}
    for instruction in input_.strip():
        house = get_next_house(instruction, house)
        visited.add(house)
    return len(visited)


def solve2(input_: str) -> int:
    santa: tuple[int, int] = 0, 0
    robot: tuple[int, int] = 0, 0
    visited: set[tuple[int, int]] = {santa}
    for i in range(0, len(input_), 2):
        santa = get_next_house(input_[i], santa)
        visited.add(santa)
        try:
            robot = get_next_house(input_[i + 1], robot)
        except IndexError:
            break
        visited.add(robot)
    return len(visited)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(11, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
