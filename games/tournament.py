from typing import List, Callable
from random import randint
from games.game import Player, Game
from ratings.ratings import elo_rating


class RatedPlayer:
    def __init__(
        self,
        rating: int,
        player: Player,
    ):
        self.rating = rating
        self.player = player

    def __str__(self):
        return self.player.name + ": " + self.rating.__str__()

    def __repr__(self):
        return self.__str__()


class Match:
    def __init__(
        self,
        player1: Player,
        player2: Player,
    ):
        self.player1 = player1
        self.player2 = player2


def play_tournament(
    players: List[Player],
    num_rounds: int,
    play_game: Callable[[List[Player]], List[int]],
) -> List[RatedPlayer]:
    if len(players) % 2 != 0:
        raise Exception("Must have an even number of players.")

    rated_players = []
    for p in players:
        rated_players.append(RatedPlayer(1000, p))

    rounds_played = 0
    while rounds_played < num_rounds:
        for i in range(0, len(rated_players), 2):
            play_match(
                rated_players[i],
                rated_players[i + 1],
                play_game,
            )

        rated_players.sort(key=lambda p: p.rating, reverse=True)
        rounds_played += 1
    else:
        return rated_players


def play_match(
    player1: RatedPlayer,
    player2: RatedPlayer,
    play_game: Callable[[List[Player]], List[int]],
):
    players = [player1, player2]
    who_goes_first = randint(1,2)
    if who_goes_first == 2:
        players.reverse()

    ranking = play_game([players[0].player, players[1].player])

    if ranking[0] == 1 and ranking[1] == 1:
        # tie - unchanged?  not right :/
        pass
    elif ranking[0] == 1:
        # player who went first wins
        new_ratings = elo_rating(
            players[0].rating,
            players[1].rating,
            32.0,
            True,
        )

        players[0].rating = new_ratings[0]
        players[1].rating = new_ratings[1]
    else:
        # player who went second wins
        new_ratings = elo_rating(
            players[0].rating,
            players[1].rating,
            32.0,
            False,
        )

        players[0].rating = new_ratings[0]
        players[1].rating = new_ratings[1]
