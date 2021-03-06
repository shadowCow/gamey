import unittest
from games.game import Player
from typing import List
from games.tournament import play_tournament

class TestTournament(unittest.TestCase):

    def test_play_tournament(self):
        players = [
            TestPlayer("D"),
            TestPlayer("B"),
            TestPlayer("C"),
            TestPlayer("A"),
        ]

        num_rounds = 5
        
        rated_players = play_tournament(
            players,
            num_rounds,
            dummy_game,
        )

        print(rated_players)
        self.assertEqual(rated_players[0].player.name, "A")
        self.assertEqual(rated_players[1].player.name, "B")
        self.assertEqual(rated_players[2].player.name, "C")
        self.assertEqual(rated_players[3].player.name, "D")
    
        
class TestPlayer(Player):
    def __init__(self, name: str):
        super().__init__(name)

    def take_action(self, game_state):
        pass


def dummy_game(players: List[Player]) -> List[int]:
    # a beats everyone
    # b beats c and d
    # c beats d

    if players[0].name == "A":
        return [1, 2]
    elif players[1].name == "A":
        return [2, 1]
    elif players[0].name == "B":
        return [1, 2]
    elif players[1].name == "B":
        return [2, 1]
    elif players[0].name == "C":
        return [1, 2]
    elif players[1].name == "C":
        return [2, 1]
    


if __name__ == '__main__':
    unittest.main()