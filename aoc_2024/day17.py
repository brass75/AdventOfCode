import functools
import re

from aoc_lib import solve_problem

INPUT = open('data/day17.txt').read()

TEST_INPUT = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


TEST_INPUT2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


def parse_input(input_: str) -> tuple:
    registers, instructions = input_.split('\n\n')
    registers = tuple(int(x) for x in re.findall(r'\d+', registers))
    program = [int(n) for n in re.findall(r'(\d+)', instructions)]
    instructions = list()
    for i in range(0, len(program), 2):
        instructions.append((program[i], program[i + 1]))
    return registers, instructions, program


def get_operand(operand: int, registers) -> int:
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4 | 5 | 6:
            return registers[operand - 4]
        case _:
            raise RuntimeError(f'Invalid operand {operand}')


@functools.cache
def run_instruction(a: int, b: int, c: int, instruction: int, operand: int) -> tuple[int, int, int]:
    match instruction:
        case 0:
            a = a // (2 ** get_operand(operand, (a, b, c)))
        case 1:
            b = b ^ operand
        case 2:
            b = get_operand(operand, (a, b, c)) % 8
        case 4:
            b = b ^ c
        case 6:
            b = a // (2 ** get_operand(operand, (a, b, c)))
        case 7:
            c = a // (2 ** get_operand(operand, (a, b, c)))
    return a, b, c


def run_code(a: int, b: int, c: int, instructions: list) -> list[int]:
    """Loop through the program and execute the instructions."""
    i = 0
    registers = (a, b, c)
    rc = list()
    while i < len(instructions):
        instruction, operand = instructions[i]
        match instruction:
            case 3:
                # Jump if a != 0 otherwise continue.
                if registers[0]:
                    i = operand
                    continue
            case 5:
                rc.append(get_operand(operand, registers) % 8)
            case _:
                # The rest of the instructions are outsourced to allow for memoization
                registers = run_instruction(*registers, instruction, operand)
        i += 1
    return rc


def find(a: int, i: int, instructions: list, program: list) -> int:
    """Starting af the back, fill in the program"""
    if (res := run_code(a, 0, 0, instructions)) == program:
        # Found it - return it.
        return a
    if res == program[-i:] or not i:
        # Found the digit, let's work on the next. Since everything is % 8 we'll multiply a by 8 to get the answer
        return min((x for n in range(8) if (x := find((8 * a) + n, i + 1, instructions, program))), default=None)


def solve(input_: str, part2: bool = False) -> str | int:
    (a, b, c), instructions, program = parse_input(input_)
    if not part2:
        return ','.join(map(str, run_code(a, b, c, instructions)))
    return find(0, 0, instructions, program)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [('4,6,3,5,6,3,5,2,1,0', [TEST_INPUT])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(117440, [TEST_INPUT2, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
