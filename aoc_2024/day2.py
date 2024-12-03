from aoc_lib import solve_problem
import re


INPUT = open("data/day2.txt").read()


TEST_INPUT = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def parse_input(input_: str) -> list[list[int]]:
    return [
        [int(c) for c in re.findall(r"\d+", line)]
        for line in input_.splitlines()
        if line
    ]


def check_line(
    nums: list[int], min_diff: int, max_diff: int, bad_allowed: bool
) -> bool:
    gt = nums[0] > nums[1]
    for i in range(len(nums) - 1):
        if gt != (nums[i] > nums[i + 1]) or not (
            min_diff <= abs(nums[i] - nums[i + 1]) <= max_diff
        ):
            return (
                any(
                    check_line(
                        [n for i, n in enumerate(nums) if i != idx],
                        min_diff,
                        max_diff,
                        False,
                    )
                    for idx in range(len(nums))
                )
                if bad_allowed
                else False
            )
    return True


def solve(input_: str, min_diff: int, max_diff: int, bad_allowed: bool) -> int:
    lines = parse_input(input_)
    return sum(check_line(line, min_diff, max_diff, bad_allowed) for line in lines)


if __name__ == "__main__":
    part1_args = [1, 3, False]
    expected_1 = [(2, [TEST_INPUT, 1, 3, False])]
    func_1 = solve

    part2_args = [1, 3, True]
    expected_2 = [(4, [TEST_INPUT, 1, 3, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
