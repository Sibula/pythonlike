import tcod
from game_map import Tile


def render(c, game_map, entities=None):
    render = render_map(game_map)
    render = render_entities(render, entities)

    # TODO: Make console "c" draw "render"
    c.clear(ch=ord(" "), fg=tcod.white, bg=tcod.black)
    # c.put_char(40, 25, ord("@"))
    tcod.console_flush()


def render_map(game_map):
    # TODO: Make a drawable array of static map elements in a format console can draw
    return ""


def render_entities(render, entities):
    # for entity in entities:
        # TODO: Edit array "render" to show entity
        # pass
    return ""
