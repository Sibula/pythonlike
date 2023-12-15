from collections import deque
from pathlib import Path
import time

import numpy as np
import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

import entity
from game_map import GameMap
from game import process_step


class Clock:
    def __init__(self) -> None:
        self.last_time = time.perf_counter()  # Last time this was synced.
        self.drift_time = 0.0  # Tracks how much the last frame was overshot.

    def sync(self, fps: float) -> None:
        """Sync to a given framerate."""
        desired_frame_time = 1 / fps
        target_time = self.last_time + desired_frame_time - self.drift_time
        # Sleep might take slightly longer than asked.
        sleep_time = max(0, target_time - self.last_time - 0.001)
        if sleep_time:
            time.sleep(sleep_time)
        # Busy wait until the target_time is reached.
        while (drift_time := time.perf_counter() - target_time) < 0:
            pass
        self.drift_time = min(drift_time, desired_frame_time)
        self.last_time = time.perf_counter()


def render(context: tcod.context.Context, root: tcod.console.Console,
           game: tcod.console.Console, log: tcod.console.Console,
           info: tcod.console.Console, game_map: GameMap,
           entities: list[entity.Entity], message_log: deque):
    """Render and draw everything."""
    # Render all consoles.
    for (x, y), t in np.ndenumerate(game_map.tiles):
        # game.print(x, y, tile.char, tile.color)
        game.rgba[x, y] = t["graphic"]

    for entity in entities:
        game.print(entity.x, entity.y, entity.char, entity.color)

    log.draw_frame(0, 0, 80, 15, "Game Log")
    for i, msg in enumerate(message_log):
        log.print(1, i + 1, msg)

    info.draw_frame(0, 0, 20, 55, "Info")

    # Blit all consoles to root and draw.
    game.blit(root)
    log.blit(root, 0, 40)
    info.blit(root, 80, 0)
    context.present(root)


def main():
    # Set variables
    root_width, root_height = 100, 55
    game_width, game_height = 80, 40
    log_width, log_height = 80, 15
    info_width, info_height = 20, 55
    map_width, map_height = game_width, game_height
    fps = 20

    # Load tileset
    tileset = tcod.tileset.load_tilesheet(
        Path(__file__).resolve().parent / "data" / "terminal12x12_gs_ro.png", 
        columns=16, rows=16, charmap=tcod.tileset.CHARMAP_CP437)
    
    # Initialize consoles
    root = tcod.console.Console(root_width, root_height, order='F')
    game = tcod.console.Console(game_width, game_height, "F")
    log = tcod.console.Console(log_width, log_height, "F")
    info = tcod.console.Console(info_width, info_height, "F")

    # Initialize game objects
    game_map = GameMap(map_width, map_height)
    entities = entity.init_entities(game_map)
    message_log = deque((log_height - 2)*[], log_height - 2)
    
    clock = Clock()

    with tcod.context.new(console=root, tileset=tileset, 
                          title="pythonlike") as context:
        # Initial rendering of the map
        render(context, root, game, log, info, game_map, entities, message_log)

        while True:  # Game loop
            # Sync to fps
            clock.sync(fps=fps)

            # Take input and update game
            message_log = process_step(game_map, entities, message_log)

            # Render game
            render(context, root, game, log, info, game_map, entities, message_log)


if __name__ == "__main__":
    main()
