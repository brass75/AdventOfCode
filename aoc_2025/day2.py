from aoc_lib import solve_problem

# TODO Point this to the correct day!
INPUT = open('data/day2.txt').read()

TEST_INPUT = ("11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,"
              "446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")

def parse_input(input_: str) -> list[tuple[int, int]]:
    ranges = list()
    for range in input_.split(','):
        ranges.append(tuple(map(int, range.split('-'))))
    return ranges

def solve(input_: str) -> int:
    matches = list()
    for start, end in parse_input(input_):
        for pid in map(str, range(start, end + 1)):
            if len(pid) % 2 != 0:
                # If the length of the ID is odd no need to check, it can't contain it.
                continue
            if pid[:len(pid) // 2] == pid[len(pid) // 2:]:
                matches.append(int(pid))
    return sum(matches)

if __name__ == '__main__':
    part1_args = []
    expected_1 = [(1227775554, [TEST_INPUT])]
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
