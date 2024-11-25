from abc import ABC
from dataclasses import dataclass, field

from .util import GraphicType


@dataclass
class Entity(ABC):
    x: int
    y: int
    name: str
    graphic: GraphicType = field(init=False)
