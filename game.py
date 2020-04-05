#!/usr/bin/env python3
from player import *

# Game logic
class Game:

    def __init__(self, player = Player()):
        self.height = 192
        self.width = 256
        self.player = player

    # Simple getters
    def get_height(self):
        return self.height

    def get_player(self):
        return self.player

    def get_width(self):
        return self.width

    height = 192
    player = Player()
    width = 256

