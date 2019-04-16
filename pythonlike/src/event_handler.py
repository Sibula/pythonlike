from tcod import event


class Action:
    def __init__(self, name, param=None):
        self.name = name
        self.param = param


def handle_events():
    """Wait for user input and return an Action object."""
    while True:
        for ev in event.wait():
            if ev.type == "QUIT":
                return Action("quit")
            elif ev.type == "KEYDOWN":
                return _handle_keydown(ev.scancode, ev.mod)


def _handle_keydown(key, mod):
    if key in commands:
        return commands[key]
    else:
        return Action("invalid", (key, mod))


commands = {
    # Movement
    89: Action("move", (-1, 1)),   # KP_1
    90: Action("move", (0, 1)),    # KP_2
    91: Action("move", (1, 1)),    # KP_3
    92: Action("move", (-1, 0)),   # KP_4
    93: Action("stay"),            # KP_5 NUMLOCK ON
    156: Action("stay"),           # KP_5 NUMLOCK OFF
    94: Action("move", (1, 0)),    # KP_6
    95: Action("move", (-1, -1)),  # KP_7
    96: Action("move", (0, -1)),   # KP_8
    97: Action("move", (1, -1)),   # KP_9

    98: Action("interact"),        # KP_0
    99: Action("loot")             # KP_PERIOD
}

# HJKLYUBN  VI move
# .         VI stay
# SPACE     VI interact
# ,         VI loot
# ENTER     VI confirm
# BACKSPACE VI cancel
# ESC       menu (save, quit, help, ...)
# i         inventory (equip, unequip, use, drop, eat, ...)
# a         aim
# NUM_ENTER confirm
# NUM_PLUS  cancel
# f         interact with force
# m         magic
# x         exchange weapons (melee and ranged)
# s         search for hidden things (traps, doors, ...)

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
