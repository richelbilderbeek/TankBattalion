import unittest
from shell import *

# Tests the Shell class
class TestShell(unittest.TestCase):

    def test_default_construction(self):
        shell = Shell()
        self.assertEqual(0, shell.get_x())
        self.assertEqual(0, shell.get_y())
        self.assertEqual(Direction.UP, shell.get_direction())

    def test_move_up(self):
        shell = Shell(direction = Direction.UP)
        self.assertTrue(shell.get_y() == 0.00)
        shell.move()
        self.assertTrue(shell.get_y() < 0.01)

    def test_move_right(self):
        shell = Shell(direction = Direction.RIGHT)
        self.assertTrue(shell.get_x() == 0.00)
        shell.move()
        self.assertTrue(shell.get_x() > 0.01)

