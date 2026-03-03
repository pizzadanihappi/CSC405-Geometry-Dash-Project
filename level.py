import pygame
from spike import Spike
from portal import Portal


def build_level(surface, ground, width=1000):
    obstacles = []
    portals = []

    spacing = 250
    x = width + 200

    obstacles.append(Spike(surface, x, ground, 40, 40))
    x += spacing

    obstacles.append(Spike(surface, x, ground, 40, 40))
    obstacles.append(Spike(surface, x + 45, ground, 40, 40))
    x += spacing

    obstacles.append(Spike(surface, x, ground, 40, 40))
    obstacles.append(Spike(surface, x + 45, ground, 40, 40))
    obstacles.append(Spike(surface, x + 90, ground, 40, 40))
    x += spacing + 100

    obstacles.append(Spike(surface, x, ground - 100, 40, 40))
    x += spacing


    portals.append(Portal(surface, x, ground, mode="ufo"))
    x += spacing

    obstacles.append(Spike(surface, x, ground - 150, 40, 40))
    x += 200

    obstacles.append(Spike(surface, x, ground - 250, 40, 40))
    x += 200

    obstacles.append(Spike(surface, x, ground - 100, 40, 40))
    x += 300

    portals.append(Portal(surface, x, ground, mode="ship"))
    x += spacing

    obstacles.append(Spike(surface, x, ground - 50, 40, 40))
    obstacles.append(Spike(surface, x, ground - 300, 40, 40))
    x += 180

    obstacles.append(Spike(surface, x, ground - 120, 40, 40))
    obstacles.append(Spike(surface, x, ground - 250, 40, 40))
    x += 200

    obstacles.append(Spike(surface, x, ground - 80, 40, 40))
    obstacles.append(Spike(surface, x, ground - 320, 40, 40))
    x += 300

    portals.append(Portal(surface, x, ground, mode="cube"))
    x += spacing


    obstacles.append(Spike(surface, x, ground, 40, 40))
    obstacles.append(Spike(surface, x + 45, ground, 40, 40))
    x += 200

    obstacles.append(Spike(surface, x, ground - 100, 40, 40))
    x += 200

    obstacles.append(Spike(surface, x, ground, 40, 40))

    return obstacles, portals