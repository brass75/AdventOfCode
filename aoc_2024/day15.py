from collections import deque

from aoc_lib import solve_problem, get_adjacent, GridBase

INPUT = open('data/day15.txt').read()

TEST_INPUT = '''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<'''

TEST_INPUT2 = '''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^'''


DIRECTIONS = {
    '^': 'N',
    '>': 'E',
    '<': 'W',
    'v': 'S',
}


def parse_input(input_: str) -> tuple[dict, str, str]:
    lines, moves = input_.split('\n\n')
    moves = moves.replace('\n', '')
    grid = dict()
    for i, line in enumerate(lines.splitlines()):
        for j in range(len(line.strip())):
            k = (j, i)
            v = line[j]
            grid.update({k: v})
    return grid, moves, lines


def find_guard(grid: dict) -> tuple[int, int]:
    for k, v in grid.items():
        if v == '@':
            return k


def move_guard(grid: dict, moves: str, unparsed: str):
    queue = deque(moves)
    guard = find_guard(grid)
    GridBase(unparsed, parsed=grid).print()
    while queue:
        move = queue.popleft()
        count = 1
        while queue and queue[0] == move:
            count += 1
            queue.popleft()
        for _ in range(count):
            adjacent = get_adjacent(DIRECTIONS[move], guard)
            match grid[adjacent]:
                case '.':
                    grid[guard] = '.'
                    grid[adjacent] = '@'
                    guard = adjacent
                case '#':
                    # print(f'{move=}')
                    # GridBase(unparsed, parsed=grid).print()
                    break
                case 'O':
                    next_ = adjacent
                    while (next_ := get_adjacent(DIRECTIONS[move], next_)) and grid[next_] == 'O':
                        ...
                    if grid[next_] == '.':
                        grid[next_] = 'O'
                        grid[adjacent] = '@'
                        grid[guard] = '.'
                        guard = adjacent

            # print(f'{move=}')
            # GridBase(unparsed, parsed=grid).print()


def solve(input_: str) -> int:
    grid, moves, unparsed_grid = parse_input(input_)
    move_guard(grid, moves, unparsed_grid)
    GridBase(unparsed_grid, parsed=grid).print()
    return sum((y * 100) + x for (x ,y), c in grid.items() if c == 'O')


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2028, [TEST_INPUT]), (10092, [TEST_INPUT2])]
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
