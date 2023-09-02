# Do not modify this file, or you will be unable to acquire data!
import pickle


def load_creatures_as_lists() -> list[list[str]]:
    """Loads the binary data file containing a list of creatures, as lists."""
    with open('creatures.pkl', 'rb') as f:
        creatures = pickle.load(f)
    return creatures


try:
    from creature import list_to_creature

    CREATURES = [list_to_creature(creature_data) for creature_data in load_creatures_as_lists()]
    CREATURES_SUBSET = [CREATURES[i] for i in [0, 3, 6, 22, 23, 51, 81, 146, 148, 149]]
except (SyntaxError, IndexError, ImportError, NameError):
    CREATURES = []
    CREATURES_SUBSET = []