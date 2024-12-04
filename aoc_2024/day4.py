from aoc_lib import GridBase, solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day4.txt').read()

TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


def get_adjacent(direction: str, point: tuple[int, int]) -> tuple[int, int]:
    col, row = point
    match direction:
        case 'N':
            return col, row - 1
        case 'NE':
            return col + 1, row - 1
        case 'E':
            return col + 1, row
        case 'SE':
            return col + 1, row + 1
        case 'S':
            return col, row + 1
        case 'SW':
            return col - 1, row + 1
        case 'W':
            return col - 1, row
        case 'NW':
            return col - 1, row - 1


def solve(input_: str) -> int:
    grid = GridBase(input_.strip())
    found = 0
    for point, letter in grid.items:
        if letter != 'X':
            continue
        for direction in DIRECTIONS:
            if (
                ((next_point := get_adjacent(direction, point)) and grid.get(next_point) == 'M')
                and ((next_point := get_adjacent(direction, next_point)) and grid.get(next_point) == 'A')
                and ((next_point := get_adjacent(direction, next_point)) and grid.get(next_point) == 'S')
            ):
                found += 1
    return found


def solve2(input_: str) -> int:
    grid = GridBase(input_.strip())
    found = 0
    for point, letter in grid.items:
        if letter != 'A':
            continue
        if (
            (grid.get(get_adjacent('NE', point)) == 'M' and grid.get(get_adjacent('SW', point)) == 'S')
            or grid.get(get_adjacent('NE', point)) == 'S'
            and grid.get(get_adjacent('SW', point)) == 'M'
        ) and (
            (grid.get(get_adjacent('NW', point)) == 'M' and grid.get(get_adjacent('SE', point)) == 'S')
            or grid.get(get_adjacent('NW', point)) == 'S'
            and grid.get(get_adjacent('SE', point)) == 'M'
        ):
            found += 1
    return found


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(18, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(9, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
