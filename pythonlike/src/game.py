import tcod

from event_handler import handle_events
from game_map import GameMap


def initialize():
    c_width, c_height = 80, 50
    m_width, m_height = 70, 40

    tcod.console_set_custom_font("data/arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    c = tcod.console_init_root(c_width, c_height, "pythonlike", False, tcod.RENDERER_SDL2, "F")

    m = GameMap(m_width, m_height)

    c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    render(c, m)
    tcod.console_flush()

    return c, m


def update(events, m):
    pass


def render(c, m):
        c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
        # c.put_char(40, 25, ord("@"))
        tcod.console_flush()


def main():
    c, m = initialize()
    game = True
    while game:
        action = handle_events()
        if action == "quit":
            print("quit")
            game = False
        elif action:
            print(action)
        # update(events, m)
        render(c, m)


if __name__ == "__main__":
    main()
