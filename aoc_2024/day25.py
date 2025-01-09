from aoc_lib import solve_problem

INPUT = open('data/day25.txt').read()

TEST_INPUT = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def parse_lock(lock: str) -> list[int]:
    lock_lines = lock.splitlines()
    cols = [0] * len(lock_lines[0])
    # Skip the first list - for a lock it doesn't contribute and for a key it's all '.'
    for line in lock_lines[1:]:
        for j,c  in enumerate(line):
            cols[j] += c == '#'
    return cols


def parse_input(input_: str) -> tuple[list, list, int]:
    keys, locks = list(), list()
    key_locks = input_.split('\n\n')
    for key_lock in key_locks:
        if key_lock[0] == '#':
            locks.append(parse_lock(key_lock))
        else:
            keys.append(parse_lock(key_lock))
    return locks, keys, len(key_locks[0].splitlines())


def solve(input_: str) -> int:
    locks, keys, height = parse_input(input_)
    return sum(all(kc + lc < height for kc, lc in zip(key, lock)) for lock in locks for key in keys)


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(3, [TEST_INPUT])]
    func_1 = solve

    part2_args = []
    expected_2 = []
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
