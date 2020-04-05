import unittest
from player import Player

# Tests the Player class
class TestPlayer(unittest.TestCase):

    def test_upper(self):
        player = Player()
        self.assertEqual(100, player.get_x())

