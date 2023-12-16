import numpy as np
from mapgen import generate_map


class GameMap:
    def __init__(self, w: int, h: int):
        self.w = w
        self.h = h
        self.tiles = generate_map(w, h)
        self.explored = np.zeros_like(self.tiles)
        self.visible = np.zeros_like(self.tiles)

    def is_walkable(self, x: int, y: int) -> bool:
        return self.tiles[x, y]["walkable"]
