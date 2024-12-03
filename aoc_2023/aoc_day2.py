#! /usr/bin/env python3

import re

input = open('data/day2.txt').read()

GAME_PATTERN = re.compile(r'Game (\d+):')
COLOR_PATTERNS = r'\d+'
MAPPINGS = {'red': 12, 'green': 13, 'blue': 14}


def part_one():
    total = 0
    for line in input.splitlines():
        game = int(GAME_PATTERN.search(line).group(1))
        for color, max_value in MAPPINGS.items():
            if max(map(int, re.findall(rf'({COLOR_PATTERNS}) {color}', line))) > max_value:
                break
        else:
            total += game

    print(f'Part 1: {total}')


def part_two():
    line_power = []
    for line in input.splitlines():
        line_vals = (max(map(int, re.findall(rf'({COLOR_PATTERNS}) {color}', line))) for color in MAPPINGS)
        power = 1
        for line_val in line_vals:
            power *= line_val
        line_power.append(power)
    print(f'Part 2: {sum(line_power)}')


part_one()
part_two()
