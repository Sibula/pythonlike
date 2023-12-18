from abc import ABC, abstractmethod
from dataclasses import dataclass

import combat
import entity
import game_map


# Abstract actions

@dataclass
class Action(ABC):
    entity: entity.Entity
    game_map: game_map.GameMap

    @abstractmethod
    def perform(self) -> str | None:
        pass

@dataclass
class DirectedAction(Action):
    dx: int
    dy: int

    @abstractmethod
    def perform(self) -> str | None:
        pass


# Actions

class Interact(Action):
    def perform(self) -> str:
        return "interact"

class InvalidAction(Action):
    def perform(self) -> None:
        # Could log these or something?
        pass

class Loot(Action):
    def perform(self) -> str:
        return "loot"

class Melee(DirectedAction):
    def perform(self) -> str:
        x = self.entity.x + self.dx
        y = self.entity.y + self.dy
        creature = self.game_map.get_creature(x, y)
        if creature:
            return f"Hit {creature.name}"
        # Other melee targets, like doors etc.
        return None

class Move(DirectedAction):
    def perform(self) -> str:
        self.entity.x += self.dx
        self.entity.y += self.dy
        
class Stay(Action):
    def perform(self) -> None:
        pass

class Bump(DirectedAction):
    def perform(self) -> str | None:
        nx = self.entity.x + self.dx
        ny = self.entity.y + self.dy
        nt = self.game_map.tiles[nx, ny]
        if nt["walkable"]:
            if self.game_map.is_occupied(nx, ny):
                return Melee(self.entity, self.game_map, self.dx, self.dy).perform()
            else:
                return Move(self.entity, self.game_map, self.dx, self.dy).perform()
        else:
            # TODO: Add door functionality
            return None

class Quit(Action):
    def perform(self) -> None:
        raise SystemExit()

'''
def _move(self, action: Action) -> str | None:
    player = self.game_map.player
    index = self.game_map.get_entity_index(player.x, player.y)
    dx, dy = action.param
    nx, ny = player.x + dx, player.y + dy
    occupied = self.game_map.is_occupied(nx, ny)
    nt = self.game_map.tiles[nx, ny]
    if nt["walkable"] and not occupied:
        player.x, player.y = nx, ny
    elif occupied:
        return attack(index, self.game_map.get_entity_index(nx, ny), self.game_map.entities)
    elif nt == tile.door:
        # game_map.tiles[nx, ny].interact()
        pass
'''