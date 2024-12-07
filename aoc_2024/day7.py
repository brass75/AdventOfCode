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
    lines = []
    for line in input_.splitlines():
        value, operands = line.split(':')
        lines.append((int(value), tuple(map(int, operands.split()))))
    return lines


def do_the_math(*args) -> int:
    """
    Recursive function to handle the math

    :param args: I have to use args here because I want to use map in the initial call.
    :arg line: The tuple representing the line (answer, (operands))
    :arg current: The current value based on what we've done so far
    :arg index: The next index to read from the operands tuple
    :arg allow_concat: Allow concatenation via the "||" operator
    :return: The answer from the line if any of the combinations find it otherwise 0
    """
    line, current, idx, allow_concat = args[0]
    answer, operands = line
    if idx >= len(operands):
        return answer if current == answer else 0
    next = operands[idx]
    idx += 1
    funcs = [
        lambda x, y: x + y,
        lambda x, y: x * y,
    ]
    if allow_concat:
        funcs.append(lambda x, y: int(str(x) + str(y)))
    for func in funcs:
        if do_the_math((line, func(current, next), idx, allow_concat)) == answer:
            return answer
    return 0


def solve(input_: str, allow_concat: bool = False) -> int:
    lines = parse_input(input_)
    return sum(Pool(10).map(do_the_math, ((line, 0, 0, allow_concat) for line in lines)))


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
