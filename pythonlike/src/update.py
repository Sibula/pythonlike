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
            if game_map.is_walkable(nw, nh):
                entities[i].w, entities[i].h = nw, nh
        break
