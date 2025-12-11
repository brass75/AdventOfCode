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

def parse_input(input_: str) -> HashableDict:
    node_map = HashableDict()
    for line in input_.strip().splitlines():
        match = re.match(r'(.*?):\s(.*)', line)
        node, nodes = match.groups()
        nodes = frozenset(map(str.strip, nodes.split()))
        node_map[node] = nodes
    return node_map


@functools.cache
def find_out(node: str, node_map: HashableDict, nodes: frozenset[str]) -> list[frozenset[str]]:
    rc = list()
    next_nodes = node_map[node]
    if 'out' not in next_nodes:
        for next_node in next_nodes:
            rc.extend(find_out(next_node, node_map, frozenset([*nodes, node])))
    else:
        rc = [frozenset([*nodes, node])]
    return rc



def solve(input_: str) -> int:
    node_map = parse_input(input_)
    paths = find_out('you', node_map, frozenset())
    return len(paths)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(5, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
