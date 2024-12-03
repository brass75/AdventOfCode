#! /usr/bin/env python3
from aoc_lib import calculate_polygon_area

LOOP_MARKER = 'x'

INPUT = open('data/day10.txt').read()

TEST_INPUT = """.....
.S-7.
.|.|.
.L-J.
....."""

TEST_INPUT2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

TEST_INPUT3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

TEST_INPUT4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what
# shape the pipe has.

MAPPINGS = {
    '|': 'NS',
    '-': 'EW',
    'L': 'NE',
    'J': 'NW',
    '7': 'SW',
    'F': 'SE',
}

TRANSLATIONS = {
    '|': '│',
    '-': '─',
    'L': '└',
    'J': '┘',
    '7': '┐',
    'F': '┌',
}


def parse_input(input_: str) -> list[list[str]]:
    # Since none of the input has the start on the edge we can just do this.
    return [list(line) for line in input_.splitlines()]


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for i, line in enumerate(grid):
        if 'S' in line:
            pos = (i, line.index('S'))
            find_starting_type(pos, grid)
            return pos


def find_starting_type(pos: tuple[int, int], grid: list[list[str]]) -> str:
    direction = ''
    y, x = pos
    if grid[y - 1][x] in '|7F':
        direction += 'N'
    if grid[y + 1][x] in '|LJ':
        direction += 'S'
    if grid[y][x + 1] in '-J7':
        direction += 'E'
    if grid[y][x - 1] in '-LF':
        direction += 'W'
    for mapping, direction_ in MAPPINGS.items():
        if direction == direction_:
            grid[y][x] = mapping
            return mapping
    raise ValueError(f'Unable to determine pipe type from {direction=}')


def get_next_location(pos: tuple[int, int], grid: list[list[str]], prev: tuple[int, int] = None) -> tuple[int, int]:
    a, b = get_options(pos, grid)
    return a if a != prev else b


def get_options(pos: tuple[int, int], grid: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    y, x = pos
    pipe = grid[y][x]
    if not (direction := MAPPINGS.get(pipe)):
        raise RuntimeError(f'No pipe found at {tuple([x, y])=} {grid[y][x]=}')
    match direction:
        case 'NS':
            return (y - 1, x), (y + 1, x)
        case 'EW':
            return (y, x - 1), (y, x + 1)
        case 'NW':
            return (y - 1, x), (y, x - 1)
        case 'SW':
            return (y + 1, x), (y, x - 1)
        case 'NE':
            return (y - 1, x), (y, x + 1)
        case 'SE':
            return (y + 1, x), (y, x + 1)


def set_position(grid: list[list[str]], pos: tuple[int, int]):
    y, x = pos
    if not (translation := TRANSLATIONS.get(grid[y][x])):
        raise RuntimeError(f'Unexpected character at {grid[y][x]=}')
    grid[y][x] = translation


def update_grid(
    pos: tuple[int, int], prev: tuple[int, int], grid: list[list[str]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    next_pos = get_next_location(pos, grid, prev)
    set_position(grid, pos)
    return next_pos, pos


def solve(input_: str, part_2: bool = False) -> int:
    grid = parse_input(input_)
    prev_a = start = find_start(grid)
    a = get_next_location(start, grid)
    loop = [start]
    set_position(grid, start)
    while a != start:
        loop.append(a)
        a, prev_a = update_grid(a, prev_a, grid)
    return int(calculate_polygon_area(loop) - 0.5 * len(loop) + 1) if part_2 else len(loop) // 2


if __name__ == '__main__':
    assert (total := solve(TEST_INPUT)) == 4, f'Test for part 1 failed! {total=}'
    total = solve(INPUT)
    print(f'Part 1: {total}')

    assert (total := solve(TEST_INPUT2, True)) == 10, f'Test for part 2 failed! {total=}'
    assert (total := solve(TEST_INPUT3, True)) == 4, f'Test for part 2 failed! {total=}'
    assert (total := solve(TEST_INPUT4, True)) == 8, f'Test for part 2 failed! {total=}'
    total = solve(INPUT, True)
    print(f'Part 2: {total}')
