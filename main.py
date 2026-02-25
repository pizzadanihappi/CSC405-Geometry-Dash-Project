import sys
import pygame
import pygame.locals

from cube import Cube
from spike import Spike

WIDTH = 1000
HEIGHT = 600
GROUND = 500

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, "white")
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    cube = Cube(screen, x = 150, y = GROUND - 40, size = 40, ground = GROUND)
    spike = Spike(screen, WIDTH, GROUND, 40, 40, speed=5)

    death_time = None
    spike.update()
    cube.update()
    state = "start"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if state == "start":
                        state = "game"
                    elif state == "game":
                        cube.jump()
        screen.fill("#00B3FF")
        if state == "start":
            draw_text(screen, "PRESS SPACE TO START", 60, WIDTH // 2, HEIGHT // 2)

        elif state == "game":
            pygame.draw.rect(screen, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
            spike.update()
            spike.display(screen)
            cube.update()
            cube.display()

            if cube.hitbox().colliderect(spike.hitbox()):
                state = "death"
                death_time = pygame.time.get_ticks()
                cube.dead()

        if state == "death":
            pygame.draw.rect(screen, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
            cube.display()
            spike.display(screen)

            if death_time is not None:
                if pygame.time.get_ticks() - death_time > 1000:
                    cube = Cube(screen, 150, GROUND - 40, 40, GROUND)
                    spike = Spike(screen, WIDTH, GROUND, 40, 40, speed=5)
                    state = "game"
                    death_time = None
        
        pygame.display.flip()
        fps_clock.tick(fps)

        

if __name__ == "__main__":
    main()

