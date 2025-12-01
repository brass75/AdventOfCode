import re
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


def parse_input(input_: str) -> list[Turn]:
    parsed = list()
    for line in input_.strip().splitlines():
        dir, count = re.match(r'([LR])(\d+)', line).groups()
        match dir:
            case'L':
                parsed.append(Turn(-1, int(count)))
            case 'R':
                parsed.append(Turn(1, int(count)))
    return parsed


def solve2(input_: str) -> int:
    turns = parse_input(input_)
    curr = 50
    count = 0
    for turn in turns:
        # Total number of cycles
        count += turn.count // 100
        for _ in range(turn.count % 100):
            # Turn the dial. Increment if we hit 0.
            curr += turn.dir
            if curr < 0 or curr > 99:
                curr %= 100
            count += curr == 0
    return count

def solve1(input_: str) -> int:
    turns = parse_input(input_)
    curr = 50
    count = 0
    for turn in turns:
        curr += (turn.dir * (turn.count % 100))
        curr %= 100
        count += curr == 0
    return count

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
