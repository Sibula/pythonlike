import tcod


class Entity:
    def __init__(self, w, h, name, char, color, size, hp, damage, defence, accuracy, equipment={}):
        self.w = w
        self.h = h
        self.name = name
        self.char = char
        self.color = color
        # tiny (<0.5m / <3kg), small (0.5-1.2m / 3-25kg), medium (1.2-2.4m / 25-200kg), large (>2.4m / >200kg)
        # acc   0.6x                     0.8x                          1x                        1.2x
        # enum    0                         1                           2                         3
        self.size = size
        self.hp = hp  # (how to handle max hp?) (calculate from base stats + modifier?)
        self.damage = damage
        self.defence = defence
        self.accuracy = accuracy  # Likely removed in favour of other stats determining accuracy with various weapons
        self.equipment = equipment
        # base stats like STR, INT, etc?


# Entities
class Player(Entity):
    def __init__(self, w, h, name="player", char=chr(64), color=tcod.yellow,
                 size=2, hp=100, damage=5, defence=1, accuracy=0.8, equipment={}):
        super().__init__(w, h, name, char, color, size, hp, damage, defence, accuracy, equipment)


class Rat(Entity):
    def __init__(self, w, h, name="rat", char=chr(114), color=tcod.red,
                 size=0, hp=5, damage=1, defence=0, accuracy=0.9):
        super().__init__(w, h, name, char, color, size, hp, damage, defence, accuracy)


def init_entities(game_map):
    """Initialize entities list."""
    entities = [Player(0, 0), Rat(10, 5)]
    return entities
