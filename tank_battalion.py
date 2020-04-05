#!/usr/bin/env python3
# From https://pythonprogramming.net/pygame-python-3-part-1-intro
import pygame
from player import Player

from player import *

pygame.init()

display_width = 256
display_height = 192

black = (0,0,0)
white = (255,255,255)

game_display = pygame.display.set_mode(
    (display_width,display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Tank Battalion')
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
crashed = False

player_up_image = pygame.image.load('sprites/PlayerUp.png')
player_right_image = pygame.image.load('sprites/PlayerRight.png')
player_down_image = pygame.image.load('sprites/PlayerDown.png')
player_left_image = pygame.image.load('sprites/PlayerLeft.png')

def get_player_image(direction):
    if direction == Direction.UP:
        return player_up_image
    elif direction == Direction.RIGHT:
        return player_right_image
    elif direction == Direction.DOWN:
        return player_down_image
    else:
        return player_left_image

background_image = pygame.image.load('sprites/Background.png')
player = Player(100, 100)

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.add_key(Key.UP)
            elif event.key == pygame.K_RIGHT:
                player.add_key(Key.RIGHT)
            elif event.key == pygame.K_DOWN:
                player.add_key(Key.DOWN)
            elif event.key == pygame.K_LEFT:
                player.add_key(Key.LEFT)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.remove_key(Key.UP)
            elif event.key == pygame.K_RIGHT:
                player.remove_key(Key.RIGHT)
            elif event.key == pygame.K_DOWN:
                player.remove_key(Key.DOWN)
            elif event.key == pygame.K_LEFT:
                player.remove_key(Key.LEFT)

    player.respond_to_keys()
    player.move()
    game_display.blit(background_image, (0,0))
    game_display.blit(
        get_player_image(player.get_direction()), 
        (player.get_x(),player.get_y()))

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit()
