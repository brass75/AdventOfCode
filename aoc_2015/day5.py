import re
import string
from abc import abstractmethod
from pathlib import Path
from typing import Any

from aoc_lib import solve_problem


def parse_input(input_: str) -> Any:
    return input_.strip().splitlines()


INPUT = parse_input(Path('data/day5.txt').read_text())

TEST_INPUT = parse_input("""ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb""")

TEST_INPUT2 = parse_input("""qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy""")

INVALID_PAIRS: list[str] = ['ab', 'cd', 'pq', 'xy']
VOWELS = 'aeiou'


class Check:
    """Base class for checking a string."""

    @staticmethod
    @abstractmethod
    def test(input_: str) -> bool: ...


class Vowels(Check):
    """Checks that the string contains at least 3 vowels."""

    @staticmethod
    def test(input_: str) -> bool:
        return len([c for c in input_ if c in VOWELS]) >= 3


class Doubles(Check):
    """Checks that the string containts double letters."""

    @staticmethod
    def test(input_: str) -> bool:
        pattern = '|'.join(c * 2 for c in string.ascii_lowercase)
        return bool(re.search(pattern, input_))


class InvalidPairs(Check):
    """Checks that the string does not contain any invalid pairs."""

    @staticmethod
    def test(input_: str) -> bool:
        return not any(s in input_ for s in INVALID_PAIRS)


class DoublePair(Check):
    """Checks that the string contains at least one pair of letters that repeats."""

    @staticmethod
    def test(input_: str) -> bool:
        for i in range(len(input_) - 2):
            if input_[i : i + 2] in input_[i + 2 :]:
                return True
        return False


class RepeatsWithSpace(Check):
    """Checks that there is at least one letter that is found again following a single letter."""

    @staticmethod
    def test(input_: str) -> bool:
        for i in range(len(input_) - 2):
            if input_[i] == input_[i + 2]:
                return True
        return False


def solve(input_: Any, checks: list[Check]) -> int:
    return sum(all(check.test(s) for check in checks) for s in input_)


if __name__ == '__main__':
    part1_args = [[InvalidPairs(), Vowels(), Doubles()]]
    expected_1 = [(2, [TEST_INPUT, *part1_args])]
    func_1 = solve

    part2_args = [[DoublePair(), RepeatsWithSpace()]]
    expected_2 = [(2, [TEST_INPUT2, *part2_args])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
