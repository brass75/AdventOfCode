from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[str]:
    return input_.splitlines()


INPUT = parse_input(Path('data/day2.txt').read_text())

TEST_INPUT = parse_input("""ULL
RRDDD
LURDL
UUUUD""")


NUMPAD: dict[str, dict[str, str]] = {
    '1': {
        'U': '1',
        'R': '2',
        'D': '4',
        'L': '1',
    },
    '2': {
        'U': '2',
        'R': '3',
        'D': '5',
        'L': '1',
    },
    '3': {
        'U': '3',
        'R': '3',
        'D': '6',
        'L': '2',
    },
    '4': {
        'U': '1',
        'R': '5',
        'D': '7',
        'L': '4',
    },
    '5': {
        'U': '2',
        'R': '6',
        'D': '8',
        'L': '4',
    },
    '6': {
        'U': '3',
        'R': '6',
        'D': '9',
        'L': '5',
    },
    '7': {
        'U': '4',
        'R': '8',
        'D': '7',
        'L': '7',
    },
    '8': {
        'U': '5',
        'R': '9',
        'D': '8',
        'L': '7',
    },
    '9': {
        'U': '6',
        'R': '9',
        'D': '9',
        'L': '8',
    },
}


NUMPAD2: dict[str, dict[str, str]] = {
    '1': {
        'U': '1',
        'R': '1',
        'D': '3',
        'L': '1',
    },
    '2': {
        'U': '2',
        'R': '3',
        'D': '6',
        'L': '2',
    },
    '3': {
        'U': '1',
        'R': '4',
        'D': '7',
        'L': '2',
    },
    '4': {
        'U': '4',
        'R': '4',
        'D': '8',
        'L': '3',
    },
    '5': {
        'U': '5',
        'R': '6',
        'D': '5',
        'L': '5',
    },
    '6': {
        'U': '2',
        'R': '7',
        'D': 'A',
        'L': '5',
    },
    '7': {
        'U': '3',
        'R': '8',
        'D': 'B',
        'L': '6',
    },
    '8': {
        'U': '4',
        'R': '9',
        'D': 'C',
        'L': '7',
    },
    '9': {
        'U': '9',
        'R': '9',
        'D': '9',
        'L': '8',
    },
    'A': {
        'U': '6',
        'R': 'B',
        'D': 'A',
        'L': 'A',
    },
    'B': {
        'U': '7',
        'R': 'C',
        'D': 'D',
        'L': 'A',
    },
    'C': {
        'U': '8',
        'R': 'C',
        'D': 'C',
        'L': 'B',
    },
    'D': {
        'U': 'B',
        'R': 'D',
        'D': 'D',
        'L': 'D',
    },
}


def solve(directions: list[str], numpad: dict[str, dict[str, str]] = NUMPAD) -> str:
    answer = ''
    current = '5'
    for row in directions:
        for c in row:
            current = numpad[current][c]
        answer += current
    return answer


if __name__ == '__main__':
    part1_args = []
    expected_1 = [('1985', [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [NUMPAD2]
    expected_2 = [('5DB3', [TEST_INPUT, *part2_args])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
