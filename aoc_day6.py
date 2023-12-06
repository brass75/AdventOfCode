#! /usr/bin/env python3
import re
from functools import reduce

input = '''Time:        41     77     70     96
Distance:   249   1362   1127   1011'''

test_input = '''Time:      7  15   30
Distance:  9  40  200'''


def parse_input(input: str, remove_spaces: bool = False) -> list[tuple]:
    times, distances = input.splitlines()
    if remove_spaces:
        times = re.sub('\s+', '', times)
        distances = re.sub('\s+', '', distances)
    times = list(map(int, re.findall(r'\d+', times)))
    distances = list(map(int, re.findall(r'\d+', distances)))

    return [(time, distance) for time, distance in zip(times, distances)]


def part_one(input: str = input):
    parsed_input = parse_input(input)
    options = []
    for time, distance in parsed_input:
        options.append(len([n for n in range(time + 1) if (run := time - n) and run * n > distance]))

    def multiply(x, y):
        return x * y
    print(f'part 1: {reduce(multiply, options)}')


def part_two(input: str = input):
    parsed_input = parse_input(input, remove_spaces=True)
    options = []
    for time, distance in parsed_input:
        options.append(len([n for n in range(time + 1) if (run := time - n) and run * n > distance]))
    print(f'Part 2: {options[0]}')


if __name__ == '__main__':
    part_one(test_input)
    part_two(test_input)

    part_one()
    part_two()

