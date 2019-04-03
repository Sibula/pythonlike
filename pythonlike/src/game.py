import tcod

import entity
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

    # Initialize entities
    entities = [entity.Player(0, 0)]

    # Initial rendering of the map
    render(console, game_map, entities)

    return console, game_map, entities


def main():
    # Initialize
    console, game_map, entities = initialize()

    while True:
        # Process input
        action = handle_events()
        if action == "quit":
            print("quit")
            break
        # elif action == "toggle":
        #     game_map.tiles[(5, 5)].toggle()
        elif action:
            print(action)

        # Update game
        # TODO: Updater

        # Render game
        render(console, game_map, entities)


if __name__ == "__main__":
    main()
