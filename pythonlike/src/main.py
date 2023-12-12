from collections import deque
from tcod import libtcodpy, console
import entity
from game_map import GameMap
from render import render
from game import process_step


def initialize():
    # Set variables
    root_width, root_height = 100, 55
    game_width, game_height = 80, 40
    log_width, log_height = 80, 15
    info_width, info_height = 20, 55
    map_width, map_height = game_width, game_height
    libtcodpy.sys_set_fps(20)

    # Initialize consoles
    libtcodpy.console_set_custom_font("data/terminal12x12_gs_ro.png",
                                 libtcodpy.FONT_TYPE_GRAYSCALE | libtcodpy.FONT_LAYOUT_ASCII_INROW)
    root = libtcodpy.console_init_root(root_width, root_height, "pythonlike", False, libtcodpy.RENDERER_SDL2, "F")
    game = console.Console(game_width, game_height, "F")
    log = console.Console(log_width, log_height, "F")
    info = console.Console(info_width, info_height, "F")

    # Initialize game objects
    game_map = GameMap(map_width, map_height)
    entities = entity.init_entities(game_map)
    message_log = deque((log_height - 2)*[], log_height - 2)

    # Initial rendering of the map
    render(root, game, log, info, game_map, entities, message_log)

    return root, game, log, info, game_map, entities, message_log


def main():
    # Initialize
    root, game, log, info, game_map, entities, message_log = initialize()

    while True:
        # Take input and update game
        message_log = process_step(game_map, entities, message_log)

        # Render game
        render(root, game, log, info, game_map, entities, message_log)


if __name__ == "__main__":
    main()
