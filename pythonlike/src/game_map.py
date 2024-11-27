import numpy as np

from .creature import Creature
from .entity import Entity
from .item import Item
from .object import Object


class GameMap:
    def __init__(
        self,
        w: int,
        h: int,
        tiles: np.ndarray,
        entities: list[Entity],
    ) -> None:
        self.w = w
        self.h = h
        self.tiles = tiles
        self.creatures = []
        self.objects = []
        self.items = []
        self.explored = np.zeros_like(self.tiles)
        self.visible = np.zeros_like(self.tiles)

        for ent in entities:
            match ent:
                case Creature():
                    self.creatures.append(ent)
                    if ent.name == "player":
                        self.player = ent
                case Object():
                    self.objects.append(ent)
                case Item():
                    self.items.append(ent)

    def is_walkable(self, x: int, y: int) -> bool:
        tile_walkable = self.tiles[x, y]["walkable"]
        obj = self.get_object(x, y)
        if obj:
            return tile_walkable and obj.walkable
        return tile_walkable

    def is_occupied(self, x: int, y: int) -> bool:
        return bool(self.get_creature(x, y))

    def get_blocking_entity(self, x: int, y: int) -> Entity | None:
        creature = self.get_creature(x, y)
        if creature:
            return creature
        obj = self.get_object(x, y)
        if obj and not obj.walkable:
            return obj
        return None

    def get_creature(self, x: int, y: int) -> Creature | None:
        """Return creature at (x,y) or None if there is no creature."""
        for c in self.creatures:
            if c.x == x and c.y == y:
                return c
        return None

    def get_creature_index(self, x: int, y: int) -> int | None:
        """Return index of creature at (x, y) in creatures."""
        for i, e in enumerate(self.creatures):
            if e.x == x and e.y == y:
                return i
        return None

    def get_object(self, x: int, y: int) -> Object | None:
        """Return object at (x,y) or None if there is no object."""
        for o in self.objects:
            if o.x == x and o.y == y:
                return o
        return None

    def get_object_index(self, x: int, y: int) -> int | None:
        """Return index of object at (x, y) in objects."""
        for i, o in enumerate(self.objects):
            if o.x == x and o.y == y:
                return i
        return None
