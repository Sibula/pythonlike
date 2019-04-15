import tcod.map
import numpy as np
from mapgen import generate_map


class GameMap:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tiles = generate_map(w, h)
        self.tcod_map = tcod.map.Map(w, h)
        self.explored = np.zeros_like(self.tiles)

    def is_walkable(self, w, h):
        return self.tiles[w, h].walkable
