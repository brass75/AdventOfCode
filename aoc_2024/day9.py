from aoc_lib import solve_problem

INPUT = open('data/day9.txt').read()

TEST_INPUT = """2333133121414131402\n"""

def checksum(nums: list[int | str]) -> int:
    return sum(i * v for i, v in enumerate(n for n in nums if n != '.'))


def solve(input_: str, whole_files: bool = False) -> int:
    file_system: list[int | str] = list()
    input_ = input_.strip()
    for n in range(0, len(input_), 2):
        file_id = n // 2
        file_size = int(input_[n])
        empty = int(input_[n + 1]) if n < (len(input_) - 1) else 0
        file_system.extend(file_id for _ in range(file_size))
        file_system.extend('.' for _ in range(empty))
    if not whole_files:
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


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(1928, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = [(2858, [TEST_INPUT, True])]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
