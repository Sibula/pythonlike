import random

from entity import Entity


def attack(attacker_i: int, defender_i: int, entities: list[Entity]) -> str:
    attacker = entities[attacker_i]
    defender = entities[defender_i]

    # Calculate values
    hit_chance = attacker.accuracy * (1 - defender.evasion)
    bypass_armor_chance = 1 - defender.armor
    damage_normal = attacker.damage
    damage_armor = attacker.damage * (1 - defender.resistance)

    # Calculate result from values
    kill = False
    damage = None

    hit = True if hit_chance > random.random() else False
    if hit:
        hit_armor = False if bypass_armor_chance > random.random() else True
        if hit_armor:
            damage = damage_armor
        else:
            damage = damage_normal
        entities[defender_i].take_damage(damage)
        if defender.hp < 1:
            kill = True

    message = construct_message(defender.name, hit, damage, kill)

    if kill:
        entities.pop(defender_i)

    return message


def construct_message(defender_name: str, hit: bool, damage: int, kill: bool) -> str:
    if hit:
        message = "You hit the {} for {} damage.".format(defender_name, damage)
    else:
        message = "You missed the {}.".format(defender_name)
    if kill:
        message += " The {} died.".format(defender_name)
    return message


# Should we have a class for combat results?
