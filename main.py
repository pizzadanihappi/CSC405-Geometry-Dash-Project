import sys
import pygame
import pygame.locals

from cube import Cube
from spike import Spike
from blocks import Blocks
from ufo import Ufo
from ship import Ship
from portal import Portal
from level import build_level

WIDTH = 1000
HEIGHT = 600
GROUND = 500

def draw_text(screen, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, "white")
    rect = surface.get_rect(center=(x, y))
    screen.blit(surface, rect)

def main():
    attempts = 1
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    obstacles, portals, blocks = build_level(screen, GROUND)
    cube = Cube(screen, x = 150, y = GROUND - 40, size = 40, ground = GROUND)
    ufo = Ufo(screen, x = 150, y = 300, size = 40, ground = GROUND)
    ship = Ship(screen, 150, 300, 40, ground = GROUND)
    spike = Spike(screen, WIDTH, GROUND, 40, 40, speed = 5)
    portal = Portal(screen, WIDTH + 300, GROUND, mode = "ufo")

    death_time = None
    spike.update()
    cube.update()
    state = "start"
    gamemode = "cube"
    portal_cooldown = 0
    on_surface = False

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
                            cube.jump(on_surface)
                        elif gamemode == "ufo":
                            ufo.jump()
        screen.fill("#00B3FF")
        draw_text(screen, f"Attempt {attempts}", 40, 100, 50)
        pygame.draw.rect(screen, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
        if state == "start":
            draw_text(screen, "PRESS SPACE TO START", 60, WIDTH // 2, HEIGHT // 2)

        elif state == "game":
            for spike in obstacles:
                spike.update()
                spike.display(screen)
            for block in blocks:
                block.update()
                block.display()
            for portal in portals:
                portal.update()
                portal.display()
            
            if portal_cooldown > 0:
                portal_cooldown -= 1

            icon = {"cube": cube, "ufo": ufo, "ship": ship}[gamemode]
            icon.update()
            icon.display()

            for portal in portals:
                if icon.hitbox().colliderect(portal.hitbox()):
                    newmode = portal.mode

                    if newmode == "cube":
                        cube.x = icon.x
                        cube.y = icon.y
                        cube.vy = getattr(icon, "vy", 0)

                    elif newmode == "ufo":
                        ufo.x = icon.x
                        ufo.y = icon.y
                        ufo.vy = getattr(icon, "vy", 0)

                    elif newmode == "ship":
                        ship.x = icon.x
                        ship.y = icon.y
                        ship.vy = getattr(icon, "vy", 0)

                    gamemode = newmode
                    portal_cooldown = 20

            for spike in obstacles:
                if icon.hitbox().colliderect(spike.hitbox()):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    icon.dead()
            for block in blocks:
                if block.top_surface(icon.hitbox(), getattr(icon, "vy", 0)):
                    icon.y = block.rect.top - icon.size
                    icon.vy = 0 
                    on_surface = True
                    break  
                else:
                    on_surface = False
            for block in blocks:
                if block.side_hit(icon.hitbox(), getattr(icon, "vy", 0)):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    icon.dead()

        if state == "death":
            pygame.draw.rect(screen, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
            for spike in obstacles:
                spike.display(screen)
            for portal in portals:
                portal.display()

            icon = {"cube": cube, "ufo": ufo, "ship": ship}[gamemode]
            icon.display()

            if death_time is not None:
                if pygame.time.get_ticks() - death_time > 1000:
                    cube = Cube(screen, 150, GROUND - 40, 40, GROUND)
                    ufo = Ufo(screen, 150, 300, 40, GROUND)
                    ship = Ship(screen, 150, 300, 40, GROUND)

                    obstacles, portals, blocks = build_level(screen, GROUND)

                    state = "game"
                    gamemode = "cube"
                    death_time = None
                    portal_cooldown = 0
                    attempts += 1
                
        pygame.display.flip()
        fps_clock.tick(fps)
        

if __name__ == "__main__":
    main()

