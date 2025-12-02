from collections.abc import Callable, Generator
from multiprocessing.pool import Pool

from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day2.txt').read()

TEST_INPUT = (
    '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,'
    '446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
)

CPUS = 10


def parse_input(input_: str) -> Generator:
    return (tuple(map(int, range.split('-'))) for range in input_.split(','))


def solve(input_: str, check: Callable, pool: Pool) -> int:
    return sum(pool.map(check, (pid for start, end in parse_input(input_) for pid in map(str, range(start, end + 1)))))


def check_2(pid: str) -> int:
    plen = len(pid)
    return (
        int(pid)
        if any(
            stop
            for stop in (n for n in range(1, (plen // 2) + 1) if plen % n == 0)
            if pid == pid[:stop] * (plen // stop)
        )
        else 0
    )


def check_1(pid: str) -> int:
    return int(pid) if len(pid) % 2 == 0 and pid[: len(pid) // 2] == pid[len(pid) // 2 :] else 0


if __name__ == '__main__':
    pool = Pool(CPUS)
    part1_args = [check_1, pool]
    expected_1 = [(1227775554, [TEST_INPUT, check_1, pool])]
    func_1 = solve

    part2_args = [check_2, pool]
    expected_2 = [(4174379265, [TEST_INPUT, check_2, pool])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
