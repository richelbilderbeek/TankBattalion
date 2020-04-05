import unittest
from player import Player

# Tests the Player class
class TestPlayer(unittest.TestCase):

    def test_at_origin(self):
        player = Player()
        self.assertEqual(0, player.get_x())
        self.assertEqual(0, player.get_y())

    def test_at_coordinat(self):
        x = 123
        y = 234
        player = Player(x, y)
        self.assertEqual(x, player.get_x())
        self.assertEqual(y, player.get_y())

