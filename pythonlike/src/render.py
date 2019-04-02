import tcod
import numpy as np


def render(console, game_map, entities=None):
    console.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    render_map(console, game_map)
    # TODO: Render entities
    tcod.console_flush()


def render_map(console, game_map):
    for (w, h), tile in np.ndenumerate(game_map.tiles):
        console.print(w, h, tile.char, tile.color)


def render_entities(console, game_map, entities):
    pass
