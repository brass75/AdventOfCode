#! /usr/bin/env python3

import re

input = open('data/day4.txt').read()

# input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''


def parse_input() -> list:
    lines = []
    for line in input.splitlines():
        match = re.search(r'([\d\s]+)\|([\d\s]+)', line)
        winning, mine = (re.split(r'\s+', s.strip()) for s in match.groups())
        lines.append({'winning': winning, 'mine': mine, 'count': 1})
    return lines


def part_one():
    parsed_lines = parse_input()
    total = 0
    for line in parsed_lines:
        winning = set(line['winning'])
        if overlap := winning.intersection(line['mine']):
            total += 2 ** (len(overlap) - 1)
    print(f'part 1: {total}')


def part_two():
    lines = parse_input()
    for i, line in enumerate(lines):
        winning = set(line['winning'])
        overlap = winning.intersection(line['mine'])
        for n in range(len(overlap)):
            lines[i + n + 1]['count'] += line['count']
    total = sum(line['count'] for line in lines)
    print(f'part 2: {total}')


part_one()
part_two()
