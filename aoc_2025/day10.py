import re
import itertools
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

def solve(input_: str) -> int:
    machines = parse_input(input_)
    return sum(check_toggles(machine) for machine in machines)



if __name__ == '__main__':
    part1_args = []
    expected_1 = [(7, [TEST_INPUT])]
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
