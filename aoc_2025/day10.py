import functools
import re
import itertools
from multiprocessing.pool import ThreadPool as Pool
from scipy.optimize import linprog
from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day10.txt').read()

TEST_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def parse_input(input_: str) -> list[dict]:
    lines = list()
    for line in input_.strip().splitlines():
        curr = dict()
        curr['lights'] = [c == '#' for c in re.search(r'\[([.#]+)]', line).group(1)]
        curr['buttons'] = tuple(tuple(map(int, group.split(','))) for group in re.findall(r'\(((?:\d+,?)+)\)', line))
        group = re.search(r'\{((?:\d+,?)+)}', line).group(1)
        curr['jolts'] = tuple(map(int, group.split(',')))
        lines.append(curr)
    return lines


def check_toggles(machine: dict) -> int:
    for n in range(1_000_000):
        for combo in itertools.combinations_with_replacement(machine['buttons'], r=n):
            lights = [False for _ in range(len(machine['lights']))]
            for toggles in combo:
                for index in toggles:
                    lights[index] = not lights[index]
            if lights == machine['lights']:
                return n
    return 0


# I'm leaving the brute force solution in here because it _should_ work but with the full data set it's
# going to take too long to actually run.
def check_joltages(machine: dict) -> int:
    @functools.cache
    def run_combo(combo, num_lights) -> list[int]:
        lights = [0 for _ in range(num_lights)]
        all_lights = set()
        for toggles in combo:
            all_lights.update(toggles)
        if not len(all_lights) == len(lights):
            return lights
        for toggles in combo:
            for index in toggles:
                lights[index] += 1
        return lights
    for n in range(1, 1_000_000):
        if any(lights == machine['jolts']
               for lights in Pool(8).starmap(run_combo,
                                             ((combo, len(machine['lights']))
                                              for combo in itertools.combinations_with_replacement(machine['buttons'], r=n)))
               ):
            return n
    return 0


# Since the only way to solve this in a reasonable amount of time is with linear algebra and I don't
# know linear algebra I'm going to let experts handle it for me.
def scipy_part2(machine: dict) -> int:
    return linprog(
        c=[1] * len(machine['buttons']),
        A_eq=[[i in move for move in machine['buttons']] for i in range(len(machine['jolts']))],
        b_eq=machine['jolts'],
        integrality=True
    ).fun


def solve(input_: str, increment: bool = False) -> int:
    machines = parse_input(input_)
    return sum(check_toggles(machine) for machine in machines) if not increment else sum(map(scipy_part2, machines))



if __name__ == '__main__':
    part1_args = []
    expected_1 = [(7, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(33, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
