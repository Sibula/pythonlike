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

        return message_log
    
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
        player = self.get_player()
        index = self.get_entity_index(player.x, player.y)
        dx, dy = action.param
        nx, ny = player.x + dx, player.y + dy
        occupied = self.is_occupied(nx, ny)
        nt = self.game_map.tiles[nx, ny]
        if nt["walkable"] and not occupied:
            player.x, player.y = nx, ny
        elif occupied:
            return attack(index, self.get_entity_index(nx, ny), self.game_map.entities)
        elif nt == tile.door:
            # game_map.tiles[nx, ny].interact()
            pass

    def _stay(self) -> None:
        return None


    def _interact(self) -> str:
        return "interact"


    def _loot(self) -> str:
        return "loot"


    def is_occupied(self, x: int, y: int) -> bool:
        # Check if the tile at (x, y) is occupied by an entity.
        has_entity = False
        for ent_x, ent_y in [(ent.x, ent.y) for ent in self.game_map.entities]:
            if (ent_x, ent_y) == (x, y):
                has_entity = True

        return has_entity


    def get_entity(self, x: int, y: int) -> entity.Entity | None:
        # Return entity at (x, y).
        for ent in self.game_map.entities:
            if (ent.x, ent.y) == (x, y):
                return ent


    def get_entity_index(self, x: int, y: int) -> int | None:
        # Return index of entity at (x, y) in entities.
        for i, ent in enumerate(self.game_map.entities):
            if (ent.x, ent.y) == (x, y):
                return i
        return None


    def get_player(self) -> entity.Player:
        # Find the Player object from entities and return it.
        for ent in self.game_map.entities:
            if type(ent) == entity.Player:
                return ent
