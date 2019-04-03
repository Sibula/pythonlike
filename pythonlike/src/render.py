import tcod
import numpy as np


def render(console, game_map, entities):
    console.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    render_map(console, game_map)
    render_entities(console, entities)
    tcod.console_flush()


def render_map(console, game_map):
    for (w, h), tile in np.ndenumerate(game_map.tiles):
        console.print(w, h, tile.char, tile.color)


def render_entities(console, entities):
    for entity in entities:
        console.print(entity.w, entity.h, entity.char, entity.color)
