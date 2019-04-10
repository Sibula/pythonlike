import tcod


class Entity:
    def __init__(self, w, h, name, char, color, size, hp, damage, armor, resistance, accuracy, equipment={}):
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
        self.armor = armor
        self.resistance = resistance
        self.accuracy = accuracy  # Likely removed in favour of other stats determining accuracy with various weapons
        self.equipment = equipment
        # base stats like STR, INT, etc?


# Entities
class Player(Entity):
    def __init__(self, w, h, name="player", char="@", color=tcod.yellow,
                 size=1, hp=10, damage=2, armor=0, resistance=0, accuracy=0.7, equipment={}):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy, equipment)


class Bat(Entity):
    def __init__(self, w, h, name="bat", char="b", color=tcod.dark_amber,
                 size=0.6, hp=2, damage=1, armor=0, resistance=0, accuracy=0.9):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy)


class GiantBat(Entity):
    def __init__(self, w, h, name="giant bat", char="b", color=tcod.red,
                 size=0.6, hp=4, damage=2, armor=0, resistance=0, accuracy=0.9):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy)


class Rat(Entity):
    def __init__(self, w, h, name="rat", char="r", color=tcod.dark_amber,
                 size=0.6, hp=3, damage=1, armor=0, resistance=0, accuracy=0.85):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy)


class GiantRat(Entity):
    def __init__(self, w, h, name="giant rat", char="r", color=tcod.red,
                 size=0.6, hp=6, damage=2, armor=0, resistance=0, accuracy=0.85):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy)


class Goblin(Entity):
    def __init__(self, w, h, name="goblin", char="o", color=tcod.dark_amber,
                 size=0.8, hp=8, damage=2, armor=0, resistance=0, accuracy=0.7, equipment={}):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy, equipment)


class Hobgoblin(Entity):
    def __init__(self, w, h, name="hobgoblin", char="o", color=tcod.red,
                 size=0.8, hp=12, damage=3, armor=0, resistance=0, accuracy=0.7, equipment={}):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy, equipment)


class Orc(Entity):
    def __init__(self, w, h, name="orc", char="o", color=tcod.dark_yellow,
                 size=0.8, hp=16, damage=4, armor=0, resistance=0, accuracy=0.7, equipment={}):
        super().__init__(w, h, name, char, color, size, hp, damage, armor, resistance, accuracy, equipment)


def init_entities(game_map):
    """Initialize entities list."""
    entities = [Player(0, 0), Rat(4, 2), GiantRat(4, 4), Bat(6, 2), GiantBat(6, 4), Goblin(8, 2), Hobgoblin(8, 4),
                Orc(8, 6)]
    return entities
