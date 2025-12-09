from dataclasses import dataclass

from aoc_lib import solve_problem

INPUT = open('data/day9.txt').read()

TEST_INPUT = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

class Point:
    def __init__(self, point: str):
        self.x, self.y = map(int, point.split(','))

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass(frozen=True)
class Rectangle:
    p1: Point
    p2: Point


    @property
    def length(self):
        return  max((self.p1.x, self.p2.x)) - min((self.p1.x, self.p2.x)) + 1

    @property
    def height(self):
        return  max((self.p1.y, self.p2.y)) - min((self.p1.y, self.p2.y)) + 1

    @property
    def area(self):
        return self.height * self.length


def solve(input_: str) -> int:
    points = [Point(line) for line in input_.strip().splitlines()]
    recatngles = dict()
    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            curr = frozenset((p1, p2))
            if curr not in recatngles:
                recatngles[curr] = Rectangle(p1, p2)
    return max(r.area for r in recatngles.values())


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(50, [TEST_INPUT])]
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
