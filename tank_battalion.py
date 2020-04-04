# From https://pythonprogramming.net/pygame-python-3-part-1-intro
import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

game_display = pygame.display.set_mode(
    (display_width,display_height))
pygame.display.set_caption('Tank Battalion')

clock = pygame.time.Clock()
crashed = False
player_image = pygame.image.load('sprites/PlayerUp.png')

def draw_player(x,y):
    game_display.blit(player_image, (x,y))

x = (display_width  * 0.45)
y = (display_height * 0.80)
x_change = 0
car_speed = 0

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change
    game_display.fill(white)
    draw_player(x,y)

    pygame.display.update()
    clock.tick(60)
    

pygame.quit()
quit()
