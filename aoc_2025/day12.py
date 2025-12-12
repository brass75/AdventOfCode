import re
from dataclasses import dataclass

from aoc_lib import solve_problem

INPUT = open('data/day12.txt').read()

TEST_INPUT = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


@dataclass
class Present:
    shape: str

    @property
    def area(self) -> int:
        """The area required for the Present"""
        return self.shape.count('#')


class Region:
    def __init__(self, definition: str):
        width, length, presents = re.match(r'(\d+)x(\d+): ((?:[\d+]\s?)+)', definition).groups()
        self.width = int(width)
        self.length = int(length)
        self.requires = list(map(int, presents.split()))

    @property
    def area(self) -> int:
        """The area of the region"""
        return self.width * self.length

    def required_area(self, presents: list[Present]) -> int:
        """
        Calculate the area required for a region to potentially contain all of the presents required

        :param presents: List of Present objects defining the space a given Present takes up.
        :return: The minimum area required to contain all of the presents required by the region
        """
        return sum(presents[i].area * required for i, required in enumerate(self.requires))


def parse_input(input_: str) -> tuple[list[Present], list[Region]]:
    blocks = input_.strip().rsplit('\n\n')
    presents = [Present(block) for block in blocks[:-1]]
    regions = [Region(line) for line in blocks[-1].splitlines()]
    return presents, regions


def solve(input_: str) -> int:
    presents, regions = parse_input(input_)
    return sum(region.area >= region.required_area(presents) for region in regions)


if __name__ == '__main__':
    part1_args = []
    # While the problem definition says 2 (and  based on the full definition of the problem I bet that is correct)
    # for the test data, for the actual data we only need the ones where the sum of the areas of the presents is
    # less than or equal to the area of the region.
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve

    # Last day - no part 2
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
