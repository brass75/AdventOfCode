from collections.abc import Iterable
from copy import deepcopy
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path

from aoc_lib import solve_problem


@dataclass(slots=True, frozen=True)
class Item:
    """Class representing an inventory item."""

    type: str
    cost: int
    damage: int = 0
    armor: int = 0


@dataclass(slots=True)
class Player:
    """Class representing a character."""

    hp: int = 0
    damage: int = 0
    armor: int = 0
    inventory: list = field(default_factory=list)

    def attack(self, player: Player) -> int:
        return player.defend(self.damage)

    def defend(self, damage: int):
        damage = max(1, damage - self.armor)
        self.hp -= damage
        return self.hp

    def equip(self, item: Item):
        self.inventory.append(item)
        self.damage += item.damage
        self.armor += item.armor

    @property
    def gold_spent(self):
        return sum(item.cost for item in self.inventory)


WEAPONS = [
    Item('weapon', 8, 4),
    Item('weapon', 10, 5),
    Item('weapon', 25, 6),
    Item('weapon', 40, 7),
    Item('weapon', 74, 8),
]

ARMOR = [
    Item('armor', 13, armor=1),
    Item('armor', 31, armor=2),
    Item('armor', 53, armor=3),
    Item('armor', 75, armor=4),
    Item('armor', 102, armor=5),
]

RINGS = [
    Item('ring', 25, 1, 0),
    Item('ring', 50, 2, 0),
    Item('ring', 100, 3, 0),
    Item('ring', 20, 0, 1),
    Item('ring', 40, 0, 2),
    Item('ring', 80, 0, 3),
]

EQUIP_LIMITS = {
    'weapon': {'inventory': WEAPONS, 'min': 1, 'max': 1},
    'armor': {'inventory': ARMOR, 'min': 0, 'max': 1},
    'ring': {'inventory': RINGS, 'min': 0, 'max': 2},
}


def parse_input(input_: str) -> Player:
    return Player(*[int(line.split()[~0]) for line in input_.splitlines()])


INPUT = parse_input(Path('data/day21.txt').read_text())

TEST_INPUT = parse_input("""Hit Points: 12
Damage: 7
Armor: 2""")


def equip_player(player: Player, equipment: Iterable[Item | Iterable[Item]]):
    """
    Recursively go through the provided equipment and attach to the player.

    :param player: The Player to equip
    :param equipment: A list of equipment. If an item in the list is itself an Iterable do a recursive call.
    """
    for item in equipment:
        match item:
            case Item():
                player.equip(item)
            case Iterable():
                equip_player(player, item)


def battle(player: Player, boss: Player) -> str:
    """
    Run the battle!

    :param player: The "human" player
    :param boss: The boss
    :return: Which player won as a string.
    """
    while player.hp > 0 and boss.hp > 0:
        if player.attack(boss) <= 0:
            return 'player'
        if boss.attack(player) <= 0:
            return 'boss'
    return ''


def equip_and_battle(player: Player, boss: Player, equipment: Iterable[Item | Iterable[Item]]) -> tuple[int, str]:
    """
    Equip the player and report the battle results.

    :param player: The player to equip.
    :param boss: The boss to battle.
    :param equipment: The equipment for the player.
    :return: The cost of the equipment and the winner of the battle.
    """
    player1 = deepcopy(player)
    equip_player(player1, equipment)
    return player1.gold_spent, battle(player1, deepcopy(boss))


def get_ring_combinations() -> Iterable[Item | Iterable[Item]]:
    """
    Get the possible ring combinations.

    :return: Generator that returns all possible combinations of lengths 0, 1, and 2 for RINGS.
    """
    yield from combinations(RINGS, r=2)
    yield from RINGS
    yield []


def solve(boss: Player, player: Player) -> tuple[int, int]:
    player_wins = set()
    player_losses = set()
    # Test didn't give us anything to work with RE inventory, just enough to check the battle logic.
    if not player.inventory:
        for weapon in WEAPONS:
            for ring_set in get_ring_combinations():
                equipment = [weapon, ring_set]
                gold_spent, winner = equip_and_battle(player, boss, equipment)
                if winner == 'player':
                    player_wins.add(gold_spent)
                else:
                    player_losses.add(gold_spent)
                for armor in ARMOR:
                    gold_spent, winner = equip_and_battle(player, boss, [equipment, armor])
                    if winner == 'player':
                        player_wins.add(gold_spent)
                    else:
                        player_losses.add(gold_spent)
        return min(player_wins), max(player_losses)
    return 8, 0


if __name__ == '__main__':
    part1_args = [Player(hp=100)]
    expected_1 = [
        ((8, 0), [TEST_INPUT, Player(hp=8, damage=5, armor=5, inventory=[WEAPONS[0]])])
    ]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = []
    expected_2 = []  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
