from creature import Creature, list_to_creature


def report_creature(Creature) -> None:
    """Function that reports all attributes for a given Creature"""
    print(f'{Creature.name}\n'
          f'\tKIND: {Creature.kinds}\n'
          f'\tHGHT: {Creature.height} (m)\n'
          f'\tWGHT: {Creature.weight} (kg)\n'
          f'\tFRND: {Creature.friendliness}\n'
          f'\tRESI: {Creature.resilience}\n'
          f'\tCOUR: {Creature.courage}\n'
          f'\tWILL: {Creature.willpower}\n'
          f'\tDETR: {Creature.determination}\n'
          f'\tLGND: {Creature.legendary}\n'
          f'\tDESC: {Creature.description}')


def load_creature_text_file(file_path: str) -> list[Creature]:
    """Function that intakes a file of text and coverts it to a list of Creatures"""
    output = []
    with open(file_path) as f:
        for line in f:
            try:
                s = line.strip().split(':')
                c = list_to_creature(s)
                output.append(c)
            except IndexError:
                continue
    return output
