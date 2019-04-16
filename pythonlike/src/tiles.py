import tcod


class Tile:
    def __init__(self, char, color, transparent, walkable):
        self.char = char
        self.color = color
        self.transparent = transparent
        self.walkable = walkable


# Map tiles
class Empty(Tile):
    def __init__(self, char=" ", color=tcod.black, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Floor(Tile):
    def __init__(self, char=".", color=tcod.light_gray, transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class Wall(Tile):
    def __init__(self, char="#", color=tcod.light_gray, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Door(Tile):
    def __init__(self, char="+", color=tcod.dark_amber, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)

    def interact(self):
        self.char = "_" if self.char == "+" else "+"
        self.transparent = not self.transparent
        self.walkable = not self.walkable


class StairsUp(Tile):
    def __init__(self, char="<", color=tcod.white, transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class StairsDown(Tile):
    def __init__(self, char=">", color=tcod.white, transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)
