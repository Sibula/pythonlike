from collections import deque

from combat import attack
import entity
from event_handler import handle_events, Action
from game_map import GameMap
import tile


def process_step(game_map: GameMap, message_log: deque) -> deque:
    action = handle_events()
    messages = _update(game_map, action)
    for msg in messages:
        if msg:
            message_log.append(msg)

    return message_log


def _update(game_map: GameMap, action: Action) -> list[str]:
    messages = []
    # If the player closes the window raise SystemExit.
    if action.name == "quit":
        raise SystemExit()
    # If command was invalid do something.
    if action.name == "invalid":
        messages.append(_invalid(action.param))
    else:
        # Update the game if the command was valid.
        if action.name == "move":
            messages.append(_move(game_map, action))
        if action.name == "stay":
            messages.append(_stay())
        if action.name == "interact":
            messages.append(_interact())
        if action.name == "loot":
            messages.append(_loot())

        # At the end of checking actions process turns for other entities.
    return messages


def _invalid(param):
    return None  # "Invalid command: {}".format(param)


def _move(game_map: GameMap, action: Action) -> str | None:
    entities = game_map.entities
    player = get_player(entities)
    index = get_entity_index(player.x, player.y, entities)
    dx, dy = action.param
    nx, ny = player.x + dx, player.y + dy
    occupied = is_occupied(nx, ny, entities)
    nt = game_map.tiles[nx, ny]
    if nt["walkable"] and not occupied:
        player.x, player.y = nx, ny
    elif occupied:
        return attack(index, get_entity_index(nx, ny, entities), entities)
    elif nt == tile.door:
        # game_map.tiles[nx, ny].interact()
        pass

def _stay() -> None:
    return None


def _interact() -> str:
    return "interact"


def _loot() -> str:
    return "loot"


def is_occupied(x: int, y: int, entities: list[entity.Entity]) -> bool:
    # Check if the tile at (x, y) is occupied by an entity.
    has_entity = False
    for ent_x, ent_y in [(ent.x, ent.y) for ent in entities]:
        if (ent_x, ent_y) == (x, y):
            has_entity = True

    return has_entity


def get_entity(x: int, y: int, entities: list[entity.Entity]) -> entity.Entity | None:
    # Return entity at (x, y).
    for ent in entities:
        if (ent.x, ent.y) == (x, y):
            return ent


def get_entity_index(x: int, y: int, entities: list[entity.Entity]) -> int | None:
    # Return index of entity at (x, y) in entities.
    for i, ent in enumerate(entities):
        if (ent.x, ent.y) == (x, y):
            return i
    return None


def get_player(entities: list[entity.Entity]) -> entity.Player:
    # Find the Player object from entities and return it.
    for ent in entities:
        if type(ent) == entity.Player:
            return ent
