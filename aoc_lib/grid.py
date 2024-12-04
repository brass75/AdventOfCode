from collections.abc import Callable
from heapq import heappop, heappush
from typing import Any

from aoc_lib.hashable_dict import HashableDict

DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


class GridBase:
    """Base class for a grid/matrix using a dictionary for storage"""

    def __init__(self, input_: str, func: Callable = None):
        self._input = input_
        lines = input_.splitlines()
        self.height = len(lines)
        self.length = len(lines[0])
        self.grid = HashableDict(
            {(j, i): func(c) if func else c for i, line in enumerate(lines) for j, c in enumerate(line)}
        )

    def __hash__(self) -> int:
        return hash(self.grid)

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

    def get(self, item, default=None):
        return self.grid.get(item, default)

    def shortest_path(
        self,
        start: tuple[int, int],
        end: tuple[int, int],
        obstacle: Any = None,
        max_length: int = 0,
        most: int = 1,
        least: int = 1,
    ) -> int:
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
                nx, ny, loop = x, y, length
                # Check each stop up to the maximum allowed
                for i in range(1, most + 1):
                    # Increment the coordinates we're looking at
                    nx, ny = nx + dx, ny + dy
                    if (nx, ny) not in self or (obstacle and self[(nx, ny)] == obstacle):
                        continue
                    if i >= least:
                        # If we're beyond the minimum number of steps add to the heap.
                        heappush(q, (loop + i, nx, ny, dx, dy))

    def print(self):
        offset = max([1, len(str(self.height)) + 1, len(str(self.length)) + 1])
        print(' ' + ''.join(f'{i:{offset}}' for i in range(self.length)))
        for j in range(self.height):
            print(
                f'{j}' + ' ' * (offset - len(str(j))) + ''.join(f'{self[(i, j)]:{offset}}' for i in range(self.length))
            )


def get_adjacent(direction: str, point: tuple[int, int]) -> tuple[int, int]:
    col, row = point
    match direction:
        case 'N':
            return col, row - 1
        case 'NE':
            return col + 1, row - 1
        case 'E':
            return col + 1, row
        case 'SE':
            return col + 1, row + 1
        case 'S':
            return col, row + 1
        case 'SW':
            return col - 1, row + 1
        case 'W':
            return col - 1, row
        case 'NW':
            return col - 1, row - 1
