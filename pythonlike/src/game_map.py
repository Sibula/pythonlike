import tcod
import tcod.map
import numpy as np


class GameMap:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tcod_map = tcod.map.Map(w, h)
        self.tiles = self.init_tiles(w, h)
        self.explored = np.zeros_like(self.tiles)

    def init_tiles(self, w, h):
        # TODO: Map generator
        tiles = np.full((w, h), Floor())
        # tiles[(5, 5)] = Door()
        # tiles[(10, 10)] = Door()

        return tiles


class Tile:
    def __init__(self, char, color, transparent, walkable):
        self.char = char
        self.color = color
        self.transparent = transparent
        self.walkable = walkable


# Map tiles
class Empty(Tile):
    def __init__(self, char=chr(32), color=tcod.black, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Floor(Tile):
    def __init__(self, char=chr(46), color=tcod.white, transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class Wall(Tile):
    def __init__(self, char=chr(35), color=tcod.white, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Door(Tile):
    def __init__(self, char="+", color=tcod.white, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)

    def toggle(self):
        self.char = "_" if self.char == "+" else "+"
        self.transparent = not self.transparent
        self.walkable = not self.walkable

    # @property
    # def char(self):
    #     return "_" if self.open else "+"

