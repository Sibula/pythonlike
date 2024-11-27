from abc import abstractmethod
from dataclasses import dataclass, field

from .entity import Entity
from .util import GraphicType


@dataclass
class Object(Entity):
    _transparent: bool = field(init=False)
    _walkable: bool = field(init=False)

    @property
    def transparent(self) -> bool:
        return self._transparent

    @property
    def walkable(self) -> bool:
        return self._walkable

    @abstractmethod
    def interact(self) -> None:
        raise NotImplementedError


@dataclass
class Door(Object):
    name: str = "door"
    open: bool = False

    @property
    def graphic(self) -> GraphicType:
        if self.open:
            return (ord("_"), (191, 143, 0, 255), (0, 0, 0, 0))
        return (ord("+"), (191, 143, 0, 255), (0, 0, 0, 0))

    @property
    def transparent(self) -> bool:
        return self.open

    @property
    def walkable(self) -> bool:
        return self.open

    def interact(self) -> None:
        self.open = not self.open


@dataclass
class StairsDown(Object):
    pass


@dataclass
class StairsUp(Object):
    pass


"""
door = new_tile(
    transparent=0,
    walkable=1,
    graphic=(ord("+"), (191, 143, 0, 255), (0, 0, 0, 255))
)

stairs_up = new_tile(
    transparent=1,
    walkable=1,
    graphic=(ord("<"), (255, 255, 255, 255), (0, 0, 0, 255))
)

stairs_down = new_tile(
    transparent=1,
    walkable=1,
    graphic=(ord(">"), (255, 255, 255, 255), (0, 0, 0, 255))
)
"""
