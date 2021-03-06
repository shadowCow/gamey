from abc import ABC, abstractmethod
from typing import Callable, Any, Optional, List


class State(ABC):
    def __init__(
        self,
        kind: str,
    ):
        self.kind = kind


class GameState(State):
    def __init__(
        self,
        kind: str,
        current_player: int,
        turn_state: State,
        is_terminal: bool = False,
    ):
        super().__init__(self, kind)

        self.current_player = current_player
        self.turn_state = turn_state
        self.is_terminal = is_terminal


class Action(ABC):
    def __init__(self, kind: str):
        self.kind = kind


# Finite State Machine
class FSM:
    def __init__(
        self,
        transition_fn: Callable[[GameState, Action], GameState],
        initial_state: GameState,
    ):
        self.tranition_fn = transition_fn
        self.current_state = initial_state

    
    def transition(self, action):
        self.current_state = self.tranition_fn(
            self.current_state,
            action,
        )

        return self.current_state

    
class Player(ABC):
    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def take_action(self, game_state):
        pass


class AiPlayer(Player):
    @abstractmethod
    def take_action(self, game_state):
        pass


class HumanPlayer(Player):
    def __init__(
        self,
        name: str,
        action_prompt_creator: Callable[[GameState], str],
        action_parser: Callable[[str], Optional[Action]]
    ):
        self.action_prompt_creator = action_prompt_creator
        self.action_parser = action_parser
        super().__init__(name)


    def take_action(self, game_state):
        prompt = self.action_prompt_creator(game_state)

        valid_action = None
        user_input = input(prompt)

        while valid_action == None:
            print("Invalid action, try again")
            user_input = input(prompt)

            valid_action = self.action_parser(user_input)
        else:
            return valid_action



class Game:
    def __init__(
        self,
        fsm: FSM,
        players: List[Player],
    ):
        self.fsm = fsm
        self.players = players

    
    def play(self):
        while self.fsm.current_state.is_terminal == False:
            player_action = self.players(
                self.fsm.current_state.current_player
            ).take_action(self.fsm.current_state)
            
            self.fsm.transition(player_action)
        else:
            return self.fsm.current_state
