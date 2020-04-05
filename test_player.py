# From
# https://docs.python.org/3/library/unittest.html#basic-example

import unittest
from player import *

class TestPlayer(unittest.TestCase):

    def test_upper(self):
        player = Player()
        self.assertEqual(100, player.get_x())


if __name__ == '__main__':
    unittest.main()
