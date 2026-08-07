import copy
import heapq
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Any, Self

from aoc_lib import solve_problem


class OutOfMana(Exception):
    pass


class NoEffect(Exception):
    pass


class Result(Enum):
    player_win = auto()
    boss_win = auto()
    no_win = auto()


@dataclass(slots=True, kw_only=True)
class Effect:
    duration: int
    damage: int = 0
    armor: int = 0
    mana: int = 0

    def __eq__(self, value) -> bool:
        if type(self) is not type(value):
            return NotImplemented
        return self.damage == value.damage and self.armor == value.armor and self.mana == value.mana

    def __hash__(self):
        return hash((self.duration, self.armor, self.mana, self.damage))


@dataclass(slots=True, frozen=True, kw_only=True)
class Spell:
    cost: int
    damage: int = 0
    hp: int = 0
    effects: dict[str, Effect | None] = field(default_factory=lambda: {'self': None, 'other': None})

    def __lt__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.cost < other.cost and (self.damage > other.damage or self.effects.get('other'))

    def __hash__(self):
        return hash((self.cost, self.damage, self.hp, tuple(self.effects.items())))


@dataclass(slots=True)
class Player:
    hp: int
    damage: int = 0
    mana: int = 0
    spells: list = field(default_factory=list)
    effects: list = field(default_factory=list)

    def start_turn(self):
        for effect in self.effects:
            if effect.damage:
                self.hp -= effect.damage
            if effect.mana:
                self.mana += effect.mana
            effect.duration -= 1
        self.effects = [effect for effect in self.effects if effect.duration >= 1]
        return self.hp

    def attack(self, other):
        armor = sum([0, *(effect.armor for effect in other.effects)])
        other.hp -= max(1, self.damage - armor)

    def cast(self: Self, spell: Spell, other: Self):
        if self.mana < spell.cost:
            raise OutOfMana
        self.mana -= spell.cost
        if spell.hp:
            self.hp += spell.hp
        if spell.damage:
            other.hp -= spell.damage
        if effect_other := spell.effects.get('other'):
            if not any(effect_other == effect for effect in other.effects):
                other.effects.append(copy.deepcopy(effect_other))
            else:
                raise NoEffect
        if effect_self := spell.effects.get('self'):
            if not any(effect_self == effect for effect in self.effects):
                self.effects.append(copy.deepcopy(effect_self))
            else:
                raise NoEffect
        return spell.cost

    def __lt__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return self.hp < other.hp

    def __repr__(self):
        return f'{self.__class__.__name__}({self.hp=}, {self.mana=} {self.effects=})'

    def __hash__(self):
        return hash((self.hp, self.mana, tuple(effect for effect in self.effects)))


SPELL_LIST = [
    Spell(cost=53, damage=4),
    Spell(cost=73, damage=2, hp=2),
    Spell(cost=113, effects={'self': Effect(armor=7, duration=6)}),
    Spell(cost=173, effects={'other': Effect(damage=3, duration=6)}),
    Spell(cost=229, effects={'self': Effect(mana=101, duration=5)}),
]


PLAYER = Player(hp=50, mana=500, spells=SPELL_LIST)


def parse_input(input_: str) -> Any:
    hp, damage = map(int, (line.split(':')[~0].strip() for line in input_.splitlines()))
    return Player(hp=hp, damage=damage)


INPUT = parse_input(Path('data/day22.txt').read_text())

TEST_INPUT = parse_input("""hp: 0
damage: 0""")


def start_turn(player: Player, boss: Player) -> Result:
    if player.start_turn() <= 0:
        return Result.boss_win
    if boss.start_turn() <= 0:
        return Result.player_win
    return Result.no_win


def solve(BOSS: Player, mode: str = 'easy') -> int:
    q = [(0, copy.deepcopy(BOSS), copy.deepcopy(PLAYER), spell) for spell in PLAYER.spells]
    seen = set(q)
    mana_spent = 0
    while q:
        mana_spent, boss, player, spell = heapq.heappop(q)
        if mode == 'hard':
            player.hp -= 1
            if player.hp <= 0:
                continue
        match start_turn(player, boss):
            case Result.player_win:
                return mana_spent
            case Result.boss_win:
                continue
        try:
            mana_spent += player.cast(spell, boss)
        except OutOfMana, NoEffect:
            continue
        if boss.hp <= 0:
            return mana_spent
        match start_turn(player, boss):
            case Result.player_win:
                return mana_spent
            case Result.boss_win:
                continue
        boss.attack(player)
        if player.hp <= 0 or player.mana < min(spell.cost for spell in player.spells):
            continue
        q.extend(
            next_up
            for spell in player.spells
            if (
                spell.cost <= player.mana
                and (next_up := (mana_spent, copy.deepcopy(boss), copy.deepcopy(player), spell))
                and (next_up not in seen and not seen.add(next_up))
            )
        )
    return -1


if __name__ == '__main__':
    part1_args = []
    expected_1 = [(0, [TEST_INPUT])]  # [(<answer>, [<input>, *part1_args])]
    func_1 = solve

    part2_args = ['hard']
    expected_2 = [(0, [TEST_INPUT, 'hard'])]  # [<answer>, [(<input>, *part2_args)]]
    func_2 = solve

    if expected_1:
        for idx, (e_total, e_params) in enumerate(expected_1):
            solve_problem(func_1, 1, (idx + 1, e_total), *e_params)
        solve_problem(func_1, 1, None, INPUT, *part1_args)

    if expected_2:
        for idx, (e_total, e_params) in enumerate(expected_2):
            solve_problem(func_2, 2, (idx + 1, e_total), *e_params)
        solve_problem(func_2, 2, None, INPUT, *part2_args)
