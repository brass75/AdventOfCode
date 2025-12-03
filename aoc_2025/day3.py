from collections import defaultdict, deque
from functools import partial

from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day3.txt').read()

TEST_INPUT = """
987654321111111
811111111111119
234234234234278
818181911112111
"""


class BatteryBank:
    def __init__(self, size: int, bank: str):
        self.highest = ''
        indices = defaultdict(deque)
        for i, n in enumerate(bank):
            indices[n].append(i)
        indices = sorted(indices.items(), reverse=True)
        if len(indices[0][1]) >= size:
            self.highest = indices[0][0] * size
            return
        base_index = 0
        while size:
            for n, index in indices:
                while index and index[0] < base_index:
                    index.popleft()
                if not index:
                    continue
                if index[0] + size <= len(bank):
                    self.highest += n
                    size -= 1
                    base_index = index[0]
                    index.popleft()
                    break

    def __add__(self, other):
        return int(self.highest) + other

    def __radd__(self, other):
        return int(self.highest) + other


def solve(input_: str, count: int) -> int:
    bank = partial(BatteryBank, count)
    return sum(map(bank, input_.strip().splitlines()))


if __name__ == '__main__':
    part1_args = [2]
    expected_1 = [(357, [TEST_INPUT, 2])]
    func_1 = solve

    part2_args = [12]
    expected_2 = [(3121910778619, [TEST_INPUT, 12])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
