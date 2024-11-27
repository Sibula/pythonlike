from collections import deque

from tcod.event import KeySym

from . import actions
from .game_map import GameMap


class Engine:
    def __init__(self, game_map: GameMap) -> None:
        self.game_map = game_map
        self.commands: dict[KeySym, actions.Action] = {
            # Movement
            KeySym.KP_1: actions.Bump(game_map.player, game_map, -1, 1),
            KeySym.KP_2: actions.Bump(game_map.player, game_map, 0, 1),
            KeySym.KP_3: actions.Bump(game_map.player, game_map, 1, 1),
            KeySym.KP_4: actions.Bump(game_map.player, game_map, -1, 0),
            KeySym.KP_5: actions.Stay(game_map.player, game_map),
            KeySym.KP_6: actions.Bump(game_map.player, game_map, 1, 0),
            KeySym.KP_7: actions.Bump(game_map.player, game_map, -1, -1),
            KeySym.KP_8: actions.Bump(game_map.player, game_map, 0, -1),
            KeySym.KP_9: actions.Bump(game_map.player, game_map, 1, -1),
            KeySym.KP_0: actions.Interact(game_map.player, game_map),
            KeySym.KP_PERIOD: actions.Loot(game_map.player, game_map),
        }

    def handle_event(self, key: KeySym, message_log: deque) -> None:
        if key in self.commands:
            action = self.commands[key]
            self.process_step(action, message_log)

    def process_step(self, action: actions.Action, message_log: deque) -> None:
        msg = action.perform()
        if msg:
            message_log.append(msg)
        # Process turns for other entities
