from collections import defaultdict, deque

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
        """
        Initialize a BatteryBank object

        :param size: The number of digits we're looking for
        :param bank: The string containing the battery definitions
        """
        self.highest = ''
        indices = defaultdict(deque)
        # Create a sorted dictionary with the key being the number and the
        # value being the indices where it appears.
        for i, n in enumerate(bank):
            indices[n].append(i)
        # Sort the dictionary, reversed, so we can process from largest to
        # smallest number.
        indices = sorted(indices.items(), reverse=True)
        if len(indices[0][1]) >= size:
            # If the highest number appears at least the number of times we're
            # looking for it has to be the highest.
            self.highest = indices[0][0] * size
            return
        base_index = 0
        while size:
            for n, index in indices:
                while index and index[0] < base_index:
                    # Get rid of indices that we have already passed
                    index.popleft()
                if not index:
                    # If there are no indices left for that number there's nothing to do
                    continue
                if index[0] + size <= len(bank):
                    # If there's enough left after the first appearance of the number to
                    # continue populating we take that number and then continue
                    self.highest += n
                    size -= 1
                    base_index = index.popleft()
                    # We need to break here to do the `while size` check.
                    break

    def __add__(self, other):
        return int(self.highest) + other

    def __radd__(self, other):
        return int(self.highest) + other


def solve(input_: str, count: int) -> int:
    return sum(BatteryBank(size=count, bank=line) for line in input_.strip().splitlines())


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
