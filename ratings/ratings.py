import math
from typing import Tuple

def elo_rating(player_1_rating: int, player_2_rating: int, K: float, player_1_wins: bool) -> Tuple[int, int]:
    p_1 = pr_win(player_1_rating, player_2_rating)
    p_2 = pr_win(player_2_rating, player_1_rating)

    if player_1_wins:
        player_1_new_rating = player_1_rating + K * (1 - p_1)
        player_2_new_rating = player_2_rating + K * (0 - p_2)

        return (
            round(player_1_new_rating),
            round(player_2_new_rating),
        )
    else:
        player_1_new_rating = player_1_rating + K * (0 - p_1)
        player_2_new_rating = player_2_rating + K * (1 - p_2)

        return (
            round(player_1_new_rating),
            round(player_2_new_rating),
        )


# Function to calculate the winning probability of player_1
def pr_win(player_1_rating: int, player_2_rating: int) -> float:
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (player_2_rating - player_1_rating) / 400)) 
