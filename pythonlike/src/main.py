import tcod

import entity
from game_map import GameMap
from render import render
from game import process_step


def initialize():
    # Set variables
    c_width, c_height = 80, 50
    m_width, m_height = c_width, c_height

    # Initialize console
    tcod.console_set_custom_font("data/terminal12x12_gs_ro.png",
                                 tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_ASCII_INROW)
    console = tcod.console_init_root(c_width, c_height, "pythonlike", False, tcod.RENDERER_SDL2, "F")

    # Initialize map
    game_map = GameMap(m_width, m_height)

    # Initialize entities
    entities = entity.init_entities(game_map)

    # Initial rendering of the map
    render(console, game_map, entities)

    return console, game_map, entities


def main():
    # Initialize
    console, game_map, entities = initialize()

    while True:
        # Take input and update game
        process_step(game_map, entities)

        # Render game
        render(console, game_map, entities)


if __name__ == "__main__":
    main()