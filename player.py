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
        if (key == Key.RIGHT and Key.LEFT in self.keys_pressed):
            self.keys_pressed.remove(Key.LEFT)
        if (key == Key.DOWN and Key.UP in self.keys_pressed):
            self.keys_pressed.remove(Key.UP)
        if (key == Key.LEFT and Key.RIGHT in self.keys_pressed):
            self.keys_pressed.remove(Key.RIGHT)

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

    # Move to player by its speed
    # The game logic will have to stop the tank from running into walls
    def move(self):
        self.x += self.dx
        self.y += self.dy

    # Remove a key to the set of keys that are active
    def remove_key(self, key):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    # Respond to the keys pressed
    # Will make the tank turn and change speed
    # The game logic will have to stop the tank from running into walls
    def respond_to_keys(self):
        if Key.UP in self.keys_pressed:
            # Brake
            if self.direction == Direction.DOWN and self.dy == 1:
                self.stop()
            elif self.direction == Direction.RIGHT and self.dx == 1:
                self.stop()
            # Turn
            elif not self.direction == Direction.UP:
                self.direction = Direction.UP
                self.keys_pressed.remove(Key.UP)
            # Start driving
            elif self.direction == Direction.UP:
                self.dy = -1
        if Key.RIGHT in self.keys_pressed:
            # Brake
            if self.direction == Direction.LEFT and self.dx == -1:
                self.stop()
            # Turn
            elif not self.direction == Direction.RIGHT:
                self.direction = Direction.RIGHT
                self.keys_pressed.remove(Key.RIGHT)
            # Start driving
            elif self.direction == Direction.RIGHT:
                self.dx = 1
        if Key.DOWN in self.keys_pressed:
            # Brake
            if self.direction == Direction.UP and self.dy == -1:
                self.stop()
            # Turn
            elif not self.direction == Direction.DOWN:
                self.direction = Direction.DOWN
                self.keys_pressed.remove(Key.DOWN)
            # Start driving
            elif self.direction == Direction.DOWN:
                self.dy = 1
        if Key.LEFT in self.keys_pressed:
            # Brake
            if self.direction == Direction.RIGHT and self.dx == 1:
                self.stop()
            # Turn
            elif not self.direction == Direction.LEFT:
                self.direction = Direction.LEFT
                self.keys_pressed.remove(Key.LEFT)
            # Start driving
            elif self.direction == Direction.LEFT:
                self.dx = -1

    # Makes the player stop and remove all keys
    def stop(self):
        self.dx = 0
        self.dy = 0
        self.keys_pressed = set()

    # Private things
    # Player logic
    direction = Direction.UP
    dx = 0
    dy = 0
    keys_pressed = set()
    x = 0
    y = 0


def is_driving(player):
    return not player.get_dx() == 0 or not player.get_dy() == 0

def is_stopped(player):
    return player.get_dx() == 0 and player.get_dy() == 0

