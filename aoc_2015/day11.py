import re
import string
from functools import cache

from aoc_lib import solve_problem

INPUT = 'hepxcrrq'
TEST_INPUT = 'abcaabcb'

DISALLOWED_LETTERS = 'ilo'

@cache
def increment_latter(char: str) -> str:
    """Get the net letter"""
    return next_letter if (next_letter := chr(ord(char) + 1)) in string.ascii_lowercase else 'a'


def sequence(value: str) -> bool:
    """Check for a sequence of 3 consecutive letters"""
    for i in range(len(value) - 2):
        if (
            ord(value[i]) == ord(value[i+1]) -1 and
            ord(value[i]) == ord(value[i+2]) - 2
        ):
            return True
    return False


def ignored_letter(value: str) -> bool:
    """Check for any disallowed letters"""
    return not any(c in DISALLOWED_LETTERS for c in value)


def double_letter(value: str) -> bool:
    """Check for 2 pairs of double letters"""
    return len(re.findall(r'(.)\1', value)) >= 2


def solve(password: str) -> str:
    c: str
    while True:
        pass_list: list[str] = list(password[::-1])  # Got from the right so we need to reverse it.
        i: int = 0
        for c in pass_list:
            if (c := increment_latter(c)) == 'a':
                # If we rolled the letter over we then proceed to the next letter in the password
                pass_list[i] = c
                i += 1
            else:
                # Check the password for validity and return if valid
                pass_list[i] = c
                password = ''.join(pass_list[::-1])
                for check in [double_letter, sequence, ignored_letter]:
                    if not check(password):
                        break
                else:
                    return password
                break

if __name__ == '__main__':
    part1_args = [INPUT]
    # [(<answer>, [<input>, *part1_args])]
    expected_1 = [('abcaabcc', [TEST_INPUT])]
    func_1 = solve

    part2_args = [solve(INPUT)]
    expected_2 = [('abcaabcc', [TEST_INPUT])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, *part2_args)
