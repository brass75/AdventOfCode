from aoc_lib import CARDINAL_DIRECTIONS, GridBase, get_adjacent, solve_problem

INPUT = open('data/day20.txt').read()

TEST_INPUT = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def find_start_and_end(grid: GridBase) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None
    for k, v in grid.items:
        if v == 'S':
            start = k
        if v == 'E':
            end = k
        if start and end:
            return start, end


def get_shortest_path(
    grid: GridBase, start: tuple[int, int], end: tuple[int, int], obstacles: set, removed: tuple[int, int], max_length: int = None
) -> tuple[tuple[int, int], int | tuple[int, list]]:
    return removed, grid.shortest_path(start, end, additional_obstacles=obstacles.difference({removed}), max_length=max_length)


def solve(input_: str, max_savings: int) -> int:
    grid = GridBase(input_)
    start, end = find_start_and_end(grid)
    obstacles = {k for k, v in grid.items if v == '#'}
    dist, path = grid.shortest_path(start, end, steps=[], obstacle='#')
    removables = set()
    for blocked in obstacles:
        if not any(get_adjacent(direction, blocked) in path for direction in CARDINAL_DIRECTIONS):
            # This is not adjacent to the path - we can ignore it.
            continue
        if blocked[0] in [0, grid.length - 1] or blocked[1] in [0, grid.height - 1]:
            # This is an edge - we can ignore it.
            continue
        for direction in CARDINAL_DIRECTIONS:
            adj = get_adjacent(direction, blocked)
            if check := grid.get(adj):
                if check != '#':
                    removables.add(blocked)
                    continue
    # Sorting to make debugging easier.
    removables = sorted(removables)
    count = 0
    from functools import partial

    p_func = partial(get_shortest_path, grid, start, end, obstacles, max_length=dist - max_savings + 1)
    all_paths = sorted(map(p_func, removables), key=lambda p: p[1])
    for removed, shortest in all_paths:
        # used = all(r in steps for r in removed)
        count += dist - shortest >= max_savings
    return count


if __name__ == '__main__':
    part1_args = [100]
    expected_1 = [(4, [TEST_INPUT, 36])]
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
