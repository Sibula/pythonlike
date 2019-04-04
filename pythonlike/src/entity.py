import tcod


class Entity:
    def __init__(self, w, h, name, char, color):
        self.w = w
        self.h = h
        self.name = name
        self.char = char
        self.color = color
        # hp (how to handle max hp?)
        # base damage
        # base defence
        # accuracy
        # equipment


# Entities
class Player(Entity):
    def __init__(self, w, h, name="player", char=chr(64), color=tcod.yellow):
        super().__init__(w, h, name, char, color)


class Rat(Entity):
    def __init__(self, w, h, name="rat", char=chr(114), color=tcod.red):
        super().__init__(w, h, name, char, color)


def init_entities(game_map):
    return [Player(0, 0), Rat(10, 5)]
