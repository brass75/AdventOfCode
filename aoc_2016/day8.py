from pathlib import Path

from aoc_lib import solve_problem

WIDTH = 50
HEIGHT = 6


class Command:
    def __init__(self, command: str) -> None:
        pieces = command.split()
        print(pieces)
        self.x = self.y = -1
        self._input = command
        if pieces[0] == 'rect':
            self.command = 'rect'
            x, y = map(int, pieces[1].split('x'))
            self.x = x
            self.y = y
            self.pixels = 0
        else:
            self.command = 'rotate'
            self.pixels = int(pieces[~0])
            dir, val = pieces[~2].split('=')
            setattr(self, dir, int(val))

    def run(self, grid: list[list[str]]) -> list[list[str]]:
        if self.command == 'rect':
            print(f'Adding rectangle ({self.x}, {self.y})')
            for y in range(self.y):
                for x in range(self.x):
                    grid[y][x] = '#'
            return grid
        new_grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for y in range(HEIGHT):
            for x in range(WIDTH):
                new_y = y if self.x == -1 or x != self.x else y + self.pixels
                new_x = x if self.y == -1 or y != self.y else x + self.pixels
                new_grid[new_y % HEIGHT][new_x % WIDTH] = grid[y][x]
        return new_grid


def parse_input(input_: str) -> list[Command]:
    return list(map(Command, input_.splitlines()))


INPUT = parse_input(Path('data/day8.txt').read_text())

TEST_INPUT = parse_input("""rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1""")


def solve(commands: list[Command]) -> int:
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for command in commands:
        grid = command.run(grid)
    # The screen is displaying the answer for part 2 so this print is needed.
    print('\n'.join(''.join(row) for row in grid))
    return sum(c == '#' for row in grid for c in row)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(6, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = []  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
