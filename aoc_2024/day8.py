import itertools
import math
from collections import defaultdict

from aoc_lib import GridBase, solve_problem
from math import dist
from pprint import pp

from aoc_lib.grid import Point

INPUT = open('data/day8.txt').read()

TEST_INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""


def sign(a, b):
    return (a - b) // (abs(a - b))


def calculate_antinodes(pos1, pos2):
    diff = abs(pos1.x - pos2.x), abs(pos1.y - pos2.y)
    pos1_signs = sign(pos1.x, pos2.x), sign(pos1.y, pos2.y)
    pos2_signs = sign(pos2.x, pos1.x), sign(pos2.y, pos1.y)

    return {Point(
        pos1.x + pos1_signs[0] * diff[0], pos1.y + pos1_signs[1] * diff[1]
    ),Point(
        pos2.x + pos2_signs[0] * diff[0], pos2.y + pos2_signs[1] * diff[1]
    )}

def solve(input_: str) -> int:
    grid = GridBase(input_)
    antennas = defaultdict(list)
    for loc, freq in grid.items:
        if freq == '.':
            continue
        antennas[freq].append(loc)
    antinodes = set()
    for positions in antennas.values():
        for segment in itertools.combinations(positions, 2):
            antinodes.update(antinode.as_tuple() for antinode in calculate_antinodes(*(Point(*s) for s in segment)) if antinode.as_tuple() in grid)
    print(antinodes)
    return len(antinodes)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(14, [TEST_INPUT])]
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
