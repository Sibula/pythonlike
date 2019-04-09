import entity
from combat import attack


def update(game_map, entities, action):
    """Update game_map and entities according to player action."""
    if action.name == "invalid":
        _invalid(action.param)

    if action.name == "move":
        _move(game_map, entities, action)


def _invalid(param):
    print("Invalid command: {}".format(param))


def _move(game_map, entities, action):
    for i, ent in enumerate(entities):
        if type(ent) == entity.Player:
            dw, dh = action.param
            nw, nh = entities[i].w + dw, entities[i].h + dh
            if game_map.is_walkable(nw, nh) and not occupied(nw, nh, entities):
                entities[i].w, entities[i].h = nw, nh
            elif occupied(nw, nh, entities):
                print("You attack the {}".format(get_entity(nw, nh, entities).name))
                attack(i, get_entity_index(nw, nh, entities), entities)


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
