#!/usr/bin/env python3
from direction import Direction
from key import Key

# Player logic
class Player:
    def __init__(self, x = 0, y = 0, direction = Direction.UP):
        self.direction = direction
        self.dx = 0
        self.dy = 0
        self.keys_pressed = set()
        self.x = x
        self.y = y

    # Add a key to the set of keys that are active
    def add_key(self, key):
        # Remove oppsitite key
        if (key == Key.UP and Key.DOWN in self.keys_pressed):
            self.keys_pressed.remove(Key.DOWN)

        self.keys_pressed.add(key)

    # Simple getters
    def get_direction(self):
        return self.direction

    # The horizontal speed, the delta x
    def get_dx(self):
        return self.dx

    # The vertical speed, the delta y
    def get_dy(self):
        return self.dy

    # Get the keys that are 'logically' pressed
    # For example, if the user pressed left, then right, this will return
    # right only, as pressing right also removes going left
    def get_keys_pressed(self):
        return self.keys_pressed

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Respond to the keys pressed
    # Will make the tank turn and change speed
    # The game logic will have to stop the tank from running into walls
    def respond_to_keys(self):
        if Key.UP in self.keys_pressed:
            # If not facing up, turn up
            if not self.direction == Direction.UP:
                self.direction = Direction.UP
            elif self.direction == Direction.UP:
                self.dy = -1
        if Key.RIGHT in self.keys_pressed:
            # If not facing right, turn right
            if not self.direction == Direction.RIGHT:
                self.direction = Direction.RIGHT
            elif self.direction == Direction.RIGHT:
                self.dx = 1
        if Key.DOWN in self.keys_pressed:
            # If not facing down, turn down
            if not self.direction == Direction.DOWN:
                self.direction = Direction.DOWN
            elif self.direction == Direction.DOWN:
                self.dy = 1
        if Key.LEFT in self.keys_pressed:
            # If not facing left, turn left
            if not self.direction == Direction.LEFT:
                self.direction = Direction.LEFT
            elif self.direction == Direction.LEFT:
                self.dx = -1

    # Private things
    # Player logic
    direction = Direction.UP
    dx = 0
    dy = 0
    keys_pressed = set()
    x = 0
    y = 0


