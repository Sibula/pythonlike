from abc import ABC
from dataclasses import dataclass, field

from .util import GraphicType


@dataclass
class Entity(ABC):
    x: int
    y: int
    name: str
    _graphic: GraphicType = field(init=False)

    @property
    def graphic(self) -> GraphicType:
        return self._graphic
