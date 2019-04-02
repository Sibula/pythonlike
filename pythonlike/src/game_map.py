import tcod
import tcod.map
import numpy as np


class GameMap:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tcod_map = tcod.map.Map(w, h)
        self.explored = np.zeros((w, h), dtype=bool, order="F")
        self.tiles = self.init_tiles()
        # TODO: Populate

    def init_tiles(self):
        tiles = [[Floor for y in range(self.h)] for x in range(self.w)]

        return tiles


# TODO: More tiles
class Tile:
    def __init__(self):
        self. char = None
        self.color = None
        self.transparent = None
        self.walkable = None


class Empty(Tile):
    Tile.char = chr(32)
    Tile.color = tcod.black
    Tile.transparent = False
    Tile.walkable = False


class Floor(Tile):
    Tile.char = chr(46)
    Tile.color = tcod.white
    Tile.transparent = True
    Tile.walkable = True


class Wall(Tile):
    Tile.char = chr(35)
    Tile.color = tcod.white
    Tile.transparent = False
    Tile.walkable = False
