import functools
import re
from collections import defaultdict

from aoc_lib import solve_problem

INPUT = open('data/day14.txt').read()

TEST_INPUT = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def parse_input(input_: str) -> list[dict]:
    lines = input_.splitlines()
    line_pattern = re.compile(r'p=(?P<start_x>\d+),(?P<start_y>\d+)\s+v=(?P<vector_x>-?\d+),(?P<vector_y>-?\d+)')
    return [{k: int(v) for k, v in line_pattern.search(line).groupdict().items()} for line in lines]


def get_next_location(
    sx: int, sy: int, vx: int, vy: int, width: int, height: int, num_steps: int = 1
) -> tuple[int, int]:
    """Calculate the position after num_steps steps"""
    nx = (sx + (vx * num_steps)) % width
    ny = (sy + (vy * num_steps)) % height
    if nx < 0:
        nx = width + nx
    if ny < 0:
        ny = width + ny
    return nx, ny


@functools.cache
def get_quadrant(x: int, y: int, w: int, h: int) -> int or None:
    """Determine which (if any!) quadrant it will be in"""
    dx = w // 2
    dy = h // 2
    if x == dx or y == dy:
        # dx and dy represent the x and y indices of the dividing void.
        return None
    # Since bool inherits from int True is 1 and 0 is false. We can then do some quick math to
    # figure out which quadrant a given robot is in.
    return (x > dx) + (2 * (y > dy))


def quadrant_math(height: int, num_steps: int, robots: list[dict], width: int) -> int:
    """Get the product of the number of robots in each quadrant"""
    # Move the robots
    after_steps = [
        get_next_location(
            robot['start_x'], robot['start_y'], robot['vector_x'], robot['vector_y'], width, height, num_steps
        )
        for robot in robots
    ]
    quadrants = defaultdict(int)
    for robot in after_steps:
        if (quadrant := get_quadrant(*robot, width, height)) is not None:
            # Increment the counter for each quadrant. None is the dividing void.
            quadrants[quadrant] += 1
    return functools.reduce(lambda x, y: x * y, quadrants.values())


def solve(input_: str, width: int, height: int, num_steps: int, tree_hunt: bool = False) -> int:
    robots = parse_input(input_)
    if not tree_hunt:
        # Part 1
        return quadrant_math(height, num_steps, robots, width)
    # By running the math for part 1 long enough we'll find that the number of steps that gives the
    # smallest answer will produce the tree.
    rc = min(
        {n + 1: quadrant_math(height, n + 1, robots, width) for n in range(num_steps)}.items(),
        key=lambda x: x[1],
    )[0]
    # Print it out to see it's correct (and the pretty picture!)
    grid = [list('.' * width) for _ in range(height)]
    for robot in [
        get_next_location(robot['start_x'], robot['start_y'], robot['vector_x'], robot['vector_y'], width, height, rc)
        for robot in robots
    ]:
        j, i = robot
        grid[i][j] = '#'
    print('\n'.join(''.join(line) for line in grid))
    return rc


if __name__ == '__main__':
    part1_args = [101, 103, 100]
    expected_1 = [(12, [TEST_INPUT, 11, 7, 100])]
    func_1 = solve

    part2_args = [101, 103, 10000, True]
    expected_2 = [(12, [TEST_INPUT, 11, 7, 100])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
