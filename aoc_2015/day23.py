import re
from enum import StrEnum
from pathlib import Path

from aoc_lib import solve_problem


class Command(StrEnum):
    HALF = 'hlf'
    TRIPLE = 'tpl'
    INC = 'inc'
    JUMP = 'jmp'
    JONE = 'jio'
    JEVEN = 'jie'


class Instruction:
    def __init__(self, line: str):
        parts = re.split(r',?\s+', line)
        self.register: str = ''
        self.offset: int = 1
        self.command: Command = Command(parts[0])
        match self.command:
            case Command.HALF | Command.TRIPLE | Command.INC:
                self.register = parts[1]
            case Command.JUMP:
                self.offset = int(parts[1])
            case Command.JEVEN | Command.JONE:
                register, offset = parts[1:]
                self.register = register
                self.offset = int(offset)

    def execute(self, registers: dict[str, int]) -> int:
        match self.command:
            case Command.HALF:
                registers[self.register] //= 2
            case Command.TRIPLE:
                registers[self.register] *= 3
            case Command.INC:
                registers[self.register] += 1
            case Command.JUMP:
                pass
            case Command.JONE:
                return self.offset if registers[self.register] == 1 else 1
            case Command.JEVEN:
                return self.offset if registers[self.register] % 2 == 0 else 1
            case _:
                raise TypeError(f'Unknown command! {self.command}')
        return self.offset

    def __repr__(self):
        return f'{self.__class__.__name__}(register={self.register}, offset={self.offset}, command={self.command.name})'


def parse_input(input_: str) -> list[Instruction]:
    return list(map(Instruction, input_.splitlines()))


INPUT = parse_input(Path('data/day23.txt').read_text())

TEST_INPUT = parse_input("""inc b
jio b, +2
tpl b
inc b""")


def solve(instructions: list[Instruction], a_start: int = 0) -> int:
    idx: int = 0
    registers: dict[str, int] = {'a': a_start, 'b': 0}
    while idx < len(instructions):
        idx += instructions[idx].execute(registers)
    return registers['b']


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [1]
    expected_2 = [(2, [TEST_INPUT, 1])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
