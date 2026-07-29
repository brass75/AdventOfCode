import re
from collections.abc import Iterable
from itertools import permutations
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> dict[str, dict[str, int]]:
    people = {}
    for match in re.finditer(r'([A-Za-z]+).*?(gain|lose)\s(\d+).*?([A-Za-z]+)\.', input_):
        person, change, value, adjacent = match.groups()
        value = int(value)
        if change == 'lose':
            value *= -1
        people.setdefault(person, dict())[adjacent] = value

    return people


INPUT = parse_input(Path('data/day13.txt').read_text())

TEST_INPUT = parse_input("""Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.""")


def solve(input_: dict[str, dict[str, int]], add_me: bool = False) -> int:
    def evaluate_group(group: Iterable, people: dict[str, dict[str, int]]) -> int:
        """
        Solve for the happiness change for a given permutation.

        :param group: The permutation to check.
        :param people: The dictionary with the definitions.
        :return: Overall happiness change for that permutation.
        """
        group = list(group)
        total = 0
        for idx, person in enumerate(group):
            current = people[person]
            left = idx - 1
            right = (idx + 1) % len(group)
            total += current.get(group[left], 0)
            total += current.get(group[right], 0)
        return total

    if add_me:
        input_['me'] = {}
    return max(evaluate_group(group, input_) for group in permutations(input_.keys()))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(330, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [True]
    expected_2 = [(286, [TEST_INPUT, True])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
