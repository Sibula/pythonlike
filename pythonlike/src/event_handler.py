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
    if key in commands:
        return commands[key]
    else:
        return key, mod


commands = {
    # Movement
    89: {"move": (-1, 1)},   # KP_1
    90: {"move": (0, 1)},    # KP_2
    91: {"move": (1, 1)},    # KP_3
    92: {"move": (-1, 0)},   # KP_4
    93: {"move": (0, 0)},    # KP_5 NUMLOCK ON
    156: {"move": (0, 0)},   # KP_5 NUMLOCK OFF
    94: {"move": (1, 0)},    # KP_6
    95: {"move": (-1, -1)},  # KP_7
    96: {"move": (0, -1)},   # KP_8
    97: {"move": (1, -1)}    # KP_9

}
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
