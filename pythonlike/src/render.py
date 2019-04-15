import tcod
import numpy as np


def render(root, game, log, info, game_map, entities, message_log):
    """Render and draw everything."""
    # Render all consoles.
    _render_map(game, game_map)
    _render_entities(game, entities)
    _render_log(log, message_log)
    _render_info(info)

    # Blit all consoles to root and draw.
    game.blit(root)
    log.blit(root, 0, 40)
    info.blit(root, 80, 0)
    tcod.console_flush()


def _render_map(game, game_map):
    for (w, h), tile in np.ndenumerate(game_map.tiles):
        game.print(w, h, tile.char, tile.color)


def _render_entities(game, entities):
    for entity in entities:
        game.print(entity.w, entity.h, entity.char, entity.color)


def _render_log(log, message_log):
    log.draw_frame(0, 0, 80, 15, "Game Log")
    for i, msg in enumerate(message_log):
        log.print(1, i + 1, msg)


def _render_info(info):
    info.draw_frame(0, 0, 20, 55, "Info")
