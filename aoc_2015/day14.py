import re
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

from aoc_lib import solve_problem


@dataclass(slots=True)
class Reindeer:
    velocity: int
    duration: int
    rest: int
    score: int = 0
    _time: int = 0

    @property
    def time(self) -> int:
        return self._time

    @time.setter
    def time(self, value: int):
        self._time = value

    @property
    def cycle(self) -> int:
        return self.duration + self.rest

    def get_distance(self, total_time: int) -> int:
        """
        Get the distance traveled over a period of time.

        :param total_time: Time traveled
        :return: Distance traveled
        """
        cycles = self.time // self.cycle
        overage = self.time % self.cycle
        return ((cycles * self.duration) + min(self.duration, overage)) * self.velocity

    def __iter__(self) -> Iterator[int]:
        """
        Get distance traveled by second

        :param total_time: Duration of the race.
        :return: List of how far the reindeer has traveled through that second.
        """
        traveled = 0
        seconds = 0
        while True:
            place = seconds % self.cycle
            if place < self.duration:
                traveled += self.velocity
            yield traveled
            seconds += 1

    def add_point(self):
        self.score += 1


def parse_input(input_: str) -> list[Reindeer]:
    return [
        Reindeer(*map(int, match.groups()))
        for match in re.finditer(r'.*?(\d+)\skm/s\sfor\s(\d+).*?(\d+)\sseconds.', input_)
    ]


INPUT = parse_input(Path('data/day14.txt').read_text())

TEST_INPUT = parse_input("""Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.""")


def solve(input_: list[Reindeer], total_time: int) -> int:
    for reindeer in input_:
        reindeer.time = total_time
    return max(reindeer.get_distance(total_time + 1) for reindeer in input_)


def solve2(reindeers: list[Reindeer], total_time: int) -> int:
    for reindeer in reindeers:
        reindeer.time = total_time
    iterators = [iter(reindeer) for reindeer in reindeers]
    for _ in range(total_time + 1):
        max_traveled = 0
        winners = []
        for i, iterator in enumerate(iterators):
            if (curr := next(iterator)) > max_traveled:
                max_traveled = curr
                winners = [i]
            elif curr == max_traveled:
                winners.append(i)
        for winner in winners:
            reindeers[winner].add_point()

    return max(reindeer.score for reindeer in reindeers)


if __name__ == '__main__':
    part1_args = [2503]
    expected_1 = [(1120, [TEST_INPUT, 1000])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [2503]
    expected_2 = [(689, [TEST_INPUT, 1000])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
