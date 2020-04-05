import unittest
from game import *
from direction import Direction
from key import Key

# Tests the Game class
class TestGame(unittest.TestCase):

    def test_default_construction(self):
        game = Game()
        self.assertEqual(0, game.get_player().get_dx())

