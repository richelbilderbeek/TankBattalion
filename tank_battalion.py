# From https://pythonprogramming.net/pygame-python-3-part-1-intro
import pygame

pygame.init()


# Do not add 'pygame.FULLSCREEN', this will change the resolution
gameDisplay = pygame.display.set_mode((256,192))
pygame.display.set_caption('Tank Battalion')

clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    print(event)

    pygame.display.update()
    clock.tick(60)
    
