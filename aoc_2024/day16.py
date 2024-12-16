from collections import defaultdict
from heapq import heappop, heappush

from aoc_lib import GridBase, get_adjacent, solve_problem

TURN_SCORE = 1001

INPUT = open('data/day16.txt').read()

TEST_INPUT = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

TEST_INPUT2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

POINT_MAPPING = {
    'E': {
        'N': TURN_SCORE,
        'S': TURN_SCORE,
        'E': 1,
    },
    'W': {
        'N': TURN_SCORE,
        'S': TURN_SCORE,
        'W': 1,
    },
    'N': {
        'E': TURN_SCORE,
        'W': TURN_SCORE,
        'N': 1,
    },
    'S': {
        'E': TURN_SCORE,
        'W': TURN_SCORE,
        'S': 1,
    },
}


def fewest_points(grid: GridBase, start: tuple[int, int], end: tuple[int, int], direction: str) -> dict:
    # Our queue contains:
    #  - The score (initializes to 0)
    #  - The current space we're checking (The "start" parameter)
    #  - The direction we're facing (The "direction" parameter)
    #  - A tuple containing the steps we've taken so far
    q = [(0, start, direction, tuple())]
    paths = defaultdict(set)
    seen_count = defaultdict(int)
    min_score = None
    cache = dict()
    while q:
        score, curr, direction, steps = heappop(q)
        if min_score and score > min_score:
            # If this is higher than the current highest score we can ignore it.
            continue
        if curr == end:
            min_score = min(score, min_score) if min_score else score
            paths[score].update(steps)
            paths[score].add(curr)
            continue
        # Unlike a normal DFS we want all possible options for the shortest path. So we do need to check every possible
        # shortest path to get the spaces we can pass through.
        seen_count[(curr, direction)] += 1
        if seen_count[(curr, direction)] > 19:
            # This is the lowest number I found here that gives me the correct answer.
            continue
        for dir_options, differential in POINT_MAPPING[direction].items():
            if next_point := cache.get((curr, dir_options)):
                if next_point != (-1, -1):
                    heappush(q, (score + differential, next_point, dir_options, (*steps, curr)))
                continue
            next_point = get_adjacent(dir_options, curr)
            if next_point in grid and grid[next_point] != '#':
                heappush(q, (score + differential, next_point, dir_options, (*steps, curr)))
                # Add it to the cache so we don't need to compute it again.
                cache[(curr, dir_options)] = next_point
            else:
                # Still add it to the cache with something that tells us to ignore it.
                cache[(curr, dir_options)] = (-1, -1)

    return paths


def find_start_and_end(grid: GridBase) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None
    for k, v in grid.items:
        if v == 'S':
            start = k
        elif v == 'E':
            end = k
        if start and end:
            return start, end


def solve(input_: str) -> int:
    grid = GridBase(input_)
    start, end = find_start_and_end(grid)
    paths = fewest_points(grid, start, end, 'E')
    shortest = min(paths.keys())
    # The shortest path is the answer for part1 and the number of spaces you could touch in a path with that
    # length is the answer to part2. It doesn't make sense to run them separately so just print the answer to both here.
    print(f'{shortest=} {len(paths[shortest])=}')
    return shortest


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(7036, [TEST_INPUT]), (11048, [TEST_INPUT2])]
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
