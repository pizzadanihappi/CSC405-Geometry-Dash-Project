import sys
import pygame
import pygame.locals

from cube import Cube

class Cube:
    def __init__(self, surface: pygame.Surface, x: float, y: float, size: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.size = size
        self.vy = 0 # velocity
        self.ay = 5 #acceleration

    def jump(self):
        self.vy = -10

    def update(self) -> None:
        self.vy += self.ay
                

    def display(self) -> None:

        pygame.draw.rect(self.surface, "#FFDD40", (self.x, self.y, self.size, self.size))