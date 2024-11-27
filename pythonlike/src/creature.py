from dataclasses import dataclass, field

from .entity import Entity
from .util import GraphicType


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

    def __post_init__(self) -> None:
        self.hp = self.max_hp

    @property
    def evasion(self) -> float:
        return self.dexterity**0.7 / 20

    @property
    def accuracy(self) -> float:
        return self.dexterity**0.75 / 10

    @property
    def max_hp(self) -> int:
        return round(1 + 0.09 * self.constitution**2)

    @property
    def damage(self) -> int:
        return round(self.strength**0.8)

    @property
    def armor(self) -> float:
        return self.b_armor

    @property
    def resistance(self) -> float:
        return self.b_armor_res

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self._dead()

    def heal(self, amount: int) -> None:
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def _dead(self) -> None:  # TODO
        pass


# Entities
@dataclass
class Player(Creature):
    name: str = "player"
    _graphic: GraphicType = (ord("@"), (255, 255, 0, 255), (0, 0, 0, 0))
    constitution: int = 10
    strength: int = 10
    dexterity: int = 10
    intelligence: int = 10
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Bat(Creature):
    name: str = "bat"
    _graphic: GraphicType = (ord("b"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 2
    strength: int = 2
    dexterity: int = 20
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class GiantBat(Creature):
    name: str = "giant bat"
    _graphic: GraphicType = (ord("b"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 3
    strength: int = 3
    dexterity: int = 19
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Rat(Creature):
    name: str = "rat"
    _graphic: GraphicType = (ord("r"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 3
    strength: int = 3
    dexterity: int = 18
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class GiantRat(Creature):
    name: str = "giant rat"
    _graphic: GraphicType = (ord("r"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 5
    strength: int = 4
    dexterity: int = 17
    intelligence: int = 1
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Goblin(Creature):
    name: str = "goblin"
    _graphic: GraphicType = (ord("o"), (191, 143, 0, 255), (0, 0, 0, 0))
    constitution: int = 7
    strength: int = 7
    dexterity: int = 15
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Hobgoblin(Creature):
    name: str = "hobgoblin"
    _graphic: GraphicType = (ord("o"), (255, 0, 0, 255), (0, 0, 0, 0))
    constitution: int = 9
    strength: int = 9
    dexterity: int = 8
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0


@dataclass
class Orc(Creature):
    name: str = "orc"
    _graphic: GraphicType = (ord("o"), (191, 191, 0, 255), (0, 0, 0, 0))
    constitution: int = 12
    strength: int = 12
    dexterity: int = 8
    intelligence: int = 3
    b_armor: float = 0
    b_armor_res: float = 0
