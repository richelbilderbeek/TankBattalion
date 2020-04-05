#!/usr/bin/env python3
# From https://pythonprogramming.net/pygame-python-3-part-1-intro
import pygame

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
player_image = pygame.image.load('sprites/PlayerUp.png')
background_image = pygame.image.load('sprites/Background.png')

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
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    x += x_change
    y += y_change
    game_display.blit(background_image, (0,0))
    game_display.blit(player_image, (x,y))

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit()
