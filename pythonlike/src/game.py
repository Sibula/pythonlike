import tcod

from event_handler import handle_events
from game_map import GameMap
from render import render


def initialize():
    c_width, c_height = 80, 50
    m_width, m_height = c_width, c_height

    tcod.console_set_custom_font("data/arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    c = tcod.console_init_root(c_width, c_height, "pythonlike", False, tcod.RENDERER_SDL2, "F")

    m = GameMap(m_width, m_height)

    c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    render(c, m)
    tcod.console_flush()

    return c, m


def update(events, m):
    pass


def main():
    c, m = initialize()
    while True:
        action = handle_events()
        if action == "quit":
            print("quit")
            break
        elif action:
            print(action)
        # update(events, m)
        render(c, m)


if __name__ == "__main__":
    main()
