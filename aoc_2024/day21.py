import functools

from aoc_lib import solve_problem

INPUT = open('data/day21.txt').read()

TEST_INPUT = """029A
980A
179A
456A
379A"""


# The mappings are defined globally to allow for memoization
def get_mappings(keypad: dict, invalid_coords) -> dict:
    mappings = {}
    for a, (x1, y1) in keypad.items():
        for b, (x2, y2) in keypad.items():
            path = '<' * (y1 - y2) + 'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
            if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
                path = path[::-1]
            mappings[(a, b)] = path + 'A'
    return mappings


NUMPAD = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2),
}
DIRPAD = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}

DIR_MAPPINGS = get_mappings(DIRPAD, (0, 0))
NUM_MAPPINGS = get_mappings(NUMPAD, (3, 0))


@functools.cache
def get_presses(buttons: str, keypads: int, map_type: str = 'dir') -> int:
    # Since the mappings are a dictionary we can't pass them in and memoize
    mappings = DIR_MAPPINGS if map_type == 'dir' else NUM_MAPPINGS
    code = 'A' + buttons
    # Return the length of the sequence when we've run out of keypads otherwise
    # recursively build the sequence till we get it to the end.
    return (
        len(buttons)
        if keypads == 0
        else sum(get_presses(mappings[code[i], code[i + 1]], keypads - 1) for i in range(len(buttons)))
    )


def solve(input_: str, keypads: int = 2) -> int:
    codes: list[str] = input_.splitlines()
    return sum(int(code[:-1]) * get_presses(code, keypads + 1, map_type='num') for code in codes)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(126384, [TEST_INPUT])]
    func_1 = solve

    part2_args = [25]
    expected_2 = [(126384, [TEST_INPUT])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
