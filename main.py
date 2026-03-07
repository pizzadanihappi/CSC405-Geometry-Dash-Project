import sys
import os
import random
import pygame
import pygame.locals

from cube import Cube
from spike import Spike
from block import Block
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


def teleport_to_final_cube(obstacles, blocks, portals, distance=6000):
    for spike in obstacles:
        spike.x -= distance

    for block in blocks:
        block.rect.x -= distance

    for portal in portals:
        portal.rect.x -= distance


def reset_game(screen):
    cube = Cube(screen, x=150, y=GROUND - 40, size=40, ground=GROUND)
    ufo = Ufo(screen, x=150, y=300, size=40, ground=GROUND)
    ship = Ship(screen, 150, 300, 40, ground=GROUND)

    obstacles, portals, blocks = build_level(screen, GROUND)

    return cube, ufo, ship, obstacles, portals, blocks


def start_level_music():
    pygame.mixer.music.load(os.path.join("sounds", "level_music.mp3"))
    pygame.mixer.music.set_volume(0.30)
    pygame.mixer.music.play(-1)


def stop_level_music():
    pygame.mixer.music.stop()


def main():
    attempts = 1
    fps = 60
    fps_clock = pygame.time.Clock()

    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Geometry Dash Clone")

    game_surface = pygame.Surface((WIDTH, HEIGHT))

    jump_sound = pygame.mixer.Sound(os.path.join("sounds", "jump.wav"))
    jump_sound.set_volume(0.35)

    portal_sound = pygame.mixer.Sound(os.path.join("sounds", "portal.wav"))
    portal_sound.set_volume(0.30)

    death_sound = pygame.mixer.Sound(os.path.join("sounds", "death.wav"))
    death_sound.set_volume(0.40)

    victory_sound = pygame.mixer.Sound(os.path.join("sounds", "victory.wav"))
    victory_sound.set_volume(0.45)

    cube, ufo, ship, obstacles, portals, blocks = reset_game(game_surface)

    death_time = None
    state = "start"
    gamemode = "cube"
    portal_cooldown = 0
    on_surface = False
    victory_played = False
    music_playing = False

    shake_duration = 350    
    shake_strength = 12      

    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if state == "start":
                        state = "game"
                        if not music_playing:
                            start_level_music()
                            music_playing = True

                    elif state == "game":
                        if gamemode == "cube":
                            was_on_ground = cube.on_ground or on_surface
                            cube.jump(on_surface)
                            if was_on_ground:
                                jump_sound.play()

                        elif gamemode == "ufo":
                            ufo.jump()
                            jump_sound.play()

                if event.key == pygame.K_t and state == "game":
                    teleport_to_final_cube(obstacles, blocks, portals)

                if event.key == pygame.K_r and state == "victory":
                    cube, ufo, ship, obstacles, portals, blocks = reset_game(game_surface)
                    state = "start"
                    gamemode = "cube"
                    death_time = None
                    portal_cooldown = 0
                    on_surface = False
                    victory_played = False
                    music_playing = False
                    attempts = 1

        game_surface.fill("#00B3FF")
        draw_text(game_surface, f"Attempt {attempts}", 40, 100, 50)
        pygame.draw.rect(game_surface, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))

        if state == "start":
            draw_text(game_surface, "PRESS SPACE TO START", 60, WIDTH // 2, HEIGHT // 2)

        elif state == "game":
            for spike in obstacles:
                spike.update()
                spike.display(game_surface)

            for block in blocks:
                block.update()
                block.display()

            for portal in portals:
                portal.update()
                portal.display()

            obstacles = [spike for spike in obstacles if spike.x + spike.width > 0]
            blocks = [block for block in blocks if block.rect.right > 0]
            portals = [portal for portal in portals if portal.rect.right > 0]

            if portal_cooldown > 0:
                portal_cooldown -= 1

            icon = {"cube": cube, "ufo": ufo, "ship": ship}[gamemode]
            icon.update()
            icon.display()

            for portal in portals:
                if portal_cooldown == 0 and icon.hitbox().colliderect(portal.hitbox()):
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
                    portal_sound.play()

            for spike in obstacles:
                offset = (int(spike.x - icon.x), int((spike.y - spike.height) - icon.y))
                if icon.mask.overlap(spike.mask, offset):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    icon.dead()
                    death_sound.play()
                    stop_level_music()
                    music_playing = False
                    break

            on_surface = False
            for block in blocks:
                if block.top_surface(icon.hitbox(), getattr(icon, "vy", 0)):
                    icon.y = block.rect.top - icon.size
                    icon.vy = 0
                    on_surface = True
                    break

            for block in blocks:
                if state == "game" and block.side_hit(icon.hitbox(), getattr(icon, "vy", 0)):
                    state = "death"
                    death_time = pygame.time.get_ticks()
                    icon.dead()
                    death_sound.play()
                    stop_level_music()
                    music_playing = False
                    break

            if state == "game" and not obstacles and not blocks and not portals:
                state = "victory"
                stop_level_music()
                music_playing = False

                if not victory_played:
                    victory_sound.play()
                    victory_played = True

        elif state == "death":
            pygame.draw.rect(game_surface, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))

            for spike in obstacles:
                spike.display(game_surface)

            for block in blocks:
                block.display()

            for portal in portals:
                portal.display()

            icon = {"cube": cube, "ufo": ufo, "ship": ship}[gamemode]
            icon.display()

            if death_time is not None and pygame.time.get_ticks() - death_time > 1000:
                cube, ufo, ship, obstacles, portals, blocks = reset_game(game_surface)
                state = "game"
                gamemode = "cube"
                death_time = None
                portal_cooldown = 0
                on_surface = False
                attempts += 1
                victory_played = False

                if not music_playing:
                    start_level_music()
                    music_playing = True

        elif state == "victory":
            game_surface.fill("#00B3FF")
            pygame.draw.rect(game_surface, "#004766", (0, GROUND, WIDTH, HEIGHT - GROUND))
            draw_text(game_surface, "LEVEL COMPLETE!", 80, WIDTH // 2, HEIGHT // 2 - 30)
            draw_text(game_surface, "Press R to restart", 40, WIDTH // 2, HEIGHT // 2 + 40)

        shake_x = 0
        shake_y = 0
        if state == "death" and death_time is not None:
            elapsed = pygame.time.get_ticks() - death_time
            if elapsed < shake_duration:
                shake_x = random.randint(-shake_strength, shake_strength)
                shake_y = random.randint(-shake_strength, shake_strength)

        screen.fill("black")
        screen.blit(game_surface, (shake_x, shake_y))

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()