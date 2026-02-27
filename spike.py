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
        margin_x = self.width * 0.15
        margin_top = self.height * 0.20 
        margin_bottom = self.height * 0.05 

        return pygame.Rect(self.x + margin_x,
            self.y - self.height + margin_top,
            self.width - 2 * margin_x,
            self.height - margin_top - margin_bottom
        )

    def display(self, surface) -> None:
        pygame.draw.polygon(surface, (255, 0, 0), [
            (self.x, self.y),
            (self.x + self.width // 2, self.y - self.height),
            (self.x + self.width, self.y)
        ])