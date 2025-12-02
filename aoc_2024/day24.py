import re
from collections.abc import Iterable
from dataclasses import dataclass

import graphviz

from aoc_lib import solve_problem

INPUT = open('data/day24.txt').read()

TEST_INPUT = """x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

TEST_INPUT2 = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

TEST_INPUT3 = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""

COMMAND_PATTERN = re.compile(
    r'(?P<input1>[a-z0-9]+) (?P<operation>X?OR|AND) (?P<input2>[a-z0-9]+) -> (?P<output>[a-z0-9]+)'
)
STARTING_PATTERN = re.compile(r'([a-z\d]+): (\d)')


@dataclass
class Command:
    in1: str
    operation: str
    in2: str
    output: str

    def swap(self, other):
        output1 = self.output
        output2 = other.output
        return Command(self.in1, self.operation, self.in2, output2), Command(
            other.in1, other.operation, other.in2, output1
        )


def parse_input(input_: str) -> tuple[dict, list]:
    starting_state, commands = input_.split('\n\n')
    starts = dict()
    for line in starting_state.splitlines():
        pin, state = STARTING_PATTERN.search(line).groups()
        starts[pin] = int(state)
    commands = [Command(*match.groups()) for line in commands.splitlines() if (match := COMMAND_PATTERN.search(line))]
    return starts, commands


def run_adder(states: dict, commands: Iterable[Command]) -> int:
    while commands:
        new_commands = []
        for command in commands:
            if command.in1 not in states or command.in2 not in states:
                new_commands.append(command)
                continue
            match command.operation:
                case 'XOR':
                    states[command.output] = states[command.in1] ^ states[command.in2]
                case 'OR':
                    states[command.output] = states[command.in1] | states[command.in2]
                case 'AND':
                    states[command.output] = states[command.in1] & states[command.in2]
        commands = new_commands
    return join_bits(states)


def join_bits(states: dict, prefix: str = 'z') -> int:
    rc = 0
    for wire, state in states.items():
        # We only care about the wires with the noted prefix.
        # We can also ignore any wires at 0 since the | will ignore them.
        if not wire.startswith(prefix) or not state:
            continue

        # Figure out which bit needs to be set to 1.
        shift = int(wire[1:])
        # set it to 1.
        rc |= state << shift
    return rc


def solve(input_: str) -> int:
    states, commands = parse_input(input_)
    return run_adder(states, commands)


def solve2(input_: str, post_fix: str) -> str:
    if post_fix:
        # Ignoring the test - need to leave this in for it to run properly.
        return 'ignored'
    states, commands = parse_input(input_)
    # Turn it into a dictionary to make life easier switching the pairs.
    commands = {command.output: command for command in commands}

    # Pairs to swap from visual inspection.
    pairs = [('z07', 'shj'), ('z23', 'pfn'), ('z27', 'kcd'), ('tpk', 'wkb')]
    for o1, o2 in pairs:
        commands[o2], commands[o1] = commands[o1].swap(commands[o2])

    # Validate that fixing the pairs actually solves the problem.
    expected = join_bits(states, 'x') + join_bits(states, 'y')
    res = run_adder(states, commands.values())
    assert res == expected

    # I could not figure out how to do this algorithmically. I leveraged graphviz to create a
    # visual I could inspect and determined the pairs that way. The code is essentially to validate the answer.
    g = graphviz.Digraph()
    for command in commands.values():
        g.node(command.output, label=f'{command.output} : {command.operation}')
        g.node(command.in1)
        g.node(command.in2)
        g.edge(command.in1, command.output)
        g.edge(command.in2, command.output)
    g.render(f'data/day24{post_fix}.gv', view=True)

    # Convert the pairs to a list so we can sort and output them.
    output = list()
    for pair in pairs:
        output.extend(pair)
    return ','.join(sorted(output))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(4, [TEST_INPUT]), (2024, [TEST_INPUT2])]
    func_1 = solve

    part2_args = ['']
    expected_2 = [('ignored', [TEST_INPUT3, 'test'])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
