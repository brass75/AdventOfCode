from collections import defaultdict
from functools import cmp_to_key

from aoc_lib import solve_problem

INPUT = open('data/day5.txt').read()

TEST_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse_input(input_: str) -> tuple[dict[str, list], list[list[str]]]:
    mappings = defaultdict(list)
    rules, order = input_.split('\n\n')
    for rule in rules.splitlines():
        before, after = rule.split('|')
        mappings[before].append(after)
    return dict(mappings), [line.split(',') for line in order.splitlines()]


def check_sort(original_list, sorted_list, not_equal):
    return original_list != sorted_list if not_equal else original_list == sorted_list


def solve(input_: str, correct_order: bool = False) -> int:
    rules, orders = parse_input(input_)

    def is_before(first, second):
        return -1 if second in rules.get(first, []) else 1

    return sum(
        int(sorted_order[len(sorted_order) // 2])
        for order in orders
        if check_sort(order, sorted_order := sorted(order, key=cmp_to_key(is_before)), correct_order)
    )


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(143, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(123, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
