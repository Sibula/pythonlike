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
    index = get_entity_index(player.w, player.h, entities)
    dw, dh = action.param
    nw, nh = player.w + dw, player.h + dh
    if game_map.is_walkable(nw, nh) and not occupied(nw, nh, entities):
        player.w, player.h = nw, nh
        return None
    elif occupied(nw, nh, entities):
        return attack(index, get_entity_index(nw, nh, entities), entities)
    elif type(game_map.tiles[nw, nh]) == Door:
        game_map.tiles[nw, nh].toggle()


def _stay():
    return None


def _interact():
    return "interact"


def _loot():
    return "loot"


def occupied(w, h, entities):
    # Check if the tile at (w, h) is occupied by an entity.
    has_entity = False
    for ent_w, ent_h in [(ent.w, ent.h) for ent in entities]:
        if (ent_w, ent_h) == (w, h):
            has_entity = True

    return has_entity


def get_entity(w, h, entities):
    # Return entity at (w, h).
    for ent in entities:
        if (ent.w, ent.h) == (w, h):
            return ent


def get_entity_index(w, h, entities):
    # Return index of entity at (w, h) in entities.
    for i, ent in enumerate(entities):
        if (ent.w, ent.h) == (w, h):
            return i
    return None


def get_player(entities):
    # Find the Player object from entities and return it.
    for ent in entities:
        if type(ent) == entity.Player:
            return ent
