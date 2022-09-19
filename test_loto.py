import unittest

from lotto_features import Kegs, Card, Person, separator


def test_separator():
    assert separator('.') == '........................................'


class TestKegs(unittest.TestCase):

    def setUp(self):
        self.barrels = Kegs()

    def test_init(self):
        self.assertEqual(len(self.barrels.kegs), 90)
        self.assertNotIn(91, self.barrels.kegs)
        self.assertNotIn(0, self.barrels.kegs)

    def test_kegs_minus(self):
        self.barrels.kegs_minus(50)
        self.assertEqual(len(self.barrels.kegs), 89)
        self.assertNotIn(50, self.barrels.kegs)


class TestCard(unittest.TestCase):
    def setUp(self):
        self.new_player = Card()

    def test_init(self):
        self.assertEqual(self.new_player.once, 0)
        self.assertEqual(len(self.new_player.card), 15)
        self.assertIsInstance(self.new_player.card, list)

    def test_card_out(self):
        self.new_player.card = [2, 6, 59, 90, 4, 55, 7, 89, 12, 77, 11, 5, 8, 9, 3]
        self.new_player.card_out(77)
        self.assertIn('-', self.new_player.card)
        self.assertNotIn(77, self.new_player.card)
        self.assertEqual(self.new_player.once, 1)


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.players = Person()

    def test_init(self):
        self.assertEqual(self.players.person, {})
        self.assertIsInstance(self.players.person, dict)

    def test_add_player(self):
        self.players.add_player('игрок')
        self.assertIn('игрок', self.players.person)
        self.assertEqual(len(self.players.person), 1)
        self.assertEqual(self.players.text, 'Игрок успешно создан!')

