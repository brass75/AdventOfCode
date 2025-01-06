from functools import cache
from multiprocessing.pool import Pool

from aoc_lib import solve_problem

INPUT = open('data/day22.txt').read()

TEST_INPUT = """1
10
100
2024"""

@cache
def mix(num1: int, num2 : int) -> int:
    return num1 ^ num2


@cache
def prune(num: int) -> int:
    return num % 16777216


def get_secret(secret: int) -> int:
    for _ in range(2000):
        secret = prune(mix(secret, secret * 64))
        secret = prune(mix(secret, secret // 32))
        secret = prune(mix(secret, secret * 2048))
    return secret


def solve(input_: str) -> int:
    secrets = [int(line) for line in input_.splitlines()]
    extrapolated = list(Pool(12).imap(get_secret, secrets))
    return sum(extrapolated)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(37327623, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
