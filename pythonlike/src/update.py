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
            if is_empty(nw, nh, game_map, entities):
                entities[i].w, entities[i].h = nw, nh
        break


def is_empty(w, h, game_map, entities):
    walkable = game_map.is_walkable(w, h)
    ent_coords = [(ent.w, ent.h) for ent in entities]
    occupied = False
    for ent_w, ent_h in ent_coords:
        if (ent_w, ent_h) == (w, h):
            occupied = True

    return walkable and not occupied
