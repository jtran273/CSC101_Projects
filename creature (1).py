# Copy your Project 3 creature.py code into this file
# Write your class below
class Creature:
    """Represents a creature with many attributes"""

    def __init__(self, name: str, kinds: list[str], height: float, weight: float, friendliness: int, resilience: int,
                 courage: int,
                 willpower: int, determination: int, legendary: bool, description: str):
        self.name = name
        self.kinds = kinds
        self.height = height
        self.weight = weight
        self.friendliness = friendliness
        self.resilience = resilience
        self.courage = courage
        self.willpower = willpower
        self.determination = determination
        self.legendary = legendary
        self.description = description

    def __repr__(self) -> str:
        return f"Creature('{self.name}',{self.kinds},{self.height},{self.weight},{self.friendliness},{self.resilience}," \
               f"{self.courage},{self.willpower},{self.determination},{self.legendary},'{self.description}')"

    def __eq__(self, other: object):
        if other is None:
            return False
        if not isinstance(other, type(self)):
            return False
        return (
                self.name == other.name
                and self.kinds == other.kinds
                and self.height == other.height
                and self.weight == other.weight
                and self.friendliness == other.friendliness
                and self.resilience == other.resilience
                and self.courage == other.courage
                and self.willpower == other.willpower
                and self.determination == other.determination
                and self.legendary == other.legendary
                and self.description == other.description
        )


# Write your class above
def list_to_creature(data: list[str]) -> Creature:
    """Returns the creature represented by a list of string data."""

    # "Kind" data is given as two different strings.
    # However, creature objects store this data as
    # a single list.
    # Because of this, you must append the individual
    # kind(s) to a list for the creature.
    # An empty string ('') represents that a kind isn't used.
    kinds = []

    # Append kinds that are non-empty strings
    # Kind 1
    if data[2] != '':
        kinds.append(data[2])
    # # Kind 2
    if data[3] != '':
        kinds.append(data[3])

    # The legendary status data is given as a string of 'yes' or 'no'.
    # This must be converted to a bool type True or False value.
    if data[11] == "yes":
        legendary = True
    else:
        legendary = False

    height = float(data[4])
    weight = float(data[5])
    friendliness = int(data[6])
    resilience = int(data[7])
    courage = int(data[8])
    willpower = int(data[9])
    determination = int(data[10])

    # Creature __init__ call parameters:
    #  1. name: str
    #  2. *kinds: list[str]
    #  3. height: float
    #  4. weight: float
    #  5. friendliness: int
    #  6. resilience: int
    #  7. courage: int
    #  8. willpower: int
    #  9. determination: int
    # 10. *legendary: bool
    # 11. description: str
    # *already completed for you
    # Note: these don't match the data list indices!
    return Creature(data[1], kinds, height, weight, friendliness, resilience, courage,
                    willpower, determination, legendary, data[12])
