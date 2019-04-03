from tcod import event


def handle_events():
    blocking = True
    while blocking:
        for x in event.get():
            if x.type == "QUIT":
                return "quit"
            elif x.type == "KEYDOWN":
                return handle_keydown(x.scancode, x.mod)
            else:
                continue


def handle_keydown(key, mod):
    if key in range(89, 98):
        direction = {89: "SW", 90: "S", 91: "SE", 92: "W", 93: "STAY", 94: "E", 95: "NW", 96:  "N", 97: "NE"}
        return "move {}".format(direction[key])  # NUM_5 only works with numlock on (returns different code)
    # elif key == 4:
    #     return "toggle"
    else:
        return key, mod


'''
LSHIFT		1
RSHIFT		2
LCTRL		64
RCTRL		128
LALT		256
RALT		512
LGUI		1024 left win/meta
RGUI		2048 right win/meta
NUMLOCK		4096
CAPSLOCK	8192
'''
