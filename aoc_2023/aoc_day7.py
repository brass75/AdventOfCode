#!/usr/bin/env python3
import copy
from collections import Counter, defaultdict

INPUT = open('data/day7.txt').read()

TEST_INPUT = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
HAND_RANKS = {
    'hc': 0,
    '1p': 1,
    '2p': 2,
    '3k': 3,
    'fh': 4,
    '4k': 5,
    '5k': 6,
}


class Card:
    def __init__(self, card: str, use_joker: bool = False):
        self.card = card
        self.use_joker = use_joker

    @property
    def value(self) -> int:
        if self.use_joker and self.card == 'J':
            return -1
        return CARDS.index(self.card)

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.card == other.card

    def __hash__(self):
        return hash(self.card)

    def __repr__(self):
        return f'Card(card={self.card}, use_joker={self.use_joker})'

    def __str__(self):
        if self.use_joker and self.card == 'J':
            return '?'
        return self.card


class Hand:
    def __init__(self, hand: str, use_joker: bool = False):
        self.hand = list(map(Card, hand, (use_joker for _ in range(len(hand)))))
        self.orig = hand
        self.use_joker = use_joker

    def __repr__(self):
        return f'Hand(hand={self.orig}, use_joker={self.use_joker})'

    def __str__(self):
        return ''.join(map(str, self.hand))

    def __gt__(self, other):
        for i in range(len(self.hand)):
            if self.hand[i] == other.hand[i]:
                continue
            return self.hand[i] > other.hand[i]


def parse_input(input_: str, use_joker: bool = False) -> list[tuple]:
    splitlines = [line.split() for line in input_.splitlines()]
    return [(Hand(hand, use_joker), int(bid)) for hand, bid in splitlines]


def get_hand_rank(hand: Hand) -> int:
    card_count = Counter(hand.hand)
    if hand.use_joker:
        _hand = copy.deepcopy(hand)
        if (jokers := card_count.pop(Card('J'), 0)) == 5:
            return HAND_RANKS['5k']
        high_count = max(card_count.items(), key=lambda x: (x[1], x[0]))
        card_count[high_count[0]] += jokers
    match len(card_count):
        case 1:
            return HAND_RANKS['5k']
        case 2:
            if 1 in card_count.values():
                return HAND_RANKS['4k']
            return HAND_RANKS['fh']
        case 3:
            if 3 in card_count.values():
                return HAND_RANKS['3k']
            return HAND_RANKS['2p']
        case 4:
            return HAND_RANKS['1p']
    return HAND_RANKS['hc']


def solve(input_: str, use_jokers: bool = False):
    parsed_input = parse_input(input_, use_jokers)
    ranked_hands = defaultdict(list)
    for hand, bid in parsed_input:
        ranked_hands[get_hand_rank(hand)].append((hand, bid))
    i = 1
    total = 0
    for _, hands in sorted(ranked_hands.items(), key=lambda x: x[0]):
        for _, bid in sorted(hands, key=lambda x: x[0]):
            total += i * bid
            i += 1

    print(f'Part one: {total} (input={"test" if input_ == TEST_INPUT else "real"}, {use_jokers=})')


if __name__ == '__main__':
    solve(TEST_INPUT)
    solve(TEST_INPUT, use_jokers=True)

    # Since the difference is whether J is a Jack or a Joker but the algorithms are the same it's the same function
    # called for both with the use_jokers flag set appropriately.
    solve(INPUT)
    solve(INPUT, use_jokers=True)
