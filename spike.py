import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


spike_width = 40
spike_height = 40
spike_x = WIDTH          
spike_y = HEIGHT - 100   
spike_speed = 5

running = True
while running:
    clock.tick(60) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    spike_x -= spike_speed

    if spike_x < -spike_width:
        spike_x = WIDTH


    screen.fill((30, 30, 30))


    pygame.draw.polygon(screen, (255, 0, 0), [
        (spike_x, spike_y),
        (spike_x + spike_width // 2, spike_y - spike_height),
        (spike_x + spike_width, spike_y)
    ])

    pygame.display.flip()

pygame.quit()
sys.exit()