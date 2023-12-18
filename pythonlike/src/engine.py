from collections import deque

from combat import attack
import entity
from event_handler import handle_events, Action
from game_map import GameMap
import tile

class Engine:
    def __init__(self, game_map: GameMap) -> None:
        self.game_map = game_map
    
    def process_step(self, message_log: deque) -> deque:
        action = handle_events()
        messages = self._update(action)
        for msg in messages:
            if msg:
                message_log.append(msg)
    
    def _update(self, action: Action) -> list[str]:
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
    
    def _invalid(self, param):
        return None  # "Invalid command: {}".format(param)

    def _move(self, action: Action) -> str | None:
        player = self.game_map.player
        index = self.game_map.get_creature_index(player.x, player.y)
        dx, dy = action.param
        nx, ny = player.x + dx, player.y + dy
        occupied = self.game_map.is_occupied(nx, ny)
        nt = self.game_map.tiles[nx, ny]
        if nt["walkable"] and not occupied:
            player.x, player.y = nx, ny
        elif occupied:
            return attack(index, self.game_map.get_creature_index(nx, ny), self.game_map.entities)
        elif nt == tile.door:
            # game_map.tiles[nx, ny].interact()
            pass

    def _stay(self) -> None:
        return None

    def _interact(self) -> str:
        return "interact"

    def _loot(self) -> str:
        return "loot"
