import unittest
from player import Player
from direction import Direction
from key import Key

# Tests the Player class
class TestPlayer(unittest.TestCase):

    def test_default_construction(self):
        player = Player()
        self.assertEqual(0, player.get_x())
        self.assertEqual(0, player.get_y())
        self.assertEqual(Direction.UP, player.get_direction())

    def test_construction(self):
        x = 123
        y = 234
        direction = Direction.DOWN
        player = Player(x, y, direction)
        self.assertEqual(x, player.get_x())
        self.assertEqual(y, player.get_y())
        self.assertEqual(direction, player.get_direction())

    def test_no_keys_pressed_at_start(self):
        player = Player()
        self.assertEqual(0, len(player.get_keys_pressed()))
        
    def test_add_key(self):
        player = Player()
        self.assertEqual(0, len(player.get_keys_pressed()))
        player.add_key(Key.DOWN)
        self.assertTrue(Key.DOWN in player.get_keys_pressed())

