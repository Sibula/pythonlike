import tcod

from event_handler import handle_events
from game_map import GameMap
from render import render


def initialize():
    # Set variables
    c_width, c_height = 80, 50
    m_width, m_height = c_width, c_height

    # Initialize console
    tcod.console_set_custom_font("data/arial10x10.png", tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    console = tcod.console_init_root(c_width, c_height, "pythonlike", False, tcod.RENDERER_SDL2, "F")

    # Initialize map
    game_map = GameMap(m_width, m_height)

    # Initial rendering of the map
    render(console, game_map)

    return console, game_map


def main():
    # Initialize
    console, game_map = initialize()

    while True:
        # Process input
        action = handle_events()
        if action == "quit":
            print("quit")
            break
        elif action:
            print(action)

        # Update game
        # TODO: Updater

        # Render game
        render(console, game_map)


if __name__ == "__main__":
    main()
