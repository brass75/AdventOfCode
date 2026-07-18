import json
from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


def parse_input(input_: str) -> dict | list:
    return json.loads(input_)


INPUT: Any = parse_input(Path('data/day12.txt').read_text())

TEST_INPUT: Any = parse_input("""{"a":2,"b":4}""")


def solve(objects: dict | list | int | str, ignore: str = '', total: int = 0) -> int:
    match objects:
        case dict():
            # IF the dictionary contains the ignored value, skip it and return the current total.
            if ignore and ignore in objects.values():
                return total
            # Iterate over everything in the dictionary
            total += sum(solve(item, ignore) for item in objects.values())
        case list():
            total += sum(solve(item, ignore) for item in objects)
        case int():
            return objects + total
        case _:
            return total
    return total


if __name__ == '__main__':
    part1_args = []
    # [(<answer>, [<input>, *part1_args])]
    expected_1: list[Any] = [
        (6, [TEST_INPUT]),
        (6, [[1, 2, 3]]),
        (0, [[]]),
        (3, [[[3]]]),
        (0, [{'a': [-1, 1]}]),
    ]
    func_1 = solve

    part2_args = ['red']
    # [<answer>, [(<input>, *part2_args)]]
    expected_2: list[Any] = [(4, [[1, {'c': 'red', 'b': 2}, 3], 'red'])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
