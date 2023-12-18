from collections import deque
from tcod.event import KeySym

import actions
from game_map import GameMap

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
    
    def handle_event(self, key: KeySym, message_log: deque)-> deque:
        action = self.commands[key] or None
        if action: 
            self.process_step(action, message_log)

    def process_step(self, action: actions.Action, message_log: deque) -> deque:
        msg = action.perform()
        if msg:
            message_log.append(msg)
        # Process turns for other entities

    def _update(self, action: actions.Action) -> list[str]:
        messages = []
        # If the player closes the window raise SystemExit.
        if action.name == "quit":
            raise SystemExit()
        # If command was invalid do something.
        if action.name == "invalid":
            messages.append(self._invalid(action.param))
        else:
            # Update the game if the command was valid.
            if action.name == "move":
                messages.append(self._move(action))
            if action.name == "stay":
                messages.append(self._stay())
            if action.name == "interact":
                messages.append(self._interact())
            if action.name == "loot":
                messages.append(self._loot())

            # At the end of checking actions process turns for other entities.
        return messages
    

