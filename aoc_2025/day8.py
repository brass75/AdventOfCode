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

    def get_distance(self, other: Point) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

def parse_input(input_: str) -> list[Point]:
    return [Point(*map(int, line.split(','))) for line in input_.strip().splitlines()]

def solve(input_: str, limit: int = 0) -> tuple[int, int]:
    part1, part2 = 0, 0
    boxes = parse_input(input_)
    pairs = dict()
    for p1 in boxes:
        for p2 in boxes:
            pair = frozenset((p1, p2))
            if p1 == p2 or pair in pairs:
                # The "pair in pairs" check is to avoid doing the unneeded calculation
                continue
            # We need the distance and the pair for the heap to work as expected
            pairs[pair] = (p1.get_distance(p2), *pair)
    pairs = list(pairs.values())
    heapq.heapify(pairs)
    circuits = {box: {box} for box in boxes}
    while not (part1 and part2):
        # We don't care about the distance at this point - that was just used for the heap to sort properly
        _, p, q = heapq.heappop(pairs)
        if circuits[p] is not circuits[q]:
            # If they're not in a circuit already merge their circuits and update all the boxes in the circuit.
            circuit = circuits[p] | circuits[q]
            circuits.update({p: circuit for p in circuit})
            if len(circuit) == len(boxes):
                # When we have a circuit that includes all the boxes we've found the part 2 solution
                part2 = p.x * q.x
        if (limit := limit - 1) == 0:
            # Part 1 is limited so we can update it now.
            part1 = math.prod(heapq.nlargest(3, {len(circuit) for circuit in circuits.values()}))
    return part1, part2


if __name__ == '__main__':
    # Same algorithm for both. Use a single run for both.
    part1_args = [1000]
    expected_1 = [((40, 25272), [TEST_INPUT, 10])]
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
