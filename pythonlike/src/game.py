import entity
from combat import attack
from event_handler import handle_events
from tiles import *


def process_step(game_map, entities, message_log):
    action = handle_events()
    messages = _update(game_map, entities, action)
    for msg in messages:
        if msg:
            message_log.append(msg)

    return message_log


def _update(game_map, entities, action):
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
            messages.append(_move(game_map, entities, action))
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


def _move(game_map, entities, action):
    player = get_player(entities)
    index = get_entity_index(player.x, player.y, entities)
    dx, dy = action.param
    nx, ny = player.x + dx, player.y + dy
    if game_map.is_walkable(nx, ny) and not occupied(nx, ny, entities):
        player.x, player.y = nx, ny
        return None
    elif occupied(nx, ny, entities):
        return attack(index, get_entity_index(nx, ny, entities), entities)
    elif type(game_map.tiles[nx, ny]) == Door:
        game_map.tiles[nx, ny].toggle()


def _stay():
    return None


def _interact():
    return "interact"


def _loot():
    return "loot"


def occupied(x, y, entities):
    # Check if the tile at (x, y) is occupied by an entity.
    has_entity = False
    for ent_x, ent_y in [(ent.x, ent.y) for ent in entities]:
        if (ent_x, ent_y) == (x, y):
            has_entity = True

    return has_entity


def get_entity(x, y, entities):
    # Return entity at (x, y).
    for ent in entities:
        if (ent.x, ent.y) == (x, y):
            return ent


def get_entity_index(x, y, entities):
    # Return index of entity at (x, y) in entities.
    for i, ent in enumerate(entities):
        if (ent.x, ent.y) == (x, y):
            return i
    return None


def get_player(entities):
    # Find the Player object from entities and return it.
    for ent in entities:
        if type(ent) == entity.Player:
            return ent
