#! /usr/bin/env python3
import re
from math import lcm

INPUT = open('data/day8.txt').read()


TEST_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_INPUT2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

TEST_INPUT3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


LINE_PATTERN = re.compile(r'([\dA-Z]{3}).*?\(([\dA-Z]{3}), ([\dA-Z]{3})\)')


def parse_input(input_: str) -> tuple[list, dict[str, tuple[str, str]]]:
    groups = input_.split('\n\n')
    instructions = list(groups[0])
    data_dict = {}
    for line in groups[1].splitlines():
        curr, left, right = LINE_PATTERN.search(line).groups()
        data_dict[curr] = (left, right)
    return instructions, data_dict


def get_next_location(options: tuple, instruction: str) -> str:
    match instruction:
        case 'R':
            return options[1]
        case 'L':
            return options[0]


def solve(input_: str, start: str = 'AAA', end: str = 'ZZZ'):
    count = 0
    instructions, data = parse_input(input_)

    curr = [s for s in data if s.endswith(start)]
    counts = []

    while curr:
        count += 1
        idx = (count - 1) % len(instructions)
        new_curr = []
        for location in curr:
            next_location = get_next_location(data[location], instructions[idx])
            if next_location.endswith(end):
                counts.append(count)
                continue
            new_curr.append(next_location)
        curr = new_curr

    print(f'Part {"2" if end == "Z" else "1"}: count={lcm(*counts)} {"[test]" if input_ != INPUT else ""}')


if __name__ == '__main__':
    solve(TEST_INPUT)
    solve(TEST_INPUT2)
    solve(TEST_INPUT3, 'A', 'Z')

    solve(INPUT)
    solve(INPUT, 'A', 'Z')
