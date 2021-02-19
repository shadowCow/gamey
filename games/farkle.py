from dice.roller import D6, d6_counts, d6_counts_by_quantity
from abc import ABC
from typing import List, Dict


class ScoringDice(ABC):
    def __init__(self, num_dice: int, points: int):
        self.num_dice = num_dice
        self.points = points


class One(ScoringDice):
    def __init__(self):
        super().__init__(self, 1, 100)


class TwoOnes(ScoringDice):
    def __init__(self):
        super().__init__(self, 2, 200)


class OneFive(ScoringDice):
    def __init__(self):
        super().__init__(self, 2, 150)


class Five(ScoringDice):
    def __init__(self):
        super().__init__(self, 1, 50)


class TwoFives(ScoringDice):
    def __init__(self):
        super().__init__(self, 2, 100)


class ThreeOnes(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 300)


class ThreeTwos(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 200)


class ThreeThrees(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 300)


class ThreeFours(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 400)


class ThreeFives(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 500)


class ThreeSixes(ScoringDice):
    def __init__(self):
        super().__init__(self, 3, 600)


class FourOfAKind(ScoringDice):
    def __init__(self):
        super().__init__(self, 4, 1000)


class FiveOfAKind(ScoringDice):
    def __init__(self):
        super().__init__(self, 5, 2000)


class SixOfAKind(ScoringDice):
    def __init__(self):
        super().__init__(self, 6, 3000)


class OneToSixStraight(ScoringDice):
    def __init__(self):
        super().__init__(self, 6, 1500)


class ThreePairs(ScoringDice):
    def __init__(self):
        super().__init__(self, 6, 1500)


class FourOfAKindWithAPair(ScoringDice):
    def __init__(self):
        super().__init__(self, 6, 1500)


class TwoTriplets(ScoringDice):
    def __init__(self):
        super().__init__(self, 6, 2500)


class ScoringOption:
    def __init__(self, scoring_dice: ScoringDice, remaining_dice: int):
        self.scoring_dice = scoring_dice
        self.remaining_dice = remaining_dice


def scoring_options(dice_counts: Dict[D6, int]) -> List[ScoringOption]:
    counts = d6_counts_by_quantity(dice_counts)

    # get scoring options based on counts of dice

    return []
