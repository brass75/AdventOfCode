#! /usr/bin/env python3

import re

input = open('data/day5.txt').read()

# input = '''seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4'''

KEYS = ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']


# I tried but I couldn't figure it out. Used
# https://github.com/morgoth1145/advent-of-code/blob/5311ed667714398cf02d9b2bc2a4e88f53f7b0dc/2023/05/solution.py
# to help.
def get_seed_data(data, len_func) -> int:
    groups = data.split('\n\n')
    seed_ranges = len_func(list(map(int, re.findall(r'\d+', groups[0]))))
    for group in groups[1:]:
        mappings = [tuple(map(int, re.findall(r'\d+', line))) for line in group.splitlines()[1:]]

        new_ranges = []
        for start, seed_len in seed_ranges:
            while seed_len:
                best_dist = seed_len
                for dest, source, length in mappings:
                    if source <= start < source + length:
                        offset = start - source
                        remaining_length = min(length - offset, seed_len)
                        new_ranges.append((dest + offset, remaining_length))
                        start += remaining_length
                        seed_len -= remaining_length
                        break
                    elif start < source:
                        best_dist = min(source - start, best_dist)
                else:
                    new_length = min(best_dist, seed_len)
                    new_ranges.append((start, new_length))
                    start += new_length
                    seed_len -= new_length
        seed_ranges = new_ranges
    return min(x for x, _ in seed_ranges)


def part_one():
    print(f'part_one: {get_seed_data(input, lambda list_: [(n, 1) for n in list_])}')


def part_two():
    print(f'part_two: {get_seed_data(input, lambda list_: list(zip(list_[::2], list_[1::2])))}')


if __name__ == '__main__':
    part_one()
    part_two()
