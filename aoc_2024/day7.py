import os
from multiprocessing import Pool

from aoc_lib import solve_problem

INPUT = open('data/day7.txt').read()

TEST_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


def parse_input(input_: str) -> list[tuple]:
    for line in input_.splitlines():
        value, operands = line.split(':')
        yield int(value), tuple(map(int, operands.split()))


def do_the_math(*args) -> int:
    """
    Recursive function to handle the math

    :param args: I have to use args here because I want to use map in the initial call.
                :arg line: The tuple representing the line (answer, (operands))
                :arg current: The current value based on what we've done so far
                :arg idx: The next index to read from the operands tuple
                :arg operators: Operators to use
    :return: The answer from the line if any of the combinations find it otherwise 0
    """
    (answer, operands), current, idx, operators = args[0]
    if idx >= len(operands) or current > answer:
        return answer if current == answer else 0

    for operator in operators:
        if do_the_math(((answer, operands), operation(current, operands[idx], operator), idx + 1, operators)) == answer:
            return answer
    return 0


def operation(x, y, op):
    if op == '+':
        return x + y
    if op == '*':
        return x * y
    if op == '||':
        return int(str(x) + str(y))


def solve(input_: str, allow_concat: bool = False) -> int:
    funcs = ['+', '*', '||'] if allow_concat else ['+', '*']
    return sum(Pool(os.cpu_count()).map(do_the_math, ((line, 0, 0, funcs) for line in parse_input(input_))))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3749, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(11387, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
