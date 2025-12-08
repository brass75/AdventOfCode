import functools
import heapq
import math
from collections import deque
from dataclasses import dataclass
from itertools import starmap, combinations

from aoc_lib import solve_problem

INPUT = open('data/day8.txt').read()

TEST_INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int
    z: int

    @property
    def magnitude(self):
      return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @classmethod
    def from_string(cls, data: str) -> Point:
        return cls(*map(int, data.split(',')))

    def __sub__(self, other) -> Point:
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __str__(self):
        return f"{self.x},{self.y},{self.z}"

def parse_input(input_: str) -> list[Point]:
    return [Point.from_string(line) for line in input_.strip().splitlines()]


def solve(input_: str, limit: int = 0) -> int:
    boxes = parse_input(input_)
    pairs = {
        frozenset((p1, p2)): ((p1 - p2).magnitude, (p1, p2))
        for p1 in boxes
        for p2 in boxes
        if p1 != p2
    }
    pairs = deque(sorted((v, p, q) for (p, q), v in pairs.items()))
    circuits = {box: {box} for box in boxes}
    for _ in range(limit):
        _, p, q = pairs.popleft()
        if circuits[p] is not circuits[q]:
            circuit = circuits[p] | circuits[q]
            circuits.update({p: circuit for p in circuit})
    return math.prod(heapq.nlargest(3, {len(circuit) for circuit in circuits.values()}))


if __name__ == '__main__':
    part1_args = [1000]
    expected_1 = [(40, [TEST_INPUT, 10])]
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
