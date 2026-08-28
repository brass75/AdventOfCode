import re
from collections import Counter
from functools import cached_property
from pathlib import Path

from aoc_lib import solve_problem


class Room:
    def __init__(self, *, name: str, sector: str, checksum: str) -> None:
        self.name = name
        self.sector = int(sector)
        self.checksum = checksum

    @cached_property
    def is_valid(self) -> bool:
        counts = Counter(sorted(self.name.replace('-', '')))

        return ''.join([c[0] for c in counts.most_common(5)]) == self.checksum

    def decode(self) -> str:
        rotation = self.sector % 26
        a = ord('a')
        return ''.join(chr((ord(c) - a + rotation) % 26 + a) for c in self.name.replace('-', ''))


def parse_input(input_: str) -> list[Room]:
    return [
        Room(**entry.groupdict())
        for entry in re.finditer(r'((?P<name>[-a-z]+)-(?P<sector>\d+)\[(?P<checksum>[a-z]+)\])', input_)
    ]


INPUT = parse_input(Path('data/day4.txt').read_text())

TEST_INPUT = parse_input("""aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]""")

TEST_INPUT2 = parse_input('qzmt-zixmtkozy-ivhz-343[zimth]')


def solve(rooms: list[Room]) -> int:
    return sum(room.sector for room in rooms if room.is_valid)


def solve2(rooms: list[Room], term: str = 'north pole') -> int:
    # Since the decode removes the - which woould be spaces we need to remove the spaces
    term = term.replace(' ', '')
    for room in rooms:
        if room.is_valid and term in room.decode():
            return room.sector
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(1514, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = [(343, [TEST_INPUT2, 'very encrypted name'])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
