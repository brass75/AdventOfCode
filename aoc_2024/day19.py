import functools
from multiprocessing import Pool
from aoc_lib import solve_problem

INPUT = open('data/day19.txt').read()

TEST_INPUT = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def parse_input(input: str) -> tuple:
    towels, patterns = input.split('\n\n')
    return towels.split(', '), patterns.split('\n')


@functools.cache
def pattern_possible(pattern: str, towels: tuple[str, ...], current: str = '') -> int:
    if current == pattern:
        # Found one. Let the caller know.
        return 1
    if not pattern.startswith(current):
        # If the pattern doesn't start with the string we're checking it can't be it. Dead end so stop.
        return 0
    return sum(pattern_possible(pattern, towels, current + towel) for towel in towels)


def solve(input_: str, part2: bool = False) -> int:
    towels, patterns = parse_input(input_)
    # Map the pattern to just the relevant towels. Eliminate any pattern where there's a
    # letter in the pattern that doesn't exist in at least onw of the towels.
    mappings = {
        pattern: towel_group
        for pattern in patterns
        if (towel_group := tuple(towel for towel in towels if towel in pattern))
        and all(c in ''.join(towel_group) for c in pattern)
    }
    possibilities = Pool(10).starmap(pattern_possible, mappings.items())
    return sum(possibilities) if part2 else sum(map(bool, possibilities))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(6, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(16, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
