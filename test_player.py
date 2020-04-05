import unittest
from player import *
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
        self.assertEqual(0, len(get_keys_pressed(player)))
        self.assertEqual(0, player.get_x())
        self.assertEqual(0, player.get_y())
        self.assertEqual(False, player.is_shooting())
        self.assertFalse(is_driving(player))
        self.assertTrue(is_stopped(player))

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
        self.assertEqual(1, len(player.get_keys_pressed()))
        add_key(player, Key.RIGHT) # Free function
        self.assertEqual(2, len(get_keys_pressed(player)))
        
    def test_add_orthogonal_key(self):
        player = Player()
        self.assertEqual(0, len(player.get_keys_pressed()))
        player.add_key(Key.DOWN)
        self.assertTrue(Key.DOWN in player.get_keys_pressed())

    def test_add_opposite_key_up_removes_down(self):
        player = Player()
        player.add_key(Key.DOWN)
        self.assertTrue(Key.DOWN in player.get_keys_pressed())
        player.add_key(Key.UP)
        self.assertFalse(Key.DOWN in player.get_keys_pressed())

    def test_add_opposite_key_right_removes_left(self):
        player = Player()
        player.add_key(Key.LEFT)
        self.assertTrue(Key.LEFT in player.get_keys_pressed())
        player.add_key(Key.RIGHT)
        self.assertFalse(Key.LEFT in player.get_keys_pressed())

    def test_add_opposite_key_down_removes_up(self):
        player = Player()
        player.add_key(Key.UP)
        self.assertTrue(Key.UP in player.get_keys_pressed())
        player.add_key(Key.DOWN)
        self.assertFalse(Key.UP in player.get_keys_pressed())

    def test_add_opposite_key_left_removes_right(self):
        player = Player()
        player.add_key(Key.RIGHT)
        self.assertTrue(Key.RIGHT in player.get_keys_pressed())
        player.add_key(Key.LEFT)
        self.assertFalse(Key.RIGHT in player.get_keys_pressed())

    def test_add_second_key(self):
        player = Player()
        player.add_key(Key.DOWN)
        player.add_key(Key.LEFT)
        self.assertTrue(Key.DOWN in player.get_keys_pressed())
        self.assertTrue(Key.LEFT in player.get_keys_pressed())

    def test_remove_key(self):
        player = Player()
        player.add_key(Key.DOWN)
        self.assertEqual(1, len(player.get_keys_pressed()))
        player.remove_key(Key.DOWN)
        self.assertEqual(0, len(player.get_keys_pressed()))

    def test_remove_absent_key_is_ignored(self):
        player = Player()
        player.remove_key(Key.DOWN)

    def test_turn_up(self):
        player = Player(direction = Direction.DOWN)
        player.add_key(Key.UP)
        self.assertEqual(Direction.DOWN, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.UP, player.get_direction())

    # If pressing up makes the player turn, 
    # the user must press up again to actually go up
    def test_turn_up_loses_key(self):
        player = Player(direction = Direction.DOWN)
        player.add_key(Key.UP)
        self.assertEqual(1, len(player.get_keys_pressed()))
        player.respond_to_keys()
        self.assertEqual(Direction.UP, player.get_direction())
        self.assertEqual(0, len(player.get_keys_pressed()))

    def test_turn_right(self):
        player = Player(direction = Direction.LEFT)
        player.add_key(Key.RIGHT)
        self.assertEqual(Direction.LEFT, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.RIGHT, player.get_direction())

    def test_turn_down(self):
        player = Player()
        player.add_key(Key.DOWN)
        self.assertEqual(Direction.UP, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.DOWN, player.get_direction())

    def test_turn_left(self):
        player = Player(direction = Direction.RIGHT)
        player.add_key(Key.LEFT)
        self.assertEqual(Direction.RIGHT, player.get_direction())
        player.respond_to_keys()
        self.assertEqual(Direction.LEFT, player.get_direction())

    def test_turn_and_go_up(self):
        player = Player(direction = Direction.DOWN)
        player.add_key(Key.UP)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dy())
        player.add_key(Key.UP)
        player.respond_to_keys()
        self.assertEqual(-1, player.get_dy())
        self.assertTrue(is_driving(player))
        self.assertFalse(is_stopped(player))
        self.assertTrue(is_driving_up(player))
        self.assertFalse(is_driving_right(player))
        self.assertFalse(is_driving_down(player))
        self.assertFalse(is_driving_left(player))

    def test_turn_and_go_right(self):
        player = Player()
        player.add_key(Key.RIGHT)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dx())
        player.add_key(Key.RIGHT)
        player.respond_to_keys()
        self.assertEqual(1, player.get_dx())
        self.assertTrue(is_driving(player))
        self.assertFalse(is_driving_up(player))
        self.assertTrue(is_driving_right(player))
        self.assertFalse(is_driving_down(player))
        self.assertFalse(is_driving_left(player))

    def test_turn_and_go_down(self):
        player = Player()
        player.add_key(Key.DOWN)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dy())
        player.add_key(Key.DOWN)
        player.respond_to_keys()
        self.assertEqual(1, player.get_dy())
        self.assertFalse(is_driving_up(player))
        self.assertFalse(is_driving_right(player))
        self.assertTrue(is_driving_down(player))
        self.assertFalse(is_driving_left(player))

    def test_turn_and_go_left(self):
        player = Player()
        player.add_key(Key.LEFT)
        player.respond_to_keys() # Only turn
        self.assertEqual(0, player.get_dx())
        player.add_key(Key.LEFT)
        player.respond_to_keys()
        self.assertEqual(-1, player.get_dx())
        self.assertFalse(is_driving_up(player))
        self.assertFalse(is_driving_right(player))
        self.assertFalse(is_driving_down(player))
        self.assertTrue(is_driving_left(player))

    def test_move_left(self):
        player = Player(direction = Direction.LEFT)
        player.add_key(Key.LEFT)
        player.respond_to_keys()
        self.assertEqual(-1, player.get_dx())
        self.assertEqual(0, player.get_x())
        self.assertEqual(0, player.get_y())
        player.move()
        self.assertEqual(-1, player.get_dx())
        self.assertEqual(-1, player.get_x())
        self.assertEqual(0, player.get_y())

    # If pressing up makes the player turn while driving down
    # the user must stop and not change direction yet
    def test_turn_around_when_going_down_brakes(self):
        player = Player(direction = Direction.DOWN)
        player.add_key(Key.DOWN)
        player.respond_to_keys()
        # Look down and drive down
        self.assertEqual(Direction.DOWN, player.get_direction())
        self.assertEqual(1, player.get_dy())
        player.add_key(Key.UP)
        player.respond_to_keys()
        # Look down and stop
        self.assertEqual(Direction.DOWN, player.get_direction())
        self.assertEqual(0, player.get_dy())
        player.respond_to_keys()
        # Still look down and stop
        self.assertEqual(Direction.DOWN, player.get_direction())
        self.assertEqual(0, player.get_dy())

    # If pressing right makes the player turn while driving left
    # the user must stop and not change direction yet
    def test_turn_around_when_going_left_brakes(self):
        player = Player(direction = Direction.LEFT)
        player.add_key(Key.LEFT)
        player.respond_to_keys()
        # Look left and drive left
        self.assertEqual(Direction.LEFT, player.get_direction())
        self.assertEqual(-1, player.get_dx())
        player.add_key(Key.RIGHT)
        player.respond_to_keys()
        # Look left and stop
        self.assertEqual(Direction.LEFT, player.get_direction())
        self.assertEqual(0, player.get_dx())
        player.respond_to_keys()
        # Still look left and stop
        self.assertEqual(Direction.LEFT, player.get_direction())
        self.assertEqual(0, player.get_dx())

    # If pressing down makes the player turn while driving up
    # the user must stop and not change direction yet
    def test_turn_around_when_going_up_brakes(self):
        player = Player(direction = Direction.UP)
        player.add_key(Key.UP)
        player.respond_to_keys()
        # Look up and drive up
        self.assertEqual(Direction.UP, player.get_direction())
        self.assertEqual(-1, player.get_dy())
        player.add_key(Key.DOWN)
        player.respond_to_keys()
        # Look up and stop
        self.assertEqual(Direction.UP, player.get_direction())
        self.assertEqual(0, player.get_dy())
        player.respond_to_keys()
        # Still look up and stop
        self.assertEqual(Direction.DOWN, player.get_direction())
        self.assertEqual(0, player.get_dy())

    # If pressing left makes the player turn while driving right
    # the user must stop and not change direction yet
    def test_turn_around_when_going_up_brakes(self):
        player = Player(direction = Direction.RIGHT)
        player.add_key(Key.RIGHT)
        player.respond_to_keys()
        # Look right and drive right
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(1, player.get_dx())
        player.add_key(Key.LEFT)
        player.respond_to_keys()
        # Look right and stop
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(0, player.get_dx())
        player.respond_to_keys()
        # Still look right and stop
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(0, player.get_dx())

    # If pressing up makes the player turn while driving right
    # the user must stop and not change direction yet
    def test_turn_around_when_going_down_brakes(self):
        player = Player(direction = Direction.RIGHT)
        player.add_key(Key.RIGHT)
        player.respond_to_keys()
        # Drive right and drive right
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(1, player.get_dx())
        player.add_key(Key.UP)
        player.respond_to_keys()
        # Look right and stop
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(0, player.get_dx())
        player.respond_to_keys()
        # Still look right and stop
        self.assertEqual(Direction.RIGHT, player.get_direction())
        self.assertEqual(0, player.get_dx())

