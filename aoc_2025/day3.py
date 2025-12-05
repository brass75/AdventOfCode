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
        indices: dict[str, deque] = defaultdict(deque)
        # Create a sorted dictionary with the key being the number and the
        # value being the indices where it appears.
        for i, n in enumerate(bank):
            indices[n].append(i)
        # Sort the dictionary, reversed, so we can process from largest to
        # smallest number.
        self._indices: list[tuple[str,deque[int]]] = sorted(indices.items(), reverse=True)

        self._len = len(bank)
        self._size = size
        self._highest = None

    @property
    def highest(self) -> int:
        if not self._highest:
            self._highest = int(self._get_highest(self._indices, self._size, self._len))
        return self._highest

    def _get_highest(self, indices: list[tuple[str,deque[int]]], size: int, bank_len: int, base_index: int = 0) -> str:
        """
        Recursively determine the highest joltage for a given bank.

        :param indices: The processed bank
        :param size: The number of batteries to use
        :param bank_len: The length of the bank
        :param base_index: The last index processed. Defaults to 0
        :return: The highest joltage available for the number of batteries permitted.
        """
        if not size:
            return ''
        for n, index in indices:
            while index and index[0] < base_index:
                index.popleft()
            if index and index[0] + size <= bank_len:
                return n + self._get_highest(indices, size - 1, bank_len, index.popleft())
        return ''

    def __add__(self, other):
        return self.highest + other

    def __radd__(self, other):
        return self.highest + other


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
