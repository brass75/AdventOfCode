from collections.abc import Generator

from aoc_lib import solve_problem

INPUT = open('data/day9.txt').read()

TEST_INPUT = """2333133121414131402"""


def checksum(nums: list[int | str]) -> int:
    return sum(i * v for i, v in enumerate(nums) if v != '.')


def parse_input(input_: str) -> Generator[tuple[int, int, int]]:
    file_id = 0
    compressed = input_.strip()
    for n in range(0, len(compressed), 2):
        file_size = int(input_[n])
        empty = int(input_[n + 1]) if n < (len(compressed) - 1) else 0
        yield file_id, file_size, empty
        file_id += 1


def solve(input_: str) -> int:
    file_system: list[int | str] = list()
    for file_id, size, empty in parse_input(input_):
        file_system.extend(file_id for _ in range(size))
        file_system.extend('.' for _ in range(empty))
    j = len(file_system) - 1
    for i, c in enumerate(file_system):
        if c != '.':
            continue
        while file_system[j] == '.':
            j -= 1
        if i >= j:
            break
        file_system[i] = file_system[j]
        file_system[j] = '.'
    return checksum(file_system)


def solve2(input_: str) -> int:
    files, gaps, curr, file_id = dict(), list(), 0, 0
    for file_id, size, empty in parse_input(input_):
        files[file_id] = (curr, size)
        gaps.append((curr + size, empty))
        curr += size + empty
    max_id = file_id
    total = 0
    # We don't need to check the first file since there's nowhere for it to go.
    for file_id in range(max_id, 0, -1):
        start, size = files[file_id]
        # if size > max_gap:
        #     continue
        for i, (gap_start, gap_size) in enumerate(gaps):
            if gap_start > start:
                break
            if gap_size < size:
                continue
            # We need to update start here for the checksum to work
            start = gap_start
            gaps[i] = update_gap(gap_size, gap_start, size)
            files[file_id] = (start, size)
            break

        # Since we can't move the file again keep a running checksum so we don't need another loop.
        total += sum(map((lambda x: file_id * x), range(start, start + size)))
    return total


def update_gap(gap_size: int, gap_start: int, size: int) -> tuple[int, int]:
    """Compute the new gap size. If it's 0 put at position -1 to avoid using it for computations"""
    return (0, -1) if gap_size == size else (gap_start + size, gap_size - size)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(1928, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(2858, [TEST_INPUT])]
    func_2 = solve2

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
