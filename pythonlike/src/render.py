import tcod
import numpy as np
from game_map import Tile


def render(console, game_map, entities=None):
    # render = np.full_like(m.tiles, chr(32))
    # render = render_map(render, m)
    # render = render_entities(render, entities)

    console.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    # TODO: Make console draw things
    # c.put_char(40, 25, ord("@"))
    render_map(console, game_map)
    tcod.console_flush()


def render_map(console, game_map):
    # TODO: Make a drawable array of static map elements in a format console can draw
    # r = render

    for (w, h), tile in np.ndenumerate(game_map.tiles):
        # r[w, h] = tile.char
        console.print(w, h, tile.char, tile.color)

    # return r


def render_entities(render, entities):
    # for entity in entities:
        # TODO: Edit array "render" to show entity
        # pass
    return ""
