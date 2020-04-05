#!/usr/bin/env python3
from direction import Direction

# Player logic
class Player:
    def __init__(self, x = 0, y = 0, direction = Direction.UP):
        self.x = x
        self.y = y
        self.direction = direction

    # Simple getters
    def get_direction(self):
        return self.direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Private things
    # Player logic
    x = None
    y = None
    direction = None
    x_change = 0
    y_change = 0


