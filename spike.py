import sys
import pygame
import pygame.locals

class Spike:
    def __init__(self, surface: pygame.Surface, x: float, y: float, width = 40, height = 40, speed = 5) -> None:
        self.surface = surface
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

    def update(self) -> None:
        self.x -= self.speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y - self.height, self.width, self.height)

    def display(self, surface) -> None:
        pygame.draw.polygon(surface, (255, 0, 0), [
            (self.x, self.y),
            (self.x + self.width // 2, self.y - self.height),
            (self.x + self.width, self.y)
        ])