import entity


def update(game_map, entities, action):
    if action.name == "invalid":
        invalid()

    if action.name == "move":
        move(game_map, entities, action)


def invalid():
    print("Invalid command")


def move(game_map, entities, action):
    for i, ent in enumerate(entities):
        if type(ent) == entity.Player:
            dw, dh = action.param
            nw, nh = entities[i].w + dw, entities[i].h + dh
            if game_map.is_walkable(nw, nh) and not occupied(nw, nh, entities):
                entities[i].w, entities[i].h = nw, nh
            elif occupied(nw, nh, entities):
                print("You attack the {}".format(get_entity(nw, nh, entities)))


def occupied(w, h, entities):
    has_entity = False
    for ent_w, ent_h in [(ent.w, ent.h) for ent in entities]:
        if (ent_w, ent_h) == (w, h):
            has_entity = True

    return has_entity


def get_entity(w, h, entities):
    for ent in entities:
        if (ent.w, ent.h) == (w, h):
            return ent.name
