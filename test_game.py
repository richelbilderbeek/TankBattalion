import unittest
from game import *
from direction import Direction
from key import Key

# Tests the Game class
class TestGame(unittest.TestCase):

    def test_default_construction(self):
        game = Game()
        self.assertEqual(game.get_player().get_direction(), Direction.UP)
        player = Player()
        self.assertEqual(0, game.get_player().get_dx())
        self.assertEqual(0, len(game.get_keys_pressed()))
        self.assertEqual(game.get_player(), Player())

    def test_default_construction(self):
        game = Game()
        self.assertFalse(game.get_quit())
        game.set_quit(True)
        self.assertTrue(game.get_quit())

    def test_add_key(self):
        game = Game()
        self.assertEqual(0, len(game.get_keys_pressed()))
        game.add_key(Key.DOWN)
        self.assertEqual(1, len(game.get_keys_pressed()))

    def test_shoot_adds_a_shell(self):
        game = Game()
        self.assertEqual(game.get_player().get_direction(), Direction.UP)
        self.assertEqual(False, game.get_player().is_shooting())
        game.add_key(Key.SHOOT)
        self.assertEqual(False, game.get_player().is_shooting())
        game.tick()
        self.assertEqual(True, game.get_player().is_shooting())

    def test_stay_in_screen_when_driving_up(self):
        game = Game()
        #self.assertEqual(game.get_player().get_direction(), Direction.UP)
        #game.add_key(Key.UP)
        #game.tick()
        #self.assertEqual(game.get_player().get_dy(), -1.0)
        #self.assertTrue(is_driving_up(game.get_player()))
        #self.assertTrue(game.get_player().get_y() >= 0.0)
        #for lp in range(game.get_height()):
        #    game.tick()
        #self.assertTrue(game.get_player().get_y() >= 0.0)

