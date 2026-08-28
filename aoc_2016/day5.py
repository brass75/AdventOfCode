from hashlib import md5

from aoc_lib import solve_problem

INPUT = 'uqwqemis'

TEST_INPUT = 'abc'


def solve(input_: str, position: bool = False) -> str:
    idx = 0
    chars = [''] * 8
    pos = 0
    while not all(chars):
        hashed = md5(f'{input_}{idx}'.encode()).hexdigest()
        if hashed.startswith('00000'):
            if position:
                try:
                    pos = int(hashed[5])
                except ValueError:
                    idx += 1
                    continue
                if pos < len(chars) and not chars[pos]:
                    chars[pos] = hashed[6]
            else:
                chars[pos] = hashed[5]
                pos += 1
        idx += 1
    return ''.join(chars)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [('18f47a30', [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [('05ace8e3', [TEST_INPUT, True])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
