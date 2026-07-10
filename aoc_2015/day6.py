import re
from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


def parse_input(input_: str) -> Any:
    command_pattern = r'(turn (?:on|off)|toggle) (\d+),(\d+) through (\d+),(\d+)'
    commands: list[Command] = []
    for line in input_.strip().splitlines():
        command, *(coordinates) = re.search(command_pattern, line).groups()
        commands.append(Command(command, *map(int, coordinates)))
    return commands


class Command:
    """Class for holding a command"""

    def __init__(self, command: str, tlx: int, tly: int, brx: int, bry: int):
        self.command = command
        self.top_left = tlx, tly
        self.bottom_right = brx, bry
        self.ranges = self._get_ranges()

    def _get_ranges(self) -> tuple[range, range]:
        """Get the ranges that define the rectangle"""
        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        sorted_y = sorted((y1, y2))
        sorted_y[1] += 1
        sorted_x = sorted((x1, x2))
        sorted_x[1] += 1
        return range(*sorted_x), range(*sorted_y)

    def run(self, grid: list[list[int]], change_type: str) -> list[list[int]]:
        """
        Run the command.

        Command can be:
          - 'turn on' - in bool mode this sets the bulb to True, in int mode it increments it,
          - 'turn off' - in bool mode this sets the bulb to False, in int mode it decrementss it to a minimum of 0.
          - 'toggle' - in bool mode this toggles the bulb, in int mode it increases it by 2.
        """
        range_x, range_y = self.ranges
        match self.command:
            case 'turn on':
                for row in range_y:
                    for bulb in range_x:
                        if change_type == 'bool':
                            grid[row][bulb] = True
                        else:
                            grid[row][bulb] += 1
            case 'turn off':
                for row in range_y:
                    for bulb in range_x:
                        if not grid[row][bulb]:
                            continue
                        if change_type == 'bool':
                            grid[row][bulb] = False
                        else:
                            grid[row][bulb] -= 1
            case 'toggle':
                for row in range_y:
                    for bulb in range_x:
                        if change_type == 'bool':
                            grid[row][bulb] = not grid[row][bulb]
                        else:
                            grid[row][bulb] += 2
        return grid


INPUT = parse_input(Path('data/day6.txt').read_text())

TEST_INPUT = parse_input("""turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500""")

TEST_INPUT2 = parse_input("""turn on 0,0 through 0,0
toggle 0,0 through 999,999""")


def solve(input_: Any, change_type: str) -> int:
    # Start with a 1_000x1_000 grid of bulbs that are all off.
    grid = [[0 for _ in range(1_000)] for _ in range(1_000)]

    # Run the commands
    for command in input_:
        grid = command.run(grid, change_type)

    # Return the sum of all the numbers (in bool mode this is how many are on, in int mode it's the brightness.)
    return sum(sum(row) for row in grid)


if __name__ == '__main__':
    part1_args = ['bool']
    expected_1 = [(1_000_000 - 1_000 - 4, [TEST_INPUT, *part1_args])]
    func_1 = solve

    part2_args = ['int']
    expected_2 = [
        (1_000_000 + 2 * 1_000 - 4, [TEST_INPUT, *part2_args]),
        (2_000_001, [TEST_INPUT2, *part2_args]),
    ]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
