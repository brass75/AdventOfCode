from heapq import heappop, heappush

from aoc_lib import GridBase, solve_problem

INPUT = open('data/day17.txt').read()

TEST_INPUT = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

# Dijkstra's Algorithm for shortest path with step constraints.


def solve(input_: str, least: int, most: int, start_point: tuple[int, int]) -> int:
    board = GridBase(input_, int)
    end = board.end
    q = [(0, *start_point, 0, 0)]
    seen = set()
    while q:
        heat, x, y, px, py = heappop(q)
        if end == (x, y):
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))

        # Loop over next possible locations excluding previously visited (px, py)
        for dx, dy in {(1, 0), (0, 1), (-1, 0), (0, -1)}.difference({(px, py), (-px, -py)}):
            # Initialize the variables for each iteration of the loop.
            nx, ny, h = x, y, heat
            # Check each stop up to the maximum allowed
            for i in range(1, most + 1):
                # Increment the coordinates we're looking at
                nx, ny = nx + dx, ny + dy
                if (nx, ny) in board:
                    # Accumulate the heat from that step
                    h = h + board[(nx, ny)]
                    if i >= least:
                        # If we're beyond the minimum number of steps add to the heap.
                        heappush(q, (h, nx, ny, dx, dy))


if __name__ == '__main__':
    part1_args = [1, 3, (0, 0)]
    expected_1 = [(102, [TEST_INPUT, *part1_args])]
    func_1 = solve

    part2_args = [4, 10, (0, 0)]
    expected_2 = [(94, [TEST_INPUT, *part2_args])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
