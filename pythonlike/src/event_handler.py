import tcod.event
from tcod.event import KeySym


class Action:
    def __init__(self, name: str, param=None):
        self.name = name
        self.param = param


def handle_events():
    """Wait for user input and return an Action object."""
    while True:
        for event in tcod.event.wait():
            # print(event)
            match event:
                case tcod.event.Quit():
                    return Action("quit")
                case tcod.event.KeyDown():
                    return _handle_keydown(event)


def _handle_keydown(event: tcod.event.KeyDown) -> Action:
    key = event.sym

    if key in commands:
        return commands[key]
    else:
        return Action("invalid", (key))


commands = {
    # Movement
    KeySym.KP_1: Action("move", (-1, 1)),
    KeySym.KP_2: Action("move", (0, 1)),
    KeySym.KP_3: Action("move", (1, 1)),
    KeySym.KP_4: Action("move", (-1, 0)),
    KeySym.KP_5: Action("stay"),
    KeySym.KP_6: Action("move", (1, 0)),
    KeySym.KP_7: Action("move", (-1, -1)),
    KeySym.KP_8: Action("move", (0, -1)),
    KeySym.KP_9: Action("move", (1, -1)),

    KeySym.KP_0: Action("interact"),
    KeySym.KP_PERIOD: Action("loot"),
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
