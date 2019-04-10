import entity
from combat import attack
from event_handler import handle_events


def process_step(game_map, entities):
    action = handle_events()
    _update(game_map, entities, action)


def _update(game_map, entities, action):
    # If the player closes the window raise SystemExit.
    if action.name == "quit":
        raise SystemExit()
    # If command was invalid do something.
    if action.name == "invalid":
        _invalid(action.param)
    else:
        # Update the game if the command was valid.
        if action.name == "move":
            _move(game_map, entities, action)
        if action.name == "stay":
            pass
        if action.name == "interact":
            _interact()
        if action.name == "loot":
            _loot()

        # At the end of checking actions process turns for other entities.


def _invalid(param):
    print("Invalid command: {}".format(param))


def _move(game_map, entities, action):
    player = get_player(entities)
    index = get_entity_index(player.w, player.h, entities)
    dw, dh = action.param
    nw, nh = player.w + dw, player.h + dh
    if game_map.is_walkable(nw, nh) and not occupied(nw, nh, entities):
        player.w, player.h = nw, nh
        pass
    elif occupied(nw, nh, entities):
        attack(index, get_entity_index(nw, nh, entities), entities)


def _interact():
    print("interact")


def _loot():
    print("loot")


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
