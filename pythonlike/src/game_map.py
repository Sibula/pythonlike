import numpy as np
from entity import Entity


class GameMap:
    def __init__(self, w: int, h: int, tiles: np.ndarray, entities: list[Entity]):
        self.w = w
        self.h = h
        self.tiles = tiles
        self.entities = entities
        self.explored = np.zeros_like(self.tiles)
        self.visible = np.zeros_like(self.tiles)

    def is_walkable(self, x: int, y: int) -> bool:
        return self.tiles[x, y]["walkable"]
