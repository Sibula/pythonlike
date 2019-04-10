import random


def attack(attacker_i, defender_i, entities):
    attacker = entities[attacker_i]
    defender = entities[defender_i]

    # Calculate values
    # TODO: Implement equipment and add them to the calculations
    # TODO: Limit maximum values for accuracy, armor, and resistance
    # Hit chance = (base accuracy * weapon modifier) * size modifier
    hit_chance = attacker.accuracy * defender.size
    # Bypass armor chance = (base accuracy * weapon modifier) / armor rating (chance to hit armor)
    bypass_armor_chance = attacker.accuracy * (1 - defender.armor)
    # Damage = (base damage * weapon modifier) / base resistance (for each damage type)
    damage_normal = attacker.damage * (1 - defender.resistance)
    # Damage on armor = (base damage * weapon modifier) / (base resistance + armor resistance) (for each damage type)
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
        entities[defender_i].hp -= damage
        if defender.hp < 1:
            kill = True

    print(construct_message(defender.name, hit, damage, kill))

    if kill:
        entities.pop(defender_i)


def construct_message(defender_name, hit, damage, kill):
    if hit:
        message = "You hit the {} for {} damage.".format(defender_name, damage)
    else:
        message = "You missed the {}.".format(defender_name)
    if kill:
        message += " The {} died.".format(defender_name)
    return message


# Should we have a class for combat results?
