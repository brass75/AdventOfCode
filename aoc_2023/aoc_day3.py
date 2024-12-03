#! /usr/bin/env python3

input = open('data/day3.txt').read()


NUMBERS = list(map(str, range(10)))
NOT_SYMBOLS = [*NUMBERS, '.']


def part_one():
    schematic = [list(line) for line in input.splitlines()]
    row_len = len(schematic[0]) + 2
    for i, row in enumerate(schematic):
        schematic[i] = ['.', *row, '.']
    schematic = [list('.' * row_len), *schematic, list('.' * row_len)]
    parts = []
    for i, line in enumerate(schematic):
        part = ''
        found = False
        for j, c in enumerate(line):
            if c in NUMBERS:
                part += c
                if not found:
                    adjacent = [
                        *schematic[i - 1][j - 1 : j + 2],
                        *schematic[i][j - 1 : j + 2],
                        *schematic[i + 1][j - 1 : j + 2],
                    ]
                    found = any(c for c in adjacent if c not in NOT_SYMBOLS)
            else:
                if found and part:
                    parts.append(int(part))
                found = False
                part = ''
    print(sum(parts))


def find_adjacent(line: list, center: int) -> list:
    found = []
    if line[center] not in NUMBERS:
        if line[center - 1] in NUMBERS:
            j = center
            while line[j - 1] in NUMBERS:
                j -= 1
            found.append(int(line[j:center]))
        if line[center + 1] in NUMBERS:
            j = center + 1
            while line[j] in NUMBERS:
                j += 1
            found.append(int(line[center + 1 : j]))
    else:
        i, j = center, center
        while line[i - 1] in NUMBERS:
            i -= 1
        while line[j] in NUMBERS:
            j += 1
        found.append(int(line[i:j]))
    return found


def part_two():
    schematic = [line for line in input.splitlines()]
    for i, row in enumerate(schematic):
        schematic[i] = str('.' + row + '.')
    row_len = len(schematic[0])
    schematic = ['.' * row_len, *schematic, '.' * row_len]
    total = 0
    for i, line in enumerate(schematic):
        for j, c in enumerate(line):
            if c != '*':
                continue
            adjacent = []
            for n in range(3):
                adjacent.extend(find_adjacent(schematic[i - 1 + n], j))
            if len(adjacent) == 2:
                total += adjacent[0] * adjacent[1]
    print(total)


part_one()
part_two()
