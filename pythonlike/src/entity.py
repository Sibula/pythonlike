import tcod


class Entity:
    def __init__(self, w, h, char, color):
        self.w = w
        self.h = h
        self.char = char
        self.color = color


# Entities
class Player(Entity):
    def __init__(self, w, h, char=chr(64), color=tcod.yellow):
        super().__init__(w, h, char, color)


class Rat(Entity):
    def __init__(self, w, h, char=chr(64), color=tcod.yellow):
        super().__init__(w, h, char, color)


def init_entities(game_map):
    return [Player(0, 0)]
