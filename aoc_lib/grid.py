from collections.abc import Callable, Generator
from heapq import heappop, heappush
from typing import Any

from aoc_lib.hashable_dict import HashableDict

DIRECTIONS = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')


TURNS = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def as_tuple(self):
        return self.x, self.y


class GridBase:
    """Base class for a grid/matrix using a dictionary for storage"""

    def __init__(self, input_: str, func: Callable = None, char_width: int = 1, ignore: Any = None):
        self._input = input_
        lines = input_.splitlines()
        self.height = len(lines)
        self.length = len(lines[0]) // char_width
        self.char_width = char_width
        self.ignore = ignore
        temp_dict = dict()
        for i, line in enumerate(lines):
            for j in range(0, len(line), char_width):
                k = (j // char_width, i)
                v = func(line[j : j + char_width]) if func else line[j : j + char_width]
                if ignore and v == ignore:
                    continue
                temp_dict.update({k: v})
        self.grid = HashableDict(temp_dict)

    def __hash__(self) -> int:
        return hash(self.grid)

    def __getitem__(self, item: tuple[int, int]) -> Any:
        return self.grid[item]

    def __str__(self) -> str:
        return '\n'.join(''.join(str(self[i, j]) for i in range(self.length)) for j in range(self.height))

    def __len__(self) -> int:
        return self.height * self.length

    def __contains__(self, item: tuple[int, int]) -> bool:
        x, y = item
        return 0 <= x < self.length and 0 <= y < self.height

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
        """
        Returns the shortest path from start to end

        :param start: start coordinate
        :param end: end coordinate
        :param obstacle: obstacle definition
        :param max_length: maximum length of shortest path
        :param most: most allowed stops.
        :param least: least allowed stops.
        """
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
        """Print the grid with axes markers"""
        offset = max([1, len(str(self.height)) + 1, len(str(self.length)) + 1])
        print(' ' + ''.join(f'{i:{offset}}' for i in range(self.length)))
        for j in range(self.height):
            print(
                f'{j}'
                + ' ' * (offset - len(str(j)))
                + ''.join(f'{self.grid.get((i, j), self.ignore):{offset}}' for i in range(self.length))
            )


def get_adjacent(direction: str, point: tuple[int, int]) -> tuple[int, int]:
    """
    Compute the next point in a grid in the selected direction

    :param direction: the direction to compute the next point
    :param point: the starting point
    :return: the next point
    """
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


def get_all_adjacent(point: tuple[int, int], directions=DIRECTIONS) -> Generator[tuple[int, int]]:
    """
    Gets all points adjacent to the specified point

    :param point: the starting point
    :param directions: the directions to compute the adjacent
    """
    for direction in directions:
        yield get_adjacent(direction, point)


def get_different(first: tuple[int, int], second: tuple[int, int]) -> tuple[int, int]:
    return first[0] - second[0], first[1] - second[1]


class InLoop(Exception):
    pass


class WalkingGrid(GridBase):
    """A grid for path tracing."""

    def __init__(self, input_: str, start: str = None, start_pos: tuple[int, int] = None, obstacle: str = None):
        """
        Initialize a WalkingGrid instance.

        :param input_: the input file
        :param start: Optional character to indicate starting position
        :param start_pos: Optional starting position
        :param obstacle: Optional obstacle
        """
        super().__init__(input_)
        self.obstacle = obstacle
        if start_pos:
            self.start = start_pos
        elif start:
            for point, space in self.items:
                if space == start:
                    self.start = point
                    break
        else:
            raise ValueError('start_pos or start must be specified')

    def walk(self, obstacle: tuple[int, int] = None) -> set:
        """
        Walks the patch as defined in the grid

        :param obstacle: Optional location to add temporary obstacle (Does not change the grid just treats
                         an individual location as if there is an obstacle)
        :return: The set of locations in the followed path
        """
        curr = self.start
        direction = 'N'
        seen, path = set(), set()
        while curr in self:
            seen.add((curr, direction))
            if (next_point := get_adjacent(direction, curr)) not in self:
                return path
            if self[next_point] == self.obstacle or next_point == obstacle:
                direction = TURNS[direction]
            else:
                curr = next_point
            path.add(curr)
            if (curr, direction) in seen:
                raise InLoop

    @property
    def path(self) -> set:
        """The set of locations in the followed path"""
        return self.walk()
