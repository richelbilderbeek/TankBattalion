#!/usr/bin/env python3
from direction import Direction
from key import Key

# Player logic
class Player:
    def __init__(self, x = 0, y = 0, direction = Direction.UP):
        self.direction = direction
        self.keys_pressed = set()
        self.x = x
        self.y = y

    # Add a key to the set of keys that are active
    def add_key(self, key):
        self.keys_pressed.add(key)

    # Simple getters
    def get_direction(self):
        return self.direction

    # Get the keys that are 'logically' pressed
    # For example, if the user pressed left, then right, this will return
    # right only, as pressing right also removes going left
    def get_keys_pressed(self):
        return self.keys_pressed

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Private things
    # Player logic
    direction = Direction.UP
    keys_pressed = set()
    x = 0
    y = 0
    x_change = 0
    y_change = 0


