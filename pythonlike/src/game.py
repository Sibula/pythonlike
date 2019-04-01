import tcod
from tcod import event


def initialize():
    c_width, c_height = 80, 50

    tcod.console_set_custom_font("data/arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(c_width, c_height, title="pythonlike", fullscreen=False, renderer=tcod.RENDERER_SDL2)

    # TODO: Render initial map


def event_handler():
    for x in event.get():
        if x.type == "QUIT":
            return "quit"
        elif x.type == "KEYDOWN":
            key = x.scancode
            return key
        else:
            pass
    return None


def update(events):
    # tcod.console_clear(0)
    pass


def render():
    pass


def main():
    initialize()
    game = True
    while game:
        action = event_handler()
        if action == "quit":
            print("quit")
            game = False
        elif action:
            print(action)
        # update(events)
        # render()


if __name__ == "__main__":
    main()
