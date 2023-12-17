class Entity:
    def __init__(self, x: int, y: int, name: str, char: str, color, b_armor: float, 
                 b_armor_res: float, attributes: list[int], equipment: dict={}):
        self.x = x
        self.y = y
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
    def evasion(self) -> float:
        b_evasion = self.dexterity ** 0.7 / 20
        return b_evasion

    @property
    def accuracy(self) -> float:
        b_accuracy = self.dexterity ** 0.75 / 10
        return b_accuracy

    @property
    def max_hp(self) -> int:
        b_max_hp = round(1 + 0.09 * self.constitution ** 2)
        return b_max_hp

    @property
    def damage(self) -> int:
        b_damage = round(self.strength ** 0.8)
        return b_damage

    @property
    def armor(self) -> float:
        b_armor = self.b_armor
        return b_armor

    @property
    def resistance(self) -> float:
        b_armor_res = self.b_armor_res
        return b_armor_res

    def take_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self._dead()

    def heal(self, amount: int):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def _dead(self):
        pass


# Entities
class Player(Entity):
    def __init__(self, x, y, name="player", char="@", color=(255, 255, 0),
                 b_armor=0, b_armor_res=0, attributes=(10, 10, 10, 10), equipment={}):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Bat(Entity):
    def __init__(self, x, y, name="bat", char="b", color=(191, 143, 0),
                 b_armor=0, b_armor_res=0, attributes=(2, 2, 20, 1)):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes)


class GiantBat(Entity):
    def __init__(self, x, y, name="giant bat", char="b", color=(255, 0, 0),
                 b_armor=0, b_armor_res=0, attributes=(3, 3, 19, 1)):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes)


class Rat(Entity):
    def __init__(self, x, y, name="rat", char="r", color=(191, 143, 0),
                 b_armor=0, b_armor_res=0, attributes=(3, 3, 18, 1)):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes)


class GiantRat(Entity):
    def __init__(self, x, y, name="giant rat", char="r", color=(255, 0, 0),
                 b_armor=0, b_armor_res=0, attributes=(5, 4, 17, 1)):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes)


class Goblin(Entity):
    def __init__(self, x, y, name="goblin", char="o", color=(191, 143, 0),
                 b_armor=0, b_armor_res=0, attributes=(7, 7, 15, 3), equipment={}):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Hobgoblin(Entity):
    def __init__(self, x, y, name="hobgoblin", char="o", color=(255, 0, 0),
                 b_armor=0, b_armor_res=0, attributes=(9, 9, 8, 3), equipment={}):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes, equipment)


class Orc(Entity):
    def __init__(self, x, y, name="orc", char="o", color=(191, 191, 0),
                 b_armor=0, b_armor_res=0, attributes=(12, 12, 8, 3), equipment={}):
        super().__init__(x, y, name, char, color, b_armor, b_armor_res, attributes, equipment)
