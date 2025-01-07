from collections import defaultdict
from functools import cache
from multiprocessing.pool import Pool

from aoc_lib import solve_problem

INPUT = open('data/day22.txt').read()

TEST_INPUT = """1
10
100
2024"""

TEST_INPUT2 = """1
2
3
2024"""


@cache
def mix(num1: int, num2: int) -> int:
    return num1 ^ num2


@cache
def prune(num: int) -> int:
    return num % 16777216


def get_secret(secret: int) -> int:
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret


def get_last_secret(secret: int) -> int:
    for _ in range(2000):
        secret = get_secret(secret)
    return secret


def build_price_db(secret: int) -> tuple[list[int], list[int]]:
    prices, deltas = list(), list()
    curr_secret = secret
    last_price = secret % 10
    for _ in range(2000):
        new_secret = get_secret(curr_secret)
        price = new_secret % 10
        prices.append(price)
        deltas.append(price - last_price)
        last_price = price
        curr_secret = new_secret
    return deltas, prices


def get_combo_prices(secret: int) -> dict:
    combo_prices = dict()
    deltas, prices = build_price_db(secret)
    for i in range(len(deltas) - 4):
        combo = tuple(deltas[i : i + 4])
        if combo in combo_prices:
            continue
        combo_prices[combo] = prices[i + 3]
    return combo_prices


def solve(input_: str) -> int:
    return sum(Pool(12).map(get_last_secret, (int(line) for line in input_.splitlines())))


def solve2(input_: str) -> int:
    combo_prices = defaultdict(int)
    for combo_price in Pool(12).map(get_combo_prices, (int(line) for line in input_.splitlines())):
        for combo, price in combo_price.items():
            combo_prices[combo] += price

    return max(combo_prices.values())


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(37327623, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(23, [TEST_INPUT2])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
