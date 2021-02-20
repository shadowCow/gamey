from dice.roller import D6, DiceCounts, d6_counts, d6_counts_by_quantity, roll_n_d6
from abc import ABC
from enum import Enum
from typing import List, Dict


class PostRollAction:
    def __init__(self, points: int, remaining_dice: int):
        self.points = points
        self.remaining_dice = remaining_dice


def farkle() -> PostRollAction:
    return PostRollAction(0, 0)


def score_three_of_a_kind(die: D6) -> int:
    if die == D6.One:
        return 300
    else:
        return die.value * 100


def get_actions(points: int, dice: List[D6]) -> List[PostRollAction]:
    num_dice = len(dice)

    if num_dice == 1:
        return get_actions_1(points, dice)
    elif num_dice == 2:
        return get_actions_2(points, dice)
    elif num_dice == 3:
        return get_actions_3(points, dice)
    elif num_dice == 4:
        return get_actions_4(points, dice)
    elif num_dice == 5:
        return get_actions_5(points, dice)
    elif num_dice == 6:
        return get_actions_6(points, dice)


def get_actions_1(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)

    return get_danglers(points, counts, 1)


def get_actions_2(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)

    return get_danglers(points, counts, len(dice))


def get_actions_3(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)

    max_count = counts.by_quantity[0][0]

    if max_count == 3:
        return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 6)]
    else:
        return get_danglers(points, counts, len(dice))


def get_actions_4(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)
    
    max_count = counts.by_quantity[0][0]
    ones = counts.by_dice[D6.One]
    fives = counts.by_dice[D6.Five]

    if max_count == 4:
        return [PostRollAction(1000, 6)]
    elif max_count == 3:
        if fives == 1:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 50, 6)]
        elif ones == 1:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 6)]
        else:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 1)]
    else:
        return get_danglers(points, counts, len(dice))


def get_actions_5(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)

    max_count = counts.by_quantity[0][0]
    ones = counts.by_dice[D6.One]
    fives = counts.by_dice[D6.Five]

    if max_count == 5:
        return [PostRollAction(points + 2000, 6)]
    elif max_count == 4:
        if ones == 1:
            return [PostRollAction(points + 1000, 6)]
        elif fives == 1:
            return [PostRollAction(points + 1000, 6)]
        else:
            return [PostRollAction(points + 1000, 1)]
    elif max_count == 3:
        if ones == 2:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 200, 6)]
        elif ones == 1 and fives == 1:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 150, 6)]
        elif fives == 2:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 6)]
        elif ones == 1:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 1),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 2)
            ]
        elif fives == 1:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 50, 1),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 2)
            ]
        else:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 2)]
    else:
        return get_danglers(points, counts, len(dice))


def get_actions_6(points: int, dice: List[D6]) -> List[PostRollAction]:
    counts = DiceCounts(dice)

    max_count = counts.by_quantity[0][0]
    ones = counts.by_dice[D6.One]
    fives = counts.by_dice[D6.Five]

    if max_count == 6:
        return [PostRollAction(points + 3000, 6)]
    elif max_count == 5:
        if ones == 1:
            return [PostRollAction(points + 2000 + 100, 6)]
        elif fives == 1:
            return [PostRollAction(points + 2000 + 50, 6)]
        else:
            return [PostRollAction(points + 2000, 1)]
    elif max_count == 4:
        if counts.by_quantity[1][0] == 2:
            return [PostRollAction(points + 1500, 6)]
        elif ones == 1 and fives == 1:
            return [PostRollAction(points + 1000 + 150, 6)]
        elif ones == 1:
            return [
                PostRollAction(points + 1000 + 100, 1),
                PostRollAction(points + 1000, 2),
            ]
        elif fives == 1:
            return [
                PostRollAction(points + 1000 + 50, 1),
                PostRollAction(points + 1000, 2),
            ]
        else:
            return [PostRollAction(points + 1000, 2)]
    elif max_count == 3:
        if counts.by_quantity[1][0] == 3:
            return [PostRollAction(points + 2500, 6)]
        elif ones == 2 and fives == 1:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 250, 6)]
        elif ones == 1 and fives == 2:
            return [PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 200, 6)]
        elif ones == 2:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 200, 1),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 2),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
        elif fives == 2:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 1),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 50, 2),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
        elif ones == 1 and fives == 1:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 150, 1),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 2),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
        elif ones == 1:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 100, 2),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
        elif fives == 1:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]) + 50, 2),
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
        else:
            return [
                PostRollAction(points + score_three_of_a_kind(counts.by_quantity[0][1]), 3),
            ]
    elif max_count == 2:
        if counts.by_quantity[1][0] == 2 and counts.by_quantity[3][0] == 2:
            return [PostRollAction(points + 1500, 6)]
        else:
            return get_danglers(points, counts, len(dice))
    else:
        # max_count == 1:
        return [PostRollAction(points + 1500, 6)]


def get_danglers(points: int, counts: DiceCounts, total_dice: int) -> List[PostRollAction]:
    ones = counts.by_dice[D6.One]
    fives = counts.by_dice[D6.Five]

    if ones == 2 and fives == 1:
        return [PostRollAction(points + 250, r_dice(total_dice - 3))]
    elif ones == 1 and fives == 2:
        return [PostRollAction(points + 200, r_dice(total_dice - 3))]
    elif ones == 2:
        return [
            PostRollAction(points + 200, r_dice(total_dice - 2)),
            PostRollAction(points + 100, r_dice(total_dice - 1)),
        ]
    elif ones == 1 and fives == 1:
        return [
            PostRollAction(points + 150, r_dice(total_dice - 2)),
            PostRollAction(points + 100, r_dice(total_dice - 1)),
        ]
    elif ones == 1:
        return [
            PostRollAction(points + 100, r_dice(total_dice - 1)),
        ]
    elif fives == 1:
        return [
            PostRollAction(points + 50, r_dice(total_dice - 1)),
        ]
    else:
        return [farkle()]


def r_dice(dice: int) -> int:
    if dice == 0:
        return 6
    else:
        return dice


class TurnPhase(Enum):
    Rolling = 1
    End = 2


class TurnState:
    def __init__(self, phase: TurnPhase, points: int, remaining_dice: int):
        self.phase = phase
        self.points = points
        self.remaining_dice = remaining_dice


def new_turn() -> TurnState:
    return TurnState(
        TurnPhase.Rolling,
        0,
        6
    )


class GameState:
    def __init__(self, scores: List[int], player_turn: int, turn_state: TurnState):
        self.scores = scores
        self.player_turn = player_turn
        self.turn_state = turn_state


def new_game(num_players: int) -> GameState:
    scores = []
    for i in range(num_players):
        scores.append(0)

    return GameState(scores, 0, new_turn())


def play(num_humans: int, num_ai: int, score_target: int):
    game_state = new_game(num_humans + num_ai)

    max_score = 0
    while max_score < score_target:
        
        while game_state.turn_state.phase != TurnPhase.End:
            roll = roll_n_d6(game_state.turn_state.remaining_dice)

            actions = get_actions(game_state.turn_state.points, roll)

            if farkled(actions):
                game_state.turn_state.phase = TurnPhase.End
                game_state.turn_state.points = 0
            else:
                is_human = game_state.player_turn < num_humans
                action = choose_action(roll, actions, is_human)

                game_state.turn_state.points = action.points
                game_state.turn_state.remaining_dice = action.remaining_dice

                keep_rolling = choose_keep_rolling(game_state.turn_state, is_human)

                if not keep_rolling:
                    game_state.scores[game_state.player_turn] += game_state.turn_state.points
                    game_state.turn_state.phase == TurnPhase.End

        game_state.player_turn = (game_state.player_turn + 1) % (num_humans + num_ai)
        game_state.turn_state = new_turn()

    print("Max score reached")
    print("Scores: {scores}".format(scores = game_state.scores))


def choose_action(roll: List[D6], actions: List[PostRollAction], is_human: bool) -> PostRollAction:
    if is_human:
        print("Roll: {roll_str}".format(roll_str = list(map(lambda d: d.value, roll))))
        # prompt for choice
        for i, a in enumerate(actions):
            print("Action: {index} - {points}, {dice}".format(index = i, points = a.points, dice = a.remaining_dice))
            
        choice = int(input('Choose an action by number: '))
        return actions[choice]
    else:
        # ai!
        # naive - choose max points action
        return max(actions, key=lambda a: a.points)


def choose_keep_rolling(turn_state: TurnState, is_human: bool) -> bool:
    if is_human:
        print("Accumulated points: {points}".format(points = turn_state.points))
        choice = input("Keep rolling [Y/N]? ")
        if choice.lower() == "n":
            return False
        else:
            return True
    else:
        # ai!
        # naive, only quit if you've got at least 300
        return turn_state.points < 300


def farkled(actions: List[PostRollAction]) -> bool:
    return len(actions) == 1 and actions[0].remaining_dice == 0
        



if __name__ == "__main__":
    play(1, 1, 3000)