from dataclasses import dataclass
from dataclasses import field

from .entity import Entity


@dataclass
class Creature(Entity):
    hp: int = field(init=False)
    constitution: int
    strength: int
    dexterity: int
    intelligence: int
    b_armor: float
    b_armor_res: float
    # equipment: dict = field(default_factory=dict)

    def __post_init__(self):
        self.hp = self.max_hp

    @property
    def evasion(self) -> float:
        b_evasion = self.dexterity**0.7 / 20
        return b_evasion

    @property
    def accuracy(self) -> float:
        b_accuracy = self.dexterity**0.75 / 10
        return b_accuracy

    @property
    def max_hp(self) -> int:
        b_max_hp = round(1 + 0.09 * self.constitution**2)
        return b_max_hp

    @property
    def damage(self) -> int:
        b_damage = round(self.strength**0.8)
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
@dataclass
class Player(Creature):
    name: str = "player"
    graphic = (ord("@"), (255, 255, 0, 255), (0, 0, 0, 0))
    constitution: int = 10
    strength: int = 10
    dexterity: int = 10
    intelligence: int = 10
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Bat(Creature):
    name: str = "bat"
    graphic = (ord("b"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 2
    strength: int = 2
    dexterity: int = 20
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class GiantBat(Creature):
    name: str = "giant bat"
    graphic = (ord("b"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 3
    strength: int = 3
    dexterity: int = 19
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Rat(Creature):
    name: str = "rat"
    graphic = (ord("r"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 3
    strength: int = 3
    dexterity: int = 18
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class GiantRat(Creature):
    name: str = "giant rat"
    graphic = (ord("r"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 5
    strength: int = 4
    dexterity: int = 17
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Goblin(Creature):
    name: str = "goblin"
    graphic = (ord("o"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 7
    strength: int = 7
    dexterity: int = 15
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Hobgoblin(Creature):
    name: str = "hobgoblin"
    graphic = (ord("o"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 9
    strength: int = 9
    dexterity: int = 8
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Orc(Creature):
    name: str = "orc"
    graphic = (ord("o"), (191, 191, 0, 255), (0, 0, 0, 0))
    constitution: int = 12
    strength: int = 12
    dexterity: int = 8
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0
