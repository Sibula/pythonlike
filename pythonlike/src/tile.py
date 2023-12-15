import numpy as np


graphic_dtype = np.dtype([
    ("ch", np.intc),
    ("fg", "(4,)u1"),
    ("bg", "(4,)u1"),
    ])

tile_dtype = np.dtype([
    ("transparent", bool),
    ("walkable", bool),
    ("graphic", graphic_dtype),
    ])


def new_tile(
        *,
        transparent: int,
        walkable: int,
        graphic: tuple[int, tuple[int, int, int, int], tuple[int, int, int, int]],
        ) -> np.ndarray:
    return np.array((transparent, walkable, graphic), dtype=tile_dtype)


# Map tiles
empty = new_tile(
    transparent=0,
    walkable=0,
    graphic=(ord(" "), (255, 255, 255, 255), (0, 0, 0, 255))
)

floor = new_tile(
    transparent=1,
    walkable=1,
    graphic=(ord("."), (159, 159, 159, 255), (0, 0, 0, 255))
)

wall = new_tile(
    transparent=0,
    walkable=0,
    graphic=(ord("#"), (159, 159, 159, 255), (0, 0, 0, 255))
)


# Placeholders to keep demo working, 
# actually objects when I get around to implement those
door = new_tile(
    transparent=0,
    walkable=1,
    graphic=(ord("+"), (191, 143, 0, 255), (0, 0, 0, 255))
)

stairs_up = new_tile(
    transparent=1,
    walkable=1,
    graphic=(ord("<"), (255, 255, 255, 255), (0, 0, 0, 255))
)

stairs_down = new_tile(
    transparent=1,
    walkable=1,
    graphic=(ord(">"), (255, 255, 255, 255), (0, 0, 0, 255))
)

'''
class Tile:
    def __init__(self, char, color, transparent, walkable):
        self.char = char
        self.color = color
        self.transparent = transparent
        self.walkable = walkable


# Map tiles
class Empty(Tile):
    def __init__(self, char=" ", color=(0, 0, 0), transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Floor(Tile):
    def __init__(self, char=".", color=(159, 159, 159), transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class Wall(Tile):
    def __init__(self, char="#", color=(159, 159, 159), transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Door(Tile):
    def __init__(self, char="+", color=(191, 143, 0), transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)

    def interact(self):
        self.char = "_" if self.char == "+" else "+"
        self.transparent = not self.transparent
        self.walkable = not self.walkable


class StairsUp(Tile):
    def __init__(self, char="<", color=(255, 255, 255), transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class StairsDown(Tile):
    def __init__(self, char=">", color=(255, 255, 255), transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)
'''
