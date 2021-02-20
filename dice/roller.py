from enum import Enum
from random import randint
from typing import List, Dict, Tuple


class D6(Enum):
    One = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6


class DiceCounts:
    def __init__(self, roll: List[D6]):
        self.by_dice = d6_counts(roll)
        self.by_quantity = d6_counts_by_quantity(self.by_dice)


def d6_counts(dice: List[D6]) -> Dict[D6, int]:
    counts = {
        D6.One: 0,
        D6.Two: 0,
        D6.Three: 0,
        D6.Four: 0,
        D6.Five: 0,
        D6.Six: 0,
    }

    for d in dice:
        counts[d] = counts[d] + 1

    return counts


def d6_counts_by_quantity(dice_counts: Dict[D6, int]) -> List[Tuple[int, D6]]:
    counts = []

    for k,v in dice_counts.items():
        if (v > 0):
            counts.append((v, k))

    counts.sort(key=lambda c: c[0], reverse=True)

    return counts


def roll_d6() -> D6:
    return D6(randint(1, 6))


def roll_n_d6(n: int) -> List[D6]:
    rolls = []
    for x in range(n):
        rolls.append(roll_d6())

    return rolls
