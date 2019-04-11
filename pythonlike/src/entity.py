import tcod


class Entity:
    def __init__(self, w, h, name, char, color, b_armor, b_armor_res, attributes, equipment={}):
        self.w = w
        self.h = h
        self.name = name
        self.char = char
        self.color = color

        self.constitution = attributes[0]
        self.strength = attributes[1]
        self.dexterity = attributes[2]
        self.intelligence = attributes[3]

        self.hp = self.max_hp
        self.b_armor = b_armor
        self.b_armor_res = b_armor_res

        self.equipment = equipment

    @property
    def evasion(self):
        b_evasion = self.dexterity ** 0.7 / 20
        # TODO: Add equipment stats
        return b_evasion

    @property
    def accuracy(self):
        b_accuracy = self.dexterity ** 0.75 / 10
        # TODO: Add equipment stats
        return b_accuracy

    @property
    def max_hp(self):
        b_max_hp = round(1 + 0.09 * self.constitution ** 2)
        # TODO: Add equipment stats
        return b_max_hp

    @property
    def damage(self):
        b_damage = round(self.strength ** 0.8)
        # TODO: Add equipment stats
        return b_damage

    @property
    def armor(self):
        b_armor = self.b_armor
        # TODO: Add equipment stats
        return b_armor

    @property
    def resistance(self):
        b_armor_res = self.b_armor_res
        # TODO: Add equipment stats
        return b_armor_res

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.dead()

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def dead(self):
        pass


# Entities
class Player(Entity):
    def __init__(self, w, h, name="player", char="@", color=tcod.yellow,
                 b_armor=0, b_armor_res=0, attributes=(10, 10, 10, 10), equipment={}):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Bat(Entity):
    def __init__(self, w, h, name="bat", char="b", color=tcod.dark_amber,
                 b_armor=0, b_armor_res=0, attributes=(2, 2, 20, 1)):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes)


class GiantBat(Entity):
    def __init__(self, w, h, name="giant bat", char="b", color=tcod.red,
                 b_armor=0, b_armor_res=0, attributes=(3, 3, 19, 1)):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes)


class Rat(Entity):
    def __init__(self, w, h, name="rat", char="r", color=tcod.dark_amber,
                 b_armor=0, b_armor_res=0, attributes=(3, 3, 18, 1)):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes)


class GiantRat(Entity):
    def __init__(self, w, h, name="giant rat", char="r", color=tcod.red,
                 b_armor=0, b_armor_res=0, attributes=(5, 4, 17, 1)):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes)


class Goblin(Entity):
    def __init__(self, w, h, name="goblin", char="o", color=tcod.dark_amber,
                 b_armor=0, b_armor_res=0, attributes=(7, 7, 15, 3), equipment={}):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Hobgoblin(Entity):
    def __init__(self, w, h, name="hobgoblin", char="o", color=tcod.red,
                 b_armor=0, b_armor_res=0, attributes=(9, 9, 8, 3), equipment={}):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Orc(Entity):
    def __init__(self, w, h, name="orc", char="o", color=tcod.dark_yellow,
                 b_armor=0, b_armor_res=0, attributes=(12, 12, 8, 3), equipment={}):
        super().__init__(w, h, name, char, color, b_armor, b_armor_res, attributes, equipment)


def init_entities(game_map):
    """Initialize entities list."""
    entities = [Player(0, 0), Rat(4, 2), GiantRat(4, 4), Bat(6, 2), GiantBat(6, 4), Goblin(8, 2), Hobgoblin(8, 4),
                Orc(8, 6)]
    return entities
