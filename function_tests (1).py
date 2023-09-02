import unittest

from creature import Creature
from functions import *
from loader import CREATURES
from loader import CREATURES_SUBSET


class FunctionTests(unittest.TestCase):
    # Insert your tests below
    def test_get_names_list(self):  # Function 1
        names = get_names(CREATURES_SUBSET)
        expected = 'Dinospore'
        self.assertEqual(expected, names[0])

    def test_get_name_subset(self):  # Function 1
        names = get_names(CREATURES)
        expected = 'Floradon'
        self.assertEqual(expected, names[1])

    def test_get_attr(self):  # Function 2
        creature = CREATURES[0]
        expected = 255
        self.assertEqual(expected, get_attr(creature, 'friendliness'))

    def test_get_attr_empty_string(self):  # Function 2
        creature = CREATURES[0]
        expected = 0
        self.assertEqual(expected, get_attr(creature, 'nothing'))

    def test_avg_attr(self):  # Function 3
        expected = 149.6
        self.assertEqual(expected, avg_attr(CREATURES_SUBSET, 'determination'))

    def test_avg_attr_empty_list(self):  # Function 3
        expected = 0
        empty = []
        self.assertEqual(expected, avg_attr(empty, 'determination'))

    def test_filter_legendary(self):  # Function 4
        expected = ['Lunaria', 'Moracle', 'Harvinger']
        legendary = filter_legendary(CREATURES_SUBSET)
        self.assertEqual(expected, get_names(legendary))

    def test_filter_legendary_length(self):  # Function 4
        expected = 3
        self.assertEqual(expected, len(filter_legendary(CREATURES_SUBSET)))

    def test_has_kind_True(self):  # Function 5
        expected = True
        creature = CREATURES_SUBSET[0]
        self.assertEqual(expected, has_kind(creature, 'nature'))

    def test_has_kind_False(self):  # Function 5
        expected = False
        creature = CREATURES_SUBSET[0]
        self.assertEqual(expected, has_kind(creature, 'anything'))

    def test_filter_by_kind(self):  # Function 6
        expected = ['Ripplefin', 'Shocktopus']
        filtered = filter_by_kind(CREATURES_SUBSET, 'water')
        self.assertEqual(expected, get_names(filtered))

    def test_filter_by_kind_empty(self):  # Function 6
        expected = []
        filtered = filter_by_kind(CREATURES_SUBSET, 'nothing')
        self.assertEqual(expected, get_names(filtered))

    def test_filter_out_kind(self):  # Function 7
        expected = ['Zapbadger', 'Rockorb', 'Lunaria', 'Moracle']
        filtered = filter_out_kind(CREATURES_SUBSET, 'nature')
        filtered = filter_out_kind(filtered, 'fire')
        filtered = filter_out_kind(filtered, 'water')
        self.assertEqual(expected, get_names(filtered))

    def test_filter_out_kind_nothing(self):  # Function 7
        expected = ['Dinospore', 'Emberspark', 'Ripplefin', 'Zapbadger', 'Frostfawn', 'Rockorb', 'Shocktopus',
                    'Lunaria', 'Moracle', 'Harvinger']
        nothing_filtered = filter_out_kind(CREATURES_SUBSET, 'nothing')
        self.assertEqual(expected, get_names(nothing_filtered))

    def test_percent_by_kind_dark(self):  # Function 8
        expected = 20.0
        self.assertEqual(expected, percent_by_kind(CREATURES_SUBSET, 'dark'))

    def test_percent_by_kind_nothing(self):  # Function 8
        expected = 0.0
        self.assertEqual(expected, percent_by_kind(CREATURES_SUBSET, 'random'))

    def test_filter_by_attr_lt(self):  # Function 9
        expected = ['Dinospore', 'Emberspark', 'Ripplefin']
        filtered = filter_by_attr_lt(CREATURES_SUBSET, 'determination', 100)
        self.assertEqual(expected, get_names(filtered))

    def test_filter_by_attr_lt_zero(self):  # Function 9
        expected = ['Dinospore', 'Emberspark', 'Ripplefin', 'Zapbadger', 'Frostfawn', 'Rockorb', 'Shocktopus',
                    'Lunaria', 'Moracle', 'Harvinger']
        no_filter = filter_by_attr_lt(CREATURES_SUBSET, 'nothing', 100)
        self.assertEqual(expected, get_names(no_filter))

    def test_filter_by_attr_gt(self):  # Function 10
        expected = ['Rockorb', 'Lunaria']
        filtered = filter_by_attr_gt(CREATURES_SUBSET, 'willpower', 200)
        self.assertEqual(expected, get_names(filtered))

    def test_filter_by_attr_gt_zero(self):  # Function 10
        expected = []
        no_filter = filter_by_attr_gt(CREATURES_SUBSET, 'nothing', 200)
        self.assertEqual(expected, get_names(no_filter))
    # Insert your tests above


if __name__ == '__main__':
    unittest.main()
