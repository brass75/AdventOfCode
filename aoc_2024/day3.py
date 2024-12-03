import re

from aoc_lib import solve_problem

INPUT = open('data/day3.txt').read()

TEST_INPUT = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


def solve(input_: str, check_do: bool = False) -> int:
    do = True
    return sum(
        int(num1) * int(num2)
        for op, num1, num2 in re.findall(r"(do|don't)\(\)|mul\((\d{1,3}),(\d{1,3})\)", input_)
        if (num1 and do)
        or (
            # The "and False" at the end is because there's no math when op is set.
            op and (do := not check_do or op == 'do') and False
        )
    )


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(161, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(48, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
