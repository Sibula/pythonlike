from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field

from .entity import Entity


@dataclass
class Object(Entity):
    transparent: bool = field(init=False)
    walkable: bool = field(init=False)

    @abstractmethod
    def interact(self):
        pass


@dataclass
class Door(Object):
    name: str = "door"
    open: bool = False

    @property
    def graphic(self):
        if self.open:
            return (ord("_"), (191, 143, 0, 255), (0, 0, 0, 0))
        else:
            return (ord("+"), (191, 143, 0, 255), (0, 0, 0, 0))

    @property
    def transparent(self):
        return self.open

    @property
    def walkable(self):
        return self.open

    def interact(self):
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
