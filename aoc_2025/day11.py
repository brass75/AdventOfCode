import functools
import re

from aoc_lib import HashableDict, solve_problem

INPUT = open('data/day11.txt').read()

TEST_INPUT = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

TEST_INPUT2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def parse_input(input_: str) -> HashableDict:
    node_map = HashableDict()
    for line in input_.strip().splitlines():
        node, nodes = re.match(r'(.*?):\s(.*)', line).groups()
        node_map[node] = frozenset(map(str.strip, nodes.split()))
    return node_map


@functools.cache
def find_out(node: str, node_map: HashableDict, filter_for: tuple[str], found: tuple[str]) -> int:
    if node in filter_for:
        # If we are filtering (part 2) and we found a node we're looking for, mark it down.
        found += (node,)
    next_nodes = node_map[node]
    return (
        # Keep checking the next nodes to see if this is a viable path.
        sum(find_out(next_node, node_map, filter_for, found) for next_node in next_nodes)
        if 'out' not in next_nodes
        # If this is a viable end node (node is "out" and the filter requirements have been met) return 1
        # The route isn't viable since we haven't met the filter requirements so return 0
        else not filter_for or found == filter_for
    )


def solve(input_: str, start: str = 'you', filter_for: tuple[str] = None) -> int:
    return find_out(start, parse_input(input_), filter_for or tuple(), tuple())


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(5, [TEST_INPUT])]
    func_1 = solve

    part2_args = ['svr', ('fft', 'dac')]
    expected_2 = [(2, [TEST_INPUT2, *part2_args])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
