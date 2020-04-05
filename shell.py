#!/usr/bin/env python3
from direction import Direction
import math

# Shell logic
class Shell:
    def __init__(self, x = 0, y = 0, direction = Direction.UP):
        self.direction = direction
        self.x = x
        self.y = y

    # Simple getters
    def get_direction(self):
        return self.direction

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Move to shell by its speed
    # The game logic will have to stop the shell from running into walls
    def move(self):
        if self.direction == Direction.UP:
          self.y -= 1.0
        elif self.direction == Direction.RIGHT:
          self.x += 1.0
        elif self.direction == Direction.DOWN:
          self.y += 1.0
        else:
          self.x -= 1.0


    # Private things
    # Shell logic
    direction = Direction.UP
    x = 0
    y = 0


# Free functions
def add_key(player: Shell, key):
    player.add_key(key)

def get_keys_pressed(player: Shell):
    return player.get_keys_pressed()

def is_driving(player):
    return not math.isclose(player.get_dx(), 0.0) or not math.isclose(player.get_dy(), 0.0)

def is_driving_up(player):
    return math.isclose(player.get_dy(), -1.0) and math.isclose(player.get_dx(), 0.0)

def is_driving_right(player):
    return math.isclose(player.get_dx(), 1.0) and math.isclose(player.get_dy(), 0.0)

def is_driving_down(player):
    return math.isclose(player.get_dy(), 1.0) and math.isclose(player.get_dx(), 0.0)

def is_driving_left(player):
    return math.isclose(player.get_dx(), -1.0) and math.isclose(player.get_dy(), 0.0)

def is_stopped(player):
    return math.isclose(player.get_dx(), 0.0) and math.isclose(player.get_dy(), 0.0)

