import random
import numpy as np
import tile


class Room:
    def __init__(self, x_min, y_min, x_max, y_max, door):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.door = door
        self.stairs_up = None
        self.stairs_down = None

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

    def contains(self, x, y):
        return self.x_min - 1 <= x <= self.x_max + 1 and self.y_min - 1 <= y <= self.y_max + 1

    def interior(self, x, y):
        return self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max


def generate_map(m_width, m_height):
    min_size = 3
    max_size = 15
    tiles = np.full((m_width, m_height), tile.empty)  # Initialize empty map.
    rooms = []  # List to store generated rooms in.
    taken = np.zeros_like(tiles, dtype=int)  # Empty array to store whether a tile belongs to a room.
    taken_ratio = 0  # Ratio of map filled with rooms.
    while taken_ratio < 0.75:
        _create_room(min_size, max_size, m_width, m_height, rooms, taken)
        taken_bincount = np.bincount(taken.flatten(), minlength=2)
        taken_ratio = taken_bincount[1] / (taken_bincount[0] + taken_bincount[1])
    add_stairs(rooms)

    return _tile_map(tiles, rooms)


def _create_room(min_size, max_size, m_width, m_height, rooms, taken):
    if not rooms:
        # Parameters for first room.
        start_tile = None
        x_min = random.randint(1, m_width - min_size - 1)
        y_min = random.randint(1, m_height - min_size - 1)
        x_max = random.randint(x_min + min_size, x_min + max_size)
        y_max = random.randint(y_min + min_size, y_min + max_size)
        door = None
    else:
        # Choose a tile next to an existing room to grow from.
        prev = random.choice(rooms)
        start_tile = random.choice(prev.candidates)
        direction = _check_dir(start_tile, prev)
        # Set parameters depending on direction relative to parent room
        if direction == "left":
            x_max = prev.x_min - 2
            x_min = random.randint(x_max - max_size + 1, x_max - min_size + 1)
            y_min = random.randint(start_tile[1] - max_size + 1, start_tile[1])
            y_max = random.randint(y_min + min_size, y_min + max_size)
            door = (start_tile[0] + 1, start_tile[1])
        elif direction == "right":
            x_min = prev.x_max + 2
            x_max = random.randint(x_min + min_size - 1, x_min + max_size - 1)
            y_min = random.randint(start_tile[1] - max_size + 1, start_tile[1])
            y_max = random.randint(y_min + min_size, y_min + max_size)
            door = (start_tile[0] - 1, start_tile[1])
        elif direction == "up":
            y_max = prev.y_min - 2
            y_min = random.randint(y_max - max_size + 1, y_max - min_size + 1)
            x_min = random.randint(start_tile[0] - max_size + 1, start_tile[0])
            x_max = random.randint(x_min + min_size, x_min + max_size)
            door = (start_tile[0], start_tile[1] + 1)
        else:  # direction == "down"
            y_min = prev.y_max + 2
            y_max = random.randint(y_min + min_size - 1, y_min + max_size - 1)
            x_min = random.randint(start_tile[0] - max_size + 1, start_tile[0])
            x_max = random.randint(x_min + min_size, x_min + max_size)
            door = (start_tile[0], start_tile[1] - 1)

    room = Room(x_min, y_min, x_max, y_max, door)
    # Check if the room passes all conditions.
    proper = _check(room, min_size, m_width, m_height, start_tile, taken)
    if proper:
        rooms.append(room)
        for (x, y) in np.ndindex(taken.shape):
            if room.contains(x, y):
                taken[x, y] = 1


def _check_dir(start_tile, room):
    # Check which direction the new room should grow.
    x, y = start_tile
    if x < room.x_min:
        return "left"
    if x > room.x_max:
        return "right"
    if y < room.y_min:
        return "up"
    if y > room.y_max:
        return "down"


def _check(room, min_size, m_width, m_height, start_tile, taken):
    # Fit inside map
    while room.x_min < 1 or room.y_min < 1 or room.x_max > m_width - 2 or room.y_max > m_height - 2:
        if room.x_min < 1:
            room.x_min += 1
        if room.y_min < 1:
            room.y_min += 1
        if room.x_max > m_width - 2:
            room.x_max -= 1
        if room.y_max > m_height - 2:
            room.y_max -= 1

    # Check if it overlaps with existing rooms
    for x in range(room.x_min, room.x_max + 1):
        for y in range(room.y_min, room.y_max + 1):
            if taken[x, y]:
                return False

    # Check if the starting coordinates are inside the room
    if start_tile:
        if not room.interior(start_tile[0], start_tile[1]):
            return False

    # Check proper size
    if room.x_max - room.x_min < min_size or room.y_max - room.y_min < min_size:
        return False

    return True


def add_stairs(rooms):
    up_room, down_room = random.sample(rooms, 2)
    up_x = random.randint(up_room.x_min, up_room.x_max)
    up_y = random.randint(up_room.y_min, up_room.y_max)
    down_x = random.randint(down_room.x_min, down_room.x_max)
    down_y = random.randint(down_room.y_min, down_room.y_max)
    up_room.stairs_up = (up_x, up_y)
    down_room.stairs_down = (down_x, down_y)


def _tile_map(tiles, rooms):
    # Add the rooms themselves (wall/floor).
    for room in rooms:
        for x in range(room.x_min, room.x_max + 1):
            for y in range(room.y_min, room.y_max + 1):
                tiles[x, y] = tile.floor
        for x in range(room.x_min - 1, room.x_max + 2):
            for y in range(room.y_min - 1, room.y_max + 2):
                if x == room.x_min - 1 or x == room.x_max + 1 or y == room.y_min - 1 or y == room.y_max + 1:
                    tiles[x, y] = tile.wall

    # Add other features.
    for room in rooms:
        if room.door:
            tiles[room.door[0], room.door[1]] = tile.door
        if room.stairs_up:
            tiles[room.stairs_up[0], room.stairs_up[1]] = tile.stairs_up
        if room.stairs_down:
            tiles[room.stairs_down[0], room.stairs_down[1]] = tile.stairs_down

    return tiles
