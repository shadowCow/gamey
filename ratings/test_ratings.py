import unittest
from ratings.ratings import elo_rating


class TestRatings(unittest.TestCase):

    def test_elo_rating(self):
        p1_rating = 1200
        p2_rating = 1000
        K = 32

        ratings_if_p1_wins = elo_rating(p1_rating, p2_rating, K, True)
        expected_ratings_p1_wins = (1208, 992)
        self.assertEqual(ratings_if_p1_wins, expected_ratings_p1_wins)

        ratings_if_p2_wins = elo_rating(p1_rating, p2_rating, K, False)
        expected_ratings_p2_wins = (1176, 1024)
        self.assertEqual(ratings_if_p2_wins, expected_ratings_p2_wins)


if __name__ == '__main__':
    unittest.main()