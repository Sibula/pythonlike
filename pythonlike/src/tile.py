import numpy as np

from .util import GraphicType
from .util import graphic_dtype


tile_dtype = np.dtype(
    [
        ("transparent", bool),
        ("walkable", bool),
        ("graphic", graphic_dtype),
    ]
)


def new_tile(
    transparent: int,
    walkable: int,
    graphic: GraphicType,
) -> np.ndarray:
    return np.array((transparent, walkable, graphic), dtype=tile_dtype)


# Map tiles
empty = new_tile(
    transparent=0, walkable=0, graphic=(ord(" "), (255, 255, 255, 255), (0, 0, 0, 255))
)

floor = new_tile(
    transparent=1, walkable=1, graphic=(ord("."), (159, 159, 159, 255), (0, 0, 0, 255))
)

wall = new_tile(
    transparent=0, walkable=0, graphic=(ord("#"), (159, 159, 159, 255), (0, 0, 0, 255))
)


# Placeholders to keep demo working,
# actually objects when I get around to implement those
door = new_tile(
    transparent=0, walkable=1, graphic=(ord("+"), (191, 143, 0, 255), (0, 0, 0, 255))
)

stairs_up = new_tile(
    transparent=1, walkable=1, graphic=(ord("<"), (255, 255, 255, 255), (0, 0, 0, 255))
)

stairs_down = new_tile(
    transparent=1, walkable=1, graphic=(ord(">"), (255, 255, 255, 255), (0, 0, 0, 255))
)
