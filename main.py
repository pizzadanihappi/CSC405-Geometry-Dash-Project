import sys
import pygame
import pygame.locals

from cube import Cube
from spike import Spike
from ufo import Ufo
from ship import Ship
from portal import Portal

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
    ufo = Ufo(screen, x = 150, y = 300, size =40)
    ship = Ship(screen, 150, 300, 40)
    spike = Spike(screen, WIDTH, GROUND, 40, 40, speed=5)
    portal = Portal(screen, WIDTH + 300, GROUND, mode = "ufo")

    death_time = None
    spike.update()
    cube.update()
    state = "start"
    gamemode = "cube"

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
                        if gamemode == "cube":
                            cube.jump()
                        elif gamemode == "ufo":
                            ufo.jump()
        screen.fill("#00B3FF")
        if state == "start":
            draw_text(screen, "PRESS SPACE TO START", 60, WIDTH // 2, HEIGHT // 2)

        elif state == "game":
            pygame.draw.rect(screen, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
            spike.update()
            spike.display(screen)
            portal.update()
            portal.display()
            if gamemode == "cube":
                cube.update()
                cube.display()
            elif gamemode == "ufo":
                ufo.update()
                ufo.display()

        icon = {"cube": cube, "ufo": ufo, "ship": ship}[gamemode]
        icon.update()
        icon.display()
        
        if icon.hitbox().colliderect(portal.hitbox()):
            gamemode = portal.mode

            if gamemode == "cube":
                if cube.hitbox().colliderect(spike.hitbox()):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    cube.dead()

            elif gamemode == "ufo":
                if ufo.hitbox().colliderect(spike.hitbox()):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    ufo.dead()
            elif gamemode == "ship":
                if ufo.hitbox().colliderect(spike.hitbox()):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    ship.dead()
            

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
                    gamemode = "cube"
        
        pygame.display.flip()
        fps_clock.tick(fps)
        

if __name__ == "__main__":
    main()

