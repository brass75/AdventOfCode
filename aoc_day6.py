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


def get_num_options(time: int, distance: int) -> int:
    least, most = 0, 0
    for n in range(time + 1):
        if (time - n) * n > distance:
            least = n
            break
    for n in range(time + 1, 0, -1):
        if (time - n) * n > distance:
            most = n
            break
    return most - least + 1


def part_one(input: str = input):
    parsed_input = parse_input(input)
    options = [get_num_options(time, distance) for time, distance in parsed_input]

    def multiply(x, y):
        return x * y
    print(f'part 1: {reduce(multiply, options)}')


def part_two(input: str = input):
    parsed_input = parse_input(input, remove_spaces=True)
    time, distance = parsed_input[0]
    print(f'Part 2: {get_num_options(time, distance)}')


if __name__ == '__main__':
    part_one(test_input)
    part_two(test_input)

    part_one()
    part_two()

