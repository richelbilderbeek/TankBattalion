#!/usr/bin/env python3
from player import *

# Game logic
class Game:

    def __init__(self, player = Player(100, 100)):
        self.height = 192
        self.player = player
        self.width = 256

    def add_key(self, key):
        self.player.add_key(key)

    def get_height(self):
        return self.height

    def get_keys_pressed(self):
        return self.player.get_keys_pressed()

    # Minimum valid X coordinat
    def get_minx(self):
        return self.minx

    # Minimum valid Y coordinat
    def get_miny(self):
        return self.miny

    def get_player(self):
        return self.player

    # Does the game want to quit?
    def get_quit(self):
        return self.quit

    def get_width(self):
        return self.width

    def remove_key(self, key):
        self.player.remove_key(key)

    # Does the game want to quit?
    def set_quit(self, quit):
        self.quit = quit

    # Process all events of the game
    def tick(self):
        self.player.respond_to_keys()

        if self.player.get_x() + self.player.get_dx() < self.minx:
            self.player.stop()
        if self.player.get_y() + self.player.get_dy() < self.miny:
            self.player.stop()
        if self.player.get_x() + self.player.get_dx() > self.maxx:
            self.player.stop()
        if self.player.get_y() + self.player.get_dy() > self.maxy:
            self.player.stop()

        self.player.move()


    height = 192
    player = Player()
    maxx = 169 # Maximum valid X coordinat
    maxy = 169 # Maximum valid Y coordinat
    minx = 14 # Minimum valid X coordinat
    miny = 7 # Minimum valid Y coordinat
    quit = False
    width = 256

# Free functions

