import random
from abc import ABC, abstractmethod
from dataclasses import dataclass

from .creature import Creature
from .entity import Entity
from .game_map import GameMap
from .object import Object

# Abstract actions


@dataclass
class Action(ABC):
    entity: Entity
    game_map: GameMap

    @abstractmethod
    def perform(self) -> str | None:
        """Perform the action."""
        pass


@dataclass
class DirectedAction(Action):
    dx: int
    dy: int

    @property
    def dest(self) -> tuple[int, int]:
        """Return the (x, y) coordinates of the destination."""
        return self.entity.x + self.dx, self.entity.y + self.dy

    @property
    def target_creature(self) -> Entity | None:
        """Return the creature at the destination or None"""
        return self.game_map.get_creature(*self.dest)

    @abstractmethod
    def perform(self) -> str | None:
        pass


# Actions


@dataclass
class Bump(DirectedAction):
    def perform(self) -> str | None:
        if self.game_map.tiles[*self.dest]["walkable"]:
            ent = self.game_map.get_blocking_entity(*self.dest)
            match ent:
                case None:
                    return Move(self.entity, self.game_map, self.dx, self.dy).perform()
                case Creature():
                    return Melee(self.entity, self.game_map, self.dx, self.dy).perform()
                case Object():
                    return ent.interact()

        return None


@dataclass
class Interact(Action):
    def perform(self) -> str:
        return "interact"


@dataclass
class InvalidAction(Action):
    def perform(self) -> None:
        # Could log these or something?
        pass


@dataclass
class Loot(Action):
    def perform(self) -> str:
        return "loot"


@dataclass
class Melee(DirectedAction):
    def perform(self) -> str | None:
        target = self.target_creature
        if target:
            return resolve_attack(self.entity, target, self.game_map.creatures)
            # Other melee targets, like doors etc.
        return None


@dataclass
class Move(DirectedAction):
    def perform(self) -> None:
        self.entity.x += self.dx
        self.entity.y += self.dy


@dataclass
class Quit(Action):
    def perform(self) -> None:
        raise SystemExit


@dataclass
class Stay(Action):
    def perform(self) -> None:
        pass


# Combat stuff


@dataclass
class CombatResult:
    attacker: Entity
    defender: Entity
    hit: bool = False
    hit_armor: bool = False
    damage: int = 0
    kill: bool = False


def resolve_attack(attacker: Entity, defender: Entity, entities: list[Entity]) -> str:
    # FIXME: Quick hack to make type checking pass, requires refactoring
    if not isinstance(attacker, Creature) or not isinstance(defender, Creature):
        return "Invalid attack: Attacker and defenced must be creatures"

    # Calculate values
    hit_chance = attacker.accuracy * (1 - defender.evasion)
    hit_armor_chance = defender.armor
    normal_damage = attacker.damage
    armor_damage = round(attacker.damage * (1 - defender.resistance))

    # Calculate result from values
    result = CombatResult(attacker, defender)
    result.hit = hit_chance > random.random()
    if result.hit:
        result.hit_armor = hit_armor_chance > random.random()
        result.damage = armor_damage if result.hit_armor else normal_damage
        defender.take_damage(result.damage)
        if defender.hp < 1:
            result.kill = True

    message = attack_message(result)

    if result.kill:
        entities.remove(defender)

    return message


def attack_message(result: CombatResult) -> str:
    att_str = (
        "you" if result.attacker.name == "player" else f"the {result.attacker.name}"
    )
    def_str = (
        "you" if result.defender.name == "player" else f"the {result.defender.name}"
    )

    if result.hit:
        message = f"{att_str} hit {def_str} for {result.damage} damage. ".capitalize()
        if result.kill:
            message += f"{def_str} died.".capitalize()
    else:
        message = f"{att_str} missed {def_str}.".capitalize()

    return message
