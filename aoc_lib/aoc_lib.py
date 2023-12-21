from collections.abc import Callable
import time
from heapq import heappop, heappush
from typing import Any


class GridBase:
    """ Base class for a grid/matrix using a dictionary for storage """
    def __init__(self, input_: str, func: Callable = None):
        self._input = input_
        lines = input_.splitlines()
        self.height = len(lines)
        self.length = len(lines[0])
        self.grid = {(j, i): func(c) if func else c
                     for i, line in enumerate(lines)
                     for j, c in enumerate(line)}

    def __hash__(self) -> int:
        return hash(self._input)

    def __getitem__(self, item: tuple[int, int]) -> Any:
        return self.grid[item]

    def __str__(self) -> str:
        return '\n'.join(''.join(str(self[i, j]) for i in range(self.length)) for j in range(self.height))

    def __len__(self) -> int:
        return self.height * self.length

    def __contains__(self, item: tuple[int, int]) -> bool:
        return item in self.grid

    @property
    def values(self):
        return self.grid.values()

    @property
    def items(self):
        return self.grid.items()

    @property
    def coordinates(self):
        return self.grid.keys()

    @property
    def end(self) -> tuple[int, int]:
        return self.length - 1, self.height - 1

    def get(self, item, default = None):
        return self.grid.get(item, default)

    def shortest_path(self, start: tuple[int, int], end: tuple[int, int], obstacle: Any = None,
                      max_length: int = 0, most: int = 1, least: int = 1) -> int:
        q = [(0, *start, 0, 0)]
        seen = set()
        while q:
            length, x, y, px, py = heappop(q)
            if end == (x, y) or (max_length and length > max_length):
                return length
            if (x, y, px, py) in seen:
                continue
            seen.add((x, y, px, py))

            # Loop over next possible locations excluding previously visited (px, py)
            for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}.difference({(-px, -py)}):
                # Initialize the variables for each iteration of the loop.
                nx, ny, l = x, y, length
                # Check each stop up to the maximum allowed
                for i in range(1, most + 1):
                    # Increment the coordinates we're looking at
                    nx, ny = nx + dx, ny + dy
                    if (nx, ny) not in self or (obstacle and self[(nx, ny)] == obstacle):
                        continue
                    if i >= least:
                        # If we're beyond the minimum number of steps add to the heap.
                        heappush(q, (l+i, nx, ny, dx, dy))


def quadratic_sequence(seq: list[int], x: int) -> int:
    diff1 = seq[1] - seq[0]
    diff2 = seq[2] - seq[1] - diff1

    a = diff2 // 2
    b = diff1 - (3 * a)
    c = seq[0] - a - b

    return (a * (x ** 2)) + (b * x) + c


def timed_call(func: Callable):
    def time_func(*args, **kwargs):
        start = time.time()
        rc = func(*args, **kwargs)
        return rc, time.time() - start
    return time_func


@timed_call
def _solve_problem(func: Callable, *args, **kwargs):
    return func(*args, **kwargs)


def calculate_polygon_area(coordinates: list[tuple[int, int]]) -> int:
    """
    Calculate the area of a polygon. This does not fully include the perimeter. To include the perimeter in the
    value add 1 + perimeter // 2 to the result.

    I'm not including the perimeter part of the calculation here for added flexibility in implementations.

    :param coordinates: List of x, y coordinates that define the perimeter of the polygon.
    :return: The area of the polygon excluding the perimeter.
    """
    x, y = zip(*coordinates)
    return abs(sum((x[i-1] + x[i]) * (y[i-1] - y[i]) for i in range(len(coordinates)))//2)


def solve_problem(func: Callable, part: int, test_data: tuple[int, int] | None, *args, **kwargs):
    result, run_time = _solve_problem(func, *args, *kwargs)
    test_string = ''
    if test_data:
        test, expected = test_data
        assert result == expected, f'Test {test} for part {part} failed: {expected=} {result=}'
        test_string = f' [test {test}]'
    print(f'Part {part}{test_string}: {result} [elapsed time: {run_time * 1000:.5f}ms]')
