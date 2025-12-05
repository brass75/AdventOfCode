from aoc_lib import Range, solve_problem

INPUT = open('data/day5.txt').read()

TEST_INPUT = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def parse_input(input_: str) -> tuple[list[Range], list[int]]:
    _ranges, ingredients = input_.strip().split('\n\n')
    ranges = {Range(*map(int, range_.strip().split('-'))) for range_ in _ranges.strip().splitlines()}

    ingredients = [int(ingredient) for ingredient in ingredients.splitlines()]
    return sorted(ranges), ingredients


def solve(input_: str) -> int:
    ranges, ingredients = parse_input(input_)
    return sum(any(ingredient in range_ for range_ in ranges) for ingredient in ingredients)


def solve2(input_: str) -> int:
    ranges, _ = parse_input(input_)
    for i, range1 in enumerate(ranges):
        # We can't use a slice for the loop since that won't reflect the update
        # and we only need one loop because the list is sorted.
        if (j := i + 1) >= len(ranges):
            break
        if consolidated := Range.consolidate(range1, ranges[j]):
            # If we can consolidate them zero out ranges[i] and replace ranges[j] with the consolidated one.
            ranges[i] = Range(1, 0)  # len(Range(1, 0) == 0
            ranges[j] = consolidated
    return sum(map(len, ranges))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(14, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
