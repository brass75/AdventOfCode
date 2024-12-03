import sys

from aoc_lib import GridBase, solve_problem

INPUT = open('data/day23.txt').read()

TEST_INPUT = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def get_intersections_and_distances(
    grid: GridBase, start: tuple[int, int], end: tuple[int, int], ignore_slopes: bool
) -> dict:
    """Builds a dictionary of intersections and the distance(s) to the next intersection(s)"""
    valid_steps = set()
    for coords, value in grid.items:
        if value != '#' and len(list(handle_slopes(coords, grid, ignore_slopes))) >= 2:
            valid_steps.add(coords)
    valid_steps.update((start, end))
    reduced = {}
    for _coords in valid_steps:
        q = [_coords]
        seen = {_coords}
        dist = 0
        while q:
            next_q = []
            dist += 1
            for coords in q:
                for step in handle_slopes(coords, grid, ignore_slopes):
                    if step not in seen:
                        if step in valid_steps:
                            reduced.setdefault(coords, list()).append((dist, step))
                            seen.add(step)
                        else:
                            seen.add(step)
                            next_q.append(step)
            q = next_q
    return reduced


def find_entry(grid: GridBase, start: bool = True) -> tuple[int, int] | None:
    """Find the entry/exit point of the grid."""
    y = 0 if start else grid.height - 1
    for p in ((x, y) for x in range(grid.length)):
        if grid[p] == '.':
            return p
    return None


def handle_slopes(p: tuple[int, int], grid: GridBase, ignore_slopes: bool = False):
    """Get the next point(s) for the current location in the grid."""
    adjacents = ((0, 1), (1, 0), (0, -1), (-1, 0))
    if not ignore_slopes:
        if curr := grid.get(p):
            match curr:
                case '^':
                    adjacents = [(0, -1)]
                case 'v':
                    adjacents = [(0, 1)]
                case '<':
                    adjacents = [(-1, 0)]
                case '>':
                    adjacents = [(1, 0)]
    for dx, dy in adjacents:
        next_possible = (p[0] + dx, p[1] + dy)
        # Set the default so we don't need to do 2 checks.
        if grid.get(next_possible, '#') != '#':
            yield next_possible


def dfs(
    grid: GridBase,
    current_location: tuple[int, int],
    path: list,
    path_set: set,
    end: tuple[int, int],
    ignore_slopes: bool = False,
):
    """Depth first search of all paths in a grid. Updates the longest path found."""
    global longest
    if current_location == end:
        longest = max(longest, len(path))
        return
    for next_location in handle_slopes(current_location, grid, ignore_slopes):
        if next_location not in path_set:
            path.append(next_location)
            path_set.add(next_location)
            dfs(grid, next_location, path, path_set, end, ignore_slopes)
            path_set.remove(next_location)
            path.pop(-1)


def dfs2(
    cur: tuple[int, int],
    path_set: set,
    total_dist: int,
    end: tuple[int, int],
    reduced: dict,
):
    """Depth first search of all paths in a grid. Updates the longest path found. Uses a data set of intersections."""
    for dist, next_step in reduced[cur]:
        if next_step not in path_set:
            if next_step == end:
                global longest
                longest = max(longest, total_dist + dist)
                continue
            path_set.add(next_step)
            dfs2(next_step, path_set, total_dist + dist, end, reduced)
            path_set.remove(next_step)


def solve(input_: str, ignore_slopes: bool = False) -> int:
    global longest
    # Reset longest before each run so we don't use the previous answer.
    longest = 0
    grid = GridBase(input_)
    start = find_entry(grid, True)
    end = find_entry(grid, False)
    if ignore_slopes:
        dfs2(
            start,
            set(),
            0,
            end,
            get_intersections_and_distances(grid, start, end, ignore_slopes),
        )
    else:
        dfs(grid, start, list(), set(), end, ignore_slopes)
    return longest


if __name__ == '__main__':
    # Large recursion depth so set it here globally.
    sys.setrecursionlimit(20_000)
    # Since the workhorse is a recursive function that doesn't return a value we need a global to handle it.
    longest = 0

    part1_args = [False]
    expected_1 = [(94, [TEST_INPUT, *part1_args])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(154, [TEST_INPUT, *part2_args])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
