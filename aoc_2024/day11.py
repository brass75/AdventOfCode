import functools
from collections import Counter, defaultdict

from aoc_lib import solve_problem

INPUT = open('data/day11.txt').read()

TEST_INPUT = """125 17"""


# Use memoization (functools.cache) to cache the results so if we've seen the stone before
# we don't need to process it again
@functools.cache
def transform(stone: int) -> tuple[int, ...]:
    if stone == 0:
        return (1,)
    as_str = str(stone)
    if len(as_str) % 2 == 0:
        split = len(as_str) // 2
        return int(as_str[:split]), int(as_str[split:])
    return (stone * 2024,)


def solve(input_: str, iterations: int) -> int:
    # Counter will create an initial dictionary with the counts of each stone.
    counts = Counter(map(int, input_.split()))
    for _ in range(iterations):
        results = defaultdict(int)
        # Iterate over the counter we have
        for stone, count in counts.items():
            # Transform each stone to get the new stone(2)
            for transformed in transform(stone):
                # Update the new counter with current stones and the count from its origin stone
                results[transformed] += count
        counts = results
    return sum(counts.values())


if __name__ == '__main__':
    part1_args = [25]
    expected_1 = [(55312, [TEST_INPUT, 25])]
    func_1 = solve

    part2_args = [75]
    expected_2 = [(55312, [TEST_INPUT, 25])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
