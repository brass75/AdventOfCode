import re
from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day1.txt').read()

TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def parse_input(input_: str) -> list[int]:
    parsed = list()
    for line in input_.strip().splitlines():
        dir, count = re.match(r'([LR])(\d+)', line).groups()
        match dir:
            case'L':
                parsed.append(int(count) * -1)
            case 'R':
                parsed.append(int(count))
    return parsed


def solve(input_: str, increment: int = 0) -> int:
    turns = parse_input(input_)
    curr = 50
    count = 0
    for turn in turns:
        curr += turn
        while curr < 0:
            curr += 100
            count += increment
            if increment and curr == 0:
                count += 1
                break
        while curr > 99:
            curr -= 100
            count += increment
            if increment and curr == 0:
                count += 1
                break
        if not increment:
            count += curr == 0
    return count

if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve

    part2_args = [(1)]
    expected_2 = [(6, [TEST_INPUT, 1])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
