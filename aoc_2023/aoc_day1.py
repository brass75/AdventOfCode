#! /usr/bin/env python3

input = open('data/day1.txt').read()


def part_one():
    digits = [[c for c in s if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']] for s in input.split('\n')]
    converted = list(map(int, (f'{group[0]}{group[-1]}' for group in digits)))
    print(f'Part 1: {sum(converted)}')


def part_two():
    num_words = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    digits = []
    for line in input.split('\n'):
        curr = []
        while line:
            for word, value in num_words.items():
                if line.startswith(word):
                    curr.append(value)
                    break
            else:
                try:
                    curr.append(int(line[0]))
                except Exception:
                    pass
            line = line[1:]
        digits.append(curr)

    converted = list(map(int, (f'{group[0]}{group[-1]}' for group in digits)))

    print(f'Part 2: {sum(converted)}')


part_one()
part_two()
