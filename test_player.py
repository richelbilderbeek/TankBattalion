import unittest
from player import Player
from direction import Direction
from key import Key

# Tests the Player class
class TestPlayer(unittest.TestCase):

    def test_default_construction(self):
        player = Player()
        self.assertEqual(Direction.UP, player.get_direction())
        self.assertEqual(0, player.get_dx())
        self.assertEqual(0, player.get_dy())
        self.assertEqual(0, len(player.get_keys_pressed()))
        self.assertEqual(0, player.get_x())
        self.assertEqual(0, player.get_y())

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

    def test_turn_down(self):
        player = Player()
        player.add_key(Key.DOWN)
        self.assertEqual(Direction.UP, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.DOWN, player.get_direction())

    def test_turn_and_go_down(self):
        player = Player()
        player.add_key(Key.DOWN)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dy())
        player.respond_to_keys()
        self.assertEqual(1, player.get_dy())

    def test_turn_up(self):
        player = Player(0, 0, Direction.DOWN)
        player.add_key(Key.UP)
        self.assertEqual(Direction.DOWN, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.UP, player.get_direction())

    def test_turn_and_go_up(self):
        player = Player(0, 0, Direction.DOWN)
        player.add_key(Key.UP)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dy())
        player.respond_to_keys()
        self.assertEqual(-1, player.get_dy())

