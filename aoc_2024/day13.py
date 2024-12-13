import re
from functools import partial
from multiprocessing import Pool
from pprint import pp

import sympy
from sympy import Integer

from aoc_lib import solve_problem

INPUT = open('data/day13.txt').read()

TEST_INPUT = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


def parse_input(input_: str) -> list[dict]:
    machines: list[dict] = list()
    for machine in input_.split('\n\n'):
        line_pattern = re.compile(r'\s?([A-Za-z]+):\sX[+=](\d+),\sY[+=](\d+)')
        machine_dict: dict[str, tuple[int, int]] = dict()
        for line in machine.splitlines():
            match: re.Match = line_pattern.search(line)
            key, x, y = match.groups()
            machine_dict[key] = (int(x), int(y))
        machines.append(machine_dict)
    return machines


def get_machine(machine: dict[str, tuple[int, int]], prize_factor: int) -> int:
    px, py = machine['Prize']
    ax, ay = machine['A']
    bx, by = machine['B']
    # This problem comes down to solving the 2 equations:
    #    ax * na + bx * nb = px
    #    ay * na + by * nb = py
    # Where:
    #    ax, ay are the motions from an A button press
    #    bx, by are the motions from an A button press
    #    px, py are the coordinates of the prize.
    #    na and nb are the number of presses for each button.
    # Since there are 2 unknowns we can leverage sympy's solve to find them out for us.
    a, b = sympy.symbols('a, b')
    eq1 = sympy.Eq(ax * a + bx * b, px + prize_factor)
    eq2 = sympy.Eq(ay * a + by * b, py + prize_factor)
    solution = sympy.solve((eq1, eq2), (a, b))

    if not all(isinstance(obj, Integer) for obj in solution.values()):
        # sympy.solve will return non-integer solutions. Since there are no partial tokens we can throw those out.
        return 0
    return solution[a] * 3 + solution[b]


def solve(input_: str, prize_factor: int = 0) -> int:
    return sum(Pool(10).map(partial(get_machine, prize_factor=prize_factor), parse_input(input_)))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(480, [TEST_INPUT])]
    func_1 = solve

    part2_args = [10000000000000]
    expected_2 = [(480, [TEST_INPUT, 0])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
