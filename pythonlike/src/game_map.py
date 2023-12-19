import numpy as np
from entity import Entity


class GameMap:
    def __init__(self, w: int, h: int, tiles: np.ndarray, entities: list[Entity]):
        self.w = w
        self.h = h
        self.tiles = tiles
        self.entities = entities
        self.player = entities[0]  # Player should always be first when initializing creatures
        # self.objects = []
        # self.items = []
        self.explored = np.zeros_like(self.tiles)
        self.visible = np.zeros_like(self.tiles)

    def is_walkable(self, x: int, y: int) -> bool:
        return self.tiles[x, y]["walkable"]
    
    def is_occupied(self, x: int, y:int) -> bool:
        return True if self.get_creature(x, y) else False

    def get_creature(self, x: int, y: int) -> Entity | None:
        """Return creature at (x,y) or None if there is no creature."""
        for e in self.entities:
            if e.x == x and e.y == y:
                return e
        return None
    
    def get_creature_index(self, x: int, y: int) -> int | None:
        """Return index of entity at (x, y) in entities."""
        for i, e in enumerate(self.entities):
            if e.x == x and e.y == y:
                return i
        return None
