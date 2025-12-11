from collections import defaultdict

from aoc_lib import solve_problem

INPUT = open('data/day7.txt').read()

TEST_INPUT = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""


def solve(input_: str) -> tuple[int, int]:
    splits = 0
    # We don't need lines that don't cause a split - it's just wasted time processing
    lines = [line for line in input_.strip().splitlines() if '^' in line]
    curr = defaultdict(int)
    # Set up the start
    curr[input_.index('S')] = 1
    for n, line in enumerate(lines, 1):
        print(f'Checking {n} line={"".join(line)}')
        next_indices = defaultdict(int)
        for i, count in curr.items():
            if count > 0:
                if line[i] == '^':
                    # The beam splits, record that and update for the next one.
                    splits += 1
                    next_indices[i - 1] += count
                    next_indices[i + 1] += count
                else:
                    # No split so keep going on that index
                    next_indices[i] += count
        curr = next_indices
    return splits, sum(curr.values())


if __name__ == '__main__':
    part1_args = []
    # Since we're running the exact same thing for both parts we can just run it once.
    expected_1 = [((21, 40), [TEST_INPUT])]
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
