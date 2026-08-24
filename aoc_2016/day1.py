import re
from collections.abc import Iterator
from itertools import zip_longest
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[tuple[str, int]]:
    return [(dir, int(count)) for dir, count in re.findall(r'(R|L)(\d+)', input_)]


INPUT = parse_input(Path('data/day1.txt').read_text())


TURNS = {
    ('n', 'R'): 'e',
    ('n', 'L'): 'w',
    ('s', 'R'): 'w',
    ('s', 'L'): 'e',
    ('e', 'R'): 's',
    ('e', 'L'): 'n',
    ('w', 'R'): 'n',
    ('w', 'L'): 's',
}


def get_locs(start: int, end: int) -> Iterator[int]:
    """
    Get all the visited points.

    :param start: Starting point.
    :param end: Ending point.
    :yield: All the points from start to end
    """
    start, end = sorted([start, end])
    yield from range(start, end + 1)


def check_points(
    x: list[int] | Iterator[int],
    y: list[int] | Iterator[int],
    seen: set[tuple[int, int]],
    start: tuple[int, int],
) -> tuple[int, int] | None:
    """
    Check all the locations to see if we've been to one before.

    :param x: Iterable of x axis locaions to check.
    :param y: Iterable of y axis locations to check.
    :param seen: Set containing all the locations we've been to.
    :param start: Starting point which needs to be skipped.
    :return: A location we have been to or None if none exists.
    """
    if isinstance(x, list):
        default = x[0]
    elif isinstance(y, list):
        default = y[0]
    else:
        raise RuntimeError(f'Neither {x!r} nor {y!r} are lists!')
    loc: tuple[int, int]
    for loc in zip_longest(x, y, fillvalue=default):
        if loc == start:
            continue
        if loc in seen or seen.add(loc):
            return loc
    return None


def solve(directions: list[tuple[str, int]], part2: bool = False) -> int:
    location: tuple[int, int] = (0, 0)
    dir = 'n'
    seen: set[tuple[int, int]] = set()
    for turn, count in directions:
        dir = TURNS[(dir, turn)]
        x, y = location
        start = location
        match dir:
            case 'n':
                location = (x, y + count)
            case 's':
                location = (x, y - count)
            case 'e':
                location = (x + count, y)
            case 'w':
                location = (x - count, y)
        if part2:
            x1, y1 = location
            for check in ((get_locs(x, x1), [y]), ([x], get_locs(y, y1))):
                if new_loc := check_points(*check, seen, start):
                    return sum(map(abs, new_loc))
    else:
        if part2:
            return -1
    return sum(map(abs, location))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [
        (5, [parse_input('R2, L3')]),
        (2, [parse_input('R2, R2, R2')]),
        (12, [parse_input('R5, L5, R5, R3')]),
    ]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(4, [parse_input('R8, R4, R4, R8'), True])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
