from collections import Counter
from pathlib import Path

from aoc_lib import solve_problem


def parse_input(input_: str) -> list[str]:
    return input_.splitlines()


INPUT = parse_input(Path('data/day6.txt').read_text())

TEST_INPUT = parse_input("""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""")


def solve(lines: list[str], common: int = 0) -> str:
    message: list[str] = []
    for n in range(len(lines[0])):
        counts = Counter(line[n] for line in lines)
        message.append(counts.most_common()[common][0])
    return ''.join(message)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [('easter', [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [-1]
    expected_2 = [('easter', [TEST_INPUT])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
