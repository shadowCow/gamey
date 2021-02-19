import unittest
from dice.roller import D6, d6_counts, d6_counts_by_quantity


class TestRoller(unittest.TestCase):

    def test_d6_counts(self):
        dice = [D6.One, D6.One, D6.Six, D6.Three, D6.Six, D6.One]
        expected_counts = {
            D6.One: 3,
            D6.Two: 0,
            D6.Three: 1,
            D6.Four: 0,
            D6.Five: 0,
            D6.Six: 2,
        }
        self.assertEqual(d6_counts(dice), expected_counts)


    def test_d6_counts_by_quantity(self):
        counts = {
            D6.One: 0,
            D6.Two: 0,
            D6.Three: 1,
            D6.Four: 3,
            D6.Five: 0,
            D6.Six: 2,
        }
        expected_result = [
            (3, D6.Four),
            (2, D6.Six),
            (1, D6.Three),
        ]
        self.assertEqual(d6_counts_by_quantity(counts), expected_result)
        

if __name__ == '__main__':
    unittest.main()