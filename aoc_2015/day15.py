import re
from collections import Counter
from dataclasses import dataclass
from functools import partial, reduce
from itertools import combinations_with_replacement
from multiprocessing import Pool
from pathlib import Path

from aoc_lib import solve_problem


@dataclass(slots=True, frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parse_input(input_: str) -> list[Ingredient]:
    ingredients = []
    for match in re.finditer(r'(.*?):.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', input_):
        name, *properties = match.groups()
        ingredients.append(Ingredient(name, *map(int, properties)))
    return ingredients


INPUT = parse_input(Path('data/day15.txt').read_text())

TEST_INPUT = parse_input("""Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""")


def solve_combination(total_calories: int, combo: tuple[Ingredient, ...]) -> int:
    counts = Counter(combo)
    if total_calories and sum(ingredient.calories * count for ingredient, count in counts.items()) != total_calories:
        return 0
    vals = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0,
    }
    vals = {attr: sum(getattr(ingredient, attr) * count for ingredient, count in counts.items()) for attr in vals}
    return reduce(lambda x, y: x * y, (val if val > 0 else 0 for val in vals.values()))


def solve(ingredients: list[Ingredient], total_calories: int = 0) -> int:
    solve_part = partial(solve_combination, total_calories)
    with Pool(20) as pool:
        return max(pool.map(solve_part, combinations_with_replacement(ingredients, r=100)))


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(62842880, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = [500]
    expected_2 = [(57600000, [TEST_INPUT, 500])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
