from tcod import event


def handle_events():
    for x in event.get():
        if x.type == "QUIT":
            return "quit"
        elif x.type == "KEYDOWN":
            key = x.scancode
            return handle_keydown(key)
        else:
            pass
    return None


def handle_keydown(key):
    if key in range(89, 98):
        direction = {89: "SW", 90: "S", 91: "SE", 92: "W", 93: "STAY", 94: "W", 95: "NW", 96:  "N", 97: "NE"}
        return "move {}".format(direction[key])
    else:
        return key


