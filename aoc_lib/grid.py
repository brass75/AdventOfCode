from collections.abc import Callable
from heapq import heappush, heappop
from typing import Any

from aoc_lib.hashable_dict import HashableDict


class Point:
    def __init__(self, x:int = None, y:int = None, p=None) -> None:
        if p:
            self.x = p.x
            self.y = p.y
        elif None in [x, y]:
            raise ValueError(f'Invalid initializers: {x=}, {y=}, {p=}')
        self.x = x
        self.y = y

    def __add__(self, item: tuple[int, int]):
        x, y = item.x, item.y if isinstance(item, Point) else item
        return Point(self.x + x, self.y + y)

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
    


class GridBase:
    """ Base class for a grid/matrix using a dictionary for storage """
    def __init__(self, input_: str, func: Callable = None):
        self._input = input_
        lines = input_.splitlines()
        self.height = len(lines)
        self.length = len(lines[0])
        self.grid = HashableDict({Point(j, i): func(c) if func else c
                                  for i, line in enumerate(lines)
                                  for j, c in enumerate(line)})

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

    def get(self, item, default = None):
        return self.grid.get(item, default)

    def shortest_path(self, start: Point | tuple[int, int], end: tuple[int, int], obstacle: Any = None,
                      max_length: int = 0, most: int = 1, least: int = 1, longest: bool = False,
                      callback: Callable = None) -> int:
        q = [(0, Point(start), 0, 0)]
        seen = set()

        while q:
            length, p, pp = heappop(q)
            if end == p or (max_length and length > max_length):
                return length
            if (p, pp) in seen:
                continue
            seen.add((p, pp))

            # Loop over next possible locations excluding previously visited (px, py)
            for dp in {p for p in map(Point, ((1, 0), (0, 1), (-1, 0), (0, -1)))}.difference({(-px, -py)}):
                # Initialize the variables for each iteration of the loop.
                l = length
                # Check each stop up to the maximum allowed
                for i in range(1, most + 1):
                    # Increment the coordinates we're looking at
                    np = p + dp
                    if callable:
                        res = callable((np), self, longest)
                        if res:
                            heappush(res)
                        continue
                    if np not in self or (obstacle and self[np] == obstacle):
                        continue
                    if i >= least:
                        # If we're beyond the minimum number of steps add to the heap.
                        heappush(q, (l - i if longest else l + i, np, dp))

