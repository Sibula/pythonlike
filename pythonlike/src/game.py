import tcod

from event_handler import handle_events


def initialize():
    c_width, c_height = 80, 50

    tcod.console_set_custom_font("data/arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    c = tcod.console_init_root(c_width, c_height, "pythonlike", False, tcod.RENDERER_SDL2, "F")

    # TODO: Create and populate map

    c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    # TODO: Render map
    tcod.console_flush()

    return c


def update(events):
    pass


def render(c):
        c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
        c.put_char(40, 25, ord("@"))
        tcod.console_flush()


def main():
    c = initialize()
    print("Initialized")
    game = True
    while game:
        action = handle_events()
        if action == "quit":
            print("quit")
            game = False
        elif action:
            print(action)
        print("Event handled")
        # update(events)
        render(c)


if __name__ == "__main__":
    main()
