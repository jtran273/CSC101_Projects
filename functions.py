# Copy your Project 3 functions.py code into this file
from creature import Creature


def get_names(db: list[Creature]) -> list[str]:
    """Function 1: A map that returns a list of names for each creature"""
    output = []
    for creature in db:
        y = creature.name
        output.append(y)
    return output


def get_attr(creature: Creature, attr: str) -> int:
    """Function 2: Returns the following Creature attribute level(int) given the following creature and attribute"""
    if attr == "friendliness":
        number = creature.friendliness
    elif attr == "resilience":
        number = creature.resilience
    elif attr == "determination":
        number = creature.determination
    elif attr == "willpower":
        number = creature.willpower
    elif attr == "courage":
        number = creature.courage
    else:
        number = 0
    return number


def avg_attr(db: list[Creature], attr: str) -> float:
    """Function 3: Returns the average level given a certain attribute"""
    if attr not in ["friendliness", "resilience", "determination", "willpower", "courage"]:
        return 0
    total = 0
    count = 0
    for creature in db:
        try:
            level = get_attr(creature, attr)
            total += level
            count += 1
        except TypeError:
            return 0

    if count > 0:
        return total / count
    else:
        return 0


def filter_legendary(db: list[Creature]) -> list[Creature]:
    """Function 4: Filter that returns the names of the creatures that are legendary"""
    output = []
    for creature in db:
        if creature.legendary:
            output.append(creature)
        else:
            continue
    return output


def has_kind(creature: Creature, kind: str) -> bool:
    """Function 5: Function returns bool value "True" if the creature contains the certain kind, returns False if not"""
    i = 0
    while i < len(creature.kinds):
        if creature.kinds[i] == kind:
            return True
        i += 1
    return False


def filter_by_kind(db: list[Creature], kind: str) -> list[Creature]:
    """Function 6: Returns the following creatures correlating to the chosen kind"""
    output = []
    for creature in db:
        if has_kind(creature, kind):
            output.append(creature)
    return output


def filter_out_kind(db: list[Creature], kind: str) -> list[Creature]:
    """Function 7: Returns the following creatures that does not contain the chosen kind"""
    output = []
    for creature in db:
        if not has_kind(creature, kind):
            output.append(creature)
    return output


def percent_by_kind(db: list[Creature], kind: str) -> float:
    """Function 8: Returns the percentage of creature objects with the given kind from the list"""
    top = 0
    bottom = len(db)
    for creature in db:
        if has_kind(creature, kind):
            top += 1
    return (top / bottom) * 100


def filter_by_attr_lt(db: list[Creature], attr: str, lim: int) -> list[Creature]:
    """Function 9: A filter only selects the creatures with a given attribute if it is less than a given limit"""
    output = []
    for creature in db:
        if get_attr(creature, attr) < lim:
            output.append(creature)
    return output


def filter_by_attr_gt(db: list[Creature], attr: str, lim: int) -> list[Creature]:
    """Function 10:  A filter only selects the creatures with a given attribute if it is higher than a given limit"""
    output = []
    for creature in db:
        if get_attr(creature, attr) > lim:
            output.append(creature)
    return output


def get_weight(creature: Creature) -> float:
    """Function 11 (Makeup): Pulls the weight of a creature"""
    return creature.weight


def avg_weight(db: list[Creature]) -> float:
    """Function 12 (Makeup): Calculates the average weight of a list of creature"""
    total_weight = 0
    count = 0

    for creature in db:
        weight = get_weight(creature)
        total_weight += weight
        count += 1

    average_weight = total_weight / count
    return average_weight


def filter_by_weight_lt(db: list[Creature], lim: int):
    """Function 13 (Makeup): Returns only the creatures less than the weight limit"""

    output = []
    for creature in db:
        weight = get_weight(creature)
        if weight < lim:
            output.append(creature)
    return output


def filter_by_weight_gt(db: list[Creature], lim: int):
    """Function 14 (Makeup): Returns only the creatures greater than the weight limit"""

    output = []
    for creature in db:
        weight = get_weight(creature)
        if weight > lim:
            output.append(creature)
    return output
