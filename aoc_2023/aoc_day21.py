from collections import deque
from math import ceil
from typing import Any

from aoc_lib import GridBase, quadratic_sequence, solve_problem

INPUT = open('data/day21.txt').read()

TEST_INPUT = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


class Grid(GridBase):
    def __init__(self, input_, obstacle: str, wraparound: bool):
        super().__init__(input_)
        self.obstacle = obstacle
        for coords, value in self.items:
            if value == 'S':
                self.start = coords
                break
        self.wraparound = wraparound

    def _compute_coordinates(self, item: tuple[int, int]) -> tuple[int, int]:
        x, y = item
        return (x % self.length, y % self.height) if self.wraparound else item

    def __getitem__(self, item: tuple[int, int]) -> str:
        return self.grid[self._compute_coordinates(item)]

    def __contains__(self, item):
        return self._compute_coordinates(item) in self.grid

    def get(self, item, default: Any = None):
        return self.grid.get(self._compute_coordinates(item), default)

    def bfs(self, max_dist: int) -> int:
        """
        Breadth first search of the grid for the total number of endpoints of a path max_dist length.

        :param max_dist: Maximum path length.
        :return: Total number of endpoints.
        """
        q = deque([(0, self.start)])
        visited = set()
        total = 0
        parity = max_dist % 2
        while q:
            dist, coords = q.popleft()
            if dist > max_dist:
                return total
            if coords in visited:
                continue
            visited.add(coords)
            total += dist % 2 == parity
            x, y = coords
            for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
                nx, ny = x + dx, y + dy
                if (step := self.get((nx, ny))) and step != self.obstacle:
                    q.append((dist + 1, (nx, ny)))
        return total


def solve(input_: str, num_steps: int, obstacle: str, wraparound: bool = False) -> int:
    grid = Grid(input_, obstacle, wraparound)
    step_interval = num_steps % grid.height
    seq = [grid.bfs(step_interval + (grid.height * n)) for n in range(3)]
    return quadratic_sequence(seq, ceil(num_steps / grid.height))


if __name__ == '__main__':
    part1_args = [64, '#']
    expected_1 = [(16, [TEST_INPUT, 6, '#'])]
    func_1 = solve

    part2_args = [26501365, '#', True]
    expected_2 = [
        (16, [TEST_INPUT, 6, '#', True]),
    ]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
