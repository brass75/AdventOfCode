import itertools
from collections import defaultdict

from aoc_lib import GridBase, solve_problem
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


def sign(a: int, b: int) -> int:
    return (a - b) // (abs(a - b))


def calculate_antinodes(pos1: Point, pos2: Point) -> set[tuple[int, int]]:
    diff = abs(pos1.x - pos2.x), abs(pos1.y - pos2.y)
    pos1_signs = sign(pos1.x, pos2.x), sign(pos1.y, pos2.y)
    pos2_signs = sign(pos2.x, pos1.x), sign(pos2.y, pos1.y)

    return {
        (pos1.x + pos1_signs[0] * diff[0], pos1.y + pos1_signs[1] * diff[1]),
        (pos2.x + pos2_signs[0] * diff[0], pos2.y + pos2_signs[1] * diff[1]),
    }


def solve(input_: str, include_antennae: bool = False) -> int:
    grid = GridBase(input_, ignore='.')
    antennas = defaultdict(list)
    for loc, freq in grid.items:
        antennas[freq].append(loc)
    antinodes = set()

    for segment in (segments for positions in antennas.values() for segments in itertools.combinations(positions, 2)):
        found = {antinode for antinode in calculate_antinodes(*(Point(*s) for s in segment)) if antinode in grid}
        antinodes.update(found)
        updated = {*found, *segment}
        while include_antennae:
            added = set()
            for updated_segment in itertools.combinations(updated, 2):
                found = calculate_antinodes(*(Point(*s) for s in updated_segment))
                added.update(antinode for antinode in found if antinode in grid and antinode not in antinodes)
            if not added:
                break
            antinodes.update(added)
            updated.update(added)

    return len(antinodes)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(14, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(34, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
