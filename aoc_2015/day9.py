import copy
import functools
import heapq
import re
from collections.abc import Callable
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> dict[str, dict[str, int]]:
    """
    Parses the input into a dictionary mapping the distances between cities.

    :param input_: The input string.
    :return: Dictionary with a city as the key and the value being a dictionary of all other cities and the distance
             from the key city to that city.
    """
    mappings = {}
    for line in input_.splitlines():
        city1, city2, dist = re.match(r'([a-z]+) to ([a-z]+) = (\d+)', line, flags=re.I).groups()

        # Since we are not guaranteed to get the distance from city2 to city1 we need to add both to the mapping.
        mappings.setdefault(city1, {})[city2] = int(dist)
        mappings.setdefault(city2, {})[city1] = int(dist)
    return mappings


INPUT = parse_input(Path('data/day9.txt').read_text())

TEST_INPUT = parse_input("""London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""")


def get_route(cities: dict[str, dict[str, int]], func: callable, start: str) -> int:
    """
    Get the shortest or longest route based on starting city.

    :param cities: Dictionary containing the cities and the distances to each other city.
    :param func: Callable containing either builtin min or max, used to determine long or short route.
    :param start: The starting city.
    """
    # Set the functions to use based on whether we need the longest or shortest route.
    push = heapq.heappush if func == min else heapq.heappush_max
    pop = heapq.heappop if func == min else heapq.heappop_max

    # Initialize the queue
    q = []
    push(q, (0, start, set()))

    while q:
        # Get the data for the city.
        traveled, city, visited = pop(q)

        # If we've been to all the cities this is the one we want - anything else will be longer/shorter so just return
        # that.
        if visited.intersection(cities[city]) == set(cities[city].keys()):
            return traveled

        # Mark down that we've now visitied this city on this route.
        visited.add(city)

        # Loop over all of the cities.
        for next_city, dist in cities[city].items():
            # Don't double back - if we've been to the next city we can skip it.
            if next_city in visited:
                continue

            # Add the data for the next city to the queue. Make sure to copy visited so we are not using the same set
            # for each one.
            push(q, (traveled + dist, next_city, copy.copy(visited)))

    # This will never be hit but it keeps the linter from yelling that there's a code path with no return value.
    return 1_000_000_000_000


def solve(input_: dict[str, dict[str, int]], func: Callable) -> int:
    """
    Solve the problem.

    :param input_: The problem input. In this case, this is a dictionary mapping the distances between cities.
    :param func: Callable containing either builtin min or max, used to determine whether we want the long or
                 short route.
    """
    # Use functools.partial so we can use map since that only takes 1 parameter and the others will be the same for
    # every iteration.
    route = functools.partial(get_route, input_, func)

    # Return the longest or shortest route based on which we're looking for.
    return func(map(route, input_))


if __name__ == '__main__':
    part1_args = [min]
    expected_1 = [(605, [TEST_INPUT, *part1_args])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [max]
    expected_2 = [(982, [TEST_INPUT, *part2_args])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
