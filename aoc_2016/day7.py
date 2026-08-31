import re
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[str]:
    return input_.splitlines()


INPUT = parse_input(Path('data/day7.txt').read_text())

TEST_INPUT = parse_input("""abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn""")

TEST_INPUT2 = parse_input("""aba[bab]xyz
xyx[xyx]xyx
aaa[kek]abaeke
zazbz[bzbaaazbz]cdb
zazbz[bbb]cdb""")


BAD_PATTERN = re.compile(r'[\[][^]]*(([a-z])([a-z])(?<!\2)\3\2)')
FULL_PATTERN = re.compile(r'[^[]*(([a-z])([a-z])(?<!\2)\3\2)')


def solve(addresses: list[str]) -> int:
    return sum(map(bool, map(FULL_PATTERN.search, (a for a in addresses if not BAD_PATTERN.search(a)))))


def ssl_check(address: str) -> bool:
    """
    Check an address for SSL support. An address supports SSL if:
        - There is a triplet of letters matching an "aba" pattern in a supernet sequence (not enclosed in brackets)
        - There is a corresponding triplet matching a "bab" pattern in a hypernet sequence (enclosed in brackets)

    Note: Can't use regex for the supernet check because it will not match on "zazbz" for both "zaz" and "zbz". Regex is
    fine fort the hypernet check because we are looking for specific letterrs and not just an "aba" pattern.

    :param address: The address to check.
    :return: True if SSL is supported else False.
    """
    return any(
        section[i + 2] == a and (b := section[i + 1]) != a and re.search(rf'\[[a-z]*{b}{a}{b}[a-z]*\]', address)
        for section in re.split(r'\[[a-z]*\]', address)
        for i, a in enumerate(section[:~1])
    )


def solve2(addresses: list[str]) -> int:
    return sum(map(ssl_check, addresses))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(2, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(3, [TEST_INPUT2])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
