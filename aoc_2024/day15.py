from collections import deque

from aoc_lib import GridBase, direction_deltas, get_adjacent, solve_problem

INPUT = open('data/day15.txt').read()

TEST_INPUT = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

TEST_INPUT2 = """##########
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
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


TEST_INPUT3 = """####################
##....[]....[]..[]##
##............[]..##
##..[][]....[]..[]##
##....[]@.....[]..##
##[]##....[]......##
##[]....[]....[]..##
##..[][]..[]..[][]##
##........[]......##
####################

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""


DIRECTIONS = {
    '^': 'N',
    '>': 'E',
    '<': 'W',
    'v': 'S',
}


def parse_input(input_: str, update: bool = False) -> tuple[str, str]:
    lines, moves = input_.split('\n\n')
    moves = moves.replace('\n', '')
    return update_input(lines) if update else lines, moves


def update_input(lines: str) -> str:
    """Update part1 type input for part 2"""
    rc = ''
    for c in lines:
        match c:
            case '#':
                rc += '##'
            case '@':
                rc += '@.'
            case '.':
                rc += '..'
            case 'O':
                rc += '[]'
            case '\n':
                rc += c
    return rc


def find_guard(grid: dict) -> tuple[int, int]:
    for k, v in grid.items():
        if v == '@':
            return k


def move_guard_part1(grid: dict, moves: str):
    queue = deque(moves)
    guard = find_guard(grid)
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
                    guard = adjacent
                case '#':
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


def move_guard_part2(position: tuple[int, int], direction: str, grid: dict):
    next_position = get_adjacent(direction, position)
    match grid.get(next_position):
        case '.':
            grid[position] = '.'
            grid[next_position] = '@'
            return next_position, grid
        case '#':
            return position, grid
        case '[' | ']':
            return horizontal(position, direction, grid) if direction in 'EW' else vertical(position, direction, grid)
        case _:
            raise RuntimeError(f'Something funky is happening at {next_position=}')


def horizontal(position: tuple[int, int], direction: str, grid: dict):
    """Move box(es) horizontally"""
    delta = direction_deltas(direction)
    dx = delta[0]
    x, y = position
    x += dx
    next_position = (x, y)
    while (next_spot := grid.get((x + dx, y))) in '[]':
        x += dx
    x += dx
    match next_spot:
        case '#':
            return position, grid
        case '.':
            while x != next_position[0]:
                grid[(x, y)] = grid[(x - dx, y)]
                x -= dx
            grid[next_position] = '@'
            grid[position] = '.'
            return next_position, grid


def can_push_vertical(position: tuple[int, int], dy: int, grid: dict):
    """
    See if boxes can be moved vertically

    Since we're starting at a single point but a box takes up 2 points we need to continue to check the spaces above
    until we hit free space or a wall.
    """
    points = list()
    x, y = position
    match adj := grid.get((x, y + dy)):
        case '.':
            return True
        case '#':
            return False
        case '[' | ']':
            dx = 1 if adj == '[' else -1
            points.append((x + dx, y + dy))
            points.append((x, y + dy))
    return all(can_push_vertical(point, dy, grid) for point in points)


def get_vertical_move_coordinates(dy: int, grid: dict, points: set) -> set:
    """Figure out which points contain a box"""
    if all(grid.get((x, y + dy)) == '.' for x, y in points):
        return points

    next_row = set()

    for x, y in points:
        if (adj := grid.get((x, y + dy))) == '[':
            next_row.update([(x, y + dy), (x + 1, y + dy)])
        elif adj == ']':
            next_row.update([(x, y + dy), (x - 1, y + dy)])

    return points | get_vertical_move_coordinates(dy, grid, next_row)


def vertical(position: tuple[int, int], direction: str, grid: dict):
    """Move the guard and box(es) vertically"""
    delta = direction_deltas(direction)
    dy = delta[1]
    if not can_push_vertical(position, dy, grid):
        return position, grid
    to_move = get_vertical_move_coordinates(dy, grid, {position}) - {position}
    to_move = sorted(to_move, key=lambda c: c[1], reverse=direction != 'N')
    for x, y in to_move:
        grid[(x, y + dy)] = grid[(x, y)]
        grid[(x, y)] = '.'
    grid[position] = '.'
    grid[(position[0], position[1] + dy)] = '@'
    return (position[0], position[1] + dy), grid


def solve2(input_: str) -> int:
    lines, moves = parse_input(input_, True)
    orig = GridBase(lines)
    grid = dict(orig.items)
    pos = find_guard(grid)
    for move in moves:
        pos, grid = move_guard_part2(pos, DIRECTIONS[move], grid)
    return sum(x + (y * 100) for (x, y), v in grid.items() if v == '[')


def solve(input_: str) -> int:
    lines, moves = parse_input(input_)
    grid = dict(GridBase(lines).items)
    move_guard_part1(grid, moves)
    return sum((y * 100) + x for (x, y), c in grid.items() if c == 'O')


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2028, [TEST_INPUT]), (10092, [TEST_INPUT2])]
    func_1 = solve

    part2_args = []
    expected_2 = [(9021, [TEST_INPUT2])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
