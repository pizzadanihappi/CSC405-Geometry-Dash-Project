import pygame
from spike import Spike
from block import Block
from portal import Portal


def build_level(surface, ground, width=1000):
    obstacles = []
    blocks = []
    portals = []

    x = width + 100

    obstacles.append(Spike(surface, x, ground, "up"))
    x += 350

    obstacles.append(Spike(surface, x, ground, "up"))
    obstacles.append(Spike(surface, x + 45, ground, "up"))
    x += 450

    obstacles.append(Spike(surface, x, ground, "up"))
    obstacles.append(Spike(surface, x + 45, ground, "up"))
    obstacles.append(Spike(surface, x + 90, ground, "up"))
    x += 450

    obstacles.append(Spike(surface, x, ground - 50, "up"))
    blocks.append(Block(surface, x, ground - 50, 40, 50))
    x += 410

    blocks.append(Block(surface, x, ground - 50, 290, 50))

    x += 250

    obstacles.append(Spike(surface, x, ground - 50, "up"))

    x += 350

    portals.append(Portal(surface, x, ground, mode = "ufo"))
    blocks.append(Block(surface, x, ground - 600, 40, 470))
    x += 350

    for i in range(24):
        obstacles.append(Spike(surface, x + (40 * i), ground, "up"))

    x += 320

    obstacles.append(Spike(surface, x, ground - 150, "up"))
    blocks.append(Block(surface, x, ground - 150, 40, 150))
    x += 200

    obstacles.append(Spike(surface, x, ground - 250, "up"))
    blocks.append(Block(surface, x, ground - 250, 40, 250))
    obstacles.append(Spike(surface, x, ground - 400, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 160))

    x += 200

    obstacles.append(Spike(surface, x, ground - 200, "up"))
    blocks.append(Block(surface, x, ground - 200, 40, 200))
    obstacles.append(Spike(surface, x, ground - 380, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 180))
    x += 250

    for i in range(10):
        obstacles.append(Spike(surface, x, ground - 400, "up"))
        blocks.append(Block(surface, x, ground - 400, 40, 400))
        x += 40

    blocks.append(Block(surface, x, ground - 400, 100, 400))

    x += 410

    for i in range(15):
        obstacles.append(Spike(surface, x, (ground - 200 - (40 * i)), "left"))
    
    obstacles.append(Spike(surface, x, (ground), "left"))

    x += 40

    portals.append(Portal(surface, x, ground - 40, mode = "ship"))
    blocks.append(Block(surface, x, ground - 600, 40, 430))
    blocks.append(Block(surface, x, ground - 40, 40, 40))

    x += 250

    obstacles.append(Spike(surface, x, ground - 50, "up"))
    blocks.append(Block(surface, x, ground - 50, 40, 50))
    obstacles.append(Spike(surface, x, ground - 300, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 260))
    x += 180

    obstacles.append(Spike(surface, x, ground - 120, "up"))
    blocks.append(Block(surface, x, ground - 120, 40, 120))
    obstacles.append(Spike(surface, x, ground - 250, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 310))
    x += 200

    obstacles.append(Spike(surface, x, ground - 80, "up"))
    blocks.append(Block(surface, x, ground - 80, 40, 80))
    obstacles.append(Spike(surface, x, ground - 320, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 240))
    x += 300

    blocks.append(Block(surface, x, ground - 300, 40, 300))
    x += 40
    blocks.append(Block(surface, x, ground - 300, 400, 40))
    x += 50
    obstacles.append(Spike(surface, x, ground - 360, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 200))
    x += 150
    obstacles.append(Spike(surface, x, ground - 460, "down"))
    obstacles.append(Spike(surface, x, ground - 300, "up"))
    x += 200
    obstacles.append(Spike(surface, x, ground - 260, "right"))

    x += 40

    for i in range(8):
        obstacles.append(Spike(surface, x, ground, "up"))
        x += 40
    x += 10

    for i in range(35):
        obstacles.append(Spike(surface, x, (ground - 130 - (40 * i)), "left"))
    x += 40

    portals.append(Portal(surface, x, ground, mode = "cube"))
    blocks.append(Block(surface, x, ground - 600, 40, 470))
    x += 250

    obstacles.append(Spike(surface, x, ground, "up"))
    obstacles.append(Spike(surface, x + 40, ground, "up"))
    x += 150

    obstacles.append(Spike(surface, x, ground - 100, "down"))
    blocks.append(Block(surface, x, ground - 600, 40, 460))

    x += 150

    obstacles.append(Spike(surface, x, ground, "up"))

    x += 300

    blocks.append(Block(surface, x, ground - 80, 40, 80))
    x += 40
    blocks.append(Block(surface, x, ground - 80, 400, 40))


    return obstacles, portals, blocks