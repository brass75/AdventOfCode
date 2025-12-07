from collections import deque

from aoc_lib import solve_problem

# TODO Point this to the correct day!
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


def solve(input_: str) -> int:
    splits = set()
    lines = input_.strip().splitlines()
    curr = deque()
    curr.append(input_.index('S'))
    for n, line in enumerate(lines[1:]):
        next_indices = deque()
        while curr and (idx := curr.popleft()):
            match line[idx]:
                case '^':
                    splits.add((n, idx))
                    for i in [idx + 1, idx - 1]:
                        if i not in next_indices:
                            next_indices.append(i)
                case '.':
                    next_indices.append(idx)
        curr = next_indices
    return len(splits)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(21, [TEST_INPUT])]
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
