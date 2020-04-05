#!/usr/bin/env python3

# Player logic
class Player:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # Simple getters
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Private things
    # Player logic
    x = -1
    y = -1
    x_change = 0
    y_change = 0


