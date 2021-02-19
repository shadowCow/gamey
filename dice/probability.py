class DiscreteProbability:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator


def d6_probability(numerator: int) -> DiscreteProbability:
    return DiscreteProbability(
        clamp(numerator, 1, 6),
        6
    )


def n_d6_probability(n: int, numerator: int) -> DiscreteProbability:
    return DiscreteProbability(
        clamp(numerator, 1, n*6),
        n*6
    )


def clamp(value: int, minimum: int, maximum: int) -> int:
    return max(minimum, min(value, maximum))