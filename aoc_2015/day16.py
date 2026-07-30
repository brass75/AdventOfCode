from pathlib import Path

from aoc_lib import solve_problem

# This is the output of the MFCSAM that is global for everyone.
FORENSICS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


class Sue:
    """
    Class to define an individual Sue. The attributes of each Sue are assigned during the initialization based on what
    is present in that line since we don't have data for all the attributes for every Sue.
    """

    def __init__(self, line: str):
        number, properties = line.split(':', 1)
        self.number = int(number.split()[~0])
        for property in properties.split(','):
            name, value = property.split(':')
            setattr(self, name.strip(), int(value.strip()))


def parse_input(input_: str) -> list[Sue]:
    return list(map(Sue, input_.splitlines()))


INPUT = parse_input(Path('data/day16.txt').read_text())

TEST_INPUT = parse_input("""Sue 84: children: 3, akitas: 0, vizslas: 1
Sue 85: cats: 6, vizslas: 5, akitas: 2
Sue 86: cars: 3, akitas: 7, goldfish: 8
Sue 87: samoyeds: 8, vizslas: 3, goldfish: 8
Sue 88: vizslas: 4, children: 0, cats: 7
Sue 89: goldfish: 9, pomeranians: 10, samoyeds: 0
Sue 90: trees: 3, akitas: 0, cars: 2
Sue 91: samoyeds: 3, akitas: 7, perfumes: 10
Sue 1000: trees: 6, cats: 19, cars: 2, golfish: 1, pomeranians: 2""")


def less_than(x, y):
    return x < y


def greater_than(x, y):
    return x > y


def equals(x, y):
    return x == y


# For part 2 we can't do a simple equality check since some attributes require other checks. This maps the attributes
# that require other checks to those checks while allowing for a default equality check.
CHECKS = {
    'trees': greater_than,
    'cats': greater_than,
    'pomeranians': less_than,
    'goldfish': less_than,
}


def solve(sues: list[Sue], checks: dict = {}) -> int:
    """
    Solve the problem.

    :param sues: List of Sues.
    :param checks: Dictionary containg the checks at the attribute level.
    :return: The correct Aunt Sue.
    """
    for sue in sues:
        for attr, value in FORENSICS.items():
            if (
                (sue_val := getattr(sue, attr, None)) is not None  # If it doesn't have the attribute skip it.
                and not checks.get(attr, equals)(sue_val, value)  #  Perform the appropriate check. Default to equality.
            ):
                break
        else:
            return sue.number
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(90, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [CHECKS]
    expected_2 = [(1000, [TEST_INPUT, CHECKS])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
