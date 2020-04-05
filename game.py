#!/usr/bin/env python3
from player import *

# Game logic
class Game:

    def __init__(self, player = Player()):
        self.height = 192
        self.player = player
        self.width = 256


    def add_key(self, key):
        self.player.add_key(key)

    # Simple getters
    def get_height(self):
        return self.height

    def get_keys_pressed(self):
        return self.player.get_keys_pressed()

    def get_player(self):
        return self.player

    # Does the game want to quit?
    def get_quit(self):
        return self.quit

    def get_width(self):
        return self.width


    # Does the game want to quit?
    def set_quit(self, quit):
        self.quit = quit

    height = 192
    player = Player()
    quit = False
    width = 256

# Free functions

