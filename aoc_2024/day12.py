from collections import defaultdict, deque

from aoc_lib import GridBase, get_adjacent, get_different, solve_problem

INPUT = open('data/day12.txt').read()

TEST_INPUT = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""


TEST_INPUT2 = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""

TEST_INPUT3 = """AAAA
BBCD
BBCC
EEEC"""


class Plot:
    def __init__(self, coords: tuple[int, int], adjacent: list, not_adjacent: list, value: str):
        self.value = value
        self.coords = coords
        self.adjacent = adjacent
        self.not_adjacent = not_adjacent

    @property
    def perimeter(self) -> int:
        return 4 - len(self.adjacent)


def find_regions(grid: GridBase) -> list[list[Plot]]:
    """DFS to sort the grid into regions"""
    regions = list()
    seen = set()
    for point in grid.coordinates:
        if point in seen:
            continue
        queue = deque([point])
        plot_type = grid[point]
        region = list()
        while queue:
            curr = queue.popleft()
            if curr in seen:
                continue
            seen.add(curr)
            adjacent = [get_adjacent(direction, curr) for direction in ['N', 'S', 'E', 'W']]
            plot = Plot(
                coords=curr,
                adjacent=[plot for plot in adjacent if grid.get(plot) == plot_type],
                not_adjacent=[plot for plot in adjacent if grid.get(plot) != plot_type],
                value=plot_type,
            )
            region.append(plot)
            queue.extend(plot.adjacent)
        regions.append(region)
    return regions


def get_map(edges: list, first: int, second: int) -> dict:
    map = defaultdict(list)
    for edge in edges:
        map[edge[first]].append(edge[second])
    return map


def calculate_region(region: list[Plot], sides: bool = False) -> int:
    if not sides:
        # Part 1 - 4 - number of adjacent plots for each plot in the region.
        perimeter = sum(plot.perimeter for plot in region)
    else:
        # Part 2 - The number of sides (or corners) in each region
        perimeter = 0
        edges = [[], [], [], []]
        y_indexes = {-1: 0, 1: 1}
        x_indexes = {-1: 2, 1: 3}
        for plot in region:
            if len(plot.adjacent) == 4:
                # This plot is surrounded - not an edge.
                continue
            for adjacent in plot.not_adjacent:
                # We want to look at adjacent plots that are not in the region.
                dx, dy = get_different(plot.coords, adjacent)
                if dy != 0:
                    edges[y_indexes[dy]].append(adjacent)
                else:
                    edges[x_indexes[dx]].append(adjacent)
        # Now that we know the edges, we can sort those into NW, NE, SW, SE
        maps = [
            get_map(edges[0], 1, 0),
            get_map(edges[1], 1, 0),
            get_map(edges[2], 0, 1),
            get_map(edges[3], 0, 1),
        ]

        for map_ in maps:
            # Finally, figure out the number of sides.
            for points in map_.values():
                if len(points) == 1:
                    # If there's only 1 point in a given direction, we know it's a side.
                    perimeter += 1
                else:
                    # If there's more than one then we need to check them all to see if they're a corner.
                    # Sort them and see if the difference with the previously checked point is 1 - if it is
                    # we have a corner.
                    points.sort()
                    prev = -500_000  # We just need to use something that we know won't register as a corner.
                    for point in points:
                        if abs(point - prev) != 1:
                            perimeter += 1
                        prev = point
    return len(region) * perimeter


def solve(input_: str, sides: bool = False) -> int:
    grid = GridBase(input_)
    return sum(calculate_region(region, sides) for region in find_regions(grid))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(772, [TEST_INPUT2]), (1930, [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(80, [TEST_INPUT3, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
