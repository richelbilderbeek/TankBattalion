import unittest
from game import *
from direction import Direction
from key import Key

# Tests the Game class
class TestGame(unittest.TestCase):

    def test_default_construction(self):
        game = Game()
        self.assertEqual(0, game.get_player().get_dx())

    def test_default_construction(self):
        game = Game()
        self.assertFalse(game.get_quit())
        game.set_quit(True)
        self.assertTrue(game.get_quit())

