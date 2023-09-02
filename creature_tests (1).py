import unittest

from creature import Creature, list_to_creature


class CreatureTests(unittest.TestCase):
    # These test are for your checkpoint, please do not modify them!
    def test_creature_eq_01(self):
        creature1 = Creature('Dinospore', ['nature'], 0.6, 8.08, 255, 117, 79, 100, 69, False,
                             'A small dinosaur that has a symbiotic relationship with a plant.')
        creature2 = Creature('Dinospore', ['nature'], 0.6, 8.08, 255, 117, 79, 100, 69, False,
                             'A small dinosaur that has a symbiotic relationship with a plant.')
        self.assertEqual(creature1, creature2)

    def test_creature_eq_02(self):
        creature1 = Creature('Neptunea', ['water', 'nature'], 1.7, 65.35, 153, 225, 189, 255, 172, True,
                             'Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep '
                             'sea, and it has the ability to predict upcoming events.')
        creature2 = Creature('Neptunea', ['water', 'nature'], 1.7, 65.35, 153, 225, 189, 255, 172, True,
                             'Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep '
                             'sea, and it has the ability to predict upcoming events.')
        self.assertEqual(creature1, creature2)

    def test_creature_repr_01(self):
        creature = Creature('Dinospore', ['nature'], 0.6, 8.08, 255, 117, 79, 100, 69, False,
                            'A small dinosaur that has a symbiotic relationship with a plant.')
        self.assertEqual(repr(creature),
                         "Creature('Dinospore',['nature'],0.6,8.08,255,117,79,100,69,False,'A small dinosaur that has "
                         "a symbiotic relationship with a plant.')")

    def test_creature_repr_02(self):
        creature = Creature('Neptunea', ['water', 'nature'], 1.7, 65.35, 153, 225, 189, 255, 172, True,
                            'Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep '
                            'sea, and it has the ability to predict upcoming events.')
        self.assertEqual(repr(creature),
                         "Creature('Neptunea',['water', 'nature'],1.7,65.35,153,225,189,255,172,True,'Neptunea is a "
                         "serene aquatic creature. Its melodies are said to resonate with the deep sea, and it has "
                         "the ability to predict upcoming events.')")

    def test_list_to_creature_01(self):
        creature = Creature('Dinospore', ['nature'], 0.6, 8.08, 255, 117, 79, 100, 69, False,
                            'A small dinosaur that has a symbiotic relationship with a plant.')
        data = ['1', 'Dinospore', 'nature', '', '0.60', '8.08', '255', '117', '79', '100', '69', 'no',
                'A small dinosaur that has a symbiotic relationship with a plant.']
        self.assertEqual(creature, list_to_creature(data))

    def test_list_to_creature_02(self):
        creature = Creature('Neptunea', ['water', 'nature'], 1.7, 65.35, 153, 225, 189, 255, 172, True,
                            'Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep '
                            'sea, and it has the ability to predict upcoming events.')
        data = ['145', 'Neptunea', 'water', 'nature', '1.70', '65.35', '153', '225', '189', '255', '172', 'yes',
                'Neptunea is a serene aquatic creature. Its melodies are said to resonate with the deep sea, '
                'and it has the ability to predict upcoming events.']
        self.assertEqual(creature, list_to_creature(data))


if __name__ == '__main__':
    unittest.main()
