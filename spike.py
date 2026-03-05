import sys
import pygame
import pygame.locals

class Spike:
    def __init__(self, surface: pygame.Surface, x: float, y: float, orientation = "up", width = 40, height = 40, speed = 6) -> None:
        self.surface = surface
        self.width = width
        self.height = height
        self.x, self.y = x, y
        self.speed = speed
        self.orientation = orientation

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._draw_triangle()
        self.mask = pygame.mask.from_surface(self.image)

    def _draw_triangle(self):
        w = self.width
        h = self.height

        if self.orientation == "up":
            points = [(0, h), (w, h), (w // 2, 0)]
        elif self.orientation == "down":
            points = [(0, 0), (w, 0), (w // 2, h)]
        elif self.orientation == "left":
            points = [(w, 0), (w, h), (0, h // 2)]
        elif self.orientation == "right":
            points = [(0, 0), (0, h), (w, h // 2)]
        else:
            points = [(0, h), (w, h), (w // 2, 0)]

        pygame.draw.polygon(self.image, "#970000", points)

    def update(self) -> None:
        self.x -= self.speed

    def display(self, surface) -> None:
        surface.blit(self.image, (self.x, self.y - self.height))