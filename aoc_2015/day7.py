import re
from pathlib import Path

from aoc_lib import solve_problem

WIRE: str = r'[a-z]+'
WIRE_OR_INT: str = rf'(?:{WIRE}|\d+)'
COMMANDS: list[str] = ['AND', 'OR', 'NOT', 'LSHIFT', 'RSHIFT']
COMMAND: str = '|'.join(COMMANDS)
COMMAND_PATTERN: re.Pattern = re.compile(rf'({WIRE_OR_INT})?\s*({COMMAND})?\s*({WIRE_OR_INT})? -> ({WIRE})')


class NoValueError(Exception):
    # Signal that the command is not ready to be processed.
    pass


class AlreadyProcessed(Exception):
    # Signal that the command has already been processed.
    pass


class Command:
    def __init__(self, cmd_string: str):
        self.lop: str | int | None
        self.operator: str | None
        self.rop: str | int | None
        self.wire: str
        self.processed: bool = False

        if match := COMMAND_PATTERN.match(cmd_string):
            lop, self.operator, rop, self.wire = match.groups()
            if lop and lop.isnumeric():
                self.lop = int(lop)
            else:
                self.lop = lop
            if rop and rop.isnumeric():
                self.rop = int(rop)
            else:
                self.rop = rop
        else:
            raise RuntimeError(f'Unhandled command format for {cmd_string=}')

    def __repr__(self) -> str:
        return f'{self.lop=} {self.operator=} {self.rop=} {self.wire=}'

    def run(self, wires: dict[str, int]) -> tuple[int, str]:
        """
        Run the command.

        The command can only be run if there is a numeric value for all operands.
        In order to have 16 bit unsigned integers we need to use `& 0xFFFF` on the
            results of the bitwise operations.

        :param wires: The dictionary containing the values of the wires.
        :returns: Tuple containing the result of the operation and the wire it is applied to.
        """
        if self.processed:
            # Ensure we don't process a command twice.
            raise AlreadyProcessed()
        lop: int = 0
        rop: int = 0
        if self.lop:
            if isinstance(self.lop, int):
                lop: int = self.lop
            elif self.lop not in wires:
                # Don't process the command without values for all operands,
                raise NoValueError()
            else:
                lop: int = wires[self.lop]
        if self.rop:
            if isinstance(self.rop, int):
                rop: int = self.rop
            elif self.rop not in wires:
                # Don't process the command without values for all operands.
                raise NoValueError()
            else:
                rop: int = wires[self.rop]
        self.processed = True
        if not self.operator:
            # No operator means that we're setting an initial value on that wire.
            return lop, self.wire
        match self.operator:
            case 'AND':
                return lop & rop & 0xFFFF, self.wire
            case 'OR':
                return lop | rop & 0xFFFF, self.wire
            case 'NOT':
                return ~rop & 0xFFFF, self.wire
            case 'LSHIFT':
                return lop << rop & 0xFFFF, self.wire
            case 'RSHIFT':
                return lop >> rop & 0xFFFF, self.wire
        raise RuntimeError(f'Unknown command: {self=}')


def parse_input(input_: str) -> str:
    return input_


INPUT: str = parse_input(Path('data/day7.txt').read_text())

TEST_INPUT: str = parse_input("""123 -> x
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
456 -> y""")


def solve(input_: str, result_wire: str, override: int = 0) -> int:
    if override:
        # Part 2 is the same as part 1 but updating the initial value of wire b with the answer from part 1.
        input_ = re.sub(r'^\d+ -> b$', f'{override} -> b', input_, count=1, flags=re.MULTILINE)
    commands = [Command(line) for line in input_.strip().splitlines()]
    wires: dict[str, int] = {}
    all_processed: bool = False
    while not all_processed:
        all_processed = True
        for command in commands:
            val: int
            wire: str
            if command.processed:
                continue
            try:
                val, wire = command.run(wires)
            except NoValueError:
                all_processed = False
                continue
            except AlreadyProcessed:
                continue
            wires[wire] = val
    return wires.get(result_wire, -1)


if __name__ == '__main__':
    part1_args = ['a']
    expected_1 = [
        (
            65412,
            [
                TEST_INPUT,
                # [(<answer>, [<input>, *part1_args])]
                'h',
            ],
        ),
        (114, [TEST_INPUT, 'g']),
    ]
    func_1 = solve

    part2_args = ['a', 3176]
    # [<answer>, [(<input>, *part2_args)]]
    expected_2 = [(114, [TEST_INPUT, 'g'])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
