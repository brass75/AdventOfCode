import itertools
from collections import defaultdict

from aoc_lib import solve_problem

INPUT = open('data/day23.txt').read()

TEST_INPUT = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""


def get_connections(pairs: str) -> dict:
    connections = defaultdict(set)
    pairs = [line.split('-') for line in pairs.splitlines()]
    for c1, c2 in pairs:
        if c1 == c2:
            continue
        connections[c1].add(c2)
        connections[c2].add(c1)
        for c3, c4 in pairs:
            if c3 == c1:
                connections[c1].add(c4)
            if c4 == c1:
                connections[c1].add(c3)
            if c3 == c2:
                connections[c2].add(c4)
            if c4 == c2:
                connections[c2].add(c3)
    return dict(sorted(connections.items(), key=lambda x: x[0]))


def solve(input_: str) -> int:
    connections = get_connections(input_)
    return len(
        {
            triplet
            for comp, connected in connections.items()
            for c1, c2 in itertools.combinations(connected, 2)
            if ((triplet := tuple(sorted([comp, c1, c2]))) and any(c.startswith('t') for c in triplet))
            and c1 in connections[c2]
        }
    )


def solve2(input_: str) -> str:
    connections = get_connections(input_)
    groups: set[tuple[str, ...]] = set()
    for comp, connected in connections.items():
        for conn in connected:
            group = {conn2 for conn2 in connected if conn != conn2 and conn in connections[conn2]}.union({comp, conn})
            # Make sure everything in the group is connected to every other thing in the group.
            if not all(c in connections[c1] for c in group for c1 in group if c != c1):
                continue
            groups.add(tuple(sorted(group)))

    party: tuple = max(groups, key=len)
    return ','.join(sorted(party))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(7, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [('co,de,ka,ta', [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
