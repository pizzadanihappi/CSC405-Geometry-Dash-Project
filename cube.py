import sys
import pygame
import pygame.locals


class Cube:
    def __init__(self, surface: pygame.Surface, x: float, y: float, size: float, ground: float) -> None:
        self.surface = surface
        self.x, self.y = x, y
        self.size = size
        self.ground = ground
        self.color = "#FFDD40"
        self.alive = True

        self.vy = 0 # velocity
        self.g = 0.3 #gravity
        self.jump_vel = -9

        if self.y + self.size >= self.ground:
            self.y = self.ground - self.size
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self) -> None:
        if self.on_ground:
            self.vy = self.jump_vel
            self.on_ground = False

    def update(self) -> None:
        if not self.alive:
            return
        
        self.vy += self.g
        self.y += self.vy

        if self.y + self.size >= self.ground:
            self.y = self.ground - self.size
            self.vy = 0
            self.on_ground = True
    
    def hitbox(self):
        return pygame.Rect(self.x, self.y, self.size, self.size)
    
    def dead(self) -> None:
        self.color = "#3C3E32"
                
    def display(self) -> None:
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.size, self.size))