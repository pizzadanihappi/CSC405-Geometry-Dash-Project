import sys
import pygame
import pygame.locals

class Ufo:
    def __init__(self, surface: pygame.Surface, x, y, size, ground) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.size = size
        self.ground = ground
        self.color = "#AE2BFF"

        self.image = pygame.image.load("icons/ufo.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)

        self.vy = 0
        self.g = 0.3
        self.jump_vel = -8

    def jump(self) -> None:
        self.vy = self.jump_vel
    
    def update(self) -> None:
        
        self.vy += self.g
        self.y += self.vy

        if self.y < 0:
            self.y = 0
            self.vy = 0
        elif self.y + self.size > 600:
            self.y = 600 - self.size
            self.vy = 0
        if self.y + self.size >= self.ground:
            self.y = self.ground - self.size
            self.vy = 0

    def display(self):
        self.surface.blit(self.image, (int(self.x), int(self.y)))

    def dead(self) -> None:
        self.color = "#3C3E32"

    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)