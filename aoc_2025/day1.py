import re
from collections.abc import Generator
from dataclasses import dataclass

from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day1.txt').read()

TEST_INPUT = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


@dataclass
class Turn:
    dir: int
    count: int

    def __add__(self, other):
        return other + (self.dir * self.count)

    def __radd__(self, other):
        return other + (self.dir * self.count)


def parse_input(input_: str) -> Generator[Turn]:
    for line in input_.strip().splitlines():
        dir_, count = re.match(r'([LR])(\d+)', line).groups()
        match dir_:
            case 'L':
                yield Turn(-1, int(count))
            case 'R':
                yield Turn(1, int(count))


def solve2(input_: str) -> int:
    turns = parse_input(input_)
    # The dial starts at 50
    curr = 50
    count = 0
    for turn in turns:
        # Total number of cycles
        count += turn.count // 100
        clicks = turn.count % 100
        while clicks:
            clicks -= 1
            # Turn the dial.
            curr += turn.dir
            if curr < 0 or curr > 99:
                # If we exit the 0..99 range, get back into it.
                curr %= 100
            if curr == 0:
                # If we're pointing at 0 we can move the dial the remaining number of clicks,
                # increment the counter, and exit the loop.
                curr += turn.dir * clicks
                count += 1
                break
    return count


def solve1(input_: str, curr: int = 50) -> int:
    return sum(1 for turn in parse_input(input_) if (curr := (curr + turn) % 100) == 0)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve1

    part2_args = []
    expected_2 = [(6, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
