from aoc_lib.aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day1.txt').read()

TEST_INPUT = """(()(()("""


vals = {'(': 1, ')': -1}


def solve(input_: str) -> int:
    return sum(vals[p] for p in input_.strip())


def solve2(input_: str) -> int:
    start = 0
    for i, c in enumerate(input_, 1):
        start += vals[c]
        if start < 0:
            return i


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(1, [')'])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
