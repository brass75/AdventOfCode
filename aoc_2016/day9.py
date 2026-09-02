import re
from pathlib import Path

from aoc_lib import solve_problem

INPUT = Path('data/day9.txt').read_text()

TEST_INPUT = 'X(8x2)(3x3)ABCY'
TEST_INPUT2 = 'ADVENT'
TEST_INPUT3 = 'A(2x2)BCD(2x2)EFG'


def solve(compressed: str, full: bool = False) -> int:
    compressed = re.sub(r'\s+', '', compressed)
    if not (marker := re.search(r'\((\d+)x(\d+)\)', compressed)):
        return len(compressed)
    pos = marker.start(0)
    count, repeat = map(int, marker.groups())
    idx = pos + len(marker.group(0))
    mid = solve(compressed[idx : idx + count], full) if full else count
    return pos + (mid * repeat) + solve(compressed[idx + count :], full)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(18, [TEST_INPUT]), (6, [TEST_INPUT2]), (11, [TEST_INPUT3])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [
        (20, [TEST_INPUT, True]),
        (445, ['(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', True]),
        (241920, ['(27x12)(20x12)(13x14)(7x10)(1x12)A', True]),
    ]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
