import sys
import pygame
import pygame.locals

from spike import Spike
from portal import Portal

def build_level(surface, ground, width=1000):
    obstacles = []
    portals = []

    # CUBE
    obstacles.append(Spike(surface, width + 300, ground, 40, 40, speed=5))
    obstacles.append(Spike(surface, width + 600, ground, 40, 40, speed=5))
    
    # UFO
    portals.append(Portal(surface, width + 900, ground, mode="ufo", width=30, height=120, speed=5))
    

    obstacles.append(Spike(surface, width + 1200, ground - 50, 40, 40, speed=5))
    obstacles.append(Spike(surface, width + 1500, ground - 100, 40, 40, speed=5))
    
    # SHIP
    portals.append(Portal(surface, width + 1800, ground, mode="ship", width=30, height=120, speed=5))
    
    obstacles.append(Spike(surface, width + 2100, ground - 150, 40, 40, speed=5))
    obstacles.append(Spike(surface, width + 2400, ground - 200, 40, 40, speed=5))
    
    # CUBE
    portals.append(Portal(surface, width + 2700, ground, mode="cube", width=30, height=120, speed=5))
    
    return obstacles, portals