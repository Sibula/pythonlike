import tcod


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
