import random
import tcod
import tcod.map
import tcod.bsp
import numpy as np


class GameMap:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.tcod_map = tcod.map.Map(w, h)
        self.tiles = generate_map(w, h)
        self.explored = np.zeros_like(self.tiles)

    def is_walkable(self, w, h):
        return self.tiles[w, h].walkable


class Tile:
    def __init__(self, char, color, transparent, walkable):
        self.char = char
        self.color = color
        self.transparent = transparent
        self.walkable = walkable


class Room:
    def __init__(self, x_min, y_min, x_max, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    @property
    def candidates(self):
        candidates = []
        for x in range(self.x_min, self.x_max):
            candidates.append((x, self.y_min - 2))
            candidates.append((x, self.y_max + 2))
        for y in range(self.y_min, self.y_max):
            candidates.append((self.x_min - 2, y))
            candidates.append((self.x_max + 2, y))

        return candidates


def generate_map(m_width, m_height):
    min_size = 3
    max_size = 15
    tiles = np.full((m_width, m_height), Empty())  # Initialize empty map.
    rooms = [create_room(min_size, max_size, m_width, m_height, [])]  # Create first room.
    for _ in range(5):
        expandable = random.choice(rooms)
        start_tile = random.choice(expandable.candidates)
        direction = check_dir(start_tile[0], start_tile[1], expandable)
        print(start_tile, direction)

    return tile_map(tiles, rooms)


def create_room(min_size, max_size, m_width, m_height, rooms):
    # Bounds for the top-left coordinates.
    x_min, y_min = 1, 1
    x_max, y_max = m_width - min_size - 1, m_height - min_size - 1

    # Randomize room position and size.
    x_min = random.randint(x_min, x_max)
    y_min = random.randint(y_min, y_max)
    x_max = random.randint(x_min + min_size, x_min + max_size)
    y_max = random.randint(y_min + min_size, y_min + max_size)

    # Make the room smaller if it doesn't fit.
    while x_max > m_width - 2 or y_max > m_height - 2:
        if x_max > m_width - 2:
            x_max -= 1
        if y_max > m_height - 2:
            y_max -= 1
    
    # Retry if the room is below minimum size.
    if x_max - x_min < min_size or y_max - y_min < min_size:
        return create_room(min_size, max_size, m_width, m_height, rooms)

    return Room(x_min, y_min, x_max, y_max)


def tile_map(tiles, rooms):
    for room in rooms:
        for x in range(room.x_min, room.x_max + 1):
            for y in range(room.y_min, room.y_max + 1):
                tiles[x, y] = Floor()
        for x in range(room.x_min - 1, room.x_max + 2):
            for y in range(room.y_min - 1, room.y_max + 2):
                if x == room.x_min - 1 or x == room.x_max + 1 or y == room.y_min - 1 or y == room.y_max + 1:
                    tiles[x, y] = Wall()

    return tiles


def check_free(x, y, rooms, m_width, m_height):
    free = True
    if 0 <= x < m_width and 0 <= y > m_height:
        for room in rooms:
            if room.x_min <= x <= room.x_max and room.y_min <= y <= room.y_max:
                free = False

    return free


def check_dir(x, y, room):
    if x < room.x_min:
        return "left"
    if x > room.x_max:
        return "right"
    if y < room.y_min:
        return "up"
    if y > room.y_max:
        return  "down"


# Map tiles
class Empty(Tile):
    def __init__(self, char=" ", color=tcod.black, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Floor(Tile):
    def __init__(self, char=".", color=tcod.white, transparent=True, walkable=True):
        super().__init__(char, color, transparent, walkable)


class Wall(Tile):
    def __init__(self, char="#", color=tcod.white, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)


class Door(Tile):
    def __init__(self, char="+", color=tcod.white, transparent=False, walkable=False):
        super().__init__(char, color, transparent, walkable)

    def toggle(self):
        self.char = "_" if self.char == "+" else "+"
        self.transparent = not self.transparent
        self.walkable = not self.walkable
