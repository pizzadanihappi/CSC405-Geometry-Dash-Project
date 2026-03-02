import sys
import pygame
import pygame.locals

class Blocks:
    def __init__(self, surface: pygame.Surface, x: float, y: float, width: float, height: float, speed = 5):
        self.surface = surface
        self.width = width
        self.height = height
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        self.rect.x -= self.speed

    def display(self):
        pygame.draw.rect(self.surface, "#5C5B68", self.hitbox())

    def hitbox(self):
        return pygame.Rect(self.rect)

    def side_hit(self, icon_rect, vy):
        if (icon_rect.bottom <= self.rect.top) or (icon_rect.top >= self.rect.bottom):
            return False
        if (icon_rect.right > self.rect.left) and (icon_rect.left < self.rect.left):
            return True
        if (icon_rect.left < self.rect.right) and (icon_rect.right > self.rect.right):
            return True
        return False
    
    def top_surface(self, icon_rect, vy):
        if vy <= 0:
            return False
        if (icon_rect.right <= self.rect.left) or (icon_rect.left >= self.rect.right):
            return False
        if (icon_rect.bottom <= self.rect.top + 10) and (icon_rect.bottom + vy >= self.rect.top):
            return True